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
 import zipfile,io,math
 from scipy.io import wavfile
 from scipy.signal import resample_poly,welch,periodogram
 paths=sources(root);z=zipfile.ZipFile(paths['SoundsDatabase.zip']);species=json.loads((HERE/'SPECIES.json').read_text());rows=[]
 for n in sorted(z.namelist()):
  if not n.endswith('.wav'):continue
  p=Path(n).stem.split('-');sp=p[1].replace('WidlBoar','WildBoar');group=sp+':'+p[0]
  if p[3] not in ['Positive','Negative']:raise ValueError('Unrecognized source context label')
  fs,x=wavfile.read(io.BytesIO(z.read(n)));dtype=x.dtype
  if np.issubdtype(dtype,np.integer):x=x.astype(float)/max(abs(np.iinfo(dtype).min),np.iinfo(dtype).max)
  else:x=x.astype(float)
  if x.ndim==2:x=x.mean(axis=1)
  if not np.isfinite(x).all() or len(x)<2 or np.std(x)==0:continue
  duration=len(x)/fs;rms=np.sqrt(np.mean(x*x));g=math.gcd(fs,8000);x=resample_poly(x,8000//g,fs//g);x=x-x.mean();f,pow=welch(x,fs=8000,nperseg=min(1024,len(x)));ok=f>=30;f=f[ok];pow=pow[ok];q=pow/(pow.sum()+1e-30);cent=float(np.sum(f*q));peak=float(f[np.argmax(pow)]);entropy=float(-np.sum(q*np.log(q+1e-30))/np.log(len(q)));flat=float(np.exp(np.mean(np.log(pow+1e-30)))/(pow.mean()+1e-30));N=len(x)//160
  if N>=2:
   env=np.sqrt(np.mean(x[:N*160].reshape(N,160)**2,axis=1));cv=float(env.std()/(env.mean()+1e-30));mf,mp=periodogram(env,fs=50,nfft=max(256,N));keep=(mf>=.5)&(mf<=20);mod=float(mf[keep][np.argmax(mp[keep])])
  else:cv=0;mod=.5
  rows.append(dict(sample_id=Path(n).name,group=group,target=int(p[3]=='Positive'),log_duration=np.log(max(duration,.001)/1),log_centroid=np.log(cent/1000),log_peak=np.log(peak/1000),high_share=float(q[f>=1000].sum()),entropy=entropy,flatness=flat,envelope_cv=cv,log_modulation=np.log(mod/1),log_rms=np.log(max(rms,1e-20)),species_code=species.index(sp),source_anchor='SoundsDatabase.zip::'+n+';filenamePositive/Negative label; DataS1 contextual documentation',calibration_anchor='No labeled held-animal calibration; waveform only',linked_unit=group,source_species_label=p[1]))
 return finish(rows)
