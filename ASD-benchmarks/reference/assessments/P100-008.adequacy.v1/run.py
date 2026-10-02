from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
def verify():
 manifest=json.loads((HERE/'MANIFEST.json').read_text())
 for a in manifest.get('assets',manifest.get('files',[])):
  p=HERE/a['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Evidence integrity failure: '+a['path'])
 e=json.loads((HERE/'data/source_evidence.json').read_text())
 checks={'one_patient':e['patients']==1,'one_mr_echo':len(e['mr_echo_times_ms'])==1,'distinct_frames':e['frame_count']>1,'clinical_truth_absent':not e['clinical_targets_retained'],'calibration_absent':not e['absolute_calibration_retained']}
 if not all(checks.values()):raise ValueError('Frozen adequacy evidence no longer matches checks')
 return {'status':'scientific_abstention','checks':checks,'prediction_metrics':None,'new_task_requires_independent_review':True}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
