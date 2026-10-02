from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def sources(root):
 p={}
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  f=Path(root)/a['path']
  if not f.is_file() or f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native asset missing or mismatched: '+a['path'])
  p[a['name']]=f
 return p
def finish(rows):
 d=pd.DataFrame(rows);s=json.loads((HERE/'SPLITS.json').read_text());d['partition']=d.group.map(s['partition']);d['fold']=d.group.map(s['fold'])
 if d.sample_id.duplicated().any() or d.partition.isna().any() or not np.isfinite(d.target).all():raise ValueError('Invalid native row identity, grouping or target')
 return d
def prepare(root):
 import h5py
 rows=[]
 for name,p in sources(root).items():
  with h5py.File(p) as h:
   group=h['general/subject/subject_id'][()].decode();r=h['acquisition/PupilTracking/pupil_raw_radius/data'][:];t=h['acquisition/PupilTracking/pupil_raw_radius/timestamps'][:];v=h['acquisition/treadmill_velocity/data'][:];tv=h['acquisition/treadmill_velocity/timestamps'][:]
  ix=np.where(np.isfinite(t))[0];r=r[ix];t=t[ix];ok=np.isfinite(tv);v=v[ok];tv=tv[ok]
  if np.any(np.diff(t)<=0) or np.any(np.diff(tv)<=0):raise ValueError('Nonmonotone source time')
  for i in range(100,len(t)-20,10):
   a=np.searchsorted(t,t[i]-5);j=np.searchsorted(t,t[i]+1,side='right')-1
   if t[i]-t[a]<4.9 or j<=i or abs(t[j]-t[i]-1)>.08:continue
   if not np.isfinite(r[a:j+1]).all() or (r[a:j+1]<0).any() or np.max(np.diff(t[a:j+1]))>.1:continue
   def pupil(end):
    z=(t>=end-.25)&(t<=end);return float(np.mean(r[z])) if z.sum()>=4 else np.nan
   def speed(end):
    z=(tv>=end-.5)&(tv<=end)
    if not z.any() or end-tv[z][-1]>.1:return np.nan
    return float(np.mean(v[z]))
   x=[pupil(t[i]),pupil(t[i]-.5),pupil(t[i]-1),float(r[a:i+1].mean()),speed(t[i]),speed(t[i]-1)];y=pupil(t[j])
   if not np.isfinite(x+[y]).all():continue
   rows.append(dict(sample_id=name+':frame'+str(ix[i]),group=group,target=y,**dict(zip(['radius','lag05','lag1','mean5','speed','speed1'],x)),source_anchor=name+'::acquisition/PupilTracking/pupil_raw_radius/data:window_ending_native_index'+str(ix[j]),calibration_anchor='Released-trace prefix through native_index'+str(ix[i])+'; no future inputs',linked_unit=group,prediction_time_seconds=float(t[i]),target_time_seconds=float(t[j])))
 return finish(rows)
