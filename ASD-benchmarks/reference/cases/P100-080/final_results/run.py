from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
INPUTS=['level','lag10','lag30','mean120','activity','temperature','temperature30','elapsed']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 e=d.level.to_numpy();v=3*(e-d.lag10.to_numpy());r=d.mean120.to_numpy()-e;a=d.activity.to_numpy();T=d.temperature.to_numpy()-d.temperature30.to_numpy();vp=np.maximum(v,0);vn=np.minimum(v,0);sat=v/(1+abs(v))
 return np.column_stack({'relaxation':[r],'damped_drift':[v,r],'activity':[v,r,a],'thermal':[v,r,T],'asymmetry':[vp,vn,r],'saturation':[sat,r,a/(1+np.maximum(e,0))],'activity_memory':[v,r,a,T,a*v],'compact_drift':[v]}[k])
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite causal EDA feature')
 k=model['kind'];b=np.asarray(model['coef']);e=d.level.to_numpy()
 if k=='persistence':return e
 if k=='velocity':return e+3*(e-d.lag10.to_numpy())
 if k=='flexible':
  x=(d[INPUTS].to_numpy()-model['mean'])/model['scale'];z=np.asarray(model['centers']);X=np.column_stack([np.ones(len(d)),np.exp(-((x[:,None,:]-z[None,:,:])**2).mean(axis=2)/2)]);return e+X@b
 return e+features(k,d)@b
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
