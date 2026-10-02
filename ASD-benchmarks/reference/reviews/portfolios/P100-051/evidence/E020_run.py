from pathlib import Path
import json,hashlib,argparse
import numpy as np
import pandas as pd

def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})

def features(kind,d):
    I=d.current_uA.to_numpy(float); I0=d.cal_current_uA.to_numpy(float);t=d.time_s.to_numpy(float)/1000.;q=d.charge_uC.to_numpy(float)/1000.;p=d.polymer_fraction.to_numpy(float);v=d.voltage_V.to_numpy(float)/40.;c=d.cal_photo_nA.to_numpy(float)
    delta=(I-I0)/100.;logt=np.log1p(t);logI=np.arcsinh(I/100.)-np.arcsinh(I0/100.)
    terms={'current':[np.ones(len(d)),delta], 'charge':[np.ones(len(d)),delta,q], 'age':[np.ones(len(d)),delta,logt], 'polymer':[np.ones(len(d)),delta,delta*p,logt,logt*p], 'saturation':[np.ones(len(d)),logI,logt,logI*p], 'calyield':[np.ones(len(d)),c*delta,c*logt,delta,logt], 'quench':[np.ones(len(d)),delta,logt,delta*logt,p*delta], 'voltage':[np.ones(len(d)),delta,logt,delta*v,v-1], 'flexible':[np.ones(len(d)),delta,logI,t,logt,q,p,v,c,delta*p,delta*v,delta*logt,p*logt,delta*delta,logt*logt,c*delta,c*logt]}
    return np.column_stack(terms[kind])

def predict(model,dataframe):
    d=dataframe;kind=model['kind'];case=model['case']
    if case==21:
        w=d.width_um.to_numpy(float);b=d.wafer_b.to_numpy(float);o=d.outer.to_numpy(float);a=np.asarray(model.get('theta',[]),float)
        if kind=='constant':return np.full(len(d),a[0])
        if kind=='area':return np.exp(a[0])/w**2
        if kind=='edge':return np.exp(a[0])/(w-a[1])**2
        if kind=='perimeter':return 1/(np.exp(a[0])*w*w+np.exp(a[1])*w)
        if kind=='wafer_edge':return np.exp(a[0]+a[1]*b)/(w-a[2]-a[3]*b)**2
        if kind=='region':return np.exp(a[0]+a[1]*b+a[2]*o)/(w-a[3])**2
        if kind=='wafer_area':return np.exp(a[0]+a[1]*b)/w**2
        if kind=='series':return np.exp(a[0]+a[1]*b)/(w-a[2])**2+np.exp(a[3])
        if kind=='flexible':return np.maximum(0,np.column_stack([np.ones(len(d)),1/w,1/w**2,b,b/w,b/w**2,o/w**2])@a)
    elif case==51:
        v=d.gate_V.to_numpy(float);lo=d.cal_minus20_uA.to_numpy(float);mid=d.cal_zero_uA.to_numpy(float);hi=d.cal_plus20_uA.to_numpy(float);pos=v>=0;u=np.where(pos,v/20.,(v+20)/20.);a=np.asarray(model.get('theta',[]),float)
        if kind=='linear':return np.where(pos,mid+(hi-mid)*u,lo+(mid-lo)*u)
        if kind=='loglinear':return np.exp(np.where(pos,np.log(np.maximum(mid,1e-9))*(1-u)+np.log(np.maximum(hi,1e-9))*u,np.log(np.maximum(lo,1e-9))*(1-u)+np.log(np.maximum(mid,1e-9))*u))
        if kind=='shape':
            shape=np.interp(v,np.asarray(model['grid']),np.asarray(model['shape']));return np.where(pos,mid+(hi-mid)*shape,lo+(mid-lo)*shape)
        if kind=='power':return np.where(pos,mid+(hi-mid)*u**a[0],lo+(mid-lo)*u**a[0])
        if kind=='two_power':return np.where(pos,mid+(hi-mid)*u**a[0],lo+(mid-lo)*u**a[1])
        if kind=='softplus':
            z=lambda x:a[1]*np.logaddexp(0,(x-a[0])/a[1]);s=(z(v)-z(-20))/(z(20)-z(-20));return lo+(hi-lo)*s
        if kind=='contact':
            z=lambda x:a[1]*np.logaddexp(0,(x-a[0])/a[1]);f=lambda x:z(x)/(1+a[2]*z(x));return lo+(hi-lo)*(f(v)-f(-20))/(f(20)-f(-20))
        if kind=='anchor_power':
            r=np.clip((mid-lo)/np.maximum(hi-lo,1e-12),1e-9,1.);p=np.clip(a[0]+a[1]*np.log(r),.1,8);return np.where(pos,mid+(hi-mid)*u**p,lo+(mid-lo)*u**a[2])
        if kind=='anchored_bend':
            s=np.where(pos,u+a[0]*u*(1-u)+a[1]*u*(1-u)*(2*u-1),u**a[2]);return np.where(pos,mid+(hi-mid)*s,lo+(mid-lo)*s)
        if kind=='shape_blend':
            shape=np.interp(v,np.asarray(model['grid']),np.asarray(model['shape']));s=a[0]*shape+(1-a[0])*u;return np.where(pos,mid+(hi-mid)*s,lo+(mid-lo)*s)
    elif case==64:
        if kind=='persistence':return d.cal_photo_nA.to_numpy(float)
        x=features(kind,d);return d.cal_photo_nA.to_numpy(float)+x@np.asarray(model['theta'])
    raise ValueError('Unknown frozen model kind')

def main():
    root=Path(__file__).resolve().parent
    for item in json.loads((root/'MANIFEST.json').read_text())['files']:
        p=root/item['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Corrupt or missing package asset: '+str(p))
    rules=json.loads((root/'rules.json').read_text());d=read_table(root/'data/inputs.csv.gz');q=read_table(root/'evidence/predictions.csv.gz')
    for name,m in rules['models'].items():
        p=predict(m,d)
        if not np.isfinite(p).all() or not np.allclose(p,q[name],rtol=1e-10,atol=1e-10):raise ValueError('Prediction mismatch: '+name)
    print(json.dumps({'case':rules['case_id'],'rows':len(d),'models':len(rules['models']),'replay':'passed'}))
if __name__=='__main__':main()
