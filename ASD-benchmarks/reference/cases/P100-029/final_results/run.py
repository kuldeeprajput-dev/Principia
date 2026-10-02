"""Standalone frozen equations; prediction reads declared inputs only."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(c,k,d):
 one=np.ones(len(d))
 if c==29:
  q=d.dose/d.dose_cal;A=d.F5-d.F0;X=[one,d.F0,d.F5,d.F2,d.F1,A*np.log(q),A*(1-1/q),d.dye_NR*A,np.log(q)*d.dye_NR*A]
 elif c==32:
  v=d.p0-d.p20;acc=d.p0-2*d.p20+d.p40;flow=d.di0-d.de0
  if k=='periodic':X=[v,acc]
  elif k=='flow':X=[v,flow,d.di0-d.di20,d.de0-d.de20]
  elif k=='regime':X=[v,acc,flow,v*(flow>0),v*d.trial_FEM,v*d.trial_BH]
  elif k=='shutter':X=[v,acc,d.p0-d.p10,d.p10-d.p30,(d.p0-d.p05)-(d.p20-d.p30),v*d.trial_FEM]
  else:X=[one]+[d[x] for x in ['p0','p05','p10','p20','p30','p40','p50','di0','de0','di20','de20']]+[d.p0*d.trial_FEM,d.p0*d.trial_BH]
 elif c==34:
  x=d.calcium;v=d.low075;u=d.low04
  X=[one,v,u,np.log(x/.75)*v,(1-.75/x)*v,np.log(x/.75)*u,d.mutant*v,d.mutant*np.log(x/.75)*v]
 elif c==76:
  x=d.current/50;s=d.soft;k=d.kd;b=d.cal_last
  X=[one,x,x*x,s,k,s*k,x*s,x*k,x*s*k,b,b*x,d.cal_mean]
 elif c==79:
  x=np.log1p(d.hours/24);b=d.baseline
  X=[one,x,x*x,x*x*x,b,b*x,d.baseline_change,d.age/40]
 elif c==89:
  r=d.reward/2;p=d.probability;a=d.child;m=d.multi;v=d.description;h=d.history_mean-.5;l=d.lag_choice-.5;ev=r*p-1
  if k=='utility':X=[one,ev]
  elif k=='context':X=[one,ev,a,m,v,a*m,ev*a,ev*m]
  elif k=='memory':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,d.has_history*h]
  elif k=='description':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,(p-.5)*v,(p-.5)*a*v]
  elif k=='history_interaction':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,h*ev,h*m,h*a]
  else:X=[one,r,p,r*p,r*r,p*p,a,m,v,a*m,a*v,r*a,p*a,r*m,p*m,r*v,p*v,h,l,h*a,h*m,d.trial_progress]
 else:raise ValueError(c)
 return np.column_stack(X).astype(float)
def predict(m,d):
 c=m['case'];k=m['kind'];p=np.asarray(m.get('coef',[]));one=np.ones(len(d))
 if k=='mean':return one*m['mean']
 if c==29:
  x=d.dose.to_numpy();z=d.dose_cal.to_numpy();b=d.F0.to_numpy();A=(d.F5-d.F0).to_numpy()
  if k=='persistence':return d.F5.to_numpy()
  if k=='linear':return b+A*x/z
  if k=='langmuir':K=p[0];H=lambda q:q/(K+q)
  elif k=='hill':K,n=p;H=lambda q:q**n/(K**n+q**n)
  elif k=='quenching':
   K,q=p;return b+A*(x/(K+x))/(z/(K+z))*np.exp(-q*(x-z))
  elif k=='two_site':K1,K2,w=p;H=lambda q:w*q/(K1+q)+(1-w)*q/(K2+q)
  elif k=='dye_hill':K=np.exp(p[0]+p[1]*d.dye_NR.to_numpy());n=p[2];H=lambda q:q**n/(K**n+q**n)
  elif k in ['local','shrink_local']:
   # Invert low-dose Langmuir ratio only from calibration, not future maximum.
   r=(d.F2-d.F0).to_numpy()/np.maximum(A,1e-8);x2=d.dose2.to_numpy();K=np.clip(x2*z*(1-r)/np.maximum(r*z-x2,1e-8),.01,1000)
   if k=='local':K=K*p[0]
   else:K=np.exp(p[0]*np.log(K)+(1-p[0])*np.log(p[1]))
   H=lambda q:q/(K+q)
  elif k=='threshold':n,K,lag=p;L=lag*z;H=lambda q:np.maximum(q-L,1e-8)**n/(K**n+np.maximum(q-L,1e-8)**n)
  elif k=='flexible':return np.maximum(0,features(c,k,d)@p)
  else:raise ValueError(k)
  return b+A*H(x)/np.maximum(H(z),1e-12)
 if c==32:
  if k=='persistence':return d.p0.to_numpy()
  if k=='tangent':return (d.p0+2*(d.p0-d.p10)).to_numpy()
  if k=='damped':return (d.p0+p[0]*(d.p0-d.p10)).to_numpy()
  if k=='limited':return (d.p0+p[0]*np.tanh((d.p0-d.p20)/p[1])*p[1]).to_numpy()
  if k in ['periodic','flow','regime','shutter']:return d.p0.to_numpy()+features(c,k,d)@p
  return features(c,k,d)@p
 if c==34:
  x=d.calcium.to_numpy();z=.75;v=d.low075.to_numpy();u=d.low04.to_numpy();g=d.mutant.to_numpy()
  if k=='persistence':return v
  if k=='hill4':K=p[0];n=4
  elif k=='genotype_hill':K=np.exp(p[0]+p[1]*g);n=p[2]
  elif k=='local_hill':
   n=p[0];r=np.clip(u/np.maximum(v,1e-8),1e-7,.99999);q=.4**n;s=z**n;K=np.maximum(q*s*(1-r)/np.maximum(r*s-q,1e-12),.000001)**(1/n)
  elif k=='two_pool':
   K1,K2,w=p;H=lambda t:w*t**4/(K1**4+t**4)+(1-w)*t**4/(K2**4+t**4);return v*H(x)/H(z)
  elif k=='genotype_exponent':K=np.exp(p[0]+p[1]*g);n=p[2]+p[3]*g
  elif k=='calibration_blend':
   K,n,w=p;H=lambda t:t**n/(K**n+t**n);glob=v*H(x)/H(z);slope=np.maximum(v-u,0)/.35;local=v+slope*K*(1-np.exp(-(x-z)/K));return (1-w)*glob+w*local
  elif k=='capacity':return np.maximum(0,v+p[0]*(1-np.exp(-(x-z)/p[1]))*(1+p[2]*g))
  elif k=='flexible':return np.maximum(0,features(c,k,d)@p)
  else:raise ValueError(k)
  H=lambda t:t**n/(K**n+t**n);return v*H(x)/H(z)
 if c==76:
  x=d.current.to_numpy();b=d.cal_last.to_numpy();s=d.soft.to_numpy();g=d.kd.to_numpy()
  if k=='persistence':return b
  if k=='rheobase':return np.maximum(0,p[0]*(x-p[1]))
  if k=='condition_threshold':return np.maximum(0,p[0]*(x-p[1]-p[2]*s-p[3]*g-p[4]*s*g))
  if k=='saturation':return b+p[0]*(1-np.exp(-np.maximum(x-10,0)/p[1]))
  if k=='recruitment':return np.maximum(0,(p[0]+p[1]*b+p[2]*d.cal_mean.to_numpy())*np.maximum(x-10,0))
  if k=='block':return b+p[0]*np.maximum(x-10,0)*np.exp(-np.maximum(x-p[1],0)/p[2])
  if k=='condition_gain':return b+np.maximum(0,p[0]+p[1]*s+p[2]*g+p[3]*s*g)*np.maximum(x-10,0)**p[4]
  if k=='calibrated_saturation':return b+(p[0]+p[1]*b)*(1-np.exp(-(x-10)/p[2]))
  if k=='flexible':return np.maximum(0,features(c,k,d)@p)
  raise ValueError(k)
 if c==79:
  t=d.hours.to_numpy();b=d.baseline.to_numpy();v=d.baseline_change.to_numpy()
  if k=='persistence':return b
  if k=='decay':return np.maximum(0,b+p[0]*np.exp(-t/p[1]))
  if k=='bateman':return np.maximum(0,b+p[0]*(np.exp(-t/p[1])-np.exp(-t/p[2])))
  if k=='relative_decay':return np.maximum(0,b+b*p[0]*np.exp(-t/p[1]))
  if k=='two_decay':return np.maximum(0,b+p[0]*np.exp(-t/p[1])+p[2]*np.exp(-t/p[3]))
  if k=='baseline_drift':return np.maximum(0,b+p[0]*np.exp(-t/p[1])+p[2]*v*np.exp(-t/24))
  if k=='lognormal':return np.maximum(0,b+p[0]*np.exp(-.5*(np.log(t/p[1])/p[2])**2))
  if k=='saturating_amplitude':return np.maximum(0,b+p[0]*b/(p[1]+np.maximum(b,0))*np.exp(-t/p[2]))
  if k=='flexible':return np.maximum(0,features(c,k,d)@p)
  raise ValueError(k)
 if c==89:
  if k=='persistence':return np.clip(d.history_mean.to_numpy(),.001,.999)
  if k=='prospect':
   alpha,gamma,beta,bias=p;r=d.reward.to_numpy()/2;prob=d.probability.to_numpy();w=prob**gamma/(prob**gamma+(1-prob)**gamma)**(1/gamma);return expit(beta*(w*r**alpha-1)+bias)
  return expit(features(c,k,d)@p)
 raise ValueError(c)
def main():
 here=Path(__file__).resolve().parent;manifest=json.loads((here/'MANIFEST.json').read_text())
 for a in manifest['assets']:
  p=here/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Integrity failure '+a['path'])
 r=json.loads((here/'rules.json').read_text());d=read_table(here/'data/inputs.csv.gz');saved=read_table(here/'evidence/predictions.csv.gz')
 for k,m in r['models'].items():
  q=predict(m,d)
  if not np.isfinite(q).all() or not np.allclose(q,saved[k],rtol=1e-10,atol=1e-9):raise ValueError('Replay mismatch '+k)
 print('All frozen models reproduce saved predictions',len(d))
if __name__=='__main__':main()
