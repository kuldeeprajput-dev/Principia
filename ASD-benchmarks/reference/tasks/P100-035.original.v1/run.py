from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
INPUTS=['log_duration','log_centroid','log_peak','high_share','entropy','flatness','envelope_cv','log_modulation','log_rms','species_code']
FAMILY={'arousal':['log_duration','log_centroid','high_share','envelope_cv'],'tonality':['log_peak','entropy','flatness'],'modulation':['log_duration','envelope_cv','log_modulation'],'recording':['log_rms','log_duration'],'spectrotemporal':['log_duration','log_centroid','entropy','envelope_cv','log_modulation'],'spectral_only':['log_centroid','entropy'],'species_interaction':['log_duration','log_centroid','entropy','envelope_cv']}
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d,m=None):
 species=d.species_code.to_numpy(int);base=np.column_stack([np.ones(len(d))]+[(species==j).astype(float) for j in range(1,7)])
 if k=='constant':return base[:,:1]
 if k=='species':return base
 if k=='flexible':
  z=(d[INPUTS[:-1]].to_numpy()-m['mean'])/m['scale'];c=np.asarray(m['centers']);return np.column_stack([base,np.exp(-((z[:,None,:]-c[None,:,:])**2).mean(axis=2)/2)])
 x=d[FAMILY[k]].to_numpy()
 if k=='species_interaction':x=np.column_stack([x]+[(species==j)*d.log_centroid.to_numpy() for j in range(1,7)])
 return np.column_stack([base,x])
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 if not all(c in dataframe for c in INPUTS) or not np.isfinite(dataframe[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite audio feature')
 return expit(features(model['kind'],dataframe,model)@np.asarray(model['coef']))
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
