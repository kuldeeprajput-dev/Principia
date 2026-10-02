"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
from . import original_mech, original_membrane, original_ecology
def mod(n):
 return original_mech if n in (24,27) else original_membrane if n==61 else original_ecology

def predict(m,d):
 n=m['case'];k=m['kind'];v=np.array(m.get('parameters',[]))
 if k=='legacy':return mod(n).predict(m['state'],d)
 if k=='soil_legacy':return mod(n).predict(m['state'],d)
 if k=='mem_legacy':return mod(n).predict(m['state'],d)
 if k=='kernel':
  if n==61 and 'calibration_j0'not in d:
   d=d.copy();d['calibration_j0']=mod(61).baseflux(dict(calibration=m['calibration']),d)
  X=d[m['numeric']].to_numpy(float);X=np.where(np.isfinite(X),X,np.array(m['median']));X=(X-np.array(m['mean']))/np.array(m['scale'])
  for c,cats in m['categories'].items():X=np.column_stack([X]+[(d[c].astype(str)==z).to_numpy(float)for z in cats])
  C=np.array(m['centers']);dist=np.maximum(0,(X*X).sum(1)[:,None]+(C*C).sum(1)[None,:]-2*X@C.T);p=m['intercept']+np.exp(-m['gamma']*dist)@np.array(m['coefficients'])
  if n==24:return d.E0_GPa.to_numpy()*np.clip(p,0,1)
  return np.clip(p,0,1)if n==27 else np.maximum(0,p)
 if n==24:
  z=d.strain_percent.to_numpy()**2*np.log1p(np.maximum(d.cycle.to_numpy()-20,0)/1000);e0=d.E0_GPa.to_numpy()
  if k=='parallel_floor':return e0*(v[1]+(1-v[1])*np.exp(-v[0]*z))
  if k=='load_feedback':return e0*np.sqrt(np.maximum(v[1]**2,1-2*v[0]*z*(e0/40)))
 if n==27:
  a=mod(27).homogeneous(d);jg=d.massflux_kg_m2_s.to_numpy()*d.quality/d.rho_vapor;jl=d.massflux_kg_m2_s.to_numpy()*(1-d.quality)/d.rho_liquid
  if k in ['unit_c0','capillary_drift']:
   if k=='unit_c0':vd=v[0]
   else:
    tau=1-d.saturation_temperature_K.to_numpy()/647.096;sigma=.2358*tau**1.256*(1-.625*tau);vd=v[0]*(9.80665*sigma*(d.rho_liquid-d.rho_vapor)/d.rho_liquid**2)**.25
   c0=1.;b0=v[1];b2=v[2]
  else:c0=v[0];vd=v[1];b0=v[2];b2=v[3]
  drift=np.clip(jg/(c0*(jg+jl)+vd),1e-7,1-1e-7);s=d.radial_fraction.to_numpy();profile=expit(np.log(drift/(1-drift))+b0+b2*s*s)
  if k=='regime_blend':return (1-a**v[4])*drift+a**v[4]*profile
  return profile
 if n==61:
  mm=mod(61);cal=m['calibration'];p0,ex=mm.pstate(dict(calibration=cal),d);x=d.feed_fraction.to_numpy();pr=d.retentate_bar.to_numpy();pp=d.permeate_bar.to_numpy();f=d.normal_flow_L_min.to_numpy()/(60*m.get('normal_molar_volume_L_mol',22.414));area=d.area_m2.to_numpy();idx=d.membrane_index.to_numpy(int);gas=mm.gasidx(d)
  flow_exponent=v[6]if k in ['plugflow_sherwood','plugflow_entrance']else.6;thermal_exponent=.75-.75*flow_exponent if k in ['plugflow_sherwood','plugflow_entrance']else m.get('thermal_exponent',1.75)
  kap=np.exp(v[:4])[idx]*np.exp(np.r_[0,v[4:6]])[gas]*(d.normal_flow_L_min.to_numpy()/5)**flow_exponent*(d.temperature_K.to_numpy()/673.15)**thermal_exponent
  def local(xx,local_kap=None):
   kk=kap if local_kap is None else local_kap
   hi=p0*np.maximum((pr*xx)**ex-pp**ex,0);lo=np.zeros(len(d))
   for _ in range(32):
    jj=(lo+hi)/2
    if k in ['plugflow_stefan','plugflow_sherwood','plugflow_entrance']:surface=np.maximum(1-(1-xx)*np.exp(np.minimum(jj/(kk*pr),50)),pp/pr);partial=pr*surface
    else:partial=np.maximum(pr*xx-jj/kk,pp)
    rhs=p0*np.maximum(partial**ex-pp**ex,0);hi=np.where(jj>rhs,jj,hi);lo=np.where(jj<=rhs,jj,lo)
   return (lo+hi)/2
  if k.startswith('plugflow'):
   q=np.zeros(len(d));segments=m.get('segments',16);equilibrium=f*np.maximum(x-pp/pr,0)/np.maximum(1-pp/pr,1e-12);capacity=f*x if k=='plugflow' else equilibrium
   factors=((np.arange(segments)+.5)/segments)**(-1/3)if k=='plugflow_entrance'else np.ones(segments);factors=factors/factors.mean()
   for i in range(segments):
    kk=kap*factors[i];xx=np.maximum((f*x-q)/np.maximum(f-q,1e-15),pp/pr);j=local(xx,kk);dq=np.minimum(j*area/segments,np.maximum(0,capacity-q));mid=np.maximum((f*x-q-dq/2)/np.maximum(f-q-dq/2,1e-15),pp/pr);q+=np.minimum(local(mid,kk)*area/segments,np.maximum(0,capacity-q))
   return q/area
  hi=np.minimum(p0*np.maximum((pr*x)**ex-pp**ex,0),f*x/area*.999999);lo=np.zeros(len(d))
  for _ in range(40):
   j=(lo+hi)/2;z=np.clip(j*area/f,1e-10,.999999);xb=1+(x-1)*(-np.log1p(-z)/z);rhs=p0*np.maximum(np.maximum(pr*xb-j/kap,pp)**ex-pp**ex,0);hi=np.where(j>rhs,j,hi);lo=np.where(j<=rhs,j,lo)
  return (lo+hi)/2
 if n==73:
  out=np.zeros(len(d));dt=d.hour.to_numpy()-8;g4=d.g4.to_numpy();g8=d.g8.to_numpy()
  for trial,par in m['trial_parameters'].items():
   z=d.trial.astype(str).to_numpy()==trial;a=np.array(par);k1=np.exp(a[0])
   if k=='prefix_gompertz':
    q=np.log(np.maximum(g8[z],1e-6)/np.maximum(g4[z],1e-6));out[z]=g8[z]*np.exp(np.clip(q*(-np.expm1(-k1*dt[z]))/np.expm1(4*k1),-20,20))
   else:
    k2=np.exp(a[1]);w=a[2];f1=-np.expm1(-k1*dt[z])/np.expm1(4*k1);f2=-np.expm1(-k2*dt[z])/np.expm1(4*k2);out[z]=g8[z]+(g8[z]-g4[z])*(w*f1+(1-w)*f2)
  return np.maximum(0,out)
 if n==82:
  T=d.t05.to_numpy();h=1/(10+46.02)-1/(T+46.02)
  if k=='dual_activation':shape=v[2]*np.exp(100*v[0]*h)+(1-v[2])*np.exp(100*v[1]*h)
  elif k=='thermal_history':shape=np.exp(100*v[0]*h-v[1]*(d.past_temperature.to_numpy()-10)/10)
  else:shape=np.exp(100*v[0]*h)
  amp=np.array([m['amplitudes'].get(c,m['site_fallback'].get(s,m['global_fallback']))for c,s in zip(d.context,d.site)]);return amp*shape
 raise ValueError((n,k))
