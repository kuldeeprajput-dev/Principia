from pathlib import Path
import sys,json,datetime,hashlib,importlib.util
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
from run import predict
ROOT=Path(__file__).parent.parent
# Fixed starts and bounds: tuning is not performed on validation outcomes.
SPECS={
'cure_first':([80,-4],[10,-15],[200,5]),'cure_logistic':([420,12,3],[300,0,0],[550,50,5]),'cure_nth':([80,-4,2],[10,-15,1.01],[200,5,8]),'cure_avrami':([80,-4,.7],[10,-15,.15],[200,5,4]),'cure_parallel':([70,-3,130,-6,.5],[10,-15,10,-15,.01],[200,5,200,5,.99]),'cure_shared':([80,-3,-3,.5],[10,-15,-10,.01],[200,5,5,.99]),'cure_plateau':([80,-4,.7,1],[10,-15,.15,.5],[200,5,4,1.05]),'cure_shift':([80,-4,.7,0],[10,-15,.15,-1],[200,5,4,1]),'cure_logistic_dose':([80,-4,.8,2],[10,-15,.15,.1],[200,5,4,10]),
'beam_rational':([30],[.1],[500]),'beam_cap':([60],[10],[150]),'beam_softening':([.02],[0],[.2]),'beam_material_cap':([60,0],[10,-50],[150,50]),'beam_bilinear':([60,0,.1],[10,-50,-.5],[150,50,1]),'beam_recent':([30],[.1],[500]),'beam_power':([30,1],[.1,.1],[500,5]),
'fracture_lefm':([1],[.01],[5]),'fracture_bridge':([1,2],[0,-10],[5,30]),'fracture_power':([1,2],[.01,-5],[5,20]),'fracture_interaction':([1,2,0],[0,-30,-30],[5,30,30]),'fracture_notch':([1,0],[0,-10],[5,10]),'fracture_regime':([1,.5,.2,.02],[0,-2,0,-.3],[5,5,2,.5]),'fracture_netligament':([1,2],[0,-30],[5,30]),'fracture_sqrt':([1,2],[0,-10],[5,20])}
EQUATIONS={'mean':'y=training-group-balanced mean(y)','cure_first':'alpha=1-exp(-q), q=k_ref/beta integral_273.15^T exp[E/R(1/423.15-1/u)]du','cure_nth':'alpha=1-[1+(n-1)q]^[-1/(n-1)]','cure_avrami':'alpha=1-exp(-q^m)','cure_parallel':'alpha=w(1-exp(-q1))+(1-w)(1-exp(-q2))','cure_shared':'alpha=w(1-exp(-q))+(1-w)(1-exp(-exp(c)q))','cure_plateau':'alpha=A_inf(1-exp(-q^m))','cure_shift':'alpha=1-exp[-(q(beta/3)^c)^m]','cure_logistic_dose':'alpha=1-(1+q^m)^(-n)','cure_logistic':'alpha=logistic[(T-T0-c log(beta))/exp(s)]','beam_elastic':'F=F0+k0(d-d0)','beam_hold':'F=F0','beam_rational':'F=F0+k0 u/(1+u/L), u=d-d0','beam_cap':'F=min(F0+k0 u,C)','beam_softening':'F=(F0+k0 u)exp(-h u)','beam_material_cap':'F=min(F0+k0 u,C0+C1 lightweight)','beam_bilinear':'F=min(F0+k0 u,C)+h max(F0+k0 u-C,0), C=C0+C1 lightweight','beam_recent':'F=F0+max(k_recent,0)u/(1+u/L)','beam_power':'F=F0+k0 u/[1+(u/L)^p]','beam_flexible':'F=dot(theta,[1,F0,k0u,z^2,m,mz,mz^2]), z=u/20','fracture_lefm':'P=s K, s=B W^(3/2)/(L f(a/W)); f(x)=1.46+24.36x-47.21x²+75.18x³','fracture_bridge':'P=s(K+c r), r=1-b/B','fracture_power':'P=s K(1+r)^c','fracture_interaction':'P=s(K+c r+d r/(a/W))','fracture_notch':'P=s(K+c a/W)','fracture_regime':'P=s(K+c logistic[(r-h a/W-v)/0.02])','fracture_netligament':'P=s(K+c r/(1-a/W))','fracture_sqrt':'P=s(K+c sqrt(r))','fracture_flexible':'P=s dot(theta,[1,a/W,r,(a/W)^2,r²,(a/W)r])'}
def fit(kind,x):
 groups=x.groupby('group').size();weights=np.sqrt(x.group.map(1/groups).to_numpy());y=x.target.to_numpy()
 if kind=='mean':p=[float(x.groupby('group').target.mean().mean())];diag={}
 elif kind in ['beam_elastic','beam_hold']:p=[];diag={}
 elif kind in ['beam_flexible','fracture_flexible']:
  n=7 if kind=='beam_flexible' else 6;A=np.column_stack([predict({'kind':kind,'parameters':np.eye(n)[i].tolist()},x) for i in range(n)]);scale=np.sqrt(np.mean(A*A,axis=0));scale=np.where(scale>0,scale,1);Z=A/scale;Aw=Z*weights[:,None];yw=y*weights;p=(np.linalg.solve(Aw.T@Aw+np.eye(n)*.1,Aw.T@yw)/scale).tolist();diag={'fixed_ridge_penalty':.1,'feature_scale':scale.tolist()}
 else:
  init,lo,hi=SPECS[kind];init=np.array(init,float);starts=[init]
  if kind.startswith('cure_') and kind!='cure_logistic':starts+=[np.array([50 if j==0 else v for j,v in enumerate(init)]),np.array([120 if j==0 else v for j,v in enumerate(init)])]
  results=[]
  for start in starts:
   f=least_squares(lambda p:(predict({'kind':kind,'parameters':p},x)-y)*weights,start,bounds=(lo,hi),x_scale='jac',max_nfev=2000,ftol=1e-9,xtol=1e-9,gtol=1e-9)
   results.append(f)
  best=min(results,key=lambda a:a.cost);p=best.x.tolist();sv=np.linalg.svd(best.jac,compute_uv=False);diag={'optimizer_success':bool(best.success),'nfev':int(best.nfev),'cost':float(best.cost),'jacobian_condition':float(sv[0]/max(sv[-1],1e-15)),'near_bound_parameters':[i for i,v in enumerate(p) if min(abs(v-lo[i]),abs(hi[i]-v))<1e-5]}
 return {'kind':kind,'parameters':p,'equation':EQUATIONS[kind],'training_groups':sorted(x.group.unique()),'training_sample_ids':x.sample_id.tolist(),'fit_diagnostics':diag}
def main():
 import argparse
 p=argparse.ArgumentParser();p.add_argument('label');p.add_argument('kind');p.add_argument('--reason',required=True);a=p.parse_args();folder=ROOT/('baselines' if a.label.startswith('baseline') else 'attempts')/a.label
 if folder.exists():raise RuntimeError('Existing attempt immutable; choose repair workflow')
 folder.mkdir(parents=True);conf={'kind':a.kind,'hypothesis':a.reason,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.json').read_bytes()).hexdigest(),'parent_attempts':sorted(v.name for v in (ROOT/'attempts').glob('attempt-*')) if (ROOT/'attempts').exists() else []}
 (folder/'config.json').write_text(json.dumps(conf,indent=2));(folder/'HYPOTHESIS.md').write_text('# Hypothesis\n\n'+a.reason+'\n\nCandidate: '+EQUATIONS[a.kind]+'\n\nFalsifier: no improvement under complete-unit development validation; boundary estimates or opposing fold effects limit mechanism.\n')
 x=pd.read_csv(ROOT/'development.csv.gz',dtype={'sample_id':str,'group':str});folds=x['family'] if 'family' in x else x.group;pred=x[['sample_id','group','target']].copy();pred['prediction']=np.nan;pred['fold']=folds
 states={}
 for f in sorted(folds.unique()):
  tr=x[folds!=f];te=x[folds==f];m=fit(a.kind,tr);pred.loc[te.index,'prediction']=predict(m,te);states[str(f)]=m
 pred['absolute_error']=abs(pred.prediction-pred.target);g=pred.groupby('group').absolute_error.mean();metrics={'primary_error':float(g.mean()),'worst_group_error':float(g.max()),'median_group_error':float(g.median()),'groups':len(g),'rows':len(pred),'by_group':g.to_dict(),'by_fold':pred.groupby('fold').absolute_error.mean().to_dict()};model=fit(a.kind,x)
 (folder/'model.json').write_text(json.dumps(model,indent=2));(folder/'fold_states.json').write_text(json.dumps(states,indent=2));(folder/'metrics.json').write_text(json.dumps(metrics,indent=2));pred.to_csv(folder/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0})
 (folder/'REPORT.md').write_text('# Development result\n\n'+a.reason+'\n\nGrouped MAE: '+str(metrics['primary_error'])+'; worst group: '+str(metrics['worst_group_error'])+'.\n\nComplete folds and residuals are in metrics.json/predictions.csv.gz. States contain exact parameters and training identities. No confirmation targets or metrics read. Physical dimensional consistency follows input units and the declared equation. Identifiability diagnostics are model.json; prediction support does not establish mechanism.\n')
 print(json.dumps({'label':a.label,'kind':a.kind,**metrics,'parameters':model['parameters'],'diagnostics':model['fit_diagnostics']}))
if __name__=='__main__':main()
