"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import previous_mech
def engine(n):
 if n!=61: raise ValueError("Unsupported dependency")
 return previous_mech

def transform(d,model=None,n=None):
 if model is None: raise ValueError("A frozen transform is required")
 X=d[model['numeric']].to_numpy(float);miss=~np.isfinite(X);X=np.where(miss,np.array(model['median']),X);parts=[X,miss.astype(float)]
 for c,vals in model['categories'].items():parts.append(np.column_stack([(d[c].astype(str)==v).to_numpy(float)for v in vals]))
 return np.column_stack(parts),model

def peak(w,f,tau):
 om=2*np.pi*f;tp=np.minimum(w,np.arctan(om*tau)/om);before=np.exp(-tp/tau)*np.sin(om*tp)
 A=np.exp(-w/tau)*np.cos(om*w)-1;B=np.exp(-w/tau)*np.sin(om*w);phi=np.arctan2(B,A);tt=np.mod(np.arctan(om*tau)-phi,np.pi)/om
 after=np.sqrt(A*A+B*B)*np.exp(-tt/tau)*abs(np.sin(om*tt+phi));return np.maximum.reduce([abs(before),abs(B),after])

def basis(n,d,m):
 one=np.ones(len(d));p=m.get('parameters',[]);k=m['kind']
 if n==53:
  e=d.early.to_numpy();X=np.column_stack([one,d.has_history*np.log(d.prev_y/d.prev_early),d.finding/e-1,1/(1+d.usage),d.left,(d.usage==0).astype(float)]);return X,np.log(e),np.r_[-np.inf,0,-np.inf,0,-np.inf,-np.inf],np.r_[np.inf,1,np.inf,np.inf,np.inf,np.inf]
 if n==57:
  x=1000/(d.T_C+273.15)-1000/(d.T_previous+273.15);r=np.log(d.shear_s/d.previous_shear_s);X=np.column_stack([v*(d.formulation==c)for c in m['categories']for v in [x,r]]);return X,np.log(np.maximum(d.eta_previous,1e-9)),np.tile([0,-1],len(m['categories'])),np.tile([30,0],len(m['categories']))
 if n==71:
  P=d.perm.to_numpy();O=d.od.to_numpy();mp=~np.isfinite(P);mq=~np.isfinite(O)|(O<=0)|mp|(P<=0);P=np.where(mp,m['P_ref'],P);Q=np.zeros(len(d));Q[~mq]=(O[~mq]/m['OD_ref'])**2/(P[~mq]/m['P_ref']);return np.column_stack([one,P,Q,mp,mq]),np.zeros(len(d)),[-np.inf,0,0,-np.inf,-np.inf],[np.inf]*5
 if n==83:
  X=np.column_stack([d.T_now-d.T_lag,d.T_external-d.T_external_lag]+[(d.stream==c).astype(float)for c in m['categories']]+[d.hour_sin,d.hour_cos]);return X,d.T_now.to_numpy(),[0,0]+[-np.inf]*(X.shape[1]-2),[1,1]+[np.inf]*(X.shape[1]-2)
 raise ValueError(n)

def predict(m,d):
 n=m['case'];k=m['kind'];p=np.array(m.get('parameters',[]));one=np.ones(len(d))
 if k=='hgb':
  X,_=transform(d,m['transform']);y=np.full(len(d),m['baseline'])
  for tree in m['trees']:
   ids=np.zeros(len(d),int);active=np.ones(len(d),bool)
   while active.any():
    for ix in np.unique(ids[active]):
     rows=np.flatnonzero(active&(ids==ix));v=tree[int(ix)]
     if v['leaf']:y[rows]+=v['value'];active[rows]=False
     else:ids[rows]=np.where(X[rows,v['feature']]<=v['threshold'],v['left'],v['right'])
  if n==67:return np.exp(np.clip(y,-20,20))
  if n==24:return d.E0_GPa.to_numpy()*np.clip(y,0,1)
  return np.clip(y,0,1)if n==27 else np.maximum(y,0)if n in [53,57,60,61,71,72,73,100]else y
 if n==24:return d.E0_GPa.to_numpy()*np.clip(1-p[0]*d.strain_percent.to_numpy()**p[1]*np.log1p(np.maximum(d.cycle.to_numpy()-20,0)/1000),0,1)
 if n==27:
  jg=d.massflux_kg_m2_s*d.quality/d.rho_vapor;jl=d.massflux_kg_m2_s*(1-d.quality)/d.rho_liquid;return expit(np.log(jg)-np.log(p[0]*jl+p[1])+p[2]*d.radial_fraction**2).to_numpy()
 if n==37:
  y=np.zeros(len(d))
  for i,r in enumerate(['A','B']):
   z=d.router==r;a,b,kk=p[i*3:i*3+3];y[z]=a+b*np.maximum(d.u[z],kk*d.q[z])
  return y
 if n in [53,57,71,83]:
  X,off,_,_=basis(n,d,m);y=off+X@p;return np.exp(np.clip(y,-30,30))if n in [53,57]else np.maximum(y,0)if n==71 else y
 if n==60:
  tau=np.where(d.resonance_kHz==110,np.exp(p[0]),np.exp(p[1]));phi=peak(d.width_us.to_numpy(),d.resonance_kHz.to_numpy()/1000,tau);return phi*np.array([m['gains'][c]for c in d.condition])
 if n==61:
  mm=dict(m['base']);length=np.array(m['lengths']);diam=np.array(m['diameters']);logkap=p[0]+np.log(.01/diam)+.6*np.log(.14/length);mm['parameters']=np.r_[logkap,p[1:3]].tolist();return engine(n).predict(mm,d)
 if n==67:return d.width_m.to_numpy()/np.exp(p[0]*np.log(d.v_near_m_s)+(1-p[0])*np.log(d.v_far_m_s))
 if n==72:
  dt=d.time_h.to_numpy()-72;y=np.zeros(len(d))
  for j,q in enumerate(['G','F']):y+=d[q+'72'].to_numpy()*np.exp(-p[j]*np.maximum(np.log(d[q+'22']/d[q+'72']),0)*(dt/50))
  return y
 if n==73:
  y=np.zeros(len(d))
  for trial,beta in zip(m['categories'],p):
   z=d.trial.astype(str)==trial;fac=np.expm1(beta*np.log(d.hour[z]/8))/(-np.expm1(-beta*np.log(2)));y[z]=d.g8[z]+(d.g8[z]-d.g4[z])*fac
  return np.maximum(0,y)
 if n==82:
  T=(d.t05.to_numpy()-10)/10;mo=d.tsmoisture.to_numpy();mi=~np.isfinite(mo);z=(np.where(mi,25,mo)-25)/20
  f=np.exp(np.clip(p[0]*T+p[1]*z+p[2]*z*z+p[3]*T*z+p[4]*mi+p[5]*np.maximum(d.moisture_change.to_numpy()/20,0),-30,30));a=np.array([m['amplitudes'].get(c,m['fallback'])for c in d.context]);return a*f
 if n==92:
  lam=np.where(d.furniture.to_numpy()==1,p[1],p[0]);r0=d.r0.to_numpy();delta=d.local_channel_power_dB.to_numpy()-r0;return r0+10*np.log10((1-lam)+lam*10**(delta/10))+p[2]+p[3]*d.furniture.to_numpy()
 if n==100:return np.maximum(0,(3*d.last2_rtt.to_numpy()+10*d.mean5_rtt.to_numpy()-3*d.last_rtt.to_numpy()-3*d.last3_rtt.to_numpy())/7)
 raise ValueError(n)
