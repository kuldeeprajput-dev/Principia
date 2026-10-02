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
 p=sources(root);a=pd.read_excel(p['raw/DETECT_Data.xlsx'],sheet_name='Antibiotic Trial',header=1);a['native_row']=np.arange(len(a))+3;a=a.iloc[1:].copy();rows=[]
 for g,b in a.groupby('ID',sort=True):
  b=b.sort_values('Timing relative to Drug delivery');cal=b[b['Timing relative to Drug delivery']<0];y=pd.to_numeric(cal.iloc[:,8],errors='raise');post=b[b['Timing relative to Drug delivery']>0]
  if len(cal)!=2:raise ValueError('Expected two baseline records')
  for _,r in post.iterrows():rows.append(dict(sample_id=f'{g}:h{r.iloc[2]}',group=str(g),target=float(r.iloc[8]),hours=float(r['Timing relative to Drug delivery']),baseline=float(y.mean()),baseline_change=float(y.iloc[1]-y.iloc[0]),age=float(post.iloc[0]['Age']),source_anchor=f'raw/DETECT_Data.xlsx::Antibiotic Trial:R{int(r.native_row)}C9',calibration_anchor=f'Antibiotic Trial:ID{g}:times-48,-24:C9',linked_unit=str(g)))
 return finish(rows)
