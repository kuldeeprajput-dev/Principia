"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

CAL = {'PLA3D850': [110, 120, 130, 140], 'PLA_recycled': [130, 140, 150]}
RESERVED = {'PLA3D850': [150, 160, 170, 180], 'PLA_recycled': [160, 170]}

def read_partition(temps):
    rows = []
    for material, ts in temps.items():
        fn = material + '_DSS_DFS.zip'
        with zipfile.ZipFile(FRESH / fn) as z:
            for name in z.namelist():
                if '/DFS_' not in name or '.RSD' in name:
                    continue
                T = int(re.search('_T(\\d+)_', name)[1])
                if T not in ts:
                    continue
                text = z.read(name).decode('cp1252').replace('\x00', '')
                d = pd.read_csv(io.StringIO(text), sep='\t', skiprows=[1])
                if 'Freq' in d.columns and 'w' not in d.columns:
                    d = d.rename(columns={'Freq': 'w'})
                if not {'w', "G'", 'G"'}.issubset(d.columns):
                    raise ValueError('Predeclared parser schema mismatch, stop before using responses')
                for j, r in d.iterrows():
                    w = float(r['w'])
                    gp = float(r["G'"])
                    gl = float(r['G"'])
                    if not np.isfinite(w) or w <= 0 or (not np.isfinite(gp)):
                        continue
                    rows.append({'sample_id': material + f'-T{T}-row{j + 3}', 'group': f'T{T}', 'material': material, 'temperature_C': T, 'omega': w, 'target': gp, 'loss_modulus': gl, 'anchor': fn + ':' + name + f':row{j + 3}'})
    return pd.DataFrame(rows)
