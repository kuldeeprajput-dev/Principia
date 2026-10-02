from pathlib import Path
import json,sys,hashlib,datetime,importlib.util
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from native import prepare
W=Path(__file__).resolve().parent;D=W.parents[3].parent/'local-datas'
sp=importlib.util.spec_from_file_location('frozen',W/'package/run.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
def save(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,indent=2,allow_nan=False)+'\n')
def rbf_fit(d,length,ridge):
 y=d.target.to_numpy(float);weight=(1/d.groupby('group').group.transform('size').to_numpy(float))**.5;X=r.features(d);mean=X.mean(0);scale=np.maximum(X.std(0),1e-6);X=(X-mean)/scale
 ix=np.linspace(0,len(d)-1,min(32,len(d)),dtype=int);centers=X[ix];F=np.c_[np.ones(len(X)),np.exp(-((X[:,None,:]-centers[None,:,:])**2).sum(2)/(2*length**2))]
 A=F*weight[:,None];z=(y-d.anchor_loss.to_numpy(float))*weight;coef=np.linalg.solve(A.T@A+ridge*np.eye(F.shape[1]),A.T@z)
 return dict(kind='rbf',coefficients=coef.tolist(),mean=mean.tolist(),scale=scale.tolist(),centers=centers.tolist(),length=length,ridge=ridge,parameters=len(coef))
def fit(kind,d):
 y=d.target.to_numpy(float);weight=(1/d.groupby('group').group.transform('size').to_numpy(float))**.5
 if kind in ['persist','log_tangent']:return dict(kind=kind,parameters=0)
 if kind=='rbf':
  candidates=[]
  for length in [1.,2.,4.]:
   for ridge in [.03,.3]:
    errors=[]
    for group in sorted(d.group.unique()):
     tr=d[d.group!=group];v=d[d.group==group];state=rbf_fit(tr,length,ridge);errors.append(float(abs(r.predict(state,v)-v.target).mean()))
    candidates.append([float(np.mean(errors)),length,ridge])
  _,length,ridge=min(candidates);state=rbf_fit(d,length,ridge);state['inner_cv']=candidates;return state
 specs={'bounded_size':([.2,.6,.1],[.005,0,.01],[2,2,5]),'balanced_geometry':([-.5,0,0],[-5,-2,-2],[1.1,2,2]),'power':([.3],[.005],[3.]),'aspect_power':([np.log(.3),0],[-5,-2],[1.1,2]),'scale_power':([np.log(.3),0],[-5,-2],[1.1,2]),'aspect_scale':([np.log(.3),0,0],[-5,-2,-2],[1.1,2,2]),'shrunk_power':([.3,1],[.005,0],[3,2]),'two_rate':([.05,.7,.5],[.005,.4,0],[.4,3,1])}
 x0,lo,hi=specs[kind]
 def f(p):return (r.predict(dict(kind=kind,coefficients=p),d)-y)*weight
 fit=least_squares(f,x0,bounds=(lo,hi),max_nfev=3000,xtol=1e-10,ftol=1e-10,gtol=1e-10)
 return dict(kind=kind,coefficients=fit.x.tolist(),parameters=len(fit.x),jacobian_condition=float(np.linalg.cond(fit.jac)),boundary_contacts=[bool(np.isclose(p,l,atol=1e-5)or np.isclose(p,h,atol=1e-5))for p,l,h in zip(fit.x,lo,hi)],fit_objective='equal-architecture weighted squared error; model selection by MAE')
def evaluate(kind,d):
 rows=[];states={}
 for g in sorted(d.group.unique()):
  tr=d[d.group!=g];v=d[d.group==g];s=fit(kind,tr);s['training_groups']=sorted(tr.group.unique());s['training_rows']=len(tr);states[g]=s;v=v[['sample_id','group','target','tokens_B','params_B','width','depth']].copy();v['prediction']=r.predict(s,d[d.group==g]);rows.append(v)
 p=pd.concat(rows).sort_values('sample_id');p['error']=p.prediction-p.target;ge=p.groupby('group').error.agg(lambda a:float(abs(a).mean()));late=p[p.tokens_B>60].groupby('group').error.agg(lambda a:float(abs(a).mean()))
 s=fit(kind,d);s['training_groups']=sorted(d.group.unique());s['training_rows']=len(d)
 return p,dict(primary_error=float(ge.mean()),worst_group=float(ge.max()),late_horizon_mae=float(late.mean()),by_group=ge.to_dict(),bias_by_group=p.groupby('group').error.mean().to_dict(),fold_states=states),s
def main():
 d=prepare(D);d=d[d.partition=='development'].copy()
 if sys.argv[1]=='rbf':jobs=[('rbf',W/'baselines/rbf')]
 elif sys.argv[1]=='baselines':jobs=[(k,W/'baselines'/k)for k in ['persist','log_tangent','power','rbf']]
 else:
  dest=W/'attempts'/('attempt-'+sys.argv[1]);cfg=json.loads((dest/'config.json').read_text());jobs=[(cfg['kind'],dest)]
 for k,dest in jobs:
  dest.mkdir(parents=True,exist_ok=True);p,m,s=evaluate(k,d);p.to_csv(dest/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});save(dest/'metrics.json',m);save(dest/'model.json',s);save(dest/'execution.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_sha256':hashlib.sha256((W/'PROTOCOL.json').read_bytes()).hexdigest(),'confirmation_used_for_fitting':False,'training_groups':sorted(d.group.unique()),'training_rows':len(d)});print(k, 'MAE',m['primary_error'],'late',m['late_horizon_mae'],'worst',m['worst_group'],'state',{k:v for k,v in s.items()if k in ['coefficients','jacobian_condition','boundary_contacts']},flush=True)
if __name__=='__main__':main()
