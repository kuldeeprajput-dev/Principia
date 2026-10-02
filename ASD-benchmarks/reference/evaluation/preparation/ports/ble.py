"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io
from datetime import datetime
FINAL = {'11012024', '15022024', '23022024'}

def extract(partition):
    allowed = SPLIT['groups']
    rows = []
    counts = {}
    with zipfile.ZipFile(ARCHIVE) as z:
        for n in sorted(z.namelist()):
            if not n.endswith('.txt'):
                continue
            meta = allowed[n.split('/')[0]]
            if meta['role'] not in ['calibration', partition]:
                continue
            pos = re.search('_x_(-?\\d+)_y_(-?\\d+)', n)
            if not pos:
                raise ValueError(f'Unmapped coordinate: {n}')
            d = pd.read_csv(io.BytesIO(z.read(n)), sep=';', header=None, names=['timestamp', 'port', 'channel', 'rssi'])
            if d.shape[1] != 4 or d.isna().any().any():
                raise ValueError(f'Malformed rows {n}')
            if (d.rssi == 127).any() or (~d.rssi.between(-127, 20)).any():
                raise ValueError(f'Unavailable/unexpected RSSI {n}')
            if not set(d.port).issubset({f'P{i}' for i in range(1, 9)}) or not set(d.channel).issubset({37, 38, 39}):
                raise ValueError('Unknown beacon/channel')
            expected = 100 if meta['role'] == 'calibration' else 10
            exception_count = 2308 if meta['role'] == 'calibration' and (int(pos[1]), int(pos[2])) == (-5, 3) else 2310 if meta['role'] == 'calibration' and (int(pos[1]), int(pos[2])) == (2, -5) else expected * 24
            if len(d) != exception_count:
                raise ValueError(f'Unexpected burst count {n}')
            dates = pd.to_datetime(d.timestamp, unit='ms', utc=True)
            named = datetime.strptime(meta['date'], '%d%m%Y').date()
            if set(dates.dt.date) != {named}:
                raise ValueError(f'Clock unit/date inconsistency {n}')
            for (port, ch), v in d.groupby(['port', 'channel'], sort=True):
                cell_expected = 8 if meta['role'] == 'calibration' and (int(pos[1]), int(pos[2]), port, int(ch)) == (-5, 3, 'P3', 39) else 10 if meta['role'] == 'calibration' and (int(pos[1]), int(pos[2]), port, int(ch)) == (2, -5, 'P3', 39) else expected
                if len(v) != cell_expected:
                    raise ValueError('Missing or duplicate channel cell')
                rows.append({'member': n, 'source_lines': ','.join((str(i + 1) for i in v.index)), 'group': meta['date'], 'role': meta['role'], 'date': named.isoformat(), 'day': (named - datetime(2023, 11, 21).date()).days, 'x': int(pos[1]), 'y': int(pos[2]), 'port': port, 'channel': int(ch), 'furniture': int(meta['furniture']), 'n_packets': len(v), 'target': float(v.rssi.mean()), 'packet_std': float(v.rssi.std()), 'timestamp_min_ms': int(v.timestamp.min()), 'timestamp_max_ms': int(v.timestamp.max())})
            counts[n.split('/')[0]] = counts.get(n.split('/')[0], 0) + len(d)
    data = pd.DataFrame(rows)
    cal = data[data.role == 'calibration'].copy()
    cal['r0'] = cal.target
    cal['channel_mean'] = cal.groupby(['x', 'y', 'port']).r0.transform('mean')
    cal['spatial_mean'] = cal.groupby(['port', 'channel']).r0.transform('mean')
    cal['position_contrast'] = cal.channel_mean - cal.groupby('port').r0.transform('mean')
    cal['channel_bias'] = cal.spatial_mean - cal.groupby('port').r0.transform('mean')
    cal['channel_contrast'] = cal.r0 - cal.channel_mean
    cal['spatial_contrast'] = cal.r0 - cal.spatial_mean
    cal['linear_channel_mean'] = cal.groupby(['x', 'y', 'port']).r0.transform(lambda x: 10 * np.log10(np.mean(10 ** (x / 10))))
    test = data[data.role == partition].merge(cal[['x', 'y', 'port', 'channel', 'r0', 'channel_mean', 'channel_contrast', 'spatial_contrast', 'linear_channel_mean', 'position_contrast', 'channel_bias']], on=['x', 'y', 'port', 'channel'], validate='many_to_one')
    if len(test) != len(data[data.role == partition]):
        raise ValueError('Lost uncalibrated test cells')
    test['lwa'] = test.port.isin(['P1', 'P2', 'P3', 'P4']).astype(int)
    return (test, cal, counts)
