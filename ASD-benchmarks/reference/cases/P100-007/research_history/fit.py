import numpy as np
from run import predict,features,INPUTS
BASE={7:['persistence','velocity','periodic','flexible']}
E={'persistence':'F','velocity':'F+v','periodic':'C','damped':'F+b0*v+b1*a','phase':'F+b0*(C-F)+b1*v','bilateral':'F+b0*v+b1*a+b2*vO','stance':'F+b0*v+b1*a+b2*v*tanh(F/100N)+b3*a*tanh(F/100N)','phase_bilateral':'F+b0*(C-F)+b1*v+b2*vO','speed_clock':'F+b0*(C-F)+b1*v*s+b2*vO*s; s=speed/(1m/s)','compact_phase':'F+b0*(C-F)','flexible':'F+b0+sum_j b_j exp(-mean((z-center_j)^2)/2)'}
def fit(case,k,d):
 m=dict(kind=k);y=d.target.to_numpy()-d.force.to_numpy();w=1/d.groupby('group').group.transform('count').to_numpy();w=w/w.sum()
 if k in ['persistence','velocity','periodic']:b=[];rank=0
 else:
  if k=='flexible':
   x=d[INPUTS].to_numpy();mean=x.mean(axis=0);scale=x.std(axis=0);scale[scale<1e-10]=1;z=(x-mean)/scale;cent=z[np.linspace(0,len(d)-1,20,dtype=int)];X=np.column_stack([np.ones(len(d)),np.exp(-((z[:,None,:]-cent[None,:,:])**2).mean(axis=2)/2)]);m.update(mean=mean.tolist(),scale=scale.tolist(),centers=cent.tolist());reg=.002
  else:X=features(k,d);reg=1e-6
  b=np.linalg.solve(X.T@(w[:,None]*X)+np.eye(X.shape[1])*reg,X.T@(w*y)).tolist();rank=int(np.linalg.matrix_rank(X))
 m.update(coef=b,equation=E[k]+'; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.',training_groups=sorted(d.group.unique()),training_rows=len(d),parameter_count=len(b),rank=rank);return m
