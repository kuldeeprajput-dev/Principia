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
 import zipfile,io,re
 from scipy.signal import detrend,periodogram,find_peaks
 p=sources(root);f=next(iter(p.values()));z=zipfile.ZipFile(f);n=next(n for n in z.namelist() if n.endswith('quality-hr-ann.csv'));ann=pd.read_csv(io.BytesIO(z.read(n)));meta=pd.read_csv(io.BytesIO(z.read(next(n for n in z.namelist() if n.endswith('subject-info.csv'))))).set_index('ID');headers={Path(n).stem.split('_')[0]:n for n in z.namelist() if n.endswith('_PPG.hea')};rows=[]
 for row,r in ann.iterrows():
  sid=str(int(r.ID));hr=float(r.HR)
  if not np.isfinite(hr) or hr<=0:continue
  hn=headers[sid];lines=[l for l in z.read(hn).decode().splitlines() if l.strip() and not l.startswith('#')];first=lines[0].split();channels=int(first[1]);fs=float(first[2]);frames=int(first[3]);b=np.frombuffer(z.read(hn.replace('.hea','.dat')),dtype='<i2').astype(float);g=[];zero=[]
  for l in lines[1:]:
   fields=l.split()
   if fields[1]!='16':raise ValueError('Unsupported WFDB encoding')
   m=re.match(r'([^()]+)\(([^()]+)\)/',fields[2])
   if m is None:raise ValueError('Missing explicit WFDB gain/baseline')
   g.append(float(m.group(1)));zero.append(float(m.group(2)))
  if channels!=len(g) or len(b)!=channels*frames:raise ValueError('Unexpected source waveform layout')
  if frames==1 and channels==300:x=(b-np.asarray(zero))/np.asarray(g)
  elif channels==3 and frames==300:
   names=[l.split()[-1] for l in lines[1:]]
   if 'PPG_R' not in names:raise ValueError('Missing declared red channel')
   signals=(b.reshape(frames,channels)-np.asarray(zero))/np.asarray(g);x=signals[:,names.index('PPG_R')]
  else:raise ValueError('Unsupported PPG source layout')
  if not np.isfinite(x).all() or len(x)<fs*5 or np.std(x)==0:continue
  x=detrend(x,type='linear');x=x/(np.std(x)+1e-15);freq,power=periodogram(x,fs=fs,window='hann',nfft=4096,detrend=False);ok=(freq>=.5)&(freq<=4);ff=freq[ok];pp=power[ok];peak=float(ff[np.argmax(pp)]);half=peak/2 if peak>=1 else peak;near=np.abs(ff-half)<.1;halfstrength=float(pp[near].max()/max(pp.max(),1e-15)) if near.any() else 0;quality=float(pp[np.abs(ff-peak)<.12].sum()/max(pp.sum(),1e-15));ac=np.correlate(x,x,mode='full')[len(x)-1:];lags=np.arange(max(1,int(fs/4)),min(len(x)-1,int(fs/.5))+1);peaks=find_peaks(ac[lags])[0];acf=float(fs/lags[peaks[np.argmax(ac[lags[peaks]])]]) if len(peaks) else peak;md=meta.loc[int(sid)]
  rows.append(dict(sample_id=sid,group=sid[:3],target=hr,fft_bpm=60*peak,acf_bpm=60*acf,half_bpm=60*half,half_strength=halfstrength,spectral_quality=quality,agreement=abs(60*(peak-acf)),motion=int(str(md.Motion)!='0'),ear=int(md['Ear/finger']),source_quality=int(r.Quality),source_anchor=f.name+'::'+n+':row'+str(row+2)+':HR; ECG reference',calibration_anchor='none; input '+hn+' plus matching PPG.dat',linked_unit=sid[:3],waveform_samples=len(x),sample_rate=fs))
 return finish(rows)
