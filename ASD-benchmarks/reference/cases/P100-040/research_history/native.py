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
def prepare(data_root):
 root=verify(data_root);lookup=pd.read_csv(root/'context/taxi_zone_lookup.csv').set_index('LocationID');frames=[]
 for file in sorted((root/'raw').glob('*.parquet')):
  d=pd.read_parquet(file);d['native_row']=np.arange(len(d));pu=pd.to_datetime(d.lpep_pickup_datetime);do=pd.to_datetime(d.lpep_dropoff_datetime);duration=(do-pu).dt.total_seconds()/60;distance=pd.to_numeric(d.trip_distance,errors='coerce')*1.609344
  # Routine-duration target intentionally excludes invalid and over24hour records; all exclusions are source-auditable.
  good=(pu.dt.year==2025)&(pu.dt.month==int(file.stem[-2:]))&duration.gt(0)&duration.le(1440)&distance.gt(0)&distance.le(1000)&d.PULocationID.isin(lookup.index)&d.DOLocationID.isin(lookup.index)
  z=d[good];p=pu[good];hour=p.dt.hour+p.dt.minute/60;orig=z.PULocationID.map(lookup.Borough);dest=z.DOLocationID.map(lookup.Borough);a=pd.DataFrame(dict(sample_id=file.name+':row='+z.native_row.astype(str),group=p.dt.strftime('%Y-%m-%d'),target=duration[good].astype(float),partition=np.where(p.dt.month>=10,'confirmation','development'),fold_key=p.dt.month,hour=hour,distance_km=distance[good].astype(float),weekend=(p.dt.dayofweek>=5).astype(float),peak=(((hour>=7)&(hour<10))|((hour>=16)&(hour<19))).astype(float),airport=(z.PULocationID.isin([1,132,138])|z.DOLocationID.isin([1,132,138])).astype(float),manhattan=((orig=='Manhattan')|(dest=='Manhattan')).astype(float),source_anchor=file.name+':parquet_row='+z.native_row.astype(str)+';dropoff-minus-pickup',input_anchor='recordedtripdistance,pickupclock,borough/airportlookup; distance unavailable at pickup',eligibility_reason='Same source month/year2025; duration0–1440min; recorded distance0–1000km; known source zones'));frames.append(a)
 return pd.concat(frames,ignore_index=True)
