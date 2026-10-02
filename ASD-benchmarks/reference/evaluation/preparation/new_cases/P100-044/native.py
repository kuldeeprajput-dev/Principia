"""Source-verified capped elapsed solver consumption, all formulations/failures."""
from pathlib import Path
import json,hashlib,csv
import numpy as np,pandas as pd
HERE=Path(__file__).resolve().parent
INPUTS=['nodes','max_degree','is_flow','is_linear','is_quadratic','moore2_occupancy']
def prepare(data_root):
 manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in manifest['assets']:
  p=Path(data_root)/a['path']
  if not p.is_file()or p.stat().st_size!=a['bytes']or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing or checksum-mismatched source: '+a['path'])
 src=Path(data_root)/'44_mathematics_qoblib_topology/raw/10-topology';split=json.loads((HERE/'SPLITS.json').read_text())['groups'];rows=[]
 for p in sorted((src/'submissions').glob('*/*/*summary.csv')):
  r=next(csv.DictReader(p.open()));g=r['Problem'];n,degree=map(int,(src/'instances'/(g+'.dat')).read_text().split())
  formulation='flow'if'MIP-Flow'in p.parts[-3]else'linear'if'MIP-Seidel-Linear'in p.parts[-3]else'quadratic'
  seconds=float(r['Total Runtime'])
  if not np.isfinite(seconds)or seconds<0:raise ValueError('Invalid elapsed runtime')
  rows.append(dict(sample_id=g+'|'+formulation,group=g,target=min(seconds,7200.),partition=split[g],nodes=n,max_degree=degree,is_flow=int(formulation=='flow'),is_linear=int(formulation=='linear'),is_quadratic=int(formulation=='quadratic'),moore2_occupancy=n/(1+degree*degree),native_anchor=str(p.relative_to(data_root))+':row2;Total Runtime',source_elapsed_seconds=seconds,time_limit_reached=seconds>=7200,formulation=formulation,source_success=r['# Successful Runs']))
 d=pd.DataFrame(rows).sort_values(['group','formulation']).reset_index(drop=True)
 assert len(d)==48 and not d.sample_id.duplicated().any()
 return d
