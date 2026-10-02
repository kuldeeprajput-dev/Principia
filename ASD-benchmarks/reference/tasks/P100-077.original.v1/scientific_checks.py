import numpy as np
def check(inputs,predictions):
 p=inputs.green.to_numpy();q=inputs.red.to_numpy();y=np.asarray(predictions)/100
 return {'finite':bool(np.isfinite(y).all()),'frechet_lower':bool((y>=np.maximum(0,p+q-1)-1e-12).all()),'frechet_upper':bool((y<=np.minimum(p,q)+1e-12).all())}
