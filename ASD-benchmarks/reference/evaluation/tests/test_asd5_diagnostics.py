"""Adverse fixtures for source-defined ASD5 diagnostics, without scientific fitting."""
from pathlib import Path
import sys,json,argparse
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import batch5_checks as b
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();rows=[]
def check(name,func):
 try:assert func();rows.append({'check':name,'status':'pass'})
 except Exception as e:rows.append({'check':name,'status':'fail','error':repr(e)})
t={'case_number':87,'eligible_rows':2};x=pd.DataFrame({'group':['p','p'],'round':[3,3],'endowment':[10,10],'productivity':[1,1],'threshold':[10,10]});y=pd.DataFrame({'target':[6,6]})
check('complete_failure_F1_zero',lambda:b.checks(t,y,[0,0],x)['coordination_success']['F1']==0)
check('both_players_aggregate_before_event',lambda:b.checks(t,y,[6,6],x)['coordination_success']['TP']==1)
check('partial_pair_abstention_has_zero_event_coverage',lambda:b.checks(t,y.iloc[:1],[6],x.iloc[:1])['coordination_success']['coverage']==0)
check('no_events_F1_undefined_reason',lambda:b.checks(t,y.assign(target=0),[0,0],x)['coordination_success']['F1_undefined_reason']is not None)
check('out_of_budget_diagnostic',lambda:b.checks(t,y,[11,-1],x)['outside_contribution_budget']==2)
check('precision_and_specificity_both_reported',lambda:set(['precision','recall','specificity','F1'])<=set(b.checks(t,y,[6,6],x)['coordination_success']))
check('conversion_bounds',lambda:b.checks({'case_number':13},y,[-.2,1.2],x)['above_complete_conversion']==1)
check('signed_optical_no_zero_floor',lambda:'below_zero'not in b.checks({'case_number':64},y,[-10,2],x))
xx=pd.DataFrame({'group':['d','d'],'gate_V':[1,2]})
check('FET_monotonic_counterexample',lambda:b.checks({'case_number':51},y,[3,2],xx)['curve_monotonicity']['decreasing_pairs']==1)
xx=pd.DataFrame({'deflection_mm':[11,12],'calibration_deflection_mm':[10,11]})
check('beam_calibration_boundary',lambda:b.checks({'case_number':56},y,[1,2],xx)['calibration_timing']['calibration_beyond_10mm']==1)
check('biosensor_timing_boundary',lambda:b.checks({'case_number':74},y,[1,2],pd.DataFrame({'time_min':[7.5,9]}))['timing']['targets_at_or_before_7_5min']==1)
check('nonzero_stoichiometric_tolerance_is_diagnostic',lambda:'diagnostic' in b.checks({'case_number':85},y,[2,3],pd.DataFrame({'eg_consumed_g_L':[1,1]}))['stoichiometric_diagnostic']['meaning'].lower() or 'not a hard' in b.checks({'case_number':85},y,[2,3],pd.DataFrame({'eg_consumed_g_L':[1,1]}))['stoichiometric_diagnostic']['meaning'])
def rejects():
 try:b.checks(t,y,[np.inf,0],x)
 except ValueError:return True
 return False
check('nonfinite_rejected',rejects)
result={'status':'pass'if all(z['status']=='pass'for z in rows)else'fail','checks':rows};a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));raise SystemExit(result['status']!='pass')
