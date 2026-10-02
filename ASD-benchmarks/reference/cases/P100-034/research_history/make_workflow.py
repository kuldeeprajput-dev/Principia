from pathlib import Path
W=Path(__file__).resolve().parents[1]
s='''"""Development-only grouped fitting; separate frozen confirmation."""
from pathlib import Path
import json,sys,hashlib,datetime
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import native
from run import predict
from fit import fit,BASE
HERE=Path(__file__).resolve().parent
CASE=int(HERE.name.split('-')[-1]);SPEC=json.loads((HERE/'SPEC.json').read_text())
def write(p,o):p.write_text(json.dumps(o,indent=2,allow_nan=False))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def metrics(d,p):
 y=d.target.to_numpy();v=pd.DataFrame(dict(group=d.group,mae=np.abs(p-y),mse=(p-y)**2,bias=p-y)).groupby('group').mean();kind=SPEC['kind'];err=float(v.mse.mean()) if kind=='brier' else float(v.mae.mean());out=dict(primary_error=err,mean_group_absolute_error=float(v.mae.mean()),group_rmse_mean=float(np.sqrt(v.mse).mean()),worst_group_mae=float(v.mae.max()),bias=float(v.bias.mean()),groups=len(v),rows=len(d),by_group=v.reset_index().to_dict('records'))
 if CASE==89:
  pred=p>=.5;true=y==1;tp=int(np.sum(pred&true));fp=int(np.sum(pred&~true));fn=int(np.sum(~pred&true));tn=int(np.sum(~pred&~true));out['events']=dict(threshold=.5,meaning='standard equal-cost classification, not an industrial acceptance limit',tp=tp,fp=fp,fn=fn,tn=tn,precision=tp/(tp+fp) if tp+fp else None,recall=tp/(tp+fn) if tp+fn else None,specificity=tn/(tn+fp) if tn+fp else None,f1=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else None);ll=-(y*np.log(np.clip(p,1e-12,1))+(1-y)*np.log(np.clip(1-p,1e-12,1)));out['group_log_loss']=float(pd.DataFrame({'g':d.group,'ll':ll}).groupby('g').ll.mean().mean());out['calibration_bins']=[dict(lower=float(i/10),upper=float((i+1)/10),n=int(((p>=i/10)&(p<((i+1)/10+1e-12))).sum()),mean_probability=float(p[(p>=i/10)&(p<(i+1)/10+1e-12)].mean()) if ((p>=i/10)&(p<(i+1)/10+1e-12)).any() else None,frequency=float(y[(p>=i/10)&(p<(i+1)/10+1e-12)].mean()) if ((p>=i/10)&(p<(i+1)/10+1e-12)).any() else None) for i in range(10)]
 return out
def evaluate(k,d):
 pred=np.zeros(len(d));states={}
 for f in sorted(d.fold.unique()):
  tr=d[d.fold!=f];va=d[d.fold==f];m=fit(CASE,k,tr);pred[d.fold==f]=predict(m,va);states[str(f)]=m
 return metrics(d,pred),pred,states,fit(CASE,k,d)
def figure(path,d,p):
 fig,ax=plt.subplots(figsize=(5,3.3));ax.scatter(d.target,p,s=8,alpha=.45);lo=min(d.target.min(),p.min());hi=max(d.target.max(),p.max());ax.plot([lo,hi],[lo,hi],color='black',lw=1);ax.set(xlabel='Observed ('+SPEC['unit']+')',ylabel='OOF prediction',title='Development groups only');fig.tight_layout();fig.savefig(path,dpi=140);plt.close(fig)
def main():
 cmd=sys.argv[1]
 if cmd=='freeze':
  b=json.loads((HERE/'BASELINES.json').read_text());a=[json.loads(p.read_text()) for p in sorted(HERE.glob('attempts/attempt-*/metrics.json'))]
  if len(a)<5 or any(v['prediction_gain'] for v in a[-2:]):raise ValueError('Need >=5 attempts and two consecutive no-gain attempts')
  cand=[(k,v['metrics']['primary_error'],len(v['model']['coef'])) for k,v in b.items()]+[(v['model_name'],v['primary_error'],v['parameter_count']) for v in a];best=min(x[1] for x in cand);selected=min([x for x in cand if x[1]<=best*1.01],key=lambda x:(x[2],x[1],x[0]))[0];files=[p for p in HERE.iterdir() if p.is_file() and (p.suffix in ['.py','.json','.md']) and p.name not in ['FREEZE.json']]+[p for p in (HERE/'attempts').rglob('*') if p.is_file()];write(HERE/'FREEZE.json',dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),selected=selected,candidates=cand,confirmation_opened=False,stopping='At least five substantive candidates; two final consecutive attempts failed to improve primary development error>1%. Their mechanistic/robustness challenges do not justify another hypothesis within these data. No confirmation score consulted.',assets=[dict(path=str(p.relative_to(HERE)),sha256=sha(p)) for p in sorted(files)]));print(CASE,'FREEZE',selected);return
 d=native.prepare(Path(sys.argv[2]));d=d[d.partition=='development'].reset_index(drop=True)
 if cmd=='baseline':
  b={};q=d[['sample_id','group','fold','target']].copy()
  for k in BASE[CASE]:
   m,p,f,state=evaluate(k,d);name='baseline_'+k;b[name]=dict(metrics=m,model=state,fold_states=f);q[name]=p;print(CASE,k,round(m['primary_error'],7))
  write(HERE/'BASELINES.json',b);q.to_csv(HERE/'BASELINE_PREDICTIONS.csv.gz',index=False,compression={'method':'gzip','mtime':0});return
 k,hyp=sys.argv[3:5];a=sorted(HERE.glob('attempts/attempt-*/metrics.json'));n=len(a)+1;prior=[json.loads(p.read_text()) for p in a];base=json.loads((HERE/'BASELINES.json').read_text());old=min([v['metrics']['primary_error'] for v in base.values()]+[v['primary_error'] for v in prior]);p=HERE/'attempts'/f'attempt-{n:03}';p.mkdir(parents=True,exist_ok=False);history='; '.join(v['model_name']+'='+format(v['primary_error'],'.7g') for v in prior) or 'Initial post-baseline hypothesis';cfg=dict(attempt=n,kind=k,hypothesis=hyp,parent_attempt=n-1 if n>1 else None,prior_development=history,incumbent=old,created_before_fit_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),falsification='Improve whole-group development prediction or supported robustness/interpretation; reject unique mechanism if parameter rank/boundaries or competing explanations contradict it.');write(p/'config.json',cfg);(p/'HYPOTHESIS.md').write_text('# Hypothesis\\n\\n'+hyp+'\\n\\nPrior development: '+history+'; incumbent '+str(old)+'.\\n\\nWhole-group validation; identical calibration budget; confirmation unopened.\\n');m,y,f,state=evaluate(k,d);m.update(model_name=f'attempt_{n:03}_{k}',parameter_count=len(state['coef']),prediction_gain=m['primary_error']<old*.99,incumbent_before=old);write(p/'metrics.json',m);write(p/'model.json',state);write(p/'fold_states.json',f);q=d[['sample_id','group','target','fold']].copy();q['prediction']=y;q.to_csv(p/'predictions.csv.gz',index=False,compression={'method':'gzip','mtime':0});figure(p/'development.png',d,y);(p/'REPORT.md').write_text('# Attempt '+str(n)+'\\n\\n'+hyp+'\\n\\n'+history+'\\n\\nPrimary group-balanced error: '+str(m['primary_error'])+'. Previous incumbent: '+str(old)+'. Gain>1%: '+str(m['prediction_gain'])+'. Worst-group MAE: '+str(m['worst_group_mae'])+'.\\n\\nEquation: '+state['equation']+'\\n\\nFull coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.\\n');print(CASE,m['model_name'],round(m['primary_error'],7),'gain',m['prediction_gain'],'params',state['coef'])
if __name__=='__main__':main()
'''
for c in [29,32,34,76,79,89]:(W/f'P100-{c:03}'/'develop.py').write_text(s)
