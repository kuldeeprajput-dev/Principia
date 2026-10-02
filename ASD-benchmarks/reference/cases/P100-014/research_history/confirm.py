"""Separate frozen confirmation; never fits or selects a model."""
from pathlib import Path
import json,hashlib,datetime,sys
import numpy as np,pandas as pd
from native import prepare
from run import predict,loss_report
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def main():
 if (P/'CONFIRMATION.json').exists():raise ValueError('Already exposed; preserve first receipt')
 fr=json.loads((P/'FREEZE.json').read_text())
 for a in fr['files']:
  f=P/a['path']
  if not f.is_file() or sha(f)!=a['sha256']:raise ValueError('Stale freeze '+a['path'])
 d=prepare(Path(sys.argv[1]));d=d[d.partition=='confirmation'].copy();spec=json.loads((P/'TASK_SPEC_PREFIT.json').read_text());inputs=spec['permitted_inputs'];q=P/'package';(q/'data').mkdir(parents=True,exist_ok=True);(q/'evidence').mkdir(exist_ok=True)
 x=d[['sample_id','group']+inputs];o=d[[k for k in d if k not in inputs]];pred=d[['sample_id','group']].copy();models=json.loads((P/'FROZEN_MODELS.json').read_text());metrics=[];groups=[]
 for name,state in models.items():
  pred[name]=predict(state,x);v=loss_report(d,pred[name].to_numpy(),spec['metric_kind']);metrics.append(dict(model=name,primary_units=spec['error_units'],**{k:v[k] for k in v if k!='per_group'}));groups.extend([dict(model=name,**g) for g in v['per_group']])
 for name,frame in [('data/inputs.csv.gz',x),('data/observations.csv.gz',o),('evidence/predictions.csv.gz',pred)]:frame.to_csv(q/name,index=False,float_format='%.17g',compression={'method':'gzip','mtime':0})
 pd.DataFrame(metrics).to_csv(q/'evidence/metrics.csv',index=False);pd.DataFrame(groups).to_csv(q/'evidence/by_group.csv',index=False)
 dump(P/'CONFIRMATION.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),freeze_sha256=sha(P/'FREEZE.json'),selected_model=fr['selected_model'],fitting_performed=False,reselection_performed=False,current_exposure='exposed',metrics=metrics,groups=groups));print(pd.DataFrame(metrics)[['model','primary_error','worst_group_error']].to_string(index=False))
if __name__=='__main__':main()
