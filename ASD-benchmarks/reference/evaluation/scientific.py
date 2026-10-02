"""Non-admissive endpoint diagnostics. No submitted code is executed."""
import numpy as np

def checks(task,y,prediction,inputs=None,full_inputs=None,full_observations=None):
 p=np.asarray(prediction,float);case=task['case_number'];constraints=[]
 # Necessary endpoint semantics, not an industrial accuracy acceptance threshold.
 bounds={27:(0.,1.,'Void fraction is a fraction'),37:(0.,None,'Consumed electrical power'),53:(0.,None,'Angle-mean thread-forming torque magnitude'),57:(0.,None,'Dynamic viscosity'),59:(0.,None,'Normalized hourly generated energy'),61:(0.,None,'Forward hydrogen flux on the declared conditions'),67:(0.,None,'Elapsed transit time'),71:(0.,None,'Viable-cell density'),73:(0.,None,'Accumulated gas volume'),100:(0.,None,'Completed round-trip time')}
 if case==72 and task['family']=='original':bounds[72]=(0.,100.,'Yeast percentage')
 if case==72 and task['family']=='round2':bounds[72]=(0.,None,'Residual sugar concentration')
 if case==69:bounds[69]=(-273.15,None,'Temperature above absolute zero in degrees Celsius')
 if case in bounds:
  lo,hi,reason=bounds[case];bad=p<lo
  if hi is not None:bad|=p>hi
  constraints.append({'test':'endpoint_domain','source':'Declared target measurement semantics','interpretation':reason,'lower':lo,'upper':hi,'tested_rows':len(p),'violations':int(bad.sum()),'status':'not_tested_no_scored_rows'if not len(p)else'violated'if bad.any()else'no_violation_in_scored_rows'})
 if task['metric_kind'] in ['log_mae','log_transit']:
  constraints.append({'test':'log_eligibility','positive_target_rows':int((y.target.to_numpy(float)>0).sum()),'nonpositive_target_rows':int((y.target.to_numpy(float)<=0).sum()),'interpretation':'Nonpositive finite observations remain in physical-unit errors; this is not outcome deletion.'})
 result={'deterministic_checks':constraints,'causal_and_linked_group_audit':'Case-specific review: reviews/portfolios/'+task['case_id']+'/computational.json; grouped reconstruction and target-poisoning do not by themselves prove native future-prefix invariance','mechanistic_tests':'See the finding-specific scientific_validators in reviews/scientific/'+task['case_id']+'.json','mechanism_admission':'not_assessed_by_endpoint_checks','training_independence':'not_established_by_prediction_files'}
 result['native_prefix_mutation_test']=task.get('native_prefix_audit',{'status':'not_assessed_by_this_score','scope':'No native future-prefix mutation coverage is inferred from prediction-file scoring. Historical RAW_INVARIANTS covers only its listed cases.'})
 if inputs is not None:
  from batch5_checks import CASES,checks as extra
  if case in CASES:
   result['task_specific']=extra(task,y,p,inputs)
   result['mechanistic_tests']='reviews/portfolios/'+task['case_id']+'/combined/review.json'
  from batch6_checks import CASES as NEW_CASES,checks as new_checks
  if case in NEW_CASES:
   result['task_specific']=new_checks(task,y,p,inputs,full_inputs=full_inputs,full_observations=full_observations)
   result['mechanistic_tests']='reviews/portfolios/'+task['case_id']+'/combined/review.json'
  from batch7_checks import CASES as ASD7_CASES,checks as asd7_checks
  if case in ASD7_CASES:
   result['task_specific']=asd7_checks(task,y,p,inputs)
   result['mechanistic_tests']='reviews/portfolios/'+task['case_id']+'/combined/review.json'
 return result
