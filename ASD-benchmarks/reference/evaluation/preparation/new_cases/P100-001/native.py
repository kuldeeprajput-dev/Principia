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

INPUTS=['prefix_json','horizon']
def prepare(data_root):
 s=source(data_root);rows=[]
 with gzip.open(s/'raw/stripped.gz','rt')as f:
  for line_no,line in enumerate(f,1):
   if not line.startswith('A'):continue
   ident,terms=line.split(' ',1)
   if hh(ident)%128:continue
   a=[int(x)for x in terms.strip().strip(',').split(',') if x.strip()]
   if len(a)<21 or any(abs(v)>10**100 for v in a[:21]):continue
   prefix=a[:16];delta=[v-prefix[0]for v in prefix];g=math.gcd(*delta)or 1
   if next((v for v in delta if v),1)<0:g=-g
   family=hashlib.sha256(json.dumps([v//g for v in delta]).encode()).hexdigest()[:16]
   rows.append(dict(sample_id=ident,group=family,target=float(np.arcsinh(float(a[20]))),prefix_json=json.dumps(prefix,separators=(',',':')),horizon=5,partition='confirmation'if hh(family)%5==0 else'development',fold=hh(family)%3,source_anchor='raw/stripped.gz:line'+str(line_no)+':term21',raw_target_integer=str(a[20]),eligibility='>=21terms; first21 within1e100; IDhashmod128=0; no outcome-based performance screening',calibration_anchor=ident+':terms1-16'))
 return finish(rows)
