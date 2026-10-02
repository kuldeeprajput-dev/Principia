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
 base=sources(data_root);fn='raw/DLR__LiGrHydra0b__20221114__GITT__25degC__Basytec.txt'
 d=pd.read_csv(base/fn,sep=r'\s+',skiprows=13,header=None,encoding='latin1');d.columns=['hours','dataset','tset','line','command','U','I','ahkg','ach','adis','astep','askg','aset','asetkg','temp','cycle','state'];d['segment']=d.command.ne(d.command.shift()).cumsum();groups=[];previous=None
 for seg,g in d.groupby('segment',sort=True):
  if g.command.iloc[0]=='Pause' and previous is not None and previous.command.iloc[0] in ['Charge','Discharge'] and (g.hours.iloc[-1]-g.hours.iloc[0])*3600>=1800:
   groups.append((int(seg),g,previous))
  previous=g
 rows=[];N=len(groups);cut=int(np.floor(N*.8))
 for j,(seg,g,prev) in enumerate(groups):
  t=(g.hours.to_numpy()-g.hours.iloc[0])*3600;u=g.U.to_numpy();ix60=np.flatnonzero(t<=60)[-1];ix120=np.flatnonzero(t<=120)[-1];ix10=np.flatnonzero(t<=10)[-1];group=f'pulse-{seg:04d}'
  for aim in [300,600,1200,1800]:
   ix=int(np.argmin(abs(t-aim)))
   if abs(t[ix]-aim)>15:continue
   rows.append(dict(sample_id=group+f'-row-{int(g.index[ix])+14}',group=group,target=float(u[ix]),partition='development' if j<cut else 'confirmation',fold=min(4,int(j*5/cut)) if j<cut else 5,t=float(t[ix]),t60=float(t[ix60]),t120=float(t[ix120]),u60=float(u[ix60]),u120=float(u[ix120]),u10=float(u[ix10]),pulse_s=float((prev.hours.iloc[-1]-prev.hours.iloc[0])*3600),current=float(prev.I.iloc[-1]),source_anchor=fn+f':line:{int(g.index[ix])+14}',calibration_anchor=fn+f':lines:{int(g.index[ix60])+14},{int(g.index[ix120])+14},{int(g.index[ix10])+14}',linked_unit='Hydra.0b_A',eligible_reason='Pause after current pulse; target timestamp within15s of fixed horizon; calibration at or before120s'))
 return pd.DataFrame(rows)
