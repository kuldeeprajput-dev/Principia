"""Separate confirmation process. This file never calls fit."""
from pathlib import Path
import json,sys,hashlib,datetime,shutil
import numpy as np
import pandas as pd
import native
from run import predict
from develop import metrics,write,SPEC,CASE
H=Path(__file__).resolve().parent

def main():
 if (H/'CONFIRMATION.json').exists():raise ValueError('Confirmation already opened; do not overwrite receipt')
 f=json.loads((H/'FREEZE.json').read_text())
 for a in f['assets']:
  if hashlib.sha256((H/a['path']).read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Frozen artifact changed '+a['path'])
 d=native.prepare(Path(sys.argv[1]));d=d[d.partition=='confirmation'].reset_index(drop=True);b=json.loads((H/'BASELINES.json').read_text());models={k:v['model'] for k,v in b.items()}
 for p in sorted(H.glob('attempts/attempt-*/model.json')):
  k=json.loads((p.parent/'metrics.json').read_text())['model_name'];models[k]=json.loads(p.read_text())
 selected=f['selected'];models={'reference':models[selected],**models};pack=H/'package';(pack/'data').mkdir(parents=True,exist_ok=True);(pack/'evidence').mkdir(exist_ok=True);shutil.copy2(H/'run.py',pack/'run.py');inp=d[['sample_id','group']+SPEC['inputs']].copy();obs=d[['sample_id','group','target','source_anchor','calibration_anchor','linked_unit','source_quality']].copy();inp.to_csv(pack/'data/inputs.csv.gz',index=False,compression={'method':'gzip','mtime':0});obs.to_csv(pack/'data/observations.csv.gz',index=False,compression={'method':'gzip','mtime':0});pred=d[['sample_id','group']].copy();allmetrics={};rows=[];by=[]
 for k,m in models.items():
  y=predict(m,inp)
  if not np.isfinite(y).all():raise ValueError('Nonfinite prediction')
  pred[k]=y;met=metrics(d,y);allmetrics[k]=met;rows.append(dict(model=k,primary_error=met['primary_error'],mean_group_absolute_error=met['mean_group_absolute_error'],groups=met['groups'],scored_rows=len(d),assigned_rows=len(d),primary_units='probability squared' if SPEC['kind']=='brier' else SPEC['unit']))
  by += [dict(model=k,**v) for v in met['by_group']]
 pred.to_csv(pack/'evidence/predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});pd.DataFrame(rows).to_csv(pack/'evidence/metrics.csv',index=False);pd.DataFrame(by).to_csv(pack/'evidence/by_group.csv',index=False);write(pack/'evidence/detailed_metrics.json',allmetrics)
 rules=dict(case_id=f'P100-{CASE:03}',input_columns=SPEC['inputs'],numeric_columns=SPEC['inputs'],input_units=SPEC['input_units'],target=SPEC['target'],target_units=SPEC['unit'],metric_kind=SPEC['kind'],reference_selected_model=selected,models=models)
 write(pack/'rules.json',rules);task=dict(case_id=f'P100-{CASE:03}',target=SPEC['target'],target_units=SPEC['unit'],error_units='probability squared' if SPEC['kind']=='brier' else SPEC['unit'],metric_kind=SPEC['kind'],permitted_inputs=SPEC['inputs'],input_units=SPEC['input_units'],numeric_columns=SPEC['inputs'],timing_contract=SPEC['timing'],calibration=SPEC['calibration'],independent_unit=SPEC['independent_unit'],scope_limits=SPEC['scope'],source_url=SPEC['source_url'],source_license=SPEC['license'],prior_art_url=SPEC['paper'],exposure='Public source-aware corpus; internally reserved confirmation opened only after candidate/selection/stopping freeze. Outcomes now exposed to future users. This is computational confirmation, not independent experimental replication.',uncertainty_policy='Show every group and matched-baseline difference. Few groups/dates do not justify narrow population confidence intervals; no row bootstrap.',applicability=dict(target_min=None if CASE==32 else 0,target_max=1 if SPEC['kind']=='brier' else None),scientific_checks='scientific_checks.py; physical-domain and probability diagnostics, not industrial tolerances')
 write(pack/'task_spec.json',task);receipt=dict(first_confirmation_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),selected_before_confirmation=selected,freeze_sha256=hashlib.sha256((H/'FREEZE.json').read_bytes()).hexdigest(),fitting_during_confirmation=False,groups=sorted(d.group.unique()),rows=len(d),metrics=allmetrics,post_confirmation_revisions_allowed=False);write(H/'CONFIRMATION.json',receipt);write(H/'FINAL_VALIDATION.json',receipt);print(CASE,'CONFIRM',selected,'primary',allmetrics['reference']['primary_error'],'groups',len(d.group.unique()),'rows',len(d));print('baselines',{k:v['primary_error'] for k,v in allmetrics.items() if k.startswith('baseline')})
if __name__=='__main__':main()
