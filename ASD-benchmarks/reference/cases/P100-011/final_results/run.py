"""Frozen, inspectable numerical equations. Predictors never load observations."""
from pathlib import Path
import json,hashlib
import numpy as np,pandas as pd
from scipy.special import i0e,i1e,expit
C=Path(__file__).resolve().parent

def read_table(p):return pd.read_csv(p,dtype={'sample_id':str,'group':str})
def values(d,k):return d[k].to_numpy(float)
def features(case,kind,d):
 o=np.ones(len(d));v=lambda k:values(d,k)
 if case==2:
  delta=v('lag1')-v('lag2');curv=v('lag1')-2*v('lag2')+v('lag3');slow=v('lag1')-v('median24');noise=np.maximum(v('mad6'),1e-9)
  fs={'drift':[delta],'damping':[slow],'oscillator':[delta,curv],'volatility':[delta/(1+abs(delta)/noise),slow],'multiscale':[(v('lag1')-v('lag6'))/5,slow],'saturated':[noise*np.tanh(delta/noise),noise*np.tanh(slow/noise)]}
  return np.column_stack(fs.get(kind,[delta,curv,slow,v('median6')-v('median24'),v('lag12')-v('lag24'),noise]))
 if case==3:
  d1=v('lag1')-v('median4');trend=v('lag1')-v('lag2');noise=np.maximum(v('mad4'),1e-9)
  fs={'relax':[d1],'drift':[trend],'bands':[d1,v('low1'),v('high1')],'line':[d1,v('line1')],'robust':[noise*np.tanh(d1/noise)],'volatility':[d1/(1+abs(trend)/noise),v('high1')]}
  return np.column_stack(fs.get(kind,[d1,trend,v('low1'),v('high1'),v('line1'),noise]))
 if case==4:return np.column_stack([o,v('recoil'),np.sqrt(np.maximum(v('scalar_activity'),0)),v('jet_activity'),v('jet_n'),v('max_lep_eta'),v('muon_fraction')])
 if case==11:return np.column_stack([np.log(np.maximum(v('offline'),1)),np.log1p(v('accelerators')),np.log1p(v('nodes'))])
 if case==45:
  z=(v('low')-v('background_low'))/1000;lag=(v('low_lag')-v('background_low'))/1000
  return np.column_stack([z,lag,z*z,np.sign(z)*np.sqrt(abs(z)),v('time_s')/100,v('channel_low_keV')/100])
 if case==46:return np.column_stack([np.log(v('density_ratio')),np.log(v('field_ratio')),v('anisotropy_lag')-1,np.log1p(v('density_lag')*v('temperature_lag')/np.maximum(v('field_lag')**2,1e-6))])
 raise ValueError(case)
def base(case,d):
 if case==2:return values(d,'lag1')
 if case==3:return values(d,'median4')
 if case==45:return values(d,'background_high')
 if case==46:return values(d,'temperature_lag')
 if case==11:return values(d,'offline')
 return np.zeros(len(d))
def predict(model,d):
 if isinstance(model,str):model=json.loads((C/'rules.json').read_text())['models'][model]
 case=model['case'];kind=model['kind'];p=np.asarray(model.get('coefficients',[]),float);v=lambda k:values(d,k);b=base(case,d)
 if kind=='constant':y=np.full(len(d),p[0])
 elif kind in['persist','offline','background','median4']:y=b
 elif kind=='rbf':
  X=features(case,'all',d)
  if 'feature_categories' in model:X=np.c_[X,*[(d.workload.astype(str)==cat).to_numpy(float)for cat in model['feature_categories']],*[(d.precision.astype(str)==cat).to_numpy(float)for cat in model['precision_categories']]]
  X=(X-np.array(model['mean']))/np.array(model['scale']);F=np.exp(-((X[:,None,:]-np.array(model['centers'])[None,:,:])**2).sum(2)/(2*model['length']**2));q=np.c_[np.ones(len(d)),F]@p
  y=b+q if case in[2,3,4,45]else b*np.exp(np.clip(q,-5,5))
 elif case in[2,3]:y=b+features(case,kind,d)@p
 elif case==4:
  R=v('recoil');H=v('scalar_activity');J=v('jet_activity');L=np.maximum(H-J,0)
  if kind=='recoil_identity':y=R
  elif kind=='rayleigh':y=p[0]*np.sqrt(H)
  elif kind=='recoil_gain':y=p[0]*R
  elif kind=='quadrature':y=np.sqrt((p[0]*R)**2+p[1]**2*H+p[2]**2)
  else:
   nu=p[0]*R
   if kind=='rician':s2=p[1]**2*H+p[2]**2
   elif kind=='subsystems':s2=p[1]**2*L+p[2]**2*J+p[3]**2
   elif kind=='acceptance':s2=(p[1]**2*H+p[2]**2)*(1+p[3]*v('max_lep_eta')**2+p[4]*v('muon_fraction'))
   else:raise ValueError(kind)
   s2=np.maximum(s2,1e-8);z=nu**2/(4*s2);y=np.sqrt(s2*np.pi/2)*((1+2*z)*i0e(z)+2*z*i1e(z))
 elif case==11:
  N=v('accelerators');Q=v('offline');coef={k:p[i]for i,k in enumerate([] if kind=='utilization' else model.get('categories',[]))};z=np.array([coef.get(str(x),model.get('fallback',0.))for x in d.workload]);offset=len(coef)
  if kind=='utilization':y=Q*expit(p[0])
  elif kind=='workload':y=Q*expit(z)
  elif kind=='parallel':y=Q*expit(z+p[offset]*np.log1p(N))
  elif kind=='capacity':y=Q/(1+np.exp(-z)*Q/np.maximum(N,1)/1e5)
  elif kind=='fixed_overhead':y=Q*expit(z)/(1+np.exp(p[offset])*v('nodes')/np.maximum(N,1))
  elif kind=='precision':y=Q*expit(z+p[offset]*np.array(['4'in str(x)for x in d.precision],float))
  elif kind=='saturating':y=Q*expit(z+p[offset]*np.tanh(np.log1p(N)/3))
  else:raise ValueError(kind)
 elif case==45:
  z=v('low')-v('background_low');lag=v('low_lag')-v('background_low');pos=np.maximum(z,0)
  if kind=='background_ratio':y=v('background_high')*v('low')/v('background_low')
  elif kind=='linear_hardness':y=b+p[0]*z
  elif kind=='saturation':y=b+p[0]*pos/(1+pos/p[1])
  elif kind=='power_hardness':y=b+p[0]*1000*np.sign(z)*abs(z/1000)**p[1]
  elif kind=='hysteresis':y=b+p[0]*z+p[1]*(z-lag)
  elif kind=='energy_response':y=b+p[0]*z*(v('channel_low_keV')/100)**p[1]
  elif kind=='memory':y=b+p[0]*z+p[1]*lag
  elif kind=='decay_hardness':y=b+p[0]*z*np.exp(-p[1]*v('time_s')/100)
  else:raise ValueError(kind)
 elif case==46:
  x=np.log(v('density_ratio'));z=np.log(v('field_ratio'));a=v('anisotropy_lag')-1
  if kind=='cgl':y=b*np.exp(z)
  elif kind=='adiabatic':y=b*np.exp(2*x/3)
  elif kind=='density':y=b*np.exp(np.clip(p[0]*x,-5,5))
  elif kind=='field':y=b*np.exp(np.clip(p[0]*z,-5,5))
  elif kind=='polytropic':y=b*np.exp(np.clip(p[0]*x+p[1]*z,-5,5))
  elif kind=='relaxation':y=b*np.exp(np.clip(p[0]*x+p[1]*z+p[2]*a,-5,5))
  elif kind=='beta_regime':
   beta=0.402670*v('density_lag')*b/np.maximum(v('field_lag')**2,1e-12);weight=beta/(1+beta);y=b*np.exp(np.clip(p[0]*x+p[1]*z+p[2]*weight*x,-5,5))
  elif kind=='saturation':y=b*np.exp(np.clip(p[0]*np.tanh(x)+p[1]*np.tanh(z),-5,5))
  else:raise ValueError(kind)
 else:raise ValueError(case)
 y=np.asarray(y,float)
 if case in[3,4,11,45,46]:y=np.maximum(y,0)
 if not np.isfinite(y).all():raise ValueError('Nonfinite arithmetic')
 return y

def main():
 mp=C/'MANIFEST.json'
 if not mp.is_file():raise ValueError('Required standalone integrity manifest is missing')
 m=json.loads(mp.read_text());assets=m.get('assets',m.get('files',[]));assets=[dict(path=k,sha256=v)for k,v in assets.items()]if isinstance(assets,dict)else assets
 if not assets:raise ValueError('Empty standalone integrity manifest')
 seen=set()
 for a in assets:
  name=a['path'];rel=Path(name)
  if rel.is_absolute()or '..'in rel.parts or name in seen:raise ValueError('Unsafe or duplicate manifest asset')
  seen.add(name);p=C/rel
  if not p.resolve().is_relative_to(C.resolve())or not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Integrity failure '+name)
 rules=json.loads((C/'rules.json').read_text());x=read_table(C/'data/inputs.csv.gz');q=read_table(C/'evidence/predictions.csv.gz')
 for name,s in rules['models'].items():
  if not np.allclose(predict(s,x),q[name],rtol=1e-8,atol=1e-8):raise ValueError('Replaymismatch '+name)
 print('PASS',rules['case_id'],len(x),'rows',len(rules['models']),'models')
if __name__=='__main__':main()
