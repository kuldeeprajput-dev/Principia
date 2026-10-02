"""Development-only fits. Run with --kind/--hypothesis to prerecord a new scientific attempt."""
from pathlib import Path
import sys,json,hashlib,datetime,argparse
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from run import predict,design
ROOT=Path(__file__).resolve().parent

def cfg(kind):
 # initialization and numerical bounds; all models fit only development partitions.
 if kind.startswith('flex') or kind in ['constant','cat_hold','cat_linear','trib_linearlog','mag_johnson']:return [],[],[]
 if kind=='atom_domain':return [0,.3,.025,.15,-.04,6,2],[-10,-2,-2,-4,-4,.1,0],[10,2,2,4,4,60,30]
 if kind=='atom_saturatingline':return [0,.3,.1,.3,1.5,6,2,2,2],[-10,-2,-2,-4,.1,.1,0,.1,.1],[10,2,4,4,8,60,30,50,50]
 if kind.startswith('atom_'):
  a=[0,.3,.01,.3,3,12,3,4,1,1,2];lo=[-10,-2,-.5,0,.1,.1,0,.1,0,0,.1];hi=[10,2,.5,5,50,70,20,40,20,5,20]
  if kind in ['atom_asym','atom_saturate','atom_quadbg']:a+=[0];lo+=[-.5];hi+=[.5]
  return a,lo,hi
 if kind=='mem_shared':return [1150,.6,-.2,.08],[100,.05,-.9,.002],[1800,1,.9,1]
 if kind.startswith('mem'):
  a=[1150,.6,.08,1150,.4,.08];lo=[100,.05,.002]*2;hi=[1800,1,1]*2
  if kind in ['mem_weibull','mem_hazard']:
   a=[1150,.6,4,1150,.4,4];lo=[100,.01,.1]*2;hi=[1800,2,40]*2
  if kind in ['mem_leak','mem_sclc','mem_voltage','mem_hazard']:
   a=[*a[:3],0 if kind=='mem_hazard' else 1,*a[3:],0 if kind=='mem_hazard' else 1];lo=[*lo[:3],-.3 if kind=='mem_hazard' else -100,*lo[3:],-.3 if kind=='mem_hazard' else -100];hi=[*hi[:3],.4 if kind=='mem_hazard' else 10000,*hi[3:],.4 if kind=='mem_hazard' else 10000]
  return a,lo,hi
 if kind in ['cat_relax','cat_log','cat_rational']:return [300],[1],[20000]
 if kind=='cat_loading':return [300,0],[1,-2],[20000,2]
 if kind=='cat_equilibrium':return [20,15,400],[-100,-100,1],[200,100,20000]
 if kind=='cat_twochannel':return [300,0,2000],[1,-100,1],[20000,100,20000]
 if kind=='cat_shrink':return [300,1],[1,0],[20000,5]
 if kind=='cat_power':return [300,1,1],[1,0,.2],[20000,5,4]
 if kind.startswith('trib'):
  a=[1,1];lo=[.01,.1];hi=[500,8]
  if kind=='trib_sqrt':return [1],[.01],[500]
  if kind=='trib_concentration':a+=[0];lo+=[-5];hi+=[5]
  if kind=='trib_drag':a+=[0];lo+=[-.05];hi+=[.05]
  if kind=='trib_bump':a+=[0,2];lo+=[-1,.2];hi+=[1,20]
  return a,lo,hi
 if kind.startswith('mag'):
  a=[7,33,.006,.212,.03,.03];lo=[6.98,10,.001,.1,0,0];hi=[7.02,60,.04,.3,.1,.15]
  if kind=='mag_kittel':a+=[.1695];lo+=[.16];hi+=[.18]
  if kind in ['mag_asym','mag_field','mag_tempwidth','mag_thermalnonlinear','mag_absorption']:a+=[0];lo+=[-2];hi+=[2]
  if kind=='mag_bg':a+=[0,0];lo+=[-1,-5];hi+=[1,5]
  return a,lo,hi
 if kind=='laser_domain':return [-3,0],[-12,-12],[6,10]
 if kind=='laser_twoflicker':return [-3,0,-2],[-12,-12,-12],[6,10,10]
 if kind.startswith('laser'):
  a=[-3,0,2];lo=[-12,-12,.1];hi=[6,10,6]
  if kind=='laser_rolloff':a+=[20];lo+=[.01];hi+=[1e5]
  if kind=='laser_sharedfloor':a+=[-2];lo+=[-12];hi+=[6]
  if kind=='laser_feedback':a+=[1];lo+=[0];hi+=[4]
  if kind=='laser_crossover':a+=[10];lo+=[.01];hi+=[1e5]
  if kind=='laser_cavity':a+=[10,100];lo+=[.01,.01];hi+=[1e5,1e5]
  return a,lo,hi
 raise ValueError(kind)

def fit(kind,d):
 y=d.target.to_numpy();weight=1/d.groupby('group').group.transform('size').to_numpy();weight=weight/weight.mean();x0,lo,hi=cfg(kind);state={'kind':kind,'parameters':[],'training_groups':sorted(d.group.unique()),'training_rows':len(d)}
 if kind=='constant':state['parameters']=[float(np.average(y,weights=weight))];return state
 if kind.startswith('flex'):
  A=design(kind,d);B=A*np.sqrt(weight)[:,None];Y=y*np.sqrt(weight);scale=np.maximum(np.sqrt((B*B).mean(axis=0)),1e-10);B=B/scale;state['parameters']=(np.linalg.solve(B.T@B+np.eye(A.shape[1])*1e-3,B.T@Y)/scale).tolist();return state
 if not x0:return state
 scale=max(float(np.std(y)),1e-4)
 def residual(p):return (predict({'kind':kind,'parameters':p},d)-y)*np.sqrt(weight)/scale
 opt=least_squares(residual,x0,bounds=(lo,hi),max_nfev=180,ftol=1e-8,xtol=1e-8,gtol=1e-8)
 sv=np.linalg.svd(opt.jac,compute_uv=False);state.update(parameters=opt.x.tolist(),optimizer_success=bool(opt.success),nfev=int(opt.nfev),jacobian_condition=float(sv[0]/max(sv[-1],1e-15)),bounds=[lo,hi],training_residual_rms=float(np.sqrt(np.mean(opt.fun**2))))
 return state

def score(d,y):
 e=abs(np.asarray(y)-d.target.to_numpy());g=pd.DataFrame({'group':d.group.to_numpy(),'error':e}).groupby('group').error.mean();return {'primary_error':float(g.mean()),'worst_group_error':float(g.max()),'groups':len(g),'rows':len(d),'by_group':g.to_dict()}

def main():
 a=argparse.ArgumentParser();a.add_argument('--kind',required=True);a.add_argument('--hypothesis',required=True);a.add_argument('--baseline',action='store_true');args=a.parse_args();p=ROOT;d=pd.read_csv(p/'development.csv.gz');case=int(json.loads((p/'PROTOCOL.json').read_text())['case_id'][-3:]);prior=sorted((p/'attempts').glob('attempt-*')) if (p/'attempts').exists() else []
 if (p/'FREEZE.json').exists():raise ValueError('Scientific campaign frozen')
 path=p/('baselines/'+args.kind if args.baseline else 'attempts/attempt-'+f'{len(prior)+1:03d}');path.mkdir(parents=True,exist_ok=False)
 conf={'kind':args.kind,'hypothesis':args.hypothesis,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'initial_and_bounds':cfg(args.kind),'parent_attempt':prior[-1].name if prior and not args.baseline else None,'fit_rows':'development only','selection_metric':'mean complete group MAE'}
 (path/'config.json').write_text(json.dumps(conf,indent=2)+'\n');(path/'HYPOTHESIS.md').write_text('# Scientific hypothesis\n\n'+args.hypothesis+'\n\nFalsifier: failure to reduce matched grouped development error or unstable transfer/identifiability. Controls are constant, domain and constrained flexible models; no confirmation feedback is available.\n')
 folds=sorted(d.fold.unique()) if case in [22,65] else sorted(d.group.unique());out=[];states=[]
 for fold in folds:
  ix=d.fold==fold if case in [22,65] else d.group==fold;tr=d[~ix];va=d[ix];m=fit(args.kind,tr);q=va[['sample_id','group','target']].copy();q['prediction']=predict(m,va);q['fold']=fold;out.append(q);states.append({'fold':fold,'state':m})
 out=pd.concat(out).sort_values('sample_id');result=score(out,out.prediction);m=fit(args.kind,d)
 out.to_csv(path/'predictions.csv.gz',index=False);(path/'metrics.json').write_text(json.dumps(result,indent=2)+'\n');(path/'model.json').write_text(json.dumps(m,indent=2)+'\n');(path/'fold_models.json').write_text(json.dumps(states,indent=2)+'\n')
 (path/'REPORT.md').write_text('# Development result\n\n'+args.hypothesis+'\n\nWhole-group MAE: '+str(result['primary_error'])+'; worst group: '+str(result['worst_group_error'])+'. Numerical optimizer success: '+str(m.get('optimizer_success','closed form'))+'.\n\nParameter vector and bounds are in model.json; predictions are entirely out of fold. No causal mechanism or novelty is established by predictive fit.\n')
 print(json.dumps({'case':case,'attempt':path.name,'kind':args.kind,**result,'fit_nfev':m.get('nfev'),'jacobian_condition':m.get('jacobian_condition')},allow_nan=False),flush=True)
if __name__=='__main__':main()
