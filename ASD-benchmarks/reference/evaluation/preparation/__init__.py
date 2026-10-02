"""Deterministic native-source preparation. No fitting and no research-history reads."""
from pathlib import Path
import importlib,json,hashlib,zipfile,re,io,contextlib,tempfile
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
class Captured(Exception):
 def __init__(self,data):self.data=data

def _sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def _meta(name):return json.loads((HERE/'metadata'/name).read_text())
def _port(name):return importlib.import_module(__name__+'.ports.'+name)
def _source(data_root,case):
 overrides=HERE/'metadata/source_folders.json'
 if overrides.exists() and str(case) in json.loads(overrides.read_text()):
  rel=Path(json.loads(overrides.read_text())[str(case)])
  if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe source folder override')
  return Path(data_root)/rel
 matches=list(Path(data_root).glob(f'{case:02}_*'))
 if len(matches)!=1:raise ValueError(f'Expected one native source folder for {case}, found {len(matches)}')
 return matches[0]
def verify_source(data_root,case):
 spec=_meta('source_assets.json')[str(case)];p=_source(data_root,case)
 for a in spec:
  f=p/a['path']
  if not f.is_file() or f.stat().st_size!=a['bytes'] or _sha(f)!=a['sha256']:raise ValueError('Native source missing/truncated/checksum mismatch: '+str(f))
 return spec

def base_table(case,data_root):
 """Reconstruct all historically eligible rows directly from native measurements."""
 source=_source(data_root,case)
 if (HERE/'new_cases'/f'P100-{case:03}'/'ADAPTER.json').exists():
  import importlib.util
  base=HERE/'new_cases'/f'P100-{case:03}'
  spec=importlib.util.spec_from_file_location(f'principia_native_{case}',base/json.loads((base/'ADAPTER.json').read_text())['entry'])
  module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
  return module.prepare(Path(data_root))
 if case in [23,52,55,58,59,66,69,78,86,96]:
  m=_port('batch4');m.DATA=Path(data_root)
  def output(i,rows,spec,reserved=None):
   d=pd.DataFrame(rows);d['sample_id']=[f'P100-{i:03}-{j:07}' for j in range(len(d))];groups=sorted(d.group.unique());held=reserved or m.reserve(groups,max(1,round(len(groups)*.2)));d['partition']=np.where(d.group.isin(held),'confirmation','development');raise Captured(d)
  m.output=output;m.WORK=Path(tempfile.gettempdir());m.save=lambda *a:None
  try:getattr(m,f'case{case}')()
  except Captured as e:return e.data
 if case in [57,60,72,83,100]:
  m=_port('batch3');m.DATA=Path(data_root)
  def save(i,rows,*a,**k):raise Captured(pd.DataFrame(rows))
  m.save=save
  try:getattr(m,{57:'rheo',60:'acoustic',72:'yeast',83:'hive',100:'mobile'}[case])()
  except Captured as e:return e.data
 if case in [73,82]:
  m=_port('rumen_soil');m.DATA=Path(data_root);m.freeze=lambda case,d,p:(_ for _ in ()).throw(Captured(d.sort_values('sample_id')))
  try:getattr(m,{73:'rumen',82:'soil'}[case])()
  except Captured as e:return e.data
 if case==61:
  m=_port('membrane');m.SOURCE=source;m.ROOT=source;m.HIST=source/'not-used';return m.prepare()
 if case in [24,27]:
  m=_port('fatigue_boiling');meta=_meta(f'{case}_protocol.json');rows=[]
  for a in meta['groups']:
   f=source/'raw'/a['file'];g=a['group'];part=a['partition']
   if case==24:
    s=f.read_text().splitlines();k=next(i for i,line in enumerate(s) if line.startswith('Timestamp'));d=pd.read_csv(io.StringIO('\n'.join(s[k:])),sep='\t');cal=d.loc[d.Cycle.between(10,20),'StiffnessAvg [GPa]'];cal=cal[np.isfinite(cal)];E0=float(cal.median())
    for ix,v in d[d.Cycle>=1000].iterrows():
     y=float(v['StiffnessAvg [GPa]']);rows.append(dict(sample_id=f'{g}:line{ix+k+2}',group=g,cycle=float(v.Cycle),E0_GPa=E0,strain_percent=float(a['header']['E-max [%]:']),frequency_Hz=float(a['header']['Waveform frequency [Hz]:']),cure=a['stratum'],source_file=f.name,source_line=int(ix+k+2),calibration_anchor=f'{f.name}:cycles10-20',target=y if np.isfinite(y) and y>0 else np.nan,native_target=y,target_quality='nonpositive_extracted_modulus' if y<=0 else 'eligible',partition=part))
   else:
    import xml.etree.ElementTree as ET
    e=ET.parse(f).getroot();rr=e.findall('radial');rmax=max(float(x.findtext('RADIUS')) for x in rr);p=float(e.findtext('PRESSURE'));t,rl,rv=m.saturation(p)
    for j,r in enumerate(rr):rows.append(dict(sample_id=f'{g}:radial{j+1:02d}',group=g,pressure_Pa=p,massflux_kg_m2_s=float(e.findtext('MASSFLUX')),quality=float(e.findtext('XOUT')),radial_fraction=float(r.findtext('RADIUS'))/rmax,rho_liquid=rl,rho_vapor=rv,source_file=f.name,source_radial_index=j+1,saturation_temperature_K=t,target=float(r.findtext('VOIDFRACTION')),partition=part))
  return pd.DataFrame(rows)
 if case==37:
  frames=[]
  for p in sorted((source/'raw').glob('*.csv')):
   d=pd.read_csv(p,sep=';');d['sample_id']=[p.name+':'+str(i+2) for i in range(len(d))];d['group']=p.name;d['source_row']=np.arange(len(d))+2;d['router']='A' if 'modelA' in p.name else 'B';d['throughput_Gbps']=d.Throughput_Gbps;d['packet_bytes']=d.PacketSize_B;d['u']=d.Throughput_Gbps/200;d['q']=d.Throughput_Gbps*1e9/(8*d.PacketSize_B)/1e8;d['target']=d.Power_Consumption;d['partition']='confirmation' if 'iteration3' in p.name else 'development';frames.append(d)
  return pd.concat(frames,ignore_index=True)
 if case==53:
  m=_port('screw');split=_meta('53_split.json');frames=[]
  with zipfile.ZipFile(source/'raw/s02_variations-in-surface-friction.zip') as z:
   for role in ['development','sealed_test']:
    d,ledger,timing,margins,audit=m.extract(z,split,role,{'authorization_sha256':'all historical outcomes now exposed'});d['sample_id']=d.run_id.astype(str);d['group']=d.workpiece_id.astype(str);d['target']=d.late_mean_torque_Nm;d['partition']='confirmation' if role=='sealed_test' else 'development';frames.append(d)
  return pd.concat(frames,ignore_index=True)
 if case==67:
  m=_port('settling');m.SOURCE=source;m.SPLIT=_meta('67_split.json');m.DESIGN=_meta('67_design.json');frames=[]
  bounds={}
  for group,value in re.findall(r'^set ([123]\.[123]) ([0-9.]+) m',(source/'raw/README_MPs_sinking_dynamics.txt').read_text(),re.M):bounds.setdefault(group,[]).append(float(value))
  if bounds!=m.DESIGN['source_interface_bounds_m']:raise ValueError('Source interface bounds differ from frozen contract')
  m.DESIGN['source_interface_bounds_m']=bounds
  for part in ['development','confirmation']:
   d,*_=m.extract(part);d['sample_id']=d.run_id;d['group']=d.config;d['target']=d.target_s;d['partition']=part;frames.append(d)
  return pd.concat(frames,ignore_index=True)
 if case==71:
  m=_port('cho');m.SOURCE=source;m.SPLIT=_meta('71_split.json');frames=[]
  for final in [False,True]:
   with contextlib.redirect_stdout(io.StringIO()):d,audit,flags=m.prepare(final)
   d['group']=d.experiment;d['target']=d.vcd_million_ml;d['partition']='confirmation' if final else 'development';d['source_workbook']=[f'Individual raw data tables/{e}_{mode}.xlsx' for e,mode in zip(d.experiment,d['mode'])];d['source_offline_sheet']=d.reactor+'_offline_CellAnalysis';d['source_vcd_cell']=['B'+str(int(s.split('_')[-1])+2) for s in d.sample_id];aa={a['sample_id']:a for a in audit if 'streams' in a};d['causal_sensor_timestamps_json']=[json.dumps(_finite_json({'current':{k:v['used_timestamp_per_channel'] for k,v in aa[s]['streams'].items()},'history':aa[s]['history']}),sort_keys=True,allow_nan=False) for s in d.sample_id];frames.append(d)
  return pd.concat(frames,ignore_index=True)
 if case==92:
  m=_port('ble');m.ARCHIVE=source/'raw/SC BLE Fingerprinting.zip';m.SPLIT=_meta('92_split.json');frames=[]
  for part in ['development','confirmation']:
   d,cal,counts=m.extract(part);d['sample_id']=d.member+'|'+d.port+'|'+d.channel.astype(str);d['partition']=part;frames.append(d)
  return pd.concat(frames,ignore_index=True)
 raise NotImplementedError(f'No native parser for case {case}')

def prepare(task,data_root,supplemental_root,output):
 case=int(task.get('case_number',str(task['case_id']).split('-')[-1]));taskid=task.get('id',task.get('task_id'));schema=_meta('task_schemas.json')[taskid]
 verified=verify_source(data_root,case);d=pd.DataFrame() if task['family']=='supplemental' or (case==96 and task['family']=='continuation') else base_table(case,data_root)
 if task['family']!='original':d=extend_table(task,d,data_root,supplemental_root)
 d['sample_id']=d.sample_id.astype(str);d['group']=d.group.astype(str)
 if d.sample_id.duplicated().any():raise ValueError('Native reconstruction duplicate sample IDs')
 # The cohort is a frozen list of metadata identifiers, never cached predictors or targets.
 selected=d.set_index('sample_id',drop=False);ids=schema['cohort_ids'];missing=sorted(set(ids)-set(selected.index))
 if missing:raise ValueError(f'Raw reconstruction missing {len(missing)} cohort IDs: {missing[:3]}')
 selected=selected.loc[ids].reset_index(drop=True)
 if 'group_by_sample_id' in schema:
  selected['source_group']=selected.group;selected['group']=[schema['group_by_sample_id'][s] for s in selected.sample_id]
 needed=set(schema['inputs_columns']+schema['observations_columns'])
 if not needed<=set(selected):raise ValueError('Native reconstruction unavailable columns: '+str(sorted(needed-set(selected))))
 out=Path(output)
 if out.exists() and any(out.iterdir()):raise FileExistsError('Preparation output must be empty/new')
 (out/'data').mkdir(parents=True,exist_ok=True)
 def write(name,frame):frame.to_csv(out/'data'/name,index=False,compression={'method':'gzip','mtime':0},float_format='%.17g')
 write('inputs.csv.gz',selected[schema['inputs_columns']]);write('observations.csv.gz',selected[schema['observations_columns']]);anchors=[c for c in selected if c.startswith('source_') or 'anchor' in c or 'timestamp' in c];write('anchors.csv.gz',selected[['sample_id','group']+anchors]);write('calibration.csv.gz',calibration_records(task,d));write('eligibility.csv.gz',pd.DataFrame({'sample_id':d.sample_id,'eligible_for_task':d.sample_id.isin(ids),'reason':np.where(d.sample_id.isin(ids),'frozen cohort included','outside frozen task cohort')}));write('groups.csv.gz',selected[[c for c in ['sample_id','group','partition','fold','particle','experiment','vessel','workpiece_id','video'] if c in selected]])
 receipt={'task_id':taskid,'status':'reconstructed','native_assets_verified':len(verified),'rows':len(selected),'fitting_performed':False,'historical_prepared_tables_read':False,'current_exposure':'exposed','parser':'source-derived frozen deterministic code','cohort':'immutable declared identifier inventory','files':[{'path':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':_sha(p)} for p in sorted((out/'data').glob('*'))]};(out/'preparation.json').write_text(json.dumps(receipt,indent=2)+'\n');return receipt

def extend_table(task,d,data_root,supplemental_root):
 from .extensions import transform
 return transform(task,d,data_root,supplemental_root)

def calibration_records(task,d):
 case=int(task['case_number']); keys=['sample_id','group']
 if 'calibration_columns'in task:
  columns=task['calibration_columns'];missing=set(columns)-set(d)
  if missing:raise ValueError('Declared calibration columns unavailable: '+str(sorted(missing)))
  anchors=[c for c in d if 'anchor'in c or c.startswith('source_')]
  selected=list(dict.fromkeys(keys+columns+anchors))
  out=d[selected].copy()if columns else pd.DataFrame(columns=keys+['calibration_status'])
  out['calibration_status']='Explicit registered calibration/history columns; '+str(task['calibration'])
  return out
 if task['family']=='supplemental':
  return d[d.partition=='calibration'][[c for c in ['sample_id','group','temperature_C','omega','target','loss_modulus','anchor'] if c in d]].copy()
 if case==61 and 'kind' in d and (d.kind=='pure').any():
  return d[(d.kind=='pure')&(d.partition=='development')].copy()
 if (HERE/'new_cases'/f'P100-{case:03}'/'ADAPTER.json').exists():
  columns=[c for c in d if c.startswith(('cal_','calibration_','anchor_','early_','lag','previous_','baseline_','prefix_'))or c in ['own_previous','other_previous','own_lag2','other_lag2','initial_stiffness_kN_mm','recent_stiffness_kN_mm','temperature_lag','density_lag','field_lag','anisotropy_lag','background_low','background_high','offline','u60','u120','u10']]
  if not columns:return pd.DataFrame(columns=['sample_id','group','calibration_status'])
  out=d[keys+columns].copy();out['calibration_status']='Explicit task-permitted calibration/history; source anchors in preparation output';return out
 columns={24:['E0_GPa','calibration_anchor'],53:['prev_y','prev_early','prev_gradient','first_y','mean_past_y','history_gap'],55:['initial_force','initial_shape_change','initial_anchor'],57:['eta_previous','eta_first','T_previous','previous_shear_s','first_shear_s'],61:['calibration_j0'],67:['z_upper_m','z_lower_m','width_m'],69:['initial_C'],72:['p22_pct','p72_pct','S22','S72','G22','G72','F22','F72'],73:['g4','g8'],92:['r0','channel_contrast','spatial_contrast']}.get(case,[])
 columns=[c for c in columns if c in d]
 if not columns:return pd.DataFrame(columns=['sample_id','group','calibration_status'])
 out=d[keys+columns].copy();out['calibration_status']='explicitly permitted historical or separate calibration; no current scored target';return out

def _finite_json(value):
 if isinstance(value,dict):return {k:_finite_json(v) for k,v in value.items()}
 if isinstance(value,list):return [_finite_json(v) for v in value]
 if isinstance(value,float) and not np.isfinite(value):return None
 return value
