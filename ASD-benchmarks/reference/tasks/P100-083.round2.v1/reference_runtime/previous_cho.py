"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist

def basis(d,kind,shape,state=None):
 state={} if state is None else dict(state);one=np.ones(len(d));p,c=shape
 def positive_median(v):
  z=np.asarray(v,float);z=z[np.isfinite(z)&(z>0)];return float(np.median(z)) if len(z) else 1.
 if not state:state={'perm':positive_median(d.perm),'fc':positive_median(d.fc),'conductivity':positive_median(d.conductivity)}
 perm=d.perm.to_numpy(float);mp=~np.isfinite(perm);perm=np.where(mp,state['perm'],perm);decline=d.perm_decline_fraction.to_numpy(float);decline=np.where(np.isfinite(decline),np.clip(decline,0,1),0)
 de=d.deltaeps.to_numpy(float);fc=d.fc.to_numpy(float);co=d.conductivity.to_numpy(float);ok=np.isfinite(de)&np.isfinite(fc)&np.isfinite(co)&(fc>0)&(co>0);q=np.full(len(d),np.nan);q[ok]=de[ok]*((fc[ok]/state['fc'])/(co[ok]/state['conductivity']))**p
 if 'q0' not in state:state['q0']=positive_median(q)
 mq=~np.isfinite(q);q=np.where(mq,state['q0'],q);q=np.maximum(0,q)/state['q0'];v=perm*np.exp(-c*decline)
 x=np.column_stack([one,v,mp,mq]) if kind=='availability' else np.column_stack([one,v,np.log1p(q) if kind!='linear_magnitude' else q,mp,mq])
 names=['offset_million_ml','permittivity_slope','missing_perm_offset','missing_spectrum_offset'] if kind=='availability' else ['offset_million_ml','permittivity_slope','spectral_bias_million_ml','missing_perm_offset','missing_spectrum_offset']
 lo=np.full(x.shape[1],-np.inf);hi=np.full(x.shape[1],np.inf);lo[1]=0
 if kind not in ['availability','unconstrained']:hi[2]=0
 return x,state,names,lo,hi

def predict(m,d):return np.maximum(0,basis(d,m['kind'],m['shape'],m['state'])[0]@np.asarray(m['beta']))
