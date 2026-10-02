from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
HERE=Path(__file__).resolve().parent
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def predict(model,dataframe):
 if isinstance(model,str):model=json.loads((HERE/'rules.json').read_text())['models'][model]
 d=dataframe;p=d.green.to_numpy(float);q=d.red.to_numpy(float);dose=d.dose.to_numpy(float);k=model['kind'];b=np.asarray(model['coef']);L=np.maximum(0,p+q-1);U=np.minimum(p,q);I=p*q
 if not np.isfinite(np.column_stack([p,q,dose])).all() or (p<0).any() or (p>1).any() or (q<0).any() or (q>1).any() or (dose<=0).any():raise ValueError('Invalid fraction/dose inputs')
 if k=='independence':j=I
 elif k=='constant':j=np.repeat(b[0],len(d))
 elif k=='flexible':j=np.column_stack([np.ones(len(d)),p,q,np.log(dose)])@b
 elif k=='competence':j=I+b[0]*(U-I)
 elif k=='odds_ratio':
  lo=L.copy();hi=U.copy();theta=np.exp(b[0])
  for _ in range(55):
   mid=(lo+hi)/2;v=mid*(1-p-q+mid)-theta*(p-mid)*(q-mid);hi=np.where(v>0,mid,hi);lo=np.where(v<=0,mid,lo)
  j=(lo+hi)/2
 elif k=='common_fraction':j=I/b[0]
 elif k=='dose_competence':j=I+expit(b[0]+b[1]*np.log(dose))*(U-I)
 elif k=='competition':j=I+b[0]*(I-L)
 elif k=='dose_odds':
  lo=L.copy();hi=U.copy();theta=np.exp(b[0]+b[1]*np.log(dose))
  for _ in range(55):
   mid=(lo+hi)/2;v=mid*(1-p-q+mid)-theta*(p-mid)*(q-mid);hi=np.where(v>0,mid,hi);lo=np.where(v<=0,mid,lo)
  j=(lo+hi)/2
 elif k=='limiting_locus':j=b[0]*U
 else:raise ValueError('Unknown joint dependence family')
 return 100*np.clip(j,L,U)
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
