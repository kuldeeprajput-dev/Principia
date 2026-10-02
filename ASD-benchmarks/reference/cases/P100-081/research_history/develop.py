from pathlib import Path
import json,datetime,argparse,hashlib
import numpy as np,pandas as pd
from scipy.optimize import least_squares
from run import predict,calc
ROOT=Path(__file__).resolve().parent

def score(d,p):
 e=np.asarray(p)-d.target.to_numpy();q=pd.DataFrame({'group':d.group,'ae':abs(e),'se':e*e,'bias':e});g=q.groupby('group').agg(mae=('ae','mean'),mse=('se','mean'),bias=('bias','mean'));return {'primary_error':float(g.mae.mean()),'rmse':float(np.sqrt(g.mse.mean())),'bias':float(g.bias.mean()),'worst_group_error':float(g.mae.max()),'groups':len(g),'rows':len(d),'by_group':g.mae.to_dict()}
def fit(conf,d):
 m={k:v for k,v in conf.items() if k not in ['initial','bounds','linear_terms','base']};m['parameters']={};m.update(training_groups=sorted(d.group.unique()),training_rows=len(d));y=d.target.to_numpy(float);w=1/d.groupby('group').group.transform('size').to_numpy();w/=w.mean()
 if conf.get('linear_terms'):
  X=np.column_stack([calc(t,d,{}) for t in conf['linear_terms']]);b=calc(conf.get('base','0'),d,{});s=np.maximum(np.sqrt(np.mean(X*X,axis=0)),1e-9);A=X/s*np.sqrt(w[:,None]);coef=np.linalg.lstsq(np.vstack([A,np.eye(X.shape[1])*1e-4]),np.r_[(y-b)*np.sqrt(w),np.zeros(X.shape[1])],rcond=None)[0]/s;m['parameters']={f'b{i}':float(v) for i,v in enumerate(coef)};m['fit_method']='weighted linear least squares';m['condition']=float(np.linalg.cond(A));return m
 keys=list(conf.get('initial',{}))
 if not keys:return m
 x0=[conf['initial'][k] for k in keys];lo=[conf['bounds'][k][0] for k in keys];hi=[conf['bounds'][k][1] for k in keys];scale=max(np.std(y),1e-8)
 def fun(p):return (predict({**m,'parameters':dict(zip(keys,p))},d)-y)*np.sqrt(w)/scale
 opt=least_squares(fun,x0,bounds=(lo,hi),max_nfev=350,ftol=1e-9,xtol=1e-9,gtol=1e-9);sv=np.linalg.svd(opt.jac,compute_uv=False);m.update(parameters=dict(zip(keys,map(float,opt.x))),optimizer_success=bool(opt.success),nfev=int(opt.nfev),jacobian_condition=float(sv[0]/max(sv[-1],1e-15)),bounds=conf['bounds']);return m

def main():
 ap=argparse.ArgumentParser();ap.add_argument('config');ap.add_argument('--baseline',action='store_true');a=ap.parse_args();c=json.loads(Path(a.config).read_text());d=pd.read_csv(ROOT/'development.csv.gz',dtype={'sample_id':str,'group':str});proto=json.loads((ROOT/'PROTOCOL.json').read_text())
 if (ROOT/'FREEZE.json').exists():raise ValueError('Frozen campaign')
 prior=sorted((ROOT/'attempts').glob('attempt-*'));out=ROOT/('baselines/'+c['name'] if a.baseline else 'attempts/attempt-'+f'{len(prior)+1:03d}');out.mkdir(parents=True,exist_ok=False);c['recorded_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();c['parent']=prior[-1].name if prior and not a.baseline else None
 (out/'config.json').write_text(json.dumps(c,indent=2)+'\n');(out/'HYPOTHESIS.md').write_text('# Hypothesis\n\n'+c['hypothesis']+'\n\nFalsifier: no material grouped development benefit, worse worst-group error, or unidentifiable parameters. Confirmation is not accessed.\n')
 preds=[];states=[]
 for f in sorted(d.fold.unique()):
  va=d[d.fold==f];tr=d[d.fold<f] if proto.get('fold_design')=='forward' else d[d.fold!=f]
  if len(tr)==0:continue
  m=fit(c,tr);q=va[['sample_id','group','target','fold']].copy();q['prediction']=predict(m,va);preds.append(q);states.append({'fold':int(f),'state':m})
 q=pd.concat(preds).sort_values('sample_id');met=score(q,q.prediction);m=fit(c,d);q.to_csv(out/'predictions.csv.gz',index=False);(out/'metrics.json').write_text(json.dumps(met,indent=2)+'\n');(out/'model.json').write_text(json.dumps(m,indent=2)+'\n');(out/'fold_models.json').write_text(json.dumps(states,indent=2)+'\n');(out/'REPORT.md').write_text('# Development result\n\n'+c['hypothesis']+'\n\nMean group MAE: '+str(met['primary_error'])+' '+proto['target_units']+'. Worst group MAE: '+str(met['worst_group_error'])+'.\n\nThese are out-of-fold estimates under the frozen information budget. See model.json for every coefficient, bounds, and fit diagnostics. Neither fit quality nor a familiar equation establishes a new physical law.\n');print(json.dumps({'attempt':out.name,'name':c['name'],**{k:v for k,v in met.items() if k!='by_group'}}))
if __name__=='__main__':main()
