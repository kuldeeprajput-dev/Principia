"""Frozen predictors: input-only, no fitting or observation access."""
from pathlib import Path
import json,argparse,hashlib
import numpy as np,pandas as pd

def read_table(path):return pd.read_csv(path,float_precision='round_trip',dtype={'sample_id':str,'group':str,'plant':str})
def thermal(d,tau,k=0):
 out=np.zeros((len(d),6));t=d.time_s.to_numpy();forcing=np.c_[d.housing_C,d.environment_C,abs(d.speed*d.friction),abs(d.speed),np.ones(len(d)),abs(d.speed*d.friction)*(d.housing_C-25)/25]
 for _,s in d.groupby('group',sort=False):
  ix=d.index.get_indexer(s.index);v=np.zeros(6)
  for j,a in enumerate(ix):
   if j:
    b=ix[j-1];r=np.exp(-(t[a]-t[b])*(1+k*abs(d.speed.iloc[b]))/tau);v=r*v+(1-r)*forcing[b]
   out[a]=v
 return out

def design(case,kind,d,q):
 if case==69:
  tau=q.get('tau',200);f=thermal(d,tau,q.get('k',0));v=thermal(d,q.get('slow',1600));t=d.time_s.to_numpy();decay=np.zeros(len(d))
  for _,s in d.groupby('group',sort=False):
   ix=d.index.get_indexer(s.index);decay[ix[0]]=1
   for j in range(1,len(ix)):
    a,b=ix[j],ix[j-1];decay[a]=decay[b]*np.exp(-(t[a]-t[b])*(1+q.get('k',0)*abs(d.speed.iloc[b]))/tau)
  base=f[:,0]+d.initial_C.to_numpy()*decay
  if kind=='housing':return np.empty((len(d),0)),d.housing_C.to_numpy(),[],[]
  if kind=='single_speed' or kind=='variable_tau':return f[:,[3]],base,['filtered |omega|'],[(0,np.inf)]
  if kind=='single_power':return f[:,[2]],base,['filtered |omega torque|'],[(0,np.inf)]
  if kind=='double_speed':
   slowbase=v[:,0]+d.initial_C.to_numpy()*np.exp(-t/q['slow']);return np.c_[f[:,3],v[:,3],slowbase-base],base,['fast speed heat','slow speed heat','slow conservative fraction'],[(0,np.inf),(0,np.inf),(0,1)]
  if kind in ['innovation_power','innovation_speed']:
   initH=np.zeros(len(d))
   for _,s in d.groupby('group',sort=False):
    ix=d.index.get_indexer(s.index);initH[ix]=d.housing_C.iloc[ix[0]]*decay[ix]
   innovation=d.housing_C.to_numpy()-f[:,0]-initH
   col=2 if kind=='innovation_power' else 3
   return np.c_[f[:,col],innovation],base,['causal heat forcing','current housing innovation'],[(0,np.inf),(0,4)]
  if kind=='temperature_power':return np.c_[f[:,2],f[:,5]],base,['power heat gain','temperature-power interaction'],[(0,np.inf),(-np.inf,np.inf)]
  if kind=='ridge_history':
   fs=[thermal(d,t) for t in [50,100,200,400,800,1600,3200]]
   X=np.column_stack([a[:,j] for a in fs for j in [0,1,2,3]]+[d.housing_C.to_numpy(),d.environment_C.to_numpy()]);return X,base,['causal history '+str(i) for i in range(X.shape[1])],[]
 if case==52:
  x=d.x_D.to_numpy();y=d.y_D.to_numpy();z=d.z_D.to_numpy();wt=(d.turbine.to_numpy()==2).astype(float);st=d.St.to_numpy();act=(st>0).astype(float);bg=d.background_u.to_numpy();k=q.get('spread',.06);ell=q.get('ell',1)
  sy=.35+k*x*(1+q.get('actwidth',0)*act);sz=sy*ell;g=np.exp(-.5*((y/sy)**2+(z/sz)**2));wake=g/(1+k*x)**2
  X=[-wake,-wake*wt];names=['negative Gaussian deficit','second-turbine deficit contrast']
  if kind in ['act_amplitude','act_width','act_quadratic','anisotropic_act']:X.extend([-wake*act,-wake*act*wt]);names+=['active control deficit','active second-turbine contrast']
  if kind=='act_quadratic':X.extend([-wake*act*(st-.35),-wake*act*(st-.35)*wt]);names+=['frequency gradient','frequency gradient second turbine']
  if kind=='anisotropic_act':X.extend([g*(y*y/sy**2-z*z/sz**2),g*z/sz]);names+=['quadrupole','wake vertical displacement linearization']
  if kind=='supergaussian':
   g=np.exp(-.5*((abs(y)/sy)**4+(abs(z)/sz)**4));X=[-g/(1+k*x)**2,-g*wt/(1+k*x)**2];names=['quartic profile','second-turbine contrast']
  if kind=='ridge_spatial':
   X=[];names=[]
   for i in range(4):
    for j in range(4-i):
     for l in range(4-i-j):
      for a in [np.ones(len(d)),wt,act]:X.append((x/5)**i*y**j*z**l*a);names.append(f'spatial monomial {i}{j}{l}')
  return np.column_stack(X),bg,names,[]
 if case==59:
  G=d.irradiance.to_numpy();Gp=d.Gpast1.to_numpy();T=d.temp_C.to_numpy();W=d.wind.to_numpy();h=(d.hour.to_numpy()-12)/12;s=2*np.pi*d.doy.to_numpy()/365.25
  gamma=q.get('gamma',0);mix=q.get('mix',0);G=(1-mix)*G+mix*Gp;Tc=T+G*1000/(25+6.84*W);eff=np.maximum(.2,1+gamma*(Tc-25));X=[G*eff];names=['G weighted by nonpositive cell-temperature coefficient']
  if kind in ['geometry','lag_geometry','signed_thermal','unrestricted_thermal','ridge_calendar']:
   # Calendar terms are gain modulation, not identified tilt/azimuth or solar-clock calibration.
   for v,n in [(np.cos(s),'season cos'),(np.sin(s),'season sin'),(h,'source-clock asymmetry'),(h*h,'hour curvature'),(h*np.cos(s),'season/hour interaction')]:X.append(G*eff*v);names.append(n)
  if kind=='unrestricted_thermal':X.extend([G*(T-25)/25,G*G/(1+W)]);names+=['ambient interaction','heating surrogate']
  if kind=='lag_response':X.extend([Gp,d.Gpast2.to_numpy()]);names+=['previous-hour radiation','two-hour-past radiation']
  if kind=='ridge_calendar':
   for a in range(1,4):
    for b in range(1,4):X.append(G*np.cos(a*s)*h**b);names.append(f'calendar cross {a} {b}')
   X.extend([G**2,G*(T-25)/25,G/(1+W)]);names+=['radiation square','ambient','wind']
  return np.column_stack(X),np.zeros(len(d)),names,[]
 raise ValueError('Unknown model')

def validate_inputs(model,d):
 if 'sample_id' not in d or 'group' not in d or not d.sample_id.is_unique or d.sample_id.isna().any() or d.group.isna().any():raise ValueError('Unique sample_id and nonmissing group required')
 needed={69:['time_s','housing_C','environment_C','speed','friction','initial_C'],52:['turbine','x_D','y_D','z_D','St','background_u'],59:['irradiance','temp_C','wind','hour','doy','limit','latitude','Gpast1','Gpast2']}[model['case']]
 if not set(needed).issubset(d):raise ValueError('Missing required prediction inputs')
 try:values=d[needed].to_numpy(float)
 except (ValueError,TypeError):raise ValueError('Malformed numeric input') from None
 if not np.isfinite(values).all():raise ValueError('Nonfinite prediction input')
 if model['case']==69:
  for _,q in d.groupby('group',sort=False):
   if q.time_s.iloc[0]!=0 or (np.diff(q.time_s)<=0).any():raise ValueError('Each thermal group must begin at calibration t=0 and be strictly chronological')
   if q.initial_C.nunique()!=1:raise ValueError('Initial thermal calibration must be constant within run')
def predict(model,d):
 if model['kind']=='legacy':return legacy_predict(model['state'],d)
 validate_inputs(model,d)
 X,o,_,_=design(model['case'],model['kind'],d,model.get('knobs',{}));z=o+X@np.array(model['beta'])
 if model['case']==59:z=np.clip(z,0,d.limit.to_numpy())
 return z

def legacy_basis(case,kind,d,knobs=None):
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

def legacy_predict(model,d):
 if model['kind']=='rbf':
  x=d[model['features']].copy();x=pd.get_dummies(x,dtype=float).reindex(columns=model['columns'],fill_value=0).to_numpy(float);x=(x-np.array(model['center']))/np.array(model['scale']);centers=np.array(model['centers']);K=np.exp(-np.maximum(np.sum(x*x,1)[:,None]+np.sum(centers*centers,1)[None,:]-2*x@centers.T,0)/(2*model['width']**2));z=K@np.array(model['beta'])+model['intercept'];return np.exp(np.clip(z,-30,40)) if model.get('log') else z
 X,_,offset=legacy_basis(model['case'],model['kind'],d,model.get('knobs'));z=X[:,model.get('active_columns',list(range(X.shape[1])))]@np.array(model['beta'])+offset
 if model['case']==59:z=np.minimum(np.maximum(z,0),d.limit.to_numpy())
 if model['case'] in [23,55,58,86,96]:z=np.maximum(z,1e-12)
 return z


def verify(root):
 for f in json.load(open(root/'MANIFEST.json'))['files']:
  p=root/f['path']
  if not p.is_file() or p.stat().st_size!=f['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:raise ValueError('Package checksum mismatch:'+f['path'])
def main():
 p=argparse.ArgumentParser();p.add_argument('--input','--inputs',dest='input',type=Path);p.add_argument('--output',type=Path);p.add_argument('--model',default='reference');a=p.parse_args();r=Path(__file__).parent;verify(r);rules=json.load(open(r/'rules.json'));x=read_table(a.input or r/'data/inputs.csv.gz')
 if a.input:
  if not a.output or a.output.exists():raise ValueError('New output path required')
  out=x[['sample_id']].copy();out['prediction']=predict(rules['models'][a.model],x);out.to_csv(a.output,index=False)
 else:
  saved=read_table(r/'evidence/predictions.csv.gz');assert x[['sample_id','group']].equals(saved[['sample_id','group']]);err=0
  for k,m in rules['models'].items():
   z=predict(m,x);err=max(err,float(np.max(abs(z-saved[k]))));assert np.allclose(z,saved[k],atol=1e-8,rtol=1e-9)
  print(json.dumps({'status':'pass','rows':len(x),'models':len(rules['models']),'max_difference':err}))
if __name__=='__main__':main()
