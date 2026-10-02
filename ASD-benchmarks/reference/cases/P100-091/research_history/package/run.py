"""Frozen diagnostic equations. No fitting, target access, or network operations."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str},float_precision='round_trip')
def features(kind,d,params=None):
 a=d.offered_Mbps.to_numpy(float)/500;b=d.achieved_Mbps.to_numpy(float)/500
 if kind=='constant':return np.ones((len(d),1))
 if kind=='offered':return np.c_[np.ones(len(d)),a]
 if kind=='achieved':return np.c_[np.ones(len(d)),b]
 if kind=='dual':return np.c_[np.ones(len(d)),b,a-b]
 if kind=='hinge':return np.c_[np.ones(len(d)),b,np.maximum(a-.4,0)]
 if kind in ['load_cells','monotone_cells']:return np.stack([(d.offered_Mbps.to_numpy()==k).astype(float) for k in [1,10,50,100,200,500]],axis=1)
 if kind=='cell_deficit':return np.c_[features('load_cells',d),a-b]
 if kind=='quadratic_offered':return np.c_[np.ones(len(d)),a,a*a]
 if kind=='deficit_hinge':return np.c_[np.ones(len(d)),b,np.maximum(a-.4,0),np.maximum(a-b,0)]
 raise ValueError('Unknown features '+kind)
def predict(model,d):
 s=json.loads((ROOT/'rules.json').read_text())['models'][model];k=s['kind']
 if k=='queue':
  b=d.achieved_Mbps.to_numpy(float);p=s['coefficients'];y=p[0]+p[1]*b+p[2]/(p[3]-b)
 elif k=='queue_deficit':
  a=d.offered_Mbps.to_numpy(float);b=d.achieved_Mbps.to_numpy(float);p=s['coefficients'];y=p[0]+p[1]*b+p[2]/(p[3]-b)+p[4]*(a-b)/500
 elif k=='rbf':
  x=d[['offered_Mbps','achieved_Mbps']].to_numpy(float)/500;centers=np.array(s['centers']);K=np.exp(-((x[:,None,:]-centers[None,:,:])**2).sum(2)/(2*s['length']**2));y=s['mean']+K@np.array(s['alpha'])
 else:y=features(k,d)@np.array(s['coefficients'])
 return np.maximum(y,0)
def main():
 m=json.loads((ROOT/'MANIFEST.json').read_text())
 for a in m['files']:
  p=ROOT/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Asset mismatch '+a['path'])
 x=read_table(ROOT/'data/inputs.csv.gz');saved=read_table(ROOT/'evidence/predictions.csv.gz');rules=json.loads((ROOT/'rules.json').read_text())
 for name in rules['models']:
  if not np.allclose(predict(name,x),saved[name],rtol=1e-9,atol=1e-9):raise AssertionError(name)
 print(json.dumps({'status':'replayed','models':len(rules['models']),'rows':len(x)}))
if __name__=='__main__':main()
