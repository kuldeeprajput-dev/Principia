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
BASE = ['early','finding','gradient_proxy','roughness','usage','left','has_history',
        'prev_y','prev_early','prev_gradient','first_y','mean_past_y','history_gap']

def design(d, kind, exponent):
    e, f, g = (d[k].to_numpy(float) for k in ['early','finding','gradient_proxy'])
    n = d.usage.to_numpy(float)
    q = (1+n)**(-exponent)
    de = e - d.prev_early.to_numpy(float)
    dg = g - d.prev_gradient.to_numpy(float)
    one = np.ones(len(d))
    if kind in ['B3','B5']:
        return np.column_stack([one]+[d[k].to_numpy(float) for k in BASE]+[q,np.log1p(n),de,dg])
    if kind == 'A3':
        return np.column_stack([one,e,f,g,q,e*q])
    if kind == 'C1':
        return np.column_stack([one,e,f,g,d.left.to_numpy(float)])
    if kind == 'A9':
        relative_change = abs(de)/(abs(d.prev_early.to_numpy(float))+.05)
        gate = relative_change/(1+relative_change)
        return np.column_stack([one,de,dg,q,de*q,d.prev_y.to_numpy(float)-d.prev_early.to_numpy(float),d.left.to_numpy(float),abs(de)*gate])
    raise ValueError('Unknown screw equation')

def predict(model, d):
    if (d.usage < 0).any() or not set(d.left).issubset({0,1}) or not set(d.has_history).issubset({0,1}):
        raise ValueError('Invalid reuse/history/location inputs')
    if model['kind'] == 'B4':
        # Export of the already fitted histogram-gradient-boosting trees.
        # Leaf values include the original learning rate; no sklearn/pickle is needed.
        x = d[model['features']].to_numpy(float)
        result = np.full(len(d), model['baseline'])
        for tree in model['trees']:
            nodes = np.zeros(len(d), dtype=int)
            pending = np.ones(len(d), dtype=bool)
            while pending.any():
                for node_index in np.unique(nodes[pending]):
                    rows = np.flatnonzero(pending & (nodes == node_index))
                    node = tree[int(node_index)]
                    if node['leaf']:
                        result[rows] += node['value']; pending[rows] = False
                    else:
                        values = x[rows, node['feature']]
                        left = np.where(np.isnan(values), node['missing_left'], values <= node['threshold'])
                        nodes[rows] = np.where(left, node['left'], node['right'])
        return result
    result = design(d, model['kind'], model['p']) @ np.asarray(model['beta'])
    if model['kind'] == 'A9':
        result += d.prev_y.to_numpy(float)
        cold = d.has_history.to_numpy() == 0
        if cold.any():result[cold] = predict(model['cold_model'], d[cold])
        virgin = d.usage.to_numpy() == 0
        if virgin.any():result[virgin] = predict(model['virgin_model'], d[virgin])
    return result


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
