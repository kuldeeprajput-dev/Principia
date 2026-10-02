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
 import rdata
 p=sources(root);rp=next(v for k,v in p.items() if k.endswith('.rds'));cp=next(v for k,v in p.items() if k.endswith('.csv'));a=rdata.read_rds(rp)['counts'];genes=[str(v) for v in a.coords[a.dims[0]].values];samples=[str(v).split('_')[0] for v in a.coords[a.dims[1]].values];v=np.asarray(a.values,float)
 if '7412' not in genes or (v<0).any() or (v.sum(axis=0)<=0).any():raise ValueError('VCAM1 or valid count libraries missing')
 y=np.log2(1+1e6*v[genes.index('7412')]/v.sum(axis=0));lookup=dict(zip(samples,y));meta=pd.read_csv(cp);rows=[]
 for donor,b in meta.groupby('donor'):
  c=b[(b.stress=='LSS')&(b.pressure=='30kpa')]
  if len(c)!=1:raise ValueError('Exactly one declared donor calibration required')
  calid=str(int(c.iloc[0]['sample']));cal=float(lookup[calid])
  for _,r in b.iterrows():
   sid=str(int(r['sample']))
   if sid==calid:continue
   rows.append(dict(sample_id='VCAM1:'+sid,group=str(donor),target=float(lookup[sid]),calibration=cal,stiffness_kpa=float(r.pressure.replace('kpa','')),hss=int(r.stress=='HSS'),source_anchor=rp.name+':counts[Entrez7412,sample'+sid+']; all genes for library depth',calibration_anchor=rp.name+':counts[Entrez7412,sample'+calid+']; LSS30kPa',linked_unit='donor:'+str(donor)))
 return finish(rows)
