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
 p=sources(root);a=pd.read_excel(p['Full_Dataset.xlsx'],header=2);m=pd.read_excel(p['Metadata.xlsx'])[['Plant ID','Genotype','Treatment']].drop_duplicates()
 if m['Plant ID'].duplicated().any():raise ValueError('Ambiguous plant-level cultivar/treatment')
 meta=m.set_index('Plant ID');rows=[]
 for i,r in a.iterrows():
  g=str(r['Plant ID'])
  if g not in meta.index:raise ValueError('Unknown plant ID')
  z=meta.loc[g];t=str(z.Treatment);vals=[r['QY_max'],r['NPQ_Lss'],r['Rfd_Lss'],r['NGRDI'],r['AREA_MM']]
  if not np.isfinite(np.asarray(vals,float)).all():continue
  if not 0<=float(r['QY_max'])<=1:raise ValueError('QY_max outside physical yield range')
  rows.append(dict(sample_id=f'{g}:native-row{i+4}',group=g,target=float(r['QY_max']),npq=float(r['NPQ_Lss']),rfd=float(r['Rfd_Lss']),ngrdi=float(r.NGRDI),area=float(r.AREA_MM),tiny=int(z.Genotype=='Tiny Tim'),salt=int(t.startswith('Salt')),drought=int(t.startswith('Drought')),high_stress=int(t.endswith('02')),source_anchor=f'Full_Dataset.xlsx:row{i+4}:QY_max; Metadata.xlsx:PlantID={g}',calibration_anchor='none; source image features only',linked_unit=g,source_sampling=str(r.Sampling)))
 return finish(rows)
