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
 p=sources(root);a=pd.read_csv(p['raw/raw data.csv']);a['native_row']=np.arange(len(a))+2;rows=[]
 for (person,protocol),b in a.groupby(['Subject','Protocol'],sort=True):
  b=b.sort_values(['Session','Block','Trial','native_row'],kind='stable');hist=[]
  for _,r in b.iterrows():
   child=str(r.Age)!='adult';y=float(r.Choice)
   if y not in [0.,1.]:raise ValueError('Nonbinary choice')
   rows.append(dict(sample_id=f'row{int(r.native_row)}',group=str(person),target=y,reward=float(r['Risk+AF8-Option']),probability=float(r['Risk+AF8-Prob']),child=int(child),age_child=float(r.Age) if child else 0.,multi=int(protocol=='E1.2'),description=int(protocol=='E2.2'),trial_progress=float(r.Trial)/40,lag_choice=hist[-1] if hist else .5,history_mean=float(np.mean(hist)) if hist else .5,has_history=int(bool(hist)),source_anchor=f'raw/raw data.csv:row{int(r.native_row)}:Choice',calibration_anchor=f'within-person-protocol strictly preceding ordered rows;count={len(hist)}',linked_unit=str(person),protocol=protocol,order=len(hist)))
   hist.append(y)
 return finish(rows)
