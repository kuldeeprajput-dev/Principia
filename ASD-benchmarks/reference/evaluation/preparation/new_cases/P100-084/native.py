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
 base=sources(data_root);archive=next((base/'raw').glob('*.zip'));z=zipfile.ZipFile(archive);s=json.loads((ROOT/'SPLITS.json').read_text());rows=[]
 for j,name in enumerate(s['members']):
  a=np.loadtxt(io.StringIO(z.read(name).decode()),skiprows=1);force=a[:,4]/1000;retract=a[:,5]/1000;baseline=float(np.mean(force[:10]));cross=np.flatnonzero(force>=baseline+5)
  if len(cross)==0:raise ValueError('Missing declared5nNapproachcalibrationcrossing')
  zc=float(a[cross[0],0]);zm=float(a[0,1]);peak=float(np.mean(retract[:5]));group=Path(name).name
  for k in range(16,len(a)):
   rows.append(dict(sample_id=group+f'-row-{k+2}',group=group,target=float(retract[k]),partition='confirmation' if name in s['confirmation_members'] else 'development',fold=j,x=float((a[k,1]-zc)/(zm-zc)),base=baseline,amp=peak-baseline,progress=float(k/(len(a)-1)),source_anchor=archive.relative_to(base).as_posix()+'::'+name+f':row:{k+2}:column:Defl_pN_Rt',calibration_anchor=archive.relative_to(base).as_posix()+'::'+name+':entire_approach_and_first5_retraction_points',linked_unit=name.split('/')[1],eligible_reason='Whole approach available before retraction; target after first16retractionpoints;5nNthresholdisfixedcalibrationrule'))
 return pd.DataFrame(rows)
