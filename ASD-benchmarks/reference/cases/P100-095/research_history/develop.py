from pathlib import Path
import json,sys,hashlib,datetime
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from run import predict,design,physical,read_table
P=Path(__file__).resolve().parent

def dump(p,x):p.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def fit(d,config):
 m=dict(config);m['training_groups']=sorted(d.group.unique());m['training_rows']=len(d);m['training_ids_sha256']=hashlib.sha256('\n'.join(d.sample_id).encode()).hexdigest()
 if m['type'] in ['fixed','preset']:return m
 if m.get('rbf_columns'):
  z=physical(d,m['case']);raw=np.column_stack([z[k] for k in m.pop('rbf_columns')]);mu=raw.mean(0);sd=raw.std(0);sd[sd<1e-10]=1;norm=(raw-mu)/sd
  # Deterministic farthest-point coverage, no response-dependent centers.
  ids=[0];dist=np.sum((norm-norm[0])**2,axis=1)
  for _ in range(min(31,len(d)-1)):
   j=int(np.argmax(dist));ids.append(j);dist=np.minimum(dist,np.sum((norm-norm[j])**2,axis=1))
  m['rbf']={'columns':config['rbf_columns'],'mean':mu.tolist(),'std':sd.tolist(),'centers':norm[ids].tolist(),'width':2.0}
 X,off,scale=design(m,d);y=(d.target.to_numpy()-off)/scale
 weights=d.group.map(1/d.groupby('group').size()).to_numpy();weights=weights/weights.sum()*len(d)
 # Fit in transformed physical response; all families share original-unit primary evaluation.
 ss=np.sqrt(np.sum(X*X*weights[:,None],axis=0)/weights.sum());ss[ss<1e-12]=1;A=X/ss;w=np.sqrt(weights);alpha=m.get('alpha',0)*len(d)
 coef=np.linalg.solve((A*w[:,None]).T@(A*w[:,None])+np.eye(A.shape[1])*(alpha+1e-10),(A*w[:,None]).T@(y*w))
 if m.get('robust'):
  resid=y-A@coef;s=max(float(np.median(np.abs(resid-np.median(resid)))*1.4826),1e-6)
  coef=least_squares(lambda b:np.r_[w*(A@b-y),np.sqrt(alpha)*b],coef,loss='soft_l1',f_scale=s,max_nfev=1000).x
 m['coef']=(coef/ss).tolist();m['rank']=int(np.linalg.matrix_rank(X));condition=float(np.linalg.cond(A));m['condition_number']=condition if np.isfinite(condition) else None;m['identifiability_warning']='Rank-deficient basis in this training partition' if m['rank']<X.shape[1] else None;m['complexity']=len(m['coef']);return m

def folds(d,c):
 k=d.fold_key
 if c==38:ranges=[(2,2),(3,3),(4,4)]
 elif c==41:ranges=[(3,3),(4,4),(5,5)]
 elif c==47:ranges=[(4047,4047),(4048,4048),(4049,4049),(4050,4050)]
 elif c==48:ranges=[(121,131),(708,715),(716,724)]
 elif c==95:ranges=[(4,4),(7,8),(9,10)]
 else:
  return [(str(g),d[d.group!=g],d[d.group==g]) for g in sorted(d.group.unique())]
 return [(f'{a}-{b}',d[k<a],d[(k>=a)&(k<=b)]) for a,b in ranges]

def metrics(d,p):
 q=d[['sample_id','group','target']].copy();q['prediction']=p;q['absolute_error']=np.abs(p-q.target);q['squared_error']=(p-q.target)**2;q['signed_error']=p-q.target
 g=q.groupby('group').agg(mae=('absolute_error','mean'),mse=('squared_error','mean'),bias=('signed_error','mean'),n=('target','size'));return {'primary_error':float(g.mae.mean()),'mean_group_absolute_error':float(g.mae.mean()),'worst_group_mae':float(g.mae.max()),'group_rmse':float(np.sqrt(g.mse).mean()),'group_bias':float(g.bias.mean()),'groups':len(g),'rows':len(q),'per_group':g.reset_index().to_dict('records')}

def main():
 out=P/sys.argv[1]
 if (out/'COMPLETED.json').exists():raise ValueError('Preserve prior attempt; do not overwrite')
 config=json.loads((out/'config.json').read_text());d=read_table(P/'development.csv.gz');allpred=[];states={}
 for name,tr,va in folds(d,config['case']):
  if not len(tr) or not len(va):raise ValueError('Empty frozen fold '+name)
  if set(tr.group)&set(va.group):raise ValueError('Group leakage')
  m=fit(tr,config);states[name]=m;q=va[['sample_id','group','target']].copy();q['prediction']=predict(m,va);q['fold']=name;allpred.append(q)
 q=pd.concat(allpred,ignore_index=True);q.to_csv(out/'predictions.csv.gz',index=False);stats=metrics(q,q.prediction.to_numpy());dump(out/'metrics.json',stats);dump(out/'fold_models.json',states);dump(out/'model.json',fit(d,config));dump(out/'COMPLETED.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'development_only':True,'protocol_sha256':hashlib.sha256((P/'PROTOCOL.json').read_bytes()).hexdigest()})
 (out/'REPORT.md').write_text(f"# {out.name}\n\n"+(out/'HYPOTHESIS.md').read_text()+f"\nDevelopment whole-group MAE: {stats['primary_error']:.8g}. Worst-group MAE: {stats['worst_group_mae']:.8g}. {stats['groups']} scored groups and {stats['rows']} rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.\n")
 print(config['case'],out.name,stats['primary_error'],stats['worst_group_mae'])
if __name__=='__main__':main()
