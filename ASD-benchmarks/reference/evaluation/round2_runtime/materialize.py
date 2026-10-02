"""One-time export of already frozen states. No fitting or history imports."""
from pathlib import Path
import json,hashlib,shutil,re
import pandas as pd
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
CASES=[24,27,37,53,57,60,61,67,71,72,73,82,83,92,100]
PILOT={37,53,67,71,92};BIO={57,60,72,83,100}
EXTRA_INPUTS={27:['saturation_temperature_K'],61:['membrane_index'],82:['past_temperature']}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def current_engine(kind):
 if kind in ['quality_profile','effective_frequency','paired_film','biological_clock','drying','absolute']:return 'adaptive'
 if kind in ['common_detuning','context_clock','common_clock','no_gas_effect','mass_only_gas']:return 'followups'
 if kind in ['common_Q','common_tau','linked_sherwood','developing_film']:return 'transport'
 if kind in ['nominal_common_Q','one_film_scale','reversed_mass']:return 'falsifiers'
 return 'current'
def source_case(n):return next(ROOT.glob(str(n)+'_*'))
def export_case(case_id,outdir):
 n=int(case_id);out=Path(outdir);out.mkdir(parents=True,exist_ok=True);work=source_case(n)/'research_history/continuation-20260930b';records=pd.read_csv(work/'COMPARISON.csv');models={};provenance=[]
 for row in records.to_dict('records'):
  pred=ROOT/row['prediction_path'];folder=pred.parent
  if sha(pred)!=row['sha256']:raise ValueError('Historical prediction checksum mismatch')
  saved=pd.read_csv(pred,dtype={'sample_id':str,'fold':str},float_precision='round_trip');foldmap=dict(zip(saved.sample_id,saved.fold));sources=[pred]
  if pred.is_relative_to(work):
   src=folder/'states.json';source=json.loads(src.read_text());full=source['model'];states={str(z['label']):z['model']for z in source['folds']};engine=current_engine(full['kind']);sources.append(src)
  elif n in PILOT:
   full=json.loads((folder/'model.json').read_text());cfg=json.loads((folder/'CONFIG.json').read_text());states={};engine='previous_cho'if 'adaptive-003'in str(folder) else 'previous_pilot';sources.extend([folder/'model.json',folder/'CONFIG.json'])
   for z in cfg['outer_models']:
    src=folder/z['file'];states[str(z['fold'])]=json.loads(src.read_text())['model'];sources.append(src)
  elif n in BIO:
   full=json.loads((folder/'model.json').read_text());tuning=json.loads((folder/'tuning.json').read_text());states={str(z['outer_fold']):z['model']for z in tuning['fold_models']};engine='previous_bio';sources.extend([folder/'model.json',folder/'tuning.json'])
  else:
   src=folder/'rules.json';rules=json.loads(src.read_text());full=rules['model'];states={str(k):v for k,v in rules['fold_models'].items()};engine='previous_mech';sources.append(src)
  if set(foldmap.values())-set(states):raise ValueError('Missing frozen fold state: '+row['model'])
  name=row['model'];key=re.sub('[^A-Za-z0-9_-]','_',name);state_file='states/'+key+'.json';dest=out/state_file;dest.parent.mkdir(exist_ok=True)
  model={'schema_version':'p100-frozen-oof-1','model_id':f'P100-{n:03d}.round2.v1/{name}','reference_name':name,'mode':'oof','deployment':{'engine':engine,'model':full},'folds':{k:{'engine':engine,'model':v}for k,v in states.items()},'validation_fold_by_sample_id':foldmap,'routing_policy':'Sample ID chooses the independently fitted outer-fold model, not a stored prediction. Unknown IDs reject in OOF mode. Full-development fitted state requires explicit deployment mode; it is not OOF evidence.'}
  dest.write_text(json.dumps(model,separators=(',',':'),allow_nan=False)+'\n');models[name]={'state_file':state_file,'engine':engine,'reference_primary_error':row['primary_error'],'rows':row['rows'],'groups':row['groups'],'metric_unit':row['unit']}
  provenance.extend({'model':name,'source':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}for p in sources)
 target=out/'reference_runtime';target.mkdir(exist_ok=True)
 for p in HERE.glob('*.py'):
  if p.name not in ['materialize.py']:shutil.copy2(p,target/p.name)
 shutil.copy2(HERE/'EXTRACTION.json',target/'EXTRACTION.json')
 (out/'run.py').write_text((HERE/'run_template.txt').read_text())
 rules={'schema_version':'p100-round2-references-1','case_id':n,'task_id':f'P100-{n:03d}.round2.v1','default_reference':'current/cycle-001','default_meaning':'Original preregistered round2 candidate; no scientific admission or winner selection is implied. Every comparator remains separately executable.','models':models,'additional_inputs_for_historical_comparators':EXTRA_INPUTS.get(n,[]),'current_outcome_exposure':'exposed'}
 (out/'rules.json').write_text(json.dumps(rules,indent=2)+'\n');shutil.copy2(out/models['current/cycle-001']['state_file'],out/'model.json')
 (out/'reference_provenance.json').write_text(json.dumps({'assets':provenance},indent=2)+'\n');(out/'requirements.txt').write_text('numpy\npandas\nscipy\n')
 files=[out/'run.py',out/'rules.json',out/'model.json']+sorted((out/'states').glob('*.json'))+sorted(target.glob('*.py'))+[target/'EXTRACTION.json']
 manifest={'schema_version':'p100-runtime-1','verification':'All executable dependency modules and frozen states must match before prediction.','files':[{'path':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':sha(p)}for p in files]}
 (out/'runtime_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 export_training_scope(n,out)
 return rules

def export_training_scope(case_id,outdir):
 """Copy archival fold metadata, preserving unavailable fields as unknown."""
 n=int(case_id);work=source_case(n)/'research_history/continuation-20260930b';models={}
 for row in pd.read_csv(work/'COMPARISON.csv').to_dict('records'):
  pred=ROOT/row['prediction_path'];folder=pred.parent;q=pd.read_csv(pred,dtype={'sample_id':str,'fold':str,'group':str});folds={};scope_source=[]
  if pred.is_relative_to(work):
   p=folder/'states.json';z=json.loads(p.read_text());scope_source=[p]
   for f in z['folds']:
    folds[str(f['label'])]={'training_groups':f.get('training_groups'),'validation_groups':sorted(set(f['validation_groups'])),'validation_ids':f['validation_ids'],'frozen_training_normalization':f.get('scale',{}),'scope_status':'source_recorded'}
  elif n in PILOT:
   cfg=json.loads((folder/'CONFIG.json').read_text());scope_source=[folder/'CONFIG.json']
   for f in cfg['outer_models']:
    p=folder/f['file'];z=json.loads(p.read_text());scope_source.append(p);label=str(f['fold']);v=q[q.fold==label]
    folds[label]={'training_groups':z.get('train_groups'),'validation_groups':z.get('test_groups',sorted(v.group.unique())),'validation_ids':v.sample_id.tolist(),'frozen_training_normalization':{},'scope_status':'source_recorded'if 'train_groups'in z else'training_inventory_unavailable'}
  elif n in BIO:
   p=folder/'tuning.json';z=json.loads(p.read_text());scope_source=[p]
   for f in z['fold_models']:
    label=str(f['outer_fold']);v=q[q.fold==label];train=f['model'].get('training_groups')
    folds[label]={'training_groups':train,'validation_groups':sorted(v.group.unique()),'validation_ids':v.sample_id.tolist(),'frozen_training_normalization':{},'scope_status':'source_recorded'if train is not None else'training_inventory_unavailable'}
  else:
   p=folder/'rules.json';z=json.loads(p.read_text());scope_source=[p]
   for label,state in z['fold_models'].items():
    label=str(label);v=q[q.fold==label];train=state.get('training_groups')
    folds[label]={'training_groups':train,'validation_groups':sorted(v.group.unique()),'validation_ids':v.sample_id.tolist(),'frozen_training_normalization':{},'scope_status':'source_recorded'if train is not None else'training_inventory_unavailable_in_serialized_state'}
  models[row['model']]={'folds':folds,'source_assets':[{'source':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in scope_source], 'interpretation':'Training groups are copied only where explicitly saved, not inferred from a validation complement. Null inventories are unknown, not empty. Validation IDs come from frozen state or frozen prediction cohort. These historical outcomes are now exposed.'}
 output={'schema_version':'principia.reference-training-scope/1.0','case_id':f'P100-{n:03d}','task_id':f'P100-{n:03d}.round2.v1','models':models,'automatic_independence_certification':False,'full_development_state_is_not_oof':True,'training_row_inventory_complete':False,'limits':'Group inventories and frozen learned parameters are reproducibility evidence. They do not prove original training code used only those groups; original fold code, source protocol and independent replay audit remain necessary. Pure-H2 calibration and causal within-group prefixes are governed separately by the task contract.'}
 p=Path(outdir)/'reference_training_scope.json';p.write_text(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n');return output

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('case',type=int);ap.add_argument('output');args=ap.parse_args();print(json.dumps(export_case(args.case,Path(args.output)),indent=2))
