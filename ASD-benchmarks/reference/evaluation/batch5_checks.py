"""Source-defined diagnostics for the ten ASD5 tasks. No submitted code is run."""
import numpy as np
import pandas as pd
EXTENSION_VERSION='asd5-diagnostics/1.0'
CASES={13,21,51,54,56,64,74,85,87,91}
def event_counts(a,b):
 a=np.asarray(a,bool);b=np.asarray(b,bool);tp=int((a&b).sum());fp=int((~a&b).sum());fn=int((a&~b).sum());tn=int((~a&~b).sum());den=2*tp+fp+fn
 return {'TP':tp,'FP':fp,'FN':fn,'TN':tn,'precision':tp/(tp+fp)if tp+fp else None,'recall':tp/(tp+fn)if tp+fn else None,'specificity':tn/(tn+fp)if tn+fp else None,'F1':2*tp/den if den else None,'F1_undefined_reason':None if den else'No observed or predicted positive events'}
def checks(task,y,prediction,inputs):
 n=task['case_number'];p=np.asarray(prediction,float);x=inputs.copy();out={'extension_version':EXTENSION_VERSION,'admission':'diagnostic_only','independent_replication':False,'scored_rows':len(p)}
 if len(p)!=len(x)or len(p)!=len(y):raise ValueError('Diagnostic input alignment mismatch')
 if len(p)and not np.isfinite(p).all():raise ValueError('Nonfinite diagnostic values')
 if n in[13,21,54,56,85,91]:out['below_zero']=int((p<0).sum())
 if n==13:
  out['above_complete_conversion']=int((p>1).sum());out['limits']='A bounded conversion prediction does not identify chemical species; one reserved heating-rate trace.'
 if n==21:out['metrology']='Recorded-channel effective resistance; undocumented gain prevents intrinsic junction resistance identification.'
 if n==51:
  violations=0;tested=0
  for _,z in x.assign(prediction=p).groupby('group'):
   delta=np.diff(z.sort_values('gate_V').prediction.to_numpy());violations+=int((delta<-1e-10).sum());tested+=len(delta)
  out['curve_monotonicity']={'tested_adjacent_pairs':tested,'decreasing_pairs':violations,'meaning':'Shape diagnostic, not proof of transport mechanism; only submitted covered voltages are compared.'}
  out['calibration_budget']='Exactly three same-device anchor currents at -20,0,20V. No scored anchor rows.'
 if n==54:out['measurement_timing']='Measured geometry may come from post-test imaging; a geometry-conditioned failure-load reconstruction is not a prospective process-control demonstration.'
 if n==56:out['calibration_timing']={'rows_after_calibration':int((x.deflection_mm>x.calibration_deflection_mm).sum()),'calibration_beyond_10mm':int((x.calibration_deflection_mm>10).sum()),'no_safety_certification':True}
 if n==64:out['signed_endpoint']='Signed photodiode current; negative values are permitted. This endpoint is not luminance.';out['causal_alignment_limit_s']=2
 if n==74:out['timing']={'targets_at_or_before_7_5min':int((x.time_min<=7.5).sum()),'calibration_times_min':[3,4.5,6]};out['metrology']='Source instrument units; no biological replication or clinical interpretation.'
 if n==85:
  out['stoichiometric_diagnostic']={'predictions_above_complete_oxidation_ratio':int((p>(76.05/62.07)*np.maximum(x.eg_consumed_g_L.to_numpy(),0)+1e-9).sum()),'meaning':'Contemporaneous assays with measurement error; this is not a hard industrial acceptance bound.'}
 if n==87:
  out['outside_contribution_budget']=int(((p<0)|(p>x.endowment.to_numpy()+1e-9)).sum())
  z=x.assign(target=y.target.to_numpy(),prediction=p);z['actual_weighted']=z.productivity*z.target;z['predicted_weighted']=z.productivity*z.prediction
  sizes=z.groupby(['group','round']).size();good=sizes[sizes==2].index;total=task['eligible_rows']//2
  # When either player abstains, the pair-round event is unscored rather than imputed.
  if len(good):
   a=z.groupby(['group','round']).agg(actual=('actual_weighted','sum'),prediction=('predicted_weighted','sum'),threshold=('threshold','first')).loc[good]
   result=event_counts(a.actual>=a.threshold-1e-9,a.prediction>=a.threshold-1e-9)
  else:result=event_counts([],[])
  out['coordination_success']={**result,'complete_scored_pair_rounds':len(good),'eligible_pair_rounds':total,'coverage':len(good)/total if total else None,'source_threshold':'theta=(p1*e1+p2*e2)/2, source game rules','aggregation':'Pair-round descriptive counts; dependent rounds are not independent replications','incomplete_pair_rounds_in_scored_rows':int((sizes!=2).sum())}
  out['falsifier']='High success-event F1 can coexist with weak specificity; report both.'
 if n==91:out['information_budget']='Achieved throughput is contemporaneous; configured minus achieved rate is not measured packet loss. Source throughput precision constrains slope interpretation.'
 return out
