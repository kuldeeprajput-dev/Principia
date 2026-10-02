import numpy as np
from run import features
BASE={75:['copy','log_additive','quadratic']}
EQUATIONS={'copy':'y_hat=c','log_additive':'y_hat=max(0,c+b1*ln(E/30)+b2*s)','quadratic':'y_hat=max(0,c+b1*x+b2*s+b3*x*s+b4*x^2+b5*x^2*s), x=ln(E/30)','saturation':'y_hat=max(0,c+b1*q+b2*s), q=E/(K+E)-30/(K+30)','synergy':'y_hat=max(0,c+b1*x+b2*s+b3*x*s), x=ln(E/30)','mechanical_only':'y_hat=max(0,c+b1*ln(E/30))','threshold':'y_hat=max(0,c+b1*I(E>=200)+b2*s+b3*s*I(E>=200))','shear_only':'y_hat=max(0,c+b1*s)','saturating_synergy':'y_hat=max(0,c+b1*q+b2*s+b3*q*s), q=E/(K+E)-30/(K+30)','calibration_scaling':'y_hat=max(0,c+b1*x+b2*s+b3*x*s+b4*(c-5)*s), x=ln(E/30)'}
def fit(case,k,d):
 y=d.target.to_numpy(float)-d.calibration.to_numpy(float);w=1/d.groupby('group').group.transform('count').to_numpy(float);states=[]
 for K in ([30.,100.,300.,1000.,3000.] if k in ['saturation','saturating_synergy'] else [200.]):
  X=features(k,d,K);pen=.1 if k=='quadratic' else 1e-8;A=X*np.sqrt(w)[:,None];b=y*np.sqrt(w);coef=np.linalg.lstsq(A.T@A+pen*np.eye(X.shape[1]),A.T@b,rcond=None)[0];err=float(np.sum(w*(X@coef-y)**2));states.append((err,K,coef,np.linalg.matrix_rank(X) if X.shape[1] else 0))
 err,K,coef,rank=min(states,key=lambda z:z[0]);return dict(kind=k,coef=coef.tolist(),K=K,equation=EQUATIONS[k],training_groups=sorted(d.group.unique()),training_rows=len(d),rank=int(rank),parameter_count=len(coef)+(k in ['saturation','saturating_synergy']),profile_training_mse=[dict(K=q[1],weighted_sse=q[0]) for q in states],ridge=.1 if k=='quadratic' else 1e-8,units='y and c: log2(1+CPM); E and K: kPa; s: HSS indicator')
