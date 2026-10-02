from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
INPUTS=['control','control_median','control_width','quantile','wt','mutant']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d,m=None):
 c=d.control.to_numpy();q=d['quantile'].to_numpy();w=d.control_width.to_numpy();wt=d.wt.to_numpy();mut=d.mutant.to_numpy();L=np.column_stack([1-wt-mut,wt,mut])
 if k=='shift':return L
 if k=='multiplicative':return L*c[:,None]
 if k=='recruitment':return L*expit((q-m['threshold'])/.1)[:,None]
 if k=='location_scale':return np.column_stack([L,L*(w*(q-.5))[:,None]])
 if k=='saturation':return L*(c/(m['K']+abs(c)))[:,None]
 if k=='specificity':return np.column_stack([np.ones(len(d)),wt,wt*(q-.5)])
 if k=='tail_selective':return np.column_stack([L,wt*(q-.5)**3])
 if k=='flexible':
  z=(d[INPUTS].to_numpy()-m['mean'])/m['scale'];cent=np.asarray(m['centers']);return np.column_stack([np.ones(len(d)),np.exp(-((z[:,None,:]-cent[None,:,:])**2).mean(axis=2)/2)])
 raise ValueError('Unknown FACS candidate')
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite paired-well feature')
 if model['kind']=='copy':return d.control.to_numpy()
 return d.control.to_numpy()+features(model['kind'],d,model)@np.asarray(model['coef'])
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
