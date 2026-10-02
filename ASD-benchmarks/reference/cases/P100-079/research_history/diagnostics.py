from pathlib import Path
import json,sys
import numpy as np
import pandas as pd
import native
from develop import metrics,write,SPEC,CASE
from fit import fit
from run import predict,features
H=Path(__file__).resolve().parent
def main():
 d=native.prepare(Path(sys.argv[1]));d=d[d.partition=='development'].reset_index(drop=True);b=json.loads((H/'BASELINES.json').read_text());models={k:v['model'] for k,v in b.items()};oof={k:pd.read_csv(H/'BASELINE_PREDICTIONS.csv.gz')[k].to_numpy() for k in b}
 for p in sorted(H.glob('attempts/attempt-*/model.json')):
  met=json.loads((p.parent/'metrics.json').read_text());models[met['model_name']]=json.loads(p.read_text());oof[met['model_name']]=pd.read_csv(p.parent/'predictions.csv.gz').prediction.to_numpy()
 best=min(models,key=lambda k:metrics(d,oof[k])['primary_error']);err={k:metrics(d,v) for k,v in oof.items()};diagnostics={'development_only':True,'best_raw_error_model':best,'paired_group_comparisons':{},'identifiability':{},'source_limits':SPEC['scope']}
 for k in b:
  a=pd.DataFrame(err[best]['by_group']).set_index('group').mae;c=pd.DataFrame(err[k]['by_group']).set_index('group').mae;delta=a-c;diagnostics['paired_group_comparisons'][k]=dict(wins=int((delta<0).sum()),ties=int((abs(delta)<1e-12).sum()),groups=len(delta),mean_mae_difference=float(delta.mean()),differences=delta.to_dict())
 for k,m in models.items():
  if 'optimizer' in m:
   op=m['optimizer'];sv=op['jacobian_singular_values'];lo,hi=map(np.array,op['bounds']);v=np.array(m['coef']);diagnostics['identifiability'][k]=dict(rank=op['jacobian_rank'],parameters=len(v),near_bound_indices=np.where((v-lo<1e-4*(hi-lo))|(hi-v<1e-4*(hi-lo)))[0].tolist(),singular_values=sv,condition_number=float(sv[0]/sv[-1]) if sv[-1]>1e-12 else None)
  elif len(m['coef']):
   X=features(CASE,m['kind'],d);diagnostics['identifiability'][k]=dict(feature_rank=int(np.linalg.matrix_rank(X)),parameters=len(m['coef']),ridge_penalty=m.get('ridge_alpha'),warning='Regularized coefficients are not uniquely identified mechanisms when design columns are dependent.')
  else:diagnostics['identifiability'][k]=dict(parameters=0,meaning='Fixed calibration/persistence control')
 # Perturbations characterize frozen equations, not new parameter fits or interventions.
 sens={};m=models[best];pr=predict(m,d)
 for col in SPEC['inputs']:
  if d[col].nunique()<3:continue
  x=d.copy();step=max(float(np.std(d[col]))*.01,1e-5);x[col]+=step;q=predict(m,x);sens[col]=dict(step=step,median_prediction_change=float(np.median(q-pr)),min_change=float((q-pr).min()),max_change=float((q-pr).max()))
 diagnostics['local_input_sensitivity']=sens
 if CASE==76:
  stress={}
  for k,m in models.items():
   pp=np.zeros(len(d));states={}
   for date in sorted(d.date.unique()):
    tr=d[d.date!=date];va=d[d.date==date];mm=fit(CASE,m['kind'],tr);pp[d.date==date]=predict(mm,va);states[str(date)]=mm
   stress[k]=dict(metrics=metrics(d,pp),fold_states=states)
  write(H/'DATE_TRANSFER_STRESS.json',stress);diagnostics['date_stress']='Two development dates held out in turn; all final-date outcomes remain sealed. This low-date-count stress is supplementary and does not establish donor-level replication.'
 write(H/'DEVELOPMENT_DIAGNOSTICS.json',diagnostics);print(CASE,'development diagnostics complete',best)
if __name__=='__main__':main()
