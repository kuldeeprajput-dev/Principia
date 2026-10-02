"""Confirmation process: verify frozen discovery states and evaluate without fitting."""
from pathlib import Path
import json,hashlib,datetime,shutil,sys
import numpy as np
import pandas as pd
from run import predict
from native import prepare
ROOT=Path(__file__).parent.parent

def main():
 data_root=Path(sys.argv[1]);freeze=json.loads((ROOT/'FREEZE.json').read_text())
 if (ROOT/'CONFIRMATION.json').exists():raise RuntimeError('Confirmation already exposed; do not overwrite first receipt')
 for item in freeze['assets']:
  p=ROOT/item['path']
  if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Frozen discovery asset changed '+item['path'])
 a=prepare(data_root);x=a[a.partition=='confirmation'].copy().reset_index(drop=True);p=ROOT.parent/'package';(p/'data').mkdir(parents=True,exist_ok=True);(p/'evidence').mkdir(exist_ok=True)
 protocol=json.loads((ROOT/'PROTOCOL.json').read_text());models={}
 paths=[ROOT/freeze['selected_path']]+sorted((ROOT/'baselines').glob('*/model.json'))+sorted((ROOT/'attempts').glob('*/model.json'))
 for i,path in enumerate(paths):models['reference' if i==0 else path.parent.name.replace('-','_')]=json.loads(path.read_text())
 inputs=x[['sample_id','group']+protocol['permitted_inputs']];observations=x[[c for c in x.columns if c not in protocol['permitted_inputs']]].copy();pred=x[['sample_id','group']].copy();metrics=[];by=[]
 for name,m in models.items():
  yhat=predict(m,inputs)
  if not np.isfinite(yhat).all():raise ValueError('Nonfinite confirmation prediction '+name)
  pred[name]=yhat;e=abs(yhat-x.target);ge=pd.DataFrame({'group':x.group,'e':e}).groupby('group').e.agg(['mean','size'])
  metrics.append({'model':name,'primary_error':float(ge['mean'].mean()),'mean_group_absolute_error':float(ge['mean'].mean()),'groups':len(ge),'scored_rows':len(x),'assigned_rows':len(x),'primary_units':protocol['target_units']})
  for g,row in ge.iterrows():by.append({'model':name,'group':g,'mean_absolute_error':float(row['mean']),'scored_rows':int(row['size'])})
 for frame,file in [(inputs,'data/inputs.csv.gz'),(observations,'data/observations.csv.gz'),(pred,'evidence/predictions.csv.gz')]:frame.to_csv(p/file,index=False,compression={'method':'gzip','mtime':0})
 pd.DataFrame(metrics).to_csv(p/'evidence/metrics.csv',index=False);pd.DataFrame(by).to_csv(p/'evidence/by_group.csv',index=False)
 rules={'schema_version':'principia.reference/3.0','case_id':protocol['case_id'],'source':{'landing_url':protocol['source_url']},'target':protocol['target'],'target_units':protocol['target_units'],'input_columns':protocol['permitted_inputs'],'numeric_columns':protocol['permitted_inputs'],'input_units':protocol['input_units'],'metric_kind':'mae','metric_units':protocol['target_units'],'assigned_rows':len(x),'models':models,'missingness_policy':'Reject missing or nonfinite required predictors; no imputation.','reference_selection':'Selected by grouped development only before confirmation; aliases name same fitted state, not independent findings.','exposure':'Confirmation opened after freeze; now exposed to future users.'}
 (p/'rules.json').write_text(json.dumps(rules,indent=2));shutil.copy(ROOT/'tools/run.py',p/'run.py');shutil.copy(ROOT/'SOURCE_MANIFEST.json',p/'SOURCE_MANIFEST.json');(p/'preparation').mkdir(exist_ok=True);shutil.copy(ROOT/'tools/native.py',p/'preparation/native.py')
 task={k:protocol[k] for k in ['target','target_units','permitted_inputs','input_units','timing_contract','independent_unit','scope_limits','source_url','source_license','uncertainty']};task.update({'error_units':protocol['target_units'],'metric_kind':'mae','numeric_columns':protocol['permitted_inputs'],'calibration':protocol['timing_contract'],'exposure':{'status':'exposed','confirmation_originally_withheld':True,'public_source_aware':True},'uncertainty_policy':protocol['uncertainty'],'applicability':'Only source material, geometry, heating-rate or measured beam ranges; no unobserved population guarantee.'});(p/'task_spec.json').write_text(json.dumps(task,indent=2))
 receipt={'opened_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((ROOT/'FREEZE.json').read_bytes()).hexdigest(),'selected_path':freeze['selected_path'],'selection_unchanged':True,'confirmation_groups':sorted(x.group.unique()),'rows':len(x),'metrics':metrics,'all_candidates_retained':True,'fresh_external_experiment':False}
 (ROOT/'CONFIRMATION.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
