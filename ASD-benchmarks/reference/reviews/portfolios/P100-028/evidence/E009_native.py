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

import h5py

def prepare(data_root):
 base=sources(data_root);fn='raw/2025-11.hdf5';path='Scattering/2025-11-21_16_40_49';rows=[]
 with h5py.File(base/fn) as h:
  g=h[path];amp=np.asarray(g['amp fc pumps']);u=np.squeeze(np.asarray(g['USB']));freq=np.squeeze(np.asarray(g['freq sig']));assert u.shape==(51,13,13)
  for k in range(12,51):
   for a in range(13):
    for b in range(13):
     if a==b:continue
     low=float(abs(u[1,a,b]));high=float(abs(u[11,a,b]));target=float(abs(u[k,a,b]));noise=float(abs(u[0,a,b]));group=f'pump-{k:02d}'
     rows.append(dict(sample_id=group+f'-edge-{a:02d}-{b:02d}',group=group,target=target,partition='confirmation' if k>=41 else 'development',fold=min(4,int((k-12)*5/29)),lo=low,hi=high,noise=noise,r=float((amp[k]-amp[1])/(amp[11]-amp[1])),g=float(amp[k]),glo=float(amp[1]),ghi=float(amp[11]),sep=float(abs(a-b)),source_anchor=fn+'::'+path+f'/USB:squeezed_index:{k},{a},{b}',calibration_anchor=fn+'::'+path+f'/USB:squeezed_indices:0,{a},{b};1,{a},{b};11,{a},{b}',linked_unit='single-microwave-installation-2025-11-21',eligible_reason='Alloffdiagonalelements; completehighpumplevelsgrouped;0/.13/.140204calibrationonly'))
 return pd.DataFrame(rows)
