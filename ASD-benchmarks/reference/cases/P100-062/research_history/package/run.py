"""Portable equation replay. No fitting, target lookup, network or historical state."""
from pathlib import Path
import ast,json,hashlib,argparse,math
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent
def slab(x):
 x=np.asarray(x,float);n=np.arange(1,41,dtype=float);return 1+2*np.sum(((-1.)**n)[:,None]*np.exp(-n[:,None]**2*np.maximum(x,.001)[None,:]),axis=0)
FUN={'erfc':np.vectorize(math.erfc),'slab':slab,'sqrt':np.sqrt,'exp':np.exp,'log':np.log,'log1p':np.log1p,'sin':np.sin,'cos':np.cos,'abs':np.abs,'maximum':np.maximum,'minimum':np.minimum,'clip':np.clip,'where':np.where,'tanh':np.tanh}
def read_table(path):return pd.read_csv(path,dtype={'sample_id':str,'group':str})
def calc(expression,d,pars):
 tree=ast.parse(expression,mode='eval')
 allowed=(ast.Expression,ast.BinOp,ast.UnaryOp,ast.Call,ast.Name,ast.Load,ast.Constant,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.USub,ast.UAdd,ast.Compare,ast.Gt,ast.GtE,ast.Lt,ast.LtE,ast.Eq)
 for n in ast.walk(tree):
  if not isinstance(n,allowed):raise ValueError('Unsafe equation syntax')
  if isinstance(n,ast.Call) and (not isinstance(n.func,ast.Name) or n.func.id not in FUN):raise ValueError('Unsupported equation function')
 env={k:d[k].to_numpy(float) for k in d.columns if k not in ['target'] and pd.api.types.is_numeric_dtype(d[k])};env.update(FUN);env.update(pars)
 a=np.asarray(eval(compile(tree,'<frozen scientific equation>','eval'),{'__builtins__':{}},env),float)
 return np.full(len(d),a) if a.ndim==0 else a

def predict(model,d):
 if isinstance(model,str):model=json.loads((ROOT/'rules.json').read_text())['models'][model]
 if 'target' in model.get('inputs',[]):raise ValueError('Target is not a predictor')
 for k in model.get('inputs',[]):
  if k not in d or not np.isfinite(pd.to_numeric(d[k],errors='coerce')).all():raise ValueError('Missing/nonfinite input '+k)
 out=calc(model['formula'],d,model.get('parameters',{}))
 if len(out)!=len(d) or not np.isfinite(out).all():raise ValueError('Nonfinite equation result')
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--inputs');ap.add_argument('--output');ap.add_argument('--model',default='reference');a=ap.parse_args()
 manifest=json.loads((ROOT/'MANIFEST.json').read_text());items=manifest.get('files',manifest)
 if isinstance(items,list):items={r['path']:r['sha256'] for r in items}
 for rel,sha in items.items():
  if isinstance(sha,dict):sha=sha['sha256']
  p=ROOT/rel
  if '..' in Path(rel).parts or Path(rel).is_absolute() or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:raise ValueError('Integrity failure: '+rel)
 d=read_table(a.inputs or ROOT/'data/inputs.csv.gz');rules=json.loads((ROOT/'rules.json').read_text());out=d[['sample_id','group']].copy()
 if a.inputs:
  out['prediction']=predict(a.model,d)
  if not a.output:raise ValueError('--output required for custom input')
  out.to_csv(a.output,index=False);return
 saved=read_table(ROOT/'evidence/predictions.csv.gz')
 if not d.sample_id.equals(saved.sample_id):raise ValueError('Identity mismatch')
 for k,m in rules['models'].items():
  out[k]=predict(m,d)
  if not np.allclose(out[k],saved[k],rtol=1e-9,atol=1e-9):raise ValueError('Replay mismatch '+k)
 print(json.dumps({'status':'passed','models':len(rules['models']),'rows':len(d)}))
if __name__=='__main__':main()
