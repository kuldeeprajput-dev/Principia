from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd

def prepare(data_root):
 root=Path(data_root);manifest=json.loads((Path(__file__).parent.parent/'SOURCE_MANIFEST.json').read_text())
 for asset in manifest['assets']:
  p=root/asset['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Native source hash mismatch: '+asset['path'])
 p=root/'56_structures_timber_concrete/raw/experimental results_summary.xlsx';a=pd.read_excel(p,sheet_name='graphs',header=None);out=[]
 for j,name in enumerate(['P-NWC-A','P-NWC-B','P-NWC-C','P-LWC-A','P-LWC-B','P-LWC-C']):
  c=17+3*j;xy=[]
  for i,row in a.iloc[6:].iterrows():
   d,f=row.iloc[c:c+2]
   if isinstance(d,(int,float)) and isinstance(f,(int,float)) and np.isfinite(d) and np.isfinite(f):xy.append((i+1,float(d),float(f)/1000))
  # Calibration is a causal prefix stopping at the first d>10; later unloading cannot re-enter calibration.
  prefix=[]
  for row in xy:
   if row[1]>10:break
   prefix.append(row)
  valid=[r for r in prefix if r[1]>0]
  if len(valid)<2:raise ValueError('Insufficient calibration '+name)
  last=valid[-1];earlier=[r for r in valid if r[1]<=last[1]/2];prev=earlier[-1] if earlier else valid[0]
  k0=last[2]/last[1]; kr=(last[2]-prev[2])/(last[1]-prev[1]);cal=';'.join(f'graphs!row{r[0]}:columns{c+1}-{c+2}' for r in prefix)
  for i,d,f in xy[len(prefix):]:
   if d<=10:continue
   out.append(dict(sample_id=f'{name}:row{i}',group=name,partition='confirmation' if name.endswith('C') else 'development',deflection_mm=d,calibration_deflection_mm=last[1],calibration_force_kN=last[2],initial_stiffness_kN_mm=k0,recent_stiffness_kN_mm=kr,lightweight=int('LWC' in name),target=f,source_asset=str(p.relative_to(root)),source_anchor=f'graphs!row{i}:columns{c+1}-{c+2}',calibration_anchors=cal,eligibility='finite d>10mm after calibration prefix; damage/drop points retained',linked_group=name))
 return pd.DataFrame(out)
