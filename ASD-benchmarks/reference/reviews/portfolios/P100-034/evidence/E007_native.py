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
 p=sources(root);z=zipfile.ZipFile(p['raw/Figure 5.zip']);n=next(n for n in z.namelist() if n.endswith('.xlsx') and 'titration' in n and not n.startswith('__MACOSX'));rows=[]
 for mut,s in enumerate(['w1118_wellgenetics','unc13A_C1mut_ex4']):
  a=pd.read_excel(io.BytesIO(z.read(n)),sheet_name=s,header=None);ix=[i for i,v in enumerate(a.iloc[:,0]) if isinstance(v,str) and v.strip().startswith('cell')]
  for b,i in enumerate(ix):
   g=f'mutant_block{b+1}' if mut else f'control_cell{b+1}'; vals=np.array([[pd.to_numeric(a.iloc[i+4+k,2+3*j],errors='coerce') for k in range(10)] for j in range(5)],float);means=np.nanmean(np.abs(vals),axis=1)
   if not np.isfinite(means[:2]).all():raise ValueError('Missing low-dose calibration '+g)
   for j,c in enumerate([.4,.75,1.5,3,6]):
    if j<2 or not np.isfinite(means[j]):continue
    rows.append(dict(sample_id=f'{g}:Ca{c}',group=g,target=means[j],calcium=c,mutant=mut,low04=means[0],low075=means[1],source_anchor=f'raw/Figure 5.zip::{n}::{s}:R{i+5}-R{i+14}:C{3+3*j}',calibration_anchor=f'{s}:R{i+5}-R{i+14}:C3,C6',linked_unit=g,source_file_label=str(a.iloc[i+1,2+3*j])))
 return finish(rows)
