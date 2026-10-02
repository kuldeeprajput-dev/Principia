"""Threshold games: canonical session-1 pairs, one-step causal forecasts."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
CASE='87_economics_public_goods'
PARAMS={'Full_equality':(24,24,1,1),'Endowment_inequality':(36,12,1,1),'Productivity_inequality':(24,24,3,1),'Aligned_inequality':(36,12,3,1),'Misaligned_inequality':(36,12,1,3)}
def prepare(data_root):
 p=Path(data_root)/CASE
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  q=p/a['path']
  if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native asset missing or checksum mismatch: '+a['path'])
 book=pd.ExcelFile(p/'raw/ThresholdPGG_ExperimentalData.xlsx'); rows=[]
 for treatment,(e1,e2,p1,p2) in PARAMS.items():
  sheet=treatment+'_Type1';d=pd.read_excel(book,sheet,header=None); n=(len(d)-1)//4
  ids=[treatment+'-pair'+str(i+1) for i in range(n)]
  reserved=set(sorted(ids,key=lambda x:hashlib.sha256(('p100-batch5-87-'+x).encode()).hexdigest())[:max(1,round(n*.2))]);remaining=sorted(set(ids)-reserved);folds={g:i%5 for i,g in enumerate(sorted(remaining,key=lambda x:hashlib.sha256(('fold-'+x).encode()).hexdigest()))}
  for i,g in enumerate(ids):
   first=1+4*i;A=d.iloc[first:first+2,2:22].to_numpy(float);theta=(p1*e1+p2*e2)/2
   if not np.isfinite(A).all():raise ValueError('Malformed native contribution')
   for role in range(2):
    endowment=[e1,e2][role];peer_endowment=[e2,e1][role];prod=[p1,p2][role];peer_prod=[p2,p1][role]
    for t in range(2,20):
     prev=A[role,t-1];peer=A[1-role,t-1]; total=p1*A[0,t-1]+p2*A[1,t-1]
     rows.append(dict(sample_id=g+'-player'+str(role+1)+'-round'+str(t+1),group=g,target=A[role,t],partition='confirmation' if g in reserved else 'development',round=t+1,own_previous=prev,peer_previous=peer,own_lag2=A[role,t-2],peer_lag2=A[1-role,t-2],own_history_mean=float(A[role,:t].mean()),peer_history_mean=float(A[1-role,:t].mean()),endowment=endowment,peer_endowment=peer_endowment,productivity=prod,peer_productivity=peer_prod,threshold=theta,previous_success=float(total>=theta-1e-9),required_contribution=np.clip((theta-peer_prod*peer)/prod,0,endowment),treatment=treatment,role=role+1,source_anchor='raw/ThresholdPGG_ExperimentalData.xlsx!'+sheet+':row='+str(first+role+1)+':column='+str(t+3),calibration_anchor='same player and peer pair, rounds strictly before '+str(t+1),eligibility_reason='session1 canonical Type1; rounds3-20; surveys/session2 excluded',fold='confirm' if g in reserved else 'fold'+str(folds[g])))
 return pd.DataFrame(rows)
