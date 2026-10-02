"""Source-native UTF16/UTF8 iPerf server summaries; no imputation or fitted transforms."""
from pathlib import Path
import hashlib,json,re,zipfile
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent

def prepare(data_root):
 s=list(Path(data_root).glob('91_*'))
 if len(s)!=1:raise ValueError('Expected unique scenario91 source')
 s=s[0];manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text());split=json.loads((HERE/'SPLITS.json').read_text())['groups']
 for a in manifest['assets']:
  f=s/a['path']
  if not f.is_file() or f.stat().st_size!=a['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Missing/truncated/checksum-mismatched source '+a['path'])
 rows=[]
 with zipfile.ZipFile(s/'raw/raw_latency_logs.zip') as z:
  for name in sorted(z.namelist()):
   if not name.endswith('.txt') or '/__MACOSX/' in name:continue
   f=Path(name).name
   m=re.fullmatch(r'k(\d)_latencyResult(\d)\.txt',f)
   if m:q,rep=map(int,m.groups());offered=1
   else:
    m=re.fullmatch(r'k(\d)_latency_(\d+)M_(\d)\.txt',f)
    if not m:raise ValueError('Unrecognized native filename '+name)
    q,offered,rep=map(int,m.groups())
   b=z.read(name)
   if b[:2] in (b'\xff\xfe',b'\xfe\xff'):text=b.decode('utf-16')
   else:
    try:text=b.decode('utf-8-sig')
    except UnicodeDecodeError:text=b.decode('cp1254') # Turkish Windows date labels; report fields are ASCII
   tail=text.split('Server Report:')
   if len(tail)!=2:raise ValueError('Missing/ambiguous server report '+name)
   line=next((x for x in tail[1].splitlines() if re.search(r'bits/sec',x)),None)
   bw=re.search(r'([\d.]+)\s*([GMK]?)bits/sec',line or '')
   lat=re.search(r'([-\d.]+)/([-\d.]+)/([-\d.]+)/([-\d.]+)\s*ms\s+[\d.]+\s*pps',line or '')
   if not bw or not lat:raise ValueError('Malformed server report '+name)
   achieved=float(bw[1])*{'G':1000,'M':1,'K':.001,'':1e-6}[bw[2]];delay,lo,hi,std=map(float,lat.groups());g=f'Q{q}'
   bad=(q==1 and offered==50 and rep in [3,4,5]);valid=np.isfinite(delay) and delay>=0 and delay<100000 and not bad
   rows.append(dict(sample_id=f'Q{q}:rate{offered}:rep{rep}',group=g,offered_Mbps=offered,achieved_Mbps=achieved,target=delay if valid else np.nan,partition=split[g],source_archive='raw/raw_latency_logs.zip',source_member=name,source_anchor=name+'#Server Report:Avg Latency(ms)',eligibility_reason='eligible' if valid else 'source-disclosed clock-wrap invalid one-way delay',repetition=rep))
 d=pd.DataFrame(rows).sort_values(['group','offered_Mbps','repetition']).reset_index(drop=True)
 if len(d)!=210 or d.sample_id.duplicated().any():raise ValueError('Expected210 unique native trials')
 return d
if __name__=='__main__':
 import sys
 d=prepare(Path(sys.argv[1]));print(d.groupby(['partition']).agg(rows=('sample_id','size'),eligible=('target','count')).to_json())
