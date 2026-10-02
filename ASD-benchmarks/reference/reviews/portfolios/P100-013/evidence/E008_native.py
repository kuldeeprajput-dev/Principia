from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd

def prepare(data_root):
 root=Path(data_root);manifest=json.loads((Path(__file__).parent.parent/'SOURCE_MANIFEST.json').read_text())
 for asset in manifest['assets']:
  p=root/asset['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Native source hash mismatch: '+asset['path'])
 p=root/'13_materials_nist_encapsulant_cure/raw/Figure 2-Conversion.xlsx';a=pd.read_excel(p,header=None);out=[]
 for j,beta in enumerate([1,3,5,10,20]):
  for i,row in a.iloc[2:].iterrows():
   t,y=row.iloc[j*4:j*4+2]
   if pd.isna(t) or pd.isna(y):continue
   out.append(dict(sample_id=f'rate{beta}:row{i+1}',group=f'rate{beta}',partition='confirmation' if beta==20 else 'development',temperature_K=float(t)+273.15,heating_rate_K_min=beta,target=float(y),source_asset=str(p.relative_to(root)),source_anchor=f'Figure2!{i+1}:columns{j*4+1}-{j*4+2}',eligibility='finite observed conversion; supplied fitted columns excluded',linked_group=f'rate{beta}'))
 return pd.DataFrame(out)
