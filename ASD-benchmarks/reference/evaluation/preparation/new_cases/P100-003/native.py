from pathlib import Path
import json,hashlib,math,itertools,gzip,zipfile,io
from fractions import Fraction
import numpy as np,pandas as pd
C=Path(__file__).resolve().parent
SEED='principia100-asd7-20261002'
def hh(s):return int(hashlib.sha256((SEED+str(s)).encode()).hexdigest(),16)
def source(data_root):
 m=json.loads((C/'SOURCE_MANIFEST.json').read_text());base=Path(data_root)
 for a in m['assets']:
  p=base/a['path']
  if not p.is_file() or p.stat().st_size!=a['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing, truncated or checksum-mismatched native asset: '+a['path'])
 return base/m['data_root_relative']
def finish(rows):
 d=pd.DataFrame(rows)
 if d.empty:raise ValueError('No eligible observations')
 if d.sample_id.duplicated().any():raise ValueError('Duplicate native identity')
 if not np.isfinite(d.target.to_numpy(float)).all():raise ValueError('Nonfinite target')
 return d.sort_values('sample_id').reset_index(drop=True)

INPUTS=['lag1','lag2','lag3','lag4','median4','mad4','low1','high1','line1']
def prepare(data_root):
 import h5py
 from scipy.signal import welch
 s=source(data_root);f=next((s/'raw').glob('*.hdf5'))
 with h5py.File(f,'r')as z:
  strain=z['strain/Strain'][:];mask=z['quality/simple/DQmask'][:];inj=z['quality/injections/Injmask'][:];gps=int(z['meta/GPSstart'][()])
 a={}
 for k in range(256):
  sec=slice(k*16,(k+1)*16)
  if not np.all((mask[sec]&1)>0)or not np.all((inj[sec]&23)==23):continue
  y=strain[k*65536:(k+1)*65536]
  if not np.isfinite(y).all():continue
  freq,p=welch(y*1e21,fs=4096,nperseg=8192,noverlap=4096,window='hann',detrend='constant')
  def band(lo,hi):return float(np.sqrt(np.trapezoid(p[(freq>=lo)&(freq<=hi)],freq[(freq>=lo)&(freq<=hi)])))
  a[k]=[band(30,80),band(10,30),band(80,200),band(59,61)]
 rows=[]
 for k in range(4,256):
  if any(k-i not in a for i in range(5)):continue
  block=k//32;past=np.array([a[k-i][0]for i in range(1,5)])
  q=dict(sample_id='H1:w'+str(k),group='block'+str(block),target=a[k][0],partition='confirmation'if block>=6 else'development',block=block,window_start_gps=gps+k*16,source_anchor='raw/'+f.name+':strain/Strain['+str(k*65536)+':'+str((k+1)*65536)+']',quality_mask=int(np.bitwise_and.reduce(mask[k*16:(k+1)*16])),injection_mask=int(np.bitwise_and.reduce(inj[k*16:(k+1)*16])),calibration_anchor='previous4nonoverlapping16s windows',median4=float(np.median(past)),mad4=float(np.median(abs(past-np.median(past)))),low1=a[k-1][1],high1=a[k-1][2],line1=a[k-1][3]);q.update({'lag'+str(i):float(past[i-1])for i in range(1,5)});rows.append(q)
 return finish(rows)
