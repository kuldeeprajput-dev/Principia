from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
INPUTS=['ev_difference','probability','valence','safe_risk','feedback_known','feedback_observed','complete','trial_progress','lag_choice','history_mean','visible_pe','visible_regret','has_history']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 v={c:d[c].to_numpy(float) for c in INPUTS};o=np.ones(len(d));p=v['probability'];H=-p*np.log(p)-(1-p)*np.log(1-p);f=v['feedback_known'];c=v['complete'];base=[o,v['ev_difference'],p-.5,2*v['valence']-1,v['safe_risk']];att=[f,f*H,f*c];inertia=[(v['lag_choice']-.5)*v['has_history'],v['history_mean']-.5,v['trial_progress']]
 if k=='constant':a=[o]
 elif k=='utility':a=base
 elif k=='attitude':a=base+att
 elif k=='learning':a=base+[v['visible_pe'],v['visible_regret'],f*v['trial_progress']]
 elif k=='inertia':a=base+att+inertia
 elif k=='regret':a=base+att+inertia+[v['visible_pe'],v['visible_regret']]
 elif k=='bayes_history':a=base+att+[np.log(v['history_mean']/(1-v['history_mean'])),(v['lag_choice']-.5)*v['has_history']]
 elif k=='feedback_inertia':a=base+att+inertia+[inertia[0]*f,inertia[1]*f]
 elif k=='history_only':a=base+inertia
 elif k=='flexible':a=base+att+inertia+[v['visible_pe'],v['visible_regret'],v['ev_difference']**2,(p-.5)**2,v['ev_difference']*(p-.5),f*inertia[0],f*inertia[1],(2*v['valence']-1)*p,f*p,v['visible_pe']*inertia[0]]
 else:raise ValueError('Unknown cognitive family '+k)
 return np.column_stack(a)
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing or nonfinite choice-time input')
 if ((d.probability<=0)|(d.probability>=1)|(d.history_mean<=0)|(d.history_mean>=1)).any():raise ValueError('Invalid probability input')
 return expit(features(model['kind'],d)@np.asarray(model['coef']))
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
