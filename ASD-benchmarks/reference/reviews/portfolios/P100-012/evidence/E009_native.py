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
 base=sources(data_root);rows=[]
 for f in sorted((base/'raw').rglob('*.ras')):
  lines=f.read_text(errors='replace').splitlines();beg=lines.index('*RAS_INT_START');end=lines.index('*RAS_INT_END');a=np.loadtxt(io.StringIO('\n'.join(lines[beg+1:end])));wafer=int(f.name.split('-')[3]);position=f.name.split('-')[4];batch=(wafer-1)//3
  if a.shape[1]!=3 or not np.allclose(a[:,2],1):raise ValueError('Unresolved RAS correction factor')
  if '*MEAS_SCAN_AXIS_X "TwoThetaOmega"' not in lines:raise ValueError('Unexpected XRR axis')
  q=4*np.pi*np.sin(np.deg2rad(a[:,0]/2))/1.540593;cal=np.flatnonzero(abs(a[:,0]-1)<=.00801);I0=float(np.mean(a[cal,1]));q0=float(np.mean(q[cal]))
  for k in range(0,len(a),10):
   if not(1.4<=a[k,0]<=4.8) or not np.isfinite(a[k,1]) or I0<=0:continue
   rel=f.relative_to(base).as_posix();rows.append(dict(sample_id=f.stem+f'-line-{beg+k+2}',group=f'wafer-{wafer:02d}',target=float(a[k,1]),partition='confirmation' if batch==3 else 'development',fold=batch,q=float(q[k]),q0=q0,I0=I0,outer=float(position!='105'),source_anchor=rel+f':line:{beg+k+2}',calibration_anchor=rel+':lines:'+','.join(str(beg+x+2) for x in cal),linked_unit=f'deposition-{batch+1}',eligible_reason='Fixed tenth native point within2theta1.4–4.8deg; calibration1.0±.008deg; correctionfactor1'))
 return pd.DataFrame(rows)
