from pathlib import Path
import json,hashlib,zipfile,io,gzip
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def hashgroup(s):return int(hashlib.sha256(('principia100-batch7:'+str(s)).encode()).hexdigest()[:16],16)
def verify(data_root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in m['assets']:
  f=Path(data_root)/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native SHA256 mismatch: '+a['path'])
 return Path(data_root)/m['folder']
import re
def prepare(data_root):
 root=verify(data_root);f=root/'raw/published_results.zip';rows=[]
 with zipfile.ZipFile(f) as z:
  def read(sdk):return json.loads(z.read('published_results/transpilation/'+sdk+'_device.json'))
  qp=read('qiskit');pilot={b['params']['filename']:b for b in qp['benchmarks'] if 'filename' in (b.get('params') or {})};families={fn:re.sub(r'[_-]?\d+','',Path(fn).stem).lower() for fn in pilot};groups=sorted(set(families.values()),key=lambda s:hashgroup('compiler-family:'+s));exposed={'mod','tof','rc_adder','adder','qpt','partial_tof'};available=[g for g in groups if g not in exposed];held=set(available[:max(1,len(groups)//5)])
  for sdk in ['tket','bqskit','staq']:
   source=read(sdk)
   if source['machine_info']['cpu']['brand_raw']!=qp['machine_info']['cpu']['brand_raw']:raise ValueError('Machine CPU mismatch')
   for idx,b in enumerate(source['benchmarks']):
    if 'filename' not in (b.get('params') or {}):continue
    fn=b['params']['filename']
    if fn not in pilot:continue
    p=pilot[fn];e=p['extra_info'];vals=[p['stats']['mean'],b['stats']['mean'],e.get('input_num_qubits'),e.get('output_gate_count_2q'),e.get('output_depth_2q'),e.get('qasm_load_time')]
    if not all(v is not None and np.isfinite(v) for v in vals) or min(vals[:3])<=0 or min(vals[3:])<0:continue
    fam=families[fn];rows.append(dict(sample_id=sdk+':'+fn,group=fam,target=float(b['stats']['mean']),partition='confirmation' if fam in held else 'development',fold_key=hashgroup('compiler-fold:'+fam)%5,pilot_seconds=float(p['stats']['mean']),qubits=float(e['input_num_qubits']),pilot_gates=float(e['output_gate_count_2q']),pilot_depth=float(e['output_depth_2q']),load_seconds=float(e['qasm_load_time']),is_tket=float(sdk=='tket'),is_bqskit=float(sdk=='bqskit'),source_anchor=f.name+'!published_results/transpilation/'+sdk+'_device.json:benchmarks['+str(idx)+'].stats.mean',input_anchor='qiskit_device.json filename='+fn+'; pilot runtime/output/calibration',eligibility_reason='Matched Qiskit pilot and successful finitepositive SDK timing; absent/failure results not silently imputed'))
 return pd.DataFrame(rows)
