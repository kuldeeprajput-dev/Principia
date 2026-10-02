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
 p=sources(root);rows=[]
 for key,f in sorted(p.items()):
  if not key.endswith('_raw.csv'):continue
  a=pd.read_csv(f);v=a.iloc[:,:4].to_numpy(float);t=v[:,0];v=((v[:,1:]-0.1*2**14)/(0.8*2**14/2)-1)*70.306957829636;g=f.name.split('_')[0];trial=f.name[len(g)+1:-8]
  # Fixed index origins, no future peak or phase selection; validate nominal cadence.
  good=np.where(np.isfinite(t)&(t>=0))[0]
  if not len(good):continue
  end=good[-1]
  for j in range(100,end-20,100):
   inds=[j,j-5,j-10,j-20,j-30,j-40,j-50,j+20]
   if not np.isfinite(v[inds]).all() or abs((t[j+20]-t[j])-.2)>.025 or abs((t[j]-t[j-50])-.5)>.025:continue
   r=dict(sample_id=f'{f.stem}:row{j+2}',group=g,target=v[j+20,0],source_anchor=f'{key}:row{j+22}:Gauge Pressure',calibration_anchor='raw/Code/DataCollection_PQ.m:fixed ADC calibration',linked_unit=g,origin_time=t[j],target_time=t[j+20],trial=trial,trial_BH=int(trial=='PEEP_BH'),trial_FEM=int(trial=='FEM'))
   r.update({k:v[j-l,0] for k,l in zip(['p0','p05','p10','p20','p30','p40','p50'],[0,5,10,20,30,40,50])});r.update(di0=v[j,1],de0=v[j,2],di20=v[j-20,1],de20=v[j-20,2]);rows.append(r)
 return finish(rows)
