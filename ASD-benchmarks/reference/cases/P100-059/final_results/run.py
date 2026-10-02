#!/usr/bin/env python3
"""Frozen executable hypotheses. Prediction has no target access or fitting."""
from pathlib import Path
import json,argparse,hashlib
import numpy as np,pandas as pd

def read_table(p):return pd.read_csv(p,float_precision='round_trip',dtype={'sample_id':str,'group':str,'plant':str,'site':str,'study':str})
def basis(case,kind,d,knobs=None):
 knobs=knobs or {};ones=np.ones(len(d));cols=[ones];names=['1'];offset=np.zeros(len(d))
 def add(v,n):cols.append(np.asarray(v,float));names.append(n)
 if kind=='persistence':
  return np.zeros((len(d),1)),['zero increment'],d.current.to_numpy() if case==86 else d.speed.to_numpy() if case==96 else d.housing_C.to_numpy()
 if kind=='mean':return np.c_[ones],names,offset
 if case==23:
  H=np.maximum(d.H.to_numpy(float),1e-10);h=H/.02;b=1/(1+h);v=d.speed.to_numpy()/.05;load=d.load.to_numpy();pressure=load/(d.area.to_numpy()/4)
  if kind=='domain':add(h**(-.25),'(H/0.02)^(-1/4)');add(h**.55,'(H/0.02)^0.55')
  else:
   add(b,'1/(1+H/0.02)');add(np.sqrt(h),'sqrt(H/0.02)')
   if kind in ['a3','a4','a5','a6','a7']:add(b*d.hydration.to_numpy()/60,'boundary * hydration/60')
   if kind in ['a4','a5','a6']:add(b*np.sqrt(pressure),'boundary * sqrt((load/1N)/(area/4cm2))')
   if kind in ['a5','a7']:add(np.log1p(d.viscosity.to_numpy())*b,'boundary * log(1+viscosity/(1Pa s))')
   if kind=='a1':add(h,'H/0.02')
   if kind=='a2':add(h/(1+h),'H/(H+0.02)')
 elif case==52:
  x=d.x_D.to_numpy();y=d.y_D.to_numpy();z=d.z_D.to_numpy();st=d.St.to_numpy();wt=(d.turbine.to_numpy()==2).astype(float);k=knobs.get('wake_spread',.1);width=.35+k*x;gauss=np.exp(-.5*((y/width)**2+(z/width)**2));offset=np.full(len(d),7.)
  cols=[];names=[]
  add(-gauss/(1+k*x)**2,'-Gaussian(r/(0.35+k*xD))/(1+k*xD)^2')
  if kind!='domain':add(-gauss*wt/(1+k*x)**2,'wake * indicator(turbine2)')
  if kind in ['a2','a3','a4','a5','a6','a7']:add(-gauss*st/(1+k*x)**2,'wake * Strouhal')
  if kind in ['a3','a4','a5','a6']:add(-gauss*st*wt/(1+k*x)**2,'wake * Strouhal * turbine2')
  if kind in ['a4','a5','a7']:add(z,'vertical ABL shear z/D')
  if kind in ['a5','a6']:add(gauss*(y*y-z*z)/(width**2),'wake anisotropy quadrupole')
 elif case==55:
  t=d.time_s.to_numpy()/100;water=d.water.to_numpy()/.3;r=d.ratio.to_numpy()/.7;age=d.age_min.to_numpy()/30
  if kind=='domain':add(t,'penetration clock/100');add(age*t,'age/30min * clock/100')
  else:
   add(t/np.maximum(water,1e-6),'clock/100 divided by water-ratio/0.30');add(age*t/np.maximum(water,1e-6),'age * clock / water')
   if kind in ['a1','a2','a3','a4','a5','a6','a7']:add(t*t,'(clock/100)^2')
   if kind in ['a2','a3','a4','a5','a6']:add(r*t,'aggregate-ratio/0.7 * clock')
   if kind in ['a3','a4','a5','a7']:add(age*r*t,'aging * aggregate * clock')
   if kind in ['a4','a5','a6']:add(age*t*t,'aging * clock^2')
   if kind=='a5':add(t*water,'water * clock')
 elif case==58:
  # Generalized Maxwell storage spectrum. Each nonnegative beta_j is an effective mode stiffness in Pa.
  T=d.temperature_C.to_numpy();w=d.omega.to_numpy();C1=knobs.get('C1',8.);C2=knobs.get('C2',80.);mode=knobs.get('shift','wlf');dt=T-60
  loga=(-C1*dt/(C2+dt)) if mode=='wlf' else knobs.get('activation',50000.)/8.314*(1/(T+273.15)-1/333.15)/np.log(10)
  freq=w*10**np.clip(loga,-10,10)
  if kind=='domain':cols=[];names=[];add((freq/(1+freq)),'saturating frequency: shifted w/(1+shifted w)')
  else:
   cols=[];names=[]
   taus=np.logspace(-4,4,3 if kind=='a1' else 7)
   if kind in ['a4','a5','a6']:taus=np.logspace(-5,5,9)
   for tau in taus:
    q=np.clip(freq*tau,0,1e100);add(q*q/(1+q*q),f'Maxwell storage tau={tau:g}s')
   if kind in ['a3','a5','a7']:add(ones,'elastic plateau')
 elif case==59:
  G=d.irradiance.to_numpy();T=d.temp_C.to_numpy();wind=d.wind.to_numpy();hour=d.hour.to_numpy();doy=d.doy.to_numpy();cols=[];names=[]
  add(G,'irradiance/(1kW m^-2)')
  if kind not in ['domain','a1']:add(G*(T-25)/25,'irradiance * (ambientC-25)/25K')
  if kind in ['a1','a3','a4','a5','a6','a7']:add(G*G,'irradiance^2: heating/clipping surrogate')
  if kind in ['a3','a4','a5','a6']:add(G/(1+wind),'irradiance/(1+wind/(1m/s))')
  if kind in ['a4','a5','a7']:
   add(G*np.cos(2*np.pi*doy/365.25),'irradiance * seasonal cosine');add(G*np.sin(2*np.pi*doy/365.25),'irradiance * seasonal sine')
  if kind in ['a5','a6']:add(G*(hour-12)/12,'irradiance * afternoon asymmetry')
 elif case==66:
  P=d.pressure_bar.to_numpy();T=d.temperature_K.to_numpy();eg=d.eg_pct.to_numpy()/10;branch=d.branch.to_numpy();cols=[];names=[]
  b=knobs.get('affinity',.1)*np.exp(np.clip(knobs.get('heat',500.)*(1/T-1/160),-20,20));q=b*P/(1+b*P)
  add(q,'Langmuir b(T)P/(1+b(T)P)')
  if kind!='domain':add(-P/100,'negative gas displacement P/(100bar)')
  if kind in ['a2','a3','a4','a5','a6','a7']:add(-q*eg,'solid dilution: -Langmuir * EG/10wt%')
  if kind in ['a3','a4','a5','a6']:add(-P/100*(160/T),'temperature-dependent gas displacement')
  if kind in ['a4','a5','a7']:add(q*branch,'branch contrast at matched pressure')
  if kind in ['a5','a6']:add(np.sqrt(q),'heterogeneous-site square-root occupancy')
 elif case==69:
  t=d.time_s.to_numpy();TH=d.housing_C.to_numpy();TE=d.environment_C.to_numpy();initial=d.initial_C.to_numpy();P=abs(d.speed.to_numpy()*d.friction.to_numpy());tau=knobs.get('tau',600.)
  if kind=='domain':return np.c_[TH],['housing temperature'],offset
  # Causal convolution under piecewise-constant previous-sample forcing; no future TL used.
  hh=np.zeros(len(d));ee=hh.copy();pp=hh.copy();sp=hh.copy();init=hh.copy()
  for group,sub in d.groupby('group',sort=False):
   ix=d.index.get_indexer(sub.index);v=[0.,0.,0.,0.]
   for k,j in enumerate(ix):
    if k:
     prev=ix[k-1];dt=t[j]-t[prev];a=np.exp(-dt/tau);v=[a*u+(1-a)*f for u,f in zip(v,[TH[prev],TE[prev],P[prev],abs(d.speed.iloc[prev])])]
    hh[j],ee[j],pp[j],sp[j]=v;init[j]=initial[j]*np.exp(-t[j]/tau)
  offset=init+ee;cols=[];names=[]
  add(hh-ee,'causal housing-minus-environment convolution; complementary weights sum to one')
  if kind in ['a2','a3','a4','a5','a6','a7']:add(pp,'causal friction-power convolution')
  if kind in ['a3','a5','a7']:add(sp,'causal absolute-speed convection surrogate')
  if kind in ['a4','a5','a6']:add(TH-TE,'instantaneous housing-environment contrast')
 elif case==78:
  t=d.time_h.to_numpy();initial=d.initial_logCFU.to_numpy();offset=initial.copy();cols=[];names=[]
  add(t/24,'elapsed time/(24h)')
  if kind!='domain':add((t/24)*(7-initial),'capacity-gap growth: time * (7-initial burden)')
  if kind in ['a2','a3','a4','a5','a6','a7']:add(t*t/576,'curvature time^2/(24h)^2')
  if kind in ['a3','a4','a5','a6']:add((t/24)*np.clip(8-initial,0,None),'positive capacity-gap at 8 logCFU')
  if kind in ['a4','a5','a7']:
   for site in ['GSK','PEI','SSI']:add((d.site.to_numpy()==site)*t/24,'site-specific time slope '+site)
  if kind in ['a5','a6']:add((t/24)*(initial-6)**2,'initial-burden nonlinear growth interaction')
 elif case==86:
  c=d.current.to_numpy();s=d.slope6.to_numpy();t=d.time_h.to_numpy();offset=c.copy();cols=[];names=[]
  if kind=='domain':add(6*s,'6h * past6h slope')
  else:
   add(ones,'constant 6h increment');add(6*s,'6h * past6h slope')
   if kind in ['a1','a2','a3','a4','a5','a6','a7']:add(c/10000,'current potency/10000 source-unit')
   if kind in ['a2','a3','a4','a5','a6']:add((c/10000)**2,'current potency^2/10000^2 saturation')
   if kind in ['a3','a4','a5','a7']:add(6*s*np.exp(-t/100),'history slope * age decay exp(-hours/100)')
   if kind in ['a4','a5','a6']:add(np.maximum(6*s,0),'positive-slope asymmetric growth')
   if kind=='a5':add((t/100)*c/10000,'clock-dependent inhibition surrogate')
 elif case==96:
  v=d.speed.to_numpy();a=d.past_acc.to_numpy();gap=d.gap.to_numpy();rel=d.relative_speed.to_numpy();lat=d.lateral_gap.to_numpy();offset=v.copy();cols=[];names=[]
  if kind=='domain':add(a,'past acceleration * 1s')
  else:
   add(ones,'free increment');add(a,'inertial acceleration * 1s')
   if kind in ['a1','a2','a3','a4','a5','a6','a7']:add(rel,'leader relative speed * relaxation')
   if kind in ['a2','a3','a4','a5','a6']:add(np.tanh(gap/5)-v/5,'optimal-velocity gap response')
   if kind in ['a3','a4','a5','a7']:add(rel*np.exp(-lat/.64),'lateral-decaying speed interaction')
   if kind in ['a4','a5','a6']:add(np.minimum(gap-1.8,0),'overlap/short-gap response')
   if kind=='a5':add(v*v/np.maximum(d.radius.to_numpy(),1),'centripetal speed^2/r surrogate')
 else:raise ValueError('Unknown case')
 return np.column_stack(cols),names,offset

def predict(model,d):
 if model['kind']=='rbf':
  x=d[model['features']].copy();x=pd.get_dummies(x,dtype=float).reindex(columns=model['columns'],fill_value=0).to_numpy(float);x=(x-np.array(model['center']))/np.array(model['scale']);centers=np.array(model['centers']);K=np.exp(-np.maximum(np.sum(x*x,1)[:,None]+np.sum(centers*centers,1)[None,:]-2*x@centers.T,0)/(2*model['width']**2));z=K@np.array(model['beta'])+model['intercept'];return np.exp(np.clip(z,-30,40)) if model.get('log') else z
 X,_,offset=basis(model['case'],model['kind'],d,model.get('knobs'));z=X[:,model.get('active_columns',list(range(X.shape[1])))]@np.array(model['beta'])+offset
 if model['case']==59:z=np.minimum(np.maximum(z,0),d.limit.to_numpy())
 if model['case'] in [23,55,58,86,96]:z=np.maximum(z,1e-12)
 return z

def verify(root):
 m=json.loads((root/'MANIFEST.json').read_text())
 for f in m['files']:
  p=root/f['path']
  if not p.is_file() or p.stat().st_size!=f['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:raise ValueError('Package checksum mismatch: '+f['path'])
def main():
 p=argparse.ArgumentParser();p.add_argument('--input','--inputs',dest='input',type=Path);p.add_argument('--output',type=Path);p.add_argument('--model',default='reference');a=p.parse_args();root=Path(__file__).parent
 verify(root);spec=json.loads((root/'rules.json').read_text());x=read_table(a.input or root/'data/inputs.csv.gz');d=x[['sample_id','group']].copy()
 for k,m in spec['models'].items():
  if not a.input or k==a.model:d[k]=predict(m,x)
 if a.input:
  if a.output is None or a.output.exists():raise ValueError('Choose a new output path')
  d.rename(columns={a.model:'prediction'}).to_csv(a.output,index=False)
 else:
  saved=read_table(root/'evidence/predictions.csv.gz')
  if not d[['sample_id','group']].equals(saved[['sample_id','group']]):raise ValueError('Identity mismatch')
  error=max(float(np.max(abs(d[k]-saved[k]))) for k in spec['models']);assert all(np.allclose(d[k],saved[k],rtol=1e-9,atol=1e-8) for k in spec['models']);print(json.dumps({'status':'pass','models':len(spec['models']),'rows':len(d),'max_prediction_difference':error}))
if __name__=='__main__':main()
