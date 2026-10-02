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
 base=sources(data_root);fn='raw/data.zip';z=zipfile.ZipFile(base/fn);member='01_XANES/LFP/LFP_raw_0-Binning_01-194.dat';a=np.loadtxt(io.BytesIO(z.read(member)));refname='01_XANES/LFP/LFP_references_FePO4_LiFePO4.xmu';r=np.loadtxt(io.BytesIO(z.read(refname)));E=a[:,0];re=r[:,0];pre=(E>=7000)&(E<=7050);post=(E>=7250)&(E<=7300);rp=(re>=7000)&(re<=7050);rr=(re>=7250)&(re<=7300);norm=(r[:,1:]-np.nanmean(r[rp,1:],axis=0))/(np.nanmean(r[rr,1:],axis=0)-np.nanmean(r[rp,1:],axis=0));rF=np.interp(E,re,norm[:,0]);rL=np.interp(E,re,norm[:,1]);dL=np.interp(E,re,np.gradient(norm[:,1],re));d2L=np.interp(E,re,np.gradient(np.gradient(norm[:,1],re),re));s=json.loads((ROOT/'SPLITS.json').read_text());rows=[]
 for col in range(1,a.shape[1]):
  u=a[:,col];base_mu=float(np.nanmean(u[pre]));jump=float(np.nanmean(u[post])-base_mu);time=(col-.5)*300;phase=0 if col<=107 else 1 if col<=131 else 2 if col<=170 else 3;f=float(np.clip(time/31981,0,1)) if phase<2 else float(np.clip(1-(time-39181)/11684,0,1));group=f'triplet-{(col-1)//3:02d}'
  if not np.isfinite([base_mu,jump]).all() or jump<=0:continue
  for k in np.flatnonzero((E>=7070)&(E<=7200))[::5]:
   if not np.isfinite(u[k]):continue
   rows.append(dict(sample_id=f'spectrum-{col:03d}-energyrow-{k+1}',group=group,target=float(u[k]),partition='confirmation' if group in s['confirmation_groups'] else 'development',fold=((col-1)//3)//13,pre=base_mu,jump=jump,rL=float(rL[k]),rF=float(rF[k]),dL=float(dL[k]),d2L=float(d2L[k]),f=f,discharge=float(phase>=2),rest=float(phase%2),e=float(E[k]-7112),source_anchor=fn+'::'+member+f':energyrow:{k+1}:spectrum:{col}',calibration_anchor=fn+'::'+member+f':spectrum:{col}:bands:7000-7050eV,7250-7300eV;reference:'+refname,linked_unit='single-LFP-charge-discharge-cycle',eligible_reason='Positivefinitecalibrationjump;fixed5eVsamplingnearFeedge;unbinnednativecolumnonly'))
 return pd.DataFrame(rows)
