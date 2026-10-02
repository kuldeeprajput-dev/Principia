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
 root=verify(data_root);rows=[];exclusions=[]
 for wave in ['2603','2605']:
  file=root/'raw'/('HTOPS_HPS_'+wave+'_CSV.zip')
  with zipfile.ZipFile(file) as z:
   name=next(x for x in z.namelist() if x.endswith('PUF.csv') and 'REPWGT' not in x);d=pd.read_csv(z.open(name));d['native_row']=np.arange(len(d))+2
  for k in ['FD_SUFF','HWEIGHT','RHHINCOME','THHLD_NUMPER','WORKLOSS','TAGE','REGION']:d[k]=pd.to_numeric(d[k],errors='coerce')
  good=d.FD_SUFF.isin([1,2,3,4])&d.RHHINCOME.between(1,7)&d.THHLD_NUMPER.between(1,7)&d.WORKLOSS.isin([1,2])&d.TAGE.between(18,100)&d.REGION.isin([1,2,3,4])&(d.HWEIGHT>0)
  for _,r in d[good].iterrows():
   rows.append(dict(sample_id=wave+':'+str(r.SCRAMID),group=wave+':region'+str(int(r.REGION)),target=float(r.FD_SUFF in [3,4]),sample_weight=float(r.HWEIGHT),partition='development' if wave=='2603' else 'confirmation',fold_key=int(r.REGION),income_proxy=[12.5,30,42.5,62.5,87.5,125,175][int(r.RHHINCOME)-1],household_size=float(r.THHLD_NUMPER),shock=float(r.WORKLOSS==1),age=float(r.TAGE),source_anchor=file.name+'!'+name+':row='+str(int(r.native_row)),input_anchor='RHHINCOME,THHLD_NUMPER,WORKLOSS,TAGE; wave='+wave,eligibility_reason='FD_SUFF1–4 and complete declared inputs; positive HWEIGHT'))
 return pd.DataFrame(rows)
