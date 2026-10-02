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
 base=sources(data_root);fn='raw/ct5km_ssta_v3.1-clim19912020-v1_20260816.nc';s=json.loads((ROOT/'SPLITS.json').read_text());rows=[]
 with h5py.File(base/fn) as f:
  v=f['sea_surface_temperature_anomaly']; a=v[0].astype(float)*float(v.attrs['scale_factor'][0]);mask=f['mask'][0];lat=f['lat'][:];lon=f['lon'][:]
  offsets=[(0,-4),(0,4),(-4,0),(4,0),(0,-8),(0,8),(-8,0),(8,0),(-4,-4),(-4,4),(4,-4),(4,4)]
  for y in range(20,3600,40):
   if abs(lat[y])>60:continue
   for x in range(20,7200,40):
    yy=np.array([y]+[y+dy for dy,dx in offsets]);xx=np.array([x]+[x+dx for dy,dx in offsets]);z=a[yy,xx]
    if np.any(mask[yy,xx]!=0) or not np.isfinite(z).all() or np.any(abs(z)>15):continue
    tile=f'{int((lat[y]+90)//20):02d}-{int((lon[x]+180)//20):02d}';h=hashlib.sha256(('P100-020-v1|'+tile).encode()).hexdigest();part='confirmation' if int(h[:8],16)%5==0 else 'development';u=z[1:]
    rows.append(dict(sample_id=f'pixel-{y}-{x}',group=tile,target=z[0],partition=part,fold=int(h[8:16],16)%5,hx=(u[0]+u[1])/2,hy=(u[2]+u[3])/2,ox=(u[4]+u[5])/2,oy=(u[6]+u[7])/2,dg=float(np.mean(u[8:])),gx=abs(u[1]-u[0]),gy=abs(u[3]-u[2]),clat=float(np.cos(np.deg2rad(lat[y]))),source_anchor=fn+f':sea_surface_temperature_anomaly[0,{y},{x}]',calibration_anchor=fn+':'+str(list(zip(yy[1:].tolist(),xx[1:].tolist()))),linked_unit='one-map-2026-08-16',eligible_reason='Center and all twelve calibration pixels are finite valid-water pixels; latitude within60degrees; fixed lattice'))
 return pd.DataFrame(rows)
