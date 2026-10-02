from pathlib import Path
import json,hashlib,zipfile,io,gzip
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def hashgroup(s):return int(hashlib.sha256(('principia100-batch7:'+str(s)).encode()).hexdigest()[:16],16)
def verify(data_root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in m['assets']:
  f=Path(data_root)/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native SHA256 mismatch: '+a['path'])
 return Path(data_root)/m['folder']
def prepare(data_root):
 root=verify(data_root);file=root/'raw/cfpb_nafbs-puf-unlabeled_2026-02.csv';d=pd.read_csv(file,encoding='utf-8-sig',low_memory=False);d['native_row']=np.arange(len(d))+2
 cols=['BRANCH','MOBILE','WEB','WEIGHT_FINAL','AGE7','INCOME9','REGION4','BR_PRESENT','BR_NET_CLOSED']
 for k in cols:d[k]=pd.to_numeric(d[k],errors='coerce')
 regions=sorted([1,2,3,4],key=lambda r:hashgroup('CFPB-region:'+str(r)));held=regions[0];good=d.BRANCH.isin([1,2])&d.MOBILE.isin([1,2])&d.WEB.isin([1,2])&d.AGE7.between(1,7)&d.INCOME9.between(1,9)&d.REGION4.isin([1,2,3,4])&d.BR_PRESENT.isin([1,2])&d.BR_NET_CLOSED.isin([1,2])&(d.WEIGHT_FINAL>0);rows=[]
 for _,r in d[good].iterrows():
  region=int(r.REGION4);rows.append(dict(sample_id=str(r.CASEID),group='region:'+str(region),target=float(r.BRANCH==1),sample_weight=float(r.WEIGHT_FINAL),partition='confirmation' if region==held else 'development',fold_key=region,mobile=float(r.MOBILE==1),web=float(r.WEB==1),age_category=float(r.AGE7),income_category=float(r.INCOME9),branch_present=float(r.BR_PRESENT==1),branch_closed=float(r.BR_NET_CLOSED==1),source_anchor=file.name+':row='+str(int(r.native_row)),input_anchor='MOBILE,WEB,AGE7,INCOME9,BR_PRESENT,BR_NET_CLOSED',eligibility_reason='BRANCH and digital questions1/2; valid declared covariates; positive WEIGHT_FINAL'))
 return pd.DataFrame(rows)
