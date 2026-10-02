"""Portable frozen equations; no fitting or target access in predict."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(case,kind,x):
 n=len(x);o=np.ones(n)
 if case==74:
  d=x.time_min.to_numpy()-6;s=x.concentration_uM.to_numpy();v=x.calibration_v6.to_numpy();c=x.calibration_curvature.to_numpy();f=x.calibration_F6.to_numpy()
  if kind=='flexible':return np.c_[o,d/60,d*d/3600,s/20,f/200,v/50,c/10,d*v/3000,d*c/600]
  if kind=='slope_gate':return np.c_[d*v,d*c*6]
  if kind=='dose_linear':return np.c_[d*v,d*v*np.log(s)]
 if case==85:
  q=x.eg_consumed_g_L.to_numpy();t=x.elapsed_h.to_numpy();p=x.pH.to_numpy();g=x.glucose_cofeed.to_numpy();a=x.acetate_cofeed.to_numpy()
  if kind=='global_yield':return q[:,None]
  if kind=='ph_yield':return np.c_[q,q*(p-7)]
  if kind=='loss_flux':return np.c_[q,t/100]
  if kind=='composition':return np.c_[q,q*g,q*a]
  if kind=='aging':return np.c_[q,q/(1+t/100)]
  if kind=='acid':return (q/(1+10**(3.83-p)))[:,None]
  if kind=='sqrt_recovery':return np.c_[q,np.sqrt(np.maximum(q,0))]
  if kind=='flexible':return np.c_[o,q/20,t/200,p/7,g,a,q*q/400,q*p/140,t*q/4000]
 if case==87:
  c=x.own_previous.to_numpy();e=x.endowment.to_numpy();peer=x.peer_previous.to_numpy();ep=x.peer_endowment.to_numpy();req=x.required_contribution.to_numpy();s=x.previous_success.to_numpy();lag=x.own_lag2.to_numpy();mu=x.own_history_mean.to_numpy();r=x['round'].to_numpy()
  if kind=='focal':return (e/2-c)[:,None]
  if kind=='reciprocal':return (e*peer/ep-c)[:,None]
  if kind=='coordination':return (req-c)[:,None]
  if kind=='success_gate':return np.c_[(req-c)*(1-s),(e/2-c)*(1-s),(e/2-c)*s]
  if kind=='history':return np.c_[mu-c,(req-c)*(1-s)]
  if kind=='momentum':return np.c_[c-lag,(req-c)*(1-s)]
  if kind=='asymmetric':return np.c_[(req-c)*(1-s),(e/2-c)*s,(req-c)*(1-s)*(e>24),(req-c)*(1-s)*(e<24)]
  if kind=='compact':return ((req-c)*(1-s))[:,None]
  if kind=='flexible':return np.c_[o,c/36,peer/36,lag/36,mu/36,e/36,ep/36,req/36,s,r/20,c*peer/1296,c*c/1296,req*s/36]
 raise ValueError('Unknown features '+kind)
def predict(m,x):
 case=m['case'];k=m['kind'];p=np.asarray(m.get('coef',[]),float)
 if case==74:
  d=x.time_min.to_numpy()-6;s=x.concentration_uM.to_numpy();v=x.calibration_v6.to_numpy();c=x.calibration_curvature.to_numpy();f=x.calibration_F6.to_numpy()
  if k=='persistence':y=f
  elif k=='linear':y=f+v*d
  elif k=='mm':y=p[0]*s/(p[1]+s)*x.time_min.to_numpy()
  elif k=='saturation':y=f+v*p[0]*(-np.expm1(-d/p[0]))
  elif k=='accelerating':y=f+v*d+p[0]*v*(d-p[1]*(-np.expm1(-d/p[1])))
  elif k=='power':y=f+p[0]*v*6*np.expm1(p[1]*np.log1p(d/6))/p[1]
  elif k=='curvature':y=f+v*d+c*p[0]*(d-p[0]*(-np.expm1(-d/p[0])))
  elif k=='dose_saturation':
   tau=np.exp(p[0]+p[1]*np.log(s));y=f+v*tau*(-np.expm1(-d/tau))
  else:y=(0 if k=='flexible' else f)+features(case,k,x)@p
 elif case==85:
  q=x.eg_consumed_g_L.to_numpy()
  if k=='zero':y=np.zeros(len(x))
  elif k=='unit_yield':y=q
  elif k=='stoichiometric':y=q*(76.05/62.07)
  elif k=='saturation':y=p[0]*(-np.expm1(-np.maximum(q,0)*p[1]/p[0]))
  else:y=features(case,k,x)@p
  y=np.maximum(0,y)
 elif case==87:
  c=x.own_previous.to_numpy();e=x.endowment.to_numpy()
  if k=='persistence':y=c
  elif k=='lag2_mean':y=(c+x.own_lag2.to_numpy())/2
  elif k=='half_endowment':y=e/2
  else:y=(0 if k=='flexible' else c)+features(case,k,x)@p
  y=np.clip(y,0,e)
 else:raise ValueError('Unknown case')
 if not np.isfinite(y).all():raise ValueError('Nonfinite prediction')
 return np.asarray(y,float)

def main():
 p=Path(__file__).resolve().parent
 if (p/'MANIFEST.json').exists():
  z=json.loads((p/'MANIFEST.json').read_text());assets=z.get('assets',z.get('files',[]))
  if isinstance(assets,dict):assets=[{'path':k,'sha256':v if isinstance(v,str) else v['sha256']} for k,v in assets.items()]
  for a in assets:
   if hashlib.sha256((p/a['path']).read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Checksum mismatch '+a['path'])
 rules=json.loads((p/'rules.json').read_text());x=read_table(p/'data/inputs.csv.gz');saved=read_table(p/'evidence/predictions.csv.gz')
 for name,m in rules['models'].items():
  y=predict(m,x)
  if not np.allclose(y,saved[name].to_numpy(float),rtol=1e-10,atol=1e-10):raise ValueError('Replay mismatch '+name)
 print(json.dumps({'models_replayed':len(rules['models']),'rows':len(x),'max_tolerance':'1e-10','status':'pass'}))
if __name__=='__main__':main()
