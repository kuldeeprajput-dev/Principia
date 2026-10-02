from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
INPUTS=['fft_bpm','acf_bpm','half_bpm','half_strength','spectral_quality','agreement','motion','ear']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing or nonfinite pulse feature')
 F=d.fft_bpm.to_numpy();A=d.acf_bpm.to_numpy();H=d.half_bpm.to_numpy();Q=d.spectral_quality.to_numpy();S=d.half_strength.to_numpy();D=d.agreement.to_numpy()/60;k=model['kind'];b=np.asarray(model['coef'])
 if k=='constant':y=np.full(len(d),b[0])
 elif k=='fourier':y=F
 elif k=='autocorrelation':y=A
 elif k=='alias':y=F-expit(b[0]+b[1]*(S-.5))*(F-H)
 elif k=='fusion':w=expit(b[0]+b[1]*(Q-.3)+b[2]*D);y=w*F+(1-w)*A
 elif k=='shrinkage':w=expit(b[0]+b[1]*(Q-.3));y=w*F+(1-w)*b[2]
 elif k=='motion_fusion':w=expit(b[0]+b[1]*(Q-.3)+b[2]*D+b[3]*d.motion.to_numpy());y=w*F+(1-w)*A+b[4]*d.ear.to_numpy()
 elif k=='agreement_gate':
  C=np.where(S>=b[0],H,F);y=np.where(np.abs(C-A)<np.abs(F-A),C,F)
 elif k=='consensus_shrink':w=expit(b[0]+b[1]*(Q-.3)-b[2]*D);y=w*(F+A)/2+(1-w)*b[3]
 elif k=='flexible':
  x=(d[INPUTS].to_numpy(float)-model['mean'])/np.asarray(model['scale']);cent=np.asarray(model['centers']);X=np.column_stack([np.ones(len(d)),np.exp(-((x[:,None,:]-cent[None,:,:])**2).mean(axis=2)/2)]);y=X@b
 else:raise ValueError('Unknown pulse estimator')
 return np.clip(y,30,240)
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
