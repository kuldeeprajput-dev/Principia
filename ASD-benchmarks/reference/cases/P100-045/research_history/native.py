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

INPUTS=['low','low_lag','background_low','background_high','time_s','channel_low_keV','channel_high_keV']
def prepare(data_root):
 from astropy.io import fits
 s=source(data_root);files=sorted((s/'raw').glob('glg_ctime_n*_v00.pha'));ids=[f.name.split('_')[2]for f in files];reserved=set(sorted(ids,key=hh)[:2]);rows=[]
 for f in files:
  detector=f.name.split('_')[2]
  with fits.open(f)as z:
   a=z['SPECTRUM'].data;trig=z[0].header['TRIGTIME'];start=np.asarray(a['TIME'],float)-trig;end=np.asarray(a['ENDTIME'],float)-trig;ex=np.asarray(a['EXPOSURE'],float);counts=np.asarray(a['COUNTS'],float);quality=np.asarray(a['QUALITY']);edge=np.array([z['EBOUNDS'].data['E_MIN'][4],z['EBOUNDS'].data['E_MAX'][4]],float)
  good=(quality==0)&(ex>0)&np.isfinite(counts).all(1);bg=good&(start>=-200)&(end<=-100)
  if not bg.any():raise ValueError('Missing declaredbackground')
  bl=float(counts[bg,2:4].sum()/ex[bg].sum());bh=float(counts[bg,4].sum()/ex[bg].sum());bins={}
  for k in range(-1,100):
   use=good&(start>=k)&(end<=k+1)
   if ex[use].sum()<.5:continue
   bins[k]=(float(counts[use,2:4].sum()/ex[use].sum()),float(counts[use,4].sum()/ex[use].sum()),np.where(use)[0],float(ex[use].sum()))
  for k in range(100):
   if k not in bins or k-1 not in bins:continue
   lo,hi,idx,exposure=bins[k];rows.append(dict(sample_id=detector+':s'+str(k),group=detector,target=hi,partition='confirmation'if detector in reserved else'development',low=lo,low_lag=bins[k-1][0],background_low=bl,background_high=bh,time_s=k+.5,channel_low_keV=edge[0],channel_high_keV=edge[1],source_anchor='raw/'+f.name+':SPECTRUMrows'+','.join(map(str,idx)),exposure_s=exposure,calibration_anchor='pretrigger[-200,-100]s same detector',eligibility='Quality0; positiveexposure; completebins >=0.5s; no burststrengthselection'))
 return finish(rows)
