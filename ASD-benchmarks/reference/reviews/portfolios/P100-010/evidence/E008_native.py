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
 root=verify(data_root);f=root/'raw/nvdcve-2.0-recent.json';r=json.loads(f.read_text());snapshot=pd.Timestamp(r['timestamp']);cs=[a['cve'] for a in r['vulnerabilities']];meta=[]
 for idx,c in enumerate(cs):
  if c['vulnStatus']=='Rejected':continue
  pub=pd.Timestamp(c['published']);age=(snapshot-pub).total_seconds()/86400
  if age<0:continue
  meta.append((idx,c,pub,age))
 batch={}
 for _,c,pub,age in meta:
  k=(c['sourceIdentifier'],str(pub.date()));batch[k]=batch.get(k,0)+1
 sources=sorted({c['sourceIdentifier'] for _,c,_,_ in meta},key=lambda s:hashgroup('NVD-source:'+s));held=set(sources[:max(1,len(sources)//5)]);rows=[]
 for idx,c,pub,age in meta:
  metrics=c.get('metrics',{}).get('cvssMetricV31',[]);src=c['sourceIdentifier'];rows.append(dict(sample_id=c['id'],group=src,target=float(any(a.get('source','').lower()=='nvd@nist.gov' for a in metrics)),partition='confirmation' if src in held else 'development',fold_key=hashgroup('NVD-fold:'+src)%5,age_days=age,cna_score=float(any(a.get('source','').lower()!='nvd@nist.gov' for a in metrics)),batch_size=float(batch[(src,str(pub.date()))]),source_anchor=f.name+':vulnerabilities['+str(idx)+'].cve.metrics.cvssMetricV31',input_anchor='published timestamp,non-NVD CVSSv3.1 presence,source-day batch count at snapshot '+str(snapshot),eligibility_reason='Non-rejected CVE; nonnegative publication age'))
 return pd.DataFrame(rows)
