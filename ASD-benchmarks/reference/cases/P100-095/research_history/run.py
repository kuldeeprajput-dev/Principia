"""Frozen equations only. No training, target access, network, or research imports."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str,'float_id':str})
def physical(d,c):
 def a(k):return d[k].to_numpy(float)
 z={'one':np.ones(len(d))}
 if c==38:
  z.update(last=a('last'),m5=a('mean5')-a('last'),m20=a('mean20')-a('last'),slope=a('slope'),noise=a('spread'))
  z.update(trendgate=z['slope']/(1+z['noise']),up=np.maximum(z['slope'],0),down=np.minimum(z['slope'],0),revertgate=z['m5']*z['noise']/(1+z['noise']))
 elif c==41:
  F=a('forecast');z.update(F=F,e48=a('error48'),e168=a('error168'),r48=a('error48')/F,r168=a('error168')/F,ramp=a('ramp')/F,weekend=a('weekend'),day48=a('load48'),week168=a('load168'))
  z.update(rweek=z['r48']*z['weekend'],rampup=np.maximum(z['ramp'],0),rampdown=np.minimum(z['ramp'],0),agree=(np.sign(z['r48'])==np.sign(z['r168'])).astype(float)*z['r48'],rsin=z['r48']*np.sin(2*np.pi*a('hour')/24),rcos=z['r48']*np.cos(2*np.pi*a('hour')/24))
 elif c==48:
  T=a('temperature')+273.15;e=a('humidity')/100*6.112*np.exp(17.67*a('temperature')/(a('temperature')+243.5));B=5.670374419e-8*T**4;q=np.clip(a('diffuse')/a('solar'),0,1);v=(e/T)**(1/7)
  z.update(B=B,v=v,clear=1.24*B*v,cloud=q,cloud2=q*q,closure=(1-1.24*v)*q,vc=v*q,sqrt_e=np.sqrt(e),site=a('site_dra'),humidity=a('humidity')/100,T=T/300,clearness=a('solar')/(1361*np.cos(np.deg2rad(a('zenith')))))
  z.update(sitecloud=z['site']*q)
 elif c in [47,94]:
  P=a('pressure');T=a('temperature');S=a('salinity');ts=np.log((298.15-T)/(273.15+T))
  # Garcia & Gordon 1992 Benson/Krause refit, umol/kg. In-situ T used as surface-equilibrium proxy; not formal potential-temperature AOU.
  A=[5.80871,3.20291,4.17887,5.10006,-.0986643,3.80369];B=[-.00701577,-.00770028,-.0113864,-.00951519]
  O=np.exp(sum(v*ts**j for j,v in enumerate(A))+S*sum(v*ts**j for j,v in enumerate(B))-2.75915e-7*S*S)
  z.update(P=P/1000,logP=np.log1p(P/100),T=T,S=S-34,surface=np.exp(-P/100),halocline=np.maximum(S-33,0),TS=T*(S-34),O=O)
  if c==47:
   N=a('nitrate');z.update(N=N,NP=N*z['logP'],Ns=N*z['surface'],float=(d.float_id.astype(str)=='5906486').to_numpy(float),redfield=O-8.625*N)
 elif c==95:
  E=a('energy');U=a('wind');G=a('gradient');ri=9.81/(a('temperature')+273.15)*G*3.3**2/(U**2+.25)
  z.update(E=E,U2=U**2,U3=U**3,E32=np.maximum(E,0)**1.5,G=G,EG=E*G,ri=ri,stable=np.maximum(ri,0),unstable=np.minimum(ri,0),suppressed=U**2/(1+np.maximum(ri,0)),direction=U**2*a('cos_direction'),cross=U**2*a('sin_direction'),vertical2=a('vertical')**2)
 return z

def design(model,d):
 z=physical(d,int(model['case']));features=model.get('features',[]);X=np.column_stack([z[k] for k in features]) if features else np.zeros((len(d),0))
 if model.get('rbf'):
  raw=np.column_stack([z[k] for k in model['rbf']['columns']]);n=(raw-np.array(model['rbf']['mean']))/np.array(model['rbf']['std']);centers=np.array(model['rbf']['centers']);rr=np.exp(-np.sum((n[:,None,:]-centers[None,:,:])**2,axis=2)/(2*model['rbf']['width']**2));X=np.column_stack([np.ones(len(d)),rr])
 offset=z.get(model.get('offset'),np.zeros(len(d)));scale=z.get(model.get('scale'),np.ones(len(d)))
 return X,offset,scale

def predict(model,d):
 X,off,scale=design(model,d)
 if model['type']=='fixed':y=off.copy()
 else:
  correction=X@np.array(model['coef'])
  if 'clip_correction' in model:correction=np.clip(correction,*model['clip_correction'])
  y=off+scale*correction
 if model.get('nonnegative'):y=np.maximum(0,y)
 if not np.isfinite(y).all():raise ValueError('Nonfinite prediction')
 return y

def main():
 root=Path(__file__).resolve().parent;m=json.loads((root/'MANIFEST.json').read_text())
 for a in m['files']:
  p=root/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package integrity mismatch: '+a['path'])
 rules=json.loads((root/'rules.json').read_text());d=read_table(root/'data/inputs.csv.gz');saved=read_table(root/'evidence/predictions.csv.gz');o=read_table(root/'data/observations.csv.gz');report={}
 if not d.sample_id.equals(o.sample_id) or not d.sample_id.equals(saved.sample_id):raise ValueError('Identity mismatch')
 for k,m in rules['models'].items():
  p=predict(m,d);err=float(np.max(np.abs(p-saved[k].to_numpy(float))))
  if not np.allclose(p,saved[k],rtol=1e-11,atol=1e-10):raise ValueError('Saved equation mismatch '+k)
  mae=float(pd.DataFrame({'group':d.group,'e':np.abs(p-o.target)}).groupby('group').e.mean().mean());report[k]={'replay_max_abs':err,'group_MAE':mae}
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
