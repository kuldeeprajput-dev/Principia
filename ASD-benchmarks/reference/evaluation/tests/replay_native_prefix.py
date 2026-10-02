"""Replay the preserved ASD7 native-prefix probes from a portable benchmark tree."""
from pathlib import Path
import argparse,importlib.util,shutil,sys,tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import common as c

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--cases',type=int,nargs='+',choices=[7,9,80,88,99],default=[7,9,80,88,99])
    args=parser.parse_args();out=c.new_output(args.output)
    c.verify_assets(c.ROOT,c.load_json(c.ROOT/'EVALUATOR_MANIFEST.json')['files'])
    receipt_path=c.ROOT/'reviews/validation/ASD7_NATIVE_PREFIX.json'
    receipt=c.load_json(receipt_path);script=c.ROOT/'reviews/validation/asd7_native_prefix.py'
    if c.digest(script)!=receipt['implementation_sha256']:raise ValueError('Native-prefix implementation checksum mismatch')
    for n in args.cases:
        task,_,_,_,_=c.context(f'P100-{n:03}.original.v1')
        if c.digest(receipt_path)!=task['native_prefix_audit']['receipt_sha256']:raise ValueError('Unbound native-prefix evidence')
    with tempfile.TemporaryDirectory(prefix='principia-prefix-replay-')as temp:
        root=Path(temp);(root/'reviews').mkdir()
        for n in args.cases:
            cid=f'P100-{n:03}';dest=root/'cases'/cid;dest.mkdir(parents=True)
            native=c.ROOT/'evaluation/preparation/new_cases'/cid
            for name in ['SOURCE_MANIFEST.json','SPLITS.json']:shutil.copyfile(native/name,dest/name)
            shutil.copyfile(native/'native.py',dest/('native_current.py'if n==88 else'native.py'))
            (dest/'package').mkdir();shutil.copyfile(c.ROOT/'tasks'/f'{cid}.original.v1/task_spec.json',dest/'package/task_spec.json')
        spec=importlib.util.spec_from_file_location('archived_native_probe',script)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.W=root;module.D=args.data_root.resolve()
        old=sys.argv;sys.argv=[str(script),'--cases']+list(map(str,args.cases))
        try:module.main()
        finally:sys.argv=old
        result=c.load_json(root/'reviews/ASD7_NATIVE_PREFIX.json')
        result['reviewer']='Local replay of archived independent audit procedure'
        result['portable_launcher_sha256']=c.digest(Path(__file__))
        out.mkdir(parents=True);c.save_json(out/'report.json',result)
        if result['failures']:raise ValueError('Native-prefix replay failed; see output report')
        print('Native-prefix replay passed',len(result['tests']),'variants')

if __name__=='__main__':main()
