from pathlib import Path
import json,hashlib,datetime,shutil
import numpy as np,pandas as pd
from run import predict
HERE=Path(__file__).resolve().parent

def main():
    f=json.loads((HERE/'FREEZE.json').read_text())
    for a in f['files']:
        p=HERE/a['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Freeze violation: '+a['path'])
    if (HERE/'CONFIRMATION_RECEIPT.json').exists():raise ValueError('Confirmation already opened; preserve its receipt')
    d=pd.read_csv(HERE/'prepared.csv.gz',float_precision='round_trip');q=d[d.partition=='confirmation'].reset_index(drop=True);protocol=json.loads((HERE/'PROTOCOL.json').read_text());out=HERE/'package';(out/'data').mkdir(exist_ok=True);(out/'evidence').mkdir(exist_ok=True)
    states={label:json.loads((HERE/path).read_text())for label,path in f['models'].items()};states={'reference':dict(states[f['selected']]),**states}
    pred=q[['sample_id','group']].copy();metrics=[];group_metrics=[]
    for label,state in states.items():
        z=predict(state,q)
        if not np.isfinite(z).all():raise ValueError('Nonfinite prediction')
        pred[label]=z;err=np.abs(q.target.to_numpy()-z);groups=[]
        for group,ix in q.groupby('group').groups.items():
            mae=float(err[list(ix)].mean());groups.append(mae);group_metrics.append({'model':label,'group':group,'mae':mae,'rmse':float(np.sqrt(np.mean((z[list(ix)]-q.target.to_numpy()[list(ix)])**2))),'bias':float(np.mean(z[list(ix)]-q.target.to_numpy()[list(ix)])),'rows':len(ix)})
        metrics.append({'model':label,'primary_error':float(np.mean(groups)),'mean_group_absolute_error':float(np.mean(groups)),'groups':len(groups),'scored_rows':len(q),'assigned_rows':len(q),'primary_units':protocol['units']})
    inp=q[['sample_id','group']+protocol['inputs']];obs=q[[c for c in q.columns if c not in protocol['inputs']]]
    inp.to_csv(out/'data/inputs.csv.gz',index=False,float_format='%.17g');obs.to_csv(out/'data/observations.csv.gz',index=False,float_format='%.17g');pred.to_csv(out/'evidence/predictions.csv.gz',index=False,float_format='%.17g');pd.DataFrame(metrics).to_csv(out/'evidence/metrics.csv',index=False,float_format='%.17g');pd.DataFrame(group_metrics).to_csv(out/'evidence/by_group.csv',index=False,float_format='%.17g')
    rules={'case_id':protocol['case_id'],'source':{'landing_url':json.loads((HERE/'PRIOR_ART.json').read_text())['primary_urls'][0]},'input_columns':protocol['inputs'],'numeric_columns':protocol['inputs'],'input_units':protocol['input_units'],'target':protocol['target'],'target_units':protocol['units'],'metric_kind':'mae','metric_units':protocol['units'],'assigned_rows':len(q),'selected_from':f['selected'],'models':states,'missingness_policy':'No nonfinite inputs; preserve signed optical targets. All eligible native rows in frozen confirmation groups.','exposure':'All packaged confirmation outcomes now exposed; internal first-use holdout history recorded in FREEZE/CONFIRMATION_RECEIPT.','classification':'Predictive reference, not automatic physical law or novelty proof.'};(out/'rules.json').write_text(json.dumps(rules,indent=2));shutil.copyfile(HERE/'run.py',out/'run.py');shutil.copyfile(HERE/'requirements.txt',out/'requirements.txt')
    spec={'case_id':protocol['case_id'],'target':protocol['target'],'target_units':protocol['units'],'error_units':protocol['units'],'metric_kind':'mae','permitted_inputs':protocol['inputs'],'input_units':protocol['input_units'],'numeric_columns':protocol['inputs'],'timing_contract':protocol['timing'],'calibration':protocol['calibration'],'independent_unit':protocol['group'],'scope_limits':protocol['scope'],'source_url':rules['source']['landing_url'],'source_license':'CC BY4.0','exposure':{'current':'exposed','internal_confirmation':'held out until frozen model/stop selection','fresh_for_future_users':False},'uncertainty_policy':protocol['uncertainty'],'aggregation':{'hierarchy':['group'],'weights':'equal group then equal eligible row'},'selection':f['selected'],'training_scope':'See each state training_scope; complete development groups only.','outcome_cohort':'reserved groups recorded in SPLITS.json; no calibration anchors scored.'};(out/'task_spec.json').write_text(json.dumps(spec,indent=2))
    receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'freeze_sha256':hashlib.sha256((HERE/'FREEZE.json').read_bytes()).hexdigest(),'selected_before_confirmation':f['selected'],'metrics':metrics,'groups':sorted(q.group.unique()),'rows':len(q),'future_status':'exposed','no_fitting_in_confirmation':True};(HERE/'CONFIRMATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2));print(json.dumps({'case':protocol['case_id'],'selected':f['selected'],'metrics':metrics},indent=2))
if __name__=='__main__':main()
