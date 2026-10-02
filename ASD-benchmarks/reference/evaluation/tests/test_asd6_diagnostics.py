from pathlib import Path
import sys,json
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));from batch6_checks import checks
base={'aggregation':{'hierarchy':['group']},'target_units':'U','error_units':'U','evaluation_groups':['g']};rows=[]
def test(n,x,y,p,expected):
 task=dict(base,case_number=n);out=checks(task,y,np.array(p,float),x);assert expected(out),out;rows.append({'case':n,'test':out['tests'][0]['test'],'status':'pass'})
y=pd.DataFrame({'group':['g'],'target':[1.]});x=pd.DataFrame({'group':['g']})
for n in[26,29,30,34,43,44,47,48,63,76,79,89,95]:
 xx=x.copy();pp=[-1.]
 if n==34:xx['calcium']=[1.5]
 if n==43:xx=xx.assign(early_tokens_B=10,anchor_tokens_B=20,tokens_B=30)
 if n==44:xx=xx.assign(is_flow=1,is_linear=0)
 test(n,xx,y,pp,lambda z:z['tests'][0]['violations']==1)
for n in[6,22,32,38,41,65,94]:
 test(n,x,y,[-1],lambda z:z['tests'][0]['negative_predictions']==1 and 'violations'not in z['tests'][0])
xx=pd.DataFrame({'group':['a','a','a','b'],'is_flow':[1,0,0,1],'is_linear':[0,1,0,0]});yy=xx[['group']].assign(target=[10,20,30,40]);z=checks(dict(base,case_number=44,evaluation_groups=['a','b']),yy,[1,1,2,3],xx);r=z['tests'][1];assert r['complete_instances']==1 and r['assigned_instances']==2 and r['mean_regret_seconds']==0;rows.append({'test':'Formulation ties and abstained incomplete triples','status':'pass'})
z=checks(dict(base,case_number=76),pd.DataFrame({'group':['a','b'],'target':[0,1]}),[1,0],pd.DataFrame({'group':['a','b']}));assert z['tests'][1]['f1']==0;rows.append({'test':'Spike event complete failure F1 zero','status':'pass'})
try:checks(dict(base,case_number=22),y,[float('nan')],x);raise AssertionError('NaN accepted')
except ValueError:rows.append({'test':'Nonfinite prediction rejection','status':'pass'})
report={'status':'pass','tests':len(rows),'checks':rows,'version':'asd6-diagnostics/1.0'}
if len(sys.argv)>1:Path(sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','tests':len(rows)}))
