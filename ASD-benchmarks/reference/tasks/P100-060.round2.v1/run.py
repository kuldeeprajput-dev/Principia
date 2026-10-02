"""Frozen portable reference. Explicit OOF and deployment states; no fitting."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys
HERE=Path(__file__).resolve().parent

def _verify():
 manifest=json.loads((HERE/'runtime_manifest.json').read_text())
 for item in manifest['files']:
  p=(HERE/item['path']).resolve()
  if not p.is_relative_to(HERE.resolve()) or not p.is_file():raise ValueError('Missing/unsafe runtime asset')
  if p.stat().st_size!=item['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Runtime asset checksum mismatch: '+item['path'])
 return manifest

def read_table(path):
 import pandas as pd
 return pd.read_csv(path,float_precision='round_trip',dtype={x:str for x in ['sample_id','group','fold','trial','particle','family','run_id','workpiece_id']})

def predict(model,data):
 _verify()
 name='_p100_reference_'+hashlib.sha256(str(HERE).encode()).hexdigest()[:12]
 if name not in sys.modules:
  spec=importlib.util.spec_from_file_location(name,HERE/'reference_runtime/__init__.py',submodule_search_locations=[str(HERE/'reference_runtime')]);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
 runtime=__import__(name+'.runtime',fromlist=['predict'])
 return runtime.predict(model,data)

def load_model(name=None,mode='oof'):
 _verify();rules=json.loads((HERE/'rules.json').read_text());key=name or rules['default_reference'];meta=rules['models'].get(key)
 if meta is None:raise ValueError('Unknown model: '+str(key))
 model=json.loads((HERE/meta['state_file']).read_text());model['mode']=mode;return model

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input','--inputs',dest='input',required=True);ap.add_argument('--output',required=True);ap.add_argument('--model');ap.add_argument('--mode',choices=['oof','deployment'],default='oof');args=ap.parse_args()
 d=read_table(args.input);v=predict(load_model(args.model,args.mode),d);q=d[['sample_id']].copy();q['prediction']=v;q.to_csv(args.output,index=False)
if __name__=='__main__':main()
