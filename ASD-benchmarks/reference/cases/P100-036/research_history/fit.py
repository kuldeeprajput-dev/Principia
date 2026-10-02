import numpy as np
from scipy.optimize import least_squares
from run import features,INPUTS
BASE={36:['constant','context','flexible']}
E={'constant':'sigmoid(b0)','context':'sigmoid(b0+b1*tiny+b2*salt+b3*drought+b4*highstress)','quenching':'sigmoid(b0+b1/(1+max(NPQ,0))+b2*tiny)','recovery':'sigmoid(b0+b1*Rfd/(1+abs(Rfd))+b2*asinh(NPQ)+b3*tiny)','pigment':'sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*q*NGRDI+b5*tiny)','morphology':'sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*size+b5*size*q+b6*tiny)','stress_regime':'sigmoid(b0+b1*r+b2*q+b3*NGRDI+b4*tiny+b5*salt+b6*drought+b7*highstress+b8*q*salt+b9*q*drought)','pigment_only':'sigmoid(b0+b1*NGRDI+b2*tiny)','recovery_only':'sigmoid(b0+b1*r+b2*tiny)','flexible':'sigmoid(b0+sum_j b_j exp(-mean((z-center_j)^2)/2)); training-only standardization'}
def fit(case,k,d):
 m=dict(kind=k);y=d.target.to_numpy(float);w=1/d.groupby('group').group.transform('count').to_numpy(float);w=w/w.sum()
 if k=='flexible':
  x=d[INPUTS].to_numpy(float);mean=x.mean(axis=0);scale=x.std(axis=0);scale[scale<1e-10]=1;z=(x-mean)/scale;idx=np.linspace(0,len(d)-1,min(16,len(d)),dtype=int);cent=z[idx];X=np.column_stack([np.ones(len(d)),np.exp(-((z[:,None,:]-cent[None,:,:])**2).mean(axis=2)/2)]);m.update(mean=mean.tolist(),scale=scale.tolist(),centers=cent.tolist())
 else:X=features(k,d)
 pen=.0003 if k=='flexible' else .000001;mask=np.ones(X.shape[1]);mask[0]=0
 from scipy.special import expit
 def res(b):return np.r_[np.sqrt(w)*(expit(X@b)-y),np.sqrt(pen)*mask*b]
 init=np.zeros(X.shape[1]);init[0]=np.log(np.clip(y.mean(),1e-4,1-1e-4)/(1-np.clip(y.mean(),1e-4,1-1e-4)));out=least_squares(res,init,max_nfev=2000,ftol=1e-11,xtol=1e-11,gtol=1e-10)
 if not out.success:raise ValueError('Response fit failed')
 m.update(coef=out.x.tolist(),equation=E[k]+'; r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10',training_groups=sorted(d.group.unique()),training_rows=len(d),rank=int(np.linalg.matrix_rank(X)),parameter_count=len(out.x),ridge=pen);return m
