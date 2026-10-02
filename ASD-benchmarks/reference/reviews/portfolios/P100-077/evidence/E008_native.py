from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def sources(root):
 p={}
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  f=Path(root)/a['path']
  if not f.is_file() or f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native asset missing or mismatched: '+a['path'])
  p[a['name']]=f
 return p
def finish(rows):
 d=pd.DataFrame(rows);s=json.loads((HERE/'SPLITS.json').read_text());d['partition']=d.group.map(s['partition']);d['fold']=d.group.map(s['fold'])
 if d.sample_id.duplicated().any() or d.partition.isna().any() or not np.isfinite(d.target).all():raise ValueError('Invalid native row identity, grouping or target')
 return d
def prepare(root):
 import zipfile,io,re,flowio
 p=sources(root);f=next(iter(p.values()));z=zipfile.ZipFile(f);members=sorted(n for n in z.namelist() if '/FIG 6H/' in n and n.endswith('.fcs'))
 def values(n):
  h=flowio.FlowData(io.BytesIO(z.read(n)));a=np.asarray(h.events,float).reshape(h.event_count,h.channel_count);names={v['pns']:int(k)-1 for k,v in h.channels.items()};cols=[names['FSC-A'],names['SSC-A'],names['GFP 525.40(488nm)-A'],names['mCherry 610.20(561nm)-A']];v=a[:,cols];v=v[np.isfinite(v).all(axis=1)&(v[:,0]>0)&(v[:,1]>0)]
  if len(v)<100:raise ValueError('Insufficient valid events')
  return v[:,2:]
 cn=next(n for n in members if 'BOB control' in n);cv=values(cn);threshold=np.quantile(cv,.995,axis=0);rows=[]
 for n in members:
  if n==cn:continue
  m=re.search(r'/(\d+)-fold_.*_([ABC])\.fcs$',n)
  if m is None:raise ValueError('Unknown Fig6H experiment name '+n)
  v=values(n);g=v[:,0]>threshold[0];r=v[:,1]>threshold[1];rows.append(dict(sample_id=Path(n).stem,group=m.group(2),target=float(100*np.mean(g&r)),green=float(g.mean()),red=float(r.mean()),dose=float(m.group(1)),source_anchor=f.name+'::'+n+':all valid scatter events; GFP-A and mCherry-A jointly above control thresholds',calibration_anchor=f.name+'::'+cn+':channel99.5percentiles',linked_unit='replicate:'+m.group(2),events=len(v),threshold_green=float(threshold[0]),threshold_red=float(threshold[1])))
 if len(rows)!=9:raise ValueError('Expected all nine dose/replicate wells')
 return finish(rows)
