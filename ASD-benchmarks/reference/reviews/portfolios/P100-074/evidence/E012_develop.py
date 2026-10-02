"""Explicit development-only entry point. No confirmation scoring or output."""
from pathlib import Path
import json,sys,hashlib,datetime
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import native
from run import predict,features
HERE=Path(__file__).resolve().parent

def write(p,x):p.write_text(json.dumps(x,indent=2,allow_nan=False))
def hashfile(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def metric(d,y):
 v=pd.DataFrame({'group':d.group.to_numpy(),'abs':np.abs(d.target.to_numpy()-y),'square':(d.target.to_numpy()-y)**2,'bias':y-d.target.to_numpy()}).groupby('group').mean();return {'primary_error':float(v['abs'].mean()),'worst_group_mae':float(v['abs'].max()),'group_rmse_mean':float(np.sqrt(v.square).mean()),'bias':float(v.bias.mean()),'groups':len(v),'rows':len(d),'by_group':v.reset_index().to_dict('records')}
def fit(case,kind,d):
 y=d.target.to_numpy();w=1/d.group.map(d.group.value_counts()).to_numpy();w=w/w.mean();m={'case':case,'kind':kind,'coef':[],'training_groups':sorted(d.group.unique()),'training_rows':len(d),'training_ids_sha256':hashlib.sha256('\n'.join(d.sample_id).encode()).hexdigest()}
 fixed={'persistence','linear','zero','unit_yield','stoichiometric','lag2_mean','half_endowment'}
 if kind in fixed:return m
 bounds={74:{'mm':([30,3],[.00001,.001],[1e5,1e4]),'saturation':([30],[.1],[1e5]),'accelerating':([0,10],[-.99,.1],[10,500]),'power':([1,1],[.01,.1],[10,2]),'curvature':([5],[.01],[300]),'dose_saturation':([3,0],[-3,-2],[12,2]),'physical_saturation':([3,.5],[-3,0],[12,2])},85:{'saturation':([20,1],[.01,.001],[500,5])},87:{}}
 if kind in bounds[case]:
  x0,lo,hi=bounds[case][kind]
  def residual(p):return (predict(dict(m,coef=p.tolist()),d)-y)*np.sqrt(w)
  res=least_squares(residual,x0,bounds=(lo,hi),max_nfev=3000,xtol=1e-10,ftol=1e-10,gtol=1e-10);m['coef']=res.x.tolist();m['optimizer']={'success':bool(res.success),'cost':float(res.cost),'optimality':float(res.optimality),'bounds':[lo,hi]};return m
 X=features(case,kind,d);offset=np.zeros(len(d))
 if case==74 and kind!='flexible':offset=d.calibration_F6.to_numpy()
 if case==87 and kind!='flexible':offset=d.own_previous.to_numpy()
 scale=np.sqrt(np.average(X*X,axis=0,weights=w));scale=np.maximum(scale,1e-8);Z=X/scale;alpha=1.0 if kind=='flexible' else 1e-7
 coef=np.linalg.solve(Z.T@(w[:,None]*Z)+alpha*np.eye(X.shape[1]),Z.T@(w*(y-offset)))/scale
 m['coef']=coef.tolist();m['fit_method']='group-weighted ridge least squares; fixed penalty';m['ridge_alpha']=alpha;m['feature_rms']=scale.tolist();return m

def evaluate(case,kind,d):
 y=np.zeros(len(d));states={}
 for f in sorted(d.fold.unique()):
  train=d[d.fold!=f];test=d[d.fold==f];model=fit(case,kind,train);y[d.fold==f]=predict(model,test);states[f]=model
 return metric(d,y),y,states,fit(case,kind,d)
def main():
 case=int(HERE.name.split('-')[-1]);cmd=sys.argv[1]
 if cmd=='freeze':
  b=json.loads((HERE/'BASELINES.json').read_text());attempts=[json.loads(p.read_text()) for p in sorted(HERE.glob('attempts/attempt-*/metrics.json'))]
  if len(attempts)<5:raise ValueError('At least5 attempts required')
  if any(a['prediction_gain'] for a in attempts[-2:]):raise ValueError('Continue: last2 attempts must provide no >1% gain, absent other justified gain')
  candidates=[(k,v['metrics']['primary_error'],len(v['model']['coef'])) for k,v in b.items()]+[(a['model_name'],a['primary_error'],a['parameter_count']) for a in attempts];best=min(x[1] for x in candidates);eligible=[x for x in candidates if x[1]<=best*1.01];selected=sorted(eligible,key=lambda x:(x[2],x[1],x[0]))[0][0]
  files=['PROTOCOL.json','SPLITS.json','SOURCE_MANIFEST.json','native.py','run.py','develop.py','BASELINES.json']+[str(p.relative_to(HERE)) for p in HERE.glob('attempts/attempt-*/*') if p.is_file()];write(HERE/'FREEZE.json',{'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selected':selected,'selection':'minimum development OOF group-MAE within1% simpler','candidates':candidates,'stopping':'At least5 material attempts and two consecutive candidates did not improve incumbent development MAE by >1%; no identified robust/interpretive gain justifies expansion.','confirmation_opened':False,'assets':[{'path':f,'sha256':hashfile(HERE/f)} for f in files]});print('Frozen selected',selected);return
 d=native.prepare(Path(sys.argv[2]));d=d[d.partition=='development'].reset_index(drop=True)
 if cmd=='baseline':
  families={74:['persistence','linear','mm','flexible'],85:['zero','unit_yield','stoichiometric','global_yield','flexible'],87:['persistence','lag2_mean','half_endowment','flexible']}[case];out={}
  for k in families:
   m,p,fold,model=evaluate(case,k,d);out['baseline_'+k]={'metrics':m,'model':model,'fold_states':fold};print(case,k,round(m['primary_error'],6))
  write(HERE/'BASELINES.json',out);return
 kind=sys.argv[3];hyp=sys.argv[4];folders=list(HERE.glob('attempts/attempt-*'));n=len(folders)+1;p=HERE/'attempts'/f'attempt-{n:03}';p.mkdir(parents=True,exist_ok=False);before=json.loads((HERE/'BASELINES.json').read_text());past=[json.loads(z.read_text()) for z in sorted(HERE.glob('attempts/attempt-*/metrics.json'))];oldbest=min([v['metrics']['primary_error'] for v in before.values()]+[x['primary_error'] for x in past]);prior='No earlier attempt; initial test beyond fixed baselines.' if not past else 'Prior development evidence: '+', '.join(x['model_name']+' MAE='+format(x['primary_error'],'.6g') for x in past)+'. Incumbent='+format(oldbest,'.6g')+'.'
 config={'attempt':n,'kind':kind,'hypothesis':hyp,'created_before_fit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent_attempt':n-1 if n>1 else None,'prior_development_evidence':prior,'primary':'group-balanced physical MAE','falsification':'Must improve matched-history simple/domain/flexible controls on whole-group OOF validation; added coefficients do not identify causality.'};write(p/'config.json',config);(p/'HYPOTHESIS.md').write_text('# Hypothesis\n\n'+hyp+'\n\n'+prior+'\n\nWritten before this candidate fit. Confirmation outcomes are not scored by this program.\n');m,y,fold,state=evaluate(case,kind,d);name=f'attempt_{n:03}_{kind}';m.update(model_name=name,parameter_count=len(state['coef']),prediction_gain=m['primary_error']<oldbest*.99,baseline_incumbent_before=oldbest,hypothesis=hyp);write(p/'metrics.json',m);write(p/'model.json',state);write(p/'fold_states.json',fold);q=d[['sample_id','group','target','fold']].copy();q['prediction']=y;q.to_csv(p/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});(p/'REPORT.md').write_text('# Attempt '+str(n)+'\n\n'+hyp+'\n\n'+prior+'\n\nGroup-held-out MAE: '+format(m['primary_error'],'.8g')+'. Worst group: '+format(m['worst_group_mae'],'.8g')+'. Parameter count: '+str(m['parameter_count'])+'.\n\n'+('Prediction gain exceeded1%.' if m['prediction_gain'] else 'No >1% improvement over the incumbent; candidate retained as negative/comparative evidence.')+' Parameters and every fold state are saved. Effects remain conditional associations; this fit cannot establish a unique mechanism.\n');print(case,name,round(m['primary_error'],6),'gain',m['prediction_gain'],'coef',state['coef'])
if __name__=='__main__':main()
