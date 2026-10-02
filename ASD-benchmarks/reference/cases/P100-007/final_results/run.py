from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
INPUTS=['force','lag20','lag50','lag100','opposite','opposite50','cycle','cycle_previous','period','speed']
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(k,d):
 F=d.force.to_numpy();v=2*(F-d.lag50.to_numpy());a=F-2*d.lag50.to_numpy()+d.lag100.to_numpy();C=d.cycle.to_numpy();O=d.opposite.to_numpy();vO=2*(O-d.opposite50.to_numpy());contact=np.tanh(F/100);period=d.period.to_numpy();speed=d.speed.to_numpy()
 x={'damped':[v,a],'phase':[C-F,v],'bilateral':[v,a,vO],'stance':[v,a,v*contact,a*contact],'phase_bilateral':[C-F,v,vO],'speed_clock':[C-F,v*speed,vO*speed],'compact_phase':[C-F]}[k]
 return np.column_stack(x)
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe
 if not all(c in d for c in INPUTS) or not np.isfinite(d[INPUTS].to_numpy()).all():raise ValueError('Missing/nonfinite causal force feature')
 k=model['kind'];b=np.asarray(model['coef']);F=d.force.to_numpy()
 if k=='persistence':return F
 if k=='velocity':return F+2*(F-d.lag50.to_numpy())
 if k=='periodic':return d.cycle.to_numpy()
 if k=='flexible':
  x=(d[INPUTS].to_numpy()-model['mean'])/model['scale'];z=np.asarray(model['centers']);X=np.column_stack([np.ones(len(d)),np.exp(-((x[:,None,:]-z[None,:,:])**2).mean(axis=2)/2)]);return F+X@b
 return F+features(k,d)@b
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
