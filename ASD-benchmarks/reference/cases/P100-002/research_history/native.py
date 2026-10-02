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

INPUTS=['lag1','lag2','lag3','lag4','lag6','lag12','lag24','median6','median24','mad6','delta_h']
def prepare(data_root):
 from astropy.io import fits
 s=source(data_root);files=sorted((s/'raw').glob('*_lc.fits'));names=[f.stem for f in files];reserved=set(sorted(names,key=hh)[:2]);rows=[]
 for f in files:
  with fits.open(f)as z:t=np.asarray(z[1].data['TIME'],float);y=np.asarray(z[1].data['FLUX'],float)
  good=np.isfinite(t)&np.isfinite(y);idx=np.where(good)[0];t=t[good];y=y[good];start=math.floor(float(t.min()));bins=np.floor((t-start)*24).astype(int);a=pd.DataFrame(dict(hour=bins,t=t,y=y,index=idx));a=a.groupby('hour').agg(t=('t','median'),y=('y','median'),lo=('index','min'),hi=('index','max'),n=('y','size'));group=f.stem
  for k in a.index:
   if any(k-i not in a.index for i in range(25)):continue
   h=a.loc[[k-i for i in range(1,25)]];last=h.y.to_numpy();q=dict(sample_id=group+':h'+str(k),group=group,target=float(a.loc[k,'y']),partition='confirmation'if group in reserved else'development',source_anchor='raw/'+f.name+':rows'+str(int(a.loc[k,'lo']))+'-'+str(int(a.loc[k,'hi'])),bin_hour=int(k),calibration_anchor='preceding24hour bins',delta_h=float((a.loc[k,'t']-h.iloc[0].t)*24),median6=float(np.median(last[:6])),median24=float(np.median(last)),mad6=float(np.median(abs(last[:6]-np.median(last[:6])))),target_rows=int(a.loc[k,'n']))
   q.update({'lag'+str(i):float(last[i-1])for i in[1,2,3,4,6,12,24]});rows.append(q)
 return finish(rows)
