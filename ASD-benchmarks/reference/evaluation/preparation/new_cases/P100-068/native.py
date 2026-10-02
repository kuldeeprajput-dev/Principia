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

from scipy.io import loadmat
import subprocess

def prepare(data_root):
 base=sources(data_root);archive=base/'raw/Data.rar';s=json.loads((ROOT/'SPLITS.json').read_text());rows=[]
 for j,name in enumerate(s['members']):
  if Path(name).is_absolute() or '..' in Path(name).parts:raise ValueError('Unsafe archive member')
  a=loadmat(io.BytesIO(subprocess.check_output(['tar','-xOf',str(archive),name])));t=np.asarray(a['t']).ravel();y=np.asarray(a['noisy_s']).ravel()
  dt=float(np.median(np.diff(t)))
  if len(t)!=len(y) or not np.allclose(np.diff(t),dt,atol=1e-9) or not (np.isclose(dt,.0005) or np.isclose(dt,.001)):raise ValueError('Unexpected stored timing')
  lag=int(round(.005/dt))
  offset=float(np.mean(y[:20]));group=Path(name).stem
  for k in range(int(round(.05/dt)),len(y)-lag,lag):
   vals=[y[k+lag],y[k],y[k-lag],y[k-2*lag],y[k-3*lag]]
   if not np.isfinite(vals).all():continue
   rows.append(dict(sample_id=group+f'-index-{k+lag}',group=group,target=float(y[k+lag]),partition='confirmation' if name in s['confirmation_members'] else 'development',fold=j%5,y0=float(y[k]-offset),y1=float(y[k-lag]-offset),y2=float(y[k-2*lag]-offset),y3=float(y[k-3*lag]-offset),offset=offset,t=float(t[k]),source_anchor='raw/Data.rar::'+name+f':noisy_s:index0:{k+lag}',calibration_anchor='raw/Data.rar::'+name+f':noisy_s:indices0:0-19,{k-3*lag},{k-2*lag},{k-lag},{k}',linked_unit='TinyLev-large-object-installation',eligible_reason='Raw voltage only; fixed5ms forecast and5ms issuance; initial20samples offset; causal15ms delay history'))
 return pd.DataFrame(rows)
