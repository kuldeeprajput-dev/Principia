"""Endpoint diagnostics remain descriptive and preserve abstention semantics."""
from pathlib import Path
import argparse,tempfile,sys,json
import numpy as np,pandas as pd
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'evaluation'));import scientific,common
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();W=a.output or Path(tempfile.mkdtemp(prefix='principia-endpoint-tests-'));W.mkdir(parents=True,exist_ok=True)
checks=[]
def check(name,case,pred,kind='mae',family='original',expect=None,target=None):
 task={'case_number':case,'case_id':f'P100-{case:03d}','metric_kind':kind,'family':family};y=pd.DataFrame({'target':pred if target is None else target});result=scientific.checks(task,y,np.asarray(pred,float));good=expect(result)
 checks.append({'check':name,'status':'pass'if good else'fail','result':result})
check('void_fraction_domain',27,[-.1,0.,.5,1.,1.1],expect=lambda r:r['deterministic_checks'][0]['violations']==2)
check('percentage_target_upper_limit',72,[0.,50.,100.,110.],expect=lambda r:r['deterministic_checks'][0]['violations']==1)
check('residual_sugar_not_percentage',72,[0.,50.,100.,110.],family='round2',expect=lambda r:r['deterministic_checks'][0]['violations']==0 and r['deterministic_checks'][0]['upper']is None)
check('signed_temperature_above_absolute_zero',69,[-273.15,-20.,0.,100.],expect=lambda r:r['deterministic_checks'][0]['violations']==0)
check('no_observations_is_not_tested',27,[],expect=lambda r:r['deterministic_checks'][0]['status']=='not_tested_no_scored_rows')
check('rheology_nonpositive_targets_disclosed',58,[1.,2.,3.],kind='log_mae',target=[-1.,0.,3.],expect=lambda r:r['deterministic_checks'][0]['nonpositive_target_rows']==2)
check('pv_energy_semantics',59,[0.,1.],expect=lambda r:'energy'in r['deterministic_checks'][0]['interpretation'].lower())
check('radio_signed_values_allowed',92,[-90.,-40.],expect=lambda r:not r['deterministic_checks'])
result={'status':'pass'if all(x['status']=='pass'for x in checks)else'fail','checks':checks,'source_sha256':common.digest(R/'evaluation/scientific.py')};common.save_json(W/'SCIENTIFIC_ENDPOINT_QA.json',result);print(json.dumps({'status':result['status'],'checks':len(checks)},indent=2));raise SystemExit(0 if result['status']=='pass'else 1)
