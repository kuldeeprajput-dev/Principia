from pathlib import Path
import hashlib,json,io,zipfile
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def sources(root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text());p={}
 for a in m['assets']:
  f=root/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native checksum mismatch: '+a['path'])
  p[a['name']]=f
 return p
def finish(rows):
 d=pd.DataFrame(rows);s=json.loads((HERE/'SPLITS.json').read_text());d['partition']=d.group.map(s['partition']);d['fold']=d.group.map(s['fold'])
 if d.sample_id.duplicated().any() or d.partition.isna().any():raise ValueError('Duplicate identity or undeclared group')
 if not np.isfinite(d.target).all():raise ValueError('Nonfinite native target')
 return d

def prepare(root):
 p=sources(root);z=zipfile.ZipFile(p['raw/main_data.zip']);rows=[]
 for n in sorted(z.namelist()):
  if '/binding/' not in n or not n.endswith('.csv') or n.startswith('__MACOSX'):continue
  a=pd.read_csv(io.BytesIO(z.read(n)));y=a.to_numpy(float).mean(axis=1).reshape(4,10);g=Path(n).stem;factor=7/8 if '9a5f' in g else 7/6 if 'Hex2' in g else 1.;x=np.array([0,1,2,5,7.5,10,15,20,25,30])*factor
  for r in range(4):
   for j in range(4,10):rows.append(dict(sample_id=f'{g}:rep{r}:dose{j}',group=g,target=y[r,j],dose=x[j],dose_cal=x[3],dose1=x[1],dose2=x[2],F0=y[r,0],F1=y[r,1],F2=y[r,2],F5=y[r,3],dye_NR=int('NR' in g),source_anchor=f'raw/main_data.zip::{n}:row{r*10+j+2}:all-spectral-columns',calibration_anchor=f'{n}:rows{r*10+2}-{r*10+5}:all-spectral-columns',linked_unit=g,replicate=r))
 return finish(rows)
