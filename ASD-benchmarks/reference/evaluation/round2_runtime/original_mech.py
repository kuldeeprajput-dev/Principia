"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist

def fatigue_design(spec,d):
    n=np.maximum(d.cycle.to_numpy()-20,0);e=d.strain_percent.to_numpy();l=np.log1p(n/1000);t=n/1e5
    kind=spec['kind']
    if kind=='log':return (l*e**2)[:,None]
    if kind=='power':return (t**.25*e**4)[:,None]
    if kind=='saturation':return ((1-np.exp(-t))*e**2)[:,None]
    if kind=='two_mechanism':return np.column_stack([l*e**2,t*e**6])
    if kind=='cure_strain':return np.column_stack([l*e**2]+[l*e**6*(d.cure.to_numpy()==c) for c in ['EQA01','EQA02','EQA03']])
    if kind=='frequency':return np.column_stack([l*e**2,l*e**2*np.sqrt(d.frequency_Hz.to_numpy()/5)])
    if kind=='delayed':return np.column_stack([l*e**2,np.maximum(t-.1,0)*e**6])
    if kind=='sqrtdose':return np.column_stack([l*e**2,np.sqrt(t)*e**4])
    raise ValueError(kind)

def homogeneous(d):
    x=d.quality.to_numpy();rl=d.rho_liquid.to_numpy();rv=d.rho_vapor.to_numpy()
    return (x/rv)/(x/rv+(1-x)/rl)

def boiling_design(spec,d):
    a=homogeneous(d);eta=np.log(a/(1-a));r=d.radial_fraction.to_numpy();g=np.log(d.massflux_kg_m2_s.to_numpy()/700);p=np.log(d.pressure_Pa.to_numpy()/7e6)
    k=spec['kind'];one=np.ones(len(d));b=r*r
    if k=='slip':return one[:,None],eta
    if k=='radial':return np.column_stack([one,b]),eta
    if k=='fluxslip':return np.column_stack([one,g]),eta
    if k=='qualityradial':return np.column_stack([one,b,b*eta]),eta
    if k=='combined':return np.column_stack([one,b,b*eta,g]),eta
    if k=='quartic':return np.column_stack([one,b,b*eta,g,r**4]),eta
    if k=='pressure':return np.column_stack([one,b,b*eta,g,p]),eta
    raise ValueError(k)

def flexible_x(case,d):
    if case.startswith('24'):
        return np.column_stack([np.log1p(d.cycle.to_numpy()/1000),d.strain_percent,d.frequency_Hz]+[(d.cure.to_numpy()==c).astype(float) for c in ['EQA01','EQA02','EQA03']])
    return np.column_stack([np.log(d.quality/(1-d.quality)),np.log(d.massflux_kg_m2_s/700),d.radial_fraction,np.log(d.pressure_Pa/7e6)])

def predict(model,d):
    case=model['case'];kind=model['spec']['kind']
    if kind=='persistence':return d.E0_GPa.to_numpy()
    if kind=='mean':return np.repeat(model['value'],len(d))
    if kind=='homogeneous':return homogeneous(d)
    if kind=='flex':
        xx=(flexible_x(case,d)-np.array(model['mean']))/np.array(model['scale']);c=np.array(model['centers']);k=np.exp(-np.sum((xx[:,None,:]-c[None,:,:])**2,axis=2)/(2*model['bandwidth']**2));z=np.column_stack([np.ones(len(d)),k])@np.array(model['coefficients'])
        return d.E0_GPa.to_numpy()*np.clip(z,0,1) if case.startswith('24') else np.clip(z,0,1)
    if case.startswith('24'):
        return d.E0_GPa.to_numpy()*np.exp(-np.clip(fatigue_design(model['spec'],d)@np.array(model['coefficients']),0,100))
    if kind=='drift':
        jg=d.massflux_kg_m2_s.to_numpy()*d.quality.to_numpy()/d.rho_vapor.to_numpy();jl=d.massflux_kg_m2_s.to_numpy()*(1-d.quality.to_numpy())/d.rho_liquid.to_numpy();C,V=model['coefficients']
        return np.clip(jg/(C*(jg+jl)+V),0,1)
    xx,eta=boiling_design(model['spec'],d);z=np.clip(eta+xx@np.array(model['coefficients']),-30,30)
    return 1/(1+np.exp(-z))
