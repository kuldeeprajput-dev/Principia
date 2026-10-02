"""Native flask-only HPLC response adapter; contemporaneous diagnostic, not future prediction."""
from pathlib import Path
import hashlib,json,zipfile,io
import numpy as np
import pandas as pd
HERE=Path(__file__).resolve().parent
CASE='85_biotechnology_yarrowia_cofeeding'
CONDITIONS={'Flask_EG_OD0.1':(2,0,0,.1),'Flask_EG_OD0.5':(2,0,0,.5),'Growth_Flask_Ace+EG':(3,1,0,.1),'Growth_Flask_Glu+EG':(2,0,1,.1)}
def prepare(data_root):
 p=Path(data_root)/CASE
 for a in json.loads((HERE/'SOURCE_MANIFEST.json').read_text())['assets']:
  q=p/a['path']
  if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Native asset missing or checksum mismatch: '+a['path'])
 reserved=sorted(CONDITIONS,key=lambda x:hashlib.sha256(('p100-batch5-85-'+x).encode()).hexdigest())[0]; rows=[]
 with zipfile.ZipFile(p/'raw/DATA.zip') as z:
  for cond,(n,ace,glu,od) in CONDITIONS.items():
   member='DATA/'+cond+'.csv';d=pd.read_csv(io.BytesIO(z.read(member)),sep=';',encoding='latin1').apply(pd.to_numeric,errors='coerce')
   for r in range(1,n+1):
    eg='Ethylene Glycol (g/L) '+str(r); ga='Glycolic Acid (g/L) '+str(r); eg0=float(d.iloc[0][eg])
    for idx,a in d.iterrows():
     if not np.isfinite(a.iloc[0]) or a.iloc[0]<=0:continue
     if not all(np.isfinite(a[v]) for v in [eg,ga,'pH '+str(r)]):continue
     rows.append(dict(sample_id=cond+'-r'+str(r)+'-row'+str(idx+2),group=cond,target=float(a[ga]),partition='confirmation' if cond==reserved else 'development',elapsed_h=float(a.iloc[0]),eg_consumed_g_L=eg0-float(a[eg]),eg_initial_g_L=eg0,pH=float(a['pH '+str(r)]),acetate_cofeed=ace,glucose_cofeed=glu,replicate=str(r),source_anchor='raw/DATA.zip!'+member+':row='+str(idx+2)+':column='+ga,calibration_anchor='raw/DATA.zip!'+member+':row=2:column='+eg,eligibility_reason='finite measured nonzero-time flask sample; bioreactor regime ambiguous and excluded',fold=cond))
 return pd.DataFrame(rows)
