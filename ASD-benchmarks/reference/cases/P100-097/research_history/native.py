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
 base=sources(data_root);rows=[];panels=['F2D','F3B','F3C','F3D','F3E'];z=zipfile.ZipFile(base/'raw/Data.zip')
 for j,panel in enumerate(panels):
  fn=panel+'_Specific_volume-Speed.dat';m=loadmat(io.BytesIO(z.read(fn)));keys=[k for k in m if not k.startswith('__')];assert len(keys)==1;v=m[keys[0]];assert v.ndim==2 and v.shape[1]==2
  for ix in range(0,len(v),10):
   eta,speed=map(float,v[ix]);
   if not np.isfinite([eta,speed]).all() or eta<=0 or speed<0:continue
   rows.append(dict(sample_id=f'{panel}-row{ix+1}',group=panel,target=speed,partition='confirmation' if j>=3 else 'development',fold=j,eta=eta,rho=1/eta,source_anchor='raw/Data.zip::'+fn+f':{keys[0]}[{ix},:]',calibration_anchor='none; density/specific volume is measured at the start of the source observation',linked_unit='Cao2017_multidirectional' if j>=3 else ['Ma2025','Zhang2011','Zhang2012'][j],eligible_reason='Every tenth native source row beginning0; finite positive specific volume and finite nonnegative measured speed'))
 return pd.DataFrame(rows)
