import numpy as np
def check(inputs,predictions):
 p=np.asarray(predictions,dtype=float);x=inputs.copy();x['prediction']=p;violations=0;comparisons=0
 for _,g in x.groupby(['group','wt','mutant']):
  v=g.sort_values('quantile')['prediction'].to_numpy();violations+=int(np.sum(np.diff(v)<-1e-9));comparisons+=max(0,len(v)-1)
 return {'finite':bool(np.isfinite(p).all()),'quantile_order_violations':violations,'adjacent_quantile_comparisons':comparisons,'interpretation':'Native fluorescence may be signed; induced distribution quantiles should be nondecreasing, not necessarily positive.'}
