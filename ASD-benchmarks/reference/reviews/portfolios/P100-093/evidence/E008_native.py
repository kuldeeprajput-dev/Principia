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
 import flowio
 paths=sources(root);meta=pd.read_excel(paths['20230823 sample list.xlsx']);quantiles=np.arange(1,10)/10;rows=[];vals={}
 for n in meta.iloc[:,0]:
  h=flowio.FlowData(str(paths[n]));names={v['pnn']:int(k)-1 for k,v in h.channels.items()};a=np.asarray(h.events,float).reshape(h.event_count,h.channel_count);v=a[:,[names['FSC-A'],names['SSC-A'],names['B/E AF 488-A']]];v=v[np.isfinite(v).all(axis=1)&(v[:,0]>0)&(v[:,1]>0),2]
  if len(v)<100:raise ValueError('Insufficient FCS events')
  vals[n]=np.quantile(v,quantiles,method='linear')
 for row in meta.itertuples(index=False,name=None):
  n,line,condition=row
  if condition!='Dox':continue
  well=n.split('_')[2];letter=well[0];num=int(well[1:]);control=n.replace('_'+well+'_','_'+letter+str(num-1)+'_').replace('_'+letter+str(num).zfill(2)+'.fcs','_'+letter+str(num-1).zfill(2)+'.fcs');c=vals[control];y=vals[n];group={'A':'AD','D':'AD','B':'BE','E':'BE','C':'CF','F':'CF'}[letter]
  for i,q in enumerate(quantiles):rows.append(dict(sample_id=Path(n).stem+':q'+str(i+1),group=group,target=float(y[i]),control=float(c[i]),control_median=float(c[4]),control_width=float(c[8]-c[0]),quantile=float(q),wt=int(line=='SLC30A8'),mutant=int(line=='SLC30A8_D110N_D224N'),source_anchor=n+'::B/E AF488-A:minimal finite-positive-scatter gate:quantile'+str(q),calibration_anchor=control+'::same gate and channel quantiles',linked_unit=group,cell_line=line))
 if len(rows)!=81:raise ValueError('Expected9 induced wells*9quantiles')
 return finish(rows)
