"""Verify native reconstruction against frozen benchmark values; never fit a model.

The comparison deliberately reads frozen task tables as expected outputs only.
Preparation itself consumes native source assets plus declared metadata/state.
"""
from pathlib import Path
import argparse,json,tempfile,traceback
import numpy as np,pandas as pd
from . import prepare,_sha

def main():
 a=argparse.ArgumentParser();a.add_argument('--benchmark',required=True,type=Path);a.add_argument('--data-root',required=True,type=Path);a.add_argument('--supplemental-58',type=Path);a.add_argument('--supplemental-96',type=Path);a.add_argument('--task',action='append');a.add_argument('--report',required=True,type=Path);args=a.parse_args();reg=json.loads((args.benchmark/'registry.json').read_text());results=[]
 # Cache only this process's freshly parsed native measurements for repeated tasks.
 import preparation as core
 original_base=core.base_table;cache={}
 def cached(case,data_root):
  if case not in cache:cache.clear();cache[case]=original_base(case,data_root)
  return cache[case].copy()
 core.base_table=cached
 for task in sorted(reg['tasks'],key=lambda t:t['case_number']):
  if args.task and task['task_id'] not in args.task:continue
  tid=task['task_id'];print('Reconstructing',tid,flush=True)
  try:
   supplement=args.supplemental_58 if task['family']=='supplemental' else args.supplemental_96 if task['case_number']==96 and task['family']=='continuation' else None
   with tempfile.TemporaryDirectory(prefix='principia-native-') as tmp:
    receipt=prepare(task,args.data_root,supplement,tmp);comparisons=[]
    for name in ['inputs','observations']:
     expected_path=args.benchmark/task['package']/f'data/{name}.csv.gz';expected=pd.read_csv(expected_path,dtype={'sample_id':str,'group':str},float_precision='round_trip');actual=pd.read_csv(Path(tmp)/f'data/{name}.csv.gz',dtype={'sample_id':str,'group':str},float_precision='round_trip');assert list(expected)==list(actual),f'{name} column mismatch';assert len(expected)==len(actual),f'{name} row mismatch'
     for c in expected:
      if pd.api.types.is_bool_dtype(expected[c]) or pd.api.types.is_bool_dtype(actual[c]):
       assert pd.api.types.is_bool_dtype(expected[c]) and pd.api.types.is_bool_dtype(actual[c]),f'{name}:{c} Boolean dtype mismatch'
       assert expected[c].equals(actual[c]),f'{name}:{c} Boolean mismatch'
       comparisons.append({'table':name,'column':c,'kind':'boolean','status':'pass'})
      elif pd.api.types.is_numeric_dtype(expected[c]) and pd.api.types.is_numeric_dtype(actual[c]):
       equal=np.allclose(expected[c],actual[c],equal_nan=True,rtol=1e-11,atol=1e-11);mask=np.isfinite(expected[c])&np.isfinite(actual[c]);maxdiff=float(abs(expected.loc[mask,c]-actual.loc[mask,c]).max()) if mask.any() else 0.;assert equal,f'{name}:{c} numerical mismatch max abs{maxdiff}';comparisons.append({'table':name,'column':c,'kind':'numeric','max_abs_difference':maxdiff,'status':'pass'})
      else:
       assert expected[c].fillna('<NA>').astype(str).equals(actual[c].fillna('<NA>').astype(str)),f'{name}:{c} metadata mismatch';comparisons.append({'table':name,'column':c,'kind':'identifier_or_metadata','status':'pass'})
    results.append({'task_id':tid,'case_id':task['case_id'],'family':task['family'],'supplemental':bool(task.get('supplemental',False)),'status':'pass','rows':receipt['rows'],'native_assets_verified':receipt['native_assets_verified'],'columns_checked':comparisons,'expected_asset_hashes':{name:_sha(args.benchmark/task['package']/f'data/{name}.csv.gz') for name in ['inputs','observations']}})
    print(tid,'PASS',receipt['rows'],flush=True)
  except Exception as e:results.append({'task_id':tid,'status':'fail','error':str(e),'traceback':traceback.format_exc()});print(tid,'FAIL',str(e),flush=True)
  report={'status':'pass' if all(r['status']=='pass' for r in results) else 'fail','tasks_checked':len(results),'passed':sum(r['status']=='pass' for r in results),'tasks':results,'comparison_policy':{'native_identifiers_metadata':'exact','numerical':'float64 rtol1e-11 atol1e-11, equal native missingness','gzip_bytes':'not equated; deterministic17-digit reconstruction and historical formatting may differ'},'fitting_performed':False,'prepared_tables_used_as_runtime_source':False,'expected_tables_used_only_for_QA':True};args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,indent=2)+'\n')
 if report['status']!='pass':raise SystemExit(1)
if __name__=='__main__':main()
