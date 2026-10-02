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
 import zipfile,io
 p=sources(root);f=next(iter(p.values()));z=zipfile.ZipFile(f);n=next(n for n in z.namelist() if n.endswith('Nasioulas2024_data.csv'));a=pd.read_csv(io.BytesIO(z.read(n)));a['native_row']=np.arange(len(a))+2;rows=[]
 for (pid,block),b in a.groupby(['EXPID','BLOCK'],sort=True):
  b=b.sort_values('TRIAL');past=[];prev=None
  for _,r in b.iterrows():
   scale=abs(float(r.MAG_RISKY));evr=float(r.P_RISKY*r.MAG_RISKY);evs=float(r.P_SURE*r.MAG_SURE1+(1-r.P_SURE)*r.MAG_SURE2);ann=bool(r.BLOCK_INSTRUCTIONS==1);observed=prev is not None;known=ann or observed;fb=float(r.FEEDBACK) if ann else (float(prev.FEEDBACK) if observed else 0.);pe=regret=0.
   if prev is not None and prev.FEEDBACK==1:
    expected=prev.P_RISKY*prev.MAG_RISKY if prev.RISKY_CHOICE==1 else prev.P_SURE*prev.MAG_SURE1+(1-prev.P_SURE)*prev.MAG_SURE2
    pe=(float(prev.OUT)-float(expected))/abs(float(prev.MAG_RISKY))
    if prev.TYPE_FEEDBACK==1:regret=(float(prev.CF_OUT)-float(prev.OUT))/abs(float(prev.MAG_RISKY))
   rows.append(dict(sample_id=f'{int(pid)}:block{int(block)}:trial{int(r.TRIAL)}',group=str(int(pid)),target=float(r.RISKY_CHOICE),ev_difference=(evr-evs)/scale,probability=float(r.P_RISKY),valence=float(r.VALENCE),safe_risk=float(r.P_SURE<1),feedback_known=fb,feedback_observed=float(known),complete=(float(r.TYPE_FEEDBACK) if ann and fb>0 else (float(prev.TYPE_FEEDBACK) if observed and fb>0 else 0.)),trial_progress=(float(r.TRIAL)-1)/9,lag_choice=float(past[-1]) if past else .5,history_mean=(sum(past)+1)/(len(past)+2),visible_pe=pe,visible_regret=regret,has_history=float(bool(past)),source_anchor=f'{f.name}::{n}:row{int(r.native_row)}:RISKY_CHOICE',calibration_anchor='same participant and block, strictly preceding trials only',linked_unit=str(int(pid)),experiment=int(r.EXP),block=int(block),trial=int(r.TRIAL)))
   past.append(float(r.RISKY_CHOICE));prev=r
 d=finish(rows)
 if not d.target.isin([0,1]).all():raise ValueError('Nonbinary choice')
 return d
