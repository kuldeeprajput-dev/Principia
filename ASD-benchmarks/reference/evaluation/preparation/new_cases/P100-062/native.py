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
 base=sources(data_root);fn='raw/Permeation_MS AHSS 1300.xlsx';rows=[]
 for j,sheet in enumerate(['0.5 to 1 mA_cm2','5 to 10 mA_cm2']):
  d=pd.read_excel(base/fn,sheet_name=sheet,header=None);x=pd.to_numeric(d.iloc[:,0],errors='coerce').to_numpy();y=pd.to_numeric(d.iloc[:,1],errors='coerce').to_numpy();ok=np.isfinite(x)&np.isfinite(y);idx=np.flatnonzero(ok);x=x[ok];y=y[ok]
  if len(x)<20 or not np.all(np.diff(x)>0):raise ValueError('Invalid trace')
  cut=int(len(x)*.8);u0=float(np.mean(y[:3]));t0=float(x[2]);N=len(x)-3
  for k in range(3,len(x)):
   b=min(4,int((k-3)*5/N));group=f'trace-{j}-block-{b}'
   rows.append(dict(sample_id=f'trace-{j}-row-{idx[k]+1}',group=group,target=float(y[k]),partition='confirmation' if b==4 else 'development',fold=b,t=float(x[k]-t0),offset=u0,drive=.5 if j==0 else 5.,high=float(j),source_anchor=fn+f':sheet:{sheet}:row:{idx[k]+1}:column:B',calibration_anchor=fn+f':sheet:{sheet}:rows:'+','.join(str(a+1) for a in idx[:3]),linked_unit='MS-AHSS-1300-linked-traces',eligible_reason='Finite chronological sample after three-point baseline; exact native current'))
 return pd.DataFrame(rows)
