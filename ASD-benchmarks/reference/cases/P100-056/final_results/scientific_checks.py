"""Physical and information diagnostics for prediction files; no submitted code execution."""
from pathlib import Path
import argparse,json
import numpy as np
import pandas as pd

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--predictions');ap.add_argument('--column',default='reference');ap.add_argument('--output');args=ap.parse_args();root=Path(__file__).resolve().parent
 rules=json.loads((root/'rules.json').read_text());x=pd.read_csv(root/'data/inputs.csv.gz',dtype={'sample_id':str,'group':str});o=pd.read_csv(root/'data/observations.csv.gz',dtype={'sample_id':str,'group':str});q=pd.read_csv(args.predictions or root/'evidence/predictions.csv.gz',dtype={'sample_id':str,'group':str})
 if q.sample_id.duplicated().any() or set(q.sample_id)!=set(x.sample_id):raise ValueError('Prediction IDs must exactly match the registered cohort')
 q=q.set_index('sample_id').loc[x.sample_id];v=pd.to_numeric(q[args.column],errors='coerce').to_numpy(float)
 if not np.isfinite(v).all():raise ValueError('Nonfinite predictions; declare abstentions through the shared evaluator')
 n=int(rules['case_id'].split('-')[-1]);out={'case_id':rules['case_id'],'rows':len(x),'independent_groups':x.group.nunique(),'role':'descriptive diagnostics; no automatic novelty, causal mechanism or industrial acceptance','negative_prediction_count':int(sum(v<0))}
 if n==13:
  out['conversion_above_one_count']=int(sum(v>1));out['source_conversion_above_one_count']=int(sum(o.target>1));out['monotonicity_violations']=[]
  for g in x.group.unique():
   ix=np.flatnonzero(x.group==g);ix=ix[np.argsort(x.temperature_K.to_numpy()[ix],kind='stable')];out['monotonicity_violations'].append({'group':g,'adjacent_decrease_count':int(sum(np.diff(v[ix]) < -1e-9))})
  out['interpretation']='Conversion is a normalized source product; small source values above1 are preserved. Bounds and monotonicity are model properties, not independent validation of two chemical pathways. No conversion history is an input.'
 if n==54:
  valid=(x.width_um>0)&(x.thickness_um>0)&(x.length_um>0)&(x.notch_depth_um>0)&(x.notch_depth_um<x.thickness_um)&(x.notch_width_um>0)&(x.notch_width_um<x.width_um)
  if not valid.all():raise ValueError('Invalid source geometry')
  out['geometry_domain']='All measured geometries positive with0<a<W and0<b<B';out['timing']='SEM dimensions can be post-test observations; submission cannot claim prospective geometry-control or intrinsic toughness from these prediction scores.'
 if n==56:
  if not (x.calibration_deflection_mm<=10).all() or not (x.deflection_mm>10).all():raise ValueError('Invalid calibration/target time boundary')
  out['calibration_domain']='Complete initial prefix≤10mm; all scored deflections>10mm; source anchors enumerate calibration.';out['mechanical_limit']='Do not impose global monotonicity: source late force drops are retained. A fitted force cap is not a structural safety limit.'
 text=json.dumps(out,indent=2,allow_nan=False)
 if args.output:Path(args.output).write_text(text)
 print(text)
if __name__=='__main__':main()
