import numpy as np
from scipy.optimize import least_squares
from run import predict,INPUTS
BASE={33:['constant','fourier','autocorrelation','flexible']}
E={'constant':'weighted development median HR','fourier':'F','autocorrelation':'A','alias':'F-sigmoid(b0+b1*(S-.5))*(F-H)','fusion':'w*F+(1-w)*A; w=sigmoid(b0+b1*(Q-.3)+b2*D)','shrinkage':'w*F+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)); mu=b2','motion_fusion':'w*F+(1-w)*A+b4*ear; w=sigmoid(b0+b1*(Q-.3)+b2*D+b3*motion)','agreement_gate':'C=H if S>=threshold else F; select C only when abs(C-A)<abs(F-A)','consensus_shrink':'w*(F+A)/2+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)-b2*D), mu=b3','flexible':'b0+sum_j b_j exp(-mean((z-center_j)^2)/2); training-only z scaling'}
def fit(case,k,d):
 m=dict(kind=k);y=d.target.to_numpy(float);w=1/d.groupby('group').group.transform('count').to_numpy(float);w=w/w.sum()
 if k=='constant':
  idx=np.argsort(y);b=[float(y[idx][np.searchsorted(np.cumsum(w[idx]),.5)])];rank=1
 elif k in ['fourier','autocorrelation']:b=[];rank=0
 elif k=='flexible':
  x=d[INPUTS].to_numpy(float);mean=x.mean(axis=0);scale=x.std(axis=0);scale[scale<1e-10]=1;z=(x-mean)/scale;idx=np.linspace(0,len(d)-1,min(20,len(d)),dtype=int);cent=z[idx];X=np.column_stack([np.ones(len(d)),np.exp(-((z[:,None,:]-cent[None,:,:])**2).mean(axis=2)/2)]);pen=np.eye(X.shape[1])*.005;pen[0,0]=1e-9;b=np.linalg.solve(X.T@(w[:,None]*X)+pen,X.T@(w*y)).tolist();m.update(mean=mean.tolist(),scale=scale.tolist(),centers=cent.tolist());rank=int(np.linalg.matrix_rank(X))
 elif k=='agreement_gate':
  candidates=[.1,.25,.5,.75,.9];err=[np.sum(w*np.abs(predict(dict(kind=k,coef=[t]),d)-y)) for t in candidates];b=[candidates[int(np.argmin(err))]];rank=1;m['training_threshold_profile']=dict(zip(map(str,candidates),map(float,err)))
 else:
  init,lo,hi={'alias':([-2,4],[-10,0],[10,20]),'fusion':([0,2,-1],[-10,-20,-20],[10,20,20]),'shrinkage':([0,5,80],[-10,0,30],[10,30,240]),'motion_fusion':([0,2,-1,0,0],[-10,-20,-20,-10,-30],[10,20,20,10,30]),'consensus_shrink':([0,4,1,80],[-10,0,0,30],[10,30,20,240])}[k]
  out=least_squares(lambda b:np.sqrt(w)*(predict(dict(kind=k,coef=b),d)-y),init,bounds=(lo,hi),max_nfev=1500,ftol=1e-11,xtol=1e-11,gtol=1e-9)
  if not out.success:raise ValueError('Pulse fitting failed')
  b=out.x.tolist();rank=int(np.linalg.matrix_rank(out.jac));m['bounds']=[lo,hi]
 m.update(coef=b,equation='clip('+E[k]+',30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60',training_groups=sorted(d.group.unique()),training_rows=len(d),parameter_count=len(b),rank=rank);return m
