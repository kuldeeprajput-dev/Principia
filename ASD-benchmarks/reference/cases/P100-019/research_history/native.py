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
 root=verify(data_root);file=root/'raw/COMPLAINTS_RECEIVED_2025-2026.zip'
 with zipfile.ZipFile(file) as z:
  name=z.namelist()[0];d=pd.read_csv(z.open(name),sep='\t',header=None,dtype=str,encoding='latin1',usecols=[0,1,3,4,5,15,16,45],keep_default_na=False);d.columns=['CMPLID','ODINO','make','model','modelyear','added','received','product'];d['native_row']=np.arange(len(d))+1
 d['date']=pd.to_datetime(d.received,format='%Y%m%d',errors='coerce');d['added_date']=pd.to_datetime(d.added,format='%Y%m%d',errors='coerce');d=d[(d['product']=='V')&d.date.notna()&d.make.ne('')&d.model.ne('')].copy();d['vehicle']=d.make.str.strip()+'|'+d.model.str.strip();d=d.sort_values(['ODINO','vehicle','native_row']).drop_duplicates(['ODINO','vehicle']);d['month']=d.date.dt.to_period('M');early=d[d.month<pd.Period('2025-07')];cohort=early.groupby('vehicle').ODINO.nunique();cohort=sorted(cohort[cohort>=6].index);months=pd.period_range('2025-01','2026-07',freq='M');counts=d.groupby(['vehicle','month']).ODINO.nunique();anchors=d.groupby(['vehicle','month']).native_row.agg(lambda x:','.join(map(str,x)));rows=[]
 for v in cohort:
  series=np.array([counts.get((v,m),0) for m in months],float)
  for j in range(6,len(months)):
   m=months[j];last=series[j-6:j];rows.append(dict(sample_id=v+':'+str(m),group=str(m),target=float(series[j]),partition='confirmation' if m>=pd.Period('2026-05') else 'development',fold_key=m.year*12+m.month,lag1=float(last[-1]),lag3=float(last[-3:].mean()),lag6=float(last.mean()),month=float(m.month),source_anchor=file.name+'!'+name+':ODINO-dedup vehicle='+v+';LDATE-month='+str(m)+';native_rows='+str(anchors.get((v,m),'')),input_anchor='ODINO-unique prior6LDATEcalendar months; fixedpreJuly2025cohort>=6complaints',eligibility_reason='Known vehicle make/model with>=6Jan–Jun2025received complaints; source productV; targetcount includes zero'))
 return pd.DataFrame(rows)
