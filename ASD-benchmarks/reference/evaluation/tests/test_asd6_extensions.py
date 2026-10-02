"""Versioned probability and Boolean-reconstruction regression fixtures."""
from pathlib import Path
import sys,json,tempfile
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import metrics
from preparation import verify_reconstruction as vr
T={'aggregation':{'hierarchy':['group']},'metric_kind':'brier','primary_units':'squared probability','target_units':'binary choice','error_units':'probability'}
checks=[]
def test(name,f):
 f();checks.append({'test':name,'status':'pass'})
def near(a,b):assert np.isclose(a,b), (a,b)
def reject(f):
 try:f()
 except ValueError:return
 raise AssertionError('Invalid input accepted')
d=pd.DataFrame({'group':['A','A','A','B'],'target':[1.,0.,1.,0.]});p=np.array([.8,.2,.5,.9]);r,_=metrics.score(d,p,T)
test('Brier respects equal participant weighting',lambda:near(r['primary_error'],((.04+.04+.25)/3+.81)/2))
test('log loss matches manual grouped calculation',lambda:near(r['probability_diagnostics']['log_loss_nats'],((-np.log(.8)-np.log(.8)-np.log(.5))/3-np.log(.1))/2))
test('invalid probability rejected',lambda:reject(lambda:metrics.score(d,[.8,.2,.5,1.1],T)))
test('nonbinary truth rejected',lambda:reject(lambda:metrics.score(d.assign(target=[.5,0,1,0]),p,T)))
a=metrics.score(pd.DataFrame({'group':['x','y'],'target':[0.,1.]}),[1.,0.],T)[0]['probability_diagnostics']
test('certainty error has explicit infinite-log-loss reason',lambda:near(a['certainty_error_rows'],2))
assert a['log_loss_nats']is None and a['log_loss_undefined_reason']
test('all-wrong binary F1 is zero',lambda:near(a['binary_events']['f1'],0))
test('calibration bin endpoints cover exactly once',lambda:near(sum(z['weight']for z in a['calibration_bins']),1))
# Exercise the actual command comparator, including CSV Boolean inference.
original=vr.prepare;argv=sys.argv[:]
for mode in ['match','changed','numeric_instead']:
 with tempfile.TemporaryDirectory()as tmp:
  q=Path(tmp);(q/'package/data').mkdir(parents=True)
  expected=pd.DataFrame({'sample_id':['a','b'],'group':['g','g'],'flag':[True,False]})
  for n in ['inputs','observations']:expected.to_csv(q/f'package/data/{n}.csv.gz',index=False)
  (q/'registry.json').write_text(json.dumps({'tasks':[{'task_id':'fixture','case_id':'fixture','case_number':1,'family':'original','package':'package'}]}))
  def fake(task,data,supp,out):
   o=Path(out)/'data';o.mkdir();actual=expected.copy()
   if mode=='changed':actual['flag']=[False,False]
   if mode=='numeric_instead':actual['flag']=[1,0]
   for n in ['inputs','observations']:actual.to_csv(o/f'{n}.csv.gz',index=False)
   return {'rows':2,'native_assets_verified':0}
  vr.prepare=fake;sys.argv=['fixture','--benchmark',str(q),'--data-root',str(q),'--report',str(q/'report.json')]
  try:vr.main()
  except SystemExit as e:assert e.code==1 and mode!='match'
  result=json.loads((q/'report.json').read_text());assert result['status']==('pass'if mode=='match'else'fail');checks.append({'test':'Boolean reconstruction '+mode,'status':'pass'})
vr.prepare=original;sys.argv=argv
report={'status':'pass','version':'asd6-evaluation-extensions/1.0','tests':len(checks),'checks':checks}
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
