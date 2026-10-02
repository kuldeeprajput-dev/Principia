"""Frozen numerical equations; targets are never accessed by predict()."""
from pathlib import Path
import json,hashlib,argparse
import numpy as np,pandas as pd
def read_table(p):return pd.read_csv(p,float_precision='round_trip',dtype={'sample_id':str,'group':str})
def shift(m,T):
 if m.get('shift','wlf')=='wlf':
  dt=np.asarray(T)-m.get('Tref',60.);return 10**np.clip(-m['C1']*dt/(m['C2']+dt),-20,20)
 return np.exp(np.clip(m['EA']/8.314462618*(1/(np.asarray(T)+273.15)-1/(m.get('Tref',60.)+273.15)),-45,45))
def gas(m,d):
 P=np.asarray(d.pressure_bar);T=np.asarray(d.temperature_K)
 if m.get('gas','ideal')=='ideal':return P,0.1*2.01588*P/(8.314462618*T)
 table=m['gas_table'];p=np.array(table['pressure_bar']);f=np.zeros(len(d));rho=f.copy()
 for temp,sub in d.groupby('temperature_K',sort=False):
  if float(temp) not in [77.,160.,273.]:raise ValueError('EOS frozen table supports only exactly77,160,273K; no silent temperature truncation')
  ix=d.index.get_indexer(sub.index);s=table['states'][str(int(temp))]
  if np.min(P[ix])<0 or np.max(P[ix])>p[-1]:raise ValueError('EOS pressure outside frozen range')
  f[ix]=np.interp(P[ix],p,s['fugacity_bar']);rho[ix]=np.interp(P[ix],p,s['density_g_cm3'])
 return f,rho
def predict_loss(m,d):
 if m['kind']=='maxwell':
  q=np.asarray(d.omega)[:,None]*shift(m,d.temperature_C)[:,None]*np.array(m['taus'])[None,:]
  return q/(1+q*q)@np.array(m['beta'])
 if m['kind']=='fractional':
  A,tau,alpha=m['params'][:3];z=(1j*np.asarray(d.omega)*shift(m,d.temperature_C)*tau)**alpha
  return np.imag(A*z/(1+z))
 raise ValueError('No physical loss response for this model')
def _predict_storage(m,d):
 k=m['kind'];n=len(d)
 if k=='constant':return np.full(n,m['value'])
 if k=='kernel':
  x=d[m['features']].to_numpy(float);x=np.log(np.maximum(x,1e-12)) if m.get('log_inputs') else x;x=(x-np.array(m['center']))/np.array(m['scale']);c=np.array(m['centers']);K=np.exp(-np.maximum(np.sum(x*x,1)[:,None]+np.sum(c*c,1)[None,:]-2*x@c.T,0)/(2*m['width']**2));z=K@np.array(m['beta'])+m['intercept'];return np.exp(z) if m.get('log_target') else z
 if k=='maxwell':
  if np.any(np.asarray(d.omega)<=0):raise ValueError('Imposed angular frequency must be positive')
  q=np.asarray(d.omega)[:,None]*shift(m,d.temperature_C)[:,None]*np.array(m['taus'])[None,:]
  return np.maximum(q*q/(1+q*q)@np.array(m['beta'])+m.get('plateau',0),1e-12)
 if k=='fractional':
  A,tau,alpha=m['params'][:3];z=(1j*np.asarray(d.omega)*shift(m,d.temperature_C)*tau)**alpha;return np.maximum(np.real(A*z/(1+z))+m.get('plateau',0),1e-12)
 if k=='friction':
  h=np.array(d.H)/.02
  if m.get('newtonian'):h=.5*np.asarray(d.viscosity)*np.asarray(d.speed)/np.asarray(d.load)/.02
  a,b,c,p,q=m['params'][:5];boundary=h**(-p) if m.get('boundary','power')=='power' else 1/(1+h**p)
  if m.get('hydration'):boundary*=np.maximum(np.asarray(d.hydration)/50,.1)**m['params'][5]
  if m.get('pressure'):boundary*=(np.asarray(d.load)/(np.asarray(d.area)/4))**m['params'][5]
  return np.maximum(a+b*boundary+c*h**q,0)
 if k=='adsorption':
  f,rho=gas(m,d);T=np.asarray(d.temperature_K);P=np.asarray(d.pressure_bar);pars=m['params'];A,lb,Q,V=pars[:4];b=np.exp(np.clip(lb+Q*(1/T-1/160),-40,40));z=b*f
  if m.get('sites')==2:
   A2,lb2,Q2=pars[4:7];b2=np.exp(np.clip(lb2+Q2*(1/T-1/160),-40,40));absolute=A*z/(1+z)+A2*b2*f/(1+b2*f)
  else:
   power=pars[4] if m.get('sips') else 1.;occupancy=z**power/(1+z**power)
   absolute=A*occupancy
   if m.get('capacity_temperature'):absolute*=np.exp(pars[4]*(160/T-1))
   if m.get('dilution'):absolute*=1-np.asarray(d.eg_pct)/100
   if m.get('branch'):absolute*=np.exp(pars[4]*np.asarray(d.branch))
  return absolute-100*V*rho
 raise ValueError('Unknown frozen model '+k)
def predict(m,d):
 if m.get('response')=='loss':return predict_loss(m,d)
 return _predict_storage(m,d)
def verify(root):
 for f in json.loads((root/'MANIFEST.json').read_text())['files']:
  p=root/f['path']
  if not p.is_file() or p.stat().st_size!=f['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:raise ValueError('Package checksum mismatch: '+f['path'])
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path);p.add_argument('--output',type=Path);p.add_argument('--model',default='reference');a=p.parse_args();root=Path(__file__).parent;verify(root);spec=json.loads((root/'rules.json').read_text());x=read_table(a.input or root/'data/inputs.csv.gz')
 if a.input:
  if a.output is None or a.output.exists():raise ValueError('Choose a new output file')
  z=x[['sample_id','group']].copy();z['prediction']=predict(spec['models'][a.model],x);z.to_csv(a.output,index=False)
 else:
  saved=read_table(root/'evidence/predictions.csv.gz');delta={}
  for name,m in spec['models'].items():
   z=predict(m,x);delta[name]=float(np.max(abs(z-saved[name])));assert np.allclose(z,saved[name],rtol=1e-9,atol=1e-8)
  print(json.dumps({'status':'pass','models':len(delta),'rows':len(x),'max_difference':max(delta.values())}))
if __name__=='__main__':main()
