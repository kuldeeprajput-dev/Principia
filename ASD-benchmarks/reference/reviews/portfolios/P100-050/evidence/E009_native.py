from pathlib import Path
import json,hashlib,io,re,zipfile
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent

def sources(data_root):
 m=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
 base=Path(data_root)/m['scenario_id']
 for a in m['assets']:
  rel=Path(a['path'])
  if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe asset path')
  f=base/rel
  if not f.is_file() or f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing/corrupt native asset: '+str(rel))
 return base

def prepare(data_root):
 base=sources(data_root);fn='raw/flume_laser_all_gate_releases.csv';d=pd.read_csv(base/fn);tt=pd.to_numeric(d.iloc[:,0],errors='coerce').to_numpy();rows=[]
 if not np.allclose(np.diff(tt),.001,atol=1e-7):raise ValueError('Unexpected native time grid')
 for j,col in enumerate(d.columns[1:]):
  z=pd.to_numeric(d[col],errors='coerce').to_numpy();group=str(col)
  for k in range(400,len(z)-200,50):
   h=np.mean(z[k-19:k+1]);prev=np.mean(z[k-119:k-99]);prev2=np.mean(z[k-219:k-199]);vals=[z[k+200],z[k],h,prev,prev2,np.median(z[k-19:k+1])]
   if not np.isfinite(vals).all():continue
   rows.append(dict(sample_id=f'run-{j}-row-{k+202}',group=group,target=float(z[k+200]),partition='confirmation' if j==4 else 'development',fold=j,h0=float(z[k]),h=float(h),v=float((h-prev)/.1),a=float((h-2*prev+prev2)/.01),median=float(vals[-1]),source_anchor=fn+f':row:{k+202}:column:{j+2}',calibration_anchor=fn+f':rows:{k-218}-{k+2}:column:{j+2}',linked_unit=group,eligible_reason='Fixed50ms issuance grid; finite causal220ms history and exact200ms future target'))
 return pd.DataFrame(rows)
