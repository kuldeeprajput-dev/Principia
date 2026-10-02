"""Registered physical/timing diagnostics for arbitrary prediction files; executes no submitted code."""
from pathlib import Path
import argparse,json
import pandas as pd
import numpy as np

def events(actual,pred):
 a=np.asarray(actual,bool);p=np.asarray(pred,bool);tp=int(sum(a&p));fp=int(sum(~a&p));fn=int(sum(a&~p));tn=int(sum(~a&~p));den=2*tp+fp+fn
 return {'TP':tp,'FP':fp,'FN':fn,'TN':tn,'precision':None if tp+fp==0 else tp/(tp+fp),'recall':None if tp+fn==0 else tp/(tp+fn),'specificity':None if tn+fp==0 else tn/(tn+fp),'F1':None if den==0 else 2*tp/den,'F1_undefined_reason':'no observed or predicted positives' if den==0 else None}
def main():
 a=argparse.ArgumentParser();a.add_argument('--predictions');a.add_argument('--column',default='reference');a.add_argument('--output');args=a.parse_args();p=Path(__file__).resolve().parent;r=json.loads((p/'rules.json').read_text());x=pd.read_csv(p/'data/inputs.csv.gz');o=pd.read_csv(p/'data/observations.csv.gz');q=pd.read_csv(args.predictions or p/'evidence/predictions.csv.gz');
 if q.sample_id.duplicated().any() or set(q.sample_id)!=set(x.sample_id):raise ValueError('Prediction identities must exactly match cohort')
 q=q.set_index('sample_id').loc[x.sample_id];pred=q[args.column].to_numpy(float)
 if not np.isfinite(pred).all():raise ValueError('Nonfinite predictions; use shared engine for explicit abstention')
 n=int(r['case_id'].split('-')[-1]);out={'case_id':r['case_id'],'rows':len(x),'scope':'exposed-cohort diagnostic; no novelty or impact certification','negative_predictions':int(sum(pred<0))}
 if n==74:
  assert (x.time_min>7.5).all();out['timing_check']='All targets strictly after fixed6-minute calibration; early3,4.5,6-minute anchors stored in observations.';out['kinetic_identifiability']='Fluorescence values are not unique calibrated kinase concentrations; no mechanistic pass/fail inferred from MAE.'
 if n==85:
  out['stoichiometric_diagnostic']={'predictions_above_complete_oxidation_by_gt_1e_9':int(sum(pred>(76.05/62.07)*np.maximum(x.eg_consumed_g_L.to_numpy(),0)+1e-9)),'meaning':'Only a diagnostic: measurement error and starting/end concentrations prevent an exact hard material balance. No industrial acceptance limit.'};out['information_access']='Current EG and pH are contemporaneous independent assays, not time-forward predictors.'
 if n==87:
  out['above_endowment']=int(sum(pred>x.endowment.to_numpy()+1e-9));z=x.copy();z['target']=o.target.to_numpy();z['prediction']=pred;z['actual_weighted']=z.productivity*z.target;z['pred_weighted']=z.productivity*z.prediction
  counts=z.groupby(['group','round']).size()
  if (counts!=2).any():raise ValueError('Both interacting players required at each scored round')
  z=z.groupby(['group','round']).agg(actual=('actual_weighted','sum'),predicted=('pred_weighted','sum'),threshold=('threshold','first'));actual=z.actual>=z.threshold-1e-9;pp=z.predicted>=z.threshold-1e-9;out['coordination_success']=events(actual,pp);out['coordination_threshold_provenance']='Source study Fig1: theta=(p1*e1+p2*e2)/2; aggregate two submitted individual forecasts before classifying. Threshold derives from game rules, not tuned labels.';out['independent_pairs']=x.group.nunique();out['event_aggregation']='Pair-round confusion counts; dependent rounds are descriptive counts, not independent experimental replicates.'
 s=json.dumps(out,indent=2,allow_nan=False)
 if args.output:Path(args.output).write_text(s)
 print(s)
if __name__=='__main__':main()
