"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import adaptive as a

def predict(m,d):
 n=m['case'];v=np.array(m['parameters']);kind=m['kind'];mm=dict(m)
 if n==60:mm['parameters']=[v[0],v[1],v[2],v[2]];return a.predict(mm,d)
 if n==72:
  beta=np.full((len(d),2),v[0])if kind=='common_clock'else np.tile(v[:2],(len(d),1))*np.exp(v[2]*d.coculture.to_numpy())[:,None];time=(d.time_h.to_numpy()-22)/50;y=np.zeros(len(d))
  for j,q in enumerate(['G','F']):y+=d[q+'72'].to_numpy()*np.exp(-np.maximum(np.log(d[q+'22']/d[q+'72']),0)*(time**beta[:,j]-1))
  return y
 if n==61:
  logs=np.array([0.,0.])
  if kind=='mass_only_gas':logs=np.log([((1/2.016+1/M)/(1/2.016+1/28.0134))**.2 for M in [39.948,4.002602]])
  mm['parameters']=np.r_[v[:2],logs].tolist();return a.predict(mm,d)
 raise ValueError(kind)
