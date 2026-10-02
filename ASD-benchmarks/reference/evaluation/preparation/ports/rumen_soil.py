"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys, json, hashlib, re, zipfile, datetime, io, math, time, collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io
CASES = ['73_agriculture_rumen_fermentation', '82_ecology_soil_respiration']

def rumen():
    case = CASES[0]
    rows = []
    for trial, f in enumerate(['11_invitro_gasdata_01.csv', '13_invitro_gasdata_02.csv', '15_invitro_gasdata_03.csv'], 1):
        raw = pd.read_csv(DATA / case / 'raw' / f, sep=';', encoding='utf-8-sig')
        raw['source_row'] = np.arange(len(raw)) + 2
        for (run, flask), v in raw.groupby(['DG', 'Flask'], sort=True):
            assert not v.Hour.duplicated().any()
            q = v.set_index('Hour')
            early = q.loc[[4, 8], 'GasVolume'].to_numpy(float)
            if not np.isfinite(early).all() or early[1] <= 0:
                raise ValueError('Unexpected nonpositive or missing causal early volume')
            for hour in [12, 24, 36, 48]:
                r = q.loc[hour]
                rows.append({'sample_id': f'T{trial}-R{run}-F{flask}-H{hour}', 'group': f'T{trial}-R{run}', 'vessel': f'T{trial}-R{run}-F{flask}', 'trial': str(trial), 'run': int(run), 'algae': str(r.Algae), 'hour': float(hour), 'g4': float(early[0]), 'g8': float(early[1]), 'target': float(r.GasVolume), 'partition': 'confirmation' if run == 4 else 'development', 'source_file': f, 'source_row': int(r.source_row), 'early_source_rows': ','.join((str(int(z)) for z in q.loc[[4, 8], 'source_row']))})
    d = pd.DataFrame(rows)
    protocol = {'case_id': case, 'target': 'GasVolume', 'units': 'mL', 'prediction_time': '8h', 'prediction_horizons_h': [12, 24, 36, 48], 'input_columns': ['trial', 'algae', 'hour', 'g4', 'g8'], 'numeric_columns': ['hour', 'g4', 'g8'], 'allows_missing_predictors': False, 'group': 'trial/run; whole vessels stay together', 'reserved': 'DG4 in all three trials; outcomes sealed until freeze', 'development_validation': 'leave one DG index (1,2,3) out across all trials; training has other two indices', 'primary_metric': 'mean complete-run RMSE (all four horizons per vessel), equal weight each run', 'metric_kind': 'rmse', 'metric_units': 'mL', 'forbidden_inputs': ['DMD_g', 'GasDM', 'end-of-incubation pH', 'SCFA', 'gas composition', 'same-vessel values after 8h'], 'baseline_families': ['trial/algae/horizon empirical ratio', 'trial first-order saturation', 'constrained RBF ridge'], 'selection': 'best development mean-run RMSE; simpler equation if within 1% of best; extension requires >=5% improvement over all baselines and majority reserved groups', 'stopping': '>=5 substantive attempts; stop after two consecutive attempts fail >1% best RMSE improvement or distinct supported explanatory gain', 'author_preprocessing': 'blank correction and conversion of measured pressure to cumulative volume by authors; no new blank correction', 'scope': 'future within-vessel volume from first8h, across independent runs of the same three protocols; not animal methane emission or digestibility'}
    base = freeze(case, d, protocol)

def soil():
    case = CASES[1]
    r = pd.read_csv(DATA / case / 'raw/holisoils_soil_respiration_dataset.csv')
    r['source_row'] = np.arange(len(r)) + 2
    dates = r[['siteid', 'date']].drop_duplicates()
    split = {}
    for site, v in dates.groupby('siteid'):
        dd = sorted(v.date)
        n = max(1, int(np.ceil(0.2 * len(dd))))
        split.update({(site, date): 'confirmation' if date in dd[-n:] else 'development' for date in dd})
    valid = np.isfinite(r.t05) & r.t05.between(-15, 50) & np.isfinite(r.flux) & (r.tsmoisture.isna() | r.tsmoisture.between(0, 100))
    d = r.loc[valid, ['siteid', 'date', 'subsiteid', 'point', 'trenched', 'treatment', 't05', 'tsmoisture', 'flux', 'source_row']].copy()
    d['sample_id'] = ['S82-row' + str(x) for x in d.source_row]
    d['site'] = d.siteid
    d['context'] = d.siteid.astype(str) + '|' + d.subsiteid.astype(str) + '|' + d.trenched.fillna('unspecified').astype(str)
    d['doy'] = pd.to_datetime(d.date).dt.dayofyear.astype(float)
    d['target'] = d.flux
    d['partition'] = [split[s, t] for s, t in zip(d.siteid, d.date)]
    d['group'] = d.siteid.astype(str) + '|' + d.partition
    d['source_file'] = 'holisoils_soil_respiration_dataset.csv'
    d = d[['sample_id', 'group', 'site', 'context', 'date', 'point', 'treatment', 'trenched', 'doy', 't05', 'tsmoisture', 'target', 'partition', 'source_file', 'source_row']]
    protocol = {'case_id': case, 'target': 'flux', 'units': 'g CO2 m^-2 h^-1', 'prediction_time': 'same-date environmental inputs, before chamber response is available', 'input_columns': ['site', 'context', 't05', 'tsmoisture', 'doy'], 'numeric_columns': ['t05', 'tsmoisture', 'doy'], 'allows_missing_predictors': True, 'group': 'one whole future block per site for final metric; development keeps whole dates in each chronological fold; collars may reappear on earlier dates', 'reserved': 'latest ceil(20%) of native measurement dates per site, selected on dates before response inspection', 'development_validation': '3 chronological blocks: train first40%/55%/70% of development dates per site and validate next15%/15%/30%, respectively; whole dates', 'primary_metric': 'mean site future-block RMSE; equal weight every retained site', 'metric_kind': 'rmse', 'metric_units': 'g CO2 m^-2 h^-1', 'input_scope': 'finite 5cm temperature [-15,50] degC; moisture missing or [0,100] native SWC percent; finite flux, negative and large values retained', 'forbidden_inputs': ['slope', 'intc', 'ci', 'chamber area/volume conversion', 'future flux', 'future fitted context offsets'], 'baseline_families': ['calibrated context mean', 'Q10 with calibrated context offsets', 'Lloyd-Taylor', 'constrained RBF ridge'], 'selection': 'best development mean-site/fold RMSE; simpler equation if within 1% of best; extension requires >=5% improvement over all baselines and majority reserved sites', 'stopping': '>=5 substantive attempts; stop after two consecutive attempts fail >1% best RMSE improvement or distinct supported explanatory gain', 'author_preprocessing': 'chamber slope conversion/calibration by source authors; no recreation of raw concentration fit', 'scope': 'future measurement dates at these calibrated sites/context categories; no unseen-site, unmeasured treatment causality or annual carbon-budget claim'}
    base = freeze(case, d, protocol)
