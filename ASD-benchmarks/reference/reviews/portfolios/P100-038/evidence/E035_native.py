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
 root=sources(data_root); rows=[]
 for flight in range(1,6):
  f=next((root/'raw').glob(f'*5G*fligth{flight}.csv'))
  d=pd.read_csv(f,sep=';',usecols=['Time','RSRP (NR SpCell)'],low_memory=False);d['native_row']=np.arange(len(d))+2
  d=d[d.Time.str.match(r'^\d\d:\d\d:\d\d\.\d+$',na=False)].copy()
  d['t']=pd.to_datetime('2025-03-31 '+d.Time,format='%Y-%m-%d %H:%M:%S.%f');d['v']=pd.to_numeric(d['RSRP (NR SpCell)'].astype(str).str.split(',').str[0],errors='coerce')
  d=d[np.isfinite(d.v)].sort_values('t').drop_duplicates('t',keep='first').reset_index(drop=True)
  t=(d.t-d.t.iloc[0]).dt.total_seconds().to_numpy();v=d.v.to_numpy()
  used=set()
  for j in range(len(d)):
   k=np.searchsorted(t,t[j]+1.0);lo=np.searchsorted(t,t[j]-5);lo20=np.searchsorted(t,t[j]-20)
   if k>=len(d) or t[k]-t[j]>1.6 or j-lo<5 or t[j]<20: continue
   if k in used: continue
   used.add(k)
   h=v[lo:j+1];h20=v[lo20:j+1];st=t[lo:j+1]-t[j]
   slope=float(np.polyfit(st,h,1)[0]); g=f'flight-{flight}'
   rows.append(dict(sample_id=f'{g}:row{int(d.native_row.iloc[k])}',group=g,target=float(v[k]),partition='confirmation' if flight==5 else 'development',fold_key=flight,last=float(v[j]),mean5=float(h.mean()),mean20=float(h20.mean()),slope=slope,spread=float(h.std()),elapsed=float(t[j]),source_anchor=f'{f.name}:row={int(d.native_row.iloc[k])}',input_anchor=f'{f.name}:rows={int(d.native_row.iloc[lo20])}-{int(d.native_row.iloc[j])}',prediction_time=d.t.iloc[j].isoformat(),target_time=d.t.iloc[k].isoformat(),horizon_s=float(t[k]-t[j])))
 return finish(rows)
