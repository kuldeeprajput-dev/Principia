"""Rebuild development attempts from native assets in a NEW disposable directory."""
from pathlib import Path
import argparse,shutil,subprocess,sys,json,importlib.util,numpy as np

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--data-root',required=True);ap.add_argument('--output-root',required=True);a=ap.parse_args();src=Path(__file__).resolve().parent;dest=Path(a.output_root)/src.name
 if dest.exists():raise ValueError('Output already exists; refusing to overwrite evidence')
 dest.mkdir(parents=True)
 for n in ['native.py','SOURCE_MANIFEST.json','SPLITS.json','PROTOCOL.json','run.py','develop.py']:shutil.copy2(src/n,dest/n)
 sp=importlib.util.spec_from_file_location('native_rebuild',dest/'native.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);d=m.prepare(Path(a.data_root));d[d.partition=='development'].to_csv(dest/'development.csv.gz',index=False)
 results=[]
 for baseline,folders in [(True,sorted(src.glob('baselines/*'))),(False,sorted(src.glob('attempts/attempt-*')))]:
  for f in folders:
   config=json.loads((f/'config.json').read_text());cmd=[sys.executable,str(dest/'develop.py'),'--kind',config['kind'],'--hypothesis',config['hypothesis']]+(['--baseline'] if baseline else[]);r=subprocess.run(cmd,text=True,capture_output=True,cwd=dest)
   if r.returncode:raise RuntimeError(r.stderr)
   new=dest/f.relative_to(src);oldmetric=json.loads((f/'metrics.json').read_text());newmetric=json.loads((new/'metrics.json').read_text());ok=bool(np.isclose(oldmetric['primary_error'],newmetric['primary_error'],rtol=1e-6,atol=1e-8));results.append({'case':src.name,'version':f.name,'metric_matches':ok,'original_MAE':oldmetric['primary_error'],'rebuilt_MAE':newmetric['primary_error']});print(json.dumps(results[-1]),flush=True)
   if not ok:raise ValueError('Scientific reproduction mismatch '+f.name)
 (dest/'REPLAY_RECEIPT.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
