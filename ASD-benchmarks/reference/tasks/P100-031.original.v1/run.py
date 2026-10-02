"""Portable frozen equations. No fitting, network access, or observation lookup."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.special import expit

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def physical(d,c):
 z={k:d[k].to_numpy(float) for k in d.columns if k not in ['target','sample_id','group'] and pd.api.types.is_numeric_dtype(d[k])};z['one']=np.ones(len(d))
 if c==16:
  z.update(p1=z['inflation1'],p3=z['inflation3'],p12=z['inflation12'],h=z['housing1'],m=z['medical1'],j=z['jobs1'],f=z['mfg1'],i=z['info1'])
  z.update(inertia=z['p1']-z['p12'],sector_gap=(z['h']+z['m'])/2-z['p1'],dispersion=np.abs(z['h']-z['m']),accel=z['p1']-z['p3'],shock_up=np.maximum(z['p1']-z['p12'],0),shock_down=np.minimum(z['p1']-z['p12'],0),job_loss=np.minimum(z['j'],0),job_gain=np.maximum(z['j'],0))
 if c in [14,15]:
  z.update(log_resource=np.log(z['income_proxy']/np.sqrt(z['household_size'])),log_percapita=np.log(z['income_proxy']/z['household_size']),log_income=np.log(z['income_proxy']),log_size=np.log(z['household_size']),age_mid=(z['age']-45)/20)
  z.update(age_sq=z['age_mid']**2,resource_shock=z['log_resource']*z['shock'],poor_shock=np.maximum(3-z['log_resource'],0)*z['shock'],low_resource=np.maximum(3-z['log_resource'],0),high_resource=np.maximum(z['log_resource']-3,0))
 if c==42:
  z.update(digital=z['mobile']+z['web'],both=z['mobile']*z['web'],older=np.maximum(z['age_category']-4,0),mobile_age=z['mobile']*(z['age_category']-4),web_age=z['web']*(z['age_category']-4),access_mobile=z['branch_present']*z['mobile'],closure_older=z['branch_closed']*np.maximum(z['age_category']-4,0))
 if c==10:
  z.update(log_age=np.log1p(z['age_days']),log_batch=np.log1p(z['batch_size']),age_cna=np.log1p(z['age_days'])*z['cna_score'],load_age=np.log1p(z['batch_size'])/(1+z['age_days']),old=np.maximum(np.log1p(z['age_days'])-np.log(7),0),young=np.minimum(np.log1p(z['age_days']),np.log(7)))
 if c==17:
  z.update(log_rms=np.log(z['rms_s']),log_n=np.log(z['phases']),log_stations=np.log(z['stations']),depth_abs=np.abs(z['depth_km']))
  z.update(log_geometry=.5*np.log1p((z['dmin_km']/(1+z['depth_abs']))**2),gap_loss=-np.log(np.maximum(1-z['gap_deg']/360,.02)),log_depth=np.log1p(z['depth_abs']),inv_info=z['log_rms']-.5*z['log_n'],fixed10=(np.abs(z['depth_km']-10)<.0001).astype(float),shallow=(z['depth_km']<5).astype(float))
 if c==18:
  z.update(log_length=np.log1p(z['length_km']),log_width=np.log1p(z['width_km']*1000),log_area=np.log1p(z['length_km']*z['width_km']),log_duration=np.log1p(z['duration_min']),sinmonth=np.sin(2*np.pi*z['month']/12),cosmonth=np.cos(2*np.pi*z['month']/12))
  z.update(area_sq=z['log_area']**2,shape=z['log_length']-z['log_width'],area_lat=z['log_area']*(z['latitude']-35)/10)
 if c==39:
  z.update(experience=np.maximum(z['age']-z['education']-6,0)/10,school=z['education']-12,degree=np.maximum(z['education']-12,0),older=np.maximum(z['age']-50,0)/10)
  z.update(exp_sq=z['experience']**2,school_sq=z['school']**2,jp_school=z['japan']*z['school'],jp_exp=z['japan']*z['experience'],jp_exp_sq=z['japan']*z['experience']**2,school_exp=z['school']*z['experience'])
 if c==31:
  z.update(log_pilot=np.log(z['pilot_seconds']),log_gates=np.log1p(z['pilot_gates']),log_depth=np.log1p(z['pilot_depth']),log_qubits=np.log(z['qubits']),log_load=np.log(np.maximum(z['load_seconds'],1e-9)))
  z.update(parallelism=z['log_gates']-z['log_depth'],gate_qubit=z['log_gates']*z['log_qubits'],large=np.maximum(z['log_qubits']-np.log(16),0),bq_pilot=z['is_bqskit']*z['log_pilot'],tk_pilot=z['is_tket']*z['log_pilot'])
 if c==40:
  z.update(km=z['distance_km'],short=np.minimum(z['distance_km'],3),long=np.maximum(z['distance_km']-3,0),log_distance=np.log1p(z['distance_km']),sinclock=np.sin(2*np.pi*z['hour']/24),cosclock=np.cos(2*np.pi*z['hour']/24))
  z.update(km_peak=z['distance_km']*z['peak'],km_weekend=z['distance_km']*z['weekend'],km_airport=z['distance_km']*z['airport'],km_manhattan=z['distance_km']*z['manhattan'],km_sin=z['distance_km']*z['sinclock'],km_cos=z['distance_km']*z['cosclock'])
 if c==19:
  z.update(l1=z['lag1'],l3=z['lag3'],l6=z['lag6'],excess=z['lag1']-z['lag3'],decay=z['lag3']-z['lag6'],up=np.maximum(z['lag1']-z['lag3'],0),down=np.minimum(z['lag1']-z['lag3'],0),rootload=np.sqrt(z['lag3']),logload=np.log1p(z['lag3']),sine=np.sin(2*np.pi*z['month']/12),cosine=np.cos(2*np.pi*z['month']/12))
 return z

def design(model,d):
 z=physical(d,int(model['case']));X=np.column_stack([z[k] for k in model.get('features',[])]) if model.get('features') else np.zeros((len(d),0))
 if model.get('rbf'):
  s=model['rbf'];q=(np.column_stack([z[k] for k in s['columns']])-s['mean'])/s['std'];r=np.exp(-np.sum((q[:,None,:]-np.array(s['centers'])[None,:,:])**2,axis=2)/(2*s['width']**2));X=np.column_stack([np.ones(len(d)),r])
 return X,z.get(model.get('offset'),np.zeros(len(d))),z.get(model.get('scale'),np.ones(len(d)))
def link(v,name):
 if name=='logit':return expit(v)
 if name=='cloglog':return -np.expm1(-np.exp(np.clip(v,-40,30)))
 if name=='log':return np.exp(np.clip(v,-60,60))
 return v

def predict(model,d):
 if isinstance(model,str):model=json.loads((Path(__file__).resolve().parent/'rules.json').read_text())['models'][model]
 if model['type']=='pipeline':
  k=d.is_tket.to_numpy(int)+2*d.is_bqskit.to_numpy(int);a=np.array(model['log_floor']);b=np.array(model['log_scale']);power=np.asarray(model['power']);power=power[k] if power.ndim else power;return np.exp(a[k])+np.exp(b[k])*d.pilot_seconds.to_numpy(float)**power
 X,offset,scale=design(model,d);v=offset.copy() if model['type']=='fixed' else offset+scale*(X@np.asarray(model['coef']))
 y=link(v,model.get('link','identity'))
 if model.get('clip') is not None:y=np.clip(y,*model['clip'])
 if not np.isfinite(y).all():raise ValueError('Nonfinite prediction')
 return y

def loss_report(d,p,metric='mae'):
 q=d[['sample_id','group','target']].copy();q['p']=p;q['w']=d['sample_weight'].to_numpy(float) if 'sample_weight' in d else 1.;valid=np.isfinite(q.target);eligible=q[valid].copy();e=eligible.p-eligible.target;eligible['ae']=np.abs(e);eligible['se']=e*e;eligible['bias']=e
 if metric=='log_mae':
  if (eligible.target<=0).any() or (eligible.p<=0).any():raise ValueError('Nonpositive logarithmic metric input')
  eligible['main']=np.abs(np.log(eligible.p/eligible.target))
 else:eligible['main']=eligible.se if metric in ['rmse','brier'] else eligible.ae
 groups=[]
 for g,z in eligible.groupby('group'):
  w=z.w.to_numpy();mean=lambda k:float(np.average(z[k],weights=w));main=mean('main');groups.append(dict(group=str(g),primary_error=float(np.sqrt(main)) if metric=='rmse' else main,mae=mean('ae'),rmse=float(np.sqrt(mean('se'))),bias=mean('bias'),n=len(z),weight_sum=float(w.sum()),p90=float(np.quantile(z.ae,.9))))
 G=pd.DataFrame(groups)
 return dict(primary_error=float(G.primary_error.mean()),mean_group_absolute_error=float(G.mae.mean()),worst_group_error=float(G.primary_error.max()),groups=len(G),scored_rows=len(eligible),assigned_rows=len(d),per_group=groups)

def main():
 root=Path(__file__).resolve().parent;m=json.loads((root/'MANIFEST.json').read_text())
 assets=m['files']
 if not assets:raise ValueError('Empty package integrity manifest')
 seen=set()
 for x in assets:
  name=x['path'];rel=Path(name)
  if rel.is_absolute() or '..' in rel.parts or name in seen:raise ValueError('Unsafe or duplicate package asset')
  seen.add(name);f=root/rel
  if not f.resolve().is_relative_to(root.resolve()) or not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=x['sha256']:raise ValueError('Package integrity mismatch: '+name)
 rules=json.loads((root/'rules.json').read_text());d=read_table(root/'data/inputs.csv.gz');o=read_table(root/'data/observations.csv.gz');pred=read_table(root/'evidence/predictions.csv.gz');stats=read_table(root/'evidence/metrics.csv').set_index('model');joined=o.copy()
 if not d.sample_id.equals(o.sample_id) or not d.sample_id.equals(pred.sample_id):raise ValueError('Identity mismatch')
 report={}
 for key,model in rules['models'].items():
  p=predict(model,d);err=float(np.max(np.abs(p-pred[key].to_numpy())));assert np.allclose(p,pred[key],rtol=1e-11,atol=1e-9),key;score=loss_report(joined,p,rules['metric_kind']);assert np.isclose(score['primary_error'],stats.loc[key,'primary_error'],rtol=1e-11,atol=1e-10);report[key]=dict(replay_max_abs=err,primary_error=score['primary_error'])
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
