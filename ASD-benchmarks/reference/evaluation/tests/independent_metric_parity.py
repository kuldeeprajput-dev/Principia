"""Reusable deterministic evaluator fixture; no model fitting or native data mutation."""
from pathlib import Path
import sys,json,hashlib
import numpy as np,pandas as pd
R=Path(__file__).resolve().parents[2]
import argparse,tempfile
_parser=argparse.ArgumentParser(description=__doc__);_parser.add_argument('--output',type=Path);_args=_parser.parse_args()
WORK=_args.output if _args.output is not None else Path(tempfile.mkdtemp(prefix='principia-evaluator-test-'))
WORK.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(R/'evaluation'));import common
records=[]
for entry in common.registry()['tasks']:
 task,package,x,y,refs=common.context(entry['task_id']);expected=common.table(package/'evidence/metrics.csv').set_index('model');keep=np.isfinite(y.target.to_numpy(float));obs=y.loc[keep].reset_index(drop=True);rr=refs.loc[keep].reset_index(drop=True)
 for name in task['baseline_models']:
  q=obs.copy();prediction=rr[name].to_numpy(float);truth=q.target.to_numpy(float);kind=task['metric_kind']
  if kind in ['log_mae','log_transit']:
   good=truth>0;q=q.loc[good].copy();q['loss']=np.abs(np.log(prediction[good]/truth[good]))
  else:q['loss']=(prediction-truth)**2 if kind in['rmse','brier'] else np.abs(prediction-truth)
  if task['aggregation'].get('within_group_weight'):
   column=task['aggregation']['within_group_weight'];groups=q.groupby('group').apply(lambda d:float(np.sum(d.loss*(d[column]/d[column].sum()))))
  elif task['aggregation']['hierarchy']==['group','particle']:
   groups=q.groupby(['group','particle']).loss.mean().groupby('group').mean()
  else:groups=q.groupby('group').loss.mean()
  if kind=='rmse':groups=groups.pow(.5)
  elif kind=='normalized_mae':groups=groups/q.groupby('group').condition_scale.first()
  value=float(groups.mean());old=float(expected.loc[name,'primary_error']);difference=abs(value-old)
  if not np.isclose(value,old,rtol=1e-9,atol=1e-10):raise ValueError(f'{task["task_id"]}/{name}: {value} != {old}')
  records.append({'task_id':task['task_id'],'model':name,'recomputed_primary_error':value,'archival_primary_error':old,'absolute_difference':difference})
print('PASS',len(records),'models')
(WORK/'INDEPENDENT_METRIC_PARITY.json').write_text(json.dumps({'status':'pass','method':'Separate direct group/particle reductions; no calls to shared metrics.py score()','models':len(records),'tasks':len({r['task_id']for r in records}),'maximum_absolute_difference':max(r['absolute_difference']for r in records),'records':records},indent=2)+'\n')
