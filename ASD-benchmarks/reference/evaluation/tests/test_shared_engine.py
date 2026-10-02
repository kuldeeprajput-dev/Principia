"""Reusable deterministic evaluator fixture; no model fitting or native data mutation."""
from pathlib import Path
import sys,json,shutil,copy,hashlib
import numpy as np,pandas as pd
R=Path(__file__).resolve().parents[2]
import argparse,tempfile
_parser=argparse.ArgumentParser(description=__doc__);_parser.add_argument('--output',type=Path);_args=_parser.parse_args()
WORK=_args.output if _args.output is not None else Path(tempfile.mkdtemp(prefix='principia-evaluator-test-'))
WORK.mkdir(parents=True,exist_ok=True)
W=WORK/'shared_fixtures';W.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'evaluation'))
import metrics,common,submissions,workflow
checks=[]
def record(name,fn,expect_reject=False):
 try:r=fn()
 except (ValueError,TypeError,KeyError)as e:
  checks.append({'check':name,'status':'pass'if expect_reject else'fail','error':str(e)});return
 checks.append({'check':name,'status':'fail'if expect_reject else'pass','detail':'unexpected acceptance'if expect_reject else str(r)})
def approx(actual,expected):
 if not np.isclose(actual,expected,rtol=1e-12,atol=1e-12):raise ValueError(f'{actual} != {expected}')
 return actual
base={'aggregation':{'hierarchy':['group']},'metric_kind':'mae','primary_units':'U','target_units':'U','error_units':'U'}
d=pd.DataFrame({'group':['A']*3+['B'],'particle':['p1','p1','p2','p1'],'target':[0.,0,0,0]});p=np.array([0.,10,10,100])
hier=dict(base,aggregation={'hierarchy':['group','particle']})
record('hierarchical_group_particle_mae',lambda:approx(metrics.score(d,p,hier)[0]['primary_error'],53.75))
record('hierarchical_weights_sum',lambda:approx(metrics.weights(d,hier).sum(),1))
record('group_mae_differs_from_row_average',lambda:approx(metrics.score(d,p,base)[0]['primary_error'],(20/3+100)/2))
record('mean_group_rmse_not_pooled_rmse',lambda:approx(metrics.score(d,p,dict(base,metric_kind='rmse'))[0]['primary_error'],(np.sqrt(200/3)+100)/2))
q=pd.DataFrame({'group':['A','A','B','B'],'target':[1.,1.,0.,0.]});pred=np.array([0.,0.,1.,1.])
record('total_event_failure_f1_is_zero',lambda:approx(metrics.event_metrics(q,pred,base,.5)['f1'],0))
record('no_event_f1_is_undefined',lambda:metrics.event_metrics(q.assign(target=0.),np.zeros(4),base,.5)['f1']is None or(_ for _ in()).throw(ValueError('not undefined')))
record('event_confusion_mass',lambda:approx(sum(metrics.event_metrics(q,pred,base,.5)['weighted_confusion'].values()),1))
q2=pd.DataFrame({'group':['A','A','B','B'],'target':[2.,2.,4.,4.],'condition_scale':[1.,1.,2.,2.]})
record('frozen_condition_normalization',lambda:approx(metrics.score(q2,np.zeros(4),dict(base,metric_kind='normalized_mae'))[0]['primary_error'],2))
record('invalid_condition_normalization',lambda:metrics.score(q2.assign(condition_scale=0.),np.zeros(4),dict(base,metric_kind='normalized_mae')),True)
q3=pd.DataFrame({'group':['A','A','B','B'],'target':[-1.,0.,1.,4.]})
record('log_eligibility_primary',lambda:approx(metrics.score(q3,np.array([1.,1.,2.,2.]),dict(base,metric_kind='log_mae'))[0]['primary_error'],np.log(2)))
record('nonpositive_targets_keep_physical_error',lambda:approx(metrics.score(q3,np.array([1.,1.,2.,2.]),dict(base,metric_kind='log_mae'))[0]['group_balanced_mae'],1.5))
record('negative_log_prediction_rejected',lambda:metrics.score(q3,np.array([-1.,1.,2.,2.]),dict(base,metric_kind='log_mae')),True)
record('signed_physical_values_allowed',lambda:approx(metrics.score(q3,q3.target.to_numpy(),base)[0]['primary_error'],0))
record('nonfinite_error_overflow_rejected',lambda:metrics.score(q3.assign(target=-1e308),np.full(4,1e308),base),True)
ival=metrics.interval_metrics(q,np.ones(4)*.5,np.zeros(4),np.ones(4),.9,base)
record('interval_constant_width_all_ties_retained',lambda:all(x['achieved_group_weighted_coverage']==1 for x in ival['risk_coverage'])or(_ for _ in()).throw(ValueError('tie selection')))
record('proper_interval_score_exact',lambda:approx(ival['proper_interval_score'],1))
record('zero_rows_abstention_defined',lambda:metrics.score(q.iloc[:0],np.array([]),base)==(None,[])or(_ for _ in()).throw(ValueError('empty')))
# Strict static parsing and safe-path rules.
for name,txt in [('duplicate_json','{"x":1,"x":2}'),('nan_json','{"x":NaN}'),('overflow_json','{"x":1e999}')]:
 path=W/(name+'.json');path.write_text(txt);record(name,lambda path=path:common.load_json(path),True)
record('path_escape_rejected',lambda:common.safe_path(W,'../x'),True)
# Minimal well-formed v3 prediction-only submission.
task=dict(base,case_id='P100-023',task_id='toy',protocol_version='toy-1',cohort_id='toy-c',input_sha256='a'*64,permitted_inputs=['x'],evaluation_groups=['A','B'],positive_prediction=False,nonnegative_prediction=False)
x=pd.DataFrame({'sample_id':['a','b','c','d'],'group':['A','A','B','B'],'x':[1.,2,3,4]})
base_s={'schema_version':'principia.submission/3.0',**{k:task[k]for k in['case_id','task_id','protocol_version','cohort_id','input_sha256','target_units']},'evaluator_version':common.VERSION,'decision':'predict','permitted_inputs':['x'],'predictions_file':'predictions.csv','training':{'training_group_ids':[],'tuning_group_ids':[],'evaluation_data_usage':'exposed'},'equations':[{'id':'E1','expression':'x'}],'findings':[{'id':'F1','equation_ids':['E1'],'statement':'Synthetic validation fixture'}],'uncertainty':{'interval_level':None},'reproducibility':{'assets':[],'entrypoint':None}}
predframe=pd.DataFrame({'sample_id':x.sample_id,'prediction':[1.,2,3,4],'status':'predict','reason':''})
def fixture(name,change=None,frame=None):
 out=W/name;out.mkdir(exist_ok=True);s=copy.deepcopy(base_s)
 if change:change(s)
 (frame if frame is not None else predframe).to_csv(out/'predictions.csv',index=False);(out/'submission.json').write_text(json.dumps(s));return out
record('valid_prediction_only_submission',lambda:submissions.validate(fixture('valid'),task,x)[2])
record('wrong_units_rejected',lambda:submissions.validate(fixture('units',lambda s:s.update(target_units='wrong')),task,x),True)
record('wrong_task_identity_rejected',lambda:submissions.validate(fixture('task',lambda s:s.update(task_id='wrong')),task,x),True)
record('wrong_protocol_rejected',lambda:submissions.validate(fixture('protocol',lambda s:s.update(protocol_version='wrong')),task,x),True)
record('wrong_input_hash_rejected',lambda:submissions.validate(fixture('hash',lambda s:s.update(input_sha256='b'*64)),task,x),True)
record('forbidden_input_rejected',lambda:submissions.validate(fixture('forbidden',lambda s:s.update(permitted_inputs=['target'])),task,x),True)
record('false_independence_declaration_rejected',lambda:submissions.validate(fixture('independence',lambda s:s['training'].update(training_group_ids=['A'],evaluation_data_usage='never_used_for_fitting_or_tuning')),task,x),True)
record('unknown_schema_version_rejected',lambda:submissions.validate(fixture('schema',lambda s:s.update(schema_version='future-garbage',protocol_id='toy-1')),task,x),True)
record('duplicate_ids_rejected',lambda:submissions.validate(fixture('duplicate',frame=predframe.assign(sample_id='a')),task,x),True)
record('missing_ids_rejected',lambda:submissions.validate(fixture('missing',frame=predframe.iloc[:-1]),task,x),True)
record('infinite_prediction_rejected',lambda:submissions.validate(fixture('infinite',frame=predframe.assign(prediction=np.inf)),task,x),True)
record('abstention_reason_required',lambda:submissions.validate(fixture('reason',frame=predframe.assign(prediction='',status='abstain')),task,x),True)
record('whole_task_abstention_valid',lambda:submissions.validate(fixture('abstain',lambda s:s.update(decision='abstain',abstention_reason='Insufficient evidence',equations=[],findings=[]),predframe.assign(prediction='',status='abstain',reason='Insufficient evidence')),task,x)[2])
record('partial_abstention_valid',lambda:submissions.validate(fixture('partial',frame=pd.concat([predframe.iloc[:2],predframe.iloc[2:].assign(prediction='',status='abstain',reason='Outside scope')])),task,x)[2])
record('prediction_nonempty_on_abstention_rejected',lambda:submissions.validate(fixture('badabstain',frame=predframe.assign(status='abstain',reason='Outside scope')),task,x),True)
record('point_outside_interval_rejected',lambda:submissions.validate(fixture('badinterval',lambda s:s['uncertainty'].update(interval_level=.9),predframe.assign(lower=0,upper=.5)),task,x),True)
record('input_asset_hash_rejected',lambda:submissions.validate(fixture('assethash',lambda s:s['reproducibility'].update(assets=[{'path':'predictions.csv','sha256':'0'*64}])),task,x),True)
record('inconsistent_finding_equation_rejected',lambda:submissions.validate(fixture('finding',lambda s:s['findings'][0].update(equation_ids=['E2'])),task,x),True)
(W.parent/'EVALUATOR_COMPUTATIONAL_FIXTURES.json').write_text(json.dumps({'checks':checks,'engine_hashes':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in (R/'evaluation').glob('*.py')}},indent=2)+'\n')
print(json.dumps({'checks':len(checks),'passed':sum(c['status']=='pass'for c in checks),'failures':[c for c in checks if c['status']=='fail']},indent=2))

raise SystemExit(0 if all(c["status"]=="pass" for c in checks) else 1)
