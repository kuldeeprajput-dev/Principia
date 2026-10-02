"""Versioned raw-information contracts; prediction scoring never executes an extractor."""
from pathlib import Path
import copy,json,tempfile,subprocess,sys,os
import pandas as pd
import numpy as np
from common import ROOT,context,load_json,save_json,safe_path,digest,verify_assets,table,new_output,evaluator_identity,asset_record,VERSION
import submissions

def contract(identifier):
 index=load_json(ROOT/'contracts/RAW_ACCESS_REGISTRY.json')
 rows=[v for v in index['contracts'] if v['contract_id']==identifier]
 if len(rows)!=1:raise ValueError('Unknown raw-access contract')
 entry=rows[0];p=safe_path(ROOT,entry['path'])
 if digest(p)!=entry['sha256']:raise ValueError('Raw contract integrity mismatch')
 c=load_json(p);t,package,x,y,refs=context(c['parent_task_id'])
 if digest(package/'task.json')!=c['parent_task_sha256'] or t['observations_sha256']!=c['observations_sha256']:raise ValueError('Raw parent contract drift')
 return c,t,package,x,y,refs

def validate(identifier,folder):
 c,t,package,x,y,refs=contract(identifier);folder=Path(folder)
 lineage=load_json(safe_path(folder,'feature_lineage.json'))
 if lineage.get('schema_version')!='principia.feature-lineage/1.0':raise ValueError('Unknown feature-lineage schema')
 if lineage.get('contract_id')!=identifier or lineage.get('contract_sha256')!=digest(ROOT/f'contracts/raw_access/{identifier}.json'):raise ValueError('Raw contract binding mismatch')
 if lineage.get('current_outcomes_exposed') is not True:raise ValueError('Declare exposed outcomes')
 assets=lineage.get('assets',[])
 if not assets:raise ValueError('Feature table, extractor and training inventory must be hashed')
 verify_assets(folder,assets);names={v['path']for v in assets}
 for k in ['features_file','extractor_file','training_inventory']:
  if lineage.get(k) not in names:raise ValueError('Unbound lineage '+k)
 if not lineage['extractor_file'].endswith('.py'):raise ValueError('Extractor must be a declared Python source asset')
 featurefile=safe_path(folder,lineage['features_file']);d=table(featurefile)
 if 'sample_id' not in d or not d.sample_id.is_unique or set(d.sample_id)!=set(x.sample_id):raise ValueError('Derived feature inventory mismatch')
 d=d.set_index('sample_id').loc[x.sample_id].reset_index();features=lineage.get('features',[]);cols=[f['name']for f in features]
 if not cols or len(cols)!=len(set(cols)) or set(d)!=set(cols+['sample_id']):raise ValueError('Derived feature declarations mismatch')
 if {'target','group','partition','fold','sample_id'} & set(cols):raise ValueError('Reserved metadata cannot become derived predictors')
 native={a['sha256']for a in c['source_assets']+c.get('supplemental_assets',[])}
 quantities=set(c['information_budget']['measured_quantities_and_default_features'])
 if c['case_id']=='P100-035':quantities|={'raw_pcm','species'}
 for f in features:
  if not f.get('units')or not f.get('expression')or not f.get('selectors'):raise ValueError('Features need units, expression and source selectors')
  if not np.isfinite(pd.to_numeric(d[f['name']],errors='raise')).all():raise ValueError('Nonfinite derived feature')
  for s in f['selectors']:
   if s.get('asset_sha256') not in native:raise ValueError('Undeclared native asset')
   if not s.get('locator')or s.get('quantity')not in quantities:raise ValueError('Selector lacks native locator or approved quantity')
   if s.get('role')not in ['predictor','declared_calibration','declared_history']:raise ValueError('Forbidden source role')
   if s.get('availability') not in ['at_or_before_prediction','static_known_context']:raise ValueError('Future or unavailable observation')
   if s.get('window_end') is not None:
    if s.get('prediction_time') is None:raise ValueError('Window requires a prediction-time bound')
    if not np.isfinite([s['window_end'],s['prediction_time']]).all()or s['window_end']>s['prediction_time']:raise ValueError('Future window exceeds prediction time')
  if f.get('calibration_used') and not t.get('calibration'):raise ValueError('Undeclared calibration')
 training=load_json(safe_path(folder,lineage['training_inventory']))
 for k in ['training_group_ids','tuning_group_ids']:
  if not isinstance(training.get(k),list)or any(not isinstance(v,str)for v in training[k]):raise ValueError('Invalid training group inventory')
 overlap=set(training['training_group_ids']+training['tuning_group_ids'])&set(t['evaluation_groups'])
 if overlap and training.get('evaluation_data_usage')=='never_used_for_fitting_or_tuning':raise ValueError('Feature training groups contradict independence claim')
 virtual=copy.deepcopy(t);virtual.update(task_id=identifier,protocol_version=c['protocol_version'],permitted_inputs=cols,input_units={f['name']:f['units']for f in features},input_sha256=digest(featurefile))
 d.insert(1,'group',x.group.to_numpy())
 if 'fold'in x:d['fold']=x.fold.to_numpy()
 s,p,audit=submissions.validate(folder,virtual,d)
 if s['training']['training_group_ids']!=training['training_group_ids']or s['training']['tuning_group_ids']!=training['tuning_group_ids']:raise ValueError('Predictor and extractor training inventories disagree')
 audit.update(raw_information_compliance='declared_not_independently_verified',feature_lineage_sha256=digest(folder/'feature_lineage.json'),raw_contract_sha256=digest(ROOT/f'contracts/raw_access/{identifier}.json'),parent_task_id=t['task_id'],raw_extractor_execution='not_run',warning='Hashed selectors and declared windows are not proof that an arbitrary extractor obeys them. Bound review is required for audited scientific claims.')
 return (virtual,package,d,y,refs),x,(s,p,audit),c

def score(identifier,folder,output,trusted=False):
 identity=evaluator_identity();ctx,diagnostics,validated,c=validate(identifier,folder)
 from benchmark import evaluate
 return evaluate(c['parent_task_id'],folder,output,trusted=trusted,_context=ctx,_validated=validated,_diagnostic_inputs=diagnostics,_route={'mode':'raw_access','contract_id':identifier,'parent_task_id':c['parent_task_id'],'contract_sha256':validated[2]['raw_contract_sha256'],'feature_lineage_sha256':validated[2]['feature_lineage_sha256']})

def replay_features(identifier,folder,data_root,output,trust=False):
 identity=evaluator_identity()
 if not trust:raise ValueError('Raw extractor replay requires --trust-code; this is not a sandbox')
 ctx,_,(_,_,audit),c=validate(identifier,folder);folder=Path(folder);lineage=load_json(folder/'feature_lineage.json')
 if lineage.get('extractor_interface')!='native-v1':raise ValueError('Native replay requires extractor_interface=native-v1; prepared-view demonstrations do not certify native extraction')
 source=Path(data_root)/c['source_folder'];verify_assets(source,c['source_assets'])
 out=new_output(output)
 with tempfile.TemporaryDirectory(prefix='p100-raw-replay-')as tmp:
  tmp=Path(tmp);save_json(tmp/'contract.json',c);ctx[2][['sample_id','group']].to_csv(tmp/'cohort.csv',index=False)
  method=tmp/'method';method.mkdir()
  for a in lineage['assets']:
   dest=method/a['path'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(safe_path(folder,a['path']).read_bytes())
  env={k:os.environ[k]for k in ['PATH','LANG','LC_ALL','TMPDIR','SYSTEMROOT']if k in os.environ};env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1')
  p=subprocess.run([sys.executable,'-B',str(method/lineage['extractor_file']),'--data-root',str(Path(data_root).resolve()),'--contract',str(tmp/'contract.json'),'--cohort',str(tmp/'cohort.csv'),'--output',str(tmp/'features.csv')],cwd=method,env=env,capture_output=True,text=True,timeout=300)
  if p.returncode:raise ValueError('Trusted native extractor failed: '+p.stderr[-1500:])
  actual=table(safe_path(tmp,'features.csv'));expected=table(folder/lineage['features_file'])
  if not actual.sample_id.is_unique or set(actual.sample_id)!=set(expected.sample_id):raise ValueError('Replayed native identities differ')
  actual=actual.set_index('sample_id').loc[expected.sample_id].reset_index()
  pd.testing.assert_frame_equal(actual,expected,check_dtype=False,rtol=1e-10,atol=0)
 result={'status':'native_feature_replay_passed','contract_id':identifier,'evaluator_identity':identity,**audit,'raw_extractor_execution':'explicitly_trusted_local','feature_replay_is_information_independence_proof':False,'source_assets_verified':len(c['source_assets'])}
 out.mkdir(parents=True);save_json(out/'native_feature_replay.json',result);return result

def example(identifier,output):
 c,t,p,x,y,refs=contract(identifier)
 # Example is an executable alternative transformation of one permitted scalar,
 # deliberately not advertised as scientific improvement or a raw extraction audit.
 names=[k for k in t['permitted_inputs'] if k in x and pd.api.types.is_numeric_dtype(x[k]) and np.isfinite(x[k]).all()]
 if not names:raise ValueError('This task needs a domain-specific raw example; numeric generic example unavailable')
 name=names[0];out=new_output(output);out.mkdir(parents=True);feature='alternative_transform'
 pd.DataFrame({'sample_id':x.sample_id,feature:np.arcsinh(x[name])}).to_csv(out/'derived_features.csv',index=False)
 (out/'extract.py').write_text('# Example transformation only: receives source-verified allowed input view.\nimport argparse,numpy as np,pandas as pd\np=argparse.ArgumentParser();p.add_argument("--inputs",required=True);p.add_argument("--output",required=True);a=p.parse_args();x=pd.read_csv(a.inputs,dtype={"sample_id":str});pd.DataFrame({"sample_id":x.sample_id,"alternative_transform":np.arcsinh(x['+repr(name)+'])}).to_csv(a.output,index=False)\n')
 (out/'predict.py').write_text('import argparse,pandas as pd\np=argparse.ArgumentParser();p.add_argument("--inputs",required=True);p.add_argument("--output",required=True);a=p.parse_args();x=pd.read_csv(a.inputs,dtype={"sample_id":str});pd.DataFrame({"sample_id":x.sample_id,"prediction":0.5,"status":"predict","reason":""}).to_csv(a.output,index=False)\n')
 training={'training_group_ids':[],'tuning_group_ids':[],'evaluation_data_usage':'no_fitting_constant_demonstration'};save_json(out/'training.json',training)
 pd.DataFrame({'sample_id':x.sample_id,'prediction':.5,'status':'predict','reason':''}).to_csv(out/'predictions.csv',index=False)
 lineage={'schema_version':'principia.feature-lineage/1.0','contract_id':identifier,'contract_sha256':digest(ROOT/f'contracts/raw_access/{identifier}.json'),'current_outcomes_exposed':True,'features_file':'derived_features.csv','extractor_file':'extract.py','training_inventory':'training.json','features':[{'name':feature,'units':'dimensionless','expression':f'asinh({name} / one declared input unit)','calibration_used':False,'selectors':[{'asset_sha256':c['source_assets'][0]['sha256'],'locator':'DEMONSTRATION ONLY: replace with exact native member/column/window before scientific review','quantity':name,'role':'predictor','availability':'at_or_before_prediction'}]}],'assets':[asset_record(out/a,out)for a in ['derived_features.csv','extract.py','training.json']],'demonstration_only':True}
 save_json(out/'feature_lineage.json',lineage)
 s={'schema_version':'principia.submission/3.0','case_id':t['case_id'],'task_id':identifier,'protocol_version':c['protocol_version'],'cohort_id':t['cohort_id'],'input_sha256':digest(out/'derived_features.csv'),'target_units':t['target_units'],'evaluator_version':VERSION,'decision':'predict','permitted_inputs':[feature],'predictions_file':'predictions.csv','training':training,'equations':[{'id':'E1','expression':'y_hat=0.5 (interface demonstration only)'}],'findings':[{'id':'F1','statement':'Interface demonstration; no scientific finding','equation_ids':['E1']}],'uncertainty':{'interval_level':None},'reproducibility':{'entrypoint':'predict.py','assets':[asset_record(out/'predict.py',out)]}}
 save_json(out/'submission.json',s);return {'status':'demonstration_created','contract_id':identifier,'scientific_admission':False}
