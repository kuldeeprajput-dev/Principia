#!/usr/bin/env python3
"""Import legacy round2 CSV predictions into a v3 numerical-only submission.

No equation, finding, training inventory, input access or reproducibility claim is
inferred from a CSV. This helper never executes imported code or refits a model.
"""
from pathlib import Path
import argparse,shutil,json,tempfile
import numpy as np
import pandas as pd
from common import VERSION, context, digest, save_json, table, new_output, asset_record

IMPORT_VERSION='principia.legacy-csv-import/1.0'
REQUIRED={'sample_id','group','prediction'}
OPTIONAL={'abstention_reason','target','fold','particle','condition_scale'}

def import_predictions(identifier,csv_path,output):
 task,package,x,y,refs=context(identifier)
 if task['family']!='round2':raise ValueError('This version imports only the registered round2 CSV interface')
 source=Path(csv_path)
 if not source.is_file():raise ValueError('Missing legacy prediction CSV')
 d=table(source,strings=True)
 if not REQUIRED.issubset(d) or set(d)-REQUIRED-OPTIONAL:raise ValueError('Unsupported legacy CSV columns')
 if d.sample_id.str.strip().eq('').any()or not d.sample_id.is_unique:raise ValueError('Empty or duplicate legacy sample IDs')
 if set(d.sample_id)!=set(x.sample_id):raise ValueError('Legacy prediction inventory mismatch; use explicit reasoned abstentions for all omitted predictions')
 d=d.set_index('sample_id').loc[x.sample_id].reset_index()
 if not np.array_equal(d.group.to_numpy(),x.group.to_numpy()):raise ValueError('Legacy group inventory mismatch')
 supplied=[]
 for col in['fold','particle']:
  if col in d:
   auth=x if col in x else y
   if col not in auth or not np.array_equal(d[col].to_numpy(),auth[col].astype(str).to_numpy()):raise ValueError('Legacy metadata mismatch: '+col)
   supplied.append(col)
 for col in['target','condition_scale']:
  if col in d:
   if col not in y:raise ValueError('Legacy metadata unavailable for verification: '+col)
   z=pd.to_numeric(d[col].replace('',np.nan),errors='raise').to_numpy(float)
   if np.isinf(z).any()or not np.allclose(z,y[col].to_numpy(float),rtol=1e-12,atol=1e-12,equal_nan=True):raise ValueError('Legacy metadata mismatch: '+col)
   supplied.append(col)
 active=d.prediction.str.strip().ne('');reasons=d.get('abstention_reason',pd.Series('',index=d.index))
 if reasons.loc[~active].str.strip().eq('').any():raise ValueError('Blank predictions require an abstention reason')
 values=pd.to_numeric(d.prediction.replace('',np.nan),errors='raise')
 if not np.isfinite(values.loc[active]).all():raise ValueError('Nonfinite legacy prediction')
 if task.get('positive_prediction')and(values.loc[active]<=0).any():raise ValueError('Task requires positive predictions')
 if task.get('nonnegative_prediction')and(values.loc[active]<0).any():raise ValueError('Task requires nonnegative predictions')
 pred=pd.DataFrame({'sample_id':x.sample_id,'prediction':d.prediction,'status':np.where(active,'predict','abstain'),'reason':reasons.where(~active,'')})
 out=new_output(output);out.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='.principia-legacy-import-',dir=out.parent)as temp:
  staged=Path(temp);source_name='legacy_predictions.csv.gz'if source.suffix=='.gz'else'legacy_predictions.csv';shutil.copyfile(source,staged/source_name);pred.to_csv(staged/'predictions.csv',index=False)
  receipt={'schema_version':IMPORT_VERSION,'task_id':task['task_id'],'protocol_version':task['protocol_version'],'cohort_id':task['cohort_id'],'evaluator_version':VERSION,'native_csv_asset':source_name,'native_csv_sha256':digest(staged/source_name),'native_source_filename':source.name,'native_columns':list(d.columns),'verified_optional_metadata':supplied,'assigned_rows':len(x),'predicted_rows':int(active.sum()),'abstained_rows':int((~active).sum()),'input_budget_status':'unknown_historical','training_inventory_status':'unknown_historical','evaluation_data_usage':'unknown_historical','inferred_equations':False,'inferred_findings':False,'source_code_executed':False,'fresh_confirmation':False}
  save_json(staged/'IMPORT_RECEIPT.json',receipt)
  assets=[asset_record(staged/source_name,staged),asset_record(staged/'IMPORT_RECEIPT.json',staged)]
  metadata={'schema_version':'principia.submission/3.0','submission_kind':'historical_prediction_import',**{k:task[k]for k in['case_id','task_id','protocol_version','cohort_id','input_sha256','target_units']},'evaluator_version':VERSION,'decision':'predict'if active.any()else'abstain','abstention_reason':''if active.any()else'All legacy records explicitly abstained; see each original row reason.','permitted_inputs':[],'input_budget_status':'unknown_historical','predictions_file':'predictions.csv','predictions_sha256':digest(staged/'predictions.csv'),'training':{'training_group_ids':[],'tuning_group_ids':[],'inventory_status':'unknown_historical','evaluation_data_usage':'unknown_historical','inventory_assets':[],'note':'Empty group and input lists represent unavailable declarations, not proof that no data or predictors were used.'},'equations':[],'findings':[],'uncertainty':{'interval_level':None,'method':'Not available in the legacy CSV interface'},'reproducibility':{'entrypoint':None,'assets':assets},'compatibility_import':{'schema_version':IMPORT_VERSION,'receipt':'IMPORT_RECEIPT.json','native_asset':source_name,'native_sha256':digest(staged/source_name),'comparability':'numerical_only_unverified_information_access'}}
  save_json(staged/'submission.json',metadata)
  from submissions import validate
  validate(staged,task,x)
  shutil.copytree(staged,out)
 return {'status':'imported_prediction_only','task_id':task['task_id'],'output':str(out),'predicted_rows':int(active.sum()),'input_budget_status':'unknown_historical','training_inventory_status':'unknown_historical','scientific_claims_supplied':False,'source_code_executed':False}

def validate_import_binding(folder,submission,task,x):
 """Check the explicit import variant; never guess absent scientific declarations."""
 from common import safe_path,load_json
 folder=Path(folder);meta=submission.get('compatibility_import',{})
 if meta.get('schema_version')!=IMPORT_VERSION or meta.get('comparability')!='numerical_only_unverified_information_access':raise ValueError('Unsupported legacy import contract')
 if task['family']!='round2':raise ValueError('Legacy CSV import task must be round2')
 if submission.get('input_budget_status')!='unknown_historical' or submission['permitted_inputs']!=[]:raise ValueError('CSV-only import must disclose unknown input access')
 tr=submission['training']
 if tr.get('inventory_status')!='unknown_historical' or tr.get('evaluation_data_usage')!='unknown_historical' or tr['training_group_ids']or tr['tuning_group_ids']or tr.get('inventory_assets'):raise ValueError('CSV-only import cannot invent training declarations')
 if submission.get('equations')or submission.get('findings')or submission['reproducibility'].get('entrypoint')is not None:raise ValueError('CSV-only import cannot invent models or scientific claims')
 names={a['path']for a in submission['reproducibility']['assets']}
 if meta.get('receipt')not in names or meta.get('native_asset')not in names:raise ValueError('Import receipt and native CSV must be hashed assets')
 receipt=load_json(safe_path(folder,meta['receipt']));native=safe_path(folder,meta['native_asset'])
 if receipt.get('schema_version')!=IMPORT_VERSION or receipt.get('task_id')!=task['task_id']or receipt.get('protocol_version')!=task['protocol_version']or receipt.get('cohort_id')!=task['cohort_id']:raise ValueError('Legacy receipt/task identity mismatch')
 if receipt.get('native_csv_asset')!=meta['native_asset']or receipt.get('native_csv_sha256')!=digest(native)or meta.get('native_sha256')!=digest(native):raise ValueError('Native CSV import hash mismatch')
 for key in['inferred_equations','inferred_findings','source_code_executed','fresh_confirmation']:
  if receipt.get(key)is not False:raise ValueError('Legacy receipt makes unsupported claims')
 for key in['input_budget_status','training_inventory_status','evaluation_data_usage']:
  if receipt.get(key)!='unknown_historical':raise ValueError('Legacy receipt hides unavailable provenance')
 native_frame=table(native,strings=True);canonical=table(safe_path(folder,submission['predictions_file']),strings=True)
 if not REQUIRED.issubset(native_frame)or set(native_frame)-REQUIRED-OPTIONAL or not native_frame.sample_id.is_unique:raise ValueError('Malformed bound native legacy CSV')
 if set(native_frame.sample_id)!=set(canonical.sample_id):raise ValueError('Imported/native prediction inventory mismatch')
 native_frame=native_frame.set_index('sample_id').loc[canonical.sample_id].reset_index();active=native_frame.prediction.str.strip().ne('')
 authoritative=x.set_index('sample_id').loc[canonical.sample_id]
 if not np.array_equal(native_frame.group.to_numpy(),authoritative.group.to_numpy()):raise ValueError('Bound native group inventory mismatch')
 if not np.array_equal(np.where(active,'predict','abstain'),canonical.status.to_numpy()):raise ValueError('Imported/native abstention mismatch')
 before=pd.to_numeric(native_frame.loc[active,'prediction'],errors='raise').to_numpy(float);after=pd.to_numeric(canonical.loc[active,'prediction'],errors='raise').to_numpy(float)
 if not np.isfinite(before).all()or not np.array_equal(before,after):raise ValueError('Imported predictions differ from bound native CSV')
 reasons=native_frame.get('abstention_reason',pd.Series('',index=native_frame.index))
 if not np.array_equal(reasons.loc[~active].to_numpy(),canonical.loc[~active,'reason'].to_numpy()):raise ValueError('Imported/native abstention reason mismatch')
 if receipt.get('assigned_rows')!=len(canonical)or receipt.get('predicted_rows')!=int(active.sum())or receipt.get('abstained_rows')!=int((~active).sum()):raise ValueError('Legacy receipt coverage mismatch')
 return {'import_schema_version':IMPORT_VERSION,'input_budget_status':'unknown_historical','information_access_verified':False,'training_inventory_status':'unknown_historical','scientific_claims_supplied':False,'comparability':'numerical_only_unverified_information_access'}

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--task',required=True);ap.add_argument('--csv',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 try:print(json.dumps(import_predictions(a.task,a.csv,a.output),allow_nan=False))
 except (ValueError,KeyError,TypeError,OSError)as e:raise SystemExit('ERROR: '+str(e))
