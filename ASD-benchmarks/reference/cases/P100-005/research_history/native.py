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

INPUTS=['graph6']
def decode(g):
 vals=[ord(c)-63 for c in g.strip()];n=vals[0]
 if n>=63:raise ValueError('Extendedgraph6 not supported')
 bits=''.join(format(v,'06b')for v in vals[1:]);adj=[0]*n;k=0
 for j in range(1,n):
  for i in range(j):
   if bits[k]=='1':adj[i]|=1<<j;adj[j]|=1<<i
   k+=1
 return adj
def alpha(adj):
 memo={0:0}
 def rec(mask):
  if mask in memo:return memo[mask]
  v=max((i for i in range(len(adj))if mask>>i&1),key=lambda i:(adj[i]&mask).bit_count());rest=mask&~(1<<v);x=max(rec(rest),1+rec(rest&~adj[v]));memo[mask]=x;return x
 return rec((1<<len(adj))-1)
def prepare(data_root):
 s=source(data_root);rows=[];seen=set();f=s/'raw/List of 4-minimal graphs.zip'
 with zipfile.ZipFile(f)as z:
  member='List of 4-minimal graphs/4Minimal.csv';lines=z.read(member).decode().splitlines()
  for i,line in enumerate(lines):
   g,parent=line.split(',');family=parent or g
   if g in seen:continue
   seen.add(g);a=decode(g);rows.append(dict(sample_id=hashlib.sha256(g.encode()).hexdigest()[:20],group=hashlib.sha256(family.encode()).hexdigest()[:20],target=alpha(a),graph6=g,partition='confirmation'if hh(family)%5==0 else'development',fold=hh(family)%3,source_anchor='raw/'+f.name+'::'+member+':row'+str(i+1),native_family=family,eligibility='Complete4107source4-minimal list; aliases/edge-subgraph references linked',calibration_anchor='none'))
 return finish(rows)
