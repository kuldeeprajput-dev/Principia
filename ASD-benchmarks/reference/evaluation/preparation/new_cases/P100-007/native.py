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
 from scipy.signal import find_peaks
 rows=[]
 for name,p in sources(root).items():
  speed=name.removeprefix('FP_S1_').removesuffix('.csv');d=pd.read_csv(p);x=d[['1:Fz','2:Fz']].to_numpy(float);n=len(x)//10;x=x[:n*10].reshape(n,10,2).mean(axis=1)
  for i in range(500,n-10,5):
   past=x[i-499:i+1,0]
   if not np.isfinite(x[i-499:i+11]).all():continue
   u=past-past.mean();ac=np.correlate(u,u,mode='full')[len(u)-1:];lags=np.arange(60,201);peaks=find_peaks(ac[lags])[0];T=int(lags[peaks[np.argmax(ac[lags][peaks])]]) if len(peaks) else int(lags[np.argmax(ac[lags])]);j=i+10-T
   rows.append(dict(sample_id='speed'+speed+':block'+str(i),group=speed,target=float(x[i+10,0]),force=x[i,0],lag20=x[i-2,0],lag50=x[i-5,0],lag100=x[i-10,0],opposite=x[i,1],opposite50=x[i-5,1],cycle=x[j,0],cycle_previous=x[j-5,0],period=T/100,speed=float(speed),source_anchor=name+':1:Fz:nativeRows'+str((i+10)*10+2)+'-'+str((i+11)*10+1),calibration_anchor='Only causal source rows through'+str((i+1)*10+1),linked_unit='participantS1',prediction_end_native_frame=(i+1)*10,target_end_native_frame=(i+11)*10))
 return finish(rows)
