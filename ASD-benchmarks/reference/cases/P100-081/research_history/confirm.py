"""Read reserved outcomes only after verifying a scientific freeze. No fitting/reselection."""
from pathlib import Path
import json,hashlib,datetime,shutil,sys
import numpy as np,pandas as pd
from native import prepare
from run import predict
ROOT=Path(__file__).resolve().parent

def main():
 if (ROOT/'CONFIRMATION_RECEIPT.json').exists():raise ValueError('Confirmation already exposed: use package replay')
 f=json.loads((ROOT/'FREEZE.json').read_text());p=json.loads((ROOT/'PROTOCOL.json').read_text())
 for rel,h in f['checked_files'].items():
  if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=h:raise ValueError('Freeze mismatch '+rel)
 d=prepare(Path(sys.argv[1]));d=d[d.partition=='confirmation'].reset_index(drop=True);out=ROOT/'package';out.mkdir(exist_ok=True);(out/'data').mkdir(exist_ok=True);(out/'evidence').mkdir(exist_ok=True)
 inputs=d[['sample_id','group']+p['input_columns']];obs=d[['sample_id','group','target']+[x for x in ['source_anchor','calibration_anchor','linked_unit','eligible_reason'] if x in d]];inputs.to_csv(out/'data/inputs.csv.gz',index=False);obs.to_csv(out/'data/observations.csv.gz',index=False)
 models={'reference':json.loads((ROOT/f['selected']/'model.json').read_text())}
 for q in sorted((ROOT/'baselines').glob('*'))+sorted((ROOT/'attempts').glob('*')):
  m=json.loads((q/'model.json').read_text());models[m['name']]=m
 rules={'case_id':p['case_id'],'input_columns':p['input_columns'],'numeric_columns':p['input_columns'],'input_units':p['input_units'],'target':p['target'],'target_units':p['target_units'],'error_units':p.get('error_units',p['target_units']),'metric_kind':'mae','models':models,'selected_from':f['selected'],'selection':'Development only; reference remains fixed even if another model is better on confirmation.'};(out/'rules.json').write_text(json.dumps(rules,indent=2)+'\n');q=d[['sample_id','group']].copy();metrics=[];bys=[]
 for name,m in models.items():
  v=predict(m,inputs);q[name]=v;e=v-d.target.to_numpy();a=pd.DataFrame({'group':d.group,'ae':abs(e),'se':e*e,'bias':e});g=a.groupby('group').agg(mae=('ae','mean'),mse=('se','mean'),bias=('bias','mean'));metrics.append(dict(model=name,primary_error=float(g.mae.mean()),mean_group_absolute_error=float(g.mae.mean()),rmse=float(np.sqrt(g.mse.mean())),bias=float(g.bias.mean()),worst_group_error=float(g.mae.max()),groups=len(g),scored_rows=len(d),assigned_rows=len(d),primary_units=p.get('error_units',p['target_units'])));bys.extend([dict(model=name,group=k,mae=float(r.mae),rmse=float(np.sqrt(r.mse)),bias=float(r.bias)) for k,r in g.iterrows()])
 q.to_csv(out/'evidence/predictions.csv.gz',index=False);pd.DataFrame(metrics).to_csv(out/'evidence/metrics.csv',index=False);pd.DataFrame(bys).to_csv(out/'evidence/by_group.csv',index=False);shutil.copy2(ROOT/'run.py',out/'run.py');(out/'requirements.txt').write_text('numpy\npandas\n')
 spec={k:p.get(k) for k in ['case_id','target','target_units','input_units','timing_contract','calibration','independent_unit','scope_limits','source_url','source_license','exposure','uncertainty_policy']};spec.update(error_units=p.get('error_units',p['target_units']),metric_kind='mae',permitted_inputs=p['input_columns'],numeric_columns=p['input_columns'],physical_bounds=p.get('physical_bounds',{}),protocol='original.v1',outcome_exposure='All packaged outcomes exposed after this campaign.');(out/'task_spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 receipt={'first_confirmation_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((ROOT/'FREEZE.json').read_bytes()).hexdigest(),'selected':f['selected'],'rows':len(d),'groups':d.group.nunique(),'no_fitting':True,'metrics':metrics};(ROOT/'CONFIRMATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'case':p['case_id'],'selected':f['selected'],'metrics':metrics}))
if __name__=='__main__':main()
