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
def pstate(model,frame):
    m=frame.membrane_index.to_numpy(dtype=int);t=frame.temperature_K.to_numpy(float)
    p=model['calibration'];lr=np.array([z['log_P_ref'] for z in p])[m];b=np.array([z['activation_over_R_K'] for z in p])[m];n=np.array([z['pressure_exponent'] for z in p])[m]
    return np.exp(lr+b*(1/673.15-1/t)),n

def gasidx(f):return np.array([{'N2':0,'Ar':1,'He':2}[g] for g in f.gas])

def baseflux(model,f):
    p,n=pstate(model,f);ph=f.feed_fraction.to_numpy()*f.retentate_bar.to_numpy();pp=f.permeate_bar.to_numpy()
    return p*np.maximum(ph**n-pp**n,0)

def rfeatures(f):
    m=f.membrane_index.to_numpy(int);g=gasidx(f)
    return np.column_stack([(f.temperature_K.to_numpy()-673.15)/50,f.feed_fraction.to_numpy(),np.log(f.normal_flow_L_min.to_numpy()/5),np.eye(4)[m],np.eye(3)[g]])

def predict(model,f):
    raw_m=f.membrane_index.to_numpy(float)
    if np.any(~np.isfinite(raw_m)) or np.any(raw_m != np.floor(raw_m)) or np.any((raw_m<0)|(raw_m>3)):
        raise ValueError('Membrane index must be an integer from 0 to 3')
    if not set(f.gas).issubset({'N2','Ar','He'}):
        raise ValueError('Unknown calibrated inert gas')
    for column in ['temperature_K','normal_flow_L_min','area_m2','diameter_m','retentate_bar']:
        values=f[column].to_numpy(float)
        if np.any(~np.isfinite(values)) or np.any(values<=0):
            raise ValueError('Positive finite physical input required: '+column)
    fraction=f.feed_fraction.to_numpy(float);pressure=f.permeate_bar.to_numpy(float)
    if np.any(~np.isfinite(fraction)) or np.any((fraction<=0)|(fraction>1)) or np.any(~np.isfinite(pressure)) or np.any(pressure<0):
        raise ValueError('Invalid feed fraction or absolute permeate pressure')
    kind=model['kind'];m=raw_m.astype(int)
    if kind=='mean':return np.array(model['means'])[m]
    j0=baseflux(model,f)
    if kind in ['richardson','sieverts']:return j0
    if kind=='rbf':
        x=(rfeatures(f)-np.array(model['center']))/np.array(model['scale']);train=np.array(model['train_features']);sq=np.maximum((x*x).sum(1)[:,None]+(train*train).sum(1)[None,:]-2*x@train.T,0)
        z=np.exp(-sq/(2*model['bandwidth']**2))@np.array(model['weights'])
        return j0*np.exp(np.clip(z,-3,3))
    v=np.array(model['parameters']);g=gasidx(f);flow=f.normal_flow_L_min.to_numpy();temp=f.temperature_K.to_numpy()
    if kind=='suppression':
        kk=np.exp(v[:4])[m];gas=np.exp(np.r_[0,v[4:6]])[g]
        return j0/(1+kk*gas*(1-f.feed_fraction.to_numpy())*(5/flow)**.6)
    # implicit nonnegative transport; bounded by feedhydrogen, partialpressure and membrane laws
    p,n=pstate(model,f);pr=f.retentate_bar.to_numpy();pp=f.permeate_bar.to_numpy();x=f.feed_fraction.to_numpy();area=f.area_m2.to_numpy()
    vm=model.get('normal_molar_volume_L',22.414);fin=flow/(60*vm)
    rho=0. if kind=='film' else (model.get('depletion_fraction',.5) if kind!='depletion' else float(v[0]))
    if kind=='depletion':k=np.full(len(f),np.inf)
    elif kind=='shared':
        kval=np.exp(v[0])*(.014/f.diameter_m.to_numpy());gas=np.exp(np.r_[0,v[1:3]])[g];k=kval*gas*(flow/5)**.6*(temp/673.15)**1.75
    else:
        kval=np.exp(v[:4])[m];gas=np.exp(np.r_[0,v[4:6]])[g]
        power=.6 if kind in ['film','coupled'] else float(v[6])
        exponent=1.75 if kind!='thermal' else float(v[7])
        k=kval*gas*(flow/5)**power*(temp/673.15)**exponent
    lo=np.zeros(len(f));hi=np.minimum(j0,fin*x/area*.999999)
    for _ in range(60):
        j=(lo+hi)/2;z=j*area/fin;bulk=(x-rho*z)/(1-rho*z)
        surface=pr*bulk-j/k
        pred=p*np.maximum(np.maximum(surface,pp)**n-pp**n,0)
        positive=pred>j;lo=np.where(positive,j,lo);hi=np.where(positive,hi,j)
    return (lo+hi)/2

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
