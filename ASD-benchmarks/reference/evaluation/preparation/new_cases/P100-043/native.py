"""Deterministic source-hashed hot training trajectories and fixed early anchors."""
from pathlib import Path
import json,hashlib
import pandas as pd
import numpy as np
HERE=Path(__file__).resolve().parent
INPUTS=['tokens_B','anchor_tokens_B','early_tokens_B','anchor_loss','early_loss','params_B','width','depth']
def verify(data_root):
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  p=Path(data_root)/a['path']
  if not p.is_file()or p.stat().st_size!=a['bytes']or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Source missing or checksum mismatch: '+a['path'])
def prepare(data_root):
 verify(data_root);rel='43_ai_gemstones_training/raw/wandb_dfs/wandb_df_raw.jsonl';p=Path(data_root)/rel;split=json.loads((HERE/'SPLITS.json').read_text())['groups'];rows=[]
 for i,line in enumerate(p.read_text().splitlines(),1):
  r=json.loads(line)
  if not(r['pretrain']and not r['cooldown']):continue
  seq=sorted((int(k),float(v))for k,v in r['val_loss_by_optimiser_step'].items()if v is not None and np.isfinite(v)and v>0)
  a=[(k,v)for k,v in seq if 0<k*4194304<=20e9];e=[(k,v)for k,v in seq if 0<k*4194304<=10e9]
  if not a or not e:raise ValueError('Missing required early calibration: '+r['model_id'])
  k0,y0=a[-1];k1,y1=e[-1]
  if k1>=k0:raise ValueError('No distinct anchor intervals')
  for k,y in seq:
   if not 20e9<k*4194304<=100e9:continue
   g=r['model_id'];rows.append(dict(sample_id=f'{g}|hot|step={k}',group=g,target=y,partition=split[g]['partition'],tokens_B=k*4194304/1e9,anchor_tokens_B=k0*4194304/1e9,early_tokens_B=k1*4194304/1e9,anchor_loss=y0,early_loss=y1,params_B=r['params']/1e9,width=r['width'],depth=r['depth'],native_anchor=f'{rel}:line={i};val_loss_by_optimiser_step/{k}',calibration_anchor=f'{rel}:line={i};val_loss_by_optimiser_step/{k1},{k0}',model_id=g))
 d=pd.DataFrame(rows).sort_values(['group','tokens_B']).reset_index(drop=True)
 if d.sample_id.duplicated().any():raise ValueError('Duplicate sample identities')
 return d
