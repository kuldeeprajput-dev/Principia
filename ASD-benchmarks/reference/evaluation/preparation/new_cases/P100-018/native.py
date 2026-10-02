from pathlib import Path
import json,hashlib,zipfile,io,gzip
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def hashgroup(s):return int(hashlib.sha256(('principia100-batch7:'+str(s)).encode()).hexdigest()[:16],16)
def verify(data_root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in m['assets']:
  f=Path(data_root)/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native SHA256 mismatch: '+a['path'])
 return Path(data_root)/m['folder']
import re
def prepare(data_root):
 root=verify(data_root);f=root/'raw/StormEvents_details-ftp_v1.0_d2025_c20260819.csv.gz';d=pd.read_csv(f,low_memory=False);d['native_row']=np.arange(len(d))+2;d=d[d.EVENT_TYPE=='Tornado'].copy()
 def money(s):
  if pd.isna(s):return np.nan
  a=re.fullmatch(r'([0-9.]+)([KMB]?)',str(s).strip().upper())
  return float(a[1])*{'':1,'K':1e3,'M':1e6,'B':1e9}[a[2]] if a else np.nan
 d['dollars']=d.DAMAGE_PROPERTY.map(money);d['start']=pd.to_datetime(d.BEGIN_DATE_TIME,format='%d-%b-%y %H:%M:%S',errors='coerce');d['end']=pd.to_datetime(d.END_DATE_TIME,format='%d-%b-%y %H:%M:%S',errors='coerce');d['duration']=(d.end-d.start).dt.total_seconds()/60;groups=sorted(d.EPISODE_ID.dropna().astype(str).unique(),key=lambda s:hashgroup('tornado:'+s));held=set(groups[:max(1,len(groups)//5)]);rows=[]
 for _,r in d.iterrows():
  vals=[r.dollars,r.TOR_LENGTH,r.TOR_WIDTH,r.duration,r.BEGIN_LAT]
  if not np.isfinite(vals).all() or min(vals[:4])<0 or pd.isna(r.start) or r.TOR_LENGTH<=0 or r.TOR_WIDTH<=0:continue
  g=str(r.EPISODE_ID);rows.append(dict(sample_id=str(r.EVENT_ID),group='episode:'+g,target=float(np.log1p(r.dollars)),partition='confirmation' if g in held else 'development',fold_key=hashgroup('tornadofold:'+g)%5,length_km=float(r.TOR_LENGTH)*1.609344,width_km=float(r.TOR_WIDTH)*.0009144,duration_min=float(r.duration),latitude=float(r.BEGIN_LAT),month=float(r.start.month),source_anchor=f.name+':row='+str(int(r.native_row))+';DAMAGE_PROPERTY',input_anchor='TOR_LENGTH miles,TOR_WIDTH yards,BEGIN/END_DATE_TIME,BEGIN_LAT,month',eligibility_reason='Tornado positive recorded path dimensions, nonnegative parsed damage and duration; unknown damage excluded'))
 return pd.DataFrame(rows)
