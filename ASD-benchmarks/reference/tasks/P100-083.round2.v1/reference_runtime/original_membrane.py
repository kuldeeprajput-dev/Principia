"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist
R=8.314462618

def pstate(model,frame):
    m=frame.membrane_index.to_numpy(dtype=int);t=frame.temperature_K.to_numpy(float)
    p=model['calibration'];lr=np.array([z['log_P_ref'] for z in p])[m];b=np.array([z['activation_over_R_K'] for z in p])[m];n=np.array([z['pressure_exponent'] for z in p])[m]
    return np.exp(lr+b*(1/673.15-1/t)),n

def gasidx(f):return np.array([{'N2':0,'Ar':1,'He':2}[g] for g in f.gas])

def baseflux(model,f):
    p,n=pstate(model,f);ph=f.feed_fraction.to_numpy()*f.retentate_bar.to_numpy();pp=f.permeate_bar.to_numpy()
    return p*np.maximum(ph**n-pp**n,0)

def rfeatures(f):
    m=f.membrane_index.to_numpy(int);g=gasidx(f)
    return np.column_stack([(f.temperature_K.to_numpy()-673.15)/50,f.feed_fraction.to_numpy(),np.log(f.normal_flow_L_min.to_numpy()/5),np.eye(4)[m],np.eye(3)[g]])

def predict(model,f):
    kind=model['kind'];m=f.membrane_index.to_numpy(int)
    if kind=='mean':return np.array(model['means'])[m]
    j0=baseflux(model,f)
    if kind in ['richardson','sieverts']:return j0
    if kind=='rbf':
        x=(rfeatures(f)-np.array(model['center']))/np.array(model['scale']);train=np.array(model['train_features']);sq=np.maximum((x*x).sum(1)[:,None]+(train*train).sum(1)[None,:]-2*x@train.T,0)
        z=np.exp(-sq/(2*model['bandwidth']**2))@np.array(model['weights'])
        return j0*np.exp(np.clip(z,-3,3))
    v=np.array(model['parameters']);g=gasidx(f);flow=f.normal_flow_L_min.to_numpy();temp=f.temperature_K.to_numpy()
    if kind=='suppression':
        kk=np.exp(v[:4])[m];gas=np.exp(np.r_[0,v[4:6]])[g]
        return j0/(1+kk*gas*(1-f.feed_fraction.to_numpy())*(5/flow)**.6)
    # implicit nonnegative transport; bounded by feedhydrogen, partialpressure and membrane laws
    p,n=pstate(model,f);pr=f.retentate_bar.to_numpy();pp=f.permeate_bar.to_numpy();x=f.feed_fraction.to_numpy();area=f.area_m2.to_numpy()
    vm=model.get('normal_molar_volume_L',22.414);fin=flow/(60*vm)
    rho=0. if kind=='film' else (model.get('depletion_fraction',.5) if kind!='depletion' else float(v[0]))
    if kind=='depletion':k=np.full(len(f),np.inf)
    elif kind=='shared':
        kval=np.exp(v[0])*(.014/f.diameter_m.to_numpy());gas=np.exp(np.r_[0,v[1:3]])[g];k=kval*gas*(flow/5)**.6*(temp/673.15)**1.75
    else:
        kval=np.exp(v[:4])[m];gas=np.exp(np.r_[0,v[4:6]])[g]
        power=.6 if kind in ['film','coupled'] else float(v[6])
        exponent=1.75 if kind!='thermal' else float(v[7])
        k=kval*gas*(flow/5)**power*(temp/673.15)**exponent
    lo=np.zeros(len(f));hi=np.minimum(j0,fin*x/area*.999999)
    for _ in range(60):
        j=(lo+hi)/2;z=j*area/fin;bulk=(x-rho*z)/(1-rho*z)
        surface=pr*bulk-j/k
        pred=p*np.maximum(np.maximum(surface,pp)**n-pp**n,0)
        positive=pred>j;lo=np.where(positive,j,lo);hi=np.where(positive,hi,j)
    return (lo+hi)/2
