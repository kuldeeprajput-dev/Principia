"""Frozen-only confirmation reader. No fitting, tuning or winner selection."""
from pathlib import Path
import json,hashlib,datetime,importlib.util,sys
import numpy as np,pandas as pd
from native import prepare,INPUTS
C=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
def main():
 if(C/'CONFIRMATION.json').exists():raise ValueError('Confirmation was already exposed; preserve its first receipt')
 freeze=json.loads((C/'FREEZE.json').read_text())
 for a in freeze['files']:
  p=C/a['path']
  if not p.is_file()or sha(p)!=a['sha256']or p.stat().st_size!=a['bytes']:raise ValueError('Stale freeze '+a['path'])
 sp=importlib.util.spec_from_file_location('frozen',C/'package/run.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
 d=prepare(Path(sys.argv[1]));d=d[d.partition=='confirmation'].copy();p=C/'package';(p/'data').mkdir(exist_ok=True);(p/'evidence').mkdir(exist_ok=True)
 ids=['sample_id','group'];x=d[ids+INPUTS].copy();obs=d[ids+['target']+[c for c in d if c not in ids+INPUTS+['target']]].copy();pred=d[ids].copy();models=json.loads((C/'FROZEN_MODELS.json').read_text());metrics=[];groups=[];extra={}
 for name,s in models.items():
  v=r.predict(s,x);pred[name]=v;z=d.copy();z['error']=v-z.target
  g=z.groupby('group').error.agg(lambda a:float(abs(a).mean()));metrics.append({'model':name,'primary_error':float(g.mean()),'mean_group_absolute_error':float(g.mean()),'groups':len(g),'scored_rows':len(z),'assigned_rows':len(z),'primary_units':'nats per token'if 'tokens_B'in d else'seconds'})
  for group,e in g.items():groups.append({'model':name,'group':group,'mae':float(e),'bias':float(z[z.group==group].error.mean()),'rows':int((z.group==group).sum())})
  if 'tokens_B'in d:extra[name]={'late_horizon_mae':float(z[z.tokens_B>60].groupby('group').error.agg(lambda a:abs(a).mean()).mean())}
  else:
   regrets=[];choices=[]
   for group,a in z.groupby('group'):
    a=a.copy();a['prediction']=a.target+a.error;choice=a.sort_values(['prediction','formulation']).iloc[0];regrets.append(float(choice.target-a.target.min()));choices.append({'group':group,'chosen_formulation':choice.formulation,'regret_seconds':regrets[-1]})
   extra[name]={'mean_offline_selection_regret':float(np.mean(regrets)),'decisions':choices}
 for name,frame in [('data/inputs.csv.gz',x),('data/observations.csv.gz',obs),('evidence/predictions.csv.gz',pred)]:frame.to_csv(p/name,index=False,float_format='%.17g',compression={'method':'gzip','mtime':0})
 pd.DataFrame(metrics).to_csv(p/'evidence/metrics.csv',index=False);pd.DataFrame(groups).to_csv(p/'evidence/by_group.csv',index=False);save(p/'evidence/complementary.json',extra)
 save(C/'CONFIRMATION.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':sha(C/'FREEZE.json'),'selected_model':freeze['selected_model'],'fitting_performed':False,'reselection_performed':False,'current_exposure':'exposed','metrics':metrics,'groups':groups,'complementary':extra,'assets':[{'path':str(q.relative_to(C)),'sha256':sha(q)}for q in sorted(p.rglob('*'))if q.is_file()and q.suffix in['.gz','.csv','.json']]})
 for m in metrics:print(m['model'],m['primary_error'])
if __name__=='__main__':main()
