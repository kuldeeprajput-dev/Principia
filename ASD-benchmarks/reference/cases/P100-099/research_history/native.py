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
 import zipfile,io
 from scipy.io import loadmat
 z=zipfile.ZipFile(next(iter(sources(root).values())));rows=[]
 for n in sorted(z.namelist()):
  if not n.endswith('.mat'):continue
  group=Path(n).stem.split('_')[-1];v=loadmat(io.BytesIO(z.read(n)),simplify_cells=True)
  if 'trace' not in v.get('processed',{}):continue
  trace=np.asarray(v['processed']['trace'],float)
  if trace.ndim!=2 or trace.shape[0]<2 or trace.shape[1]<360:raise ValueError('Unexpected processed trace matrix')
  m=np.mean(trace,axis=0)
  for i in range(299,len(m)-60,30):
   if not np.isfinite(m[i-299:i+61]).all():continue
   cell=np.mean(trace[:,i-29:i+1],axis=1);x=[float(m[i-29:i+1].mean()),float(m[i-59:i-29].mean()),float(m[i-89:i-59].mean()),float(m[i-299:i+1].mean()),float(cell.std()),float(np.mean(cell==0)),int('/Day' in n and '_vCA1_' in n),int('_g3/' in n)];y=float(m[i+31:i+61].mean())
   if not np.isfinite(x+[y]).all():continue
   rows.append(dict(sample_id=n+':endframe'+str(i+1),group=group,target=y,**dict(zip(['level','lag30','lag60','mean300','dispersion','zero_fraction','ventral','condition_group3'],x)),source_anchor='Data_ToUpload.zip::'+n+'::processed.trace[:,native1basedframes'+str(i+32)+'-'+str(i+61)+']',calibration_anchor='processed.trace prefix ending native1basedframe'+str(i+1),linked_unit=group,neurons=trace.shape[0],prediction_end_frame=i+1,target_end_frame=i+61))
 return finish(rows)
