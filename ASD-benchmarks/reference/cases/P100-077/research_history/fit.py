import numpy as np
from scipy.optimize import least_squares
from run import predict
BASE={77:['independence','constant','flexible']}
E={'independence':'j=p*q','constant':'j=clip(b0,L,U)','flexible':'j=clip(b0+b1*p+b2*q+b3*ln(dose),L,U)','competence':'j=p*q+alpha*(min(p,q)-p*q)','odds_ratio':'j*(1-p-q+j)=exp(beta)*(p-j)*(q-j)','common_fraction':'j=clip(p*q/tau,L,U)','dose_competence':'j=p*q+sigmoid(b0+b1*ln(dose))*(min(p,q)-p*q)','competition':'j=p*q+alpha*(p*q-L), -1<=alpha<=0','dose_odds':'j*(1-p-q+j)=exp(b0+b1*ln(dose))*(p-j)*(q-j)','limiting_locus':'j=clip(alpha*min(p,q),L,U)'}
def fit(case,k,d):
 y=d.target.to_numpy(float);w=1/d.groupby('group').group.transform('count').to_numpy(float);w=w/w.sum()
 if k=='independence':b=[];rank=0;bounds=None
 else:
  init,lo,hi={'constant':([.05],[0],[1]),'flexible':([0,0,0,0],[-2]*4,[2]*4),'competence':([.3],[0],[1]),'odds_ratio':([1],[-6],[6]),'common_fraction':([.5],[.02],[1]),'dose_competence':([0,0],[-8,-5],[8,5]),'competition':([-.3],[-1],[0]),'dose_odds':([1,0],[-6,-5],[6,5]),'limiting_locus':([.5],[0],[1])}[k]
  def residual(b):
   v=(predict({'kind':k,'coef':b},d)-y)*np.sqrt(w)
   return np.r_[v,.1*np.asarray(b)] if k=='flexible' else v
  result=least_squares(residual,init,bounds=(lo,hi),max_nfev=2000,ftol=1e-12,xtol=1e-12,gtol=1e-10)
  if not result.success:raise ValueError('Dependence fit failed')
  b=result.x.tolist();rank=int(np.linalg.matrix_rank(result.jac));bounds=[lo,hi]
 return dict(kind=k,coef=b,equation=E[k]+'; y_hat=100*j, L=max(0,p+q-1), U=min(p,q)',parameter_count=len(b),rank=rank,bounds=bounds,training_groups=sorted(d.group.unique()),training_rows=len(d),fit='replicate-balanced nonlinear least squares; flexible control has fixed L2 penalty0.01',identifiability='Effective association, not unique shared molecular mechanism; three doses per training replicate')
