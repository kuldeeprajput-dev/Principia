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
def prepare(data_root):
 base=sources(data_root);rows=[]
 for specimen,fn in [('CSH','raw/CSH_FOV5_Bz_uc0.mat'),('CSL','raw/CSL_FOV4_Bz_uc0.mat')]:
  a=loadmat(base/fn,variable_names=['Bz'])['Bz'];offsets=[(0,-4),(0,4),(-4,0),(4,0),(0,-8),(0,8),(-8,0),(8,0),(-4,-4),(-4,4),(4,-4),(4,4)]
  for y in range(20,a.shape[0]-8,20):
   for x in range(20,a.shape[1]-8,20):
    yy=np.array([y]+[y+dy for dy,dx in offsets]);xx=np.array([x]+[x+dx for dy,dx in offsets]);z=a[yy,xx]
    if not np.isfinite(z).all():continue
    u=z[1:];scale=max(float(np.sqrt(np.mean(u*u))),1e-15);block=f'{specimen}-r{y//200:02d}-c{x//320:02d}';rows.append(dict(sample_id=f'{specimen}-{y}-{x}',group=block,target=z[0],partition='confirmation' if specimen=='CSL' else 'development',fold=y//200,hx=(u[0]+u[1])/2,hy=(u[2]+u[3])/2,ox=(u[4]+u[5])/2,oy=(u[6]+u[7])/2,dg=float(np.mean(u[8:])),gx=abs(u[1]-u[0])/scale,gy=abs(u[3]-u[2])/scale,lo=float(min(u)),hi=float(max(u)),source_anchor=fn+f':Bz[{y},{x}]',calibration_anchor=fn+':Bz:'+str(list(zip(yy[1:].tolist(),xx[1:].tolist()))),linked_unit=specimen,eligible_reason='Finite measured Bz center and twelve fixed neighbors; target lattice and calibration offsets cannot overlap'))
 return pd.DataFrame(rows)
