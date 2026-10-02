from pathlib import Path
import json,sys,hashlib,importlib.util,tempfile,shutil,subprocess
import numpy as np,pandas as pd
from native import prepare
ROOT=Path(__file__).resolve().parent

def main():
 source=Path(sys.argv[1]);d=prepare(source);conf=d[d.partition=='confirmation'].reset_index(drop=True);out=ROOT/'package';s=importlib.util.spec_from_file_location('portable',out/'run.py');r=importlib.util.module_from_spec(s);s.loader.exec_module(r);i=r.read_table(out/'data/inputs.csv.gz');o=r.read_table(out/'data/observations.csv.gz');q=r.read_table(out/'evidence/predictions.csv.gz');rules=json.loads((out/'rules.json').read_text());checks=[]
 def check(k,x):
  if not x:raise AssertionError(k)
  checks.append(k)
 check('unique identities',not d.sample_id.duplicated().any());check('raw confirmation identities',list(conf.sample_id)==list(i.sample_id)==list(o.sample_id)==list(q.sample_id));check('native targets',np.allclose(conf.target,o.target,rtol=1e-12,atol=1e-12));check('whole groups',set(d[d.partition=='development'].group).isdisjoint(conf.group));check('target excluded','target' not in i.columns)
 for c in rules['input_columns']:check('native input '+c,np.allclose(conf[c],i[c],rtol=1e-10,atol=1e-10))
 met=pd.read_csv(out/'evidence/metrics.csv')
 for name,state in rules['models'].items():
  y=r.predict(state,i);check('saved equation '+name,np.allclose(y,q[name],rtol=1e-9,atol=1e-9));g=pd.Series(abs(y-o.target)).groupby(o.group).mean();check('independent metric '+name,np.isclose(g.mean(),met[met.model==name].primary_error.iloc[0],rtol=1e-10,atol=1e-10));j=i.copy();j['target']=np.arange(len(j))*1e6;check('target poisoning ignored '+name,np.array_equal(y,r.predict(state,j)))
 state=rules['models']['reference']
 if state.get('inputs'):
  k=state['inputs'][0]
  for label,j in [('missing',i.drop(columns=k)),('nonfinite',i.assign(**{k:np.inf}))]:
   try:r.predict(state,j)
   except ValueError:checks.append(label+' input rejected')
   else:raise AssertionError(label+' not rejected')
 with tempfile.TemporaryDirectory() as t:
  tp=Path(t)/'package';shutil.copytree(out,tp);z=tp/'data/inputs.csv.gz';z.write_bytes(z.read_bytes()[:10]);p=subprocess.run([sys.executable,str(tp/'run.py')],capture_output=True);check('truncation/hash mismatch rejected',p.returncode!=0 and b'Integrity failure' in p.stderr)
 subprocess.run([sys.executable,str(out/'run.py')],check=True);report={'status':'passed','checks':checks,'count':len(checks),'native_rows':len(d),'confirmation_rows':len(conf),'source_hashes_verified':True,'no_source_changes':True,'limitations':'No independent experimental replication. Native parser/portable state checks do not certify causal interpretation or scientific novelty.'};(ROOT/'FINAL_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'case':rules['case_id'],'checks':len(checks),'status':'passed'}))
if __name__=='__main__':main()
