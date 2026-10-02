"""Maintainer-controlled task admission. Local trusted adapter execution is explicit."""
from pathlib import Path
import json,copy,re,subprocess,sys,os,tempfile,shutil
import numpy as np
import pandas as pd
from common import ROOT,registry,load_json,save_json,safe_path,verify_assets,digest,new_output,table,validate_schema,evaluator_identity,asset_record
import metrics

def candidate(package,allow_registered=False):
 package=Path(package);m=load_json(safe_path(package,'MANIFEST.json'))
 if not m.get('files'):raise ValueError('Empty candidate manifest')
 verify_assets(package,m['files']);required={'task.json','adapter.json','run.py','rules.json'}
 actual={p.relative_to(package).as_posix()for p in package.rglob('*')if p.is_file()and p.name!='MANIFEST.json'and '__pycache__'not in p.parts}
 if actual!={a['path']for a in m['files']}:raise ValueError('Candidate contains unmanifested or missing files')
 if not required.issubset({a['path']for a in m['files']}):raise ValueError('Incomplete standalone candidate')
 t=load_json(safe_path(package,'task.json'));validate_schema(t,'task.schema.json')
 if not re.fullmatch(r'P100-\d{3}\.[A-Za-z0-9_.-]+',t['task_id']):raise ValueError('Unsafe task ID')
 if t['case_id']not in {c['case_id']for c in registry()['cases']}:raise ValueError('Unknown case')
 if not t['task_id'].startswith(t['case_id']+'.')or int(t['case_id'][-3:])!=t['case_number']:raise ValueError('Task/case identity mismatch')
 if not allow_registered and t['task_id']in {v['task_id']for v in registry()['tasks']}:raise ValueError('Cannot overwrite a registered task')
 bound={a['path']for a in m['files']}
 if not set(t['data'].values()).issubset(bound)or 'evidence/metrics.csv'not in bound:raise ValueError('Unbound candidate tables')
 if t['exposure'].get('current')!='exposed':raise ValueError('New tasks on this corpus remain exposed')
 x,y,refs=[table(safe_path(package,t['data'][k]))for k in ['inputs','observations','reference_predictions']]
 for d in [x,y,refs]:
  if not d.sample_id.is_unique or not d[['sample_id','group']].equals(x[['sample_id','group']]):raise ValueError('Candidate identities/groups mismatch')
 if x.group.isna().any()or len(x)!=t['assigned_rows']or sorted(x.group.unique().tolist())!=t['evaluation_groups']:raise ValueError('Candidate cohort contract mismatch')
 for key,field in [('inputs','input_sha256'),('observations','observations_sha256')]:
  if digest(package/t['data'][key])!=t[field]:raise ValueError('Candidate data binding mismatch')
 if np.isinf(y.target.to_numpy(float)).any():raise ValueError('Infinite target')
 valid=np.isfinite(y.target.to_numpy(float))
 if not valid.any():raise ValueError('Use adequacy route when no eligible target exists')
 if int(valid.sum())!=t['eligible_rows']:raise ValueError('Candidate eligible-target denominator mismatch')
 if not set(t['permitted_inputs']).issubset(x):raise ValueError('Missing declared predictors')
 expected=table(safe_path(package,'evidence/metrics.csv')).set_index('model')
 for model in t['baseline_models']:
  p=refs.loc[valid,model].to_numpy(float)
  if not np.isfinite(p).all():raise ValueError('Nonfinite comparator')
  score,_=metrics.score(y.loc[valid],p,t)
  if not np.isclose(score['primary_error'],float(expected.loc[model,'primary_error']),rtol=1e-9,atol=1e-10):raise ValueError('Comparator metric parity failure')
 return t,x,y,refs

def validate_adapter(package,data_root,output,trust=False,allow_registered=False):
 identity=evaluator_identity();package=Path(package);t,x,y,refs=candidate(package,allow_registered)
 if not trust:raise ValueError('Adapter execution requires --trust-code; no untrusted-code sandbox is provided')
 a=load_json(package/'adapter.json');m=load_json(package/'MANIFEST.json');names={z['path']for z in m['files']}
 if a.get('entrypoint')not in names or not a['entrypoint'].endswith('.py'):raise ValueError('Unbound adapter entrypoint')
 if not a.get('source_assets'):raise ValueError('Native source inventory required')
 verify_assets(data_root,a['source_assets']);out=new_output(output);out.mkdir(parents=True)
 with tempfile.TemporaryDirectory(prefix='p100-adapter-review-')as tmp:
  tmp=Path(tmp);prepared=tmp/'prepared'
  env={k:os.environ[k]for k in ['PATH','LANG','LC_ALL','TMPDIR','SYSTEMROOT']if k in os.environ};env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1')
  p=subprocess.run([sys.executable,'-B',str(safe_path(package,a['entrypoint'])),'--data-root',str(Path(data_root).resolve()),'--output',str(prepared)],cwd=package,env=env,capture_output=True,text=True,timeout=300)
  if p.returncode:raise ValueError('Trusted adapter failed: '+p.stderr[-1500:])
  for name,expected in [('inputs',x),('observations',y)]:
   actual=table(safe_path(prepared,'data/'+name+'.csv.gz'))
   pd.testing.assert_frame_equal(actual,expected,check_dtype=False,rtol=1e-12,atol=0)
  import submissions
  for i,model in enumerate(t['baseline_models']):
   example=tmp/f'reference-{i}';submissions.example(t,package,x,refs,example,model)
   s,pred,_=submissions.validate(example,t,x);submissions.replay(example,s,pred,t,x,300)
 report={'schema_version':'principia.adapter-validation/1.0','status':'pass','task_id':t['task_id'],'package_manifest_sha256':digest(package/'MANIFEST.json'),'source_inventory_sha256':digest(package/'adapter.json'),'evaluator_identity':identity,'checks':['manifest','source_hashes','exact_identities_groups','native_predictors_targets_reconstruction','comparator_metric_parity','all_frozen_predictors_replayed'],'execution':'explicitly_trusted_local','training_independence_verified':False}
 save_json(out/'validation.json',report);return report

def admit(proposal,package,validation,review_paths,decision,output):
 proposal=Path(proposal);package=Path(package);p=load_json(safe_path(proposal,'proposal.json'));t,*_=candidate(package)
 import workflow
 with tempfile.TemporaryDirectory()as tmp:workflow.propose(proposal,Path(tmp)/'intake')
 if p['proposed_task_id']!=t['task_id']or p['case_id']!=t['case_id']:raise ValueError('Proposal/candidate identity mismatch')
 if p['target']!=t['target']or p['target_units']!=t['target_units']or set(p['permitted_inputs'])!=set(t['permitted_inputs']):raise ValueError('Proposal/candidate endpoint or budget mismatch')
 v=load_json(validation);d=load_json(decision)
 bindings={'proposal_sha256':digest(proposal/'proposal.json'),'package_manifest_sha256':digest(package/'MANIFEST.json'),'validation_sha256':digest(validation)}
 if v.get('status')!='pass'or v.get('package_manifest_sha256')!=bindings['package_manifest_sha256']or v.get('task_id')!=t['task_id']or v.get('source_inventory_sha256')!=digest(package/'adapter.json')or v.get('execution')!='explicitly_trusted_local':raise ValueError('Missing bound adapter validation')
 if 'all_frozen_predictors_replayed'not in v.get('checks',[]):raise ValueError('Frozen executable reference validation required')
 if d.get('bindings')!=bindings or not d.get('maintainer_id')or not d.get('rationale'):raise ValueError('Maintainer decision needs exact bindings and rationale')
 if d.get('decision')not in ['accept','reject']:raise ValueError('Unknown admission decision')
 roles={};required={'measurement_semantics','information_budget','grouping','controls','source_rights','scientific_nontriviality'}
 for path in review_paths:
  r=load_json(path)
  if r.get('bindings')!=bindings or r.get('role')not in ['computational','scientific_critical']or r['role']in roles or not r.get('reviewer_id'):raise ValueError('Invalid bound contract review')
  if not required.issubset(r.get('checks',{}))or any(not r['checks'][k].get('rationale')for k in required):raise ValueError('Incomplete contract review')
  roles[r['role']]=r
 if len(roles)!=2 or len({r['reviewer_id']for r in roles.values()})!=2:raise ValueError('Two distinct review roles required')
 if d['decision']=='accept':
  if d['maintainer_id']in {r['reviewer_id']for r in roles.values()}:raise ValueError('Maintainer acceptance needs a separate decision identity')
  if any(r.get('recommendation')!='accept'or any(r['checks'][k].get('status')!='supported'for k in required)for r in roles.values()):raise ValueError('Acceptance blocked by unresolved contract review')
 out=new_output(output);out.mkdir(parents=True)
 # Self-contained immutable admission bundle, no reliance on an absolute source path.
 for name,path in [('validation.json',validation),('decision.json',decision)]:shutil.copyfile(path,out/name)
 shutil.copytree(proposal,out/'proposal');shutil.copytree(package,out/'package')
 for i,path in enumerate(review_paths):shutil.copyfile(path,out/f'review-{i}.json')
 receipt={'schema_version':'principia.task-admission/1.0','task_id':t['task_id'],'case_id':t['case_id'],'decision':d['decision'],'maintainer_id':d['maintainer_id'],'bindings':bindings,'review_sha256':[digest(p)for p in review_paths],'registered':False,'rationale':d['rationale'],'source_rights':d.get('source_rights','Bound reviewers assessed supplied terms; no blanket relicensing'), 'files':[asset_record(f,out)for f in sorted(out.rglob('*'))if f.is_file()]}
 save_json(out/'admission.json',receipt);return receipt

def register(bundle,maintainer,output,root=None):
 root=Path(root)if root is not None else ROOT;bundle=Path(bundle);a=load_json(safe_path(bundle,'admission.json'));verify_assets(bundle,a['files'])
 if a['decision']!='accept'or a['maintainer_id']!=maintainer:raise ValueError('Registration requires the accepting maintainer identity')
 reg=load_json(root/'registry.json');t=load_json(bundle/'package/task.json')
 candidate(bundle/'package')
 if any(v['task_id']==t['task_id']for v in reg['tasks']):raise ValueError('Task already registered')
 if t['task_id']!=a['task_id']or digest(bundle/'package/MANIFEST.json')!=a['bindings']['package_manifest_sha256']:raise ValueError('Admission package drift')
 # Existing frozen package bytes are copied, never rewritten; registry path is external.
 destination=root/'tasks'/t['task_id']
 if destination.exists():raise ValueError('Destination exists')
 receipt_out=new_output(output);shutil.copytree(bundle/'package',destination)
 entry=copy.deepcopy(t);entry['package']=str(destination.relative_to(root));entry['manifest_sha256']=digest(destination/'MANIFEST.json');entry['admission_sha256']=digest(bundle/'admission.json');entry['preparation_mode']='explicitly_trusted_external_adapter';reg['tasks'].append(entry)
 case=next(c for c in reg['cases']if c['case_id']==t['case_id']);case['task_ids'].append(t['task_id'])
 temp=root/'registry.pending.json';save_json(temp,reg);temp.replace(root/'registry.json')
 receipt_out.mkdir(parents=True);result={'registered':True,'task_id':t['task_id'],'admission_sha256':entry['admission_sha256'],'default_task_changed':False,'catalog_and_release_refresh_required':True,'publication_performed':False};save_json(receipt_out/'registration.json',result);return result
