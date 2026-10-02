from pathlib import Path
import json,hashlib,io,re,zipfile
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent

def sources(data_root):
 m=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
 base=Path(data_root)/m['scenario_id']
 for a in m['assets']:
  rel=Path(a['path'])
  if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe asset path')
  f=base/rel
  if not f.is_file() or f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing/corrupt native asset: '+str(rel))
 return base

def prepare(data_root):
 base=sources(data_root);fn='raw/DigitAF_Soil_All_LLs_Data.xlsx';d=pd.read_excel(base/fn,sheet_name='Data Ph, C, Bulk density, worms');s=json.loads((ROOT/'SPLITS.json').read_text());rows=[]
 for ix,r in d.iterrows():
  try:
   bd=float(r.iloc[21]);C=float(r.iloc[23]);ph=float(r.iloc[18]);country=str(r.iloc[1]);ss=re.findall(r'\d+(?:\.\d+)?',str(r.iloc[14]));depth=(float(ss[0])+float(ss[1]))/2
  except (ValueError,TypeError,IndexError):continue
  if not np.isfinite([bd,C,ph,depth]).all() or bd<=0 or C<0 or country not in s['all_countries']:continue
  rows.append(dict(sample_id=f'soil-row-{ix+2}',group=country,target=bd,partition='confirmation' if country in s['confirmation'] else 'development',fold=s['development'].index(country) if country in s['development'] else 9,C=C,depth=depth,pH=ph,source_anchor=fn+f':sheet:Data Ph, C, Bulk density, worms:row:{ix+2}',calibration_anchor='none',linked_unit=str(r.iloc[2])+'|'+str(r.iloc[5]),eligible_reason='Finite measured BD, Corg, pH and explicit depth interval; positive BD; nonnegative carbon'))
 return pd.DataFrame(rows)
