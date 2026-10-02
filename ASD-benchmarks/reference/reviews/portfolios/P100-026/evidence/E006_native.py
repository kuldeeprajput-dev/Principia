"""Deterministic, hash-verified native preparation; no scientific fitting."""
from pathlib import Path
import json,hashlib,io,zipfile,csv,tarfile
import numpy as np
import pandas as pd

def prepare(data_root):
 root=Path(__file__).resolve().parent;meta=json.loads((root/'SOURCE_MANIFEST.json').read_text());split=json.loads((root/'SPLITS.json').read_text());data_root=Path(data_root)
 for a in meta['files']:
  if Path(a['path']).is_absolute() or '..' in Path(a['path']).parts:raise ValueError('Unsafe source path')
  p=data_root/a['path']
  if not p.is_file() or p.stat().st_size!=a['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Source asset checksum mismatch/missing: '+a['path'])
 src=data_root/meta['source_folder'];case=int(meta['case_id'][-3:]);rows=[]
 def add(group,anchor,target,**kw):
  rows.append(dict(sample_id=f'{meta["case_id"]}:{anchor}',group=str(group),target=float(target),source_anchor=anchor,eligibility_reason='finite measured response and declared task domain',**kw))
 if case==6:
  n='FIG3b_IonSpectra_with_ProbeRabiFrequency.csv';d=pd.read_csv(src/'raw'/n);d.columns=['detuning','rabi','y'];u=np.sort(d.rabi.unique());look={v:i for i,v in enumerate(u)}
  for i,r in d.loc[d.detuning.abs()<=60].iterrows():
   q=look[r.rabi];g=f'rabi-block-{q//30:02d}'
   if np.isfinite(r.y):add(g,f'{n}:row{i+2}',r.y,detuning_MHz=r.detuning,rabi_MHz=r.rabi,condition_id=f'omega-{q:03d}',fold=f'block-{q//30:02d}')
 elif case==22:
  z=zipfile.ZipFile(src/'raw/dataset.zip');seen={}
  for comp,n in [(0,'dataset/Figure 3(a).xlsx'),(1,'dataset/Figure 3(d).xlsx')]:
   a=pd.read_excel(io.BytesIO(z.read(n)),header=None)
   for j in range(50):
    d=a.iloc[:,2*j:2*j+2].dropna().astype(float);key=hashlib.sha256(d.to_numpy().tobytes()).hexdigest()
    if key in seen:continue
    g=('Br' if comp else 'I')+f'-device-{j+1:02d}';seen[key]=g
    for k,r in d.iloc[:100].iterrows():
     if r.iloc[0]>=.05 and np.isfinite(r.iloc[1]):add(g,f'{n}:row{k+1}:columns{2*j+1}-{2*j+2}',r.iloc[1]*1e6,voltage_V=r.iloc[0],bromine_rich=comp,condition_id=g,fold='fold-'+str(int(hashlib.sha256(g.encode()).hexdigest(),16)%5))
 elif case==26:
  import py7zr
  from py7zr.io import BytesIOFactory
  fac=BytesIOFactory(2000000)
  with py7zr.SevenZipFile(src/'raw/zenodo raw data.7z') as z:
   ns=[n for n in z.getnames() if 'reaction_' in n and 'Figure1_' not in n];z.extract(targets=ns,factory=fac)
  for n in ns:
   text=fac.get(n).read().decode(errors='replace');d=pd.read_csv(io.StringIO(text),sep='\t',skiprows=3,header=None);t=pd.to_numeric(d.iloc[:,0],errors='coerce');y=pd.to_numeric(d.iloc[:,6],errors='coerce');valid=np.isfinite(t)&np.isfinite(y);d=pd.DataFrame({'t':t[valid],'y':y[valid],'native_row':np.flatnonzero(valid)+4})
   # Restart segments are kept together; calibration from each segment separately.
   d['segment']=(d.t.diff()<0).cumsum();g=Path(n).stem;ag=1 if '_Ag1-' in n else 5 if '_Ag5-' in n else 20
   for seg,e in d.groupby('segment'):
    cal=e[e.t<=300];late=e[(e.t>300)&(e.t<=1500)];win=cal[cal.t>=120]
    if len(cal)<2 or len(win)<2:raise ValueError('Insufficient fixed causal calibration '+n)
    last=cal.sort_values('t').iloc[-1];slope=float(np.sum((win.t-win.t.mean())*(win.y-win.y.mean()))/np.sum((win.t-win.t.mean())**2))
    for i,r in late.iterrows():add(g,f'{n}:row{int(r.native_row)}',r.y,elapsed_min=r.t-last.t,anchor_selectivity_pct=last.y,prefix_slope_pct_min=slope,ag_wt_pct=ag,condition_id=g+f':segment{seg}',calibration_anchor=f'{n}:segment{seg}:t<=300',fold=g)
 elif case==30:
  z=zipfile.ZipFile(src/'raw/dataset.zip');seen=set()
  definitions=[('concentration',['PEG','P5','P2','P1'],[0,5,2,1]),('functionalization',['PEG','P5','N','NS'],[0,5,5,5]),('suppliers',['PEG','P5','PCH','NG'],[0,5,5,5])]
  for kind,groups,cs in definitions:
   n=f'dataset/CoF dataset {kind}.csv';a=list(csv.reader(io.StringIO(z.read(n).decode('utf-8-sig'))))
   for j,(g,c) in enumerate(zip(groups,cs),1):
    arr=np.array([[float(r[0]),float(r[j])] for r in a[18:43]]);key=hashlib.sha256(arr.tobytes()).hexdigest()
    if key in seen:continue
    seen.add(key);lo=float(arr[arr[:,0]==.2,1][0]);hi=float(arr[arr[:,0]==500,1][0])
    for k,(v,y) in enumerate(arr):
     if .2<v<=10:add(g,f'{n}:row{k+19}:column{j+1}',y,speed_mm_s=v,boundary_cof=lo,highspeed_cof=hi,concentration_wt_pct=c,condition_id=f'{kind}:{g}',calibration_anchor=f'{n}:rows19,43:column{j+1}',fold=g)
 elif case==63:
  import h5py
  t=tarfile.open(src/'raw/iRRYHMPwMObNsUOM.tar');n=next(m.name for m in t.getmembers() if '/dataset/Figure6' in m.name and m.name.endswith('.h5'))
  with h5py.File(io.BytesIO(t.extractfile(n).read())) as f:
   freq=f['f'][:]/1e9
   for T in [77,195,293,352,389]:
    B=f[f'B_{T}K'][:];a=f[f'Sn_{T}K'][:]
    for bi,b in enumerate(B):
     for fi,fr in enumerate(freq):
      if np.isfinite(a[bi,fi]):add(f'T{T}',f'{n}:Sn_{T}K[{bi},{fi}]',a[bi,fi],frequency_GHz=fr,field_T=b,termination_K=T,condition_id=f'T{T}:B{bi:02d}',fold=f'T{T}')
 elif case==65:
  z=zipfile.ZipFile(src/'raw/data-pr.zip');a=np.loadtxt(io.BytesIO(z.read('figure 8.txt')))
  for db,j in [(-30,0),(-20,2),(-15,4)]:
   for i,r in enumerate(a):
    f,y=r[j:j+2]
    if 100<=f<=1e6 and np.isfinite(y) and y>0:add(f'ratio{db}',f'figure 8.txt:row{i+1}:columns{j+1}-{j+2}',10*np.log10(y),frequency_Hz=f,injection_dB=db,condition_id=f'ratio{db}',fold='frequency-band-'+str(min(3,int(np.log10(f)-2))))
 d=pd.DataFrame(rows)
 if case==22:
  conf=[]
  for prefix in ['I-','Br-']:
   gs=[g for g in d.group.unique() if g.startswith(prefix)];conf.extend(sorted(gs,key=lambda g:hashlib.sha256(('ASD6-device-v1|'+g).encode()).hexdigest())[:10])
 else:conf=split['confirmation']
 d['partition']=np.where(d.group.isin(conf),'confirmation','development')
 if d.sample_id.duplicated().any() or not np.isfinite(d.target).all():raise ValueError('Invalid native identities/targets')
 return d.reset_index(drop=True)
