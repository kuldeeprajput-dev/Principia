"""Build an explicitly non-scientific native-feature interface example."""
from pathlib import Path
import argparse,sys,shutil,subprocess,tempfile
E=Path(__file__).resolve().parents[1];sys.path.insert(0,str(E))
import common,raw_access
p=argparse.ArgumentParser();p.add_argument('--data-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();identifier='P100-037.original.v1.raw-access.v1'
raw_access.example(identifier,a.output);c,t,package,x,y,refs=raw_access.contract(identifier);shutil.copyfile(Path(__file__).with_name('native_router_features.py'),a.output/'extract.py')
with tempfile.TemporaryDirectory()as d:
 d=Path(d);common.save_json(d/'contract.json',c);x[['sample_id','group']].to_csv(d/'cohort.csv',index=False)
 subprocess.run([sys.executable,'-B',str(a.output/'extract.py'),'--data-root',str(a.data_root),'--contract',str(d/'contract.json'),'--cohort',str(d/'cohort.csv'),'--output',str(a.output/'derived_features.csv')],check=True)
lineage=common.load_json(a.output/'feature_lineage.json');lineage['extractor_interface']='native-v1';selectors=[]
for asset in c['source_assets']:
 if not asset['path'].endswith('.csv'):continue
 for quantity,column in [('throughput_Gbps','Throughput_Gbps'),('packet_bytes','PacketSize_B')]:selectors.append({'asset_sha256':asset['sha256'],'locator':asset['path']+'; column '+column+'; exact source line specified by each cohort sample_id','quantity':quantity,'role':'predictor','availability':'at_or_before_prediction'})
lineage['features']=[{'name':'log_packet_million','units':'dimensionless','expression':'log1p(Throughput_Gbps*1e9/(8*PacketSize_B)/1e6)','calibration_used':False,'selectors':selectors}];lineage['assets']=[common.asset_record(a.output/q,a.output)for q in ['derived_features.csv','extract.py','training.json']];common.save_json(a.output/'feature_lineage.json',lineage)
s=common.load_json(a.output/'submission.json');s['permitted_inputs']=['log_packet_million'];s['input_sha256']=common.digest(a.output/'derived_features.csv');common.save_json(a.output/'submission.json',s)
print('Created native-feature demonstration; constant predictions are not a scientific finding.')
