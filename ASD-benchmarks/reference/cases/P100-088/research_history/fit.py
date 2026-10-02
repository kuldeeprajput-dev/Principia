import numpy as np
from scipy.optimize import minimize
from scipy.special import expit
from run import features
BASE={88:['constant','utility','flexible']}
TERMS={'constant':['1'],'utility':['1','normalized expected-value difference','risky probability minus0.5','gain/loss sign','safe lottery variable indicator'],'attitude':['known feedback','known feedback times lottery entropy','known complete feedback'],'inertia':['previous-choice centered × history available','Beta(1,1) historical risky-choice mean minus0.5','trial progress'],'learning':['visible previous reward error','visible previous counterfactual regret','known feedback times trial progress']}
def fit(case,k,d):
 X=features(k,d);y=d.target.to_numpy(float);w=1/d.groupby('group').group.transform('count').to_numpy(float);w=w/w.sum();pen=.001 if k=='flexible' else .00001;mask=np.ones(X.shape[1]);mask[0]=0
 def fun(b):
  z=X@b;p=expit(z);loss=np.sum(w*(np.logaddexp(0,z)-y*z))+.5*pen*np.sum(mask*b*b);g=X.T@(w*(p-y))+pen*mask*b;return loss,g
 result=minimize(fun,np.zeros(X.shape[1]),jac=True,method='L-BFGS-B',options={'maxiter':400,'ftol':1e-12,'gtol':1e-8});b=result.x
 if not result.success:raise ValueError('Logistic optimizer failed '+result.message)
 return dict(kind=k,coef=b.tolist(),equation='p_hat=1/(1+exp(-sum_j beta_j*phi_j)); exact ordered phi in run.features for '+k,feature_names=TERMS,training_groups=sorted(d.group.unique()),training_rows=len(d),rank=int(np.linalg.matrix_rank(X)),parameter_count=len(b),ridge=pen,fit_loss='participant-balanced logistic loss plus L2 excluding intercept; primary selection metric remains held-group Brier',optimizer_message=str(result.message),gradient_max=float(np.max(np.abs(fun(b)[1]))))
