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

INPUTS=['metric_json']
def prepare(data_root):
 s=source(data_root);rows=[];seen={};perms=list(itertools.permutations(range(5)));pairs=list(itertools.combinations(range(5),2))
 for f in sorted((s/'raw').glob('*.mrdi')):
  j=json.loads(f.read_text())
  for i,(poly,metric)in enumerate(j['data']):
   # Derive exact distances from labeled +/- root vertices, then cross-check author's10-vector.
   distances={}
   for v in poly['POINTS']:
    vals=[Fraction(x)for x in v[1:]];nz=[k for k,x in enumerate(vals)if x]
    if len(nz)!=2 or vals[nz[0]]!=-vals[nz[1]]:raise ValueError('Unexpected rootpolyvertex')
    distances[tuple(nz)]=1/abs(vals[nz[0]])
   arr=[distances[p]for p in pairs]
   author=[Fraction(x)for x in metric]
   if sorted(v/min(arr)for v in arr)!=sorted(v/min(author)for v in author):raise ValueError('Metric-vector / native-points mismatch beyond uniform scale')
   m=[[Fraction(0)for _ in range(5)]for _ in range(5)]
   for (a,b),v in zip(pairs,arr):m[a][b]=m[b][a]=v
   canonical=min(tuple(m[p[a]][p[b]]/min(arr)for a,b in pairs)for p in perms);key=hashlib.sha256(str(canonical).encode()).hexdigest()[:20]
   facets=poly.get('POINTS_IN_FACETS',poly.get('VERTICES_IN_FACETS'))
   if facets is None:raise ValueError('Missing native incidence')
   if any(not isinstance(row,list) and row!={'cols':len(poly['POINTS'])} for row in facets):raise ValueError('Unknown incidence metadata')
   facets=[row for row in facets if isinstance(row,list)]
   target=len(facets)
   roots=[]
   for v in poly['POINTS']:
    vals=[Fraction(x)for x in v[1:]];roots.append((next(k for k,x in enumerate(vals)if x>0),next(k for k,x in enumerate(vals)if x<0)))
   typekey=min(tuple(sorted(tuple(sorted((per[roots[v][0]],per[roots[v][1]])for v in facet))for facet in facets))for per in perms)
   family=hashlib.sha256(str(typekey).encode()).hexdigest()[:20]
   if key in seen:
    if seen[key]!=target:raise ValueError('Conflicting duplicate metric')
    continue
   seen[key]=target;rows.append(dict(sample_id=f.name+':'+str(i),group=family,target=target,metric_json=json.dumps([str(v)for v in arr],separators=(',',':')),partition='confirmation'if hh(family)%5==0 else'development',fold=hh(family)%3,source_anchor='raw/'+f.name+':data['+str(i)+'].POINTS_IN_FACETS',calibration_anchor='none',eligibility='Allnative5pointmetricrecords; permutation/positive-scale duplicates merged',source_class='generic'if 'generic'in f.name else'strict'))
 return finish(rows)
