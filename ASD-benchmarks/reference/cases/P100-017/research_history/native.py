from pathlib import Path
import json,hashlib,zipfile,io,gzip
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
def hashgroup(s):return int(hashlib.sha256(('principia100-batch7:'+str(s)).encode()).hexdigest()[:16],16)
def verify(data_root):
 m=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
 for a in m['assets']:
  f=Path(data_root)/a['path']
  if not f.is_file():raise ValueError('Missing native asset: '+a['path'])
  if hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native SHA256 mismatch: '+a['path'])
 return Path(data_root)/m['folder']
import xml.etree.ElementTree as ET
from scipy.spatial import cKDTree
def prepare(data_root):
 root=verify(data_root);f=root/'raw/usgs_2026-07_m2.5.quakeml';tree=ET.parse(f);ns={'b':'http://quakeml.org/xmlns/bed/1.2'};allrows=[]
 def val(node,path):
  a=node.find(path,ns)
  try:return float(a.text)
  except (AttributeError,TypeError,ValueError):return np.nan
 for e in tree.findall('.//b:event',ns):
  o=e.find('b:origin',ns)
  if o is None:continue
  q=o.find('b:quality',ns);t=pd.Timestamp(o.find('b:time/b:value',ns).text);lat=val(o,'b:latitude/b:value');lon=val(o,'b:longitude/b:value');sid=e.attrib['publicID'];allrows.append(dict(sample_id=sid,target=val(o,'b:depth/b:uncertainty')/1000,depth_km=val(o,'b:depth/b:value')/1000,rms_s=val(q,'b:standardError'),phases=val(q,'b:usedPhaseCount'),stations=val(q,'b:usedStationCount'),gap_deg=val(q,'b:azimuthalGap'),dmin_km=val(q,'b:minimumDistance')*111.195,lat=lat,lon=lon,time=t.timestamp(),source_anchor=f.name+':event@publicID='+sid+';origin.depth.uncertainty',input_anchor='same preferred origin quality/depth; minimumDistance degrees*111.195'))
 d=pd.DataFrame(allrows);parent=list(range(len(d)))
 def find(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 a=np.deg2rad(d.lat);b=np.deg2rad(d.lon);xyz=np.column_stack([np.cos(a)*np.cos(b),np.cos(a)*np.sin(b),np.sin(a)])*6371
 for i,j in cKDTree(xyz).query_pairs(100):
  if abs(d.iloc[i].time-d.iloc[j].time)<=7*86400:
   u,v=find(i),find(j);parent[max(u,v)]=min(u,v)
 clusters={}
 for i in range(len(d)):clusters.setdefault(find(i),[]).append(i)
 for inds in clusters.values():
  sid=min(d.iloc[inds].sample_id);d.loc[inds,'group']='cluster:'+sid
 groups=sorted(d.group.unique(),key=lambda s:hashgroup('quake:'+s));held=set(groups[:max(1,len(groups)//5)]);d['partition']=np.where(d.group.isin(held),'confirmation','development');d['fold_key']=d.group.map(lambda s:hashgroup('quakefold:'+s)%5)
 good=np.isfinite(d[['target','depth_km','rms_s','phases','stations','gap_deg','dmin_km']]).all(axis=1)&(d.target>0)&(d.rms_s>0)&(d.phases>0)&(d.stations>0)&d.gap_deg.between(0,360)&(d.dmin_km>=0)
 d=d[good].copy();d['eligibility_reason']='Positive supplied uncertainty/RMS/counts, finite declared geometry; reported zero/fixed uncertainties excluded from positive-scale task';return d
