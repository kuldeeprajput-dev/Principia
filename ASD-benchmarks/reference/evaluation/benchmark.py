#!/usr/bin/env python3
"""Principia-100 shared evaluator. Score files without executing submitted code."""
from pathlib import Path
import argparse, json, shutil, sys
import numpy as np
import pandas as pd
from common import ROOT,VERSION,context,registry,load_json,save_json,digest,table,new_output,verify_assets,safe_path,evaluator_identity
import metrics,submissions,workflow,scientific

def evaluate(identifier,folder,output,thresholds=None,trusted=False,timeout=120,_context=None,_validated=None,_diagnostic_inputs=None,_route=None):
 identity=evaluator_identity()
 task,package,x,y,refs=_context if _context is not None else context(identifier)
 s,pred,audit=_validated if _validated is not None else submissions.validate(folder,task,x)
 physical_units='probability' if task['metric_kind']=='brier' else task['error_units']
 out=new_output(output);mask=pred.status.eq('predict').to_numpy()&np.isfinite(y.target.to_numpy(float));eligible=np.isfinite(y.target.to_numpy(float));cohort=y.loc[mask].copy();v=pred.loc[mask,'prediction'].to_numpy(float)
 scores={};groups=[]
 for name,values in [('candidate',v)]+[(m,refs.loc[mask,m].to_numpy(float))for m in task['baseline_models']]:
  val,by=metrics.score(cohort,values,task);scores[name]=val;groups.extend(dict(model=name,**r)for r in by)
 full_baselines={m:metrics.score(y.loc[eligible],refs.loc[eligible,m].to_numpy(float),task)[0]for m in task['baseline_models']}
 scale=min(z['group_balanced_mae']for z in full_baselines.values()if z is not None)
 if scores['candidate']:
  candidate=scores['candidate'];candidate['matched_baseline_skill']={m:(1-candidate['primary_error']/z['primary_error'])if candidate['primary_error']is not None and z is not None and z['primary_error']not in[None,0]else None for m,z in scores.items()if m!='candidate'}
  candidate['normalized_mae_to_exposed_reference_scale']=candidate['group_balanced_mae']/scale if scale else None
  w=metrics.weights(cohort,task);ae=abs(v-cohort.target.to_numpy(float))
  candidate['tolerance_accuracy']=[{'absolute_tolerance':mult*scale,'units':physical_units,'weighted_fraction':float(w@(ae<=mult*scale)),'interpretation':'Exposed-reference diagnostic; not an operational acceptance limit'}for mult in[.5,1.,2.]]
 intervals=metrics.interval_metrics(cohort,v,pred.loc[mask,'lower'].to_numpy(float),pred.loc[mask,'upper'].to_numpy(float),s['uncertainty']['interval_level'],task)if len(cohort)and'lower'in pred else None
 events=[metrics.event_metrics(cohort,v,task,t)for t in(thresholds or[])]if len(cohort)else[]
 replay=submissions.replay(folder,s,pred,task,x,timeout)if trusted else{'status':'not_run','execution_mode':'prediction_files_only'}
 eligible_weights=metrics.weights(y.loc[eligible],task)
 quality_path=ROOT/'quality/ELIGIBILITY.json';quality=load_json(quality_path)
 quality_id=(_route or {}).get('parent_task_id',task['task_id'])
 qualification=next((q for q in quality['tasks']if q['task_id']==quality_id),{'task_id':quality_id,'tier':'pending_eligibility_refresh'})
 report={
 'schema_version':'principia.report/3.0','evaluator_version':VERSION,'evaluator_identity':identity,'physical_error_units':physical_units,
 'contract_notice':next((e.get('contract_notice') for e in registry()['tasks'] if e['task_id']==task['task_id']),None),
 'additive_extensions':{'weighting':'asd7-weighted/1.0' if task['aggregation'].get('within_group_weight') else None,'probability':'asd6-probability/1.1' if task['metric_kind']=='brier' else None,'endpoint_diagnostics':task.get('scientific_evaluator_extension')},
 'identity':{k:task[k]for k in['case_id','task_id','protocol_version','cohort_id']},'evaluation_route':_route or {'mode':'prepared_features'},
 'reference_baseline':load_json(ROOT/'BASELINE.json'),'benchmark_eligibility':qualification,'eligibility_registry_sha256':digest(quality_path),
 'submission_assessment':{'numerical_format':'validated','information_access':audit.get('raw_information_compliance','declared_not_proven_by_prediction_scoring'),'scientific_reference_admission':'not_assessed','task_tier_is_not_submission_admission':True,'current_outcomes_exposed':True},
 'bindings':{'task_sha256':digest(package/'task.json'),'manifest_sha256':digest(package/'MANIFEST.json'),'input_sha256':task['input_sha256'],'observations_sha256':task['observations_sha256'],'submission_sha256':digest(Path(folder)/'submission.json'),'predictions_sha256':digest(Path(folder)/s['predictions_file'])},
 'coverage':{'assigned_rows':len(y),'eligible_target_rows':int(eligible.sum()),'predicted_rows':int(pred.status.eq('predict').sum()),'scored_rows':int(mask.sum()),'abstained_rows':int(pred.status.eq('abstain').sum()),'eligible_group_weighted_coverage':float(eligible_weights@mask[eligible])if eligible.any()else None,'full_eligible_cohort':bool(np.array_equal(mask,eligible))},
 'scores':scores,'groups':groups,'uncertainty':intervals,'events':events,'training_audit':audit,'replay':replay,
 'normalization':{'physical_mae_scale':scale,'units':physical_units,'source':'Best frozen comparator on exposed full cohort; diagnostic only'},
 'scientific_status':{'current_outcomes_exposed':True,'fresh_confirmation':False,'automatic_admission':False,'novelty':'not_assessed','industrial_intervention_impact':'not_assessed','review_required':True},
 'scientific_checks':scientific.checks(task,cohort,v,(_diagnostic_inputs if _diagnostic_inputs is not None else x).loc[mask].copy(),full_inputs=_diagnostic_inputs if _diagnostic_inputs is not None else x,full_observations=y),
 'metric_corrections':['F1=2TP/(2TP+FP+FN); zero for complete nonempty failure, undefined only when denominator is zero.','Evaluator3.1: case44 decision coverage uses the full cohort inventory. Probability absolute-error diagnostics use probability units, while Brier primary error remains squared probability. Historical primary-error arithmetic is unchanged.'],
 }
 out.mkdir(parents=True);save_json(out/'report.json',report);pd.DataFrame(groups).to_csv(out/'by_group.csv',index=False)
 text=f"# {task['task_id']}: numerical evaluation\n\nScored {int(mask.sum())} / {int(eligible.sum())} eligible rows. All current outcomes are exposed. Comparators use identical covered observations.\n\n| Model | Primary error ({task['primary_units']}) | Physical MAE ({physical_units}) |\n|---|---:|---:|\n"
 for name,val in scores.items():text+=f"| {name} | {val['primary_error'] if val else 'undefined'} | {val['group_balanced_mae'] if val else 'undefined'} |\n"
 text+='\nNumerical quality does not certify a mechanism, novelty or industrial impact. See structured scientific review. Training independence is not established by scoring alone.\n'
 if report['contract_notice']:text+='\n**Contract correction.** '+report['contract_notice']+'\n'
 if audit.get('comparability')=='numerical_only_unverified_information_access':text+='\nThis historical prediction import has unknown input-access and training provenance. Its comparisons are numerical only, not verified protocol-compliant scientific claims.\n'
 (out/'REPORT.md').write_text(text);return report

def verify(identifier=None):
 identity=evaluator_identity()
 tasks=[context(identifier)[0]]if identifier else registry()['tasks'];rows=[]
 for entry in tasks:
  task,package,x,y,refs=context(entry['task_id']);expected=table(package/'evidence/metrics.csv').set_index('model');valid=np.isfinite(y.target.to_numpy(float))
  for model in task['baseline_models']:
   result,_=metrics.score(y.loc[valid],refs.loc[valid,model].to_numpy(float),task)
   old=float(expected.loc[model,'primary_error']);new=result['primary_error']
   if new is None or not np.isclose(old,new,rtol=1e-9,atol=1e-10):raise ValueError(f'Historical metric mismatch: {task["task_id"]}/{model}: {old} versus {new}')
  rows.append({'task_id':task['task_id'],'models':len(task['baseline_models']),'rows':len(x),'status':'pass'})
 return{'status':'pass','evaluator_version':VERSION,'evaluator_identity':identity,'tasks':len(rows),'models':sum(x['models']for x in rows),'checks':rows}

def export(output):
 out=new_output(output);allow=load_json(ROOT/'RELEASE_ALLOWLIST.json');verify_assets(ROOT,allow['files']);out.mkdir(parents=True)
 for a in allow['files']:
  p=safe_path(ROOT,a['path']);name=a.get('export_path',a['path']);rel=Path(name)
  if rel.is_absolute()or'..'in rel.parts:raise ValueError('Unsafe export destination')
  dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 projected=[{'path':a.get('export_path',a['path']),'sha256':a['sha256'],'bytes':a['bytes']}for a in allow['files']]
 save_json(out/'RELEASE_ALLOWLIST.json',{'schema_version':'principia.release-allowlist/1.0','version':allow.get('version',VERSION),'files':projected,'exclusions':allow.get('exclusions',[]),'publication_performed':False})
 save_json(out/'RELEASE_MANIFEST.json',{'schema_version':'principia.release/1.0','version':allow.get('version',VERSION),'status':'local_public_ready_projection','files':len(projected),'stored_bytes':sum(a['bytes']for a in projected),'registry_sha256':digest(out/'registry.json'),'allowlist_sha256':digest(out/'RELEASE_ALLOWLIST.json'),'exclusions':allow.get('exclusions',[]),'publication_performed':False})
 save_json(out/'EXPORT_RECEIPT.json',{'status':'local_export','source_allowlist_sha256':digest(ROOT/'RELEASE_ALLOWLIST.json'),'files':len(allow['files']),'publication_performed':False,'exclusions':allow.get('exclusions',[])})
 return{'status':'local_export','files':len(allow['files'])}

def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
 a=sub.add_parser('list');a.add_argument('--all-cases',action='store_true')
 for cmd in['example','validate','score','replay','prepare','verify']:
  a=sub.add_parser(cmd);a.add_argument('--task',required=cmd!='verify');a.add_argument('--output',type=Path,required=cmd in['example','score','replay','prepare']);
  if cmd in['score','replay','validate']:a.add_argument('--submission',type=Path,required=True)
  if cmd in['score','replay']:a.add_argument('--trust-code',action='store_true');a.add_argument('--timeout',type=int,default=120);a.add_argument('--event-threshold',type=float,action='append')
  if cmd=='example':a.add_argument('--model')
  if cmd=='prepare':a.add_argument('--data-root',type=Path,required=True);a.add_argument('--supplemental-root',type=Path);a.add_argument('--trust-code',action='store_true')
 a=sub.add_parser('assess');a.add_argument('--case',required=True);a.add_argument('--data-root',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
 a=sub.add_parser('propose-task');a.add_argument('--proposal',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
 a=sub.add_parser('review');a.add_argument('action',choices=['prepare','combine','adjudicate']);a.add_argument('--claims',type=Path);a.add_argument('--packet',type=Path);a.add_argument('--reviews',nargs='+',type=Path);a.add_argument('--combined',type=Path);a.add_argument('--decision',type=Path);a.add_argument('--output',type=Path,required=True)
 a=sub.add_parser('export');a.add_argument('--output',type=Path,required=True)
 for cmd in ['raw-example','raw-validate','raw-score','raw-replay']:
  a=sub.add_parser(cmd);a.add_argument('--contract',required=True)
  if cmd!='raw-example':a.add_argument('--submission',type=Path,required=True)
  if cmd!='raw-validate':a.add_argument('--output',type=Path,required=True)
  if cmd in ['raw-score','raw-replay']:a.add_argument('--trust-code',action='store_true')
  if cmd=='raw-replay':a.add_argument('--data-root',type=Path,required=True)
 a=sub.add_parser('validate-task');a.add_argument('--package',type=Path,required=True);a.add_argument('--data-root',type=Path,required=True);a.add_argument('--output',type=Path,required=True);a.add_argument('--trust-code',action='store_true')
 a=sub.add_parser('admit-task');a.add_argument('--proposal',type=Path,required=True);a.add_argument('--package',type=Path,required=True);a.add_argument('--validation',type=Path,required=True);a.add_argument('--reviews',type=Path,nargs=2,required=True);a.add_argument('--decision',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
 a=sub.add_parser('register-task');a.add_argument('--admission',type=Path,required=True);a.add_argument('--maintainer-id',required=True);a.add_argument('--output',type=Path,required=True)
 a=p.parse_args()
 if a.command=='list':
  rows=registry()['cases']if a.all_cases else registry()['tasks']
  for r in rows:print(r.get('task_id',r['case_id']),r.get('status',r.get('target')),r.get('source_scope',''))
  return
 if a.command.startswith('raw-'):
  import raw_access
  if a.command=='raw-example':result=raw_access.example(a.contract,a.output)
  elif a.command=='raw-score':result=raw_access.score(a.contract,a.submission,a.output,a.trust_code)
  elif a.command=='raw-replay':result=raw_access.replay_features(a.contract,a.submission,a.data_root,a.output,a.trust_code)
  else:
   identity=evaluator_identity();_,_,(_,_,audit),_=raw_access.validate(a.contract,a.submission);result=dict(status='valid',evaluator_identity=identity,**audit)
 elif a.command in ['validate-task','admit-task','register-task']:
  import admission
  if a.command=='validate-task':result=admission.validate_adapter(a.package,a.data_root,a.output,a.trust_code)
  elif a.command=='admit-task':result=admission.admit(a.proposal,a.package,a.validation,a.reviews,a.decision,a.output)
  else:result=admission.register(a.admission,a.maintainer_id,a.output)
 elif a.command=='verify':result=verify(a.task)
 elif a.command=='export':result=export(a.output)
 elif a.command=='assess':
  from adequacy import assess
  result=assess(a.case,a.data_root,a.output)
 elif a.command=='propose-task':result=workflow.propose(a.proposal,a.output)
 elif a.command=='review':
  if a.action=='adjudicate':
   if not a.combined or not a.decision:raise ValueError('--combined and --decision required')
   from adjudication import adjudicate
   result=adjudicate(a.combined,a.decision,a.output)
  elif a.action=='prepare':
   if not a.claims:raise ValueError('--claims required')
   result=workflow.prepare_review(a.claims,a.output)
  else:
   if not a.packet or not a.reviews:raise ValueError('--packet and --reviews required')
   result=workflow.combine_reviews(a.packet,a.reviews,a.output)
 elif a.command=='prepare':
  task,*_=context(a.task)
  entry=next(t for t in registry()['tasks']if t['task_id']==task['task_id'])
  if entry.get('preparation_mode')=='explicitly_trusted_external_adapter':
   import admission
   result=admission.validate_adapter(ROOT/entry['package'],a.data_root,a.output,a.trust_code,allow_registered=True)
   print(json.dumps(result,indent=2));return
  new_output(a.output)
  # Static scorer/task assets were verified before this curated adapter is imported.
  engine_manifest=ROOT/'EVALUATOR_MANIFEST.json'
  if not engine_manifest.exists():raise ValueError('Preparation engine has not been sealed')
  verify_assets(ROOT,load_json(engine_manifest)['files'])
  from preparation import prepare
  result=prepare(task,a.data_root,a.supplemental_root,a.output)
 else:
  task,package,x,y,refs=context(a.task)
  if a.command=='example':result=submissions.example(task,package,x,refs,a.output,a.model)
  elif a.command=='validate':
   identity=evaluator_identity();s,d,result=submissions.validate(a.submission,task,x);result=dict(status='valid',evaluator_identity=identity,**result)
  else:
   if a.command=='replay'and not a.trust_code:raise ValueError('Replay executes local submitted code; explicitly pass --trust-code')
   result=evaluate(a.task,a.submission,a.output,a.event_threshold,a.trust_code,a.timeout)
 print(json.dumps({'status':result.get('status','complete'),'command':a.command,'task':getattr(a,'task',None),'output':str(a.output)if getattr(a,'output',None)else None,'tasks':result.get('tasks'),'models':result.get('models')},allow_nan=False))
 if a.command=='verify'and a.output:save_json(a.output,result)

if __name__=='__main__':
 try:main()
 except (ValueError,KeyError,TypeError,OSError)as e:raise SystemExit('ERROR: '+str(e))
