#!/usr/bin/env python3
"""Portable frozen prediction. No source access, history access, target access or fitting."""
from pathlib import Path
import json,argparse,hashlib
import numpy as np,pandas as pd

def read_table(path): return pd.read_csv(path,float_precision="round_trip",dtype={"sample_id":str,"group":str})

def basis(case,kind,d):
 n=len(d);one=np.ones(n)
 if case==86:
  s=d.slope6.to_numpy();clock=d.time_h.to_numpy();c=d.current.to_numpy();off=c
  cols={'trend':[6*s],'multi':[one,6*d.slope1,6*d.slope3,6*s,6*d.slope12],'curvature':[6*s,36*d.past_acc6],'phase':[one,6*s,6*s*(clock-100)/100,6*s*np.exp(-clock/100)],'memory':[one,6*d.ewma3,6*d.ewma6],'ar':[one,6*s,6*d.slope3,6*d.slope12,c/5000,clock/100,6*s*c/5000],'asymmetry':[one,6*s,6*np.maximum(s,0),6*d.slope3]}
  names={'trend':['6*slope6'],'multi':['intercept','6*slope1','6*slope3','6*slope6','6*slope12'],'curvature':['6*slope6','36*past_acc6'],'phase':['intercept','6*slope6','6*slope6*(time_h-100)/100','6*slope6*exp(-time_h/100)'],'memory':['intercept','6*ewma3','6*ewma6'],'ar':['intercept','6*slope6','6*slope3','6*slope12','current/5000','time_h/100','6*slope6*current/5000'],'asymmetry':['intercept','6*slope6','6*max(slope6,0)','6*slope3']}
 elif case==78:
  t=d.time_h.to_numpy()/24;l=d.initial_logCFU.to_numpy();off=np.zeros(n)
  cols={'clock':[one,t],'burden':[one,t,l-7],'burden_clock':[one,t,(l-7)*(1-t)],'quadratic':[one,t,t*t,l-7],'capacity':[t,t*(7-l)],'shrink':[one,t,(l-7)/(1+.25)]};names={k:[f'basis{j}' for j in range(len(v))] for k,v in cols.items()}
  if kind=='capacity':off=l
 elif case==96:
  s=d.speed.to_numpy();a=d.past_acc.to_numpy();rel=d.relative_speed.to_numpy();off=s
  cols={'acceleration':[a],'leader':[rel],'acc_leader':[a,rel],'gap_brake':[a,rel,np.minimum(d.gap.to_numpy()/2-1,0)],'reverse':[a,d.reverse_relative_speed.to_numpy()],'shuffle':[a,d.shuffle_relative_speed.to_numpy()],'lateral':[a,rel*np.exp(-d.lateral_gap.to_numpy()**2/.5)],'saturating':[a,rel/(1+d.gap.to_numpy()/5)]};names={k:[f'basis{j}' for j in range(len(v))] for k,v in cols.items()}
 return np.column_stack(cols[kind]),names[kind],np.asarray(off)

def predict(model,d):
 case=model['case'];kind=model['kind'];n=len(d)
 if kind=='persistence':return d.current.to_numpy() if case==86 else d.speed.to_numpy() if case==96 else d.initial_logCFU.to_numpy()
 if kind=='endpoint':return np.interp(d.time_h.to_numpy(),model['times'],model['medians'])
 if kind=='hgb':
  X=d[model['features']].to_numpy(float);z=np.full(n,model['base']);
  for nodes in model['trees']:
   ix=np.zeros(n,dtype=int);active=np.ones(n,dtype=bool)
   while active.any():
    for k in np.unique(ix[active]):
     mask=active&(ix==k);node=nodes[k]
     if node['leaf']:z[mask]+=node['value'];active[mask]=False
     else:ix[mask]=np.where(X[mask,node['feature']]<=node['threshold'],node['left'],node['right'])
  return np.maximum(d.current.to_numpy()+z,0)
 if kind=='gap_general':
  q=d[model['leader_feature']].to_numpy()/(1+d.gap.to_numpy()/model['gap_scale_m']);X=np.column_stack([d.past_acc.to_numpy(),q]) if model['acceleration'] else q[:,None];return np.maximum(d.speed.to_numpy()+X@np.asarray(model['coefficients']),0)
 X,_,offset=basis(case,kind,d);return np.maximum(offset+X@np.asarray(model['coefficients']),0) if case in [86,96] else offset+X@np.asarray(model['coefficients'])

def verify(root):
 for f in json.loads((root/'MANIFEST.json').read_text())['files']:
  p=root/f['path']
  if not p.is_file() or p.stat().st_size!=f['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:raise ValueError('Package checksum mismatch: '+f['path'])
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path);p.add_argument('--output',type=Path);p.add_argument('--model',default='reference');a=p.parse_args();root=Path(__file__).parent;verify(root);rules=json.loads((root/'rules.json').read_text());d=read_table(a.input or root/'data/inputs.csv.gz')
 missing=set(rules['numeric_columns'])-set(d)
 if missing:raise ValueError('Missing declared inputs: '+str(sorted(missing)))
 if not np.isfinite(d[rules['numeric_columns']].to_numpy(float)).all():raise ValueError('Malformed/nonfinite inputs')
 if a.input:
  if a.output is None or a.output.exists():raise ValueError('Choose a new output file')
  z=d[['sample_id','group']].copy();z['prediction']=predict(rules['models'][a.model],d);z.to_csv(a.output,index=False);return
 saved=read_table(root/'evidence/predictions.csv.gz');assert d[['sample_id','group']].equals(saved[['sample_id','group']]);diff=0.
 for name,model in rules['models'].items():
  z=predict(model,d);diff=max(diff,float(np.max(abs(z-saved[name]))));assert np.allclose(z,saved[name],rtol=1e-9,atol=1e-8)
 print(json.dumps({'status':'pass','rows':len(d),'models':len(rules['models']),'max_prediction_difference':diff}))
if __name__=='__main__':main()
