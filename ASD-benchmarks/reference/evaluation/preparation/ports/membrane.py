"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

MEMBRANES = ['S-PdAg-YSZ/Al2O3', 'S-PdAg-HT', 'S-Pd', 'S-PdAg']
L = [189.0, 189.0, 136.0, 141.0]
D = [14.0, 14.0, 10.0, 10.0]

def prepare():
    if False:
        raise RuntimeError('Refusing to overwrite frozen protocol')

    rows = []
    name = 'DataPalladiumBasedMembranes.xlsx'
    w = openpyxl.load_workbook(SOURCE / 'raw' / name, data_only=True)
    for sheet, starts in [('Pure H2 tests', [1, 6, 11, 16]), ('Mixture tests', [2, 10, 18, 26])]:
        for m, a in enumerate(starts):
            for rn, row in enumerate(list(w[sheet].values)[7:], 8):
                end = a + 3 if sheet == 'Pure H2 tests' else a + 6
                if not isinstance(row[end], (float, int)):
                    continue
                if sheet == 'Pure H2 tests':
                    t, pp, pr, j = row[a:end + 1]
                    gas = 'H2'
                    x = 1.0
                    f = 0.0
                    kind = 'pure'
                else:
                    gas, t, x, f, pp, pr, j = row[a:end + 1]
                    kind = 'mixture'
                assert 0 < x <= 1 and pr > pp and (300 < t < 500)
                sid = f'P100-061-{kind}-m{m + 1}-r{rn:03}'
                part = 'confirmation' if t == 400 else 'development'
                group = f'{gas}-T{int(t)}'
                rows.append(dict(sample_id=sid, group=group, membrane=MEMBRANES[m], membrane_index=m, kind=kind, gas=gas, temperature_C=float(t), temperature_K=t + 273.15, feed_fraction=float(x), normal_flow_L_min=float(f), permeate_bar=float(pp), retentate_bar=float(pr), length_m=L[m] / 1000, diameter_m=D[m] / 1000, area_m2=np.pi * L[m] * D[m] / 1000000.0, partition=part, target=float(j), source_file=name, source_sheet=sheet, source_row=rn, source_target_cell=f'{openpyxl.utils.get_column_letter(end + 1)}{rn}'))
    df = pd.DataFrame(rows)
    return df
