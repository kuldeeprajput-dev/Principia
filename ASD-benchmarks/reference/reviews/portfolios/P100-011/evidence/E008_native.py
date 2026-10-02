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

INPUTS=['offline','accelerators','nodes','workload','precision']
def prepare(data_root):
 s=source(data_root);j=json.loads((s/'raw/summary_results.json').read_text());ix={};rows=[]
 for i,r in enumerate(j):
  if r.get('Category')!='closed'or r.get('Performance_Units')!='Tokens/s'or r.get('inferred',0)or r.get('errors',0)or str(r['Model']).endswith('99.9'):continue
  if r['Scenario']not in['Offline','Server']:continue
  key=(r['Submitter'],r['Platform'],r['Model']);slot=ix.setdefault(key,{})
  if r['Scenario']in slot:raise ValueError('Ambiguous duplicate scenario result')
  slot[r['Scenario']]=(i,r)
 for (submitter,platform,model),pair in sorted(ix.items()):
  if set(pair)!=set(['Offline','Server']):continue
  oi,o=pair['Offline'];si,r=pair['Server'];group=submitter+'/'+platform
  if float(o['Performance_Result'])<=0 or float(r['Performance_Result'])<=0:continue
  rows.append(dict(sample_id=group+'/'+model,group=group,target=float(r['Performance_Result']),partition='confirmation'if hh(group)%5==0 else'development',fold=hh(group)%4,offline=float(o['Performance_Result']),accelerators=float(o['Total Accelerators']),nodes=float(o['Nodes']),workload=model,precision=str(o.get('weight_data_types','unknown')),source_anchor='raw/summary_results.json:index'+str(si),calibration_anchor='raw/summary_results.json:index'+str(oi),eligibility='Uniqueclosednoninferred positiveToken/s matchedOfflineServer;99.9aliasesexcluded'))
 return finish(rows)
