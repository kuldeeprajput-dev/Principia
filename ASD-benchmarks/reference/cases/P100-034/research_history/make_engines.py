from pathlib import Path
W=Path(__file__).resolve().parents[1]
run='''"""Standalone frozen equations; prediction reads declared inputs only."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def features(c,k,d):
 one=np.ones(len(d))
 if c==29:
  q=d.dose/d.dose_cal;A=d.F5-d.F0;X=[one,d.F0,d.F5,d.F2,d.F1,A*np.log(q),A*(1-1/q),d.dye_NR*A,np.log(q)*d.dye_NR*A]
 elif c==32:
  v=d.p0-d.p20;acc=d.p0-2*d.p20+d.p40;flow=d.di0-d.de0
  if k=='periodic':X=[v,acc]
  elif k=='flow':X=[v,flow,d.di0-d.di20,d.de0-d.de20]
  elif k=='regime':X=[v,acc,flow,v*(flow>0),v*d.trial_FEM,v*d.trial_BH]
  elif k=='shutter':X=[v,acc,d.p0-d.p10,d.p10-d.p30,(d.p0-d.p05)-(d.p20-d.p30),v*d.trial_FEM]
  else:X=[one]+[d[x] for x in ['p0','p05','p10','p20','p30','p40','p50','di0','de0','di20','de20']]+[d.p0*d.trial_FEM,d.p0*d.trial_BH]
 elif c==34:
  x=d.calcium;v=d.low075;u=d.low04
  X=[one,v,u,np.log(x/.75)*v,(1-.75/x)*v,np.log(x/.75)*u,d.mutant*v,d.mutant*np.log(x/.75)*v]
 elif c==76:
  x=d.current/50;s=d.soft;k=d.kd;b=d.cal_last
  X=[one,x,x*x,s,k,s*k,x*s,x*k,x*s*k,b,b*x,d.cal_mean]
 elif c==79:
  x=np.log1p(d.hours/24);b=d.baseline
  X=[one,x,x*x,x*x*x,b,b*x,d.baseline_change,d.age/40]
 elif c==89:
  r=d.reward/2;p=d.probability;a=d.child;m=d.multi;v=d.description;h=d.history_mean-.5;l=d.lag_choice-.5;ev=r*p-1
  if k=='utility':X=[one,ev]
  elif k=='context':X=[one,ev,a,m,v,a*m,ev*a,ev*m]
  elif k=='memory':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,d.has_history*h]
  elif k=='description':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,(p-.5)*v,(p-.5)*a*v]
  elif k=='history_interaction':X=[one,ev,a,m,v,a*m,ev*a,ev*m,h,l,h*ev,h*m,h*a]
  else:X=[one,r,p,r*p,r*r,p*p,a,m,v,a*m,a*v,r*a,p*a,r*m,p*m,r*v,p*v,h,l,h*a,h*m,d.trial_progress]
 else:raise ValueError(c)
 return np.column_stack(X).astype(float)
def predict(m,d):
 c=m['case'];k=m['kind'];p=np.asarray(m.get('coef',[]));one=np.ones(len(d))
 if k=='mean':return one*m['mean']
 if c==29:
  x=d.dose.to_numpy();z=d.dose_cal.to_numpy();b=d.F0.to_numpy();A=(d.F5-d.F0).to_numpy()
  if k=='persistence':return d.F5.to_numpy()
  if k=='linear':return b+A*x/z
  if k=='langmuir':K=p[0];H=lambda q:q/(K+q)
  elif k=='hill':K,n=p;H=lambda q:q**n/(K**n+q**n)
  elif k=='two_site':K1,K2,w=p;H=lambda q:w*q/(K1+q)+(1-w)*q/(K2+q)
  elif k=='dye_hill':K=np.exp(p[0]+p[1]*d.dye_NR.to_numpy());n=p[2];H=lambda q:q**n/(K**n+q**n)
  elif k in ['local','shrink_local']:
   # Invert low-dose Langmuir ratio only from calibration, not future maximum.
   r=(d.F2-d.F0).to_numpy()/np.maximum(A,1e-8);x2=d.dose2.to_numpy();K=np.clip(x2*z*(1-r)/np.maximum(r*z-x2,1e-8),.01,1000)
   if k=='local':K=K*p[0]
   else:K=np.exp(p[0]*np.log(K)+(1-p[0])*np.log(p[1]))
   H=lambda q:q/(K+q)
  elif k=='threshold':n,K,lag=p;L=lag*z;H=lambda q:np.maximum(q-L,1e-8)**n/(K**n+np.maximum(q-L,1e-8)**n)
  elif k=='flexible':return np.maximum(0,features(c,k,d)@p)
  else:raise ValueError(k)
  return b+A*H(x)/np.maximum(H(z),1e-12)
 if c==32:
  if k=='persistence':return d.p0.to_numpy()
  if k=='tangent':return (d.p0+2*(d.p0-d.p10)).to_numpy()
  if k=='damped':return (d.p0+p[0]*(d.p0-d.p10)).to_numpy()
  if k=='limited':return (d.p0+p[0]*np.tanh((d.p0-d.p20)/p[1])*p[1]).to_numpy()
  if k in ['periodic','flow','regime','shutter']:return d.p0.to_numpy()+features(c,k,d)@p
  return features(c,k,d)@p
 if c==34:
  x=d.calcium.to_numpy();z=.75;v=d.low075.to_numpy();u=d.low04.to_numpy();g=d.mutant.to_numpy()
  if k=='persistence':return v
  if k=='hill4':K=p[0];n=4
  elif k=='genotype_hill':K=np.exp(p[0]+p[1]*g);n=p[2]
  elif k=='local_hill':
   n=p[0];r=np.clip(u/np.maximum(v,1e-8),1e-7,.99999);q=.4**n;s=z**n;K=np.maximum(q*s*(1-r)/np.maximum(r*s-q,1e-12),.000001)**(1/n)
  elif k=='two_pool':
   K1,K2,w=p;H=lambda t:w*t**4/(K1**4+t**4)+(1-w)*t**4/(K2**4+t**4);return v*H(x)/H(z)
  elif k=='genotype_exponent':K=np.exp(p[0]+p[1]*g);n=p[2]+p[3]*g
  elif k=='calibration_blend':
   K,n,w=p;H=lambda t:t**n/(K**n+t**n);glob=v*H(x)/H(z);slope=np.maximum(v-u,0)/.35;local=v+slope*K*(1-np.exp(-(x-z)/K));return (1-w)*glob+w*local
  elif k=='capacity':return np.maximum(0,v+p[0]*(1-np.exp(-(x-z)/p[1]))*(1+p[2]*g))
  elif k=='flexible':return np.maximum(0,features(c,k,d)@p)
  else:raise ValueError(k)
  H=lambda t:t**n/(K**n+t**n);return v*H(x)/H(z)
 if c==76:
  x=d.current.to_numpy();b=d.cal_last.to_numpy();s=d.soft.to_numpy();g=d.kd.to_numpy()
  if k=='persistence':return b
  if k=='rheobase':return np.maximum(0,p[0]*(x-p[1]))
  if k=='condition_threshold':return np.maximum(0,p[0]*(x-p[1]-p[2]*s-p[3]*g-p[4]*s*g))
  if k=='saturation':return b+p[0]*(1-np.exp(-np.maximum(x-10,0)/p[1]))
  if k=='recruitment':return np.maximum(0,(p[0]+p[1]*b+p[2]*d.cal_mean.to_numpy())*np.maximum(x-10,0))
  if k=='block':return b+p[0]*np.maximum(x-10,0)*np.exp(-np.maximum(x-p[1],0)/p[2])
  if k=='condition_gain':return b+np.maximum(0,p[0]+p[1]*s+p[2]*g+p[3]*s*g)*np.maximum(x-10,0)**p[4]
  if k=='calibrated_saturation':return b+(p[0]+p[1]*b)*(1-np.exp(-(x-10)/p[2]))
  if k=='flexible':return np.maximum(0,features(c,k,d)@p)
  raise ValueError(k)
 if c==79:
  t=d.hours.to_numpy();b=d.baseline.to_numpy();v=d.baseline_change.to_numpy()
  if k=='persistence':return b
  if k=='decay':return np.maximum(0,b+p[0]*np.exp(-t/p[1]))
  if k=='bateman':return np.maximum(0,b+p[0]*(np.exp(-t/p[1])-np.exp(-t/p[2])))
  if k=='relative_decay':return np.maximum(0,b+b*p[0]*np.exp(-t/p[1]))
  if k=='two_decay':return np.maximum(0,b+p[0]*np.exp(-t/p[1])+p[2]*np.exp(-t/p[3]))
  if k=='baseline_drift':return np.maximum(0,b+p[0]*np.exp(-t/p[1])+p[2]*v*np.exp(-t/24))
  if k=='lognormal':return np.maximum(0,b+p[0]*np.exp(-.5*(np.log(t/p[1])/p[2])**2))
  if k=='saturating_amplitude':return np.maximum(0,b+p[0]*b/(p[1]+np.maximum(b,0))*np.exp(-t/p[2]))
  if k=='flexible':return np.maximum(0,features(c,k,d)@p)
  raise ValueError(k)
 if c==89:
  if k=='persistence':return np.clip(d.history_mean.to_numpy(),.001,.999)
  if k=='prospect':
   alpha,gamma,beta,bias=p;r=d.reward.to_numpy()/2;prob=d.probability.to_numpy();w=prob**gamma/(prob**gamma+(1-prob)**gamma)**(1/gamma);return expit(beta*(w*r**alpha-1)+bias)
  return expit(features(c,k,d)@p)
 raise ValueError(c)
def main():
 here=Path(__file__).resolve().parent;manifest=json.loads((here/'MANIFEST.json').read_text())
 for a in manifest['assets']:
  p=here/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Integrity failure '+a['path'])
 r=json.loads((here/'rules.json').read_text());d=read_table(here/'data/inputs.csv.gz');saved=read_table(here/'evidence/predictions.csv.gz')
 for k,m in r['models'].items():
  q=predict(m,d)
  if not np.isfinite(q).all() or not np.allclose(q,saved[k],rtol=1e-10,atol=1e-9):raise ValueError('Replay mismatch '+k)
 print('All frozen models reproduce saved predictions',len(d))
if __name__=='__main__':main()
'''
fit='''from pathlib import Path
import json,hashlib
import numpy as np
from scipy.optimize import least_squares,minimize
from scipy.special import expit
from run import predict,features
BOUNDS={29:{'langmuir':([5],[.001],[1000]),'hill':([5,1],[.001,.1],[1000,4]),'local':([1],[.01],[100]),'two_site':([1,50,.5],[.001,.01,0],[1000,1000,1]),'dye_hill':([2,0,1],[-6,-6,.1],[8,6,4]),'threshold':([1,5,.2],[.1,.001,0],[4,1000,.95]),'shrink_local':([.5,5],[0,.001],[1,1000])},32:{'damped':([1],[-2],[3]),'limited':([1,2],[-2,.001],[4,50])},34:{'hill4':([1],[.01],[100]),'genotype_hill':([0,0,3],[-4,-4,.5],[5,4,6]),'local_hill':([3],[1],[6]),'two_pool':([.5,3,.5],[.01,.02,0],[100,100,1]),'genotype_exponent':([0,0,3,0],[-4,-4,1,-.9],[5,4,5,1]),'calibration_blend':([1,3,.5],[.01,.5,0],[100,6,1]),'capacity':([50000,1,0],[0,.01,-.95],[1e7,100,10])},76:{'rheobase':([.1,0],[0,-50],[10,100]),'condition_threshold':([.1,0,0,0,0],[0,-50,-100,-100,-100],[10,100,100,100,100]),'saturation':([10,40],[0,.1],[200,1000]),'recruitment':([.1,.01,.01],[0,0,0],[10,10,10]),'block':([.2,50,40],[0,10,.1],[10,100,1000]),'condition_gain':([.1,0,0,0,1],[0,-5,-5,-5,.1],[5,5,5,5,2]),'calibrated_saturation':([10,1,40],[0,0,.1],[200,50,1000])},79:{'decay':([.1,20],[0,.01],[10,1000]),'bateman':([.1,24,1],[0,.1,.01],[10,1000,48]),'relative_decay':([2,24],[0,.01],[1000,1000]),'two_decay':([.05,2,.05,48],[0,.01,0,1],[10,48,10,1000]),'baseline_drift':([.1,24,0],[0,.01,-5],[10,1000,5]),'lognormal':([.1,1,1],[0,.1,.05],[10,96,5]),'saturating_amplitude':([.1,.01,24],[0,.000001,.01],[10,1,1000])},89:{'prospect':([1,1,1,0],[.1,.1,.01,-10],[4,4,30,10])}}
BASE={29:['persistence','linear','langmuir','flexible'],32:['persistence','tangent','flexible'],34:['persistence','hill4','flexible'],76:['persistence','rheobase','flexible'],79:['persistence','decay','flexible'],89:['mean','utility','persistence','flexible']}
EQ={
29:{'persistence':'Fhat=F5','linear':'Fhat=F0+(F5-F0)*dose/dose_cal','langmuir':'Fhat=F0+(F5-F0)*H(dose)/H(dose_cal); H(x)=x/(K+x)','hill':'Fhat=F0+(F5-F0)*H(dose)/H(dose_cal); H(x)=x^n/(K^n+x^n)','local':'Langmuir normalized at calibration dose; K inverted from F2/F5 baseline-subtracted ratio then multiplied by fitted factor','two_site':'H(x)=w*x/(K1+x)+(1-w)*x/(K2+x), amplitude fixed by low-dose calibration','dye_hill':'Hill H with log K=b0+b1*dye_NR and common exponent n','threshold':'H(x)=max(x-lag*dose_cal,epsilon)^n/(K^n+max(x-lag*dose_cal,epsilon)^n)','shrink_local':'log K=w*log K_local+(1-w)*log K_shared'},
32:{'persistence':'p_hat(t+.2)=p(t)','tangent':'p_hat(t+.2)=p(t)+2*(p(t)-p(t-.1))','damped':'p_hat=p0+a*(p0-p10)','periodic':'p_hat=p0+a*(p0-p20)+b*(p0-2*p20+p40)','flow':'p_hat=p0+a*(p0-p20)+b*(di0-de0)+c*(di0-di20)+d*(de0-de20)','regime':'p_hat=p0+beta dot [v,acc,flow,v*I(flow>0),v*FEM,v*BH]','limited':'p_hat=p0+a*s*tanh((p0-p20)/s)','shutter':'p_hat=p0+beta dot [v,acc,p0-p10,p10-p30,(p0-p05)-(p20-p30),v*FEM]'},
34:{'persistence':'Ihat=I(.75)','hill4':'Ihat=I(.75)*H(C)/H(.75); H(C)=C^4/(K^4+C^4)','genotype_hill':'Ihat=I(.75)*H(C)/H(.75); H=C^n/(K_g^n+C^n); log K_g=b0+b1*mutant','local_hill':'n shared; invert K from ratio I(.4)/I(.75), then Hill extrapolation; clipped ill-conditioned inversions recorded','two_pool':'H=w*H4(C;K1)+(1-w)*H4(C;K2), scale fixed at.75mM','genotype_exponent':'log K_g=b0+b1*g; n_g=n0+dn*g; calibrated Hill dose curve','calibration_blend':'Ihat=(1-w)*calibrated Hill +w*[I(.75)+max(I(.75)-I(.4),0)/.35*K*(1-exp(-(C-.75)/K))]','capacity':'Ihat=I(.75)+A*(1-exp(-(C-.75)/tau))*(1+b*mutant)'},
76:{'persistence':'Nhat=N_last_prefix','rheobase':'Nhat=max(0,g*(I-I0))','condition_threshold':'Nhat=max(0,g*(I-I0-bs*soft-bk*kd-bsk*soft*kd))','saturation':'Nhat=N_last+A*(1-exp(-(I-10)/K))','recruitment':'Nhat=max(0,(a+b*N_last+c*N_prefix_mean)*(I-10))','block':'Nhat=N_last+g*(I-10)*exp(-max(I-Iblock,0)/K)','condition_gain':'Nhat=N_last+max(0,a+bs*soft+bk*kd+bsk*soft*kd)*(I-10)^n','calibrated_saturation':'Nhat=N_last+(A+B*N_last)*(1-exp(-(I-10)/K))'},
79:{'persistence':'yhat=baseline','decay':'yhat=max(0,baseline+A*exp(-hours/tau))','bateman':'yhat=max(0,baseline+A*(exp(-hours/tau_decay)-exp(-hours/tau_rise)))','relative_decay':'yhat=max(0,baseline*(1+A*exp(-hours/tau)))','two_decay':'yhat=max(0,baseline+Afast*exp(-hours/tfast)+Aslow*exp(-hours/tslow))','baseline_drift':'yhat=max(0,baseline+A*exp(-hours/tau)+b*baseline_change*exp(-hours/24))','lognormal':'yhat=max(0,baseline+A*exp(-.5*(log(hours/tpeak)/sigma)^2))','saturating_amplitude':'yhat=max(0,baseline+A*baseline/(K+max(baseline,0))*exp(-hours/tau))'},
89:{'mean':'p_hat=development group-weighted choice mean','persistence':'p_hat=clip(causal within-protocol previous-choice mean,.001,.999)','utility':'logit(p_hat)=b0+b1*(reward*probability/2-1)','prospect':'p_hat=sigmoid(beta*(w(p)*(reward/2)^alpha-1)+bias); w(p)=p^gamma/(p^gamma+(1-p)^gamma)^(1/gamma)','context':'logit(p_hat)=beta dot [1,EVdiff,child,multi,description,child*multi,EVdiff*child,EVdiff*multi]','memory':'Context logits plus h,l,has_history*h, where h=history_mean-.5 and l=lag_choice-.5','description':'Memory logits plus (probability-.5)*description and its child interaction','history_interaction':'Context logits plus h,l,h*EVdiff,h*multi,h*child'}}
def fit(c,k,d):
 y=d.target.to_numpy(float);w=1/d.group.map(d.group.value_counts()).to_numpy();w=w/w.mean();m=dict(case=c,kind=k,coef=[],training_groups=sorted(d.group.unique()),training_rows=len(d),training_ids_sha256=hashlib.sha256('\\n'.join(d.sample_id).encode()).hexdigest(),equation=EQ[c].get(k,'Frozen coefficient vector times exact features(case,kind,data) in run.py; fitted scale/ridge fully recorded.'))
 if k=='mean':m['mean']=float(np.average(y,weights=w));return m
 if k in ['persistence','linear','tangent']:return m
 if k in BOUNDS[c]:
  x,lo,hi=BOUNDS[c][k];scale=max(float(np.sqrt(np.average(y*y,weights=w))),1e-5)
  fun=lambda p:(predict(dict(m,coef=p.tolist()),d)-y)*np.sqrt(w)/scale
  r=least_squares(fun,x,bounds=(lo,hi),max_nfev=600,ftol=1e-9,xtol=1e-9,gtol=1e-9);m['coef']=r.x.tolist();m['optimizer']=dict(success=bool(r.success),cost=float(r.cost),bounds=[lo,hi],jacobian_rank=int(np.linalg.matrix_rank(r.jac)),jacobian_singular_values=np.linalg.svd(r.jac,compute_uv=False).tolist());return m
 X=features(c,k,d);s=np.maximum(np.sqrt(np.average(X*X,axis=0,weights=w)),1e-8);Z=X/s;alpha=1 if k=='flexible' else .01
 if c==89:
  def obj(b):
   pr=expit(Z@b);loss=np.sum(w*(np.logaddexp(0,Z@b)-y*(Z@b)))+.5*alpha*np.sum(b*b);grad=Z.T@(w*(pr-y))+alpha*b;return loss,grad
  r=minimize(obj,np.zeros(Z.shape[1]),jac=True,method='L-BFGS-B',options={'maxiter':400});coef=r.x/s;m['optimizer_success']=bool(r.success)
 else:
  offset=d.p0.to_numpy() if c==32 and k!='flexible' else np.zeros(len(d));coef=np.linalg.solve(Z.T@(w[:,None]*Z)+alpha*np.eye(Z.shape[1]),Z.T@(w*(y-offset)))/s
 m['coef']=coef.tolist();m['feature_rms']=s.tolist();m['ridge_alpha']=alpha;m['coefficient_order']='Exact columns returned by run.features(case,kind,inputs)';return m
'''
for c in [29,32,34,76,79,89]:
 p=W/f'P100-{c:03}';(p/'run.py').write_text(run);(p/'fit.py').write_text(fit)
print('Model libraries created; no fits executed')
