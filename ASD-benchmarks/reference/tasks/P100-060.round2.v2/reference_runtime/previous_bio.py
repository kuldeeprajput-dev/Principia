"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
NUMS={57:['T_C','shear_s','T_previous','eta_previous','eta_first','previous_shear_s','first_shear_s'],60:['distance_mm','resonance_kHz','width_us'],72:['S22','S72','G22','G72','F22','F72','time_h','coculture'],83:['T_now','T_lag','T_external','T_external_lag','RH_external','hour_sin','hour_cos'],100:['payload_B','last_rtt','mean5_rtt','mean3_rtt','trend_rtt','RSRP','RSRQ','last2_rtt','last3_rtt','median5_rtt','std5_rtt']}
CAT={57:'formulation',60:'condition',83:'stream',100:'route'}
from . import original_bio as OLD

def category(case,d):return d[CAT[case]].to_numpy(str)if case in CAT else None

def columns(case,kind,d,cats,h):
 n=len(d);one=np.ones(n);X=[];terms=[];lo=[];hi=[];base=np.zeros(n);link='identity'
 def add(v,t,l=-np.inf,u=np.inf):X.append(np.asarray(v,float));terms.append(t);lo.append(l);hi.append(u)
 def per(v,t,l=-np.inf,u=np.inf):
  cc=category(case,d)
  for c in cats:add(v*(cc==c),c+': '+t,l,u)
 if case==57:
  eta=d.eta_previous.to_numpy();dx=1000/(d.T_C.to_numpy()+273.15)-1000/(d.T_previous.to_numpy()+273.15)
  if kind=='additive_structure':
   dx=1000/(d.T_C.to_numpy()+273.15)-1000/(d.T_previous.to_numpy()+273.15);per(eta*np.exp(h['B']*dx),'thermal transport of previous viscosity',0,np.inf);per(d.eta_first.to_numpy()*(d.T_C.to_numpy()-d.T_previous.to_numpy())/10,'positive structure-history increment',0,np.inf)
  elif kind=='previous':base=eta
  elif kind in ['thermal_history','curved_history','signed_history']:
   base=np.log(np.maximum(eta,1e-9));link='exp';per(dx,'B: 1000K inverse-temperature increment',0 if kind=='thermal_history'else-30,30)
   if kind=='curved_history':per(dx*(d.T_previous.to_numpy()-60)/100,'C: activation changes with preceding temperature',-100,100);add(np.log(d.shear_s/d.previous_shear_s),'actual shear-rate ratio',-10,10)
 elif case==60:
  w=d.width_us.to_numpy();f=d.resonance_kHz.to_numpy()/1000
  if kind=='constant':per(one,'condition constant gain',0,np.inf)
  else:
   tau=np.where(d.resonance_kHz.to_numpy()==110,h.get('tau110',5),h.get('tau500',5));phi=np.maximum(1,np.sqrt(1+np.exp(-2*w/tau)-2*np.exp(-w/tau)*np.cos(2*np.pi*f*w)))
   if kind in ['edge_mixture','bounded_edge']:per(one,'width-independent leading response',0,np.inf);per(phi-1,'damped edge excess response',0,np.inf)
   elif kind=='hybrid_contact':per(np.where(d.distance_mm.to_numpy()==0,phi,1),'contactedge/airleading gain',0,np.inf)
   elif kind=='edge_frequency':per(phi,'frequency-conditional edge gain',0,np.inf)
   elif kind=='global_edge':
    tau=h['tau'];phi=np.maximum(1,np.sqrt(1+np.exp(-2*w/tau)-2*np.exp(-w/tau)*np.cos(2*np.pi*f*w)));per(phi,'shared tau edge gain',0,np.inf)
   else:raise ValueError(kind)
 elif case==72:
  if kind in ['persistence','linear_sugar','first_order','monod','separate_pool','coculture_pool','arrested_pool']:return np.empty((n,0)),np.zeros(n),[],[],[],kind
 elif case==83:
  base=d.T_now.to_numpy()
  if kind!='persistence':
   a=d.T_external.to_numpy()-base;memory=base-d.T_lag.to_numpy();te=d.T_external.to_numpy();vpd=.6108*np.exp(17.27*te/(te+237.3))*(1-d.RH_external.to_numpy()/100)
   per(one,'effective forcing offset degC/h')
   constrained=kind in ['positive_exchange','delayed_exchange','heterogeneous_exchange','positive_no_ambient','positive_no_memory']
   if kind=='heterogeneous_exchange':
    per(a,'positive current ambient exchange',0,1);per(memory,'internal preceding-hour memory',0,.95);per(-vpd,'effective external dryness-linked cooling',0,np.inf)
   else:
    if kind!='positive_no_ambient':add(a,'positive current ambient exchange',0 if constrained else-np.inf,1 if constrained else np.inf)
    if kind!='positive_no_memory':add(memory,'internal preceding-hour memory',0 if constrained else-np.inf,.95 if constrained else np.inf)
    add(-vpd,'effective external dryness-linked cooling',0 if constrained else-np.inf,np.inf)
   add(d.hour_sin,'daily sine forcing');add(d.hour_cos,'daily cosine forcing')
   if kind=='delayed_exchange':add(d.T_external_lag.to_numpy()-base,'positive delayed ambient exchange',0,1)
 elif case==100:
  if kind in ['last','lag2','rolling']:base=d[{'last':'last_rtt','lag2':'last2_rtt','rolling':'mean5_rtt'}[kind]].to_numpy()
  else:
   base=d.last2_rtt.to_numpy();per(one,'route offset ms');add(d.mean5_rtt.to_numpy()-base,'lag2 relaxation to preceding5-probe mean')
   if kind=='lag2_memory':add(d.last_rtt.to_numpy()-d.last3_rtt.to_numpy(),'same-phase recent change')
   elif kind=='bounded_lag2':add(h['clip_ms']*np.tanh((d.last_rtt.to_numpy()-d.last3_rtt.to_numpy())/h['clip_ms']),'bounded same-phase recent change');add(d.std5_rtt.to_numpy(),'trailing jitter');add(np.maximum(-90-d.RSRP.to_numpy(),0),'weak-RSRP excess dB');add(np.maximum(-15-d.RSRQ.to_numpy(),0),'poor-RSRQ excess dB')
   else:raise ValueError(kind)
 return np.column_stack(X)if X else np.empty((n,0)),base,terms,np.asarray(lo),np.asarray(hi),link

def monod_remaining(S22,S72,dt,K,a):
 # Analytic integrated Monod depletion using monotone Newton iteration; never consumes future targets.
 v=np.maximum((S22-S72+K*np.log(np.maximum(S22,1e-9)/np.maximum(S72,1e-9)))/50,0)*a
 c=S72+K*np.log(np.maximum(S72,1e-9))-v*dt
 s=np.maximum(S72*np.exp(np.clip(-v*dt/np.maximum(S72+K,1e-9),-100,0)),1e-9)
 for _ in range(40):
  f=s+K*np.log(np.maximum(s,1e-9))-c;step=f/(1+K/np.maximum(s,1e-9));s=np.maximum(s-step,1e-9)
 return np.minimum(s,np.maximum(S72,1e-9))

def predict(m,d):
 case=m['case'];kind=m['kind']
 if kind=='old':return OLD.predict(m['state'],d)
 if kind=='flex':
  x=d[NUMS[case]].to_numpy(float);x=(x-np.asarray(m['mean']))/np.asarray(m['scale']);cc=category(case,d)
  if cc is not None:x=np.column_stack([x]+[(cc==c).astype(float)for c in m['categories']])
  C=np.asarray(m['centers']);dist=np.maximum((x*x).sum(1)[:,None]+(C*C).sum(1)[None,:]-2*x@C.T,0);y=predict(m['base_model'],d)+m['intercept']+np.exp(-dist/(2*m['h']['width']**2))@np.asarray(m['coef'])
 elif case==72:
  dt=d.time_h.to_numpy()-72;s22=d.S22.to_numpy();s72=d.S72.to_numpy()
  if kind=='persistence':y=s72
  elif kind=='linear_sugar':y=np.maximum(s72-(s22-s72)/50*dt,0)
  elif kind=='first_order':y=s72*np.exp(np.clip(-np.log(np.maximum(s22,1e-9)/np.maximum(s72,1e-9))/50*dt,-100,100))
  elif kind=='monod':y=monod_remaining(s22,s72,dt,m['h']['K'],m['coef'][0])
  elif kind=='coculture_pool':
   idx=d.coculture.to_numpy(int);a=np.asarray(m['coef']);y=monod_remaining(d.G22.to_numpy(),d.G72.to_numpy(),dt,m['h']['K'],a[idx])+monod_remaining(d.F22.to_numpy(),d.F72.to_numpy(),dt,m['h']['K'],a[2+idx])
  elif kind=='arrested_pool':
   dt_eff=m['h']['tau_h']*(1-np.exp(-dt/m['h']['tau_h']));y=monod_remaining(d.G22.to_numpy(),d.G72.to_numpy(),dt_eff,m['h']['K'],m['coef'][0])+monod_remaining(d.F22.to_numpy(),d.F72.to_numpy(),dt_eff,m['h']['K'],m['coef'][1])
  elif kind=='separate_pool':y=monod_remaining(d.G22.to_numpy(),d.G72.to_numpy(),dt,m['h']['K'],m['coef'][0])+monod_remaining(d.F22.to_numpy(),d.F72.to_numpy(),dt,m['h']['K'],m['coef'][1])
  else:raise ValueError(kind)
 else:
  X,b,_,_,_,link=columns(case,kind,d,m['categories'],m['h']);v=b+X@np.asarray(m['coef']);y=np.exp(np.clip(v,-30,30))if link=='exp'else v
 if case in [57,60,72,100]:y=np.maximum(y,0)
 return y
