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

def prepare(data_root):
    root=verified(data_root);path=root/'raw/Figure 2e-Vg sweep of 36 FET.csv';f=pd.read_csv(path);v=f.iloc[:,0].to_numpy(float);rows=[]
    for j in range(1,len(f.columns)):
        y=f.iloc[:,j].to_numpy(float)*1e6;g=f'device-{j:02d}';cal={str(a):float(y[np.where(np.isclose(v,a,atol=1e-10))[0][0]])for a in [-20.,0.,20.]}
        for k in range(len(v)):
            if any(np.isclose(v[k],a,atol=1e-10)for a in [-20,0,20]):continue
            if not np.isfinite(y[k]):raise ValueError('Unexpected missing target')
            rows.append(dict(sample_id=f'{g}:row-{k+2}',group=g,gate_V=float(v[k]),cal_minus20_uA=cal['-20.0'],cal_zero_uA=cal['0.0'],cal_plus20_uA=cal['20.0'],target=float(y[k]),source_anchor=f'raw/{path.name}::row={k+2};column={f.columns[j]}',calibration_anchor=f'raw/{path.name}::{f.columns[j]};Vg=-20,0,20 V',eligible=True,eligibility_reason='finite measured current; excludes three disclosed calibration points',linked_device=g))
    return finish(rows)
