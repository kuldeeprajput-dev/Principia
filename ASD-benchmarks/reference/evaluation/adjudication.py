"""Evidence-bound explicit resolution; never edits submitted claims or old reviews."""
from pathlib import Path
from common import load_json,digest,save_json,new_output
from workflow import STATUSES,DIMENSIONS,RUBRIC_VERSION

def adjudicate(combined_path,decision_path,output):
 report=load_json(combined_path);decision=load_json(decision_path)
 if decision.get('review_sha256')!=digest(combined_path):raise ValueError('Adjudication must bind exact combined review')
 if not decision.get('adjudicator_id')or not decision.get('scope'):raise ValueError('Adjudicator identity and scope required')
 items=decision.get('findings',[]);ids=[f.get('finding_id')for f in items];expected=[f['finding_id']for f in report['reviews']]
 if len(ids)!=len(set(ids))or set(ids)!=set(expected):raise ValueError('Adjudication finding inventory mismatch')
 evidence=set(report['bindings']['evidence_sha256'])
 for row in items:
  if row.get('disposition')not in STATUSES or not row.get('rationale'):raise ValueError('Resolution requires disposition and reason')
  if not row.get('evidence_ids')or not set(row['evidence_ids'])<=evidence:raise ValueError('Unbound adjudication evidence')
  prior=next(f for f in report['reviews']if f['finding_id']==row['finding_id'])
  if not set(prior['disagreements'])<=set(row.get('resolved_dimensions',[])):raise ValueError('Every substantive disagreement needs explicit resolution')
 out=new_output(output);out.mkdir(parents=True);result={'schema_version':'principia.adjudication/1.0','rubric_version':RUBRIC_VERSION,'review_sha256':digest(combined_path),'decision_sha256':digest(decision_path),'adjudicator_id':decision['adjudicator_id'],'scope':decision['scope'],'findings':items,'automatic_task_registration':False,'novelty_certified':False};save_json(out/'adjudication.json',result);return result
