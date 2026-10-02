from pathlib import Path
import pandas as pd,numpy as np,json,hashlib,zipfile,re,openpyxl,datetime,shutil
def dump(*args): pass
def transform(case,d,DATA):
    d=d[d.partition=="development"].copy()
    out=Path(".")
    if case == 57:
        z = zipfile.ZipFile(next(DATA.glob('57_*/raw/*.zip')))
        starts = {}
        for n in z.namelist():
            if not n.endswith('.csv'):
                continue
            text = z.read(n).decode('utf-16')
            uid = re.search('^Test ID:\\t([^\\t]+)', text, re.M).group(1)
            ts = [float(v) for v in re.findall('^Result Start Time:\\t([\\d.]+) s', text, re.M)]
            assert len(ts) == 10 and len(set(ts)) == 10
            starts[uid] = ts
        rows = []
        for g, v in d.groupby('group', sort=False):
            blocks = sorted(v.source_block.unique(), key=lambda b: starts[g][int(b) - 1])
            for j, b in enumerate(blocks[1:], 1):
                cur = v[v.source_block == b]
                prev = v[v.source_block == blocks[j - 1]].set_index('shear_s')
                first = v[v.source_block == blocks[0]].set_index('shear_s')
                for point, (_, r) in enumerate(cur.iterrows()):
                    p = prev.iloc[point]
                    f = first.iloc[point]
                    a = r.to_dict()
                    a.update(previous_shear_s=float(p.name), first_shear_s=float(f.name), T_previous=p.T_C, eta_previous=p.target, eta_first=f.target, source_previous_line=int(p.source_line), source_first_line=int(f.source_line), block_start_s=starts[g][int(b) - 1], previous_block_start_s=starts[g][int(blocks[j - 1]) - 1])
                    rows.append(a)
        d = pd.DataFrame(rows)
    elif case == 72:
        dev = {str(g): int(v.fold.iloc[0]) for g, v in d.groupby('group')}
        p = next(DATA.glob('72_*/raw/*.xlsx'))
        w = openpyxl.load_workbook(p, read_only=True, data_only=True)
        rr = list(w['HPLC'].values)
        samples = {}
        omissions = []
        for line, r in enumerate(rr, 1):
            name = r[1] if len(r) > 1 else None
            if not isinstance(name, str):
                continue
            m = re.fullmatch('\\s*R([123])\\s+(.+?)\\s*_\\s*(\\d+)h\\s*', name)
            if not m:
                continue
            rep, s, t = (int(m[1]), m[2].strip(), int(m[3]))
            s = re.sub('\\s+', '', s.replace('ICV', ''))
            co = int('+' in s)
            s = s.split('+')[0]
            s = {'EC1118': 'Ec1118', 'Cr96,2': 'Chr96,2'}.get(s, s)
            if s not in dev:
                continue
            if not isinstance(r[3], (int, float)) or not isinstance(r[4], (int, float)):
                omissions.append({'row': line, 'sample': name, 'reason': 'native missing sugar amount'})
                continue
            k = (s, co, rep, t)
            if k in samples:
                raise ValueError('ambiguous repeated injection ' + str(k))
            samples[k] = (float(r[3]), float(r[4]), line, name)
        rows = []
        for (s, co, rep, t), (G, F, li, n) in samples.items():
            if t < 96 or (s, co, rep, 22) not in samples or (s, co, rep, 72) not in samples:
                continue
            g22, f22, l22, _ = samples[s, co, rep, 22]
            g72, f72, l72, _ = samples[s, co, rep, 72]
            rows.append(dict(sample_id=f'HPLC:{s}:{co}:R{rep}:{t}:row{li}', group=s, partition='development', fold=dev[s], S22=g22 + f22, S72=g72 + f72, G22=g22, G72=g72, F22=f22, F72=f72, time_h=t, coculture=co, target=G + F, replicate=rep, source_file=p.name, source_sheet='HPLC', source_row=li, source_columns='D:E', prefix22_row=l22, prefix72_row=l72, source_sample_name=n))
        d = pd.DataFrame(rows)
        dump(out / 'HPLC_AUDIT.json', {'native_header_units': 'glucose/fructose g/L', 'native_rows': len(samples), 'eligible_future_rows': len(d), 'whole_strain_groups': sorted(d.group.unique().tolist()), 'missing_measurements': omissions, 'excluded': 'CR85 monoculture, original reservedT73/D245 strains, nonmatching sample names, HPLCaa independent campaign; no outcome-based exclusions', 'source_paper': 'https://doi.org/10.1016/j.fm.2023.104276'})
    elif case == 83:
        tables = {p.name: pd.read_csv(p) for p in next(DATA.glob('83_*')).glob('raw/*.csv') if 'Pluvio' not in p.name}
        lags = []
        for _, r in d.iterrows():
            v = tables[r.source_file]
            s = int(str(r.stream).split('sensor')[-1])
            u = v[v.id_sensor == s].copy()
            tt = pd.to_datetime(u.time, format='mixed')
            cut = pd.Timestamp(r.lag_time)
            i = tt[tt <= cut].idxmax()
            assert pd.Timestamp(tt.loc[i]) == cut
            lags.append(float(u.loc[i, 'ext_temperature']))
        d['T_external_lag'] = lags
    elif case == 100:
        z = zipfile.ZipFile(next(DATA.glob('100_*/raw/*.zip')))
        tt = {n: pd.read_csv(z.open(n)) for n in d.source_ping_member.unique()}
        feats = []
        for _, r in d.iterrows():
            v = tt[r.source_ping_member]
            k = int(r.source_ping_row) - 2
            p = v['Ping Time (ms)'].iloc[k - 5:k].to_numpy(float)
            assert len(p) == 5 and np.isclose(p[-1], r.last_rtt)
            feats.append([p[-2], p[-3], np.median(p), np.std(p)])
        d[['last2_rtt', 'last3_rtt', 'median5_rtt', 'std5_rtt']] = feats
    return d
