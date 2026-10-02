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
 root=verify(data_root);rows=[]
 for country,file in [('USA','prgusap2.csv'),('Japan','prgjpnp2.csv')]:
  d=pd.read_csv(root/'raw'/file,sep=';',low_memory=False);d['native_row']=np.arange(len(d))+2
  for k in ['AGEG5LFS','YRSQUALC2','EARNHRDCLC2','SPFWT0']:d[k]=pd.to_numeric(d[k],errors='coerce')
  # Codes beyond scientific domains are published missing codes, never earnings.
  good=d.AGEG5LFS.between(3,10)&d.YRSQUALC2.between(0,30)&d.EARNHRDCLC2.between(1,10)&d.SPFWT0.gt(0)
  for _,r in d[good].iterrows():
   sid=country+':'+str(r.SEQID);bucket=hashgroup('PIAAC:'+sid)%10;rows.append(dict(sample_id=sid,group=country+':respondentblock'+str(bucket),target=float(r.EARNHRDCLC2>=8),sample_weight=float(r.SPFWT0),partition='confirmation' if bucket in [0,1] else 'development',fold_key=bucket//2,education=float(r.YRSQUALC2),age=[17.5,22,27,32,37,42,47,52,57,62.5][int(r.AGEG5LFS)-1],japan=float(country=='Japan'),source_anchor=file+':row='+str(int(r.native_row))+';EARNHRDCLC2',input_anchor='AGEG5LFS,YRSQUALC2,country; PVNUM1..10 forbidden in prediction',eligibility_reason='Age25–65,education0–30,positive uncoded PPP hourly wage and final weight'))
 return pd.DataFrame(rows)
