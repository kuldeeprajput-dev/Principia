"""Check collection contracts and release assets without fitting or running submitted code."""
from pathlib import Path
import sys,argparse,json,re
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'evaluation'))
from common import *
import workflow
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();rows=[]
def check(name,fn):
 try:detail=fn();rows.append({'check':name,'status':'pass','detail':detail})
 except Exception as e:rows.append({'check':name,'status':'fail','detail':str(e)})
r=registry()
def catalog():
 assert len(r['cases'])==100 and len({c['case_id']for c in r['cases']})==100
 assert sum(c['evaluator_ready']for c in r['cases'])==100
 assert sum(c['status']=='awaiting_asd_and_evaluator'for c in r['cases'])==0
 assert len(r['tasks'])in[134,135] and len({t['task_id']for t in r['tasks']})==len(r['tasks'])
 assert sum(c.get('predictive_ready', bool(c['task_ids'])) for c in r['cases'])==99
 assert len(r.get('assessments',[]))==1
 for c in r['cases']:
  assert set(c['task_ids'])=={t['task_id']for t in r['tasks']if t['case_id']==c['case_id']}
 return {'cases':100,'equipped':100,'pending':0,'tasks':len(r['tasks'])}
check('registry_cardinality_and_links',catalog)
for t in r['tasks']:
 def run(t=t):
  task,p,x,y,refs=context(t['task_id']);validate_schema(task,'task.schema.json');assert set(task['permitted_inputs'])==set(task['input_units']);assert set(task['permitted_inputs'])<=set(x.columns);assert task['exposure']['current']=='exposed';return{'rows':len(x),'models':len(refs.columns)-2}
 check('task:'+t['task_id'],run)
for c in r['cases']:
 if not c['evaluator_ready']:continue
 def case(c=c):
  p=R/'cases'/c['case_id']/'final_results';verify_assets(p,load_json(p/'MANIFEST.json')['files']);assert (p/'FINDINGS.pdf').read_bytes().startswith(b'%PDF');assert (p/'FINDINGS.md').stat().st_size>100
  q=workflow.claims(R/'reviews/portfolios'/c['case_id']);assert q['case_id']==c['case_id'];return{'findings':len(q['findings'])}
 check('portfolio:'+c['case_id'],case)
def finding_ids():
 known={t['task_id']for t in r['tasks']};count=0
 for c in r['cases']:
  if not c['evaluator_ready']:continue
  j=load_json(R/'cases'/c['case_id']/'final_results/findings.json')
  for f in j['findings']:
   assert set(f.get('task_ids',[]))<=known,(c['case_id'],f['finding_id'],'unregistered task')
   count+=1
 return {'finding_records':count,'all_indexed_tasks_available':True}
check('finding_index_task_references',finding_ids)
check('sealed_evaluator_assets',lambda:verify_assets(R,load_json(R/'EVALUATOR_MANIFEST.json')['files']))
check('release_allowlist',lambda:verify_assets(R,load_json(R/'RELEASE_ALLOWLIST.json')['files']))
def privacy():
 bad=[];count=0
 for item in load_json(R/'RELEASE_ALLOWLIST.json')['files']:
  q=R/item['path']
  if q.suffix not in['.json','.md','.py','.txt','.csv','.cff']:continue
  content=q.read_text(errors='replace');count+=1
  if re.search(r'''/(?:Users|home)/[A-Za-z0-9_][^\s'"]+''',content):bad.append(item['path'])
 assert not bad,bad;return{'text_assets_scanned':count,'user_specific_paths_or_private_markers':0}
check('public_text_privacy_scan',privacy)
result={'status':'pass'if all(z['status']=='pass'for z in rows)else'fail','checks':rows,'test_scope':'Static schema, exact asset hashes, inventory and policy markers; not a universal sensitive-content detector.'};save_json(a.output,result);print(json.dumps({'status':result['status'],'checks':len(rows),'failures':[z for z in rows if z['status']=='fail']}));raise SystemExit(0 if result['status']=='pass'else 1)
