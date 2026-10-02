"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist

def offset(d,k):
 if k==53:return d.early.to_numpy(float)
 if k==67:return np.log(d.width_m.to_numpy(float)/d.v_up_m_s.to_numpy(float))
 if k==92:return d.r0.to_numpy(float)
 return np.zeros(len(d))

def restore(v,d,k):
 y=v+offset(d,k)
 return np.exp(np.clip(y,-20,20)) if k==67 else np.maximum(0,y) if k==71 else y

def general_raw(d,k):
 if k==37:
  u=d.u.to_numpy(float);q=d.q.to_numpy(float);l=np.log(d.packet_bytes.to_numpy(float)/1500)
  return np.column_stack([u,q,l,u*u,q*q,u*q,l*l,u*l]),['u','q','log_packet_ratio','u2','q2','u_q','log_packet_ratio2','u_log_packet_ratio'],['router']
 if k==53:cols=['early','finding','gradient_proxy','roughness','usage','left','has_history','prev_y','prev_early','prev_gradient','first_y','mean_past_y','history_gap'];cats=[]
 elif k==67:cols=['width_m','longest_m','v_up_m_s','v_near_m_s','v_far_m_s','orientation_cos2','orientation_dispersion','delta_density_kg_m3'];cats=['particle','family']
 elif k==71:cols=['perm','permittivity_decline','perm_decline_fraction','perm_peak_past','deltaeps','fc','conductivity','cole_r2','od','transmission','reflection','time_h','fed_batch','dperm24','dod24'];cats=[]
 else:cols=['r0','channel_contrast','position_contrast','spatial_contrast','furniture','day','lwa'];cats=['port','channel']
 return d[cols].to_numpy(float),cols,cats

def transform(d,k,s):
 a,_,_=general_raw(d,k);miss=~np.isfinite(a);a=np.where(miss,np.asarray(s['medians']),a);parts=[(a-np.asarray(s['means']))/np.asarray(s['scales']),miss.astype(float)];names=list(s['numeric_columns'])+['missing_'+c for c in s['numeric_columns']]
 for c,values in s['categories'].items():
  parts.append(np.column_stack([(d[c].astype(str)==v).to_numpy(float) for v in values]));names.extend(c+'='+v for v in values)
 return np.column_stack(parts),names

def basis(d,k,cycle,shape,s=None):
 one=np.ones(len(d));s={} if s is None else s;lo=[];hi=[];names=[];extra=np.zeros(len(d))
 if k==37:
  u=d.u.to_numpy(float);q=d.q.to_numpy(float)
  if cycle==1:
   sat=q/(float(shape)+q);raw=np.column_stack([one,u,sat,u*sat]);nm=['baseline_W','byte_cost_W','packet_cost_W','interaction_W']
  else:
   ku,kq=shape;raw=np.column_stack([one,-np.expm1(-u/ku),-np.expm1(-q/kq)]);nm=['baseline_W','bounded_byte_amplitude_W','bounded_packet_amplitude_W']
  parts=[]
  for router in ['A','B']:
   parts.append(raw*(d.router==router).to_numpy(float)[:,None]);names.extend(router+':'+x for x in nm)
  x=np.column_stack(parts);lo=np.zeros(x.shape[1]);hi=np.full(x.shape[1],np.inf)
 elif k==53:
  e=d.early.to_numpy(float);h=d.has_history.to_numpy(float);state=h*(d.prev_y.to_numpy(float)-d.prev_early.to_numpy(float));gate=one
  if cycle==2:gate=np.exp(-abs(e-d.prev_early.to_numpy(float))/(float(shape)*(abs(d.prev_early.to_numpy(float))+.05)))
  parts=[one,state*gate,d.finding.to_numpy(float)-e,1/(1+d.usage.to_numpy(float)),d.left.to_numpy(float),(d.usage.to_numpy()==0).astype(float)]
  names=['offset_Nm','retained_engagement_fraction','finding_to_early_fraction','reuse_amplitude_Nm','left_offset_Nm','virgin_offset_Nm']
  if cycle==2:parts.append(h*(d.gradient_proxy.to_numpy(float)-d.prev_gradient.to_numpy(float)));names.append('gradient_innovation_fraction')
  x=np.column_stack(parts);lo=np.full(x.shape[1],-np.inf);hi=np.full(x.shape[1],np.inf);lo[1]=0;hi[1]=1;lo[3]=0
 elif k==67:
  if cycle==1:
   ri=9.81*np.maximum(0,d.delta_density_kg_m3.to_numpy(float))/1000*d.width_m.to_numpy(float)/(d.v_up_m_s.to_numpy(float)**2)
   x=np.column_stack([np.log1p(ri),np.log1p(d.width_m.to_numpy(float)/d.longest_m.to_numpy(float))]);names=['density_energy_response','relative_interface_size_response']
  else:
   slowdown=np.maximum(0,-np.log(d.v_near_m_s.to_numpy(float)/d.v_far_m_s.to_numpy(float)));x=np.column_stack([slowdown,d.orientation_dispersion.to_numpy(float)]);names=['upstream_slowdown_response','orientation_dispersion_response']
  lo=np.zeros(x.shape[1]);hi=np.full(x.shape[1],np.inf)
 elif k==71:
  if not s:
   def med(c):
    a=d[c].to_numpy(float);a=a[np.isfinite(a)&(a>0)];return float(np.median(a)) if len(a) else 1.
   s={'perm_median':med('perm'),'fc_median':med('fc'),'conductivity_median':med('conductivity')}
  p=d.perm.to_numpy(float);mp=~np.isfinite(p);p=np.where(mp,s['perm_median'],p)
  if cycle==1:
   decay=np.clip(d.perm_decline_fraction.to_numpy(float),0,1);decay=np.where(np.isfinite(decay),decay,0);x=np.column_stack([one,p*np.exp(-float(shape)*decay),mp]);names=['offset_million_ml','permittivity_slope','missing_perm_offset'];lo=np.array([-np.inf,0,-np.inf]);hi=np.full(3,np.inf)
  else:
   de=d.deltaeps.to_numpy(float);fc=d.fc.to_numpy(float);co=d.conductivity.to_numpy(float);ok=np.isfinite(de)&np.isfinite(fc)&np.isfinite(co)&(fc>0)&(co>0)
   q=np.full(len(d),np.nan);q[ok]=de[ok]*((fc[ok]/s['fc_median'])/(co[ok]/s['conductivity_median']))**float(shape)
   if 'q_median' not in s:s['q_median']=float(np.median(q[np.isfinite(q)])) if np.isfinite(q).any() else 0.
   mq=~np.isfinite(q);q=np.where(mq,s['q_median'],q);x=np.column_stack([one,p,q,mp,mq]);names=['offset_million_ml','permittivity_slope','positive_spectral_slope','missing_perm_offset','missing_Q_offset'];lo=np.array([-np.inf,0,0,-np.inf,-np.inf]);hi=np.full(5,np.inf)
 else:
  f=d.furniture.to_numpy(float)
  if cycle==1:
   lam=float(shape);mix=10*np.log10((1-lam)*10**(d.r0.to_numpy(float)/10)+lam*10**(d.global_power_reference.to_numpy(float)/10));extra=mix-d.r0.to_numpy(float);x=np.column_stack([one,f]);names=['offset_dB','furniture_offset_dB'];lo=np.full(2,-np.inf);hi=np.full(2,np.inf)
  else:
   c=np.tanh(d.channel_contrast.to_numpy(float)/float(shape));p=np.tanh(d.position_contrast.to_numpy(float)/float(shape));x=np.column_stack([one,f,(1-f)*c,f*c,(1-f)*p,f*p]);names=['offset_dB','furniture_offset_dB','channel_unfurnished_dB','channel_furnished_dB','position_unfurnished_dB','position_furnished_dB'];lo=np.full(6,-np.inf);hi=np.r_[np.inf,np.inf,np.zeros(4)]
 return x,extra,names,lo,hi,s

def predict(model,d):
 k=model['case_id'];kind=model['kind']
 if kind=='zero':v=np.zeros(len(d))
 elif kind.startswith('cycle') or kind.startswith('unconstrained'):
  x,extra,*_=basis(d,k,int(kind[-1]),model['shape'],dict(model['state']));v=x@np.asarray(model['beta'])+extra
 else:
  x,_=transform(d,k,model['transform'])
  if kind=='linear':v=np.column_stack([np.ones(len(x)),x[:,model['take']]])@np.asarray(model['beta'])
  elif kind=='rbf':
   c=np.asarray(model['centers']);dist=np.sum((x[:,None,:]-c[None,:,:])**2,axis=2);v=np.exp(-model['gamma']*dist)@np.asarray(model['dual'])
  else:
   v=np.full(len(d),model['baseline'])
   for tree in model['trees']:
    nodes=np.zeros(len(d),int);pending=np.ones(len(d),bool)
    while pending.any():
     for node_id in np.unique(nodes[pending]):
      rows=np.flatnonzero(pending&(nodes==node_id));node=tree[int(node_id)]
      if node['leaf']:v[rows]+=node['value'];pending[rows]=False
      else:
       z=x[rows,node['feature']];left=np.where(np.isnan(z),node['missing_left'],z<=node['threshold']);nodes[rows]=np.where(left,node['left'],node['right'])
 return restore(v,d,k)
