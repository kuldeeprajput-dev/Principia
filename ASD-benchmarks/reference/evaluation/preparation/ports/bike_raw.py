"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

def prepare96(part):
    paths = sorted((PARENT / 'sources/data/3_C_vehiclized').glob('*.txt'))
    rows = []
    audit = []
    for p in paths:
        n = p.name
        video = n.split('.MP4')[0]
        serial = int(video.split('_')[-2])
        group = 'narrow-early-0003-0005' if serial <= 5 else 'narrow-late-0007-0009' if serial <= 9 else 'wide-0010-0012-connected'
        if (part == 'development') == (serial >= 10):
            continue
        raw = pd.read_csv(p, sep='\t', header=None, names=['frame', 'kind', 'x', 'y', 'width', 'length', 'angle', 'confidence', 'track', 'vehicle'])
        raw['source_row'] = np.arange(len(raw)) + 1
        raw = raw[raw.vehicle.str.startswith('BICYCLE_', na=False)].copy()
        raw = raw.drop_duplicates(['vehicle', 'frame'], keep='last')
        raw = raw.sort_values(['vehicle', 'frame'])
        states = {}
        for vehicle, s in raw.groupby('vehicle', sort=True):
            fr = s.frame.to_numpy(int)
            xx = s.x.to_numpy(float)
            yy = s.y.to_numpy(float)
            theta = np.unwrap(np.arctan2(yy, xx))
            rad = np.sqrt(xx ** 2 + yy ** 2)
            sr = s.source_row.to_numpy(int)
            for f in np.arange(int(fr.min()) + 50, int(fr.max()) + 1, 25):
                q = np.searchsorted(fr, [f - 50, f - 25, f], side='right') - 1
                if np.any(q < 0) or np.any(np.array([f - 50, f - 25, f]) - fr[q] > 5):
                    continue
                th = theta[q]
                rr = rad[q]
                signed = (th[2] - th[1]) * (rr[2] + rr[1]) / 2 / ((fr[q[2]] - fr[q[1]]) / 25)
                prior = (th[1] - th[0]) * (rr[1] + rr[0]) / 2 / ((fr[q[1]] - fr[q[0]]) / 25)
                direction = 1 if signed >= 0 else -1
                fq = np.searchsorted(fr, f + 25, side='right') - 1
                future = direction * (theta[fq] - th[2]) * (rad[fq] + rr[2]) / 2 / ((fr[fq] - fr[q[2]]) / 25) if fq >= 0 and f + 25 - fr[fq] <= 5 else np.nan
                if not np.isfinite([signed, prior]).all():
                    continue
                states[int(f), vehicle] = {'speed': abs(signed), 'past_acc': abs(signed) - abs(prior), 'target': future, 'theta': th[2] % (2 * np.pi), 'radius': rr[2], 'direction': direction, 'source_row': int(sr[q[2]]), 'future_row': int(sr[fq]) if fq >= 0 else -1}
        for f in sorted(set((k[0] for k in states))):
            vehicles = sorted((v for ff, v in states if ff == f))
            sub = [states[f, v] for v in vehicles]
            for j, (v, r) in enumerate(zip(vehicles, sub)):
                if not np.isfinite(r['target']):
                    continue
                others = [(u, a) for u, a in zip(vehicles, sub) if u != v]
                if not others:
                    continue
                good = [(u, a) for u, a in others if abs(a['radius'] - r['radius']) <= 1 and a['direction'] == r['direction']]
                ahead = [(float(r['direction'] * (a['theta'] - r['theta']) % (2 * np.pi)) * r['radius'], u, a) for u, a in good]
                rev = [(float(-r['direction'] * (a['theta'] - r['theta']) % (2 * np.pi)) * r['radius'], u, a) for u, a in good]
                lead = min(ahead, key=lambda x: x[0]) if ahead else None
                rear = min(rev, key=lambda x: x[0]) if rev else None
                shuffled = others[int(hashlib.sha256(f'{video}:{f}:{v}'.encode()).hexdigest(), 16) % len(others)][1]
                rows.append({'sample_id': f'P100-096-clock-v2:{n}:{f}:{v}', 'group': group, 'video': video, 'sequence': n, 'frame': f, 'vehicle': v, 'speed': r['speed'], 'past_acc': r['past_acc'], 'relative_speed': lead[2]['speed'] - r['speed'] if lead else 0.0, 'gap': lead[0] if lead else 100.0, 'lateral_gap': abs(lead[2]['radius'] - r['radius']) if lead else 1.0, 'reverse_relative_speed': rear[2]['speed'] - r['speed'] if rear else 0.0, 'shuffle_relative_speed': shuffled['speed'] - r['speed'], 'radius': r['radius'], 'count': len(sub), 'direction': r['direction'], 'has_lane_leader': lead is not None, 'target': r['target'], 'anchor': f'{n}:row{r['source_row']}:future_row{r['future_row']}'})
        audit.append({'file': n, 'observations': len(raw), 'eligible_interval_predictions': len([x for x in rows if x['sequence'] == n]), 'directions': {str(d): sum((s['direction'] == d for s in states.values())) for d in [-1, 1]}})
    unused = ( {'files': audit, 'scope': 'backward rawannotation interval speed; targets are forward rawannotation arc speeds, not authorsRTSspeed', 'no_future_interpolation': True})
    return pd.DataFrame(rows)
