"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import current as c

def predict(m,d):
 n=m['case'];v=np.array(m['parameters']);k=m['kind']
 if n==27:
  jg=d.massflux_kg_m2_s*d.quality/d.rho_vapor;jl=d.massflux_kg_m2_s*(1-d.quality)/d.rho_liquid;a=jg/(jg+jl);return expit(np.log(jg)-np.log(v[0]*jl+v[1])+(v[2]+v[3]*a)*d.radial_fraction**2).to_numpy()
 if n==60:
  tau=np.where(d.resonance_kHz==110,np.exp(v[0]),np.exp(v[1]));ratio=np.where(d.resonance_kHz==110,v[2],v[3]);phi=c.peak(d.width_us.to_numpy(),d.resonance_kHz.to_numpy()/1000*ratio,tau);return phi*np.array([m['gains'][x]for x in d.condition])
 if n==61:
  base=dict(m['base']);L=np.array(m['lengths']);D=np.array(m['diameters']);idx=(D>.012).astype(int);logkap=v[idx]+np.log(.01/D)+.6*np.log(.14/L);base['parameters']=np.r_[logkap,v[2:4]].tolist();return c.engine(n).predict(base,d)
 if n==72:
  time=(d.time_h.to_numpy()-22)/50;y=np.zeros(len(d))
  for j,q in enumerate(['G','F']):y+=d[q+'72'].to_numpy()*np.exp(-np.maximum(np.log(d[q+'22']/d[q+'72']),0)*(time**v[j]-1))
  return y
 if n==82:
  dd=d.copy();z=d.moisture_change.to_numpy();dd['moisture_change']=np.maximum(-z,0)if k=='drying'else abs(z)if k=='absolute'else np.maximum(z,0);return c.predict(dict(m,kind='rewetting'),dd)
 raise ValueError(n)
