from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
INPUTS=['npq','rfd','ngrdi','area','tiny','salt','drought','high_stress']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 q=np.arcsinh(d.npq.to_numpy(float));r=d.rfd.to_numpy(float)/(1+np.abs(d.rfd.to_numpy(float)));g=d.ngrdi.to_numpy(float);size=np.log1p(np.maximum(d.area.to_numpy(float),0))/10;t=d.tiny.to_numpy(float);s=d.salt.to_numpy(float);w=d.drought.to_numpy(float);h=d.high_stress.to_numpy(float);o=np.ones(len(d))
 if k=='constant':a=[o]
 elif k=='context':a=[o,t,s,w,h]
 elif k=='quenching':a=[o,1/(1+np.maximum(d.npq.to_numpy(float),0)),t]
 elif k=='recovery':a=[o,r,q,t]
 elif k=='pigment':a=[o,r,q,g,q*g,t]
 elif k=='morphology':a=[o,r,q,g,size,size*q,t]
 elif k=='stress_regime':a=[o,r,q,g,t,s,w,h,q*s,q*w]
 elif k=='pigment_only':a=[o,g,t]
 elif k=='recovery_only':a=[o,r,t]
 else:raise ValueError('Unknown photophysiology family '+k)
 return np.column_stack(a)
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Invalid imaging inputs')
 if model['kind']=='flexible':
  x=(d[INPUTS].to_numpy(float)-model['mean'])/np.asarray(model['scale']);cent=np.asarray(model['centers']);dist=((x[:,None,:]-cent[None,:,:])**2).mean(axis=2);X=np.column_stack([np.ones(len(d)),np.exp(-dist/2)])
 else:X=features(model['kind'],d)
 return expit(X@np.asarray(model['coef']))
def verify():
 for a in json.loads((HERE/'MANIFEST.json').read_text())['assets']:
  p=HERE/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package checksum mismatch '+a['path'])
 d=read_table(HERE/'data/inputs.csv.gz');p=read_table(HERE/'evidence/predictions.csv.gz');r=json.loads((HERE/'rules.json').read_text())
 if d.sample_id.tolist()!=p.sample_id.tolist():raise ValueError('Alignment mismatch')
 for k,m in r['models'].items():
  if not np.allclose(predict(m,d),p[k],rtol=1e-10,atol=1e-10):raise ValueError('Prediction mismatch '+k)
 return {'models':len(r['models']),'rows':len(d),'status':'verified'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
