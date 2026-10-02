import argparse,json
from pathlib import Path
import pandas as pd
from run import predict, read_table
p=argparse.ArgumentParser();p.add_argument('--inputs',required=True);p.add_argument('--output',required=True);a=p.parse_args()
x=read_table(a.inputs);model=json.loads((Path(__file__).parent/'submission_model.json').read_text())
y=predict(model,x);z=pd.DataFrame({'sample_id':x.sample_id,'prediction':y,'status':'predict','reason':''});z.to_csv(a.output,index=False)
