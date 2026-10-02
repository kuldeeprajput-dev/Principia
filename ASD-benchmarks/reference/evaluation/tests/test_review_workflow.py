"""Reusable deterministic evaluator fixture; no model fitting or native data mutation."""
from pathlib import Path
import sys,json,copy,hashlib,uuid
R=Path(__file__).resolve().parents[2]
import argparse,tempfile
_parser=argparse.ArgumentParser(description=__doc__);_parser.add_argument('--output',type=Path);_args=_parser.parse_args()
WORK=_args.output if _args.output is not None else Path(tempfile.mkdtemp(prefix='principia-evaluator-test-'))
WORK.mkdir(parents=True,exist_ok=True)
W=WORK/'review_fixtures';W.mkdir(exist_ok=True);sys.path.insert(0,str(R/'evaluation'));import common,workflow
checks=[]
def check(name,fn,reject=False):
 try:r=fn()
 except (ValueError,TypeError,KeyError)as e:checks.append({'check':name,'status':'pass'if reject else'fail','detail':str(e)});return
 checks.append({'check':name,'status':'fail'if reject else'pass','detail':'unexpected acceptance'if reject else'tested'})
def write(path,x):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(x));return path
case=W/'claims';case.mkdir(exist_ok=True);(case/'evidence.txt').write_text('Synthetic validation fixture, not scientific evidence or a benchmark reference.\n');evidence={'id':'A1','path':'evidence.txt','sha256':common.digest(case/'evidence.txt'),'role':'fixture'}
claims={'schema_version':'principia.claims/3.0','case_id':'P100-023','training_and_exposure':{'current_outcomes_exposed':True},'evidence_assets':[evidence],'findings':[{'id':'F1','classification':'falsified','statement':'Synthetic fixture to validate the protocol','applicability':'No scientific applicability','limitations':'Fixture only','falsification':'Illustrative inconsistent inputs','prior_art':'Not a scientific claim','evidence_ids':['A1']}]};write(case/'claims.json',claims)
check('falsification_without_fabricated_equation',lambda:workflow.claims(case))
packetdir=W/('packet-'+uuid.uuid4().hex);packet=workflow.prepare_review(case,packetdir)
def review(role,rid):
 q=common.load_json(packetdir/(role+'.template.json'));q['reviewer_id']=rid
 for f in q['findings']:
  for k,v in f['dimensions'].items():v.update(status='not_assessed',rationale='Synthetic fixture has no scientific evidence',evidence_ids=[])
 return q
comp=review('computational','reviewer_A');sci=review('scientific_critical','reviewer_B')
def combine(label,a=comp,b=sci,p=packet):
 d=W/(label+'-'+uuid.uuid4().hex);d.mkdir();write(d/'packet.json',p);write(d/'a.json',a);write(d/'b.json',b);return workflow.combine_reviews(d/'packet.json',[d/'a.json',d/'b.json'],d/'out')
check('two_separate_review_roles',lambda:combine('valid'))
q=copy.deepcopy(sci);q['reviewer_id']='reviewer_A';check('same_reviewer_id_rejected',lambda:combine('same',b=q),True)
q=copy.deepcopy(sci);q['bindings']['claims_sha256']='bad';check('tampered_claim_binding_rejected',lambda:combine('binding',b=q),True)
q=copy.deepcopy(sci);q['findings'][0]['dimensions']['novelty']={'status':'supported','rationale':'No anchor','evidence_ids':[]};check('unsupported_assessment_without_anchor_rejected',lambda:combine('anchor',b=q),True)
q=copy.deepcopy(sci);q['findings'][0]['dimensions']['novelty']['status']='excellent';check('unknown_dimension_status_rejected',lambda:combine('status',b=q),True)
q=copy.deepcopy(sci);q['schema_version']='garbage';check('unknown_review_schema_rejected',lambda:combine('schema',b=q),True)
q=copy.deepcopy(sci);q['findings'][0]['disposition']='automatically_publish_as_new_law';check('unknown_review_disposition_rejected',lambda:combine('disposition',b=q),True)
q=copy.deepcopy(packet);q['schema_version']='garbage';check('unknown_packet_schema_rejected',lambda:combine('packetschema',p=q),True)
proposal={'schema_version':'principia.task-proposal/3.0','case_id':'P100-023','proposed_task_id':'P100-023.synthetic-fixture.v1','target':'fixture only','target_units':'U','permitted_inputs':['x'],'input_availability':'before response','independent_groups':['group'],'baseline_families':['constant'],'exclusions':['none'],'measurement_anchors':[{'evidence_id':'A1','locator':'synthetic line1'}],'exposure':{'fresh_confirmation':False},'scientific_test':'fixture only','source_derived_targets_disclosure':'no real scientific target','evidence_assets':[evidence]}
def propose(label,change=None):
 d=W/(label+'-'+uuid.uuid4().hex);d.mkdir();(d/'evidence.txt').write_bytes((case/'evidence.txt').read_bytes());q=copy.deepcopy(proposal)
 if change:change(q)
 write(d/'proposal.json',q);return workflow.propose(d,d/'out')
check('valid_proposal_remains_unregistered',lambda:propose('validproposal'))
check('existing_task_overwrite_rejected',lambda:propose('overwrite',lambda q:q.update(proposed_task_id='P100-023.original.v1')),True)
check('false_freshness_rejected',lambda:propose('fresh',lambda q:q['exposure'].update(fresh_confirmation=True)),True)
check('unbound_native_anchor_rejected',lambda:propose('badanchor',lambda q:q['measurement_anchors'][0].update(evidence_id='missing')),True)
check('proposal_string_predictor_list_rejected',lambda:propose('badinputs',lambda q:q.update(permitted_inputs='x')),True)
check('proposal_nonstring_identity_rejected',lambda:propose('badid',lambda q:q.update(proposed_task_id=123)),True)
(WORK/'EVALUATOR_REVIEW_FIXTURES.json').write_text(json.dumps({'checks':checks},indent=2)+'\n');print(json.dumps({'checks':len(checks),'passed':sum(x['status']=='pass'for x in checks),'failures':[x for x in checks if x['status']=='fail']},indent=2))

raise SystemExit(0 if all(c["status"]=="pass" for c in checks) else 1)
