"""Reusable deterministic evaluator fixture; no model fitting or native data mutation."""
from pathlib import Path
import sys,uuid,json,copy,shutil
import numpy as np,pandas as pd
R=Path(__file__).resolve().parents[2]
import argparse,tempfile
_parser=argparse.ArgumentParser(description=__doc__);_parser.add_argument('--output',type=Path);_args=_parser.parse_args()
WORK=_args.output if _args.output is not None else Path(tempfile.mkdtemp(prefix='principia-evaluator-test-'))
WORK.mkdir(parents=True,exist_ok=True)
W=WORK/('legacy-import-'+uuid.uuid4().hex[:8]);W.mkdir();sys.path.insert(0,str(R/'evaluation'))
import common,import_legacy,submissions,benchmark
checks=[]
def test(name,fn,reject=False):
 try:r=fn()
 except (ValueError,TypeError,KeyError)as e:checks.append({'check':name,'status':'pass'if reject else'fail','detail':str(e).replace(str(W),'<temporary-fixture>').replace(str(R),'<benchmark-root>')});return
 checks.append({'check':name,'status':'fail'if reject else'pass','detail':'unexpected acceptance'if reject else (r.get('status','passed')if isinstance(r,dict)else str(r))})
tid='P100-024.round2.v1';task,package,x,y,refs=common.context(tid);legacy=x[['sample_id','group','fold']].copy();legacy['prediction']=refs[task['reference_model']];legacy['target']=y.target
source=W/'legacy.csv';legacy.to_csv(source,index=False)
test('import_complete_native_csv',lambda:import_legacy.import_predictions(tid,source,W/'valid'))
s,d,a=submissions.validate(W/'valid',task,x)
assert s['equations']==[]and s['findings']==[]and s['permitted_inputs']==[]and s['reproducibility']['entrypoint']is None
assert a['information_access_verified']is False and a['comparability']=='numerical_only_unverified_information_access'
test('import_scores_without_executing_code',lambda:benchmark.evaluate(tid,W/'valid',W/'score')['scores']['candidate']['primary_error'])
test('import_replay_rejected_without_model',lambda:submissions.replay(W/'valid',s,d,task,x,10),True)
def mutate_csv(name,fn):
 q=legacy.copy();fn(q);p=W/(name+'.csv');q.to_csv(p,index=False);return import_legacy.import_predictions(tid,p,W/name)
test('wrong_task_family_rejected',lambda:import_legacy.import_predictions('P100-024.original.v1',source,W/'wrong-family'),True)
test('source_group_mismatch_rejected',lambda:mutate_csv('groups',lambda q:q.__setitem__('group','wrong')),True)
test('source_fold_mismatch_rejected',lambda:mutate_csv('folds',lambda q:q.__setitem__('fold','wrong')),True)
test('source_target_mismatch_rejected',lambda:mutate_csv('targets',lambda q:q.__setitem__('target',1e9)),True)
test('duplicate_ids_rejected',lambda:mutate_csv('ids',lambda q:q.__setitem__('sample_id','one')),True)
test('nonfinite_prediction_rejected',lambda:mutate_csv('nonfinite',lambda q:q.__setitem__('prediction',np.inf)),True)
test('unexplained_blank_prediction_rejected',lambda:mutate_csv('blank',lambda q:q.__setitem__('prediction','')),True)
test('unknown_column_rejected',lambda:mutate_csv('column',lambda q:q.__setitem__('extra',1)),True)
test('existing_output_preserved',lambda:import_legacy.import_predictions(tid,source,W/'valid'),True)
partial=legacy.copy();partial['prediction']=partial.prediction.astype(object);partial.loc[partial.index[:10],'prediction']='';partial['abstention_reason']='';partial.loc[partial.index[:10],'abstention_reason']='Outside supported domain';partial.to_csv(W/'partial.csv',index=False)
test('partial_abstention_preserved',lambda:import_legacy.import_predictions(tid,W/'partial.csv',W/'partial'))
whole=partial.copy();whole['prediction']='';whole['abstention_reason']='Insufficient information';whole.to_csv(W/'whole.csv',index=False)
test('whole_abstention_without_claims',lambda:import_legacy.import_predictions(tid,W/'whole.csv',W/'whole'))
def mutate_output(name,modify):
 out=W/name;shutil.copytree(W/'valid',out);s=common.load_json(out/'submission.json');modify(s,out);common.save_json(out/'submission.json',s);return submissions.validate(out,task,x)
test('invented_import_equation_rejected',lambda:mutate_output('equation',lambda s,o:s.update(equations=[{'id':'X','expression':'fabricated'}])),True)
test('false_input_budget_rejected',lambda:mutate_output('budget',lambda s,o:s.update(permitted_inputs=['cycle'])),True)
test('false_training_inventory_rejected',lambda:mutate_output('train',lambda s,o:s['training'].update(training_group_ids=['G'])),True)
test('unknown_import_version_rejected',lambda:mutate_output('version',lambda s,o:s['compatibility_import'].update(schema_version='future')),True)
def changed_prediction(s,o):
 q=pd.read_csv(o/'predictions.csv');q['prediction']+=1;q.to_csv(o/'predictions.csv',index=False);s['predictions_sha256']=common.digest(o/'predictions.csv')
test('native_prediction_binding_enforced',lambda:mutate_output('changed_prediction',changed_prediction),True)
def corrupted_receipt(s,o):
 q=common.load_json(o/'IMPORT_RECEIPT.json');q['protocol_version']='wrong';common.save_json(o/'IMPORT_RECEIPT.json',q)
 for z in s['reproducibility']['assets']:
  if z['path']=='IMPORT_RECEIPT.json':z.update(common.asset_record(o/z['path'],o))
test('receipt_task_binding_enforced',lambda:mutate_output('receipt',corrupted_receipt),True)
# Import every actual round2 CSV shape and compare its native numerical result.
for entry in common.registry()['tasks']:
 if entry['family']!='round2':continue
 t,p,xx,yy,rr=common.context(entry['task_id']);q=xx[['sample_id','group','fold']].copy();q['prediction']=rr[t['reference_model']];q['target']=yy.target
 for col in['particle','condition_scale']:
  if col in yy:q[col]=yy[col]
 f=W/(entry['task_id']+'.csv');q.to_csv(f,index=False);out=W/(entry['task_id']+'-submission')
 test('registered_round2_csv_'+entry['task_id'],lambda t=t,f=f,out=out:import_legacy.import_predictions(t['task_id'],f,out))
result={'checks':checks,'status':'pass'if all(x['status']=='pass'for x in checks)else'fail','passed':sum(x['status']=='pass'for x in checks),'total':len(checks),'engine_hashes':{str(p.relative_to(R)):common.digest(p)for p in (R/'evaluation').glob('*.py')},'schema_sha256':common.digest(R/'schemas/submission.schema.json')};(WORK/'LEGACY_IMPORT_QA.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'total':len(checks),'passed':result['passed'],'failures':[x for x in checks if x['status']=='fail']},indent=2))

raise SystemExit(0 if result["status"]=="pass" else 1)
