"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist

def logitp(v):
 p=np.clip(np.asarray(v,float)/100,.0001,.9999);return np.log(p/(1-p))

def raw_features(case,d):
 cols={57:['T_C','shear_s'],60:['distance_mm','resonance_kHz','width_us'],72:['p22_pct','p72_pct','time_h'],83:['T_now','T_lag','T_external','RH_external','hour_sin','hour_cos'],100:['payload_B','last_rtt','mean5_rtt','mean3_rtt','trend_rtt','RSRP','RSRQ']}[case]
 return d[cols].to_numpy(float)

def categories(case,d):
 col={57:'formulation',60:'condition',83:'stream',100:'route'}.get(case);return None if col is None else d[col].to_numpy(str)

def basis(case,kind,d,h,cats):
 n=len(d);one=np.ones(n);x=[];terms=[];base=np.zeros(n);link='identity'
 def add(v,t):x.append(np.asarray(v,float));terms.append(t)
 def per(v,t):
  observed=categories(case,d)
  for cat in cats:add(v*(observed==cat),f'{cat}: {t}')
 if case==57:
  T=d.T_C.to_numpy()+273.15;g=d.shear_s.to_numpy();B=h.get('B',5);a=np.exp(np.clip(B*(1000/T-1000/333.15),-30,30));kind0=kind
  if kind=='mean':a=one
  if kind=='vft':a=np.exp(np.clip(h['B']*(1000/(T-h['T0'])-1000/(333.15-h['T0'])),-30,30))
  if kind=='cross':a/=1+(g*h.get('lam',.1))**h.get('m',1)
  if kind=='curvature':a*=np.exp(h.get('C',1)*(1000/T-1000/333.15)**2)
  if kind in ['carreau','hetero','interaction','synthesis']:
   shape=(1+(g*h.get('lam',.1))**2)**((h.get('n',.5)-1)/2)
   if kind=='interaction':shape=(1+(g*h['lam'])**2)**((h['n']-1+h['k']*(T-333.15)/100)/2)
   a*=shape
  per(a,'thermal/shear shape')
  if kind=='two_activation':per(np.exp(12*(1000/T-1000/333.15)),'second activation channel')
  if kind in ['yield','synthesis']:per(np.exp(B*(1000/T-1000/333.15))/g,'thermal yield / shear')
  if kind=='hetero':per(a*np.log(g/10),'shear log perturbation')
 elif case==60:
  w=d.width_us.to_numpy();f=d.resonance_kHz.to_numpy()/1000;tau=h.get('tau',5);z=1-np.exp(-w/tau)
  if kind=='mean':phi=one
  elif kind=='linear_width':phi=w/10
  elif kind in ['ringup','contact','two_scale','synthesis','spreading']:phi=z
  elif kind=='cycle_collapse':phi=1-np.exp(-f*w/h['cycles'])
  elif kind=='edge_interference':phi=np.maximum(1,np.sqrt(1+np.exp(-2*w/tau)-2*np.exp(-w/tau)*np.cos(2*np.pi*f*w)))
  elif kind=='power':phi=(w/10)**h['p']
  else:raise ValueError(kind)
  if kind=='contact':phi=np.where(d.distance_mm.to_numpy()==0,1-np.exp(-w/h['tau_contact']),phi)
  if kind=='spreading':
   for frequency in sorted(set(d.resonance_kHz)):
    add(phi*(d.resonance_kHz.to_numpy()==frequency)*(d.distance_mm.to_numpy()==0),'contact gain '+str(frequency))
    add(phi*(d.resonance_kHz.to_numpy()==frequency)*np.where(d.distance_mm.to_numpy()>0,1/np.maximum(d.distance_mm.to_numpy(),1),0),'air spreading gain '+str(frequency))
  else:per(phi,'width response')
  if kind=='two_scale':per(1-np.exp(-w/h['tau2']),'second ringup response')
  if kind=='synthesis':per(np.exp(-w/tau)*np.sin(np.pi*f*w)**2,'decaying edge interference')
 elif case==72:
  dt=d.time_h.to_numpy()-72;p=d.p72_pct.to_numpy();s=(logitp(p)-logitp(d.p22_pct))/50;tau=h.get('tau',150)
  if kind=='equilibrium':base=p;b=1-np.exp(-dt/tau);add(b,'approach fraction');add(-p*b,'initial fraction depletion')
  elif kind=='persistence':base=p
  elif kind=='constant_selection':base=logitp(p)+s*dt;link='logit'
  else:
   base=logitp(p);link='logit'
   if kind=='adaptive':
    tau_eff=tau*(.5+p/100);add(s*tau_eff*(1-np.exp(-dt/tau_eff)),'fraction-dependent selection relaxation')
   if kind=='log_equilibrium':add(-logitp(p)*dt/(dt+tau),'log-odds restoring displacement')
   if kind in ['relaxation','combined']:add(s*tau*(1-np.exp(-dt/tau)),'early selection × saturating time')
   if kind=='reversal':add(s*dt,'early selection × elapsed');add(dt**2/(tau*(dt+tau)),'late global selection reversal')
   if kind=='frequency':add(s*dt,'early selection × elapsed');add((p/100-.5)*dt/100,'frequency-dependent selection perturbation')
   if kind=='bounded_rate':add(s*dt/(1+abs(s)*dt),'bounded early selection displacement')
   if kind in ['time_only','combined']:add(dt/(dt+tau),'late log-odds displacement')
 elif case==83:
  a=d.T_external.to_numpy()-d.T_now.to_numpy();memory=d.T_now.to_numpy()-d.T_lag.to_numpy();base=d.T_now.to_numpy()
  if kind=='persistence':pass
  else:
   per(one,'biotic/calibration offset degC')
   if kind in ['asymmetric','synthesis']:add(np.maximum(a,0),'ambient warming');add(np.minimum(a,0),'ambient cooling')
   elif kind=='radiative':add(((d.T_external.to_numpy()+273.15)**4-(d.T_now.to_numpy()+273.15)**4)/(4*303.15**3),'radiative temperature gradient K')
   else:add(a,'ambient gradient')
   if kind in ['regulated','asymmetric','memory','evaporation','synthesis','diurnal','humidity_feedback','daynight','radiative','saturated_cooling']:add(30-d.T_now.to_numpy(),'restoring gradient to30degC reference')
   if kind in ['memory','synthesis','simple_memory','diurnal','humidity_feedback','daynight','radiative','saturated_cooling']:add(memory,'previous1h internal change')
   if kind in ['diurnal','daynight']:add(d.hour_sin.to_numpy(),'daily sine forcing');add(d.hour_cos.to_numpy(),'daily cosine forcing')
   if kind=='daynight':add(a*d.hour_sin.to_numpy(),'daily phase × ambient exchange');add(a*d.hour_cos.to_numpy(),'daily cosine × ambient exchange')
   if kind in ['evaporation','synthesis','humidity_feedback','radiative','saturated_cooling']:
    te=d.T_external.to_numpy();vpd=.6108*np.exp(17.27*te/(te+237.3))*(1-d.RH_external.to_numpy()/100);add(vpd,'external VPD kPa')
    if kind=='saturated_cooling':add((vpd/(h['K']+vpd))*(30-d.T_now.to_numpy()),'saturating VPD × restoring gradient')
    if kind in ['humidity_feedback','radiative']:add(vpd*(30-d.T_now.to_numpy()),'VPD × restoring gradient')
 elif case==100:
  last=d.last_rtt.to_numpy();mean=d.mean5_rtt.to_numpy();short=d.mean3_rtt.to_numpy();base=last
  if kind=='persistence':pass
  elif kind=='rolling':base=mean
  else:
   per(one,'route calibration ms')
   if kind=='static':base=np.zeros(n);add(d.payload_B.to_numpy()/1000,'payload kB')
   else:
    if kind=='bounded_memory':add(20*np.tanh((mean-last)/20),'bounded queue-memory discrepancy ms')
    else:add(mean-last,'queue-memory discrepancy ms')
    if kind=='radio_memory':add((mean-last)*np.maximum(-90-d.RSRP.to_numpy(),0)/10,'weak-RSRP × queue-memory')
    if kind=='refractory':add(20*np.tanh(d.trend_rtt.to_numpy()/20),'bounded preceding RTT change ms')
    if kind in ['two_scale','synthesis']:add(short-mean,'short versus long memory ms')
    if kind in ['radio','synthesis']:add(np.maximum(-90-d.RSRP.to_numpy(),0),'weak-RSRP excess dB');add(np.maximum(-15-d.RSRQ.to_numpy(),0),'poor-RSRQ excess dB')
    if kind=='regime':add(np.maximum(last-h.get('threshold',40),0),'high-latency excess ms');add(d.trend_rtt.to_numpy(),'previous RTT change ms')
    if kind=='serialization':add(d.payload_B.to_numpy()/1000,'payload kB');add((d.payload_B.to_numpy()/1000)*(mean-last),'payload × queue discrepancy')
 return np.column_stack(x)if x else np.empty((n,0)),base,terms,link

def predict(m,d):
 case=int(m['case']);kind=m['kind']
 if kind in ['rbf','residual_rbf']:
  X=raw_features(case,d);mu=np.asarray(m['mean']);scale=np.asarray(m['scale']);x=(X-mu)/scale
  cat=categories(case,d)
  if cat is not None:x=np.column_stack([x]+[(cat==c).astype(float)for c in m['categories']])
  centers=np.asarray(m['centers']);dist=np.maximum((x*x).sum(1)[:,None]+(centers*centers).sum(1)[None,:]-2*x@centers.T,0);y=m['intercept']+np.exp(-dist/(2*m['width']**2))@np.asarray(m['coefficients'])
  if kind=='residual_rbf':y+=predict(m['base_model'],d)
 else:
  x,b,_,link=basis(case,kind,d,m['hyperparameters'],m.get('categories',[]));v=b+x@np.asarray(m['coefficients']);y=100*expit(v)if link=='logit'else v
 if case==72:y=np.clip(y,0,100)
 if case in[57,60,100]:y=np.maximum(y,0)
 return y
