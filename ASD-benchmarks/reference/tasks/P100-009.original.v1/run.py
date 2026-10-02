from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
INPUTS=['radius','lag05','lag1','mean5','speed','speed1']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 p=d.radius.to_numpy();v=2*(p-d.lag05.to_numpy());a=p-2*d.lag05.to_numpy()+d.lag1.to_numpy();r=d.mean5.to_numpy()-p;u=np.log1p(np.maximum(d.speed.to_numpy(),0));du=u-np.log1p(np.maximum(d.speed1.to_numpy(),0));positive=np.maximum(v,0);negative=np.minimum(v,0)
 return np.column_stack({'relaxation':[r],'inertia':[r,v],'arousal':[r,v,u,du],'asymmetry':[r,positive,negative],'curvature':[r,v,a],'speed_gate':[r,v,v*u]}[k])
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite pupil feature')
 k=model['kind'];b=np.asarray(model['coef']);p=d.radius.to_numpy()
 if k=='persistence':y=p
 elif k=='velocity':y=p+2*(p-d.lag05.to_numpy())
 elif k=='flexible':
  x=(d[INPUTS].to_numpy()-model['mean'])/model['scale'];z=np.asarray(model['centers']);X=np.column_stack([np.ones(len(d)),np.exp(-((x[:,None,:]-z[None,:,:])**2).mean(axis=2)/2)]);y=p+X@b
 else:y=p+features(k,d)@b
 return np.maximum(0,y)
def verify():
 for a in json.loads((HERE/'MANIFEST.json').read_text()).get('assets',json.loads((HERE/'MANIFEST.json').read_text()).get('files',[])):
  p=HERE/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package checksum mismatch '+a['path'])
 d=read_table(HERE/'data/inputs.csv.gz');p=read_table(HERE/'evidence/predictions.csv.gz');r=json.loads((HERE/'rules.json').read_text())
 if d.sample_id.tolist()!=p.sample_id.tolist():raise ValueError('Alignment mismatch')
 for k,m in r['models'].items():
  if not np.allclose(predict(m,d),p[k],rtol=1e-10,atol=1e-10):raise ValueError('Prediction mismatch '+k)
 return {'models':len(r['models']),'rows':len(d),'status':'verified'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
