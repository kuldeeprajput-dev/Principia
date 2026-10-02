"""Prediction-file scientific diagnostics; no fitting or submitted-code execution."""
import numpy as np
import pandas as pd
def check(inputs,observations,predictions,model='reference'):
 if not inputs.sample_id.astype(str).equals(observations.sample_id.astype(str)) or not inputs.sample_id.astype(str).equals(predictions.sample_id.astype(str)):raise ValueError('Identity/order mismatch')
 y=observations.target.to_numpy(float);p=predictions[model].to_numpy(float)
 if not np.isfinite(y).all() or not np.isfinite(p).all():raise ValueError('Nonfinite arithmetic')
 out={'rows':len(y),'negative_predictions':int((p<0).sum()),'nonfinite':0,'diagnostic_only':True}
 if 'probability' in inputs:
  out['probability_outside_unit_interval']=int(((p<0)|(p>1)).sum());out['binary_target_violations']=int((~np.isin(y,[0,1])).sum());out['threshold']=.5;out['threshold_meaning']='Conventional equal-cost classifier; not a validated clinical or industrial limit.'
 if 'calcium' in inputs:
  q=inputs[['group','calcium']].copy();q['prediction']=p;out['within_animal_negative_dose_increments']=sum(int((b.sort_values('calcium').prediction.diff().dropna()<-1e-9).sum()) for _,b in q.groupby('group'));out['monotonicity_limit']='Diagnostic only; calcium order is confounded with recording time.'
 if 'p0' in inputs:out['negative_prediction_interpretation']='Signed gauge pressures are permitted, so negatives are not invalid.'
 return out
