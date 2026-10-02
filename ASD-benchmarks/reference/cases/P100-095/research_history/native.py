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
 root=sources(data_root);f=next((root/'raw').glob('*TKE*.csv'));d=pd.read_csv(f);d.columns=d.columns.str.strip();t=pd.to_datetime(d.Time,format='%d/%m/%Y %H:%M:%S');rows=[]
 for j in range(len(d)-1):
  z=d.iloc[j];n=d.iloc[j+1];tt=t.iloc[j+1]
  if (tt-t.iloc[j]).total_seconds()!=1800 or any(z[k]!=0 or n[k]!=0 for k in ['Flag_RawAnyS2','Flag_H2']) or z.Flag_MetT!=0:continue
  vals=[n.MeanTKE2,z.MeanTKE2,z.MeanU2,z.MeanV2,z.MeanW2,z.MeanU2_unrot,z.MeanV2_unrot,z.Tair1,z.Tair3]
  if not np.isfinite(vals).all() or min(vals[:2])<0 or any(abs(v)>1e5 for v in vals):continue
  u=float(np.hypot(z.MeanU2,z.MeanV2));T=float((z.Tair1+z.Tair3)/2);grad=float((z.Tair3-z.Tair1)/(z.Ht3-z.Ht1));angle=float(np.arctan2(z.MeanV2_unrot,z.MeanU2_unrot))
  rows.append(dict(sample_id=f'TKE:row-{j+3}',group=f'week-{((tt-pd.Timestamp('2021-01-04')).days//7+1):02d}',target=float(n.MeanTKE2),partition='confirmation' if tt>=pd.Timestamp('2021-03-15') else 'development',fold_key=int((tt-pd.Timestamp('2021-01-04')).days//7+1),energy=float(z.MeanTKE2),wind=u,vertical=float(z.MeanW2),temperature=T,gradient=grad,sin_direction=float(np.sin(angle)),cos_direction=float(np.cos(angle)),source_anchor=f'{f.name}:row={j+3};MeanTKE2;flags=0',input_anchor=f'{f.name}:row={j+2};causal_30min_meanflow_and_TKE;flags=0',prediction_time=t.iloc[j].isoformat(),target_time=tt.isoformat()))
 return finish(rows)
