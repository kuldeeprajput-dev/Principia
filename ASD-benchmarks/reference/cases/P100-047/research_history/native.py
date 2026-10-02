from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def sources(root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in m['assets']:
  p=Path(root)/a['path']
  if not p.is_file(): raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']: raise ValueError('Native SHA256 mismatch: '+a['path'])
 return Path(root)/m['folder']
def finish(rows):
 d=pd.DataFrame(rows)
 if d.empty: raise ValueError('No eligible observations')
 if d.sample_id.duplicated().any(): raise ValueError('Duplicate native identities')
 d['sample_id']=d.sample_id.astype(str);d['group']=d.group.astype(str)
 return d
def prepare(data_root:Path):
 import netCDF4 as nc
 root=sources(data_root);rows=[]
 for f in sorted((root/'raw').rglob('*_Sprof.nc')):
  fl=f.name.split('_')[0]
  with nc.Dataset(f) as n:
   dates=nc.num2date(n['JULD'][:],n['JULD'].units)
   names={'pressure':'PRES','temperature':'TEMP','salinity':'PSAL','oxygen':'DOXY','nitrate':'NITRATE'}
   arrays={k:np.ma.filled(n[v+'_ADJUSTED'][:],np.nan) for k,v in names.items()}
   quals={k:np.ma.filled(n[v+'_ADJUSTED_QC'][:],b'9').astype('U1') for k,v in names.items()}
   for j,t0 in enumerate(dates):
    t=pd.Timestamp(str(t0));g=f'{fl}:profile-{j:03d}'
    for k in range(arrays['pressure'].shape[1]):
     vals={x:float(a[j,k]) for x,a in arrays.items()}
     ok=all(quals[x][j,k] in (['1','2','8'] if x in ['temperature','salinity'] else ['1','2']) for x in arrays)
     if not ok or not np.isfinite(list(vals.values())).all() or not 0<=vals['pressure']<=2000: continue
     rows.append(dict(sample_id=f'{g}:level-{k:03d}',group=g,target=vals.pop('oxygen'),partition='confirmation' if t>=pd.Timestamp('2025-07-01') else 'development',fold_key=2*t.year+int(t.month>=7),float_id=fl,**vals,source_anchor=f'{f.name}:N_PROF={j};N_LEVELS={k};DOXY_ADJUSTED',input_anchor=f'{f.name}:N_PROF={j};N_LEVELS={k};ADJUSTED',prediction_time=t.isoformat(),target_time=t.isoformat(),quality_flags=';'.join(f'{x}:{quals[x][j,k]}' for x in arrays)))
 return finish(rows)
