"""Strict static contracts for Principia-100. This module executes no task code."""
from pathlib import Path
import csv, gzip, hashlib, json
import numpy as np
import pandas as pd
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent.parent
VERSION='3.1.0-rc.1'
COMPATIBLE_SUBMISSION_VERSIONS={VERSION,'3.0.0-rc.1'}

def evaluator_identity(root=None):
 """Verify the installed engine, and bind the actual numerical environment.

 This detects local drift against the installed manifest, not malicious replacement
 of both manifest and implementation. Release authenticity needs its release hash.
 """
 import importlib.metadata,platform,sys
 root=Path(root) if root is not None else ROOT
 manifest=safe_path(root,'EVALUATOR_MANIFEST.json');record=load_json(manifest)
 assets=record.get('files')
 if not isinstance(assets,list) or not assets:raise ValueError('Empty evaluator manifest')
 required={'evaluation/benchmark.py','evaluation/metrics.py','evaluation/common.py','evaluation/submissions.py','evaluation/requirements.lock.txt'}
 if not required.issubset({a['path'] for a in assets}):raise ValueError('Incomplete evaluator manifest')
 verify_assets(root,assets)
 lock=safe_path(root,'evaluation/requirements.lock.txt')
 packages={}
 for line in lock.read_text().splitlines():
  if not line or line.startswith('#'):continue
  name,expected=line.split('==',1)
  try:actual=importlib.metadata.version(name)
  except importlib.metadata.PackageNotFoundError:actual=None
  packages[name]={'expected':expected,'actual':actual}
 mismatches={k:v for k,v in packages.items() if v['expected']!=v['actual']}
 runtime={'python':platform.python_version(),'implementation':sys.implementation.name,'platform':platform.system(),'machine':platform.machine(),'packages':packages}
 return {'evaluator_version':VERSION,'manifest_sha256':digest(manifest),'dependency_lock_sha256':digest(lock),'runtime':runtime,'runtime_sha256':hashlib.sha256(json.dumps(runtime,sort_keys=True).encode()).hexdigest(),'environment_matches_lock':not mismatches,'dependency_mismatches':mismatches,'integrity':'verified_against_installed_manifest'}

def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()

def load_json(path):
 def pairs(xs):
  d={}
  for k,v in xs:
   if k in d:raise ValueError('Duplicate JSON key: '+k)
   d[k]=v
  return d
 def invalid(x):raise ValueError('Nonfinite JSON value: '+x)
 def number(s):
  x=float(s)
  if not np.isfinite(x):invalid(s)
  return x
 return json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_constant=invalid,parse_float=number)

def save_json(path,obj):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')

def safe_path(root,name):
 root=Path(root).resolve();p=Path(name)
 if not str(name)or p.is_absolute()or '..'in p.parts:raise ValueError('Unsafe relative path: '+str(name))
 if any((root/Path(*p.parts[:i])).is_symlink()for i in range(1,len(p.parts)+1)):raise ValueError('Symlink asset rejected: '+str(name))
 q=root/p
 if not q.is_file()or not q.resolve().is_relative_to(root):raise ValueError('Missing or escaping asset: '+str(name))
 return q

def verify_assets(root,assets):
 seen=set()
 for item in assets:
  name=item['path']
  if name in seen:raise ValueError('Duplicate asset: '+name)
  seen.add(name);p=safe_path(root,name)
  if ('bytes'in item and p.stat().st_size!=item['bytes'])or digest(p)!=item['sha256']:raise ValueError('Asset integrity mismatch: '+name)
 return len(seen)

def table(path,strings=False):
 p=Path(path);opener=gzip.open if p.suffix=='.gz'else open
 with opener(p,'rt',newline='')as f:header=next(csv.reader(f),[])
 if not header or len(header)!=len(set(header)):raise ValueError('Empty or duplicate table header')
 if strings:return pd.read_csv(p,dtype=str,keep_default_na=False)
 return pd.read_csv(p,float_precision='round_trip',dtype={k:str for k in ['sample_id','group','fold','particle','port','router','family','trial','condition','site','workpiece_id','run_id']})

def new_output(path):
 p=Path(path)
 if p.exists():raise ValueError('Choose a new output path: '+str(p))
 return p

def registry():return load_json(ROOT/'registry.json')

def validate_schema(value,name):
 schema=load_json(ROOT/'schemas'/name)
 errors=list(Draft202012Validator(schema).iter_errors(value))
 if errors:
  e=errors[0];raise ValueError(name+' at '+'.'.join(map(str,e.absolute_path))+': '+e.message)

def context(identifier):
 reg=registry();found=[x for x in reg['tasks']if x['task_id']==identifier]
 if not found:
  cases=[x for x in reg['cases']if x['case_id']==identifier or x['case_id'].split('-')[-1].lstrip('0')==str(identifier).lstrip('0')]
  if len(cases)!=1 or not cases[0]['default_task']:raise ValueError('Unknown task or scenario without an evaluator')
  found=[x for x in reg['tasks']if x['task_id']==cases[0]['default_task']]
 if len(found)!=1:raise ValueError('Ambiguous task')
 entry=found[0];package=ROOT/entry['package']
 if 'manifest_sha256'in entry and digest(package/'MANIFEST.json')!=entry['manifest_sha256']:raise ValueError('Registered package manifest mismatch')
 verify_assets(package,load_json(package/'MANIFEST.json')['files'])
 task=load_json(package/'task.json')
 for k in ['task_id','case_id','protocol_version','cohort_id','input_sha256','observations_sha256']:
  if task[k]!=entry[k]:raise ValueError('Registry/task mismatch: '+k)
 x=table(package/task['data']['inputs']);y=table(package/task['data']['observations']);refs=table(package/task['data']['reference_predictions'])
 for d in[x,y,refs]:
  if d.sample_id.isna().any()or not d.sample_id.is_unique or d.group.isna().any():raise ValueError('Invalid authoritative identities')
  if not d[['sample_id','group']].equals(x[['sample_id','group']]):raise ValueError('Authoritative identity alignment mismatch')
 if len(x)!=task['assigned_rows']or sorted(y.group.unique().tolist())!=task['evaluation_groups']:raise ValueError('Task cohort mismatch')
 if digest(package/task['data']['inputs'])!=task['input_sha256']or digest(package/task['data']['observations'])!=task['observations_sha256']:raise ValueError('Authoritative input/target binding mismatch')
 if np.isinf(y.target.to_numpy(float)).any():raise ValueError('Infinite authoritative target')
 if not set(task['baseline_models']).issubset(refs.columns):raise ValueError('Missing reference predictions')
 return task,package,x,y,refs

def asset_record(path,root):
 p=Path(path);return{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':digest(p)}

def seal_package(path):
 p=Path(path)
 assets=[asset_record(f,p)for f in sorted(p.rglob('*'))if f.is_file()and f.name!='MANIFEST.json'and '__pycache__'not in f.parts]
 save_json(p/'MANIFEST.json',{'schema_version':'principia.assets/1.0','files':assets})
