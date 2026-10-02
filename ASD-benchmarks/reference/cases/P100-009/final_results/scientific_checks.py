import numpy as np
def check(inputs,predictions):
 p=np.asarray(predictions,dtype=float)
 return {'finite':bool(np.isfinite(p).all()),'domain_respected':bool((p>=0).all()),'interpretation':'Declared numerical domain only; not an industrial acceptance threshold'}
