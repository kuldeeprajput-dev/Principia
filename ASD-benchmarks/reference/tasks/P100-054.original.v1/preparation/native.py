from pathlib import Path
import io,json,hashlib,re,zipfile
import pandas as pd
import numpy as np

def canonical(s):return re.sub(r'-2$','',re.sub(r'^2_','',s))
def prepare(data_root):
 root=Path(data_root);manifest=json.loads((Path(__file__).parent.parent/'SOURCE_MANIFEST.json').read_text())
 for asset in manifest['assets']:
  p=root/asset['path']
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Native source hash mismatch: '+asset['path'])
 p=root/'54_materials_microfracture/raw/Data for publication.zip'
 if not p.exists():p=next(root.glob('54_*/raw/*.zip'))
 z=zipfile.ZipFile(p);member='Data for publication/Result analysis.xlsx';book=pd.read_excel(io.BytesIO(z.read(member)),sheet_name=None,header=None);out=[]
 for sheet,a in book.items():
  for i,row in a.iloc[2:].iterrows():
   if not isinstance(row.iloc[0],str) or not re.match(r'^(2_)?[CDE][0-9]',row.iloc[0]):continue
   sid=row.iloc[0].strip();vals=pd.to_numeric(row.iloc[[1,2,3,4,8,6]],errors='coerce').to_numpy(float)
   if not np.all(np.isfinite(vals)):continue
   B,W,L,notch,b,y=vals
   if min(B,W,L,notch,b)<=0 or notch>=W or b>=B:raise ValueError('Invalid geometry '+sid)
   g=canonical(sid);family=re.search('[CDE]',g).group();held=int(hashlib.sha256(('P100054-v1-'+g).encode()).hexdigest(),16)%5==0 and g not in {'C1','C11','C35','C36'}
   out.append(dict(sample_id=sid,group=g,partition='confirmation' if held else 'development',family=family,width_um=B,thickness_um=W,length_um=L,notch_depth_um=notch,notch_width_um=b,target=y,source_asset=str(p.relative_to(root)),source_anchor=member+'::'+sheet+f'!row{i+1}:B-E,I->G',eligibility='finite measured Pb2 and physical measured geometry; source toughness and fitted corrections excluded',linked_group=g))
 return pd.DataFrame(out)
