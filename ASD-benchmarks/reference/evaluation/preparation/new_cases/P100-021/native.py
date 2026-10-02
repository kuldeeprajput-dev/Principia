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
    root=verified(data_root); z=zipfile.ZipFile(root/'raw/Data.zip'); rows=[]
    for name in sorted(z.namelist()):
        if not name.endswith('_gen.csv'):continue
        stem=Path(name).name;match=re.fullmatch(r'(\d+(?:_\d+)?)um_0_gen.csv',stem)
        if not match:continue # Ambiguous 1_0_2um excluded by frozen filename rule.
        w=float(match[1].replace('_','.')); g='/'.join(name.split('/')[1:3]);sig=name.replace('_gen.csv','_sig.csv')
        x=pd.read_csv(io.BytesIO(z.read(name)));y=pd.read_csv(io.BytesIO(z.read(sig)))
        if len(x)!=len(y)or not np.array_equal(x.time.to_numpy(),y.time.to_numpy()):raise ValueError('Unaligned waveform pair')
        I=x.voltage.to_numpy()/100.; V=y.voltage.to_numpy(); slopes=[]; intercepts=[]; counts=[]
        for mask in [I<=np.quantile(I,.2),I>=np.quantile(I,.8)]:
            a=np.column_stack([np.ones(mask.sum()),I[mask]])
            intercept,slope=np.linalg.lstsq(a,V[mask],rcond=None)[0]; slopes.append(float(slope));intercepts.append(float(intercept));counts.append(int(mask.sum()))
        s=.5*sum(slopes)
        if not np.isfinite(s) or s<=0:raise ValueError('Nonpositive native resistance estimate')
        region=0 if 'Inner' in g else 1 if 'Outer' in g else 2
        rows.append(dict(sample_id=name[:-8],group=g,width_um=w,wafer_b=float(region==2),outer=float(region==1),target=s,resistance_low=slopes[0],resistance_high=slopes[1],slope_asymmetry=abs(slopes[0]-slopes[1])/s,source_anchor='raw/Data.zip::'+name+' + '+sig+'; all rows; tails<=q20/>=q80',eligible=True,eligibility_reason='unambiguous design width; aligned complete waveform; both current tails',native_rows=len(x),tail_rows=sum(counts),linked_device=name[:-8]))
    return finish(rows)
