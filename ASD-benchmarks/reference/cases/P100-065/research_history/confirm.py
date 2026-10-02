"""Separate confirmation process. Checks scientific freeze before importing any predictor or adapter."""
from pathlib import Path
import hashlib,json,datetime,importlib.util,sys
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 p=ROOT;freeze=json.loads((p/'FREEZE.json').read_text())
 for a in freeze['files']:
  f=p/a['path']
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Frozen scientific asset changed '+a['path'])
 if (p/'CONFIRMATION_RECEIPT.json').exists():raise ValueError('Confirmation already exposed; replay saved artifacts instead')
 data_root=Path(sys.argv[1]);native=load('native_confirm',p/'native.py');run=load('run_confirm',p/'run.py');full=native.prepare(data_root);x=full[full.partition=='confirmation'].copy();protocol=json.loads((p/'PROTOCOL.json').read_text());st=json.loads((p/'STOPPING.json').read_text());pkg=p/'package';(pkg/'data').mkdir(parents=True);(pkg/'evidence').mkdir()
 selected=json.loads((p/'attempts'/st['selected_attempt']/'model.json').read_text());models={'reference':selected}
 for a in sorted(p.glob('baselines/*')):models['baseline_'+a.name]=json.loads((a/'model.json').read_text())
 for a in sorted(p.glob('attempts/attempt-*')):models[a.name.replace('-','_')]=json.loads((a/'model.json').read_text())
 cols=protocol['input_columns'];inputs=x[['sample_id','group']+cols+['condition_id']].reset_index(drop=True);obs=x[['sample_id','group','target','source_anchor','eligibility_reason']].reset_index(drop=True)
 rules={'case_id':p.name,'schema_version':'asd6.portable/1.0','input_columns':cols,'numeric_columns':cols,'input_units':protocol['input_units'],'target':protocol['target'],'target_units':protocol['target_units'],'error_units':protocol['error_units'],'metric_kind':'mae','aggregation':'Equal top-level group weight; equal rows within group. Dependent spectral bins are not independent replication.','reference_attempt':st['selected_attempt'],'models':models}
 (pkg/'rules.json').write_text(json.dumps(rules,indent=2)+'\n');inputs.to_csv(pkg/'data/inputs.csv.gz',index=False);obs.to_csv(pkg/'data/observations.csv.gz',index=False);(pkg/'run.py').write_bytes((p/'run.py').read_bytes());(pkg/'SOURCE_MANIFEST.json').write_bytes((p/'SOURCE_MANIFEST.json').read_bytes());(pkg/'dependencies.txt').write_bytes((p/'dependencies.txt').read_bytes())
 pred=inputs[['sample_id','group']].copy();metrics=[];by=[];extra=[]
 for name,state in models.items():
  pr=run.predict(state,inputs);pred[name]=pr
  if not np.isfinite(pr).all():raise ValueError('Nonfinite frozen confirmation prediction')
  err=pr-obs.target.to_numpy();g=pd.DataFrame({'group':inputs.group,'abs_error':abs(err),'sq_error':err*err,'bias':err}).groupby('group').mean();mae=float(g.abs_error.mean())
  metrics.append(dict(model=name,primary_error=mae,mean_group_absolute_error=mae,groups=len(g),scored_rows=len(obs),assigned_rows=len(obs),primary_units=protocol['error_units']))
  for group,r in g.iterrows():by.append(dict(model=name,group=group,mae=r.abs_error,rmse=np.sqrt(r.sq_error),bias=r.bias,rows=int((inputs.group==group).sum())))
  item=dict(model=name,group_mean_rmse=float(np.sqrt(g.sq_error).mean()),mean_bias=float(g.bias.mean()),worst_group_mae=float(g.abs_error.max()),row_absolute_error_q90=float(np.quantile(abs(err),.9)),negative_predictions=int((pr<0).sum()))
  if p.name=='P100-065':item['raw_PSD_MAE_Hz2_per_Hz']=float(np.mean(abs(10**(pr/10)-10**(obs.target.to_numpy()/10))))
  extra.append(item)
 pred.to_csv(pkg/'evidence/predictions.csv.gz',index=False);pd.DataFrame(metrics).to_csv(pkg/'evidence/metrics.csv',index=False);pd.DataFrame(by).to_csv(pkg/'evidence/by_group.csv',index=False);(pkg/'evidence/complementary_metrics.json').write_text(json.dumps(extra,indent=2)+'\n')
 receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((p/'FREEZE.json').read_bytes()).hexdigest(),'confirmation_rows':len(obs),'confirmation_groups':list(inputs.group.unique()),'selected_before_opening':st['selected_attempt'],'future_status':'exposed; no further tuning under this confirmation claim','scientific_revisions_after_opening':False,'result_metrics':metrics}
 (p/'CONFIRMATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'case':p.name,'reference':metrics[0],'comparators':metrics[1:]}),flush=True)
if __name__=='__main__':main()
