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
 root=sources(data_root);f=next((root/'raw').glob('*.csv'));cols={'Balancing Authority':'authority','UTC Time at End of Hour':'timestamp','Demand Forecast (MW)':'forecast','Demand (MW)':'target'}
 d=pd.read_csv(f,usecols=list(cols)).rename(columns=cols);d['row']=np.arange(len(d))+2;d['timestamp']=pd.to_datetime(d.timestamp,format='%m/%d/%Y %I:%M:%S %p');d['forecast']=pd.to_numeric(d.forecast,errors='coerce');d['target']=pd.to_numeric(d.target,errors='coerce');out=[]
 for ba,z in d.groupby('authority',sort=True):
  z=z.sort_values('timestamp').drop_duplicates('timestamp',keep='first').set_index('timestamp');idx=z.index
  a=z.reindex(idx-pd.Timedelta(hours=48)).reset_index(drop=True);b=z.reindex(idx-pd.Timedelta(hours=168)).reset_index(drop=True);pr=z.reindex(idx-pd.Timedelta(hours=1)).reset_index(drop=True);q=z.reset_index();q['load48']=a.target;q['load168']=b.target;q['F48']=a.forecast;q['F168']=b.forecast;q['r48row']=a.row;q['r168row']=b.row;q['ramp']=q.forecast-pr.forecast
  cc=['forecast','target','load48','load168','F48','F168'];mask=np.isfinite(q[cc+['ramp']]).all(axis=1)&(q[cc]>=0).all(axis=1)&(q.forecast>0)&(q.timestamp<pd.Timestamp('2025-07-01'))
  q=q[mask].copy();q['error48']=q.load48-q.F48;q['error168']=q.load168-q.F168;q['group']=ba+':'+q.timestamp.dt.strftime('%Y-%m');q['sample_id']=ba+':'+q.timestamp.dt.strftime('%Y-%m-%dT%H:%M:%S');q['partition']=np.where(q.timestamp>=pd.Timestamp('2025-06-01'),'confirmation','development');q['fold_key']=q.timestamp.dt.month;q['hour']=q.timestamp.dt.hour;q['weekend']=(q.timestamp.dt.dayofweek>=5).astype(int);q['prediction_time']=(q.timestamp-pd.Timedelta(hours=24)).dt.strftime('%Y-%m-%dT%H:%M:%S');q['target_time']=q.timestamp.dt.strftime('%Y-%m-%dT%H:%M:%S');q['source_anchor']=f.name+':row='+q.row.astype(str);q['input_anchor']=f.name+':lag48row='+q.r48row.astype(int).astype(str)+';lag168row='+q.r168row.astype(int).astype(str)
  out.append(q[['sample_id','group','target','partition','fold_key','forecast','error48','error168','load48','load168','ramp','hour','weekend','source_anchor','input_anchor','prediction_time','target_time','authority']])
 return finish(pd.concat(out,ignore_index=True).to_dict('records'))
