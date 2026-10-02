import numpy as np
from run import predict,features,INPUTS
BASE={93:['copy','shift','flexible']}
E={'copy':'c','shift':'c+delta_line','multiplicative':'c*(1+b_line)','recruitment':'c+delta_line*sigmoid((q-q0)/.1)','location_scale':'c+delta_line+s_line*control_width*(q-.5)','saturation':'c+delta_line*c/(K+abs(c))','specificity':'c+b0+b1*WT+b2*WT*(q-.5)','tail_selective':'c+delta_line+b3*WT*(q-.5)^3','flexible':'c+b0+sum_j b_j exp(-mean((z-center_j)^2)/2)'}
def fit(case,k,d):
 m=dict(kind=k);y=d.target.to_numpy()-d.control.to_numpy();w=1/d.groupby('group').group.transform('count').to_numpy();w=w/w.sum()
 if k=='copy':b=[];rank=0
 else:
  if k=='flexible':
   x=d[INPUTS].to_numpy();mean=x.mean(axis=0);scale=x.std(axis=0);scale[scale<1e-10]=1;z=(x-mean)/scale;cent=z[np.linspace(0,len(d)-1,9,dtype=int)];m.update(mean=mean.tolist(),scale=scale.tolist(),centers=cent.tolist())
  profile=[dict(threshold=t) for t in [.2,.4,.6,.8]] if k=='recruitment' else ([dict(K=t) for t in [50,200,1000,5000,20000]] if k=='saturation' else [{}]);best=None;records=[]
  for v in profile:
   mm={**m,**v};X=features(k,d,mm);reg=.002 if k=='flexible' else 1e-8;b=np.linalg.solve(X.T@(w[:,None]*X)+np.eye(X.shape[1])*reg,X.T@(w*y));err=float(np.sum(w*np.abs(X@b-y)));records.append(dict(**v,error=err))
   if best is None or err<best[0]:best=(err,b,X,mm)
  _,b,X,m=best;b=b.tolist();rank=int(np.linalg.matrix_rank(X));m['training_profile']=records
 m.update(coef=b,equation=E[k]+'; c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.',training_groups=sorted(d.group.unique()),training_rows=len(d),parameter_count=len(b),rank=rank);return m
