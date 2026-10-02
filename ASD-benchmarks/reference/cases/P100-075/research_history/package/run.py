from pathlib import Path
import json,hashlib,sys
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d,K=200.):
 x=np.log(d.stiffness_kpa.to_numpy(float)/30);s=d.hss.to_numpy(float);q=d.stiffness_kpa.to_numpy(float)/(K+d.stiffness_kpa.to_numpy(float))-30/(K+30)
 if k=='copy':return np.zeros((len(d),0))
 if k=='log_additive':return np.column_stack([x,s])
 if k=='quadratic':return np.column_stack([x,s,x*s,x*x,x*x*s])
 if k=='saturation':return np.column_stack([q,s])
 if k=='synergy':return np.column_stack([x,s,x*s])
 if k=='mechanical_only':return x[:,None]
 if k=='threshold':return np.column_stack([(d.stiffness_kpa.to_numpy(float)>=200).astype(float),s,(d.stiffness_kpa.to_numpy(float)>=200)*s])
 if k=='shear_only':return s[:,None]
 if k=='saturating_synergy':return np.column_stack([q,s,q*s])
 if k=='calibration_scaling':return np.column_stack([x,s,x*s,(d.calibration.to_numpy(float)-5)*s])
 raise ValueError('Unknown response family '+k)
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 for c in ['stiffness_kpa','hss','calibration']:
  if c not in d or not np.isfinite(d[c]).all():raise ValueError('Invalid declared input '+c)
 if (d.stiffness_kpa<=0).any() or not d.hss.isin([0,1]).all():raise ValueError('Invalid mechanosensing input domain')
 y=d.calibration.to_numpy(float)+features(model['kind'],d,model.get('K',200))@np.asarray(model['coef'])
 return np.maximum(y,0)
def verify():
 for a in json.loads((HERE/'MANIFEST.json').read_text())['assets']:
  p=HERE/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package checksum mismatch: '+a['path'])
 d=read_table(HERE/'data/inputs.csv.gz');p=read_table(HERE/'evidence/predictions.csv.gz');r=json.loads((HERE/'rules.json').read_text())
 if d.sample_id.tolist()!=p.sample_id.tolist():raise ValueError('Prediction alignment mismatch')
 for k,m in r['models'].items():
  if not np.allclose(predict(m,d),p[k],rtol=1e-10,atol=1e-10):raise ValueError('Saved prediction mismatch: '+k)
 return {'models':len(r['models']),'rows':len(d),'status':'verified'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
