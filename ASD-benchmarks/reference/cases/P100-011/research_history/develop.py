from pathlib import Path
import json,sys,hashlib,datetime,importlib.util,time
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from native import prepare,INPUTS
C=Path(__file__).resolve().parent;N=int(C.name[-3:]);sp=importlib.util.spec_from_file_location('frozen',C/'package/run.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
def weights(d):return np.sqrt(1/d.groupby('group').group.transform('size').to_numpy(float))
def fit(kind,d):
 s={'case':N,'kind':kind,'training_groups':sorted(d.group.unique()),'training_rows':len(d),'parameters':0,'equation':'See executable predict in run.py and parameter state; no target lookup.'}
 if N in[1,5]or(N==98 and kind in['generic','qhull','polar','star']):s['training_groups']=[];s['training_rows']=0;return s
 y=d.target.to_numpy(float);w=weights(d)
 if N==98:
  ix={'ties':[0,1],'rank':[0,2],'interactions':[0,1,2,3]}[kind];X=np.array([r.metric_features(v)[ix]for v in d.metric_json]);coef=np.linalg.lstsq(X*w[:,None],y*w,rcond=None)[0];s.update(coefficients=coef.tolist(),feature_indices=ix,parameters=len(coef));return s
 if kind in['persist','offline','background','background_ratio','median4','recoil_identity','cgl','adiabatic']:return s
 if kind=='constant':s.update(coefficients=[float(np.median(y))],parameters=1);return s
 if kind=='rbf':
  X=r.features(N,'all',d)
  if N==11:
   s['feature_categories']=sorted(d.workload.astype(str).unique());s['precision_categories']=sorted(d.precision.astype(str).unique());X=np.c_[X,*[(d.workload.astype(str)==cat).to_numpy(float)for cat in s['feature_categories']],*[(d.precision.astype(str)==cat).to_numpy(float)for cat in s['precision_categories']]]
  mean=X.mean(0);scale=np.maximum(X.std(0),1e-9);X=(X-mean)/scale;centers=X[np.linspace(0,len(X)-1,min(24,len(X)),dtype=int)];F=np.c_[np.ones(len(X)),np.exp(-((X[:,None,:]-centers[None,:,:])**2).sum(2)/8)];A=F*w[:,None];target=y-r.base(N,d)if N in[2,3,4,45]else np.log(np.maximum(y,1e-10)/r.base(N,d));coef=np.linalg.solve(A.T@A+.3*np.eye(F.shape[1]),A.T@(target*w));s.update(coefficients=coef.tolist(),mean=mean.tolist(),scale=scale.tolist(),centers=centers.tolist(),length=2.,ridge=.3,parameters=len(coef));return s
 if N in[2,3]:
  X=r.features(N,kind,d);A=X*w[:,None];z=(y-r.base(N,d))*w;coef=np.linalg.lstsq(A,z,rcond=None)[0];s.update(coefficients=coef.tolist(),parameters=len(coef),jacobian_condition=float(np.linalg.cond(A)));return s
 if N==4:
  configs={'rayleigh':([2.],[0.],[20.]),'recoil_gain':([.7],[0.],[3.]),'quadrature':([.7,1.,1.],[0.,0.,0.],[3.,30.,100.]),'rician':([.7,1.,2.],[0.,0.,.01],[3.,30.,100.]),'subsystems':([.7,1.,1.,2.],[0.,0.,0.,.01],[3.,30.,30.,100.]),'acceptance':([.7,1.,2.,0.,0.],[0.,0.,.01,0.,0.],[3.,30.,100.,5.,5.])};x0,lo,hi=configs[kind]
 elif N==11:
  cats=sorted(d.workload.unique());s['categories']=cats;s['fallback']=0.;k=len(cats)
  if kind=='utilization':x0=[2.];lo=[-8.];hi=[8.]
  else:
   x0=[2.]*k;lo=[-8.]*k;hi=[8.]*k
   if kind in['parallel','precision','saturating']:x0+=[0.];lo+=[-3.];hi+=[3.]
   if kind=='fixed_overhead':x0+=[-4.];lo+=[-10.];hi+=[3.]
 elif N==45:
  configs={'linear_hardness':([.3],[0.],[5.]),'saturation':([.3,1e4],[0.,10.],[5.,1e7]),'power_hardness':([.3,1.],[0.,.2],[5.,2.]),'hysteresis':([.3,0],[0.,-2.],[5.,2.]),'energy_response':([.3,0],[0.,-5.],[5.,5.]),'memory':([.3,0],[0.,0.],[5.,5.]),'decay_hardness':([.3,0],[0.,-3.],[5.,3.])};x0,lo,hi=configs[kind]
 elif N==46:
  configs={'density':([.66],[-3.],[3.]),'field':([1.],[-3.],[3.]),'polytropic':([.5,.5],[-3.,-3.],[3.,3.]),'relaxation':([.5,.5,0],[-3.,-3.,-2.],[3.,3.,2.]),'beta_regime':([.5,.5,0],[-3.,-3.,-3.],[3.,3.,3.]),'saturation':([.5,.5],[-3.,-3.],[3.,3.])};x0,lo,hi=configs[kind]
 else:raise ValueError('Unknown fit')
 scale=max(float(np.median(abs(y))),1e-8)
 def residual(p):return (r.predict(dict(s,coefficients=p),d)-y)*w/scale
 opt=least_squares(residual,x0,bounds=(lo,hi),max_nfev=350,xtol=1e-9,ftol=1e-9,gtol=1e-9)
 s.update(coefficients=opt.x.tolist(),parameters=len(opt.x),fit_objective='equal-group weighted least squares; development selection by MAE',jacobian_condition=float(np.linalg.cond(opt.jac)),optimizer_success=bool(opt.success),boundary_contacts=[bool(np.isclose(p,l,atol=1e-4)or np.isclose(p,h,atol=1e-4))for p,l,h in zip(opt.x,lo,hi)])
 if N==11 and kind!='utilization':s['fallback']=float(np.median(opt.x[:len(s['categories'])]))
 return s

def folds(d):
 if N in[3,46]:
  for block in sorted(d.block.unique())[2:]:yield str(block),d[d.block<block],d[d.block==block]
 elif N in[1,5,11,98]:
  for f in sorted(d.fold.unique()):yield str(f),d[d.fold!=f],d[d.fold==f]
 else:
  for g in sorted(d.group.unique()):yield g,d[d.group!=g],d[d.group==g]

def evaluate(kind,d):
 parts=[];states={};start=time.perf_counter()
 if N in[1,5]or(N==98 and kind in['generic','qhull','polar','star']):
  state=fit(kind,d);pred=r.predict(state,d);p=d[['sample_id','group','target']].copy();p['prediction']=pred;parts=[p];states={'deterministic':state}
 else:
  for name,tr,val in folds(d):
   state=fit(kind,tr);p=val[['sample_id','group','target']].copy();p['prediction']=r.predict(state,val);p['fold']=name;parts.append(p);states[name]=state
 p=pd.concat(parts).sort_values('sample_id');p['error']=p.prediction-p.target;g=p.groupby('group').error.agg(lambda a:float(abs(a).mean()));s=fit(kind,d)
 return p,{'primary_error':float(g.mean()),'worst_group':float(g.max()),'by_group':g.to_dict(),'bias_by_group':p.groupby('group').error.mean().to_dict(),'rmse_by_group':p.groupby('group').error.agg(lambda a:float(np.sqrt(np.mean(a*a)))).to_dict(),'exact_fraction':float((abs(p.error)<1e-8).mean())if N in[1,5,98]else None,'fold_states':states,'development_seconds':time.perf_counter()-start},s

def main():
 data_root=Path(sys.argv[1]);dest=C/sys.argv[2];cfg=json.loads((dest/'config.json').read_text());d=prepare(data_root);d=d[d.partition=='development'].copy()
 if (dest/'metrics.json').exists():raise ValueError('Refuse overwrite completed attempt')
 p,m,s=evaluate(cfg['kind'],d);p.to_csv(dest/'predictions.csv.gz',index=False,float_format='%.17g',compression={'method':'gzip','mtime':0});save(dest/'metrics.json',m);save(dest/'model.json',s);save(dest/'execution.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_sha256':hashlib.sha256((C/'PROTOCOL.json').read_bytes()).hexdigest(),'config_sha256':hashlib.sha256((dest/'config.json').read_bytes()).hexdigest(),'development_only':True,'rows':len(d),'groups':d.group.nunique(),'confirmation_metrics_revealed':False});print(N,cfg['kind'],'MAE',m['primary_error'],'worst',m['worst_group'],'params',s.get('coefficients'),flush=True)
if __name__=='__main__':main()
