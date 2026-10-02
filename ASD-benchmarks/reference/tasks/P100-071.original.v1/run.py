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

# Scientific equation implementation is inserted below during packaging.
def predict(model, d):
    # Fixed development imputation and standardization; never learn from these rows.
    columns = [np.isfinite(d.deltaeps_fc4.to_numpy(float)).astype(float) if f == 'cole_available'
               else d[f].to_numpy(float) for f in model['features']]
    x = np.column_stack(columns)
    missing = ~np.isfinite(x)
    x = np.where(missing, np.asarray(model['medians']), x)
    z = (np.column_stack([x, missing.astype(float)])-np.asarray(model['means']))/np.asarray(model['scales'])
    if model.get('kind') == 'rbf_kernel':
        centers = np.asarray(model['training_x_standardized'])
        squared_distance = np.maximum(0,(z*z).sum(1)[:,None]+(centers*centers).sum(1)[None,:]-2*z@centers.T)
        return np.maximum(0,model['intercept']+np.exp(-model['gamma']*squared_distance)@np.asarray(model['dual_coefficients']))
    return np.maximum(0,np.column_stack([np.ones(len(d)),z])@np.asarray(model['coefficients']))


def read_table(path):
    return pd.read_csv(path, dtype={'sample_id': str, 'group': str, 'router': str,
                                    'port': str, 'family': str, 'particle': str},
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
