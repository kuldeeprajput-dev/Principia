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
 root=verify(data_root);file=root/'raw/SHED_public_use_data_2025_CSV.zip'
 with zipfile.ZipFile(file) as z:
  name=next(x for x in z.namelist() if x.endswith('public2025.csv'));d=pd.read_csv(z.open(name),low_memory=False);d['native_row']=np.arange(len(d))+2
 for k in ['EF3_h','D1A']:d[k]=d[k].map({'No':0,'Yes':1})
 d['ppinc7']=d.ppinc7.map({'Less than $10,000':1,'$10,000 to $24,999':2,'$25,000 to $49,999':3,'$50,000 to $74,999':4,'$75,000 to $99,999':5,'$100,000 to $149,999':6,'$150,000 or more':7})
 for k in ['weight','pphhsize','ppage']:d[k]=pd.to_numeric(d[k],errors='coerce')
 states=sorted(d.ppstaten.dropna().astype(str).unique(),key=lambda s:hashgroup('SHED-state:'+str(s)));held=set(states[:max(1,len(states)//5)]);good=d.EF3_h.isin([0,1])&d.ppinc7.between(1,7)&d.pphhsize.between(1,20)&d.ppage.between(18,100)&d.D1A.isin([0,1])&(d.weight>0)&d.ppstaten.notna();rows=[]
 for _,r in d[good].iterrows():
  state=str(r.ppstaten);rows.append(dict(sample_id=str(r.shedid),group='state:'+str(state),target=float(r.EF3_h),sample_weight=float(r.weight),partition='confirmation' if state in held else 'development',fold_key=hashgroup('SHED-fold:'+str(state))%5,income_proxy=[5,17.5,37.5,62.5,87.5,125,175][int(r.ppinc7)-1],household_size=float(r.pphhsize),shock=float(r.D1A==0),age=float(r.ppage),source_anchor=file.name+'!'+name+':row='+str(int(r.native_row)),input_anchor='ppinc7,pphhsize,D1A,ppage; whole state '+str(state),eligibility_reason='EF3_h0/1, complete declared inputs and positive final weight'))
 return pd.DataFrame(rows)
