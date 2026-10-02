"""Regenerate only current navigation from the authoritative registry. Frozen task cards are versioned assets."""
from pathlib import Path
import json,csv
B=Path(__file__).resolve().parents[1];r=json.loads((B/'registry.json').read_text());n=sum(c['status'].startswith('explored')for c in r['cases']);m=sum(len(t['models'])for t in r['tasks']);predictive=sum(bool(c.get('default_task'))for c in r['cases']);adequacy=sum(c.get('evaluation_mode')=='admissibility_only'for c in r['cases'])
(B/'CATALOG.json').write_text(json.dumps({'benchmark':'Principia-100','version':r['version'],'cases':r['cases']},indent=2,ensure_ascii=False)+'\n')
cols=['case_id','title','domain','status','evaluator_ready','predictive_evaluator_ready','evaluation_mode','default_task','task_ids','modalities','source_url','license_or_terms']
with(B/'CATALOG.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
 for original in r['cases']:
  c=dict(original);c.setdefault('predictive_evaluator_ready',bool(c.get('default_task')));c.setdefault('evaluation_mode','registered_prediction'if c.get('default_task')else'pending');w.writerow({k:'; '.join(c[k])if isinstance(c[k],list)else c[k]for k in cols})
s='# Principia-100 catalog\n\n100 scenarios: **'+str(n)+' explored; '+str(100-n)+' pending**. Of the explored cases, '+str(predictive)+' have registered prediction evaluators and '+str(adequacy)+' have source-adequacy assessment only. Scientific abstention is explicit and carries no invented accuracy score. The local registry has '+str(len(r['tasks']))+' versioned prediction contracts and '+str(m)+' model/task comparisons, including archival and corrected contract versions. Documentation-only v2 contracts do not add experiments or discoveries. All current outcomes are exposed.\n\n| Case | Scenario | Status | Task versions | Current quality |\n|---|---|---|---:|---|\n'
for c in r['cases']:
 s+='| ['+c['case_id']+'](cases/'+c['case_id']+'/README.md) | '+c['title'].replace('|',' / ')+' | '+('Scientific abstention; adequacy evaluator'if c.get('evaluation_mode')=='admissibility_only'else'Explored; prediction evaluator'if c.get('default_task')else'Pending')+' | '+str(len(c['task_ids']))+' | '+('[Audit](cases/'+c['case_id']+'/QUALITY_AUDIT.md)'if c['evaluator_ready']else'Awaiting ASD')+' |\n'
(B/'CATALOG.md').write_text(s)
