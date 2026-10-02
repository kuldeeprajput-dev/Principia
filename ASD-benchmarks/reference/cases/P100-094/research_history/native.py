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
 import re
 root=sources(data_root);rows=[]
 for f in sorted((root/'raw').rglob('*Station-*_Cast-*.csv')):
  st=int(re.search(r'Station-(\d+)',f.name).group(1));d=pd.read_csv(f)
  for j,z in d.iterrows():
   vals=[z.pressure,z.T1,z.S1,z.CDOM]
   if not np.isfinite(vals).all() or not 5<=z.pressure<=500 or z.pump!=1 or z.T1_quality_flag!=0 or z.S1_quality_flag!=0:continue
   g=f'station-{st:02d}'
   rows.append(dict(sample_id=f'{g}:row-{j+2}',group=g,target=float(z.CDOM),partition='confirmation' if st in [10,12] else 'development',fold_key=st,pressure=float(z.pressure),temperature=float(z.T1),salinity=float(z.S1),source_anchor=f'{f.name}:row={j+2};CDOM',input_anchor=f'{f.name}:row={j+2};pressure,T1,S1;T/S_QC=0',prediction_time=str(z.time),target_time=str(z.time)))
 return finish(rows)
