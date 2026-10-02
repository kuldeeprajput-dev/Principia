"""Deterministic Src curve preparation. No fitting; finite differences are declared calibration."""
from pathlib import Path
import hashlib,json,re
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
CASE='74_biochemistry_kinase_biosensors'
def prepare(data_root):
 p=Path(data_root)/CASE
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  q=p/a['path']
  if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native asset missing or checksum mismatch: '+a['path'])
 d=pd.read_csv(p/'raw/Fig_S3A.csv').apply(pd.to_numeric,errors='coerce'); rows=[]
 cols=pd.read_csv(p/'raw/Fig_S3A.csv',nrows=0).columns[1:10]
 groups=[format(float(re.search(r'BS ([\d,]+)',c).group(1).replace(',','.')),'g') for c in cols]
 reserved=set(sorted(groups,key=lambda x:hashlib.sha256(('p100-batch5-74-'+x).encode()).hexdigest())[:2])
 for c,g in zip(cols,groups):
  curve=d[[d.columns[0],c]].dropna();curve.columns=['time','y']; y=dict(zip(curve.time,curve.y)); f6=y[6.]; v6=(y[6.]-y[4.5])/1.5; curv=(y[6.]-2*y[4.5]+y[3.])/2.25
  for idx,z in curve[curve.time>7.5].iterrows():
   rows.append(dict(sample_id='src-'+g+'-row'+str(idx+2),group='dose-'+g,target=z.y,partition='confirmation' if g in reserved else 'development',concentration_uM=float(g),time_min=z.time,calibration_F6=f6,calibration_v6=v6,calibration_curvature=curv,source_anchor='raw/Fig_S3A.csv:row='+str(idx+2)+':column='+c,calibration_anchor='raw/Fig_S3A.csv:time_min=3,4.5,6:column='+c,eligibility_reason='finite Src response and t>7.5; no response-based exclusion',fold='dose-'+g))
 return pd.DataFrame(rows)
