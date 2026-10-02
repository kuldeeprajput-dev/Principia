"""Frozen prediction-only functions extracted from archived scientific implementations.
No fitting, data acquisition or research-history imports are included.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.spatial.distance import cdist

def _vector(d, key):
    return d[key].to_numpy(float)

def _rumen(m, d):
    t=_vector(d,'hour');g8=_vector(d,'g8');g4=_vector(d,'g4');y=np.zeros(len(d))
    if m['kind']=='persistence': return g8
    if m['kind']=='linear_prefix': return g8+np.maximum(0,g8-g4)*(t-8)/4
    if m['kind']=='empirical_ratio':
        return np.array([row.g8*m['ratios'].get(f'{row.trial}|{row.algae}|{row.hour:g}',m['fallback'][f'{row.trial}|{row.hour:g}']) for row in d.itertuples()])
    for trial, p in m['trial_parameters'].items():
        ix=d.trial.astype(str).to_numpy()==trial
        tt=t[ix];a=g8[ix];b=g4[ix];ratio=b/a
        kind=m['kind']
        if kind in ['first_order','stretched','curvature','treatment_shape','lag_shape']:
            tau=np.full(len(tt),p['tau_h']);beta=p.get('beta',1.)
            if 'gamma_curvature' in p:tau=tau*np.exp(p['gamma_curvature']*(ratio-.5))
            if 'algae_log_tau' in p:tau=tau*np.exp([p['algae_log_tau'].get(x,0.) for x in d.loc[ix,'algae']])
            lag=p.get('lag_h',0.)
            f=-np.expm1(-np.power(np.maximum(0,tt-lag)/tau,beta));f8=-np.expm1(-np.power((8-lag)/tau,beta));z=a*f/f8
        elif kind=='dual_pool':
            w=p['fast_fraction'];tf=p['tau_fast_h'];ts=p['tau_slow_h']
            f=w*(-np.expm1(-tt/tf))+(1-w)*(-np.expm1(-tt/ts));f8=w*(-np.expm1(-8/tf))+(1-w)*(-np.expm1(-8/ts));z=a*f/f8
        elif kind in ['tangent_decay','tangent_curvature']:
            tau=p['tau_h']*np.exp(p.get('gamma_curvature',0.)*(ratio-.5))
            z=a+p['rate_multiplier']*np.maximum(0,a-b)*(tau/4)*(-np.expm1(-(tt-8)/tau))
        else:raise ValueError(kind)
        y[ix]=z
    return y

def soil_shape(m, d):
    x=(_vector(d,'t05')-10)/10
    M=_vector(d,'tsmoisture');missing=~np.isfinite(M);M=np.where(missing,30,M);z=(M-30)/30
    p=m.get('parameters',{})
    kind=m['kind'];eta=p.get('b',0)*x+p.get('missing',0)*missing
    if kind=='lloyd_taylor':
        eta=p['E0_K']*(1/(10+46.02)-1/(_vector(d,'t05')+46.02))
    if kind in ['moisture_optimum','temperature_moisture','site_heterogeneity','seasonal','trench_sensitivity','wet_asymmetry']:
        eta+=p.get('c',0)*z+p.get('d',0)*z*z+p.get('interaction',0)*x*z
    if kind=='dry_saturation':
        K=p['K_percent'];eta+=np.log(np.maximum(1e-9,M/(K+M)/(30/(K+30))))*(~missing)
    if kind in ['site_heterogeneity','seasonal','trench_sensitivity','wet_asymmetry']:
        eta+=np.array([p['site_b_deviation'].get(s,0.) for s in d.site])*x
    if kind in ['seasonal','trench_sensitivity','wet_asymmetry']:
        phase=2*np.pi*(_vector(d,'doy')-1)/365.25
        eta+=p.get('season_sin',0)*np.sin(phase)+p.get('season_cos',0)*np.cos(phase)
    if kind in ['trench_sensitivity','wet_asymmetry']:
        trenched=d.context.str.endswith('|True').to_numpy(float)
        eta+=p.get('trench_b',0)*x*trenched
    if kind=='wet_asymmetry':eta+=p.get('wet_cube',0)*np.maximum(z,0)**3
    return np.exp(np.clip(eta,-15,15))

def flexible_features(m,d):
    keys=m['numeric_features'];x=np.column_stack([_vector(d,k) for k in keys]);bad=~np.isfinite(x)
    x=np.where(bad,np.asarray(m['medians']),x)
    z=(x-np.asarray(m['means']))/np.asarray(m['scales'])
    columns=[z,bad.astype(float)]
    for key,values in m['categories'].items():columns.append((d[key].astype(str).to_numpy()[:,None]==np.asarray(values)[None,:]).astype(float))
    return np.column_stack(columns)

def predict(m,d):
    if m['kind']=='rbf_ridge':
        z=flexible_features(m,d);c=np.asarray(m['centers']);dist=np.maximum(0,(z*z).sum(1)[:,None]+(c*c).sum(1)[None,:]-2*z@c.T)
        return np.maximum(0,m['intercept']+np.exp(-m['gamma']*dist)@np.asarray(m['coefficients']))
    if m['case']=='rumen':return _rumen(m,d)
    f=soil_shape(m,d)
    a=np.array([m['context_amplitudes'].get(c,m['site_fallback'].get(s,m['global_fallback'])) for c,s in zip(d.context,d.site)])
    return a*f
