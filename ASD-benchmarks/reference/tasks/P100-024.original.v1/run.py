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
def fatigue_design(spec,d):
    n=np.maximum(d.cycle.to_numpy()-20,0);e=d.strain_percent.to_numpy();l=np.log1p(n/1000);t=n/1e5
    kind=spec['kind']
    if kind=='log':return (l*e**2)[:,None]
    if kind=='power':return (t**.25*e**4)[:,None]
    if kind=='saturation':return ((1-np.exp(-t))*e**2)[:,None]
    if kind=='two_mechanism':return np.column_stack([l*e**2,t*e**6])
    if kind=='cure_strain':return np.column_stack([l*e**2]+[l*e**6*(d.cure.to_numpy()==c) for c in ['EQA01','EQA02','EQA03']])
    if kind=='frequency':return np.column_stack([l*e**2,l*e**2*np.sqrt(d.frequency_Hz.to_numpy()/5)])
    if kind=='delayed':return np.column_stack([l*e**2,np.maximum(t-.1,0)*e**6])
    if kind=='sqrtdose':return np.column_stack([l*e**2,np.sqrt(t)*e**4])
    raise ValueError(kind)

def homogeneous(d):
    x=d.quality.to_numpy();rl=d.rho_liquid.to_numpy();rv=d.rho_vapor.to_numpy()
    return (x/rv)/(x/rv+(1-x)/rl)

def boiling_design(spec,d):
    a=homogeneous(d);eta=np.log(a/(1-a));r=d.radial_fraction.to_numpy();g=np.log(d.massflux_kg_m2_s.to_numpy()/700);p=np.log(d.pressure_Pa.to_numpy()/7e6)
    k=spec['kind'];one=np.ones(len(d));b=r*r
    if k=='slip':return one[:,None],eta
    if k=='radial':return np.column_stack([one,b]),eta
    if k=='fluxslip':return np.column_stack([one,g]),eta
    if k=='qualityradial':return np.column_stack([one,b,b*eta]),eta
    if k=='combined':return np.column_stack([one,b,b*eta,g]),eta
    if k=='quartic':return np.column_stack([one,b,b*eta,g,r**4]),eta
    if k=='pressure':return np.column_stack([one,b,b*eta,g,p]),eta
    raise ValueError(k)

def flexible_x(case,d):
    if case.startswith('24'):
        return np.column_stack([np.log1p(d.cycle.to_numpy()/1000),d.strain_percent,d.frequency_Hz]+[(d.cure.to_numpy()==c).astype(float) for c in ['EQA01','EQA02','EQA03']])
    return np.column_stack([np.log(d.quality/(1-d.quality)),np.log(d.massflux_kg_m2_s/700),d.radial_fraction,np.log(d.pressure_Pa/7e6)])

def predict(model,d):
    case=model['case'];kind=model['spec']['kind']
    if case.startswith('24'):
        if not set(d.cure).issubset({'EQA01','EQA02','EQA03'}) or (d.E0_GPa<=0).any() or (d.cycle<1000).any() or (d.strain_percent<=0).any() or (d.frequency_Hz<=0).any():
            raise ValueError('Invalid fatigue predictors or undeclared laminate/cure')
    else:
        if ((d.quality<=0)|(d.quality>=1)).any() or ((d.radial_fraction<0)|(d.radial_fraction>1)).any() or (d.pressure_Pa<=0).any() or (d.massflux_kg_m2_s<=0).any() or (d.rho_liquid<=0).any() or (d.rho_vapor<=0).any():
            raise ValueError('Invalid two-phase boundary or radial predictors')
    if kind=='persistence':return d.E0_GPa.to_numpy()
    if kind=='mean':return np.repeat(model['value'],len(d))
    if kind=='homogeneous':return homogeneous(d)
    if kind=='flex':
        xx=(flexible_x(case,d)-np.array(model['mean']))/np.array(model['scale']);c=np.array(model['centers']);k=np.exp(-np.sum((xx[:,None,:]-c[None,:,:])**2,axis=2)/(2*model['bandwidth']**2));z=np.column_stack([np.ones(len(d)),k])@np.array(model['coefficients'])
        return d.E0_GPa.to_numpy()*np.clip(z,0,1) if case.startswith('24') else np.clip(z,0,1)
    if case.startswith('24'):
        return d.E0_GPa.to_numpy()*np.exp(-np.clip(fatigue_design(model['spec'],d)@np.array(model['coefficients']),0,100))
    if kind=='drift':
        jg=d.massflux_kg_m2_s.to_numpy()*d.quality.to_numpy()/d.rho_vapor.to_numpy();jl=d.massflux_kg_m2_s.to_numpy()*(1-d.quality.to_numpy())/d.rho_liquid.to_numpy();C,V=model['coefficients']
        return np.clip(jg/(C*(jg+jl)+V),0,1)
    xx,eta=boiling_design(model['spec'],d);z=np.clip(eta+xx@np.array(model['coefficients']),-30,30)
    return 1/(1+np.exp(-z))

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
