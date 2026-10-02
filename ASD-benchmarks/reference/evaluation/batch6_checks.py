"""ASD6 registered endpoint diagnostics; static arithmetic, no submitted code."""
import numpy as np,pandas as pd
from metrics import event_metrics,weights
CASES={6,22,26,29,30,32,34,38,41,43,44,47,48,63,65,76,79,89,94,95}
VERSION='asd6-diagnostics/1.1'
def checks(task,y,prediction,inputs,full_inputs=None,full_observations=None):
 p=np.asarray(prediction,float);n=task['case_number'];x=inputs.copy();out={'version':VERSION,'rows':len(p),'diagnostic_only':True,'automatic_mechanism_admission':False,'tests':[]}
 if len(p)!=len(x)or len(p)!=len(y)or not np.isfinite(p).all():raise ValueError('Nonfinite or misaligned scientific diagnostic')
 def emit(test,**kw):out['tests'].append(dict(test=test,**kw))
 bounded={26:(0.,100.,'Selectivity percentage'),29:(0.,None,'Recorded fluorescence intensity; background uncertainty remains source-specific'),30:(0.,None,'Coefficient of friction'),34:(0.,None,'Magnitude of author-extracted first-pulse current'),43:(0.,None,'Validation log-perplexity'),44:(0.,7200.,'Capped resource consumption in seconds'),47:(0.,None,'Adjusted dissolved oxygen concentration'),48:(0.,None,'Downwelling longwave irradiance'),63:(0.,None,'Measured noise power spectral density'),76:(0.,None,'Spike-count expectation; fractional forecasts are permitted'),79:(0.,None,'Author-assigned emission rate; limits of detection not independently specified'),89:(0.,1.,'Binary choice probability'),95:(0.,None,'Author-derived turbulence kinetic energy')}
 if n in bounded:
  lo,hi,meaning=bounded[n];bad=p<lo
  if hi is not None:bad|=p>hi
  emit('endpoint_domain',lower=lo,upper=hi,interpretation=meaning,violations=int(bad.sum()))
 if n in[6,22,32,38,41,65,94]:emit('signed_or_offset_response',negative_predictions=int((p<0).sum()),interpretation='Sign alone does not establish physical invalidity for this registered response; use its units/source audit.')
 if n==43:
  emit('early_anchor_window',violations=int(((x.early_tokens_B>=x.anchor_tokens_B)|(x.anchor_tokens_B>20)|(x.tokens_B<=20)|(x.tokens_B>100)).sum()))
  rows=[]
  for g,a in x.assign(pred=p).groupby('group'):
   a=a.sort_values('tokens_B');rows.append({'group':str(g),'increasing_forecast_steps':int((a.pred.diff()>1e-9).sum())})
  emit('diminishing_loss_diagnostic',groups=rows,interpretation='A violation is a reported counterexample to monotone-decay claims, not automatic rejection of a valid noisy predictor.')
 if n==44:
  z=x[['group','is_flow','is_linear']].copy();z['target']=y.target.to_numpy();z['prediction']=p;regrets=[]
  for g,a in z.groupby('group'):
   if len(a)!=3:continue
   # Freeze the same tie order as source task: flow, linear, quadratic.
   a=a.assign(order=np.where(a.is_flow==1,0,np.where(a.is_linear==1,1,2))).sort_values(['prediction','order']);regrets.append({'group':str(g),'regret_seconds':float(a.iloc[0].target-a.target.min())})
  inventory=set(str(g) for g in task['evaluation_groups'])
  eligible=inventory.copy()
  if full_inputs is not None and full_observations is not None:
   zfull=full_inputs[['group']].copy();zfull['eligible']=np.isfinite(full_observations.target.to_numpy(float))
   eligible={str(g) for g,a in zfull.groupby('group') if len(a)==3 and a.eligible.all()}
  present=set(str(g) for g in x.group.unique());complete={r['group'] for r in regrets}
  emit('complete_instance_formulation_selection',complete_instances=len(regrets),assigned_instances=len(inventory),eligible_instances=len(eligible),incomplete_instances=len((present&eligible)-complete),fully_abstained_instances=len(eligible-present),ineligible_instances=len(inventory-eligible),decision_coverage=len(complete)/len(eligible) if eligible else None,mean_regret_seconds=float(np.mean([r['regret_seconds']for r in regrets]))if regrets else None,groups=regrets,interpretation='Offline paired replay only; denominator is the frozen full instance inventory. Incomplete triples are omitted from regret and remain visible in coverage. No deployment benefit is established.')
 if n==34:
  z=x[['group','calcium']].copy();z['prediction']=p;bad=sum(int((a.sort_values('calcium').prediction.diff()<-1e-9).sum())for _,a in z.groupby('group'));emit('within_animal_dose_monotonicity',negative_increments=bad,interpretation='Dose is confounded with time; monotonicity is a model claim, not causal proof.')
 if n==76 and len(y):
  e=event_metrics(y,p,task,.5);e.update(status='registered_integer_count_event',event='At least one spike: integer count >= 1',threshold_registered_before_outcomes=True);emit('spike_occurrence',**e)
 if n==65 and len(y):
  # A dB spectral task benefits from an explicitly secondary linear-PSD error.
  if np.any(np.maximum(p,y.target.to_numpy())>3000):emit('linear_psd_error',status='not_computed_overflow_domain')
  else:
   v=10**(p/10);t=10**(y.target.to_numpy()/10);w=weights(y,task);emit('linear_psd_error',group_balanced_mae=float(w@abs(v-t)),units='source linear frequency-noise PSD units',interpretation='Secondary to the frozen dB loss; dynamic-range weighting differs.')
 if n in[38,41]and {'prediction_time','target_time'}<=set(y):
  a=pd.to_datetime(y.prediction_time,errors='coerce',utc=True);b=pd.to_datetime(y.target_time,errors='coerce',utc=True);valid=a.notna()&b.notna();emit('forecast_time_order',parseable_rows=int(valid.sum()),non_future_targets=int((b[valid]<=a[valid]).sum()),interpretation='Tests declared timestamp ordering only; native causal-prefix audit checks source dependencies separately.')
 return out
