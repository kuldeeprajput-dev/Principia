from pathlib import Path
import sys,json,hashlib,datetime,importlib.util
import numpy as np,pandas as pd
from scipy.optimize import least_squares,linprog
from native import prepare
W=Path(__file__).resolve().parent;D=W.parents[3].parent/'local-datas'
spec=importlib.util.spec_from_file_location('frozen',W/'package/run.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
def save(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,allow_nan=False)+'\n')
def fit(kind,d):
 y=d.target.to_numpy(float)
 if kind=='rbf':
  settings=[]
  for length in [.1,.3,1.]:
   for ridge in [.01,.1,1.]:
    e=[]
    for g in sorted(d.group.unique()):
     tr=d[d.group!=g];v=d[d.group==g];s=rbf_fit(tr,length,ridge);e.append(np.abs(predict_state(s,v)-v.target).mean())
    settings.append((np.mean(e),length,ridge))
  _,length,ridge=min(settings);s=rbf_fit(d,length,ridge);s['inner_cv']=settings;return s
 if kind in ['queue','queue_deficit']:
  b=d.achieved_Mbps.to_numpy(float);a=d.offered_Mbps.to_numpy(float)
  def fun(p):return p[0]+p[1]*b+p[2]/(p[3]-b)+(p[4]*(a-b)/500 if kind=='queue_deficit' else 0)-y
  p0=[5,.03,1000,800]+([0] if kind=='queue_deficit' else []);lo=[0,0,0,600]+([-100] if kind=='queue_deficit' else []);hi=[100,1,50000,5000]+([100] if kind=='queue_deficit' else [])
  fits=[least_squares(fun,[*p0[:3],c,*p0[4:]],bounds=(lo,hi),loss='soft_l1',f_scale=1,max_nfev=20000) for c in [650,1000,3000]]
  best=min(fits,key=lambda f:np.mean(np.abs(fun(f.x))));return dict(kind=kind,coefficients=best.x.tolist(),fit_loss='soft-L1; deterministic3-start; minimumMAE',capacity_boundary=bool(best.x[3]<600.01 or best.x[3]>4999.99))
 X=r.features(kind,d);n,k=X.shape
 # Exact least absolute deviation; coefficients unconstrained, deployed prediction nonnegative.
 A=np.r_[np.c_[X,-np.eye(n)],np.c_[-X,-np.eye(n)]];bb=np.r_[y,-y]
 if kind=='monotone_cells':
  M=np.zeros((k-1,k+n))
  for j in range(k-1):M[j,j]=1;M[j,j+1]=-1
  A=np.r_[A,M];bb=np.r_[bb,np.zeros(k-1)]
 res=linprog(np.r_[np.zeros(k),np.ones(n)],A_ub=A,b_ub=bb,bounds=[(None,None)]*k+[(0,None)]*n,method='highs')
 if not res.success:raise ValueError(res.message)
 return dict(kind=kind,coefficients=res.x[:k].tolist(),design_rank=int(np.linalg.matrix_rank(X)),condition_number=float(np.linalg.cond(X)),fit_loss='L1')
def rbf_fit(d,length,ridge):
 x=d[['offered_Mbps','achieved_Mbps']].to_numpy(float)/500;y=d.target.to_numpy(float);mu=float(y.mean());K=np.exp(-((x[:,None,:]-x[None,:,:])**2).sum(2)/(2*length**2));alpha=np.linalg.solve(K+ridge*np.eye(len(x)),y-mu)
 return dict(kind='rbf',length=length,ridge=ridge,centers=x.tolist(),mean=mu,alpha=alpha.tolist())
def predict_state(s,d):
 k=s['kind']
 if k in ['queue','queue_deficit']:
  b=d.achieved_Mbps.to_numpy(float);a=d.offered_Mbps.to_numpy(float);p=s['coefficients'];y=p[0]+p[1]*b+p[2]/(p[3]-b)+(p[4]*(a-b)/500 if k=='queue_deficit' else 0)
 elif k=='rbf':
  x=d[['offered_Mbps','achieved_Mbps']].to_numpy(float)/500;c=np.array(s['centers']);y=s['mean']+np.exp(-((x[:,None,:]-c[None,:,:])**2).sum(2)/(2*s['length']**2))@np.array(s['alpha'])
 else:y=r.features(k,d)@np.array(s['coefficients'])
 return np.maximum(y,0)
def evaluate(kind,d):
 rows=[];states={}
 for g in sorted(d.group.unique()):
  tr=d[d.group!=g];v=d[d.group==g];s=fit(kind,tr);states[g]=s;v=v[['sample_id','group','offered_Mbps','achieved_Mbps','target']].copy();v['prediction']=predict_state(s,v);rows.append(v)
 out=pd.concat(rows);out['error']=out.prediction-out.target;ge=out.groupby('group').error.agg(lambda x:float(np.abs(x).mean()))
 return out,dict(primary_error=float(ge.mean()),worst_group=float(ge.max()),by_group=ge.to_dict(),bias_by_rate=out.groupby('offered_Mbps').error.mean().to_dict(),fold_states=states),fit(kind,d)
def main():
 d=prepare(D);d=d[(d.partition=='development')&d.target.notna()].copy()
 if sys.argv[1]=='baselines':
  for k in ['constant','offered','achieved','queue','rbf']:
   p,m,s=evaluate(k,d);dest=W/'baselines'/k;dest.mkdir(parents=True,exist_ok=True);p.to_csv(dest/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});save(dest/'metrics.json',m);save(dest/'model.json',s);print(k,m['primary_error'],m['worst_group'])
 else:
  attempt=sys.argv[1];dest=W/'attempts'/('attempt-'+attempt);config=json.loads((dest/'config.json').read_text());kind=config['kind'];p,m,s=evaluate(kind,d);p.to_csv(dest/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});save(dest/'metrics.json',m);save(dest/'model.json',s);save(dest/'execution.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'development_groups':sorted(d.group.unique()),'development_rows':len(d),'protocol_sha256':hashlib.sha256((W/'PROTOCOL.json').read_bytes()).hexdigest(),'config_sha256':hashlib.sha256((dest/'config.json').read_bytes()).hexdigest(),'confirmation_read_for_fitting':False});print(json.dumps({k:v for k,v in m.items() if k!='fold_states'},indent=2))
if __name__=='__main__':main()
