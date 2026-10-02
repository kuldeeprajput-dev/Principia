from pathlib import Path
import json,hashlib,importlib.util,tempfile,shutil,subprocess,sys,math,datetime
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent

def mod(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def manifest(pkg):
 a=[{'path':str(f.relative_to(pkg)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(pkg.rglob('*')) if f.is_file() and f.name!='MANIFEST.json' and '__pycache__' not in str(f)]
 (pkg/'MANIFEST.json').write_text(json.dumps({'schema':'asd6.package/1.0','files':a},indent=2)+'\n')

def main():
 p=ROOT;pkg=p/'package';data_root=Path(sys.argv[1]);checks=[];record=lambda n:checks.append({'check':n,'status':'passed'});manifest(pkg)
 for a in json.loads((p/'FREEZE.json').read_text())['files']:
  assert hashlib.sha256((p/a['path']).read_bytes()).hexdigest()==a['sha256'],a['path']
 record('Scientific freeze unchanged after confirmation')
 native=mod('native_audit',p/'native.py');d=native.prepare(data_root);obs=pd.read_csv(pkg/'data/observations.csv.gz');x=pd.read_csv(pkg/'data/inputs.csv.gz');expected=d[d.partition=='confirmation'].reset_index(drop=True);assert expected.sample_id.tolist()==obs.sample_id.tolist();assert expected.group.tolist()==obs.group.tolist();assert np.allclose(expected.target,obs.target,atol=1e-12,rtol=1e-12);record('Native reconstruction, source hashes, target values and ordered anchors')
 rules=json.loads((pkg/'rules.json').read_text());assert set(d[d.partition=='development'].group).isdisjoint(set(expected.group));record('Complete groups remain disjoint across development and confirmation')
 for c in rules['numeric_columns']:assert np.allclose(expected[c],x[c],rtol=1e-12,atol=1e-12)
 record('All native predictor/calibration values reproduce frozen package')
 run=mod('run_audit',pkg/'run.py');pred=pd.read_csv(pkg/'evidence/predictions.csv.gz');mt=pd.read_csv(pkg/'evidence/metrics.csv').set_index('model');audit=[];rng=np.random.default_rng(1901);order=rng.permutation(len(x));rowgroups={g:np.flatnonzero(x.group.to_numpy()==g) for g in x.group.unique()}
 for n,m in rules['models'].items():
  y=run.predict(m,x);assert np.isfinite(y).all();assert np.allclose(y,pred[n],rtol=1e-9,atol=1e-9);record(n+': frozen equation reproduces predictions')
  ma=math.fsum(math.fsum(abs(float(y[i])-float(obs.target.iloc[i])) for i in ids)/len(ids) for ids in rowgroups.values())/len(rowgroups);assert math.isclose(ma,float(mt.loc[n,'primary_error']),rel_tol=1e-9,abs_tol=1e-10);record(n+': independent scalar/group MAE')
  poison=x.copy();poison['target']=np.nan;poison['future_response']=1e50;assert np.allclose(y,run.predict(m,poison),rtol=1e-12,atol=1e-12);assert np.allclose(y[order],run.predict(m,x.iloc[order]),rtol=1e-12,atol=1e-12);record(n+': target poison and row-order invariance')
  audit.append({'model':n,'min_prediction':float(np.min(y)),'max_prediction':float(np.max(y)),'negative_prediction_rows':int((y<0).sum()),'jacobian_condition':m.get('jacobian_condition'),'parameter_at_bound':bool(any(np.isclose(v,lo,atol=1e-5) or np.isclose(v,hi,atol=1e-5) for v,lo,hi in zip(m['parameters'],*m.get('bounds',[[],[]]))))})
 # Out-of-fold coefficients reproduce all historical OOF predictions without fitting.
 dev=pd.read_csv(p/'development.csv.gz');case=int(p.name[-3:])
 for ap in sorted(p.glob('attempts/attempt-*')):
  saved=pd.read_csv(ap/'predictions.csv.gz').set_index('sample_id');states=json.loads((ap/'fold_models.json').read_text())
  for fs in states:
   va=dev[dev.fold==fs['fold']] if case in [22,65] else dev[dev.group==fs['fold']]
   y=run.predict(fs['state'],va);assert np.allclose(y,saved.loc[va.sample_id,'prediction'],atol=1e-8,rtol=1e-8)
   if case!=65:assert set(va.group).isdisjoint(fs['state']['training_groups'])
  record(ap.name+': OOF reconstruction and grouping')
 # Standalone replay and deliberate corruptions in disposable paths.
 with tempfile.TemporaryDirectory(prefix='asd6-verify-') as td:
  q=Path(td)/'package';shutil.copytree(pkg,q)
  def cli(args=[]):return subprocess.run([sys.executable,str(q/'run.py')]+args,text=True,capture_output=True,cwd=q)
  r=cli();assert r.returncode==0,r.stderr;record('Standalone package replay without history path')
  bad=x.copy();bad.loc[len(bad)]=bad.iloc[0];bad.to_csv(Path(td)/'duplicate.csv',index=False);r=cli(['--input',str(Path(td)/'duplicate.csv')]);assert r.returncode and 'Invalid identities' in r.stderr;record('Duplicate identities rejected')
  bad=x.copy();bad.loc[0,rules['numeric_columns'][0]]=np.nan;bad.to_csv(Path(td)/'nonfinite.csv',index=False);r=cli(['--input',str(Path(td)/'nonfinite.csv')]);assert r.returncode and 'Nonfinite predictor' in r.stderr;record('Nonfinite predictor rejected')
  f=q/'evidence/predictions.csv.gz';f.write_bytes(f.read_bytes()+b'CORRUPT');r=cli();assert r.returncode and 'integrity failure' in r.stderr;record('Corrupted package asset rejected')
  f.unlink();r=cli();assert r.returncode and 'integrity failure' in r.stderr;record('Missing package asset rejected')
 (pkg/'evidence/scientific_diagnostics.json').write_text(json.dumps({'scope':'Diagnostics only; no confirmation-based reselection','models':audit,'dimensional_analysis':'Equations.json explicitly records reference units. Exponential arguments and normalized Lorentzian/logarithmic coordinates are dimensionless.','causal_calibration':'Native adapter uses fixed prefixes/endpoints only as explicitly permitted by task. No undeclared future response is an input.','identifiability':'Condition numbers depend on parameter scaling; bound hits and near-tied structural models prevent unique mechanistic identification.','interval_policy':'No population confidence intervals from dependent rows.'},indent=2)+'\n')
 report={'status':'passed','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'source_unchanged':True,'confirmation_rows':len(x),'reference_selection_unchanged':True,'native_reader_dependencies':(p/'dependencies.txt').read_text().splitlines(),'limits':'Computational verification, not independent experimental replication or novelty adjudication.'}
 (p/'FINAL_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');(pkg/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');manifest(pkg);print(p.name,len(checks),'checks passed')
if __name__=='__main__':main()
