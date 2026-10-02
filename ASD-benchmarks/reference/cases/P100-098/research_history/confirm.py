"""One-shot evaluation of frozen models; never fits or selects a model."""
from pathlib import Path
import json, hashlib, datetime, importlib.util, sys
import numpy as np
import pandas as pd
C=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_text())
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
def module(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 if (C/'CONFIRMATION_RECEIPT.json').exists():raise ValueError('Confirmation already exposed; do not replace the first receipt')
 freeze=load(C/'FREEZE.json')
 for a in freeze['files']:
  p=C/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Frozen artifact changed: '+a['path'])
 native=module('native_confirm',C/'native.py');run=module('predict_confirm',C/'package/run.py')
 d=native.prepare(Path(sys.argv[1]));d=d[d.partition=='confirmation'].reset_index(drop=True)
 models=load(C/'FROZEN_MODELS.json');spec=load(C/'package/task_spec.json');p=C/'package';(p/'data').mkdir(exist_ok=True);(p/'evidence').mkdir(exist_ok=True)
 pred=d[['sample_id','group']].copy();rows=[];groups=[]
 for name,state in models.items():
  z=run.predict(state,d);pred[name]=z;g=[]
  for group,ix in d.groupby('group').groups.items():
   ix=np.array(list(ix));e=z[ix]-d.target.to_numpy(float)[ix];a={'model':name,'group':group,'mae':float(np.mean(abs(e))),'rmse':float(np.sqrt(np.mean(e*e))),'bias':float(np.mean(e)),'rows':len(ix)};g.append(a);groups.append(a)
  rows.append({'model':name,'primary_error':float(np.mean([a['mae']for a in g])),'groups':len(g),'scored_rows':len(d),'assigned_rows':len(d),'primary_units':spec['error_units'],'worst_group_mae':max(a['mae']for a in g),'mean_group_rmse':float(np.mean([a['rmse']for a in g]))})
 def table(name,df):df.to_csv(p/name,index=False,float_format='%.17g',compression={'method':'gzip','mtime':0}if name.endswith('.gz')else None)
 inputs=spec['permitted_inputs'];table('data/inputs.csv.gz',d[['sample_id','group']+inputs]);table('data/observations.csv.gz',d[[k for k in d if k not in inputs]])
 table('evidence/predictions.csv.gz',pred);table('evidence/metrics.csv',pd.DataFrame(rows));table('evidence/by_group.csv',pd.DataFrame(groups))
 save(p/'rules.json',{'case_id':spec['case_id'],'input_columns':inputs,'numeric_columns':spec['numeric_columns'],'input_units':spec['input_units'],'target':spec['target'],'target_units':spec['target_units'],'metric_kind':spec['metric_kind'],'models':models,'selection':freeze['selected_model'],'all_coefficients_frozen':True,'outcomes_now_exposed':True})
 receipt={'opened_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((C/'FREEZE.json').read_bytes()).hexdigest(),'selected_model':freeze['selected_model'],'no_fitting':True,'rows':len(d),'groups':sorted(d.group.unique()),'future_status':'exposed','metrics':rows}
 save(C/'CONFIRMATION_RECEIPT.json',receipt)
 print(spec['case_id'],freeze['selected_model'],[(r['model'],r['primary_error'])for r in rows],flush=True)
if __name__=='__main__':main()
