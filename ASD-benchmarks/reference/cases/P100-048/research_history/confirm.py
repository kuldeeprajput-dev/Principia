from pathlib import Path
import json,hashlib,datetime,shutil
import numpy as np,pandas as pd
from run import predict,read_table
P=Path(__file__).resolve().parent

def main():
 f=json.loads((P/'FREEZE.json').read_text())
 for a in f['files']:
  p=P/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Frozen artifact mismatch: '+a['path'])
 if (P/'CONFIRMATION_RECEIPT.json').exists():raise ValueError('Confirmation already opened; preserve first receipt')
 d=read_table(P/'prepared.csv.gz');q=d[d.partition=='confirmation'].reset_index(drop=True);spec=json.loads((P/'task_spec.json').read_text());out=P/'package';(out/'data').mkdir(parents=True,exist_ok=True);(out/'evidence').mkdir(exist_ok=True)
 states={k:json.loads((P/path).read_text()) for k,path in f['models'].items()};states={'reference':dict(states[f['selected']]),**states};pred=q[['sample_id','group']].copy();metrics=[];bygroup=[]
 for label,m in states.items():
  y=predict(m,q);pred[label]=y;rows=[]
  for group,ix in q.groupby('group').groups.items():
   ix=np.array(list(ix));err=y[ix]-q.target.to_numpy()[ix];row={'model':label,'group':group,'mae':float(np.mean(np.abs(err))),'rmse':float(np.sqrt(np.mean(err**2))),'bias':float(np.mean(err)),'q90_absolute_error':float(np.quantile(np.abs(err),.9)),'rows':len(ix)};rows.append(row);bygroup.append(row)
  metrics.append({'model':label,'primary_error':float(np.mean([r['mae'] for r in rows])),'mean_group_absolute_error':float(np.mean([r['mae'] for r in rows])),'groups':len(rows),'scored_rows':len(q),'assigned_rows':len(q),'primary_units':spec['error_units'],'worst_group_mae':max(r['mae'] for r in rows),'mean_group_rmse':float(np.mean([r['rmse'] for r in rows])),'mean_group_bias':float(np.mean([r['bias'] for r in rows]))})
 cols=spec['permitted_inputs'];q[['sample_id','group']+cols].to_csv(out/'data/inputs.csv.gz',index=False,float_format='%.17g');q[[c for c in q.columns if c not in cols]].to_csv(out/'data/observations.csv.gz',index=False,float_format='%.17g');pred.to_csv(out/'evidence/predictions.csv.gz',index=False,float_format='%.17g');pd.DataFrame(metrics).to_csv(out/'evidence/metrics.csv',index=False,float_format='%.17g');pd.DataFrame(bygroup).to_csv(out/'evidence/by_group.csv',index=False,float_format='%.17g')
 rules={'case_id':spec['case_id'],'input_columns':cols,'numeric_columns':spec['numeric_columns'],'input_units':spec['input_units'],'target':spec['target'],'target_units':spec['target_units'],'metric_kind':'mae','metric_units':spec['error_units'],'source':{'landing_url':spec['source_url']},'selected_from':f['selected'],'models':states,'exposure':'All confirmation outcomes now public-source-aware/exposed; no future fresh-test claim.','selection':'Frozen minimum development group-MAE,1% simplicity tie rule; no confirmation promotion.'};(out/'rules.json').write_text(json.dumps(rules,indent=2,allow_nan=False)+'\n')
 spec.update(selection=f['selected'],aggregation={'hierarchy':['group'],'weights':'equal group then equal eligible row'},exposure={'schema':spec['exposure'],'current':'exposed','confirmation_history':'Scores hidden until candidate selection, stopping and code/state freeze','fresh_for_future_users':False});(out/'task_spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 shutil.copy(P/'run.py',out/'run.py');shutil.copy(P/'requirements.txt',out/'requirements.txt');shutil.copy(P/'PRIOR_ART.json',out/'PRIOR_ART.json')
 receipt={'opened_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((P/'FREEZE.json').read_bytes()).hexdigest(),'selected':f['selected'],'no_fitting':True,'rows':len(q),'groups':sorted(q.group.unique()),'metrics':metrics,'future_status':'exposed'};(P/'CONFIRMATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'case':spec['case_id'],'selected':f['selected'],'metrics':metrics},indent=2))
if __name__=='__main__':main()
