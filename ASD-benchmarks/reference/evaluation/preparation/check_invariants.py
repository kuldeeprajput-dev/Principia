"""Portable native-preparation guard and causal-prefix falsification checks."""
from pathlib import Path
import argparse,json,tempfile,shutil,hashlib
import numpy as np,pandas as pd
from . import _port,verify_source,_source,_meta

def run(data_root):
 checks=[]
 def ok(name,detail):checks.append({'name':name,'status':'pass','detail':detail})
 m=_port('screw');x=np.arange(0.,1401.,10.);y=.2+.0001*x;step={'graph':{'angle values':x.tolist(),'torque values':y.tolist()}};finding={'graph':{'angle values':np.arange(20.).tolist(),'torque values':np.ones(20).tolist()}};steps={'Thread forming':step,'Finding':finding};a,_=m.prefix_features(steps);corrupted=json.loads(json.dumps(steps));corrupted['Thread forming']['graph']['torque values'][26:]=[1e9]*(len(x)-26);b,_=m.prefix_features(corrupted);assert a==b;ok('screw_future_torque_poisoning','Later torque values cannot change at-trigger prefix features.')
 m=_port('settling');d=pd.DataFrame({'x':np.zeros(12),'z':np.linspace(.012,.036,12),'t':np.arange(12,dtype=float),'angle':np.linspace(0,90,12)});a,_,_=m.upstream_features(d,.03,'D_a');ix=np.flatnonzero(d.z.to_numpy()>.028)[0];v=d.copy();v.loc[ix:,'angle']=1e12;v.loc[ix:,'x']=1e10;v.loc[ix:,'z']+=.1;b,_,_=m.upstream_features(v,.03,'D_a');assert a==b;ok('settling_future_position_orientation_poisoning','Post-cutoff amplitude/orientation perturbations leave all upstream features unchanged.')
 m=_port('cho');d=pd.DataFrame({'Time (h)':[0,.5,1,1.5,2],'Status':['Ok','Ok','bad','Ok','Ok'],'Permittivity (pF/cm)':[1,2,50,4,5]});a,aa=m.summarize(d,.5,['Permittivity (pF/cm)']);v=d.copy();v.loc[v['Time (h)']>.5,'Permittivity (pF/cm)']=1e10;b,bb=m.summarize(v,.5,['Permittivity (pF/cm)']);assert a==b and aa==bb;assert a['Permittivity (pF/cm)']==1.5;ok('cho_future_sensor_poisoning','Trailing valid sensor summary has no future response dependence.')
 a,qa=m.summarize(d,1.,['Permittivity (pF/cm)']);assert a['Permittivity (pF/cm)']==2 and qa['invalid_status_rows']==1;ok('cho_quality_flag_preserved','Invalid source status cannot enter the native summary even when its reading is finite.')
 src=_source(data_root,23);spec=_meta('source_assets.json')['23']
 with tempfile.TemporaryDirectory() as tmp:
  root=Path(tmp);dest=root/src.name;shutil.copytree(src/'raw',dest/'raw')
  verify_source(root,23);ok('native_hash_verified_before_parse','Pristine copied native input verifies.')
  first=dest/spec[0]['path'];saved=first.read_bytes();first.write_bytes(saved[:-1])
  try:verify_source(root,23)
  except ValueError:ok('truncated_native_rejected','Truncated source rejected by frozen byte count and SHA-256.')
  else:raise AssertionError('Truncation accepted')
  first.write_bytes(bytes([saved[0]^1])+saved[1:])
  try:verify_source(root,23)
  except ValueError:ok('same_size_native_mutation_rejected','Equal-length source mutation rejected by SHA-256.')
  else:raise AssertionError('Mutation accepted')
  first.unlink()
  try:verify_source(root,23)
  except ValueError:ok('missing_native_rejected','Missing source rejected before scientific parsing.')
  else:raise AssertionError('Missing file accepted')
 return {'status':'pass','checks':checks,'no_fitting':True,'scientific_scope':'Computational prefix/guard checks, not independent experimental replication.'}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--data-root',required=True,type=Path);a.add_argument('--output',type=Path);o=a.parse_args();report=run(o.data_root)
 if o.output:o.output.write_text(json.dumps(report,indent=2)+'\n')
 else:print(json.dumps(report,indent=2))
