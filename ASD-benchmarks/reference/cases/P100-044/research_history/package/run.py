from pathlib import Path
import json,hashlib
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent
def read_table(p):return pd.read_csv(p,dtype={'sample_id':str,'group':str},float_precision='round_trip')
def features(kind,d):
 n=d.nodes.to_numpy(float);de=d.max_degree.to_numpy(float);f=d.is_flow.to_numpy(float);l=d.is_linear.to_numpy(float);o=d.moore2_occupancy.to_numpy(float);one=np.ones(len(d))
 if kind=='exp_size':return np.c_[one,np.log(n/25),np.log(de/4),f,l]
 if kind=='exp_occupancy':return np.c_[one,np.log(o),f,l]
 if kind=='exp_combinatorial':return np.c_[one,n*np.log(de)/40,f,l]
 if kind=='sigmoid':return np.c_[one,np.log(n/25),np.log(o),f,l]
 if kind=='formulation_threshold':return np.c_[one,np.log(n/25),np.log(o),f,l,f*np.log(n/25),l*np.log(n/25)]
 if kind=='no_degree':return np.c_[one,np.log(n/25),f,l]
 if kind=='rbf':return np.c_[np.log(n),np.log(de),f,l]
 raise ValueError(kind)
def predict(model,d):
 s=model if isinstance(model,dict)else json.loads((ROOT/'rules.json').read_text())['models'][model];k=s['kind']
 if k=='constant':z=np.full(len(d),s['value'])
 elif k=='form_median':z=np.array([s['values']['flow'if a else'linear'if b else'quadratic']for a,b in zip(d.is_flow,d.is_linear)])
 elif k=='rbf':
  X=(features(k,d)-np.array(s['mean']))/np.array(s['scale']);C=np.array(s['centers']);F=np.c_[np.ones(len(d)),np.exp(-((X[:,None,:]-C[None,:,:])**2).sum(2)/(2*s['length']**2))];z=7200*(F@np.array(s['coefficients']))
 else:
  a=features(k,d)@np.array(s['coefficients'])
  z=7200/(1+np.exp(-np.clip(a,-40,40)))if k in ['sigmoid','formulation_threshold']else np.exp(np.clip(a,-20,20))
 return np.clip(z,0,7200)
def main():
 for a in json.loads((ROOT/'MANIFEST.json').read_text())['files']:
  p=ROOT/a['path']
  if not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package integrity failure: '+a['path'])
 x=read_table(ROOT/'data/inputs.csv.gz');y=read_table(ROOT/'data/observations.csv.gz');p=read_table(ROOT/'evidence/predictions.csv.gz');m=pd.read_csv(ROOT/'evidence/metrics.csv').set_index('model')
 for name,s in json.loads((ROOT/'rules.json').read_text())['models'].items():
  v=predict(s,x);assert np.allclose(v,p[name],rtol=1e-10,atol=1e-9)
  mae=pd.DataFrame({'g':y.group,'e':abs(v-y.target)}).groupby('g').e.mean().mean();assert np.isclose(mae,m.loc[name,'primary_error'],rtol=1e-10,atol=1e-9)
 print('Verified frozen models and grouped metrics.')
if __name__=='__main__':main()
