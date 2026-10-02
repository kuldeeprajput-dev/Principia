import numpy as np
def check(inputs,predictions):
 return {'finite':bool(np.isfinite(predictions).all()),'nonnegative_log_count':bool((np.asarray(predictions)>=0).all()),'positive_stiffness':bool((inputs.stiffness_kpa>0).all()),'known_shear':bool(inputs.hss.isin([0,1]).all())}
