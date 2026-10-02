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
 p=sources(root);z=zipfile.ZipFile(p['raw/20250611_data.zip']);n=next(n for n in z.namelist() if 'figure-2h-FI-curve-data' in n);a=pd.read_csv(io.BytesIO(z.read(n)));a['native_row']=np.arange(len(a))+2;rows=[]
 for cell,b in a.groupby('filename',sort=True):
  b=b.sort_values('sweep');cal=b[b['applied current']<=10]
  if cal.empty:continue
  for _,r in b.iterrows():
   if r['applied current']<=10 or str(r['use for FI (manually confirmed)']).strip()!='y':continue
   g=str(r['date'])+':'+str(r['dish']);rows.append(dict(sample_id=f'{cell}:sweep{int(r.sweep)}',group=g,target=float(r['spike count']),current=float(r['applied current']),soft=int(str(r.Stiffness).strip()=='0.1kPa'),kd=int('KD' in str(r.Condition)),cal_mean=float(cal['spike count'].mean()),cal_last=float(cal.iloc[-1]['spike count']),source_anchor=f'raw/20250611_data.zip::{n}:row{r.native_row}:spike count',calibration_anchor=f'{n}:cell={cell}:current<=10pA',linked_unit=g,cell=cell,date=str(r['date'])))
 return finish(rows)
