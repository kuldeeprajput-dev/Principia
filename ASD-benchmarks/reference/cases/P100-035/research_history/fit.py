import numpy as np
from scipy.optimize import minimize
from scipy.special import expit
from run import predict,features,INPUTS,FAMILY
BASE={35:['constant','species','flexible']}
def fit(case,k,d):
 m=dict(kind=k);y=d.target.to_numpy();w=1/d.groupby('group').group.transform('count').to_numpy();w=w/w.sum()
 if k=='flexible':
  x=d[INPUTS[:-1]].to_numpy();mean=x.mean(axis=0);scale=x.std(axis=0);scale[scale<1e-10]=1;z=(x-mean)/scale;cent=z[np.linspace(0,len(d)-1,16,dtype=int)];m.update(mean=mean.tolist(),scale=scale.tolist(),centers=cent.tolist())
 X=features(k,d,m);pen=np.ones(X.shape[1])*.002;pen[0]=1e-9
 def loss(b):
  z=X@b;return np.sum(w*(np.logaddexp(0,z)-y*z))+.5*np.sum(pen*b*b),X.T@(w*(expit(z)-y))+pen*b
 out=minimize(loss,np.zeros(X.shape[1]),jac=True,method='L-BFGS-B',options={'maxiter':1500,'ftol':1e-13,'gtol':1e-8})
 if not out.success:raise ValueError('Logistic convergence failed')
 names=['intercept']+(['species_code='+str(j) for j in range(1,7)] if k!='constant' else [])
 if k=='flexible':names+=['training_RBF'+str(j) for j in range(16)]
 elif k in FAMILY:names+=FAMILY[k]+(['log_centroid*species_code='+str(j) for j in range(1,7)] if k=='species_interaction' else [])
 m.update(coef=out.x.tolist(),feature_names=names,equation='Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order '+str(names)+'; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.',training_groups=sorted(d.group.unique()),training_rows=len(d),parameter_count=len(out.x),rank=int(np.linalg.matrix_rank(X)));return m
