"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

LONGEST = {'D_a': 1.96, 'D_b': 3.0, 'D_c': 3.03, 'R_a': 2.39, 'R_b': 4.05, 'S': 1.5}

def read_member(archive, name, allowed):
    m = re.search('set([123])_([123])', name)
    if not m or '.'.join(m.groups()) not in allowed:
        raise PermissionError('Partition member forbidden: ' + name)
    return pd.read_csv(io.BytesIO(archive.read(name)), encoding='utf-8-sig').dropna(axis=1, how='all')

def passage(z, t, h):
    ix = np.flatnonzero((z[:-1] <= h) & (z[1:] >= h) & (z[1:] > z[:-1]))
    if not len(ix):
        return np.nan
    i = ix[0]
    return t[i] + (h - z[i]) / (z[i + 1] - z[i]) * (t[i + 1] - t[i])

def slope(frame, lo, hi, fallback=None):
    d = frame[(frame.z >= lo) & (frame.z <= hi)]
    if len(d) < 2 or d.t.max() == d.t.min():
        return (fallback, len(d))
    t = d.t.to_numpy()
    z = d.z.to_numpy()
    v = float(np.dot(t - t.mean(), z - z.mean()) / np.dot(t - t.mean(), t - t.mean()))
    return (v if v > 0 else fallback, len(d))

def upstream_features(n, zu, particle):
    cutoff = zu - 0.002
    after = np.flatnonzero(n.z.to_numpy() > cutoff)
    if len(after):
        n = n.iloc[:int(after[0])]
    pre = n[(n.z >= zu - 0.015) & (n.z <= cutoff)]
    if len(pre) < 4:
        return (None, 'fewer than4 strictly available upstream rows', None)
    vu, nu = slope(n, zu - 0.01, zu - 0.003)
    if vu is None:
        vu, nu = slope(n, zu - 0.015, cutoff)
    if vu is None:
        return (None, 'no positive strict upstream slope', None)
    vn, nn = slope(n, zu - 0.005, cutoff, vu)
    vf, nf = slope(n, zu - 0.015, zu - 0.01, vu)
    theta = pre.angle.dropna().to_numpy()
    g = np.cos(np.deg2rad(theta)) ** 2 if particle != 'S' else np.array([0.0])
    if not len(g):
        return (None, 'no finite upstream angle', None)
    ori = float(2 * g.mean() - 1) if particle != 'S' else 0.0
    spin = float(1 - abs(np.mean(np.exp(2j * np.deg2rad(theta))))) if particle != 'S' else 0.0
    xp = pre.x.to_numpy()
    zz = pre.z.to_numpy()
    sinu = float(np.sum(np.hypot(np.diff(xp), np.diff(zz))) / (zz[-1] - zz[0]) - 1) if zz[-1] > zz[0] else 0.0
    values = {'n_upstream_rows': len(pre), 'v_up_m_s': vu, 'v_near_m_s': vn, 'v_far_m_s': vf, 'history_log_ratio': float(np.log(vn / vf)), 'near_log_ratio': float(np.log(vn / vu)), 'orientation_cos2': ori, 'orientation_dispersion': spin, 'lateral_sinuosity': sinu, 'last_allowed_observation_s': float(pre.t.max()), 'n_v_up_rows': nu, 'n_v_near_rows': nn, 'n_v_far_rows': nf}
    meta = {'cos_squared': g.tolist(), 'latest_observation_s': float(pre.t.max()), 'cutoff_z_m': cutoff, 'max_input_z_m': float(pre.z.max())}
    assert meta['max_input_z_m'] <= cutoff
    return (values, None, meta)

def extract(partition):
    source = SOURCE
    split = SPLIT
    design = DESIGN
    if partition == 'confirmation':
        allowed = set(split['final_test_configs'])
    elif partition == 'development':
        allowed = set(split['development_configs'])
    else:
        raise ValueError('Unknown partition')
    rows = []
    excluded = []
    angles = {}
    profiles = []
    audits = []
    considered = 0
    with zipfile.ZipFile(source / 'raw/MPs_sinking_dynamics.zip') as zp, zipfile.ZipFile(source / 'raw/Density_and_refractive_index_profiles.zip') as zd:
        for name in zp.namelist():
            m = re.match('MPs_sinking_dynamics/MPs_position/IW1/set([123])_([123])/set\\1_\\2_(D_[abc]|R_[ab]|S)_run_(\\d+)\\.csv$', name)
            if not m:
                continue
            config = m[1] + '.' + m[2]
            if config not in allowed:
                continue
            considered += 1
            pt = m[3]
            run = m[4]
            rid = f'{config}/{pt}/{run}'
            n = read_member(zp, name, allowed)[['x', 'z', 't', 'angle']].apply(pd.to_numeric, errors='coerce')
            n = n[np.isfinite(n[['x', 'z', 't']]).all(axis=1)]
            n = n[n.t.diff().fillna(1) > 0]
            z = n.z.to_numpy()
            t = n.t.to_numpy()
            zu, zl = design['source_interface_bounds_m'][config]
            h = zl - zu
            ts = [passage(z, t, zu - dist) for dist in [0.015, 0.01, 0.005, 0.003, 0.002, 0]]
            end = passage(z, t, zl)
            coverage = (z >= zu - 0.015) & (z <= zu - 0.002) & (t <= ts[4])
            if not all((np.isfinite(v) for v in [ts[1], ts[3], ts[4], ts[5], end])) or end <= ts[5] or ts[3] <= ts[1] or (coverage.sum() < 4):
                excluded.append({'run_id': rid, 'config': config, 'particle': pt, 'source_member': name, 'reason': 'inadequate upstream coverage or unobserved/nonpositive transit'})
                continue
            inputs, reason, meta = upstream_features(n, zu, pt)
            if inputs is None:
                excluded.append({'run_id': rid, 'config': config, 'particle': pt, 'source_member': name, 'reason': reason})
                continue
            assert inputs['last_allowed_observation_s'] < ts[5]
            dn = f'Density_and_refractive_index_profiles/Density_and_RI_measured/set{m[1]}_{m[2]}.csv'
            rho = read_member(zd, dn, allowed).iloc[:, 1].dropna().to_numpy()
            drho = float(np.median(rho[-3:]) - np.median(rho[:3]))
            target = float(end - ts[5])
            t0 = h / inputs['v_up_m_s']
            row = {'Index': len(rows), 'run_id': rid, 'config': config, 'family': m[1], 'particle': pt, 'run': int(run), 'source_member': name, 'source_density_member': dn, 'n_native_rows': len(n), 'z_upper_m': zu, 'z_lower_m': zl, 'width_m': h, 'longest_m': LONGEST[pt] / 1000, **inputs, 'delta_density_kg_m3': drho, 'target_s': target, 'ballistic_s': t0, 'entry_time_s': float(ts[5]), 'log_response': float(np.log(target / t0))}
            rows.append(row)
            angles[rid] = {k: v for k, v in meta.items() if k != 'max_input_z_m'}
            audits.append({'run_id': rid, 'max_input_z_m': meta['max_input_z_m'], 'cutoff_z_m': zu - 0.002, 'latest_input_time_s': inputs['last_allowed_observation_s'], 'earliest_target_time_s': float(ts[5])})
            for frac in [0.25, 0.5, 0.75, 1.0]:
                tp = passage(z, t, zu + frac * h)
                if np.isfinite(tp):
                    profiles.append({'run_id': rid, 'config': config, 'particle': pt, 'fraction': frac, 'passage_s': float(tp - ts[5])})
    frame = pd.DataFrame(rows)
    assert set(frame.config) <= allowed
    return (frame, angles, pd.DataFrame(excluded), pd.DataFrame(profiles), pd.DataFrame(audits), {'partition': partition, 'native_iw1_considered': considered, 'eligible': len(frame), 'excluded': len(excluded), 'groups': frame.groupby('config').size().to_dict()})
