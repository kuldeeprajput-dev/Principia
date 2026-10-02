"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import transport as t, current as c

def predict(m,d):
 n=m['case'];v=np.array(m['parameters']);k=m['kind']
 if n==60:return t.predict(dict(m,kind='common_Q',parameters=[v[0],1]),d)
 vv=np.repeat(v[0],2)if k=='one_film_scale'else v
 if k!='reversed_mass':return t.predict(dict(m,kind='developing_film',parameters=vv.tolist()),d)
 L=np.array(m['lengths']);D=np.array(m['diameters']);idx=(D>.012).astype(int);logkap=vv[idx]+np.log(.01/D)+.6*np.log(.14/L);logs=-np.log([((1/2.016+1/M)/(1/2.016+1/28.0134))**.2 for M in [39.948,4.002602]]);base=dict(m['base'],kind='plugflow_entrance',parameters=np.r_[logkap,logs,.6].tolist());return c.engine(61).predict(base,d)
