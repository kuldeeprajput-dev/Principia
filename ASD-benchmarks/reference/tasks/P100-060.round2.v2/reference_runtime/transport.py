"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import followups as b, current as c

def predict(m,d):
 n=m['case'];v=np.array(m['parameters']);k=m['kind']
 if n==60:
  tau110=np.exp(v[0]);tau500=tau110*110/500 if k=='common_Q'else tau110;mm=dict(m,parameters=[np.log(tau110),np.log(tau500),v[1]]);return b.predict(mm,d)
 aa=v[2]if k=='linked_sherwood'else.6;L=np.array(m['lengths']);D=np.array(m['diameters']);idx=(D>.012).astype(int);logkap=v[idx]+np.log(.01/D)+aa*np.log(.14/L);logs=np.log([((1/2.016+1/M)/(1/2.016+1/28.0134))**((1-aa)/2)for M in [39.948,4.002602]])
 base=dict(m['base'],kind='plugflow_sherwood'if k=='linked_sherwood'else'plugflow_entrance',parameters=np.r_[logkap,logs,aa].tolist());return c.engine(61).predict(base,d)
