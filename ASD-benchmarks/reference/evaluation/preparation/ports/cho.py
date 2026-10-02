"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
TARGET = 'VCD Mean (cells/mL)'

def colidx(ref):
    n = 0
    for c in re.match('[A-Z]+', ref).group():
        n = n * 26 + ord(c) - 64
    return n - 1

def xlsx_tables(payload, wanted):
    """Read cached native values without Excel rewriting or formula evaluation."""
    result = {}
    with zipfile.ZipFile(io.BytesIO(payload)) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(n.itertext()) for n in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        rel = {n.attrib['Id']: n.attrib['Target'] for n in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets = ET.fromstring(z.read('xl/workbook.xml')).find('s:sheets', NS)
        for node in sheets:
            name = node.attrib['name']
            if name not in wanted:
                continue
            target = rel[node.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
            path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            rows = []
            with z.open(path) as stream:
                for event, row in ET.iterparse(stream, events=('end',)):
                    if row.tag != '{' + NS['s'] + '}row':
                        continue
                    vals = {}
                    for c in row:
                        if not c.tag.endswith('}c'):
                            continue
                        typ = c.attrib.get('t')
                        v = c.find('s:v', NS)
                        if typ == 'inlineStr':
                            value = ''.join(c.find('s:is', NS).itertext())
                        elif v is None:
                            value = None
                        elif typ == 's':
                            value = strings[int(v.text)]
                        elif typ == 'e':
                            value = None
                        else:
                            try:
                                value = float(v.text)
                            except (ValueError, TypeError):
                                value = v.text
                        vals[colidx(c.attrib['r'])] = value
                    if vals:
                        arr = [None] * (max(vals) + 1)
                        for k, v in vals.items():
                            arr[k] = v
                        rows.append(arr)
                    row.clear()
            width = max(map(len, rows))
            rows = [r + [None] * (width - len(r)) for r in rows]
            result[name] = pd.DataFrame(rows[1:], columns=rows[0])
    return result

def summarize(stream, t, cols):
    ts = pd.to_numeric(stream['Time (h)'], errors='coerce').to_numpy(float)
    past = np.isfinite(ts) & (ts <= t + 1e-10) & (ts >= 0)
    status = stream.get('Status', pd.Series(['Ok'] * len(stream))).astype(str).str.strip().str.lower()
    valid = past & status.eq('ok').to_numpy()
    out = {}
    latest = {}
    for c in cols:
        if c not in stream:
            out[c] = np.nan
            latest[c] = np.nan
            continue
        a = pd.to_numeric(stream[c], errors='coerce').to_numpy(float)
        keep = valid & np.isfinite(a)
        if c in ['DeltaEps (pF/cm)', 'fc (kHz)', 'Alpha']:
            q = pd.to_numeric(stream['Fitting Quality (Cole fit R2)'], errors='coerce').to_numpy(float)
            keep &= q >= 0.9
        j = np.flatnonzero(keep)
        if len(j) == 0 or t - ts[j[-1]] > 2:
            out[c] = np.nan
            latest[c] = np.nan
            continue
        win = j[ts[j] >= t - 0.5]
        if len(win) == 0:
            win = j[-1:]
        out[c] = float(np.median(a[win]))
        latest[c] = float(np.max(ts[win]))
    return (out, {'past_rows': int(past.sum()), 'valid_status_rows': int(valid.sum()), 'invalid_status_rows': int((past & ~status.eq('ok').to_numpy()).sum()), 'latest_source_timestamp_max': max([v for v in latest.values() if np.isfinite(v)], default=None), 'used_timestamp_per_channel': latest})
STREAMS = {'inline_Turbidity': {'Transmission (arb. Unit)': 'transmission', 'Reflection (arb. Unit)': 'reflection'}, 'inline_Permittivity': {'Permittivity (pF/cm)': 'perm', 'Conductivity (mS/cm)': 'conductivity', 'DeltaEps (pF/cm)': 'deltaeps', 'fc (kHz)': 'fc', 'Alpha': 'cole_alpha', 'C (300kHz)': 'c300', 'C (1118kHz)': 'c1118', 'C (9995kHz)': 'c9995', 'Fitting Quality (Cole fit R2)': 'cole_r2'}, 'inline_CO2': {'Dissolved CO2 (%-sat)': 'co2'}, 'inline_ProcessParameters': {'pH': 'ph', 'Dissolved O2 (% air sat)': 'do', 'Temperature (°C)': 'temperature', 'Agitation rate (rpm)': 'agitation', 'Aeration rate total (sL/h)': 'aeration', 'O2 fraction inlet (%)': 'o2_inlet', 'Liquid volume (L)': 'volume'}}

def prepare(final=False):

    selected = [e for e in SPLIT['entries'] if (e['split'] == 'locked_confirmation') == final]
    rows = []
    audit = []
    flags = []
    started = time.time()
    with zipfile.ZipFile(SOURCE / 'raw/Dataset.zip') as z:
        for e in selected:
            wanted = [f'{r}_{s}' for r in ['R01', 'R02'] for s in list(STREAMS) + ['offline_CellAnalysis']]
            tables = xlsx_tables(z.read(e['workbook']), wanted)
            for r in ['R01', 'R02']:
                for kind in STREAMS:
                    d = tables[f'{r}_{kind}']
                    ts = pd.to_numeric(d['Time (h)'], errors='coerce')
                    reversals = int((ts.diff() < 0).sum())
                    if reversals:
                        d = d.assign(_native_row=np.arange(len(d))).sort_values('Time (h)', kind='stable').reset_index(drop=True)
                        tables[f'{r}_{kind}'] = d
                    flags.append({'experiment': e['experiment'], 'reactor': r, 'stream': kind, 'rows': len(d), 'time_min': float(ts.min()), 'time_max': float(ts.max()), 'native_time_reversals': reversals, 'statuses': d['Status'].fillna('<blank>').value_counts().to_dict() if 'Status' in d else {'no_status_column': len(d)}})
                off = tables[f'{r}_offline_CellAnalysis']
                for idx, sample in off.iterrows():
                    t = float(sample['Time (h)'])
                    y = pd.to_numeric(sample[TARGET], errors='coerce')
                    if not np.isfinite(t):
                        continue
                    rid = f'{e['experiment']}_{r}_{idx:03d}'
                    if not np.isfinite(y) or y < 0:
                        audit.append({'sample_id': rid, 'excluded_target': 'nonfinite_or_negative'})
                        continue
                    row = {'sample_id': rid, 'experiment': e['experiment'], 'reactor': r, 'mode': e['mode'], 'time_h': t, 'vcd_million_ml': float(y) / 1000000.0, 'vcd_sem_million_ml': float(sample['VCD SEM (cells/mL)']) / 1000000.0}
                    ra = {'sample_id': rid, 'target_time_h': t, 'streams': {}, 'history': {}}
                    for kind, mapping in STREAMS.items():
                        v, qa = summarize(tables[f'{r}_{kind}'], t, list(mapping))
                        row.update({mapping[k]: v[k] for k in mapping})
                        ra['streams'][kind] = qa
                        if qa['latest_source_timestamp_max'] is not None:
                            assert qa['latest_source_timestamp_max'] <= t + 1e-10
                    for kind, cols in [('inline_Permittivity', ['Permittivity (pF/cm)']), ('inline_Turbidity', ['Transmission (arb. Unit)'])]:
                        v, qa = summarize(tables[f'{r}_{kind}'], max(0, t - 24), cols)
                        ra['history'][kind + '_lag24'] = {'evaluation_time_h': max(0, t - 24), **qa}
                        for k in cols:
                            row[STREAMS[kind][k] + '_lag24'] = v[k]
                    ps = tables[f'{r}_inline_Permittivity']
                    ts = pd.to_numeric(ps['Time (h)'], errors='coerce').to_numpy(float)
                    pv = pd.to_numeric(ps['Permittivity (pF/cm)'], errors='coerce').to_numpy(float)
                    good = (ts >= 0) & (ts <= t) & np.isfinite(pv) & ps['Status'].astype(str).str.lower().eq('ok').to_numpy()
                    row['perm_peak_past'] = float(np.max(pv[good])) if good.any() else np.nan
                    peak_indices = np.flatnonzero(good)
                    ra['history']['perm_peak_past'] = {'latest_permitted_time_h': t, 'peak_source_time_h': float(ts[peak_indices[np.argmax(pv[good])]]) if len(peak_indices) else None}
                    row['fed_batch'] = float(e['mode'] == 'fed-batch')
                    rows.append(row)
                    audit.append(ra)
            print(json.dumps({'prepared': e['experiment'], 'rows_cumulative': len(rows), 'elapsed_s': round(time.time() - started, 1)}), flush=True)
    d = pd.DataFrame(rows)
    d['od'] = np.where(d.transmission > 0, -np.log(d.transmission.where(d.transmission > 0)), np.nan)
    lagod = np.where(d.transmission_lag24 > 0, -np.log(d.transmission_lag24.where(d.transmission_lag24 > 0)), np.nan)
    dt = np.minimum(24, d.time_h).replace(0, np.nan)
    d['dperm24'] = (d.perm - d.perm_lag24) / dt
    d['dod24'] = (d.od - lagod) / dt
    d.loc[d.time_h == 0, ['dperm24', 'dod24']] = 0.0
    d['spectral_span'] = d.c300 - d.c9995
    d['spectral_midspan'] = d.c1118 - d.c9995
    d['fc_mhz'] = d.fc / 1000.0
    d['permittivity_decline'] = np.maximum(0, d.perm_peak_past - d.perm)
    d['perm_decline_fraction'] = d.permittivity_decline / np.maximum(d.perm_peak_past, 0.1)
    d['od_sq'] = d.od ** 2
    d['perm_sq'] = d.perm ** 2
    d['deltaeps_fc4'] = d.deltaeps * d.fc_mhz ** 4
    d['perm_fc'] = d.perm * d.fc_mhz
    d['perm_x_decline'] = d.perm * d.perm_decline_fraction
    d['perm_x_conductivity'] = d.perm * (d.conductivity - 12.0)
    d['perm_x_growth'] = d.perm * d.dperm24
    d['od_x_decline'] = d.od * d.perm_decline_fraction
    label = 'confirmation' if final else 'development'
    return d, audit, flags
