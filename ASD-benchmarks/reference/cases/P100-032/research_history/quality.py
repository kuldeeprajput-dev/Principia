from pathlib import Path
import sys,json,hashlib,importlib.util,tempfile,shutil,subprocess
import numpy as np,pandas as pd
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H));import native
from run import predict
from develop import metrics
D=Path(sys.argv[1]);p=H/'package';r=json.loads((p/'rules.json').read_text());d=native.prepare(D);dd=d[d.partition=='confirmation'].reset_index(drop=True);x=pd.read_csv(p/'data/inputs.csv.gz',dtype={'sample_id':str,'group':str});y=pd.read_csv(p/'data/observations.csv.gz',dtype={'sample_id':str,'group':str});pr=pd.read_csv(p/'evidence/predictions.csv.gz',dtype={'sample_id':str,'group':str});m=pd.read_csv(p/'evidence/metrics.csv').set_index('model');checks={}
assert x.sample_id.tolist()==dd.sample_id.tolist()==y.sample_id.tolist()==pr.sample_id.tolist();assert np.allclose(dd.target,y.target,atol=1e-12);assert np.allclose(x[r['numeric_columns']].to_numpy(float),dd[r['numeric_columns']].to_numpy(float),atol=1e-12);checks['native_reconstruction']='identities, groups, targets and declared inputs match package exactly'
assert not(set(d[d.partition=='development'].group)&set(dd.group));assert d.groupby('linked_unit').partition.nunique().max()==1;checks['linked_groups']='no group or linked unit crosses partition';checks['models']={}
for k,state in r['models'].items():
 v=predict(state,x);maxerr=float(np.max(np.abs(v-pr[k])));score=metrics(dd,v);err=abs(score['primary_error']-m.loc[k,'primary_error']);assert maxerr<1e-8 and err<1e-8;checks['models'][k]=dict(max_prediction_difference=maxerr,primary_metric_difference=err)
with tempfile.TemporaryDirectory() as t:
 root=Path(t);iso=root/'standalone';shutil.copytree(p,iso);q=subprocess.run([sys.executable,'run.py'],cwd=iso,capture_output=True,text=True,env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1'});assert q.returncode==0,q.stderr;checks['isolated_replay']=q.stdout.strip()
 # Missing assets and corrupted native bytes fail before parsing.
 try:native.prepare(root/'missing');raise AssertionError('missing source accepted')
 except ValueError as e:checks['missing_source_rejected']=str(e)
 man=json.loads((H/'SOURCE_MANIFEST.json').read_text());bad=root/'corrupt';bad.mkdir();first=man['assets'][0];f=bad/first['path'];f.parent.mkdir(parents=True);f.write_bytes(b'corrupt')
 try:native.prepare(bad);raise AssertionError('corrupt source accepted')
 except ValueError as e:checks['corrupt_source_rejected']=str(e)
 # Freeze current source models remains exact; a documentation addition does not replace states.
 (iso/'rules.json').write_text((iso/'rules.json').read_text()+' ');q=subprocess.run([sys.executable,'run.py'],cwd=iso,capture_output=True,text=True,env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1'});assert q.returncode!=0;checks['corrupt_package_rejected']='rules.json hash mismatch'
 for name in ['native.py','SOURCE_MANIFEST.json','SPLITS.json']:shutil.copy2(H/name,root/name)
 z=importlib.util.spec_from_file_location('relocated',root/'native.py');mod=importlib.util.module_from_spec(z);z.loader.exec_module(mod);e=mod.prepare(D);assert e.sample_id.tolist()==d.sample_id.tolist() and np.allclose(e.target,d.target);checks['relocated_native_adapter']='passes with adjacent source/split manifests only'
freeze=json.loads((H/'FREEZE.json').read_text());assert all(hashlib.sha256((H/a['path']).read_bytes()).hexdigest()==a['sha256'] for a in freeze['assets']);checks['freeze_integrity']='all frozen files unchanged';checks['confirmation_status']='outcomes exposed after the recorded first confirmation; no refitting'
(H/'QUALITY_CHECKS.json').write_text(json.dumps(checks,indent=2));print(H.name,'quality checks passed',len(r['models']),'models')
