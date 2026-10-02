"""Adversarial quality gates; all writes are disposable fixtures, never corpus data."""
from pathlib import Path
import sys,copy,json,tempfile,argparse,shutil
import pandas as pd
import numpy as np
B=Path(__file__).resolve().parents[2];sys.path.insert(0,str(B/'evaluation'))
import common,workflow,benchmark,raw_access,admission,adjudication,batch6_checks
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();W=a.output;W.mkdir(parents=True,exist_ok=False)
checks=[]
def check(name,fn,reject=False):
 try:
  result=fn()
 except (ValueError,KeyError,TypeError,AssertionError,OSError)as e:
  checks.append({'test':name,'passed':reject,'detail':str(e)[:250]});return
 checks.append({'test':name,'passed':not reject,'detail':'unexpected acceptance'if reject else'verified'})
def ensure(b,msg='assertion failed'):
 if not b:raise AssertionError(msg)
def write(path,obj):common.save_json(path,obj);return path
# Review contradiction vs complementary scopes.
def judgement(disposition):return {'disposition':disposition,'dimensions':{k:{'status':'not_assessed','rationale':'fixture','evidence_ids':[]}for k in workflow.DIMENSIONS}}
a1=judgement('supported');a2=judgement('unsupported')
check('opposing_dispositions_require_resolution',lambda:ensure(workflow.reconcile(a1,a2)['disagreements']==['disposition']))
a2=judgement('partially_supported');a1['disposition_scope']='computational';a2['disposition_scope']='scientific'
a1['dimensions']['reproducibility'].update(status='supported',scope='computational');a2['dimensions']['reproducibility'].update(status='partially_supported',scope='experimental')
check('complementary_roles_are_not_contradictions',lambda:ensure(not workflow.reconcile(a1,a2)['requires_resolution']))
a2['dimensions']['reproducibility'].update(status='unsupported',scope='computational')
check('same_scope_opposite_evidence_still_conflicts',lambda:ensure('reproducibility'in workflow.reconcile(a1,a2)['disagreements']))
# Actual case44 full inventory and all types of abstention.
t,package,x,y,refs=common.context('P100-044.original.v1');g=x.group.iloc[0]
def decision(mask):return next(z for z in batch6_checks.checks(t,y.loc[mask],refs.loc[mask,t['reference_model']].to_numpy(),x.loc[mask],x,y)['tests']if z['test']=='complete_instance_formulation_selection')
r=decision(x.group.eq(g));check('formulation_1_of_4_coverage',lambda:ensure(r['assigned_instances']==4 and r['complete_instances']==1 and r['decision_coverage']==.25 and r['fully_abstained_instances']==3))
mask=x.group.eq(g);mask.iloc[np.flatnonzero(mask)[0]]=False;r=decision(mask);check('partial_instance_reports_incomplete',lambda:ensure(r['incomplete_instances']==1 and r['complete_instances']==0 and r['decision_coverage']==0))
r=decision(np.zeros(len(x),dtype=bool));check('all_instances_abstain',lambda:ensure(r['fully_abstained_instances']==4 and r['decision_coverage']==0))
# Engine drift can no longer share an identity with the recorded build.
def engine_fixture():
 d=W/'engine';d.mkdir();files=['evaluation/benchmark.py','evaluation/metrics.py','evaluation/common.py','evaluation/submissions.py','evaluation/requirements.lock.txt']
 for s in files:
  f=d/s;f.parent.mkdir(parents=True,exist_ok=True);f.write_text('# test\n')
 write(d/'EVALUATOR_MANIFEST.json',{'files':[common.asset_record(d/s,d)for s in files]});return d
e=engine_fixture();check('sealed_engine_validates',lambda:common.evaluator_identity(e));(e/'evaluation/metrics.py').write_text('# altered arithmetic\n');check('scorer_drift_rejected',lambda:common.evaluator_identity(e),True)
write(e/'EVALUATOR_MANIFEST.json',{'files':[]});check('empty_engine_manifest_rejected',lambda:common.evaluator_identity(e),True)
# Alternative features preserve parent target/cohort, but remain disclosed declarations.
ident='P100-037.original.v1.raw-access.v1';example=W/'raw';raw_access.example(ident,example)
check('alternative_feature_names_allowed',lambda:raw_access.validate(ident,example))
result=raw_access.score(ident,example,W/'raw_score');check('raw_target_binding_unchanged',lambda:ensure(result['bindings']['observations_sha256']==common.context('P100-037.original.v1')[0]['observations_sha256']))
check('raw_information_not_falsely_verified',lambda:ensure(result['training_audit']['raw_information_compliance']=='declared_not_independently_verified'))
base=common.load_json(example/'feature_lineage.json')
def mutation(name,change):
 d=W/name;shutil.copytree(example,d);l=copy.deepcopy(base);change(l,d);write(d/'feature_lineage.json',l);return raw_access.validate(ident,d)
check('future_selector_rejected',lambda:mutation('future',lambda l,d:l['features'][0]['selectors'][0].update(availability='future_response')),True)
check('target_as_predictor_rejected',lambda:mutation('target',lambda l,d:l['features'][0]['selectors'][0].update(role='target')),True)
check('extra_raw_channel_rejected',lambda:mutation('channel',lambda l,d:l['features'][0]['selectors'][0].update(quantity='Power_Consumption')),True)
check('future_numeric_window_rejected',lambda:mutation('window',lambda l,d:l['features'][0]['selectors'][0].update(window_end=2,prediction_time=1)),True)
check('wrong_contract_rejected',lambda:mutation('contract',lambda l,d:l.update(contract_sha256='0'*64)),True)
check('unknown_source_hash_rejected',lambda:mutation('source',lambda l,d:l['features'][0]['selectors'][0].update(asset_sha256='0'*64)),True)
check('corrupt_feature_hash_rejected',lambda:mutation('feature_corrupt',lambda l,d:(d/l['features_file']).write_text('truncated')),True)
def bad_training(l,d):
 q=common.load_json(d/'training.json');q.update(training_group_ids=['modelA_TCP_iteration3.csv'],evaluation_data_usage='never_used_for_fitting_or_tuning')
 q['training_group_ids']=[common.context('P100-037.original.v1')[0]['evaluation_groups'][0]];write(d/'training.json',q)
 for v in l['assets']:
  if v['path']=='training.json':v.update(common.asset_record(d/'training.json',d))
check('extractor_group_leakage_rejected',lambda:mutation('training',bad_training),True)
check('native_replay_requires_trust',lambda:raw_access.replay_features(ident,example,W,W/'untrusted',False),True)
# End-to-end alternative endpoint admission with a tiny synthetic native fixture.
# This never becomes an actual Principia task; registration is to a disposable registry.
fixture=W/'admission_fixture';fixture.mkdir();native=fixture/'native';native.mkdir();pack=fixture/'package';pack.mkdir()
xx=pd.DataFrame({'sample_id':['a','b','c','d'],'group':['g1','g2','g3','g4'],'x':[1.,2.,3.,4.]});yy=xx[['sample_id','group']].copy();yy['target']=[2.,4.,6.,8.]
pd.DataFrame({**{c:xx[c]for c in xx},'target':yy.target}).to_csv(native/'native.csv',index=False)
(pack/'data').mkdir();(pack/'evidence').mkdir();xx.to_csv(pack/'data/inputs.csv.gz',index=False);yy.to_csv(pack/'data/observations.csv.gz',index=False);rr=xx[['sample_id','group']].copy();rr['reference']=5.;rr.to_csv(pack/'evidence/predictions.csv.gz',index=False)
task=copy.deepcopy(common.context('P100-037.original.v1')[0]);task.update(task_id='P100-037.synthetic-validation.v1',protocol_version='fixture-v1',cohort_id='fixture-cohort',target='Synthetic fixture response, not a scientific finding',target_units='fixture units',primary_units='fixture units',error_units='fixture units',permitted_inputs=['x'],input_units={'x':'fixture units'},assigned_rows=4,eligible_rows=4,evaluation_groups=['g1','g2','g3','g4'],baseline_models=['reference'],reference_model='reference',models={'reference':{'equation':'5'}},input_sha256=common.digest(pack/'data/inputs.csv.gz'),observations_sha256=common.digest(pack/'data/observations.csv.gz'),fixture_only=True)
score,_=__import__('metrics').score(yy,rr.reference.to_numpy(),task);pd.DataFrame([{'model':'reference','primary_error':score['primary_error']}]).to_csv(pack/'evidence/metrics.csv',index=False)
write(pack/'task.json',task);write(pack/'rules.json',{'models':{'reference':{'constant':5}}});(pack/'run.py').write_text('import pandas as pd,numpy as np\ndef read_table(path):return pd.read_csv(path,dtype={"sample_id":str,"group":str})\ndef predict(model,x):return np.full(len(x),model["constant"])\n')
(pack/'native.py').write_text('import argparse,pandas as pd\nfrom pathlib import Path\np=argparse.ArgumentParser();p.add_argument("--data-root");p.add_argument("--output");a=p.parse_args();d=pd.read_csv(Path(a.data_root)/"native.csv");o=Path(a.output)/"data";o.mkdir(parents=True);d[["sample_id","group","x"]].to_csv(o/"inputs.csv.gz",index=False);d[["sample_id","group","target"]].to_csv(o/"observations.csv.gz",index=False)\n')
write(pack/'adapter.json',{'entrypoint':'native.py','source_assets':[common.asset_record(native/'native.csv',native)]});common.seal_package(pack)
check('candidate_without_trust_rejected',lambda:admission.validate_adapter(pack,native,fixture/'no_trust'),True)
v=admission.validate_adapter(pack,native,fixture/'validation',True);check('candidate_native_reconstruction',lambda:ensure(v['status']=='pass'))
proposal=fixture/'proposal';proposal.mkdir();(proposal/'evidence.txt').write_text('Synthetic fixture, not scientific evidence or a submitted discovery.');prop={'schema_version':'principia.task-proposal/3.0','case_id':task['case_id'],'proposed_task_id':task['task_id'],'target':task['target'],'target_units':task['target_units'],'permitted_inputs':['x'],'input_availability':'fixture static input','independent_groups':['four synthetic groups'],'baseline_families':['constant'],'exclusions':['none'],'measurement_anchors':[{'evidence_id':'A','locator':'synthetic native fixture'}],'exposure':{'fresh_confirmation':False},'scientific_test':'test admission software only','source_derived_targets_disclosure':'synthetic QA fixture only','evidence_assets':[dict(common.asset_record(proposal/'evidence.txt',proposal),id='A',role='fixture')]};write(proposal/'proposal.json',prop)
bindings={'proposal_sha256':common.digest(proposal/'proposal.json'),'package_manifest_sha256':common.digest(pack/'MANIFEST.json'),'validation_sha256':common.digest(fixture/'validation/validation.json')}
reviews=[]
for role in ['computational','scientific_critical']:
 review={'role':role,'reviewer_id':role+'-fixture','bindings':bindings,'recommendation':'accept','checks':{k:{'status':'supported','rationale':'Synthetic pipeline fixture only, no scientific endorsement'}for k in ['measurement_semantics','information_budget','grouping','controls','source_rights','scientific_nontriviality']}};reviews.append(write(fixture/(role+'.json'),review))
decision={'bindings':bindings,'maintainer_id':'fixture-maintainer','rationale':'Software fixture only','decision':'accept'};dp=write(fixture/'decision.json',decision)
accepted=admission.admit(proposal,pack,fixture/'validation/validation.json',reviews,dp,fixture/'accepted');check('accepted_task_not_self_registered',lambda:ensure(accepted['decision']=='accept'and not accepted['registered']))
root=fixture/'registry';root.mkdir();write(root/'registry.json',{'tasks':[],'cases':[{'case_id':'P100-037','task_ids':[],'default_task':'unchanged'}]});r=admission.register(fixture/'accepted','fixture-maintainer',fixture/'registered',root);check('maintainer_registers_versioned_task',lambda:ensure(r['registered']and common.load_json(root/'registry.json')['cases'][0]['default_task']=='unchanged'))
check('duplicate_registration_rejected',lambda:admission.register(fixture/'accepted','fixture-maintainer',fixture/'again',root),True)
check('wrong_maintainer_rejected',lambda:admission.register(fixture/'accepted','impostor',fixture/'wrong',root),True)
rejected_review=common.load_json(reviews[1]);rejected_review['checks']['scientific_nontriviality']['status']='unsupported';write(reviews[1],rejected_review)
check('unresolved_review_blocks_admission',lambda:admission.admit(proposal,pack,fixture/'validation/validation.json',reviews,dp,fixture/'bad_accept'),True)
decision['decision']='reject';decision['rationale']='Fixture demonstrates explicit nontriviality rejection';write(dp,decision);r=admission.admit(proposal,pack,fixture/'validation/validation.json',reviews,dp,fixture/'rejected');check('justified_rejection_recorded',lambda:ensure(r['decision']=='reject'and not r['registered']))
check('rejected_task_cannot_register',lambda:admission.register(fixture/'rejected','fixture-maintainer',fixture/'reject_register',root),True)
# Brier primary units must not contaminate absolute-probability diagnostics.
bt,bp,bx,by,br=common.context('P100-035.original.v1');__import__('submissions').example(bt,bp,bx,br,W/'probability_example');pr=benchmark.evaluate(bt['task_id'],W/'probability_example',W/'probability_report')
check('probability_mae_units_are_not_squared',lambda:ensure(pr['physical_error_units']=='probability' and pr['normalization']['units']=='probability'))

# Audit coverage and explicitly preserved historical evidence.
q=common.load_json(B/'quality/ELIGIBILITY.json');check('all100_cases_and_registered_tasks',lambda:ensure(len(q['cases'])==100 and len(q['tasks'])==len(common.registry()['tasks']) and len(q['tasks'])in[134,135]))
findings=common.load_json(B/'quality/FINDING_REGISTER.json')['findings'];check('all_nonadequacy_findings_have_executable_context',lambda:ensure(all(f['executable_bindings']or f['assessment_id'] for f in findings)))
def verify_finding_bindings():
 def walk(value):
  if isinstance(value,dict):
   if isinstance(value.get('path'),str) and 'sha256'in value:
    path=common.safe_path(B,value['path'])
    ensure(common.digest(path)==value['sha256'],'Finding evidence hash mismatch: '+value['path'])
    if 'bytes'in value:ensure(path.stat().st_size==value['bytes'],'Finding evidence size mismatch')
   for child in value.values():walk(child)
  elif isinstance(value,list):
   for child in value:walk(child)
 for finding in findings:
  walk(finding)
  source=finding['claim_source'];claim=common.load_json(B/source['path'])
  for key in source['json_pointer'].strip('/').split('/'):
   claim=claim[int(key)]if isinstance(claim,list)else claim[key]
  ensure(claim['id']==finding['finding_id'],'Claim pointer identifies a different finding')
 for case in q['cases']:
  ensure(set(case['finding_ids'])=={v['finding_id']for v in findings if v['case_id']==case['case_id']},'Case finding inventory mismatch')
check('finding_evidence_hashes_and_projection_links',verify_finding_bindings)
check('all_baseline_labels_present',lambda:ensure(all(c['baseline_label']=='implemented by GPT-6 Astra'for c in q['cases'])))
check('degenerate_case5_diagnostic',lambda:ensure(next(c for c in q['cases']if c['case_id']=='P100-005')['default_tier']=='adequacy_falsification_diagnostic'))
check('no_novelty_or_impact_fabricated',lambda:ensure(all(c['novelty_status']=='not_adjudicated'and not c['practical_relevance']['demonstrated_deployment_benefit']for c in q['cases'])))
common.save_json(W/'RESULTS.json',{'checks':checks,'passed':sum(c['passed']for c in checks),'total':len(checks)});print(json.dumps({'passed':sum(c['passed']for c in checks),'total':len(checks),'failures':[c for c in checks if not c['passed']]},indent=2));raise SystemExit(0 if all(c['passed']for c in checks)else 1)
