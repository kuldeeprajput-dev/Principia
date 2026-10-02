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
 root=sources(data_root);rows=[]
 for f in sorted((root/'raw').rglob('*.dat')):
  a=np.loadtxt(f,skiprows=2);site=f.name[:3]
  for j,z in enumerate(a):
   # index8:downSW,14:diffuse,16:downLW,38:airT,40:RH; following columns are QC.
   if any(z[q]!=0 for q in [9,15,17,39,41]) or not 0<=z[7]<75 or z[8]<=20 or not 0<z[40]<=100:continue
   t=pd.Timestamp(year=int(z[0]),month=int(z[2]),day=int(z[3]),hour=int(z[4]),minute=int(z[5]));key=int(z[2])*100+int(z[3])
   vals=[z[16],z[38],z[40],z[8],z[14],z[7]]
   if not np.isfinite(vals).all() or any(v<=-9999 for v in vals):continue
   rows.append(dict(sample_id=f'{site}:{t.isoformat()}',group=f'{site}:{t:%Y-%m-%d}',target=float(z[16]),partition='confirmation' if key>=725 else 'development',fold_key=key,temperature=float(z[38]),humidity=float(z[40]),solar=float(z[8]),diffuse=float(z[14]),zenith=float(z[7]),site_dra=int(site=='dra'),source_anchor=f'{f.name}:line={j+3};dw_ir;QC=0',input_anchor=f'{f.name}:line={j+3};met_and_independent_solar;QC=0',prediction_time=t.isoformat(),target_time=t.isoformat()))
 return finish(rows)
