from pathlib import Path
import json,hashlib,math,itertools,gzip,zipfile,io
from fractions import Fraction
import numpy as np,pandas as pd
C=Path(__file__).resolve().parent
SEED='principia100-asd7-20261002'
def hh(s):return int(hashlib.sha256((SEED+str(s)).encode()).hexdigest(),16)
def source(data_root):
 m=json.loads((C/'SOURCE_MANIFEST.json').read_text());base=Path(data_root)
 for a in m['assets']:
  p=base/a['path']
  if not p.is_file() or p.stat().st_size!=a['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing, truncated or checksum-mismatched native asset: '+a['path'])
 return base/m['data_root_relative']
def finish(rows):
 d=pd.DataFrame(rows)
 if d.empty:raise ValueError('No eligible observations')
 if d.sample_id.duplicated().any():raise ValueError('Duplicate native identity')
 if not np.isfinite(d.target.to_numpy(float)).all():raise ValueError('Nonfinite target')
 return d.sort_values('sample_id').reset_index(drop=True)

INPUTS=['temperature_lag','density_ratio','field_ratio','density_lag','field_lag','anisotropy_lag','elapsed_lag_s']
def prepare(data_root):
 import cdflib
 s=source(data_root);ef=next((s/'raw').rglob('*des-moms*.cdf'));bf=next((s/'raw').rglob('*fgm*.cdf'));e=cdflib.CDF(ef);b=cdflib.CDF(bf)
 et=e.varget('Epoch');bt=b.varget('Epoch');ep=(et-et[0])*1e-9;idx=np.searchsorted(bt,et,side='right')-1
 den=e.varget('mms1_des_numberdensity_fast');tp=e.varget('mms1_des_tempperp_fast');ta=e.varget('mms1_des_temppara_fast');flags=e.varget('mms1_des_errorflags_fast');bv=b.varget('mms1_fgm_b_gse_srvy_l2')[:,3];bfla=b.varget('mms1_fgm_flag_srvy_l2');valid=(idx>=0)&(flags==0);idx=np.maximum(idx,0);valid&=(bfla[idx]==0)&((et-bt[idx])*1e-9<1)&(den>0)&(tp>0)&(ta>0)&(bv[idx]>0);rows=[]
 for k in range(len(et)):
  old=np.searchsorted(et,et[k]-60_000_000_000,side='right')-1
  if old<0 or not valid[k]or not valid[old]:continue
  block=int(ep[k]//1200)
  rows.append(dict(sample_id='MMS1:des:'+str(k),group='block'+str(block),block=block,target=float(tp[k]),partition='confirmation'if block>=4 else'development',temperature_lag=float(tp[old]),density_ratio=float(den[k]/den[old]),field_ratio=float(bv[idx[k]]/bv[idx[old]]),density_lag=float(den[old]),field_lag=float(bv[idx[old]]),anisotropy_lag=float(ta[old]/tp[old]),elapsed_lag_s=float((et[k]-et[old])*1e-9),source_anchor=str(ef.relative_to(s))+':des_tempperp:'+str(k),calibration_anchor=str(ef.relative_to(s))+':row'+str(old),field_anchor=str(bf.relative_to(s))+':row'+str(idx[k]),electron_quality=int(flags[k]),eligibility='DESflag0,FGMflag0,positive values,backwardfieldmatch<1s; ionfieldsneverconsumed'))
 return finish(rows)
