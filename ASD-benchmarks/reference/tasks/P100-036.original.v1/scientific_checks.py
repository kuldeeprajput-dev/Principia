import numpy as np
def check(inputs,predictions):
 q=np.asarray(predictions)
 return {'finite':bool(np.isfinite(q).all()),'quantum_yield_bounds':bool(((q>=0)&(q<=1)).all())}
