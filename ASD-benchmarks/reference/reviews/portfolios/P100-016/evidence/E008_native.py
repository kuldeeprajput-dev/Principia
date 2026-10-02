from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def prepare(data_root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text());root=Path(data_root)/m['folder']
 for a in m['assets']:
  f=Path(data_root)/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native SHA256 mismatch: '+a['path'])
 specs={'cpi':('CU/cu.data.1.AllItems','CUSR0000SA0'),'housing':('CU/cu.data.12.USHousing','CUSR0000SAH'),'medical':('CU/cu.data.15.USMedical','CUSR0000SAM'),'jobs':('CE/ce.data.00a.TotalNonfarm.Employment','CES0000000001'),'mfg':('CE/ce.data.30a.Manufacturing.Employment','CES3000000001'),'info':('CE/ce.data.50a.Information.Employment','CES5000000001')};series={};anchors={}
 for k,(file,sid) in specs.items():
  d=pd.read_csv(root/'raw'/file,sep='\t');d.columns=d.columns.str.strip();d['native_row']=np.arange(len(d))+2;d['series_id']=d.series_id.str.strip();d['period']=d.period.str.strip();d=d[(d.series_id==sid)&d.period.str.match(r'^M(0[1-9]|1[0-2])$')].copy();d['time']=pd.to_datetime(d.year.astype(str)+'-'+d.period.str[1:]+'-01');d['value']=pd.to_numeric(d.value,errors='coerce');d=d.set_index('time').sort_index()
  if d.index.duplicated().any():raise ValueError('Duplicate monthly series date')
  series[k]=d.value;anchors[k]=d.native_row.to_dict()
 z=pd.DataFrame(series).reindex(pd.date_range('1988-01-01','2026-12-01',freq='MS'));growth=100*np.log(z/z.shift(1));rows=[]
 for t,v in growth.iterrows():
  if t<pd.Timestamp('1990-01-01') or not np.isfinite(v.cpi):continue
  j=growth.index.get_loc(t);prior=growth.iloc[:j]
  if len(prior)<12:continue
  features={'inflation1':prior.cpi.iloc[-1],'inflation3':prior.cpi.iloc[-3:].mean() if prior.cpi.iloc[-3:].notna().all() else np.nan,'inflation12':prior.cpi.iloc[-12:].mean() if prior.cpi.iloc[-12:].notna().all() else np.nan,**{k+'1':prior[k].iloc[-1] for k in ['housing','medical','jobs','mfg','info']}}
  if not np.isfinite(list(features.values())).all():continue
  rows.append(dict(sample_id='US-CPI:'+t.strftime('%Y-%m'),group=t.to_period('Q').__str__(),target=float(v.cpi),partition='confirmation' if t.year>=2023 else 'development',fold_key=t.year,prediction_time=(t-pd.DateOffset(months=1)).strftime('%Y-%m'),target_time=t.strftime('%Y-%m'),source_anchor='CU/cu.data.1.AllItems:CUSR0000SA0:row='+str(anchors['cpi'][t])+';target=100*log(CPI_t/CPI_previous)',input_anchor='All six declared seasonally-adjusted series; exact calendar-month lags through '+(t-pd.DateOffset(months=1)).strftime('%Y-%m'),**features))
 d=pd.DataFrame(rows)
 if d.empty or d.sample_id.duplicated().any():raise ValueError('No eligible rows or duplicate identities')
 return d
