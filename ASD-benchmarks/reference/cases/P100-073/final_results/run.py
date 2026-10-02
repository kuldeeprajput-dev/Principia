#!/usr/bin/env python3
"""Frozen prediction equations and confirmation replay. No training is performed.

Run: python run.py
Save a replay: python run.py --output /path/to/new-directory
Predict other prepared inputs: python run.py --input inputs.csv --output /path/to/new-directory
The preparation contract and units are in data/README.md.
"""
from pathlib import Path
import argparse, hashlib, json
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent

# Frozen scientific equations, preserved from this campaign.
def _vector(d, key):
    return d[key].to_numpy(float)

def _rumen(m, d):
    t=_vector(d,'hour');g8=_vector(d,'g8');g4=_vector(d,'g4');y=np.zeros(len(d))
    if m['kind']=='persistence': return g8
    if m['kind']=='linear_prefix': return g8+np.maximum(0,g8-g4)*(t-8)/4
    if m['kind']=='empirical_ratio':
        return np.array([row.g8*m['ratios'].get(f'{row.trial}|{row.algae}|{row.hour:g}',m['fallback'][f'{row.trial}|{row.hour:g}']) for row in d.itertuples()])
    for trial, p in m['trial_parameters'].items():
        ix=d.trial.astype(str).to_numpy()==trial
        tt=t[ix];a=g8[ix];b=g4[ix];ratio=b/a
        kind=m['kind']
        if kind in ['first_order','stretched','curvature','treatment_shape','lag_shape']:
            tau=np.full(len(tt),p['tau_h']);beta=p.get('beta',1.)
            if 'gamma_curvature' in p:tau=tau*np.exp(p['gamma_curvature']*(ratio-.5))
            if 'algae_log_tau' in p:tau=tau*np.exp([p['algae_log_tau'].get(x,0.) for x in d.loc[ix,'algae']])
            lag=p.get('lag_h',0.)
            f=-np.expm1(-np.power(np.maximum(0,tt-lag)/tau,beta));f8=-np.expm1(-np.power((8-lag)/tau,beta));z=a*f/f8
        elif kind=='dual_pool':
            w=p['fast_fraction'];tf=p['tau_fast_h'];ts=p['tau_slow_h']
            f=w*(-np.expm1(-tt/tf))+(1-w)*(-np.expm1(-tt/ts));f8=w*(-np.expm1(-8/tf))+(1-w)*(-np.expm1(-8/ts));z=a*f/f8
        elif kind in ['tangent_decay','tangent_curvature']:
            tau=p['tau_h']*np.exp(p.get('gamma_curvature',0.)*(ratio-.5))
            z=a+p['rate_multiplier']*np.maximum(0,a-b)*(tau/4)*(-np.expm1(-(tt-8)/tau))
        else:raise ValueError(kind)
        y[ix]=z
    return y

def soil_shape(m, d):
    x=(_vector(d,'t05')-10)/10
    M=_vector(d,'tsmoisture');missing=~np.isfinite(M);M=np.where(missing,30,M);z=(M-30)/30
    p=m.get('parameters',{})
    kind=m['kind'];eta=p.get('b',0)*x+p.get('missing',0)*missing
    if kind=='lloyd_taylor':
        eta=p['E0_K']*(1/(10+46.02)-1/(_vector(d,'t05')+46.02))
    if kind in ['moisture_optimum','temperature_moisture','site_heterogeneity','seasonal','trench_sensitivity','wet_asymmetry']:
        eta+=p.get('c',0)*z+p.get('d',0)*z*z+p.get('interaction',0)*x*z
    if kind=='dry_saturation':
        K=p['K_percent'];eta+=np.log(np.maximum(1e-9,M/(K+M)/(30/(K+30))))*(~missing)
    if kind in ['site_heterogeneity','seasonal','trench_sensitivity','wet_asymmetry']:
        eta+=np.array([p['site_b_deviation'].get(s,0.) for s in d.site])*x
    if kind in ['seasonal','trench_sensitivity','wet_asymmetry']:
        phase=2*np.pi*(_vector(d,'doy')-1)/365.25
        eta+=p.get('season_sin',0)*np.sin(phase)+p.get('season_cos',0)*np.cos(phase)
    if kind in ['trench_sensitivity','wet_asymmetry']:
        trenched=d.context.str.endswith('|True').to_numpy(float)
        eta+=p.get('trench_b',0)*x*trenched
    if kind=='wet_asymmetry':eta+=p.get('wet_cube',0)*np.maximum(z,0)**3
    return np.exp(np.clip(eta,-15,15))

def flexible_features(m,d):
    keys=m['numeric_features'];x=np.column_stack([_vector(d,k) for k in keys]);bad=~np.isfinite(x)
    x=np.where(bad,np.asarray(m['medians']),x)
    z=(x-np.asarray(m['means']))/np.asarray(m['scales'])
    columns=[z,bad.astype(float)]
    for key,values in m['categories'].items():columns.append((d[key].astype(str).to_numpy()[:,None]==np.asarray(values)[None,:]).astype(float))
    return np.column_stack(columns)

def predict(m,d):
    if m['kind']=='rbf_ridge':
        z=flexible_features(m,d);c=np.asarray(m['centers']);dist=np.maximum(0,(z*z).sum(1)[:,None]+(c*c).sum(1)[None,:]-2*z@c.T)
        return np.maximum(0,m['intercept']+np.exp(-m['gamma']*dist)@np.asarray(m['coefficients']))
    if m['case']=='rumen':return _rumen(m,d)
    f=soil_shape(m,d)
    a=np.array([m['context_amplitudes'].get(c,m['site_fallback'].get(s,m['global_fallback'])) for c,s in zip(d.context,d.site)])
    return a*f

def read_table(path):
    return pd.read_csv(path, dtype={'sample_id': str, 'group': str, 'router': str,
                                    'port': str, 'family': str, 'particle': str, 'cure': str, 'trial': str, 'algae': str, 'site': str, 'context': str, 'gas': str},
                       float_precision='round_trip')

def verify_package():
    manifest = json.loads((HERE / 'MANIFEST.json').read_text())
    for entry in manifest['files']:
        path = (HERE / entry['path']).resolve()
        if not path.is_relative_to(HERE) or not path.is_file():
            raise ValueError('Missing or escaping package file: ' + entry['path'])
        data = path.read_bytes()
        if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Package checksum mismatch: ' + entry['path'])
    return manifest

def evaluate(predictions, observed, spec):
    if not predictions.sample_id.equals(observed.sample_id):
        raise ValueError('Observation identity/order mismatch')
    results, groups = [], []
    for model_id in spec['models']:
        d = observed.copy()
        d['error'] = predictions[model_id] - d.target
        if np.isinf(d.target).any():
            raise ValueError('Infinite observed target')
        d = d[np.isfinite(d.target)].copy()
        d['absolute_error'] = abs(d.error)
        d['squared_error'] = d.error ** 2
        if spec['metric_kind'] == 'log_transit':
            if (d.target <= 0).any() or (predictions[model_id] <= 0).any():
                raise ValueError('Transit times must be positive')
            d['absolute_log_error'] = abs(np.log((d.error + d.target) / d.target))
            cells = d.groupby(['group', 'particle'])[['absolute_error', 'squared_error', 'error', 'absolute_log_error']].mean()
            g = cells.groupby('group').mean()
            g['primary_error'] = g.absolute_log_error
        else:
            g = d.groupby('group')[['absolute_error', 'squared_error', 'error']].mean()
            g['primary_error'] = np.sqrt(g.squared_error) if spec['metric_kind'] == 'rmse' else g.absolute_error
        g['model'] = model_id
        g['scored_rows'] = d.groupby('group').size()
        groups.append(g.reset_index())
        results.append({'model': model_id, 'primary_error': float(g.primary_error.mean()),
                        'mean_group_absolute_error': float(g.absolute_error.mean()),
                        'groups': len(g), 'scored_rows': len(d), 'assigned_rows': spec['assigned_rows'],
                        'primary_units': spec['metric_units']})
    return pd.DataFrame(results), pd.concat(groups, ignore_index=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Prepared predictor table; does not read bundled observations')
    parser.add_argument('--output', type=Path, help='New output directory; existing directories are rejected')
    args = parser.parse_args()
    verify_package()
    if args.output and args.output.exists():
        raise FileExistsError('Choose a new output directory')
    spec = json.loads((HERE / 'rules.json').read_text())
    inputs = read_table(args.input or HERE / 'data/inputs.csv.gz')
    required = ['sample_id', 'group'] + spec['input_columns']
    missing = set(required) - set(inputs)
    if missing:
        raise ValueError('Missing declared input columns: ' + ', '.join(sorted(missing)))
    if inputs.sample_id.isna().any() or not inputs.sample_id.is_unique or inputs.group.isna().any():
        raise ValueError('Sample identities must be unique and group identifiers present')
    for col in spec['numeric_columns']:
        values = pd.to_numeric(inputs[col], errors='raise').to_numpy(float)
        if np.isinf(values).any() or (not spec['allows_missing_predictors'] and np.isnan(values).any()):
            raise ValueError('Nonfinite predictor: ' + col)
    predictions = inputs[['sample_id', 'group']].copy()
    for model_id, model in spec['models'].items():
        y = predict(model, inputs)
        if np.asarray(y).shape != (len(inputs),) or not np.isfinite(y).all():
            raise ValueError('Invalid model predictions: ' + model_id)
        predictions[model_id] = y
    metrics = groups = None
    if args.input is None:
        expected = read_table(HERE / 'evidence/predictions.csv.gz')
        if not expected[['sample_id','group']].equals(predictions[['sample_id','group']]):
            raise ValueError('Reference sample identity/order mismatch')
        maximum = 0.0
        for model_id in spec['models']:
            error = float(np.max(abs(predictions[model_id] - expected[model_id])))
            if error > 1e-8:
                raise ValueError('Saved predictions do not reproduce: ' + model_id)
            maximum = max(maximum, error)
        metrics, groups = evaluate(predictions, read_table(HERE / 'data/observations.csv.gz'), spec)
        expected_metrics = pd.read_csv(HERE / 'evidence/metrics.csv', float_precision='round_trip').set_index('model')
        for row in metrics.itertuples():
            if abs(row.primary_error - expected_metrics.loc[row.model, 'primary_error']) > 1e-9:
                raise ValueError('Saved primary metric does not reproduce: ' + row.model)
        print(metrics[['model','primary_error','primary_units','groups','scored_rows']].to_string(index=False))
        print(f'PASS: frozen predictions and primary metrics reproduced; maximum prediction difference {maximum:.3g}.')
    else:
        print(f'Computed {len(inputs)} rows with frozen models. No validation claim is made for custom inputs.')
    if args.output:
        args.output.mkdir(parents=True)
        predictions.to_csv(args.output / 'predictions.csv', index=False)
        if metrics is not None:
            metrics.to_csv(args.output / 'metrics.csv', index=False)
            groups.to_csv(args.output / 'by_group.csv', index=False)

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, FileNotFoundError, FileExistsError, json.JSONDecodeError) as error:
        raise SystemExit('ERROR: ' + str(error))
