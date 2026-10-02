"""Portable frozen scientific predictors. No fitting, observation reads or network."""
from pathlib import Path
import argparse,json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit,ndtr

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def design(k,x):
 if k=='flex6':
  u=x.rabi_MHz.to_numpy()/5;v=x.detuning_MHz.to_numpy()/60
  return np.column_stack([np.ones(len(x)),u,u*u,u**3,v,v*v,v**3,u*v,u*v*v,u*u*v,v**4])
 if k=='flex22':
  v=x.voltage_V.to_numpy();b=x.bromine_rich.to_numpy();A=np.column_stack([np.ones(len(x)),v,v*v,v**3]+[np.maximum(v-t,0)**3 for t in [.2,.4,.6,.8]])
  return np.column_stack([A*(1-b[:,None]),A*b[:,None]])
 if k=='flex26':
  t=x.elapsed_min.to_numpy()/1000;a=x.anchor_selectivity_pct.to_numpy()/100;s=x.prefix_slope_pct_min.to_numpy()*100;g=x.ag_wt_pct.to_numpy()/20
  return np.column_stack([np.ones(len(x)),a,t,t*t,s*t,s*t*t,g*t])
 if k=='flex30':
  u=np.log(x.speed_mm_s.to_numpy());a=x.boundary_cof.to_numpy();b=x.highspeed_cof.to_numpy();return np.column_stack([np.ones(len(x)),a,b,u,u*u,a*u,a*u*u])
 if k=='flex63':
  f=x.frequency_GHz.to_numpy()-7;b=(x.field_T.to_numpy()-.1702)*100;t=(x.termination_K.to_numpy()-293)/200
  return np.column_stack([np.ones(len(x)),t,f,b,f*f,b*b,f*b,t*f,t*b,t*f*f,t*b*b])
 if k=='flex65':
  f=np.log10(x.frequency_Hz.to_numpy())-4;r=(x.injection_dB.to_numpy()+20)/10
  return np.column_stack([np.ones(len(x)),f,f*f,f**3,r,r*f,r*f*f])
 raise ValueError(k)

def predict(model,x):
 k=model['kind'];p=np.asarray(model.get('parameters',[]),float)
 if k=='constant':return np.full(len(x),p[0])
 if k.startswith('flex'):return design(k,x)@p
 if k.startswith('atom'):
  v=x.detuning_MHz.to_numpy();u=x.rabi_MHz.to_numpy();L=lambda w:1/(1+((v-p[0])/w)**2)
  if k=='atom_domain':return p[1]+p[2]*u+(p[3]+p[4]*u)*L(np.sqrt(p[5]**2+(p[6]*u)**2))
  if k=='atom_saturatingline':return p[1]+p[2]*u/(1+u/p[7])+p[3]*(p[4]-u)/(1+u/p[8])*L(np.sqrt(p[5]**2+(p[6]*u)**2))
  if k=='atom_flip':return p[1]+p[2]*u+p[3]*(p[4]-u)*L(np.sqrt(p[5]**2+(p[6]*u)**2))
  if k in ['atom_double','atom_asym','atom_saturate','atom_equalwidth','atom_quadbg','atom_fixedcenter','atom_powerwidth']:
   bg=p[1]+p[2]*u; amp=p[3]*u/(1+u/p[4]);wide=p[5]+p[6]*u;narrow=p[7]+p[8]*u
   
   if k=='atom_powerwidth':wide=np.sqrt(p[5]**2+(p[6]*u)**2);narrow=np.sqrt(p[7]**2+(p[8]*u)**2)
   y=bg+amp*L(wide)-p[9]*u*u/(p[10]**2+u*u)*L(narrow)
   if k=='atom_asym':y+=p[11]*u*((v-p[0])/wide)*L(wide)
   if k=='atom_saturate':y+=p[11]*u*u/(1+u*u)
   if k=='atom_equalwidth':y=bg+amp*L(wide)-p[9]*u*u/(p[10]**2+u*u)*L(wide/2)
   if k=='atom_quadbg':y+=p[11]*u*u
   return y
 if k=='mem_shared':
  v=x.voltage_V.to_numpy();b=x.bromine_rich.to_numpy();return p[0]*expit((v-(p[1]+p[2]*b))/p[3])
 if k.startswith('mem'):
  v=x.voltage_V.to_numpy();b=x.bromine_rich.to_numpy().astype(int);theta=p.reshape(2,-1)[b];cap=theta[:,0];vs=theta[:,1];w=theta[:,2]
  if k=='mem_domain':q=expit((v-vs)/w);return cap*q
  if k=='mem_weibull':return cap*(-np.expm1(-np.minimum((v/vs)**w,700)))
  if k=='mem_probit':return cap*ndtr((v-vs)/w)
  if k=='mem_leak':q=expit((v-vs)/w);return (1-q)*theta[:,3]*v+cap*q
  if k=='mem_sclc':q=expit((v-vs)/w);return (1-q)*theta[:,3]*v*v+cap*q
  if k=='mem_voltage':return np.minimum(cap,np.maximum(0,theta[:,3]*(v-vs)))
  if k=='mem_hazard':q=1-np.exp(-np.minimum((np.maximum(v-theta[:,3],0)/vs)**w,700));return cap*q
  if k=='mem_shared':return p[0]*expit((v-(p[1]+p[2]*b))/p[3])
 if k.startswith('cat'):
  t=x.elapsed_min.to_numpy();a=x.anchor_selectivity_pct.to_numpy();s=x.prefix_slope_pct_min.to_numpy();g=x.ag_wt_pct.to_numpy()
  if k=='cat_hold':return a
  if k=='cat_linear':return a+s*t
  if k=='cat_relaxdrift':return a+s*p[0]*(-np.expm1(-t/p[0]))+p[1]*t
  if k=='cat_relax':return a+s*p[0]*(-np.expm1(-t/p[0]))
  if k=='cat_log':return a+s*p[0]*np.log1p(t/p[0])
  if k=='cat_loading':
   tau=p[0]*(g/20)**p[1];return a+s*tau*(-np.expm1(-t/tau))
  if k=='cat_equilibrium':return a+(p[0]+p[1]*np.log1p(g)-a)*(-np.expm1(-t/p[2]))
  if k=='cat_twochannel':return a+s*p[0]*(-np.expm1(-t/p[0]))+p[1]*(-np.expm1(-t/p[2]))
  if k=='cat_shrink':return a+p[1]*s*p[0]*(-np.expm1(-t/p[0]))
  if k=='cat_rational':return a+s*t/(1+t/p[0])
  if k=='cat_power':return a+p[1]*s*t/(1+(t/p[0])**p[2])
 if k.startswith('trib'):
  v=x.speed_mm_s.to_numpy();a=x.boundary_cof.to_numpy();b=x.highspeed_cof.to_numpy();c=x.concentration_wt_pct.to_numpy()
  if k=='trib_linearlog':w=(np.log(500)-np.log(v))/(np.log(500)-np.log(.2));return b+(a-b)*w
  vs=p[0];shape=p[1] if len(p)>1 else 1
  if k=='trib_concentration':vs=vs*np.exp(p[2]*c/5)
  f=lambda q:np.exp(-(q/vs)**shape) if k in ['trib_domain','trib_poisson'] else 1/(1+(q/vs)**shape)
  if k=='trib_sqrt':f=lambda q:1/(1+np.sqrt(q/vs))
  w=(f(v)-f(500))/(f(.2)-f(500));y=b+(a-b)*w
  if k=='trib_drag':y+=p[2]*(v-.2)*(500-v)/500
  if k=='trib_bump':y+=p[2]*(a-b)*np.log(v/.2)*np.exp(-np.log(v/p[3])**2)
  return y
 if k.startswith('mag'):
  f=x.frequency_GHz.to_numpy();B=x.field_T.to_numpy();T=x.termination_K.to_numpy();dt=(T-293)/200
  if k=='mag_johnson':return 1.380649e-23*50*T*1e18
  # f0+slope field relation is locally identifiable; no independent Ms inference.
  z=(f-(p[0]+p[1]*(B-.1702)))/(p[2]);L=1/(1+z*z);bg=p[3]+p[4]*dt;A=-p[5]*dt
  if k=='mag_domain':return bg+A*L
  if k=='mag_kittel':
   f0=28.3*np.sqrt(B*(B+p[6]));z=(f-f0)/p[2];return bg+A/(1+z*z)
  if k=='mag_asym':return bg+A*(L+p[6]*z*L)
  if k=='mag_field':return bg+A*(1+p[6]*(B-.1702)*100)*L
  if k=='mag_tempwidth':z=(f-(p[0]+p[1]*(B-.1702)))/(p[2]*np.exp(p[6]*dt));return bg+A/(1+z*z)
  if k=='mag_bg':return bg+A*L+p[6]*(f-7)+p[7]*(f-7)**2
  if k=='mag_thermalnonlinear':return bg+(A+p[6]*dt*dt)*L
  if k=='mag_absorption':return bg+A*(2*L-p[6]*L*L)
 if k.startswith('laser'):
  f=x.frequency_Hz.to_numpy();r=10**(x.injection_dB.to_numpy()/10);q=f/1e4
  if k=='laser_domain':S=10**p[0]/r+10**p[1]/q**2
  elif k=='laser_colored':S=10**p[0]/r+10**p[1]/q**p[2]
  elif k=='laser_rolloff':S=10**p[0]/r*(1+(q/p[3])**2)+10**p[1]/q**p[2]
  elif k=='laser_sharedfloor':S=10**p[0]/r+10**p[1]/q**p[2]+10**p[3]
  elif k=='laser_feedback':S=10**p[0]/(r**p[3])+10**p[1]/q**p[2]
  elif k=='laser_crossover':S=10**p[0]/r+10**p[1]/q**p[2]/(1+q/p[3])
  elif k=='laser_twoflicker':S=10**p[0]/r+10**p[1]/q**2+10**p[2]/q
  elif k=='laser_cavity':S=10**p[0]/r*(1+(q/p[3])**2)/(1+(q/p[4])**2)+10**p[1]/q**p[2]
  else:raise ValueError(k)
  return 10*np.log10(np.maximum(S,1e-30))
 raise ValueError('Unknown model '+k)

def verify(root):
 mf=root/'MANIFEST.json'
 if not mf.exists():raise ValueError('Missing package manifest')
 for a in json.loads(mf.read_text())['files']:
  q=root/a['path']
  if Path(a['path']).is_absolute() or '..' in Path(a['path']).parts or not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package asset integrity failure '+a['path'])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--output');a=ap.parse_args();root=Path(__file__).resolve().parent;verify(root);rules=json.loads((root/'rules.json').read_text());x=read_table(a.input or root/'data/inputs.csv.gz')
 if x.sample_id.duplicated().any() or x[['sample_id','group']].isna().any().any():raise ValueError('Invalid identities')
 if not np.isfinite(x[rules['numeric_columns']].to_numpy(float)).all():raise ValueError('Nonfinite predictor')
 out=x[['sample_id','group']].copy()
 for n,m in rules['models'].items():
  out[n]=predict(m,x)
  if not np.isfinite(out[n]).all():raise ValueError('Nonfinite prediction')
 if a.output:out.to_csv(a.output,index=False);return
 saved=read_table(root/'evidence/predictions.csv.gz');obs=read_table(root/'data/observations.csv.gz');mt=pd.read_csv(root/'evidence/metrics.csv').set_index('model')
 if not out[['sample_id','group']].equals(saved[['sample_id','group']]) or not out[['sample_id','group']].equals(obs[['sample_id','group']]):raise ValueError('Alignment mismatch')
 for n in rules['models']:
  if not np.allclose(out[n],saved[n],rtol=1e-9,atol=1e-9):raise ValueError('Prediction replay mismatch '+n)
  err=pd.DataFrame({'g':x.group,'e':abs(out[n]-obs.target)}).groupby('g').e.mean().mean()
  if not np.isclose(err,mt.loc[n,'primary_error'],rtol=1e-9,atol=1e-10):raise ValueError('Metric replay mismatch '+n)
 print(json.dumps({'status':'passed','rows':len(out),'models':len(rules['models'])}))
if __name__=='__main__':main()
