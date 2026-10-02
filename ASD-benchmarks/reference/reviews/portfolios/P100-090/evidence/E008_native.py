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
 root=verify(data_root);file=root/'raw/ExperimentalData.zip';rows=[]
 with zipfile.ZipFile(file) as z:
  names=[n for n in z.namelist() if n.endswith('.csv') and '__MACOSX' not in n and '/Individual/' not in n and len(Path(n).parts) in [3,4]];groups=sorted({Path(n).parts[1]+'/'+(Path(n).parts[2] if len(Path(n).parts)==4 else Path(n).stem) for n in names});held=set()
  for country in sorted({g.split('/')[0] for g in groups}):
   gs=sorted([g for g in groups if g.startswith(country+'/')],key=lambda g:hashgroup('rotation:'+g))
   if len(gs)>1:held.update(gs[:max(1,len(gs)//5)])
  for name in sorted(names):
   d=pd.read_csv(z.open(name))
   if 'X(cm)' in d:d['X(m)']=d['X(cm)']/100;d['Y(m)']=d['Y(cm)']/100
   need=['Time(s)','Id-Ped','X(m)','Y(m)']
   if any(k not in d for k in need):raise ValueError('Unexpected trajectory schema '+name)
   d=d.sort_values(['Id-Ped','Time(s)']);grid=np.arange(int(np.ceil(d['Time(s)'].min())),int(np.floor(d['Time(s)'].max()))+1);end=len(grid)-1;ids=sorted(d['Id-Ped'].unique());X=np.full((len(grid),len(ids)),np.nan);Y=X.copy()
   for j,pid in enumerate(ids):
    a=d[d['Id-Ped']==pid];times=a['Time(s)'].to_numpy();k=np.searchsorted(times,grid,side='right')-1;ok=(k>=0)&((grid-times[np.maximum(k,0)])<=1.0);X[ok,j]=a['X(m)'].to_numpy()[k[ok]];Y[ok,j]=a['Y(m)'].to_numpy()[k[ok]]
   cx=np.nanmean(X,axis=1);cy=np.nanmean(Y,axis=1);rx=X-cx[:,None];ry=Y-cy[:,None];vx=np.vstack([np.full((1,len(ids)),np.nan),np.diff(X,axis=0)]);vy=np.vstack([np.full((1,len(ids)),np.nan),np.diff(Y,axis=0)]);speed=np.sqrt(vx*vx+vy*vy);rad=np.sqrt(rx*rx+ry*ry);valid=(speed>1e-3)&(rad>1e-3);spin=np.divide(rx*vy-ry*vx,rad*speed,out=np.full_like(rad,np.nan),where=valid);polar=np.nanmean(spin,axis=1);variance=np.nanvar(spin,axis=1);r90=np.nanquantile(rad,.9,axis=1);mean_speed=np.nanmean(speed,axis=1);init=float(np.nanmean(polar[1:3]));g=Path(name).parts[1]+'/'+(Path(name).parts[2] if len(Path(name).parts)==4 else Path(name).stem)
   for t in range(4,end-1,2):
    vals=[np.mean(polar[t+1:t+3]),polar[t],np.mean(polar[t-1:t+1]),init,np.sum(np.isfinite(X[t])&np.isfinite(Y[t]))/(np.pi*r90[t]**2),mean_speed[t],r90[t],variance[t]]
    if not np.isfinite(vals).all():continue
    rows.append(dict(sample_id=name+':origin='+str(int(grid[t])),group=g,target=float(vals[0]),partition='confirmation' if g in held else 'development',fold_key=hashgroup('rotation-fold:'+g)%5,p_now=float(vals[1]),p_past=float(vals[2]),p_initial=float(vals[3]),density=float(vals[4]),speed=float(vals[5]),radius90=float(vals[6]),polarization_variance=float(vals[7]),source_anchor=file.name+'!'+name+':targetseconds='+str(int(grid[t+1]))+'..'+str(int(grid[t+2]))+';XY-only-derived',input_anchor='same trajectory prefix throughseconds='+str(int(grid[t]))+';leftsamplehold,1sbackwardvelocity;relativeinitial1..2s calibration',eligibility_reason='Finite synchronized tracked positions,nonzero velocity/radius; full2snextwindow; relative trial time>=4s'))
 return pd.DataFrame(rows)
