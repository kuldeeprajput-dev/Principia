"""Independent native future-mutation tests; all mutations occur in temporary fixtures.
Run with the campaign QA Python. No fitting, model selection or scientific-package writes.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,io,json,math,os,shutil,tempfile,zipfile,datetime,csv
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np
import pandas as pd
W=Path(__file__).resolve().parents[1]
D=Path(os.environ.get('PRINCIPIA_DATA_ROOT',str(W.parents[2]/'local-datas')))
import threading
BASE88=None
LOCK88=threading.Lock()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def csv_tail(blob,cut,cols,increment,header_rows=1):
 lines=blob.decode().splitlines(keepends=True);changed=0
 for i in range(cut,len(lines)-header_rows):
  j=i+header_rows;row=next(csv.reader([lines[j]]));modified=False
  for k in cols:
   x=float(row[k])
   if np.isfinite(x):row[k]=format(x+increment,'.17g');modified=True
  if modified:
   buf=io.StringIO();csv.writer(buf,lineterminator='\n').writerow(row);lines[j]=buf.getvalue();changed+=1
 return ''.join(lines).encode(),changed

def patch_zip(source,dest,patch):
 changes=[]
 with zipfile.ZipFile(source) as zin,zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1) as zout:
  for info in zin.infolist():
   blob=zin.read(info.filename)
   if info.filename in patch:blob,detail=patch[info.filename](blob);changes.append(dict(member=info.filename,**detail))
   zout.writestr(info,blob)
 return changes

def fixture(C,manifest,mutate_paths):
 # Read-only symlinks are used only for assets that are never modified.
 temp=tempfile.TemporaryDirectory(prefix='principia_native_prefix_');T=Path(temp.name);A=T/'adapter';E=T/'data';A.mkdir()
 fname='native_current.py' if C.name=='P100-088' else 'native.py';shutil.copy2(C/fname,A/'native.py');shutil.copy2(C/'SPLITS.json',A/'SPLITS.json')
 for asset in manifest['assets']:
  p=E/asset['path'];p.parent.mkdir(parents=True,exist_ok=True)
  if asset['path'] not in mutate_paths:p.symlink_to(D/asset['path'])
 return temp,A,E

def compare(base,modified,selected,inputs,scope):
 B=base.set_index('sample_id');M=modified.set_index('sample_id');details=[];maxerr=0.;changed=0
 for sid in selected:
  assert sid in M.index,'Mutated fixture lost eligible origin '+sid
  b=B.loc[sid];m=M.loc[sid];err=max(abs(float(b[k])-float(m[k])) for k in inputs);delta=float(m.target)-float(b.target);maxerr=max(maxerr,err);changed+=abs(delta)>1e-12
  assert err<=1e-10,(sid,err)
  assert abs(delta)>1e-12,(sid,'target did not change')
  details.append(dict(sample_id=sid,group=str(b.group),partition=str(b.partition),max_input_change=err,target_change=delta))
 # selected includes one issuance per native recording/session/block; each changes its own future.
 return dict(scope=scope,origins=len(details),max_input_change=maxerr,targets_changed=changed,selected_origins=details,passed=True)

def case_signal(n):
 C=W/f'cases/P100-{n:03}';fname='native.py';native=load(C/fname,f'original_{n}');manifest=json.loads((C/'SOURCE_MANIFEST.json').read_text());original_hashes={a['path']:sha(D/a['path']) for a in manifest['assets']};base=native.prepare(D);task=json.loads((C/'package/task_spec.json').read_text());inputs=task['numeric_columns'];selection={};patch={};details=[]
 if n==7:
  for group,q in base.groupby('group'):
   chosen=q.sort_values('prediction_end_native_frame').iloc[len(q)//2];asset=next(a for a in manifest['assets'] if a['name']=='FP_S1_'+str(group)+'.csv');selection[asset['name']]=chosen
 elif n==9:
  for name,q in base.groupby(base.sample_id.str.split(':frame').str[0]):selection[name]=q.sort_values('prediction_time_seconds').iloc[len(q)//2]
 elif n==80:
  for name,q in base.groupby(base.sample_id.str.split(':t').str[0]):selection[name]=q.sort_values('prediction_elapsed_seconds').iloc[len(q)//2]
 elif n==99:
  for name,q in base.groupby(base.sample_id.str.rsplit(':endframe',n=1).str[0]):selection[name]=q.sort_values('prediction_end_frame').iloc[len(q)//2]
 paths={a['path'] for a in manifest['assets'] if n in [80,99] or a['name'] in selection}
 temp,A,E=fixture(C,manifest,paths)
 try:
  for asset in manifest['assets']:
   if asset['path'] not in paths:continue
   source=D/asset['path'];dest=E/asset['path']
   if n==7:
    chosen=selection[asset['name']];cut=int(chosen.prediction_end_native_frame);header=next(csv.reader([source.read_text().splitlines()[0]]));blob,count=csv_tail(source.read_bytes(),cut,[header.index('1:Fz'),header.index('2:Fz')],123.);dest.write_bytes(blob);details.append(dict(asset=asset['path'],first_mutated_zero_based_row=cut,changed_rows=count,mutation='Add123N to both force channels strictly after issuance; original prefix bytes unchanged.'))
   elif n==9:
    import h5py
    chosen=selection[asset['name']];cut=float(chosen.prediction_time_seconds);shutil.copy2(source,dest);counts={}
    with h5py.File(dest,'r+') as f:
     for path,amount in [('acquisition/PupilTracking/pupil_raw_radius',5.),('acquisition/treadmill_velocity',17.)]:
      t=f[path+'/timestamps'][:];q=f[path+'/data'];mask=np.isfinite(t)&(t>cut);v=q[:];good=mask&np.isfinite(v);v[good]+=amount;q[:]=v;counts[path]=int(good.sum())
    details.append(dict(asset=asset['path'],issuance_time=cut,changed=counts,mutation='Add5px radius and17cm/s velocity only at native timestamps strictly after issuance.'))
   elif n==80:
    with zipfile.ZipFile(source) as z:
     for name,chosen in selection.items():
      eda=next(k for k in z.namelist() if '/AEROBIC/' in k and k.endswith('/'+name+'/EDA.csv'));lines=z.read(eda).decode().splitlines();origin=pd.Timestamp(lines[0].split(',')[0]).timestamp()+float(chosen.prediction_elapsed_seconds)
      for channel,increment,columns in [('EDA.csv',1.,[0]),('TEMP.csv',7.,[0]),('ACC.csv',32.,[0,1,2])]:
       member=eda.rsplit('/',1)[0]+'/'+channel
       def change(blob,origin=origin,increment=increment,columns=columns):
        lines=blob.decode().splitlines();start=pd.Timestamp(lines[0].split(',')[0]).timestamp();fs=float(lines[1].split(',')[0]);cut=max(0,int(np.floor((origin-start)*fs+1e-7))+1);b,count=csv_tail(blob,cut,columns,increment,header_rows=2);return b,dict(first_mutated_zero_based_sample=cut,changed_rows=count,mutation='Add offset only after own-channel issuance boundary; header/rate/prefix bytes preserved.')
       patch[member]=change
    details=patch_zip(source,dest,patch)
   elif n==99:
    from scipy.io import loadmat,savemat
    for member,chosen in selection.items():
     cut=int(chosen.prediction_end_frame)
     def change(blob,cut=cut):
      v=loadmat(io.BytesIO(blob),struct_as_record=True,squeeze_me=False);trace=v['processed']['trace'][0,0];trace[:,cut:]+=0.001;out=io.BytesIO();savemat(out,{k:x for k,x in v.items() if not k.startswith('__')},do_compression=True,long_field_names=True);return out.getvalue(),dict(first_mutated_zero_based_frame=cut,changed_values=int(trace[:,cut:].size),mutation='Add0.001 author trace units to every component strictly after issuance; other MAT fields retained through lossless numeric MAT serialization.')
     patch[member]=change
    details=patch_zip(source,dest,patch)
   asset['bytes']=dest.stat().st_size;asset['sha256']=sha(dest)
  (A/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest));mod=load(A/'native.py',f'modified_{n}');modified=mod.prepare(E);result=compare(base,modified,[v.sample_id for v in selection.values()],inputs,'One middle eligible forecast origin from every native recording/session with at least one eligible origin; all currently exposed partitions covered.')
  for p,h in original_hashes.items():assert sha(D/p)==h,'Original source changed'
  result.update(case_id=f'P100-{n:03}',adapter=fname,adapter_sha256=sha(C/fname),source_manifest_sha256=sha(C/'SOURCE_MANIFEST.json'),task_sha256=sha(C/'package/task_spec.json'),native_rows_original=len(base),native_rows_mutated=len(modified),source_assets_without_eligible_origins=[a['name'] for a in manifest['assets'] if a['name'] not in selection] if n in [7,9] else [],mutations=details,original_assets_unchanged=True,fixture_source_hashes_recomputed=True,prediction_file_poisoning=False)
  return result
 finally:temp.cleanup()

def case88(mode):
 global BASE88
 C=W/'cases/P100-088';native=load(C/'native_current.py','original88_'+mode);manifest=json.loads((C/'SOURCE_MANIFEST.json').read_text());asset=manifest['assets'][0];source=D/asset['path'];original_hash=sha(source)
 with LOCK88:
  if BASE88 is None:BASE88=native.prepare(D)
  base=BASE88
 inputs=json.loads((C/'package/task_spec.json').read_text())['numeric_columns'];selection=[];cuts={}
 with zipfile.ZipFile(source) as z:
  member=next(n for n in z.namelist() if n.endswith('Nasioulas2024_data.csv'));table=pd.read_csv(io.BytesIO(z.read(member)))
 for (pid,block),q in table.groupby(['EXPID','BLOCK']):
  q=q.sort_values('TRIAL')
  if bool(q.iloc[0].BLOCK_INSTRUCTIONS==1):continue
  row=q.iloc[0 if mode=='first' else len(q)//2];cuts[(int(pid),int(block))]=float(row.TRIAL);selection.append(f'{int(pid)}:block{int(block)}:trial{int(row.TRIAL)}')
 def change(blob):
  a=pd.read_csv(io.BytesIO(blob));a['OUT']=a['OUT'].astype(float);a['CF_OUT']=a['CF_OUT'].astype(float)
  threshold=np.array([cuts.get((int(p),int(b)),np.inf) for p,b in zip(a.EXPID,a.BLOCK)]);mask=a.TRIAL.to_numpy()>=threshold
  a.loc[mask,'RISKY_CHOICE']=1-a.loc[mask,'RISKY_CHOICE'];a.loc[mask,'OUT']=-a.loc[mask,'OUT']+0.125;a.loc[mask,'CF_OUT']=-a.loc[mask,'CF_OUT']+0.25;a.loc[mask,'FEEDBACK']=1-a.loc[mask,'FEEDBACK'];a.loc[mask,'TYPE_FEEDBACK']=1-a.loc[mask,'TYPE_FEEDBACK'];altered=int(mask.sum())
  return a.to_csv(index=False).encode(),dict(changed_rows=altered,mutation='Flip current/future choice, feedback availability/type and alter current/future outcomes in unannounced blocks; prior trials and current lottery remain unchanged.')
 temp,A,E=fixture(C,manifest,{asset['path']})
 try:
  details=patch_zip(source,E/asset['path'],{member:change});asset['bytes']=(E/asset['path']).stat().st_size;asset['sha256']=sha(E/asset['path']);(A/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest));modified=load(A/'native.py','modified88_'+mode).prepare(E);result=compare(base,modified,selection,inputs,'Unannounced-feedback blocks: '+mode+' issuance, all participant blocks with metadata-designated unannounced instructions.');assert sha(source)==original_hash
  result.update(case_id='P100-088',test_variant=mode,adapter='native_current.py',adapter_sha256=sha(C/'native_current.py'),task_sha256=sha(C/'package/task_spec.json'),source_manifest_sha256=sha(C/'SOURCE_MANIFEST.json'),mutations=details,original_assets_unchanged=True,prediction_file_poisoning=False,fixture_source_hashes_recomputed=True,limited_to='Current known announced instruction metadata is legitimately available and is not mutated. Current/future outcome/choice fields and unannounced feedback types must not change issued inputs. No changes to prior visible history.')
  return result
 finally:temp.cleanup()

def main():
 args=argparse.ArgumentParser();args.add_argument('--cases',nargs='+',type=int,default=[7,9,80,99,88]);a=args.parse_args();jobs=[(f'case{n}',lambda n=n:case_signal(n)) for n in a.cases if n!=88]
 if 88 in a.cases:jobs += [(f'case88_{k}',lambda k=k:case88(k)) for k in ['first','middle']]
 results=[];failures=[];parts=W/'reviews/ASD7_NATIVE_PREFIX.parts';parts.mkdir(exist_ok=True)
 with ThreadPoolExecutor(max_workers=2) as pool:
  fs={pool.submit(fn):name for name,fn in jobs}
  for f in as_completed(fs):
   try:r=f.result()
   except Exception as e:failures.append(dict(test=fs[f],error=repr(e)));print(fs[f],repr(e),flush=True);continue
   r['implementation_sha256']=sha(__file__);results.append(r);(parts/(fs[f]+'.json')).write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(r['case_id'],r.get('test_variant',''),r['origins'],'origins PASS; max input change',r['max_input_change'],flush=True)
 result=dict(version='1.0',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/asd5_electronics',implementation=Path(__file__).name,implementation_sha256=sha(__file__),tests=sorted(results,key=lambda x:(x['case_id'],x.get('test_variant',''))),failures=failures,scope='Native source future-mutation invariance, not prediction-file target poisoning. Adapters run unchanged against disposable source fixtures with recomputed fixture integrity manifests. No fits, selection, outcomes or original assets/packages are modified.',limitations=['Tests are finite adversarial probes, not a formal proof for every possible input.','Only already-released native products are tested; publisher full-session filtering, denoising and normalization can have used future data.','Finite additive/choice mutations preserve timing, dimensions, existing missingness and source quality flags; missingness/eligibility changes are outside this probe.','No physiological or causal mechanism is established by prefix invariance.','For cases7/9/80/99 one midpoint origin per eligible native recording/session is tested; full temporal coverage is not claimed.'])
 (W/'reviews/ASD7_NATIVE_PREFIX.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
