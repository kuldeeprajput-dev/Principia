"""Confirmation-only evaluation: verifies frozen development artifacts; never fits."""
from pathlib import Path
import json,hashlib,datetime,shutil,sys,platform
import numpy as np
import pandas as pd
import native
from run import predict
P=Path(__file__).resolve().parent
EQUATIONS={
'persistence':'74: F_hat(t)=F6; 87: c_hat(t)=c(t-1)',
'linear':'F_hat=F6+v6*(t-6)',
'mm':'F_hat=V*S*t/(K+S)',
'saturation':'74: F_hat=F6+v6*tau*(1-exp(-(t-6)/tau));85: P_hat=max(0,A*(1-exp(-q*max(E0-E,0)/A)))',
'accelerating':'F_hat=F6+v6*d+a*v6*(d-tau*(1-exp(-d/tau))),d=t-6',
'power':'F_hat=F6+a*v6*6*((1+d/6)^p-1)/p',
'curvature':'F_hat=F6+v6*d+c6*tau*(d-tau*(1-exp(-d/tau)))',
'dose_saturation':'F_hat=F6+v6*tau*(1-exp(-d/tau)),tau=exp(a+b*log(S));S is numerical concentration in uM',
'physical_saturation':'F_hat=F6+v6*tau*(1-exp(-d/tau)),tau=exp(a+b*log(S)),b>=0',
'slope_gate':'F_hat=F6+d*(a*v6+b*6*c6)',
'slope_only':'F_hat=F6+a*d*v6',
'unit_yield':'P_hat=max(0,E0-E)',
'stoichiometric':'P_hat=max(0,(76.05/62.07)*(E0-E))',
'global_yield':'P_hat=max(0,q*(E0-E))',
'ph_yield':'P_hat=max(0,(E0-E)*(a+b*(pH-7)))',
'loss_flux':'P_hat=max(0,a*(E0-E)+b*t/100)',
'composition':'P_hat=max(0,(E0-E)*(a+b*glucose+c*acetate))',
'acid':'P_hat=max(0,q*(E0-E)/(1+10^(3.83-pH)))',
'zero':'P_hat=0',
'lag2_mean':'c_hat=clip((c(t-1)+c(t-2))/2,0,e)',
'half_endowment':'c_hat=e/2',
'focal':'c_hat=clip(c_prev+a*(e/2-c_prev),0,e)',
'reciprocal':'c_hat=clip(c_prev+a*(e*c_peer_prev/e_peer-c_prev),0,e)',
'coordination':'c_hat=clip(c_prev+a*(required-c_prev),0,e)',
'success_gate':'c_hat=clip(c_prev+a*(required-c_prev)*(1-success)+b*(e/2-c_prev)*(1-success)+c*(e/2-c_prev)*success,0,e)',
'history':'c_hat=clip(c_prev+a*(own_history_mean-c_prev)+b*(required-c_prev)*(1-success),0,e)',
'flexible':'Frozen ridge polynomial: y_hat=phi(x)^T beta; exact dimensionless feature order/scales in run.features and coefficients in rules.json;85 nonnegative,87 clipped0..endowment'}
def write(p,o):p.write_text(json.dumps(o,indent=2,allow_nan=False))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scores(d,y):
 e=y-d.target.to_numpy();g=pd.DataFrame({'group':d.group.to_numpy(),'mae':abs(e),'mse':e*e,'bias':e}).groupby('group').mean();return {'primary_error':float(g.mae.mean()),'mean_group_absolute_error':float(g.mae.mean()),'groups':len(g),'scored_rows':len(d),'assigned_rows':len(d)},g

def main():
 case=int(P.name.split('-')[-1]);freeze=json.loads((P/'FREEZE.json').read_text())
 for a in freeze['assets']:
  if sha(P/a['path'])!=a['sha256']:raise ValueError('Freeze mismatch: '+a['path'])
 c=json.loads((P/'SETTINGS.json').read_text());prot=json.loads((P/'PROTOCOL.json').read_text());d=native.prepare(Path(sys.argv[1]));q=d[d.partition=='confirmation'].reset_index(drop=True);base=json.loads((P/'BASELINES.json').read_text());states={k:v['model'] for k,v in base.items()};devmetrics={k:v['metrics']['primary_error'] for k,v in base.items()};attempts=[]
 for a in sorted(P.glob('attempts/attempt-*')):
  m=json.loads((a/'metrics.json').read_text());states[m['model_name']]=json.loads((a/'model.json').read_text());devmetrics[m['model_name']]=m['primary_error'];attempts.append(m)
 selected=freeze['selected'];models={'reference':states[selected],**states}
 for k,m in models.items():
  m['equation']=EQUATIONS[m['kind']]
  if m['kind']=='persistence':m['equation']='F_hat(t)=F6' if case==74 else 'c_hat(i,t)=c(i,t-1)'
  if m['kind']=='saturation':m['equation']='F_hat=F6+v6*tau*(1-exp(-(t-6)/tau))' if case==74 else 'P_hat=max(0,A*(1-exp(-q*max(E0-E,0)/A)))'
  m['coefficients_order']='Expression and run.features define exact order; raw double precision coefficients in coef.'
 out=P/'package';out.mkdir(exist_ok=True);(out/'data').mkdir(exist_ok=True);(out/'evidence').mkdir(exist_ok=True)
 x=q[['sample_id','group',*c['inputs']]].copy();obs=q[['sample_id','group','target','source_anchor','calibration_anchor','eligibility_reason']].copy();pred=q[['sample_id','group']].copy();metrics=[];groups=[]
 for k,m in models.items():
  pred[k]=predict(m,x);s,g=scores(q,pred[k].to_numpy());s.update(model=k,primary_units=c['unit']);metrics.append(s);g=g.reset_index();g['model']=k;g['scored_rows']=g.group.map(q.group.value_counts());groups.append(g)
 for name,z in [('data/inputs.csv.gz',x),('data/observations.csv.gz',obs),('evidence/predictions.csv.gz',pred)]:z.to_csv(out/name,index=False,compression={'method':'gzip','mtime':0})
 pd.DataFrame(metrics).to_csv(out/'evidence/metrics.csv',index=False);pd.concat(groups).to_csv(out/'evidence/by_group.csv',index=False)
 rules={'case_id':P.name,'input_columns':list(c['inputs']),'numeric_columns':list(c['inputs']),'input_units':c['inputs'],'source':{'landing_url':c['url'],'publication':c['pub']},'target':c['target'],'units':c['unit'],'metric_units':c['unit'],'metric_kind':'mae','assigned_rows':len(q),'selected_development_model':selected,'models':models,'missingness_policy':'No imputation; explicit native eligibility; all packaged predictors finite','classification':'Reproduction/validated scoped comparison; novelty not established','fresh_confirmation_for_future_users':False,'training_scope':'Coefficients fit development only; group/fold states in research history','limits':c['limits']};write(out/'rules.json',rules)
 task={'target':c['target'],'target_units':c['unit'],'error_units':c['unit'],'metric_kind':'mae','permitted_inputs':list(c['inputs']),'input_units':c['inputs'],'numeric_columns':list(c['inputs']),'timing_contract':c['timing'],'calibration':c['timing'],'independent_unit':c['grouping'],'scope_limits':c['limits'],'source_url':c['url'],'source_license':'CC-BY-4.0','exposure':{'status':'exposed_after_local_confirmation','original_audit':c['audit'],'fresh_for_future_users':False,'new_independent_experiments':False},'uncertainty_policy':prot['uncertainty'],'applicability':'Only stated experimental conditions and declared information budget; no universal or intervention claim','physical_bounds':('0<=prediction<=endowment' if case==87 else 'prediction>=0' if case==85 else 'source instrument response; no calibrated fluorophore ceiling')};write(out/'task_spec.json',task)
 shutil.copy(P/'run.py',out/'run.py');(out/'requirements.txt').write_text('numpy\npandas\n');write(P/'FINAL_VALIDATION.json',{'evaluated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':sha(P/'FREEZE.json'),'selected':selected,'confirmation_groups':sorted(q.group.unique()),'confirmation_rows':len(q),'metrics':metrics,'freshness':task['exposure'],'all_states_frozen_before_scores':True,'fitting_performed':False,'case_id':P.name});write(P/'DEPENDENCIES.json',{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'fitting':'scipy','native_xlsx':'openpyxl' if case==87 else 'not required'})
 # This summary is written only after immutable selection and stopping.
 lines=['# '+c['title'],'','Selected on development: `'+selected+'`. Confirmation cannot change selection.','','| Model | OOF development MAE | Confirmation MAE |','|---|---:|---:|']
 for z in metrics[1:]:lines.append('| '+z['model']+' | '+format(devmetrics[z['model']],'.7g')+' | '+format(z['primary_error'],'.7g')+' |')
 lines+=['','Attempts: '+str(len(attempts))+'. '+freeze['stopping'],'',c['audit'],'','See each attempt for hypothesis, parent evidence, negative outcomes, coefficients, fold predictions and native anchors.'];(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(case,selected,'confirmation',metrics[0]['primary_error'],'groups',len(q.group.unique()),'rows',len(q));print(pd.DataFrame(metrics)[['model','primary_error']].to_string(index=False))
if __name__=='__main__':main()
