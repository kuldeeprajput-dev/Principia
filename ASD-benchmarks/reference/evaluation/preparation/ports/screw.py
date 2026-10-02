"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io
class IntegrityError(ValueError): pass
TARGET = 'late_mean_torque_Nm'

def arr(step):
    g = step['graph']
    x = np.array(g['angle values'], float)
    y = np.array(g['torque values'], float)
    if len(x) != len(y) or len(x) < 10 or (not np.isfinite(x).all()) or (not np.isfinite(y).all()):
        raise ValueError('malformed_graph')
    keep = np.r_[True, x[1:] > np.maximum.accumulate(x)[:-1]]
    x = x[keep]
    y = y[keep]
    x = x - x[0]
    ux, ii = np.unique(x, return_index=True)
    return (ux, y[ii])

def mean_window(x, y, a, b):
    if x[0] > a or x[-1] < b:
        raise ValueError('insufficient_angle_coverage')
    mid = (x > a) & (x < b)
    xx = np.r_[a, x[mid], b]
    yy = np.interp(xx, x, y)
    if len(xx) < 4 or np.diff(xx).max() > 35:
        raise ValueError('sparse_angle_window')
    return float(np.trapezoid(yy, xx) / (b - a))

def prefix_features(steps):
    """Use only Finding and the first native >=250deg sampled trigger, inclusive."""
    step = steps['Thread forming']
    g = step['graph']
    x = np.asarray(g['angle values'], float)
    if not len(x):
        raise ValueError('malformed_graph')
    crossing = np.flatnonzero(x - x[0] >= 250)
    if not len(crossing):
        raise ValueError('insufficient_angle_coverage')
    trigger_index = int(crossing[0])
    prefix = {'graph': {'angle values': g['angle values'][:trigger_index + 1], 'torque values': g['torque values'][:trigger_index + 1]}}
    px, py = arr(prefix)
    fx, fy = arr(steps['Finding'])
    return ({'early': mean_window(px, py, 0, 250), 'gradient_proxy': mean_window(px, py, 100, 250) - mean_window(px, py, 0, 100), 'finding': float(np.trapezoid(fy, fx) / (fx[-1] - fx[0])), 'roughness': float(np.std(py[px <= 250]))}, trigger_index)

def timing(d, steps, op, eligible):
    step = steps['Thread forming']
    g = step['graph']
    x = np.asarray(g['angle values'], float)
    t = np.asarray(g['time values'], float)
    x = x - x[0]
    if len(x) != len(t) or not np.isfinite(t).all() or (np.diff(t) < 0).any():
        raise IntegrityError('Malformed/nonmonotonic acquisition clock: ' + op['run_id'])
    keep = np.r_[True, x[1:] > np.maximum.accumulate(x)[:-1]]
    x = x[keep]
    t = t[keep]
    j = int(np.searchsorted(x, 250))
    if j >= len(x):
        return None
    ideal = float(np.interp(250, x, t))
    trigger = float(t[j])
    target_j = int(np.searchsorted(x, 1300))
    ft = np.array(steps['Finding']['graph']['time values'], float)
    if not np.isfinite(ft).all() or max(ft) > trigger + 1e-09:
        raise IntegrityError('Finding unavailable at trigger: ' + op['run_id'])
    duration = max(float(d['total time']), max((float(np.max(s['graph']['time values'])) for s in d['tightening steps'] if 'graph' in s)))
    return {'run_id': op['run_id'], 'workpiece_id': op['workpiece_id'], 'location': op['workpiece_location'], 'usage': int(op['workpiece_usage']), 'source_wallclock_timestamp': op['workpiece_date'], 'source_timestamp_timezone': 'unspecified', 'source_timestamp_origin': 'start versus completion not documented; conservative bounds used', 'trigger_time_relative_s': trigger, 'trigger_angle_relative_deg': float(x[j]), 'interpolated_ideal_crossing_time_s': ideal, 'sampled_trigger_latency_s': trigger - ideal, 'angle_overshoot_deg': float(x[j] - 250), 'finding_last_sample_time_s': float(max(ft)), 'target_last_needed_sample_time_s': float(t[target_j]) if target_j < len(t) else None, 'conservative_full_operation_duration_s': duration, 'primary_target_eligible': eligible}

def extract(archive, split, partition, authorization_receipt=None):
    if partition not in ('development', 'sealed_test'):
        raise IntegrityError('Unknown partition')
    if partition == 'sealed_test' and (not (authorization_receipt or {}).get('authorization_sha256')):
        raise IntegrityError('Adapter refuses final partition without verified archive authorization receipt')
    names = {}
    for n in archive.namelist():
        if n.endswith('.json'):
            name = Path(n).name
            if name in names:
                raise IntegrityError('Ambiguous native filename: ' + name)
            names[name] = n
    valid = []
    ledger = []
    read_names = []
    times = []
    for op in split['operations']:
        group = split['groups'][op['workpiece_id']]
        if group['partition'] != partition:
            continue
        r = dict(op, fold=group['fold'], surface_class=group['class'])
        r['usage'] = int(r.pop('workpiece_usage'))
        r['left'] = int(r['workpiece_location'] == 'left')
        name = names[r['file_name']]
        d = json.loads(archive.read(name))
        read_names.append(name)
        steps = {s['name']: s for s in d['tightening steps']}
        try:
            x, y = arr(steps['Thread forming'])
            fx, fy = arr(steps['Finding'])
            f, _ = prefix_features(steps)
            r.update(f)
            r[TARGET] = mean_window(x, y, 700, 1300)
            r['source_threadforming_span_deg'] = float(x[-1])
            r['source_threadforming_points'] = len(x)
            valid.append(r)
            reason = 'eligible'
        except (ValueError, KeyError, TypeError, ZeroDivisionError) as e:
            reason = str(e)
        ledger.append({k: r[k] for k in ['run_id', 'workpiece_id', 'surface_class', 'usage', 'workpiece_location']} | {'status': reason})
        try:
            tr = timing(d, steps, op, reason == 'eligible')
        except (KeyError, TypeError, ValueError, IndexError) as e:
            if reason == 'eligible':
                raise IntegrityError('Cannot establish prediction timing: ' + op['run_id']) from e
            tr = None
        if tr is not None:
            times.append(tr)
    df = pd.DataFrame(valid).sort_values(['workpiece_id', 'workpiece_location', 'workpiece_date', 'run_id'])
    out = []
    for _, g in df.groupby(['workpiece_id', 'workpiece_location'], sort=True):
        past = []
        for _, row in g.iterrows():
            r = row.to_dict()
            p = past[-1] if past else None
            r['has_history'] = int(p is not None)
            r['prev_y'] = p[TARGET] if p else r['early']
            r['prev_early'] = p['early'] if p else r['early']
            r['prev_gradient'] = p['gradient_proxy'] if p else r['gradient_proxy']
            r['prev_usage'] = p['usage'] if p else r['usage']
            r['first_y'] = past[0][TARGET] if past else r['early']
            r['mean_past_y'] = float(np.mean([p[TARGET] for p in past])) if past else r['early']
            r['history_gap'] = r['usage'] - p['usage'] if p else 0
            if p and (r['usage'] <= p['usage'] or r['workpiece_date'] <= p['workpiece_date']):
                raise IntegrityError('Noncausal source sequence')
            out.append(r)
            past.append(r)
    df = pd.DataFrame(out)
    a = pd.DataFrame(times)
    lookup = a.set_index('run_id')
    margins = []
    for _, g in df.groupby(['workpiece_id', 'workpiece_location'], sort=True):
        previous = None
        for _, r in g.iterrows():
            curr = lookup.loc[r.run_id]
            if previous is not None:
                prev = lookup.loc[previous]
                current_earliest = pd.Timestamp(curr.source_wallclock_timestamp) - pd.Timedelta(seconds=curr.conservative_full_operation_duration_s + 1 - curr.trigger_time_relative_s)
                previous_latest = pd.Timestamp(prev.source_wallclock_timestamp) + pd.Timedelta(seconds=prev.target_last_needed_sample_time_s + 1)
                margin = (current_earliest - previous_latest).total_seconds()
                if margin <= 0:
                    raise IntegrityError('Prior response not proven available: ' + r.run_id)
                margins.append({'run_id': r.run_id, 'previous_run_id': previous, 'workpiece_id': r.workpiece_id, 'location': r.workpiece_location, 'conservative_history_margin_s': margin})
            previous = r.run_id
    expected = {w for w, g in split['groups'].items() if g['partition'] == partition}
    if not set(df.workpiece_id).issubset(expected):
        raise IntegrityError('Cross-partition extraction')
    audit = {'partition': partition, 'json_members_read': len(read_names), 'json_read_names': read_names, 'operation_denominator': len(ledger), 'workpiece_denominator': len(expected), 'eligible_operations': len(df), 'eligible_workpieces': int(df.workpiece_id.nunique()), 'unscorable_workpieces': sorted(expected - set(df.workpiece_id)), 'coverage_status': dict(collections.Counter((x['status'] for x in ledger))), 'maximum_trigger_latency_s': float(a.sampled_trigger_latency_s.max()), 'maximum_trigger_overshoot_deg': float(a.angle_overshoot_deg.max()), 'history_links': len(margins), 'minimum_history_margin_s': min([x['conservative_history_margin_s'] for x in margins], default=None), 'causal_timing_passed': True}
    return (df, pd.DataFrame(ledger), a, pd.DataFrame(margins), audit)
