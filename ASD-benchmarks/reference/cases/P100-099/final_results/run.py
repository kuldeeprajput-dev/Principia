from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
INPUTS=['level','lag30','lag60','mean300','dispersion','zero_fraction','ventral','condition_group3']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 e=d.level.to_numpy();v=2*(e-d.lag30.to_numpy());r=d.mean300.to_numpy()-e;sd=d.dispersion.to_numpy();z=d.zero_fraction.to_numpy();V=d.ventral.to_numpy();G=d.condition_group3.to_numpy();a=e-2*d.lag30.to_numpy()+d.lag60.to_numpy()
 return np.column_stack({'decay':[e],'relaxation':[r],'inertia':[r,v],'heterogeneity':[r,v,sd,sd*z],'region':[r,v,r*V,v*V],'asymmetry':[r,np.maximum(v,0),np.minimum(v,0)],'curvature':[r,v,a],'condition':[r,v,r*G,v*G]}[k])
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite native-trace feature')
 k=model['kind'];b=np.asarray(model['coef']);e=d.level.to_numpy()
 if k=='persistence':return e
 if k=='velocity':return e+2*(e-d.lag30.to_numpy())
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
