"""Submission validation and explicitly trusted local replay."""
from pathlib import Path
import json, os, shutil, subprocess, sys, tempfile
import numpy as np
import pandas as pd
from common import ROOT, VERSION, COMPATIBLE_SUBMISSION_VERSIONS, digest, load_json, save_json, safe_path, verify_assets, table, new_output, asset_record,validate_schema

def read_predictions(path,ids,task,level):
 d=table(path,strings=True)
 # Compatibility with the older round2 CSV interface.
 legacy='status'not in d
 if legacy:
  if not {'sample_id','group','prediction'}.issubset(d)or set(d)-{'sample_id','group','prediction','abstention_reason'}:raise ValueError('Invalid legacy prediction columns')
  d['status']=np.where(d.prediction.str.strip().eq(''),'abstain','predict');d['reason']=d.get('abstention_reason','')
  d=d.drop(columns=['group','abstention_reason'],errors='ignore')
 required={'sample_id','prediction','status','reason'}
 if not required.issubset(d)or set(d)-required-{'lower','upper'}:raise ValueError('Prediction columns must be sample_id,prediction,status,reason and optional lower,upper')
 if not d.sample_id.is_unique or d.sample_id.str.strip().eq('').any():raise ValueError('Duplicate or empty prediction ID')
 if set(d.sample_id)!=set(ids):raise ValueError('Prediction inventory mismatch; use explicit abstentions for every unpredicted ID')
 d=d.set_index('sample_id').loc[list(ids)].reset_index()
 if not set(d.status).issubset({'predict','abstain'}):raise ValueError('Unknown prediction status')
 mask=d.status.eq('predict')
 if d.loc[~mask,'reason'].str.strip().eq('').any():raise ValueError('Every abstention needs a reason')
 for col in['prediction']+[k for k in['lower','upper']if k in d]:
  if d.loc[~mask,col].str.strip().ne('').any():raise ValueError('Abstained numeric fields must be blank')
  d[col]=pd.to_numeric(d[col].replace('',np.nan),errors='raise')
  if not np.isfinite(d.loc[mask,col]).all():raise ValueError('Nonfinite submitted values')
 if task.get('positive_prediction')and(d.loc[mask,'prediction']<=0).any():raise ValueError('Task requires positive predictions')
 if task.get('nonnegative_prediction')and(d.loc[mask,'prediction']<0).any():raise ValueError('Task requires nonnegative predictions')
 if ('lower'in d)!=('upper'in d)or('lower'in d)!=(level is not None):raise ValueError('Provide both interval bounds and nominal level together')
 if level is not None:
  if not isinstance(level,(int,float))or not np.isfinite(level)or not 0<level<1:raise ValueError('Invalid interval level')
  if((d.loc[mask,'lower']>d.loc[mask,'prediction'])|(d.loc[mask,'prediction']>d.loc[mask,'upper'])).any():raise ValueError('Intervals must contain point predictions')
 return d,legacy

def validate(folder,task,x):
 folder=Path(folder);s=load_json(safe_path(folder,'submission.json'));version=s.get('schema_version')
 if version=='principia.submission/3.0':
  validate_schema(s,'submission.schema.json')
  for key in['case_id','task_id','protocol_version','cohort_id','input_sha256','target_units']:
   if s.get(key)!=task[key]:raise ValueError('Submission/task mismatch: '+key)
  if s.get('evaluator_version')not in COMPATIBLE_SUBMISSION_VERSIONS:raise ValueError('Evaluator version mismatch')
 else:
  if version not in ['1.0']:raise ValueError('Unsupported submission schema version')
  # Historical metadata uses protocol_id and may have a supplemental case suffix.
  if s.get('case_id')not in[task['case_id'],task.get('legacy_case_id',task['case_id'])]:raise ValueError('Legacy case mismatch')
  for key,value in [('protocol_id',task['protocol_version']),('input_sha256',task['input_sha256']),('target_units',task['target_units'])]:
   if s.get(key)!=value:raise ValueError('Legacy task mismatch: '+key)
 if not isinstance(s.get('permitted_inputs'),list)or len(s['permitted_inputs'])!=len(set(s['permitted_inputs']))or not set(s['permitted_inputs']).issubset(task['permitted_inputs']):raise ValueError('Forbidden or duplicate declared predictor')
 training=s.get('training')
 if not isinstance(training,dict):raise ValueError('Training and exposure declaration required')
 for k in['training_group_ids','tuning_group_ids']:
  if not isinstance(training.get(k),list)or any(not isinstance(v,str)for v in training[k]):raise ValueError('Declare string group inventories: '+k)
 overlap=set(training['training_group_ids']+training['tuning_group_ids'])&set(task['evaluation_groups'])
 if overlap and training.get('evaluation_data_usage')=='never_used_for_fitting_or_tuning':raise ValueError('Training groups contradict separation claim')
 if not training.get('evaluation_data_usage'):raise ValueError('Evaluation exposure declaration required')
 equations=s.get('equations',[]);findings=s.get('findings',[])
 for items,label in[(equations,'equation'),(findings,'finding')]:
  ids=[v.get('id')for v in items]
  if any(not isinstance(v,str)or not v for v in ids)or len(ids)!=len(set(ids)):raise ValueError('Invalid or duplicate '+label+' ID')
 for f in findings:
  if not set(f.get('equation_ids',[])).issubset({v['id']for v in equations}):raise ValueError('Unknown equation referenced by finding')
 reproducibility=s.get('reproducibility',{});assets=reproducibility.get('assets',[])
 if not isinstance(assets,list):raise ValueError('Reproducibility assets must be a list')
 verify_assets(folder,assets)
 names=[a['path']for a in assets];entry=reproducibility.get('entrypoint')
 if entry is not None and(entry not in names or not entry.endswith('.py')):raise ValueError('Entrypoint must be a hashed Python asset')
 prediction_path=safe_path(folder,s['predictions_file'])
 if any(n in['submission.json',s['predictions_file']]for n in names):raise ValueError('Model assets cannot replace metadata or predictions')
 if 'predictions_sha256'in s and digest(prediction_path)!=s['predictions_sha256']:raise ValueError('Prediction hash mismatch')
 level=s.get('uncertainty',{}).get('interval_level');d,legacy=read_predictions(prediction_path,x.sample_id,task,level)
 if legacy:
  old=table(prediction_path,strings=True).set_index('sample_id').loc[x.sample_id]
  if not np.array_equal(old.group.to_numpy(),x.group.to_numpy()):raise ValueError('Legacy group mismatch')
 active=d.status.eq('predict')
 if s.get('decision')not in['predict','abstain']:raise ValueError('Decision must be predict or abstain')
 if s['decision']=='abstain'and(active.any()or not s.get('abstention_reason','').strip()):raise ValueError('Whole-task abstention must explain and cover every row')
 import_audit={}
 if s.get('submission_kind')=='historical_prediction_import':
  from import_legacy import validate_import_binding
  import_audit=validate_import_binding(folder,s,task,x)
 elif s.get('submission_kind','scientific_submission')!='scientific_submission':raise ValueError('Unknown submission kind')
 if s['decision']=='predict'and(not active.any()or(not import_audit and(not equations or not findings))):raise ValueError('Predictive submission needs predictions, equation/program description and a finding')
 audit='prediction_only'
 training_assets=training.get('inventory_assets',[])
 if training_assets:
  verify_assets(folder,training_assets);audit='declared_training_inventory_bound'
 if reproducibility.get('fit_entrypoint'):
  f=reproducibility['fit_entrypoint']
  if f not in names:raise ValueError('Fit recipe must be a hashed asset')
  audit='fit_recipe_and_inventory_supplied'if training_assets else'fit_recipe_without_complete_inventory'
 return s,d,{'compatibility_import':version!='principia.submission/3.0'or bool(import_audit),'training_overlap_groups':sorted(overlap),'training_auditability':audit,'training_independence_verified_by_scoring':False,**import_audit}

def replay(folder,s,d,task,x,timeout):
 if s['decision']=='abstain':return{'status':'not_applicable','reason':'Whole-task abstention'}
 entry=s['reproducibility'].get('entrypoint')
 if entry is None:raise ValueError('No executable entrypoint supplied')
 with tempfile.TemporaryDirectory(prefix='principia-trusted-replay-')as tmp:
  tmp=Path(tmp);method=tmp/'method';method.mkdir()
  for a in s['reproducibility']['assets']:
   dest=method/a['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(safe_path(folder,a['path']),dest)
  columns=['sample_id','group']+s['permitted_inputs']
  if task['family']=='round2'and'fold'in x:columns+=['fold']
  staged=x[list(dict.fromkeys(columns))];staged.to_csv(tmp/'inputs.csv.gz',index=False,compression={'method':'gzip','mtime':0})
  env={k:os.environ[k]for k in['PATH','LANG','LC_ALL','SYSTEMROOT','TMPDIR']if k in os.environ}
  env.update(OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
  result=subprocess.run([sys.executable,'-B',str(method/entry),'--inputs',str(tmp/'inputs.csv.gz'),'--output',str(tmp/'predictions.csv')],cwd=method,env=env,capture_output=True,text=True,timeout=timeout)
  if result.returncode:raise ValueError('Trusted replay failed: '+result.stderr[-2500:])
  actual,_=read_predictions(tmp/'predictions.csv',x.sample_id,task,s.get('uncertainty',{}).get('interval_level'))
  if not actual.status.equals(d.status):raise ValueError('Replayed abstention mask mismatch')
  mask=d.status.eq('predict');maximum=0.
  for col in['prediction']+[k for k in['lower','upper']if k in d]:
   a=actual.loc[mask,col].to_numpy(float);b=d.loc[mask,col].to_numpy(float)
   if not np.allclose(a,b,rtol=1e-9,atol=1e-8):raise ValueError('Replayed '+col+' mismatch')
   maximum=max(maximum,float(np.max(abs(a-b),initial=0)))
 return{'status':'passed','maximum_absolute_difference':maximum,'security_sandbox':False,'execution_mode':'explicitly_trusted_local','environment_secrets_inherited':False}

def example(task,package,x,refs,out,model=None):
 out=new_output(out);model=model or task['reference_model']
 if model not in task['baseline_models']:raise ValueError('Unknown model')
 out.mkdir(parents=True)
 if task['family']=='round2':
  index=load_json(package/'rules.json')
  state=load_json(package/index['models'][model]['state_file'])
  required=load_json(package/'runtime_manifest.json')['files']
  for item in required:
   src=safe_path(package,item['path']);dest=out/item['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
  shutil.copyfile(package/'runtime_manifest.json',out/'runtime_manifest.json')
 else:state=load_json(package/'rules.json')['models'][model]
 save_json(out/'submission_model.json',state)
 for p in package.rglob('*.py'):
  if 'evaluator'in p.relative_to(package).parts:continue
  rel=p.relative_to(package);dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 # run.py is imported only by explicit trusted replay. Its CLI remains standalone.
 (out/'predict.py').write_text('''import argparse,json
from pathlib import Path
import pandas as pd
from run import predict, read_table
p=argparse.ArgumentParser();p.add_argument('--inputs',required=True);p.add_argument('--output',required=True);a=p.parse_args()
x=read_table(a.inputs);model=json.loads((Path(__file__).parent/'submission_model.json').read_text())
y=predict(model,x);z=pd.DataFrame({'sample_id':x.sample_id,'prediction':y,'status':'predict','reason':''});z.to_csv(a.output,index=False)
''')
 pred=pd.DataFrame({'sample_id':x.sample_id,'prediction':refs[model],'status':'predict','reason':''});pred.to_csv(out/'predictions.csv',index=False)
 assets=[asset_record(p,out)for p in sorted(out.rglob('*'))if p.is_file()and p.name not in['predictions.csv','submission.json']]
 metadata={
 'schema_version':'principia.submission/3.0',**{k:task[k]for k in['case_id','task_id','protocol_version','cohort_id','input_sha256','target_units']},
 'evaluator_version':VERSION,'decision':'predict','abstention_reason':'','permitted_inputs':task['permitted_inputs'],
 'predictions_file':'predictions.csv','predictions_sha256':digest(out/'predictions.csv'),
 'training':{'training_group_ids':[],'tuning_group_ids':[],'evaluation_data_usage':'frozen_reference_with_disclosed_historical_exposure','inventory_assets':[],'note':'Runnable reference example. Historical source protocols document training; empty lists are not a claim of verified training independence. Replace declarations for your own method.'},
 'equations':[{'id':'E1','expression':task['models'].get(model,{}).get('equation','Complete executable equation/program in hashed model/runtime artifacts'),'coefficients_asset':'submission_model.json','variables_and_units':task.get('input_units',{})}],
 'findings':[{'id':'F1','equation_ids':['E1'],'classification':'reproduction','statement':'Reproduce the frozen '+model+' numerical reference; no new discovery or fresh confirmation is claimed.'}],
 'uncertainty':{'interval_level':None,'method':'Not supplied'},'reproducibility':{'entrypoint':'predict.py','assets':assets},
 }
 save_json(out/'submission.json',metadata)
 return metadata
