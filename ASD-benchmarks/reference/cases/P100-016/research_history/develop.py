from pathlib import Path
import sys,json,hashlib,datetime
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
from scipy.special import logit
from run import predict,physical,design,read_table,link,loss_report
P=Path(__file__).resolve().parent

def dump(path,obj):path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def weights(d):
 s=d.sample_weight.to_numpy(float) if 'sample_weight' in d else np.ones(len(d));g=pd.Series(s,index=d.index).groupby(d.group).transform('sum').to_numpy();w=s/g;return w/w.sum()*len(w)

def fit(d,config):
 m=dict(config);m['training_groups']=sorted(d.group.unique());m['training_rows']=len(d);m['training_ids_sha256']=hashlib.sha256('\n'.join(d.sample_id).encode()).hexdigest();w=weights(d)
 if m['type']=='fixed':return m
 if m.get('rbf_columns'):
  z=physical(d,m['case']);raw=np.column_stack([z[k] for k in m.pop('rbf_columns')]);mu=np.average(raw,axis=0,weights=w);sd=np.sqrt(np.average((raw-mu)**2,axis=0,weights=w));sd[sd<1e-10]=1;norm=(raw-mu)/sd;ids=[int(np.argmin(np.sum(norm**2,axis=1)))];dist=np.sum((norm-norm[ids[0]])**2,axis=1)
  for _ in range(min(31,len(d)-1)):
   j=int(np.argmax(dist));ids.append(j);dist=np.minimum(dist,np.sum((norm-norm[j])**2,axis=1))
  m['rbf']=dict(columns=config['rbf_columns'],mean=mu.tolist(),std=sd.tolist(),centers=norm[ids].tolist(),width=2.)
 X,off,scale=design(m,d);y=d.target.to_numpy(float);lk=m.get('link','identity');yt=np.log(y) if lk=='log' else y;ss=np.sqrt(np.average(X*X,axis=0,weights=w));ss[ss<1e-12]=1;A=X/ss;sw=np.sqrt(w);alpha=m.get('alpha',0)*len(d)
 b=np.linalg.lstsq(np.vstack([A*sw[:,None],np.sqrt(alpha)*np.eye(A.shape[1])]),np.r_[((yt-off)/scale)*sw,np.zeros(A.shape[1])],rcond=None)[0]
 if lk in ['logit','cloglog']:
  b=np.zeros(A.shape[1]);prevalence=np.clip(np.average(y,weights=w),1e-5,1-1e-5);b[0]=logit(prevalence) if lk=='logit' else np.log(-np.log1p(-prevalence));b=least_squares(lambda b:np.r_[sw*(link(off+scale*(A@b),lk)-y),np.sqrt(alpha)*b],b,max_nfev=500).x
 elif m.get('robust'):
  rr=yt-(off+scale*(A@b));s=max(float(np.median(np.abs(rr-np.median(rr)))*1.4826),1e-6);b=least_squares(lambda b:np.r_[sw*((off+scale*(A@b))-yt),np.sqrt(alpha)*b],b,loss='soft_l1',f_scale=s,max_nfev=800).x
 cond=float(np.linalg.cond(A));m.update(coef=(b/ss).tolist(),complexity=len(b),rank=int(np.linalg.matrix_rank(X)),condition_number=cond if np.isfinite(cond) else None);return m

def folds(d):
 s=json.loads((P/'SPLITS.json').read_text());out=[]
 if isinstance(s['folds'],list) and s['folds'] and 'train_before' in s['folds'][0]:
  for x in s['folds']:out.append((str(x['validation_from'])+'-'+str(x['validation_through']),d[d.fold_key<x['train_before']],d[d.fold_key.between(x['validation_from'],x['validation_through'])]))
 else:
  for k in sorted(d.fold_key.unique()):out.append((str(k),d[d.fold_key!=k],d[d.fold_key==k]))
 return out

def main():
 out=P/sys.argv[1]
 if (out/'COMPLETED.json').exists():raise ValueError('Completed attempts are immutable')
 config=json.loads((out/'config.json').read_text());spec=json.loads((P/'TASK_SPEC_PREFIT.json').read_text());d=read_table(P/'development.csv.gz');predictions=[];states={}
 for name,tr,va in folds(d):
  if len(tr)==0 or len(va)==0 or set(tr.group)&set(va.group):raise ValueError('Invalid fold '+name)
  state=fit(tr,config);states[name]=state;cols=['sample_id','group','target']+(['sample_weight'] if 'sample_weight' in va else []);q=va[cols].copy();q['prediction']=predict(state,va);q['fold']=name;predictions.append(q)
 q=pd.concat(predictions,ignore_index=True);q.to_csv(out/'predictions.csv.gz',index=False);stats=loss_report(q,q.prediction.to_numpy(),spec['metric_kind']);dump(out/'metrics.json',stats);dump(out/'fold_models.json',states);dump(out/'model.json',fit(d,config));dump(out/'COMPLETED.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),development_only=True,protocol_sha256=hashlib.sha256((P/'PROTOCOL.json').read_bytes()).hexdigest(),run_sha256=hashlib.sha256((P/'run.py').read_bytes()).hexdigest(),develop_sha256=hashlib.sha256((P/'develop.py').read_bytes()).hexdigest()));(out/'REPORT.md').write_text('# '+out.name+'\n\n'+(out/'HYPOTHESIS.md').read_text()+f"\n\nDevelopment primary error: {stats['primary_error']:.10g}. Worst-group error: {stats['worst_group_error']:.10g}. {stats['groups']}groups/{stats['scored_rows']}observations. Model and fold states contain all coefficients, rank, training groups and training-row hashes. No confirmation feedback used.\n");print(config['case'],out.name,stats['primary_error'],stats['worst_group_error'])
if __name__=='__main__':main()
