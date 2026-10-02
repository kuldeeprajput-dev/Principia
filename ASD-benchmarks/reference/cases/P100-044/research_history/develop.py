from pathlib import Path
import json,sys,hashlib,datetime,importlib.util
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from native import prepare
W=Path(__file__).resolve().parent;D=W.parents[3].parent/'local-datas'
sp=importlib.util.spec_from_file_location('frozen',W/'package/run.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
def save(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,allow_nan=False)+'\n')
def rbfit(d,length,ridge):
 X=r.features('rbf',d);mu=X.mean(0);sd=np.maximum(X.std(0),1e-6);X=(X-mu)/sd;F=np.c_[np.ones(len(d)),np.exp(-((X[:,None,:]-X[None,:,:])**2).sum(2)/(2*length**2))];A=F/(len(d)**.5);b=d.target.to_numpy(float)/(7200*len(d)**.5);coef=np.linalg.solve(A.T@A+ridge*np.eye(F.shape[1]),A.T@b)
 return dict(kind='rbf',coefficients=coef.tolist(),centers=X.tolist(),mean=mu.tolist(),scale=sd.tolist(),length=length,ridge=ridge,parameters=len(coef))
def fit(kind,d):
 y=d.target.to_numpy(float)
 if kind=='constant':return dict(kind=kind,value=float(np.median(y)),parameters=1)
 if kind=='form_median':return dict(kind=kind,values={k:float(g.target.median())for k,g in d.groupby('formulation')},parameters=3)
 if kind=='rbf':
  cs=[]
  for length in [1.,2.,4.]:
   for ridge in [.001,.03,.3]:
    errs=[]
    for g in sorted(d.group.unique()):
     tr=d[d.group!=g];v=d[d.group==g];s=rbfit(tr,length,ridge);errs.append(float(abs(r.predict(s,v)-v.target).mean()))
    cs.append([float(np.mean(errs)),length,ridge])
  _,le,ri=min(cs);s=rbfit(d,le,ri);s['inner_cv']=cs;return s
 X=r.features(kind,d);k=X.shape[1];fits=[]
 for b0 in ([0.,-2.,2.]if kind in ['sigmoid','formulation_threshold']else[3.,6.,8.]):
  x0=np.zeros(k);x0[0]=b0;x0[1]=2.
  def fun(p):return np.r_[(r.predict(dict(kind=kind,coefficients=p),d)-y)/7200/len(d)**.5,.005*p[1:]]
  q=least_squares(fun,x0,bounds=(-20,20),max_nfev=2500);fits.append(q)
 q=min(fits,key=lambda q:float(abs(r.predict(dict(kind=kind,coefficients=q.x),d)-y).mean()))
 cond=float(np.linalg.cond(q.jac));return dict(kind=kind,coefficients=q.x.tolist(),parameters=len(q.x),jacobian_condition=cond if np.isfinite(cond)else None,boundary_contacts=[bool(abs(p)>19.99)for p in q.x],fit_objective='squared capped-consumption residual with weak slope regularization; three deterministic starts selected by training MAE')
def evaluate(kind,d):
 frames=[];states={}
 for g in sorted(d.group.unique()):
  tr=d[d.group!=g];v=d[d.group==g];s=fit(kind,tr);s['training_groups']=sorted(tr.group.unique());s['training_rows']=len(tr);states[g]=s
  z=v[['sample_id','group','target','formulation','nodes','max_degree']].copy();z['prediction']=r.predict(s,v);frames.append(z)
 p=pd.concat(frames);p['error']=p.prediction-p.target;ge=p.groupby('group').error.agg(lambda a:float(abs(a).mean()));reg=[]
 for g,z in p.groupby('group'):
  chosen=z.sort_values(['prediction','formulation']).iloc[0];reg.append(float(chosen.target-z.target.min()))
 state=fit(kind,d);state['training_groups']=sorted(d.group.unique());state['training_rows']=len(d)
 return p,dict(primary_error=float(ge.mean()),worst_group=float(ge.max()),by_group=ge.to_dict(),formulation_bias=p.groupby('formulation').error.mean().to_dict(),offline_selection_regret_mean=float(np.mean(reg)),fold_states=states),state
def main():
 d=prepare(D);d=d[d.partition=='development'].copy()
 if sys.argv[1]=='baselines':jobs=[(k,W/'baselines'/k)for k in ['constant','form_median','exp_size','rbf']]
 else:
  p=W/'attempts'/('attempt-'+sys.argv[1]);jobs=[(json.loads((p/'config.json').read_text())['kind'],p)]
 for kind,p in jobs:
  p.mkdir(parents=True,exist_ok=True);pred,m,s=evaluate(kind,d);pred.to_csv(p/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});save(p/'metrics.json',m);save(p/'model.json',s);save(p/'execution.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_sha256':hashlib.sha256((W/'PROTOCOL.json').read_bytes()).hexdigest(),'confirmation_used_for_fitting':False,'training_groups':sorted(d.group.unique()),'training_rows':len(d)});print(kind,m['primary_error'],'worst',m['worst_group'],'selectionregret',m['offline_selection_regret_mean'],flush=True)
if __name__=='__main__':main()
