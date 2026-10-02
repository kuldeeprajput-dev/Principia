from pathlib import Path
import json,hashlib,datetime,importlib.util
import numpy as np,pandas as pd
from native import prepare
W=Path(__file__).resolve().parent;P=W/'package';D=W.parents[3].parent/'local-datas'
def main():
 freeze=json.loads((W/'FREEZE.json').read_text())
 for a in freeze['files']:
  p=W/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Frozen asset changed '+a['path'])
 d=prepare(D);d=d[(d.partition=='confirmation')&d.target.notna()].reset_index(drop=True)
 spec=importlib.util.spec_from_file_location('frozen',P/'run.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
 def write(name,x):
  p=P/name;p.parent.mkdir(parents=True,exist_ok=True);x.to_csv(p,index=False,compression={'method':'gzip','mtime':0}if p.suffix=='.gz'else None,float_format='%.17g')
 x=d[['sample_id','group','offered_Mbps','achieved_Mbps']];write('data/inputs.csv.gz',x);write('data/observations.csv.gz',d[['sample_id','group','target','partition','source_archive','source_member','source_anchor']]);pred=x[['sample_id','group']].copy();metrics=[];group=[]
 for k in json.loads((P/'rules.json').read_text())['models']:
  y=r.predict(k,x);pred[k]=y;errs=pd.DataFrame({'group':d.group,'error':y-d.target});m=errs.groupby('group').error.agg(lambda a:np.abs(a).mean());metrics.append(dict(model=k,primary_error=m.mean(),mean_group_absolute_error=m.mean(),groups=len(m),scored_rows=len(d),assigned_rows=len(d),primary_units='ms',rmse=float(np.sqrt(np.mean(errs.error**2))),bias=float(errs.error.mean())))
  for g,e in m.items():group.append(dict(model=k,group=g,mae=e))
 write('evidence/predictions.csv.gz',pred);write('evidence/metrics.csv',pd.DataFrame(metrics));write('evidence/by_group.csv',pd.DataFrame(group))
 receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((W/'FREEZE.json').read_bytes()).hexdigest(),'fitting_performed':False,'confirmation_groups':sorted(d.group.unique()),'rows':len(d),'current_exposure':'exposed','future_scoring':'retrospective','metrics':metrics}
 (W/'CONFIRMATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(pd.DataFrame(metrics).to_string(index=False))
if __name__=='__main__':main()
