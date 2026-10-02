import numpy as np
def check(inputs,predictions):
 p=np.asarray(predictions)
 return {'finite':bool(np.isfinite(p).all()),'probability_bounds':bool(((p>=0)&(p<=1)).all()),'first_trial_neutral_history':bool((inputs.loc[inputs.has_history==0,'history_mean']==.5).all())}
