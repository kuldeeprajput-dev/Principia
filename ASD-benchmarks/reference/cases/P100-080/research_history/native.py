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
 import zipfile,io,datetime
 z=zipfile.ZipFile(next(iter(sources(root).values())));rows=[]
 def load(n):
  lines=z.read(n).decode().splitlines();start=pd.Timestamp(lines[0].split(',')[0]).timestamp();fs=float(lines[1].split(',')[0]);x=np.loadtxt(io.StringIO('\n'.join(lines[2:])),delimiter=',');return start,fs,x
 for n in sorted(z.namelist()):
  if not ('/AEROBIC/' in n and n.endswith('/EDA.csv')):continue
  name=n.split('/')[-2];group=name.split('_')[0];start,fs,e=load(n);ts,tf,temp=load(n.replace('EDA.csv','TEMP.csv'));ats,af,acc=load(n.replace('EDA.csv','ACC.csv'));acc=acc/64;norm=np.linalg.norm(acc,axis=1)
  def segment(x,st,rate,a,b):
   i=int(np.ceil((a-st)*rate-1e-7));j=int(np.floor((b-st)*rate+1e-7))+1
   if i<0 or j>len(x) or j<=i:return None
   out=x[i:j];return out if np.isfinite(out).all() else None
  def avg(x,st,rate,a,b):
   q=segment(x,st,rate,a,b);return float(np.mean(q)) if q is not None else np.nan
  for sec in np.arange(120,(len(e)-1)/fs-30,5):
   t=start+sec;past=segment(e,start,fs,t-120,t);act=segment(norm,ats,af,t-10,t)
   if past is None or act is None:continue
   x=[avg(e,start,fs,t-5,t),avg(e,start,fs,t-15,t-10),avg(e,start,fs,t-35,t-30),float(past.mean()),float(act.std()),avg(temp,ts,tf,t-5,t),avg(temp,ts,tf,t-35,t-30),sec/60];y=avg(e,start,fs,t+25,t+30)
   if not np.isfinite(x+[y]).all():continue
   rows.append(dict(sample_id=name+':t'+str(int(sec)),group=group,target=y,**dict(zip(['level','lag10','lag30','mean120','activity','temperature','temperature30','elapsed'],x)),source_anchor=n+':futureEDA'+str(sec+25)+'to'+str(sec+30)+'s from native start',calibration_anchor=n+':EDA/TEMP/ACC timestamps<=issuance '+str(sec)+'s',linked_unit=group,prediction_elapsed_seconds=float(sec),target_end_elapsed_seconds=float(sec+30)))
 return finish(rows)
