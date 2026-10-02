"""Explicit information-contract changes, computed from native source records."""
from pathlib import Path
import json,re,io,zipfile,hashlib
import numpy as np,pandas as pd,scipy.io,openpyxl
from . import _source,_port,_meta,_sha

def supplemental_folder(case,supplemental_root):
 if supplemental_root is None:raise ValueError('This optional task requires explicit --supplemental-root; core local-datas is insufficient')
 p=Path(supplemental_root);spec=_meta('supplemental_assets.json')[str(case)]
 # Accept direct payload folder or standardized scenario child, never search a research tree.
 bases=[p,p/str(case),p/f'P100-{case:03}'];candidates=[q/suffix for q in bases for suffix in ['', 'data/3_C_vehiclized','sources/data/3_C_vehiclized','fresh_materials']]
 found=[q for q in candidates if all((q/a['path']).is_file() for a in spec)]
 if not found:raise ValueError(f'Supplemental native files for case {case} absent under declared root')
 q=found[0]
 for a in spec:
  f=q/a['path']
  if f.stat().st_size!=a['bytes'] or _sha(f)!=a['sha256']:raise ValueError('Supplemental file checksum/size mismatch: '+a['path'])
 return q

def transform(task,d,data_root,supplemental_root):
 case=int(task['case_number']);family=task['family'];source=_source(data_root,case)
 if family=='supplemental':
  p=supplemental_folder(case,supplemental_root);m=_port('pla');m.FRESH=p;d=m.read_partition({k:m.CAL[k]+m.RESERVED[k] for k in m.CAL});material=task['task_id'].split('supplemental-')[1].rsplit('-',1)[0];d=d[d.material==material].copy();d['partition']=np.where(d.temperature_C.isin(m.RESERVED[material]),'confirmation','calibration')
  if '-loss.' in task['task_id']:d['target']=d.loss_modulus
  return d
 if family=='continuation':
  if case==58:d['loss_modulus_secondary_response']=d.loss_modulus
  if case==52:
   b=scipy.io.loadmat(source/'raw/NoTurbine_ABL_Type_II.mat',simplify_cells=True)['NoTurbine_ABL_TypeII'];grids={int(re.search(r'_(\d+)D$',k)[1]):v['uu'] for k,v in b.items() if isinstance(v,dict)};vals=[]
   for r in d.itertuples():
    xg=int(r.x_D)+(5 if int(r.turbine)==2 else 0);iy=int(round((r.y_D*.58+.75)/.075));iz=int(round((r.z_D*.58+.75)/.075));lo=max(a for a in grids if a<=xg);hi=min(a for a in grids if a>=xg);vals.append(grids[lo][iz,iy] if lo==hi else ((hi-xg)*grids[lo][iz,iy]+(xg-lo)*grids[hi][iz,iy])/(hi-lo))
   d['background_u']=vals
  elif case==55:
   w=openpyxl.load_workbook(source/'raw/08.2025_mixes_strength-results.xlsx',read_only=True,data_only=True);s=w['Mix Design&Proportioning'];mix=[]
   for row in range(69,78):
    label=str(s.cell(row,27).value).replace('M-','');b=float(s.cell(row,30).value);sp=float(s.cell(row,33).value);vma=float(s.cell(row,34).value);mix.append(dict(group=label,sp_fraction=sp/b,vma_fraction=vma/b,binder_kg_m3=b,sp_kg_m3=sp,vma_kg_m3=vma,formulation_anchor=f'08.2025_mixes_strength-results.xlsx:Mix Design&Proportioning:row{row}:cols27,30,33,34'))
   early=d[d.age_min==0].groupby(['group','time_s']).agg(initial_force=('target','mean'),initial_anchor=('anchor',lambda x:';'.join(x))).reset_index();lookup={(str(r.group),float(r.time_s)):float(r.initial_force) for r in early.itertuples()};early['initial_shape_change']=[float(r.initial_force)-lookup[(str(r.group),max(1.,float(r.time_s)-50.))] for r in early.itertuples()];d=d[d.age_min==30].merge(early,on=['group','time_s'],validate='many_to_one').merge(pd.DataFrame(mix),on='group',validate='many_to_one').rename(columns={'time_s':'penetration_index'})
  elif case==59:
   with zipfile.ZipFile(source/'raw/weather_files.zip') as z:ww={k[:-12]:pd.read_csv(io.BytesIO(z.read(k))) for k in z.namelist()}
   weather={}
   for k,v in ww.items():v.index=pd.to_datetime(v.iloc[:,0],format='%m/%d/%y %I:%M %p');weather[k]=v.iloc[:,-1]/1000
   ts=pd.to_datetime(d.anchor.str.extract(r':(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)$')[0]);d['year']=ts.dt.year.to_numpy();d['date']=ts.dt.strftime('%Y-%m-%d').to_numpy()
   for lag in [1,2]:d[f'Gpast{lag}']=[weather[r.group].get(t-pd.Timedelta(hours=lag),np.nan) for (_,r),t in zip(d.iterrows(),ts)]
  elif case==86:
   native=pd.read_csv(source/'raw/EFP_long.csv',dtype={'batch_id':str});lookup={}
   for g,s in native.groupby('batch_id',sort=False):
    s=s.sort_values('hh');t=s.hh.to_numpy(float);y=s.hx.to_numpy(float)
    for j,(tt,yy) in enumerate(zip(t,y)):
     prior=np.flatnonzero((t>=tt-12)&(t<=tt));v=y[prior];tv=t[prior];rates=np.diff(v)/np.maximum(np.diff(tv),1);a3=a6=0.
     for r in rates:a3=(1-np.exp(-1/3))*r+np.exp(-1/3)*a3;a6=(1-np.exp(-1/6))*r+np.exp(-1/6)*a6
     def slope(k):
      ix=np.flatnonzero(t==tt-k);return (yy-y[ix[-1]])/k if len(ix) else (yy-v[0])/max(tt-tv[0],1)
     lookup[(str(g),tt)]={'slope1':slope(1),'slope3':slope(3),'slope12':slope(12),'past_acc6':(slope(6)-slope(12))/6,'ewma3':a3,'ewma6':a6,'window6_sd':float(np.std(rates[-6:]))}
   for name in ['slope1','slope3','slope12','past_acc6','ewma3','ewma6','window6_sd']:d[name]=[lookup[(str(g),float(t))][name] for g,t in zip(d.group,d.time_h)]
  elif case==96:
   p=supplemental_folder(96,supplemental_root);m=_port('bike_raw');m.PARENT=p.parent.parent.parent if p.name=='3_C_vehiclized' else p
   # Parser receives one explicit payload directory; no historical-path fallback.
   class Prefix:
    def __truediv__(self,other):return p
   m.PARENT=Prefix();m.HERE=Path('.');d=pd.concat([m.prepare96('development'),m.prepare96('diagnostic')],ignore_index=True);d['partition']=np.where(d.group=='wide-0010-0012-connected','confirmation','development')
  return d
 if family=='round2':
  if case in [57,60,72,83,100]:d=_port('round2_bio').transform(case,d,Path(data_root))
  else:d=d[d.partition=='development'].copy()
  if case==61:
   d=d[d.kind=='mixture'].copy();pars=_meta('61_calibration.json')['calibration'];i=d.membrane_index.to_numpy(int);lr=np.array([x['log_P_ref'] for x in pars])[i];b=np.array([x['activation_over_R_K'] for x in pars])[i];n=np.array([x['pressure_exponent'] for x in pars])[i];per=np.exp(lr+b*(1/673.15-1/d.temperature_K.to_numpy()));d['calibration_j0']=per*np.maximum((d.feed_fraction*d.retentate_bar).to_numpy()**n-d.permeate_bar.to_numpy()**n,0)
  if case==82:
   u=d.groupby(['site','date'],as_index=False).tsmoisture.mean();hist={}
   for s,q in u.groupby('site'):
    q=q.sort_values('date');dates=pd.to_datetime(q.date)
    for _,r in q.iterrows():
     before=q[(dates<pd.Timestamp(r.date))&(dates>=pd.Timestamp(r.date)-pd.Timedelta(days=30))];v=before.tsmoisture.dropna();hist[(s,r.date)]=float(r.tsmoisture-v.iloc[-1]) if len(v) and np.isfinite(r.tsmoisture) else 0.
   d['moisture_change']=[hist[(s,t)] for s,t in zip(d.site,d.date)]
   u=d.groupby(['site','date'],as_index=False).t05.mean();history={}
   for site,q in u.groupby('site'):
    dates=pd.to_datetime(q.date);vals=q.t05.to_numpy()
    for i,day in enumerate(dates):
     good=(dates<day)&(dates>=day-pd.Timedelta(days=30));history[(site,str(q.date.iloc[i]))]=float(vals[good].mean()) if np.any(good) else 10.
   d['past_temperature']=[history[(s,str(t))] for s,t in zip(d.site,d.date)]
  if case==92:
   d['sample_id']=d.member+':'+d.port+':'+d.channel.astype(str)
   # Initial calibration map repeated across dates is reduced to unique cells first.
   c=d[['x','y','port','channel','r0']].drop_duplicates();c['power']=10**(c.r0/10);g=c.groupby(['port','channel']).power.mean();local=c.groupby(['x','y','port']).power.mean();d['global_power_reference']=[10*np.log10(g.loc[(p,ch)]) for p,ch in zip(d.port,d.channel)];d['local_channel_power_dB']=[10*np.log10(local.loc[(x,y,p)]) for x,y,p in zip(d.x,d.y,d.port)]
  schema=_meta('task_schemas.json')[task['task_id']]
  if 'fold_by_sample_id'in schema:d['fold']=[schema['fold_by_sample_id'].get(str(s),'not_scored') for s in d.sample_id]
  if case==60:
   scales={str(f['label']):f['scale'] for f in _meta('60_normalization.json')['folds']};d['condition_scale']=[scales[str(f)][str(c)] if str(f) in scales else np.nan for f,c in zip(d.fold,d.condition)]
  return d
 raise ValueError('Unknown preparation family: '+family)
