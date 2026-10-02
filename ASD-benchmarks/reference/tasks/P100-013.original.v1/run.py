"""Portable frozen equations. No fitting, target reads, networking or history imports."""
from pathlib import Path
import json,hashlib,argparse
import numpy as np
import pandas as pd
from scipy.special import expi,expit

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def dose(T,beta,E,logk):
 c=E*1000/8.314462618;low=273.15
 integral=(T*np.exp(-c/T)+c*expi(-c/T))-(low*np.exp(-c/low)+c*expi(-c/low))
 return np.maximum(0,np.exp(logk+c/423.15)*integral/beta)
def geom(x):
 a=x.notch_depth_um.to_numpy()/x.thickness_um.to_numpy();r=1-x.notch_width_um.to_numpy()/x.width_um.to_numpy();f=1.46+24.36*a-47.21*a*a+75.18*a*a*a
 s=x.width_um.to_numpy()*x.thickness_um.to_numpy()**1.5/x.length_um.to_numpy()/f
 return a,r,s

def predict(model, dataframe):
 # Domain checks added after the scientific freeze; no equation or coefficient changed.
 kind=model['kind']
 required=(['temperature_K','heating_rate_K_min'] if kind.startswith('cure_') else ['deflection_mm','calibration_deflection_mm','calibration_force_kN','initial_stiffness_kN_mm','recent_stiffness_kN_mm','lightweight'] if kind.startswith('beam_') else ['width_um','thickness_um','length_um','notch_depth_um','notch_width_um'] if kind.startswith('fracture_') else [])
 for column in required:
     if column not in dataframe or not np.isfinite(pd.to_numeric(dataframe[column],errors='coerce')).all():raise ValueError('Missing or nonfinite required predictor: '+column)
 if not np.isfinite(np.asarray(model.get('parameters',[]),float)).all():raise ValueError('Nonfinite frozen model parameter')
 if kind.startswith('cure_') and ((dataframe.temperature_K<273.15).any() or (dataframe.heating_rate_K_min<=0).any()):raise ValueError('Invalid thermal program domain')
 if kind.startswith('fracture_') and ((dataframe[required]<=0).any().any() or (dataframe.notch_depth_um>=dataframe.thickness_um).any() or (dataframe.notch_width_um>=dataframe.width_um).any()):raise ValueError('Invalid fracture geometry')
 if kind.startswith('beam_') and ((dataframe.calibration_deflection_mm<=0).any() or (dataframe.deflection_mm<=10).any()):raise ValueError('Outside calibrated late-beam task domain')
 x=dataframe;p=np.asarray(model.get('parameters',[]),float);kind=model['kind']
 if kind=='mean':return np.full(len(x),p[0])
 if kind.startswith('cure_'):
  T=x.temperature_K.to_numpy();beta=x.heating_rate_K_min.to_numpy()
  if kind=='cure_logistic':return expit((T-p[0]-p[1]*np.log(beta))/np.exp(p[2]))
  q=dose(T,beta,p[0],p[1])
  if kind=='cure_first':return -np.expm1(-q)
  if kind=='cure_nth':return 1-np.exp(-np.log1p((p[2]-1)*q)/(p[2]-1))
  if kind=='cure_avrami':return -np.expm1(-np.minimum(q**p[2],700))
  if kind=='cure_parallel':return p[4]*(-np.expm1(-q))+(1-p[4])*(-np.expm1(-dose(T,beta,p[2],p[3])))
  if kind=='cure_shared':return p[3]*(-np.expm1(-q))+(1-p[3])*(-np.expm1(-q*np.exp(p[2])))
  if kind=='cure_plateau':return p[3]*(-np.expm1(-np.minimum(q**p[2],700)))
  if kind=='cure_shift':return -np.expm1(-np.minimum((q*np.exp(p[3]*np.log(beta/3)))**p[2],700))
  if kind=='cure_logistic_dose':return 1-(1+q**p[2])**(-p[3])
 if kind.startswith('beam_'):
  d=x.deflection_mm.to_numpy();d0=x.calibration_deflection_mm.to_numpy();f0=x.calibration_force_kN.to_numpy();k=x.initial_stiffness_kN_mm.to_numpy();kr=x.recent_stiffness_kN_mm.to_numpy();m=x.lightweight.to_numpy();u=np.maximum(d-d0,0)
  if kind=='beam_elastic':return f0+k*u
  if kind=='beam_hold':return f0
  if kind=='beam_rational':return f0+k*u/(1+u/p[0])
  if kind=='beam_cap':return np.minimum(f0+k*u,p[0])
  if kind=='beam_softening':return (f0+k*u)*np.exp(-p[0]*u)
  if kind=='beam_material_cap':return np.minimum(f0+k*u,p[0]+p[1]*m)
  if kind=='beam_bilinear':
   cap=p[0]+p[1]*m; elastic=f0+k*u;return np.minimum(elastic,cap)+p[2]*np.maximum(elastic-cap,0)
  if kind=='beam_recent':return f0+np.maximum(0,kr)*u/(1+u/p[0])
  if kind=='beam_power':return f0+k*u/(1+(u/p[0])**p[1])
  if kind=='beam_flexible':
   z=u/20;A=np.column_stack([np.ones(len(x)),f0,k*u,z*z,m,m*z,m*z*z]);return A@p
 if kind.startswith('fracture_'):
  a,r,s=geom(x)
  if kind=='fracture_lefm':return s*p[0]
  if kind=='fracture_bridge':return s*(p[0]+p[1]*r)
  if kind=='fracture_power':return s*p[0]*(1+r)**p[1]
  if kind=='fracture_interaction':return s*(p[0]+p[1]*r+p[2]*r/a)
  if kind=='fracture_notch':return s*(p[0]+p[1]*a)
  if kind=='fracture_regime':return s*(p[0]+p[1]*expit((r-p[2]*a-p[3])/0.02))
  if kind=='fracture_netligament':return s*(p[0]+p[1]*r/(1-a))
  if kind=='fracture_sqrt':return s*(p[0]+p[1]*np.sqrt(r))
  if kind=='fracture_flexible':
   A=np.column_stack([np.ones(len(x)),a,r,a*a,r*r,a*r]);return s*(A@p)
 raise ValueError('Unknown frozen model '+kind)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--input');parser.add_argument('--output');args=parser.parse_args();root=Path(__file__).resolve().parent
 if (root/'MANIFEST.json').exists():
  manifest=json.loads((root/'MANIFEST.json').read_text());items=manifest.get('files',manifest)
  if isinstance(items,dict):items=[{'path':k,'sha256':v} for k,v in items.items()]
  for a in items:
   q=root/a['path']
   if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Package hash mismatch: '+a['path'])
 rules=json.loads((root/'rules.json').read_text());x=read_table(args.input or root/'data/inputs.csv.gz');pred=x[['sample_id','group']].copy()
 for name,m in rules['models'].items():pred[name]=predict(m,x)
 if args.output:
  out=Path(args.output);out.mkdir(parents=True,exist_ok=True);pred.to_csv(out/'predictions.csv',index=False)
 else:
  saved=read_table(root/'evidence/predictions.csv.gz')
  for name in rules['models']:
   if not np.allclose(pred[name],saved[name],rtol=1e-10,atol=1e-10):raise ValueError('Prediction mismatch '+name)
  y=read_table(root/'data/observations.csv.gz');metrics=pd.read_csv(root/'evidence/metrics.csv')
  for name in rules['models']:
   err=pd.DataFrame({'g':x.group,'e':abs(pred[name]-y.target)}).groupby('g').e.mean().mean();expected=metrics.set_index('model').loc[name,'primary_error']
   if not np.isclose(err,expected,rtol=1e-10,atol=1e-10):raise ValueError('Metric mismatch '+name)
  print(json.dumps({'status':'passed','rows':len(x),'models':len(rules['models'])}))
if __name__=='__main__':main()
