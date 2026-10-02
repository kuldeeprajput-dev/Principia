"""Native router feature demonstration; no power measurements are used."""
import argparse,json
from pathlib import Path
import pandas as pd,numpy as np
p=argparse.ArgumentParser();p.add_argument('--data-root',required=True);p.add_argument('--contract',required=True);p.add_argument('--cohort',required=True);p.add_argument('--output',required=True);a=p.parse_args()
c=json.loads(Path(a.contract).read_text());cohort=pd.read_csv(a.cohort,dtype=str);root=Path(a.data_root)/c['source_folder'];frames={};rows=[]
for identity in cohort.sample_id:
 name,line=identity.rsplit(':',1)
 if name not in frames:frames[name]=pd.read_csv(root/'raw'/name,sep=';',usecols=['Throughput_Gbps','PacketSize_B'])
 r=frames[name].iloc[int(line)-2];packet_rate=float(r.Throughput_Gbps)*1e9/(8*float(r.PacketSize_B))
 rows.append({'sample_id':identity,'log_packet_million':float(np.log1p(packet_rate/1e6))})
pd.DataFrame(rows).to_csv(a.output,index=False)
