#!/usr/bin/env python3
"""Verify joined public reference contracts; works with frozen LFS pointers.

This is a structural check, not numerical or remote-payload verification.
Run verify_git_release.py as well to check every admitted file/pointer.
"""
import sys
sys.dont_write_bytecode = True
import argparse, hashlib, json
from pathlib import Path
from replay import safe
from verify_git_release import pointer_matches

def validate(root):
    def load(p): return json.loads(safe(root,p).read_text())
    index=load('TASK_INDEX.json'); registry=load('reference/registry.json')
    source=load('BENCHMARK_MANIFEST.json'); release=load('RELEASE_MANIFEST.json')
    actual={a['path']:a for a in release['files']}; issues=[]
    def require(ok,reason):
        if not ok: issues.append(reason)
    rows=index['cases']; ids={r['case_id'] for r in rows}
    require(len(rows)==100 and ids=={f'P100-{i:03d}' for i in range(1,101)},'100 unique case IDs required')
    raw={r['case_id']:r for r in source['cases']}; cases={r['case_id']:r for r in registry['cases']}
    tasks={r['task_id']:r for r in registry['tasks']}
    require(len(tasks)==len(registry['tasks'])==134,'134 unique public task versions required')
    require(sum(bool(r['predictive_ready']) for r in rows)==99,'99 numerical cases required')
    require('P100-096.continuation.v1' not in tasks,'unresolved supplemental task must not be included')
    for row in rows:
        cid=row['case_id']; case=cases[cid]
        require(row['baseline_label']=='implemented by GPT-6 Astra',cid+': baseline attribution')
        require(row['task_ids']==case['task_ids'],cid+': task navigation mismatch')
        require(row['outcome_exposure']=='exposed',cid+': exposure mismatch')
        require(set(row['task_ids'])=={t for t,v in tasks.items() if v['case_id']==cid},cid+': task ownership')
        require(set(raw[cid]['asset_paths'])<=actual.keys(),cid+': missing source asset')
        require(all(p.startswith(row['source_folder']+'/') for p in raw[cid]['asset_paths']),cid+': incorrect source folder')
        for name in ['FINDINGS.md','FINDINGS.pdf','findings.json','MANIFEST.json']:
            require(row['reference_folder']+'/final_results/'+name in actual,cid+': missing '+name)
        require(row['audit_card'] in actual,cid+': missing audit card')
    for inner_name,base in [('RELEASE_ALLOWLIST.json','reference/'),('EVALUATOR_MANIFEST.json','reference/')]:
        for a in load('reference/'+inner_name)['files']:
            key=base+a['path']; outer=actual.get(key,{})
            require(all(outer.get(k)==a[k] for k in ['bytes','sha256']),'inner/outer manifest disagreement: '+key)
    require(index['release_version']==release['version']==source['version'],'release version mismatch')
    baseline=load('reference/BASELINE.json'); require(baseline['current_outcomes_exposed'] is True,'baseline exposure missing')
    return {'status':'pass' if not issues else 'fail','cases':len(rows),'numerical_task_versions':len(tasks),'checks':'source, reference, task, attribution and nested manifest linkage; no numerical execution','issues':issues}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);a=p.parse_args()
    try: result=validate(a.root)
    except (ValueError,KeyError,OSError) as e: result={'status':'fail','issues':[str(e)]}
    print(json.dumps(result,indent=2));sys.exit(result['status']!='pass')
