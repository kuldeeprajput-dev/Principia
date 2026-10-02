from pathlib import Path
import hashlib, json, io, re, zipfile
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent

def verified(data_root):
    manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
    root=Path(data_root)
    for a in manifest['assets']:
        p=root/a['path']
        if not p.is_file() or p.stat().st_size != a['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:
            raise ValueError('Missing or checksum-mismatched source: '+a['path'])
    return root/manifest['source_scenario']

def finish(rows):
    f=pd.DataFrame(rows); splits=json.loads((HERE/'SPLITS.json').read_text())['groups']
    f['partition']=f.group.map(splits)
    if f.sample_id.duplicated().any() or f.partition.isna().any():raise ValueError('Invalid source identities')
    return f.sort_values('sample_id',kind='stable').reset_index(drop=True)

def read_trace(path):
    rows=[]; start=None
    for n,line in enumerate(path.read_text().splitlines(),1):
        if re.fullmatch(r'\d{4}-\d\d-\d\dT.*',line.strip()):
            start=pd.Timestamp(line.strip()).value/1e9;continue
        if line.startswith('#') or not line.strip():continue
        values=line.split()
        if len(values)!=6 or start is None:raise ValueError('Malformed instrument record')
        q=dict(zip(['step','time','current','voltage','clock','temp'],map(float,values)));q['absolute_s']=start+q['time'];q['native_row']=n;rows.append(q)
    a=pd.DataFrame(rows)
    if not a.absolute_s.is_monotonic_increasing:raise ValueError('Nonmonotone source clock')
    return a

def prepare(data_root):
    root=verified(data_root);base=root/'raw/Archive_Stretchable_LEC/Backlog_Statistic_Stretchable_LEC';rows=[]
    for ip in sorted(base.rglob('*_it*.txt')):
        pp=ip.with_name(ip.name.replace('_it','_pt'));m=re.search(r'(\d+)wt%_no(\d+)_(\d+)[Vv]_it(_2)?',ip.name)
        if not pp.exists()or not m:raise ValueError('Unmatched device files')
        it=read_trace(ip);pt=read_trace(pp);g=f'{m[1]}wt%_no{m[2]}';duration=it.time.to_numpy(float);times=it.absolute_s.to_numpy(float)
        charge=np.r_[0.,np.cumsum(.5*(it.current.to_numpy()[1:]+it.current.to_numpy()[:-1])*np.diff(times))]*1e6
        t=pt.absolute_s.to_numpy(float)-times[0];cal=(t>=0)&(t<=20)
        if cal.sum()<3:continue # Frozen minimum viable early calibration.
        early=float(np.median(pt.current.to_numpy()[cal])*1e9);early_i=float(np.median(it.current.to_numpy()[duration<=20])*1e6)
        sel=(t>20)&(t<=duration[-1]);q=np.searchsorted(times,pt.absolute_s.to_numpy(),side='right')-1
        for k in np.flatnonzero(sel):
            j=q[k]
            if j<0 or pt.absolute_s.iloc[k]-times[j]>2.:continue # causal last-observation join; reject stale readings
            target=float(pt.current.iloc[k]*1e9)
            if not np.isfinite(target):continue
            rows.append(dict(sample_id=f'{ip.stem}:pt-row-{int(pt.native_row.iloc[k])}',group=g,time_s=float(t[k]),current_uA=float(it.current.iloc[j]*1e6),voltage_V=float(it.voltage.iloc[j]),polymer_fraction=float(m[1])/100,charge_uC=float(charge[j]),cal_photo_nA=early,cal_current_uA=early_i,target=target,source_anchor=f'{pp.relative_to(root)}::row={int(pt.native_row.iloc[k])};{ip.relative_to(root)}::row={int(it.native_row.iloc[j])}',calibration_anchor=f'{pp.relative_to(root)}::0<=aligned_time_s<=20;median;{ip.relative_to(root)}::0<=time_s<=20;median',alignment_lag_s=float(pt.absolute_s.iloc[k]-times[j]),eligible=True,eligibility_reason='after early calibration; current available within preceding2s; finite target',linked_device=g,run_id=ip.stem))
    return finish(rows)
