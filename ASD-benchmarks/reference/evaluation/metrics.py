"""Common, declarative numerical scoring. Independent groups define the weights."""
import numpy as np
import pandas as pd

def weights(d,task):
 if not len(d):return np.array([],float)
 hierarchy=task['aggregation']['hierarchy']
 weight_column=task['aggregation'].get('within_group_weight')
 if weight_column:
  if hierarchy!=['group']:raise ValueError('Within-group survey weights currently require the group hierarchy')
  if weight_column not in d:raise ValueError('Missing declared observation weight: '+weight_column)
  a=pd.to_numeric(d[weight_column],errors='raise').to_numpy(float)
  if not np.isfinite(a).all()or np.any(a<=0):raise ValueError('Observation weights must be finite and positive')
  total=d.assign(_w=a).groupby('group')._w.transform('sum').to_numpy(float)
  if not np.isfinite(total).all()or np.any(total<=0):raise ValueError('Invalid within-group weight sum')
  return (a/total)/d.group.nunique()
 if hierarchy==['group','particle']:
  return 1/(d.group.nunique()*d.groupby('group').particle.transform('nunique').to_numpy()*d.groupby(['group','particle']).target.transform('size').to_numpy())
 if hierarchy!=['group']:raise ValueError('Unsupported aggregation hierarchy')
 return 1/(d.group.nunique()*d.groupby('group').target.transform('size').to_numpy())

def group_mean(d,cols,task):
 if task['aggregation'].get('within_group_weight'):
  w=weights(d,task);z=d[cols].mul(w,axis=0);z['group']=d.group.to_numpy();mass=pd.Series(w,index=d.index).groupby(d.group).sum();return z.groupby('group')[cols].sum().div(mass,axis=0)
 if task['aggregation']['hierarchy']==['group','particle']:return d.groupby(['group','particle'])[cols].mean().groupby('group').mean()
 return d.groupby('group')[cols].mean()

def quantile(values,w,q):
 order=np.argsort(values,kind='stable');return float(np.interp(q,np.cumsum(w[order])/w.sum(),np.asarray(values)[order]))

def score(d,prediction,task):
 if not len(d):return None,[]
 d=d.copy();v=np.asarray(prediction,float);truth=d.target.to_numpy(float)
 if v.shape!=truth.shape or not np.isfinite(v).all()or not np.isfinite(truth).all():raise ValueError('Scoring requires aligned finite values')
 with np.errstate(over='ignore',invalid='ignore'):error=v-truth;ae=abs(error);se=error**2
 if not np.isfinite(np.c_[error,ae,se]).all():raise ValueError('Nonfinite error arithmetic')
 d['absolute_error']=ae;d['squared_error']=se;d['bias']=error;w=weights(d,task)
 g=group_mean(d,['absolute_error','squared_error','bias'],task);kind=task['metric_kind'];eligible=np.ones(len(d),bool)
 if kind in['log_transit','log_mae']:
  if np.any(v<=0):raise ValueError('Log task requires positive predictions')
  eligible=truth>0
  if kind=='log_transit'and not eligible.all():raise ValueError('Transit target must be positive')
  if eligible.any():
   z=d.loc[eligible].copy();z['log_error']=abs(np.log(v[eligible])-np.log(truth[eligible]));primary=group_mean(z,['log_error'],task).log_error
  else:primary=pd.Series(dtype=float)
 elif kind=='rmse':primary=np.sqrt(g.squared_error)
 elif kind=='normalized_mae':
  if 'condition_scale'not in d:raise ValueError('Missing frozen training-fold normalization')
  scales=d.groupby('group').condition_scale.first()
  if not np.isfinite(scales).all()or(scales<=0).any():raise ValueError('Invalid training-fold scale')
  primary=g.absolute_error/scales
 elif kind=='mae':primary=g.absolute_error
 elif kind=='brier':
  if not np.isin(truth,[0.,1.]).all()or np.any((v<0)|(v>1)):raise ValueError('Brier scoring requires binary truth and probabilities in [0,1]')
  primary=g.squared_error
 else:raise ValueError('Unsupported metric kind: '+kind)
 p90=quantile(ae,w,.9);tail=ae>=p90
 result={
 'primary_error':float(primary.mean())if len(primary)else None,'primary_units':task['primary_units'],
 'primary_eligible_rows':int(eligible.sum()),'primary_eligible_groups':len(primary),
 'primary_undefined_reason':None if len(primary)else'No positive target among covered rows; physical errors remain valid',
 'group_balanced_mae':float(w@ae),'group_balanced_rmse':float(np.sqrt(w@se)),
 'mean_group_rmse':float(np.sqrt(g.squared_error).mean()),'group_balanced_bias':float(w@error),
 'median_absolute_error':quantile(ae,w,.5),'p90_absolute_error':p90,'p95_absolute_error':quantile(ae,w,.95),
 'maximum_absolute_error':float(ae.max()),'tail_conditional_mae_p90':float(w[tail]@ae[tail]/w[tail].sum()),
 'worst_group_mae':float(g.absolute_error.max()),'groups':len(g),'rows':len(d),'error_units':task['error_units'],
 'negative_prediction_count':int((v<0).sum()),'negative_values_are_not_automatically_physical_violations':True,
 'nonpositive_targets_retained':int((truth<=0).sum())if kind=='log_mae'else None,
 }
 if kind in['log_mae','log_transit']and len(primary):result['multiplicative_error_scale']=float(np.exp(min(result['primary_error'],700)))
 if kind=='brier':result['probability_diagnostics']=probability_metrics(d,v,task)
 rows=[]
 for name,r in g.iterrows():
  rows.append({'group':str(name),'mae':float(r.absolute_error),'rmse':float(np.sqrt(r.squared_error)), 'bias':float(r.bias),'primary_error':float(primary.loc[name])if name in primary.index else None,'rows':int((d.group==name).sum())})
 return result,rows

def probability_metrics(d,v,task):
 """ASD6 probability extension 1.0; no change to existing task arithmetic."""
 truth=d.target.to_numpy(float);v=np.asarray(v,float);w=weights(d,task)
 if not np.isin(truth,[0.,1.]).all()or not np.isfinite(v).all()or np.any((v<0)|(v>1)):raise ValueError('Invalid binary probability inputs')
 certainty_error=((truth==1)&(v==0))|((truth==0)&(v==1))
 assigned=np.where(truth==1,v,1-v);bins=[]
 for i in range(10):
  keep=(v>=i/10)&((v<(i+1)/10)if i<9 else(v<=1))
  mass=float(w[keep].sum())
  if mass:bins.append({'lower':i/10,'upper':(i+1)/10,'weight':mass,'rows':int(keep.sum()),'mean_probability':float(w[keep]@v[keep]/mass),'event_frequency':float(w[keep]@truth[keep]/mass)})
 declaration=task.get('binary_decision_threshold',{});threshold=float(declaration.get('value',.5))
 if not 0<threshold<1:raise ValueError('Binary decision threshold must be in(0,1)')
 registered=declaration.get('frozen_before_confirmation')is True and bool(declaration.get('provenance'))
 event=event_metrics(d,v,task,threshold);event.update(status='registered_binary_decision_threshold'if registered else'conventional_descriptive_threshold',threshold_registered_before_outcomes=registered,threshold_provenance=declaration.get('provenance'),operational_claim=False)
 return {'extension_version':'asd6-probability/1.1','brier':float(w@((v-truth)**2)),'log_loss_nats':None if certainty_error.any()else float(w@(-np.log(assigned))), 'log_loss_undefined_reason':'Infinite log loss from certainty assigned to the wrong event'if certainty_error.any()else None,'certainty_error_rows':int(certainty_error.sum()),'clipped_log_loss_nats':float(w@(-np.log(np.maximum(assigned,1e-12)))),'clipping_epsilon':1e-12,'calibration_bins':bins,'calibration_status':'descriptive on exposed cohort; dependent trial rows are not independent populations','binary_events':event}

def event_metrics(d,v,task,threshold):
 if not np.isfinite(threshold):raise ValueError('Event threshold must be finite')
 w=weights(d,task);y=d.target.to_numpy(float)>=threshold;p=np.asarray(v)>=threshold
 tp=float(w@(y&p));fp=float(w@(~y&p));fn=float(w@(y&~p));tn=float(w@(~y&~p));denom=2*tp+fp+fn
 return{'event':'target >= threshold','threshold':threshold,'target_units':task['target_units'],
 'weighted_confusion':{'tp':tp,'fp':fp,'fn':fn,'tn':tn},'row_confusion':{'tp':int((y&p).sum()),'fp':int((~y&p).sum()),'fn':int((y&~p).sum()),'tn':int((~y&~p).sum())},
 'precision':tp/(tp+fp)if tp+fp else None,'recall':tp/(tp+fn)if tp+fn else None,'specificity':tn/(tn+fp)if tn+fp else None,
 'f1':2*tp/denom if denom else None,
 'undefined_reasons':{'precision':None if tp+fp else'No predicted positives','recall':None if tp+fn else'No observed positives','specificity':None if tn+fp else'No observed negatives','f1':None if denom else'No observed or predicted positives'},
 'operational_claim':False,'status':'exploratory_user_threshold','threshold_registered_before_outcomes':False}

def interval_metrics(d,v,lo,hi,level,task):
 if not(0<level<1):raise ValueError('Interval level must be in(0,1)')
 v=np.asarray(v);lo=np.asarray(lo);hi=np.asarray(hi);truth=d.target.to_numpy(float);w=weights(d,task);width=hi-lo
 with np.errstate(over='ignore'):proper=width+2/(1-level)*(np.maximum(lo-truth,0)+np.maximum(truth-hi,0))
 if not np.isfinite(proper).all():raise ValueError('Nonfinite interval arithmetic')
 risk=[]
 for fraction in[1.,.9,.75,.5,.25]:
  cutoff=quantile(width,w,fraction);keep=width<=cutoff;value,_=score(d.loc[keep],v[keep],task)
  risk.append({'requested_coverage':fraction,'achieved_group_weighted_coverage':float(w[keep].sum()),'width_cutoff':cutoff,'conditional_mae':value['group_balanced_mae'],'ties_retained':True})
 return{'nominal_level':level,'group_balanced_coverage':float(w@((truth>=lo)&(truth<=hi))), 'mean_width':float(w@width),'proper_interval_score':float(w@proper),'endpoint_units':task['target_units'],'width_error_units':task['error_units'],'calibration_is_descriptive':True,'risk_coverage':risk}
