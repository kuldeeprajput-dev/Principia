"""Frozen curve predictors; no fitting or external dependencies beyond NumPy/Pandas."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent
def read_table(p):return pd.read_csv(p,dtype={'sample_id':str,'group':str},float_precision='round_trip')
def ratio(d,beta):
 t=d.tokens_B.to_numpy(float);a=d.anchor_tokens_B.to_numpy(float);e=d.early_tokens_B.to_numpy(float);beta=np.asarray(beta)
 return np.expm1(-beta*np.log(t/a))/(-np.expm1(-beta*np.log(e/a)))
def features(d):
 return np.c_[np.log(d.tokens_B/d.anchor_tokens_B),np.log(d.params_B),np.log(d.width/d.depth),d.anchor_loss,d.early_loss-d.anchor_loss]
def predict(model,d):
 s=model if isinstance(model,dict)else json.loads((ROOT/'rules.json').read_text())['models'][model];kind=s['kind'];p=s.get('coefficients',[]);y0=d.anchor_loss.to_numpy(float);dy=(d.anchor_loss-d.early_loss).to_numpy(float);z=np.log((d.width/d.depth).to_numpy(float)/32);n=np.log(d.params_B.to_numpy(float)/.5)
 if kind=='persist':y=y0
 elif kind=='log_tangent':y=y0+dy*np.log(d.tokens_B/d.anchor_tokens_B)/np.log(d.anchor_tokens_B/d.early_tokens_B)
 elif kind in ['power','aspect_power','scale_power','aspect_scale','shrunk_power']:
  if kind=='power':b=np.full(len(d),p[0]);c=1
  elif kind=='aspect_power':b=np.exp(p[0]+p[1]*z);c=1
  elif kind=='scale_power':b=np.exp(p[0]+p[1]*n);c=1
  elif kind=='aspect_scale':b=np.exp(p[0]+p[1]*z+p[2]*n);c=1
  else:b=np.full(len(d),p[0]);c=p[1]
  y=y0+c*dy*ratio(d,np.clip(b,.005,3))
 elif kind=='bounded_size':
  b=p[0]+p[1]/(1+d.params_B.to_numpy(float)/p[2]);y=y0+dy*ratio(d,b)
 elif kind=='balanced_geometry':
  b=np.exp(p[0]+p[1]*n+p[2]*abs(z));y=y0+dy*ratio(d,np.clip(b,.005,3))
 elif kind=='two_rate':
  a=p[0];b=p[1];w=p[2];y=y0+dy*(w*ratio(d,a)+(1-w)*ratio(d,b))
 elif kind=='rbf':
  X=(features(d)-np.array(s['mean']))/np.array(s['scale']);C=np.array(s['centers']);F=np.c_[np.ones(len(d)),np.exp(-((X[:,None,:]-C[None,:,:])**2).sum(2)/(2*s['length']**2))]
  y=y0+F@np.array(s['coefficients'])
 else:raise ValueError('Unknown frozen model: '+kind)
 return np.maximum(y,0.)
def main():
 j=json.loads((ROOT/'MANIFEST.json').read_text())
 for a in j['files']:
  p=ROOT/a['path']
  if not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package checksum mismatch: '+a['path'])
 x=read_table(ROOT/'data/inputs.csv.gz');y=read_table(ROOT/'data/observations.csv.gz');r=read_table(ROOT/'evidence/predictions.csv.gz');m=pd.read_csv(ROOT/'evidence/metrics.csv').set_index('model')
 for name,state in json.loads((ROOT/'rules.json').read_text())['models'].items():
  v=predict(state,x);assert np.allclose(v,r[name],rtol=1e-10,atol=1e-10)
  err=pd.DataFrame({'g':y.group,'e':abs(v-y.target)}).groupby('g').e.mean().mean();assert np.isclose(err,m.loc[name,'primary_error'],rtol=1e-10,atol=1e-10)
 print('Verified frozen predictions and metrics.')
if __name__=='__main__':main()
