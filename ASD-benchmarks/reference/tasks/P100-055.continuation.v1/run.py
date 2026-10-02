#!/usr/bin/env python3
"""Frozen, target-free initial-to-aged penetration predictors. No fitting."""
import argparse,json
from pathlib import Path
import numpy as np,pandas as pd
def read_table(p):return pd.read_csv(p,float_precision='round_trip',dtype={'sample_id':str,'group':str})
def basis(kind,d,scale=1.):
 f=d.initial_force.to_numpy();s=d.penetration_index.to_numpy()/600.;w=d.water.to_numpy()/.30;r=d.ratio.to_numpy();sp=d.sp_fraction.to_numpy()/.01;vma=d.vma_fraction.to_numpy()/.001;h=d.initial_shape_change.to_numpy()
 if kind=='mean':return np.ones((len(d),1)),['1'],[0]
 if kind=='identity':return np.empty((len(d),0)),[],[]
 if kind=='gain':return f[:,None],['initial_force'],[0]
 if kind=='affine':return np.c_[np.ones(len(d)),f],['1','initial_force'],[1]
 if kind=='finite_buildup':return np.c_[np.ones(len(d)),f,1-np.exp(-f/scale)],['1','initial_force','1-exp(-initial_force/Fscale)'],[1,2]
 if kind=='water_rebuild':return np.c_[np.ones(len(d)),f,f/w],['1','initial_force','initial_force/w_norm'],[1]
 if kind=='shape_memory':return np.c_[np.ones(len(d)),f,h],['1','initial_force','initial_force_change_over50indices'],[1]
 if kind=='clock_build':return np.c_[np.ones(len(d)),f,s/(s+scale)],['1','initial_force','indexnorm/(indexnorm+scale)'],[1,2]
 if kind=='packing_additive':return np.c_[np.ones(len(d)),f,f/(1+r),f*sp,f*vma],['1','initial_force','initial_force/(1+a/b)','initial_force*SPnorm','initial_force*VMAnorm'],[1]
 if kind=='shape_water':return np.c_[np.ones(len(d)),f,h,h/w],['1','initial_force','initial_change50','initial_change50/w_norm'],[1]
 if kind=='remove_shape':return np.c_[np.ones(len(d)),f],['1','initial_force'],[1]
 raise ValueError(kind)
FEATURES=['ratio','water','sp_fraction','vma_fraction','penetration_index','initial_force','initial_shape_change']
def predict(m,d):
 if m['kind']=='identity':return d.initial_force.to_numpy()
 if m['kind']=='kernel':
  x=(d[m['columns']].to_numpy()-np.array(m['center']))/np.array(m['std']);c=np.array(m['centers']);K=np.exp(-np.maximum((x**2).sum(1)[:,None]+(c**2).sum(1)[None,:]-2*x@c.T,0)/(2*m['scale']**2));v=m['intercept']+K@np.array(m['beta'])
 else:v=basis(m['kind'],d,m['scale'])[0]@np.array(m['beta'])
 return np.maximum(v,0.)

def verify():
 import hashlib
 h=Path(__file__).resolve().parent;m=json.loads((h/'MANIFEST.json').read_text())
 for asset in m['files']:
  f=(h/asset['path']).resolve()
  if not f.is_relative_to(h) or not f.is_file():raise ValueError('Missing or unsafe asset: '+asset['path'])
  if f.stat().st_size!=asset['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Checksum mismatch: '+asset['path'])
 d=read_table(h/'data/inputs.csv.gz');e=read_table(h/'evidence/predictions.csv.gz');models=json.loads((h/'rules.json').read_text())['models']
 for n,m in models.items():
  v=predict(m,d)
  if not np.isfinite(v).all() or not np.allclose(v,e[n].to_numpy(),atol=1e-10,rtol=1e-9):raise ValueError('Frozen prediction mismatch: '+n)
 print(json.dumps({'status':'pass','models':len(models),'rows':len(d),'source_fitting':False}))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--inputs','--input',dest='inputs',type=Path);a.add_argument('--output',type=Path);a.add_argument('--model',default='reference');x=a.parse_args()
 if x.inputs is None and x.output is None:verify()
 else:
  if x.output is None:a.error('--output is required for custom prediction')
  h=Path(__file__).parent;d=read_table(x.inputs or h/'data/inputs.csv.gz')
  required=['sample_id','group']+FEATURES
  if any(c not in d for c in required):raise ValueError('Missing declared input columns')
  if d.sample_id.isna().any() or not d.sample_id.is_unique or d.group.isna().any():raise ValueError('Invalid sample/group identities')
  if not np.isfinite(d[FEATURES].to_numpy(float)).all():raise ValueError('Nonfinite declared inputs')
  m=json.loads((h/'rules.json').read_text())['models'][x.model];o=d[['sample_id','group']].copy();o['prediction']=predict(m,d);o.to_csv(x.output,index=False)
