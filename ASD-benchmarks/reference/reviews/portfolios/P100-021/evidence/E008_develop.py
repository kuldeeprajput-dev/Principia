from pathlib import Path
import argparse,datetime,hashlib,json,shutil
import numpy as np,pandas as pd
from scipy.optimize import minimize
from run import predict,features
HERE=Path(__file__).resolve().parent

def weights(d):return 1/d.groupby('group').group.transform('size').to_numpy(float)/d.group.nunique()
def metric(d,p):
    a=pd.DataFrame({'group':d.group.to_numpy(),'error':np.abs(d.target.to_numpy()-p)}).groupby('group').error.mean()
    return {'primary_error':float(a.mean()),'worst_group_error':float(a.max()),'by_group':a.to_dict(),'groups':len(a),'rows':len(d)}

def fit(case,kind,d):
    y=d.target.to_numpy(float);wt=weights(d);m={'case':case,'kind':kind}
    if case==21:
        w=d.width_um.to_numpy(float);b=d.wafer_b.to_numpy(float);o=d.outer.to_numpy(float);A=float(np.median(y*w*w));
        if kind=='constant':m['theta']=[float(np.median(y))];return m
        if kind=='flexible':
            x=np.column_stack([np.ones(len(d)),1/w,1/w**2,b,b/w,b/w**2,o/w**2]);c=np.linalg.lstsq(x*np.sqrt(wt[:,None]),y*np.sqrt(wt),rcond=None)[0];m['theta']=c.tolist();return m
        setups={'area':([np.log(A)],[(0,20)]),'edge':([np.log(A),0],[(0,20),(-2,.8)]),'perimeter':([-np.log(A),-np.log(A)-2],[(-25,0),(-25,0)]),'wafer_edge':([np.log(A),0,0,0],[(0,20),(-5,5),(-1,.6),(-.2,.2)]),'region':([np.log(A),0,0,0],[(0,20),(-5,5),(-5,5),(-2,.8)]),'wafer_area':([np.log(A),0],[(0,20),(-5,5)]),'series':([np.log(A),0,0,0],[(0,20),(-5,5),(-2,.8),(-15,10)])}
        init,bounds=setups[kind]
    elif case==51:
        if kind in ['linear','loglinear']:return m
        if kind in ['shape','shape_blend']:
            v=d.gate_V.to_numpy();pos=v>=0;lo=d.cal_minus20_uA.to_numpy();mid=d.cal_zero_uA.to_numpy();hi=d.cal_plus20_uA.to_numpy();z=np.where(pos,(y-mid)/np.maximum(hi-mid,1e-12),(y-lo)/np.maximum(mid-lo,1e-12));a=pd.DataFrame({'v':v,'z':z}).groupby('v').z.median();m['grid']=a.index.tolist();m['shape']=a.to_list()
            if kind=='shape':return m
            init,bounds=[.5],[(0,1)]
        else:
            setups={'power':([1.5],[(.1,8)]),'two_power':([1.5,2],[(.1,8),(.1,12)]),'softplus':([3,2],[(-15,19),(.1,20)]),'contact':([3,2,.01],[(-15,19),(.1,20),(0,2)]),'anchor_power':([1.5,0,2],[(.1,8),(-.5,.5),(.1,12)]),'anchored_bend':([-.2,0,2],[(-1,1),(-1,1),(.1,12)])};init,bounds=setups[kind]
    else:
        if kind=='persistence':return m
        x=features(kind,d);scale=np.sqrt(np.sum(wt[:,None]*x*x,axis=0));scale[scale<1e-8]=1;xx=x/scale;ridge=.01 if kind=='flexible'else 1e-6
        c=np.linalg.solve(xx.T@(wt[:,None]*xx)+ridge*np.eye(x.shape[1]),xx.T@(wt*(y-d.cal_photo_nA.to_numpy())))/scale;m['theta']=c.tolist();return m
    fun=lambda a:float(np.sum(wt*np.abs(predict({**m,'theta':a},d)-y)))
    opt=minimize(fun,init,method='Powell',bounds=bounds,options={'maxiter':200,'ftol':1e-9,'xtol':1e-7});m['theta']=opt.x.tolist();m['optimizer']={'success':bool(opt.success),'message':str(opt.message),'objective':float(opt.fun)};return m

def run(config):
    c=json.loads(Path(config).read_text());case=c['case'];kind=c['kind'];label=c['label'];out=HERE/('baselines'if c.get('baseline')else'attempts')/label
    if (out/'metrics.json').exists():raise ValueError('Completed receipt is immutable; use separate correction record')
    out.mkdir(parents=True,exist_ok=True);shutil.copyfile(config,out/'config.json') if Path(config).resolve()!=(out/'config.json').resolve()else None
    d=pd.read_csv(HERE/'development.csv.gz');pred=np.empty(len(d));states={}
    for g in sorted(d.group.unique()):
        tr=d[d.group!=g];q=d.group==g;state=fit(case,kind,tr);states[g]=state;pred[q]=predict(state,d[q])
    full=fit(case,kind,d);full['training_scope']={'groups':sorted(d.group.unique()),'rows':len(d),'partition':'development only','prepared_sha256':hashlib.sha256((HERE/'development.csv.gz').read_bytes()).hexdigest()};scores=metric(d,pred)
    (out/'model.json').write_text(json.dumps(full,indent=2));(out/'fold_models.json').write_text(json.dumps(states,indent=2));(out/'metrics.json').write_text(json.dumps(scores,indent=2));q=d[['sample_id','group','target']].copy();q['prediction']=pred;q.to_csv(out/'predictions.csv.gz',index=False,float_format='%.17g');(out/'COMPLETED.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'run_sha256':hashlib.sha256((HERE/'run.py').read_bytes()).hexdigest(),'config_sha256':hashlib.sha256((out/'config.json').read_bytes()).hexdigest()},indent=2));print(json.dumps({'case':case,'label':label,'kind':kind,**{k:v for k,v in scores.items()if k!='by_group'},'theta':full.get('theta')}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('config');run(p.parse_args().config)
