"""ASD7 source-aware endpoint diagnostics; arithmetic only, no submitted code."""
import json
import numpy as np
from metrics import weights
CASES={1,2,3,4,5,7,9,10,11,12,14,15,16,17,18,19,20,25,28,31,33,35,36,39,40,42,45,46,49,50,62,68,70,75,77,80,81,84,88,90,93,97,98,99}
VERSION='asd7-diagnostics/1.0'
def checks(task,y,prediction,inputs):
 p=np.asarray(prediction,float);n=task['case_number'];x=inputs
 if len(p)!=len(x)or len(p)!=len(y)or not np.isfinite(p).all():raise ValueError('Nonfinite or misaligned scientific diagnostic')
 result={'version':VERSION,'diagnostic_only':True,'automatic_mechanism_admission':False,'tests':[]}
 def emit(name,**v):result['tests'].append(dict(test=name,**v))
 if task.get('metric_kind')=='brier':emit('probability_domain',lower=0,upper=1,violations=int(((p<0)|(p>1)).sum()),interpretation='A probability of the registered event, not a mechanistic or causal score.')
 elif task.get('nonnegative_prediction'):emit('declared_nonnegative_endpoint',violations=int((p<0).sum()),interpretation='Necessary registered measurement domain; it does not establish accuracy.')
 for constraint in task.get('scientific_constraints',[]):
  if constraint.get('kind')=='target_bounds':
   lo=constraint.get('lower');hi=constraint.get('upper');bad=np.zeros(len(p),bool)
   if lo is not None:bad|=p<lo
   if hi is not None:bad|=p>hi
   emit('registered_target_bounds',lower=lo,upper=hi,violations=int(bad.sum()),meaning=constraint.get('meaning','Task-supplied measurement bound'))
 if n==1:emit('finite_prefix_scope',prefix_lengths=sorted({len(json.loads(s))for s in x.prefix_json}),horizons=sorted(x.horizon.unique().tolist()),interpretation='Signed-asinh prediction error is not an exact integer certificate or an infinite-sequence proof.')
 if n==3:emit('recorded_signal_scope',interpretation='This source segment includes a continuous-wave hardware injection. Endpoint accuracy cannot identify uncontaminated detector noise.')
 if n==4:emit('shared_reconstruction_scope',interpretation='Same-event reconstructed objects and MET share detector components; no independent new conservation-law evidence.')
 if n==5:
  nv=np.array([ord(str(g)[0])-63 for g in x.graph6]);emit('graph_size_bound',violations=int(((p<0)|(p>nv)).sum()),fractional_predictions=int((abs(p-np.rint(p))>1e-8).sum()),interpretation='Fractional size forecasts are permitted; certificate validity requires separate exact verification. The frozen source cohort has constant alpha.')
 if n==11:emit('offline_ratio_diagnostic',predictions_above_calibrated_offline=int((p>x.offline.to_numpy(float)).sum()),interpretation='Diagnostic only: source Server/Offline ratios can exceed one; this is not a universal physical bound.')
 if n==45:emit('same_event_detector_transfer',interpretation='Independent detector groups share one burst; current low-channel counts and pretrigger backgrounds are permitted. No independent-event test.')
 if n==46:emit('calibration_age',minimum_seconds=float(x.elapsed_lag_s.min())if len(x)else None,nonpositive_lags=int((x.elapsed_lag_s<=0).sum()),interpretation='Temperature history is earlier; current density and field are permitted. This is a local closure, not an as-issued future forecast.')
 if n==77:
  g=x.green.to_numpy(float);r=x.red.to_numpy(float);lo=100*np.maximum(0,g+r-1);hi=100*np.minimum(g,r);emit('joint_event_frechet_bounds',violations=int(((p<lo-1e-9)|(p>hi+1e-9)).sum()),interpretation='The joint percentage must be compatible with declared same-sample channel marginals. This logical bound is not independent biological confirmation.')
 if n==90:emit('normalized_rotation_bounds',lower=-1,upper=1,violations=int((abs(p)>1+1e-9).sum()),interpretation='Mean signed tangential direction cosine; a kinematic domain check, not a collective-motion law.')
 if n==98:emit('facet_count_diagnostic',fractional_predictions=int((abs(p-np.rint(p))>1e-8).sum()),interpretation='A regression estimate is not a combinatorial certificate. Exact native constructions and counterexamples are supplied separately.')
 if task['aggregation'].get('within_group_weight'):
  col=task['aggregation']['within_group_weight'];w=weights(y,task);emit('survey_weight_estimand',weight_column=col,normalized_weight_sum=float(w.sum()),groups=y.group.nunique(),interpretation='Source sample weights normalize within each complete evaluation group, then groups receive equal mass. This is not automatically a population-national estimator or design-based confidence interval.')
 if not result['tests']:emit('registered_contract_scope',interpretation=task['scope_limits'])
 return result
