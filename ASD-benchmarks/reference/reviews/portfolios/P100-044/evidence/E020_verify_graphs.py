from pathlib import Path
import argparse,json,csv,hashlib
import pandas as pd
D=None
def graphs(c):
 rows=[];src=D/'44_mathematics_qoblib_topology/raw/10-topology'
 for p in sorted((src/'submissions').glob('*/*/*.gph')):
  n,degree=map(int,(src/'instances'/(p.parent.name+'.dat')).read_text().split());adj={i:set()for i in range(1,n+1)};edges=[]
  for line in p.read_text().splitlines():
   a=line.split()
   if a and a[0]=='e':u,v=map(int,a[1:]);adj[u].add(v);adj[v].add(u);edges.append((min(u,v),max(u,v)))
  diam=0
  for u in adj:
   dist={u:0};queue=[u]
   for v in queue:
    for z in adj[v]:
     if z not in dist:dist[z]=dist[v]+1;queue.append(z)
   if len(dist)!=n:raise ValueError('Disconnected source graph')
   diam=max(diam,max(dist.values()))
  r=next(csv.DictReader((p.parent/(p.parent.name+'_summary.csv')).open()));obj=float(r['Best Objective Value']);actual_degree=max(map(len,adj.values()));lower=1
  while 1+degree*sum((degree-1)**i for i in range(lower))<n:lower+=1
  assert diam<=obj and actual_degree<=degree and len(edges)==len(set(edges))
  rows.append({'native_anchor':str(p.relative_to(D)),'group':p.parent.name,'diameter':diam,'reported_MIP_objective':obj,'objective_tight':diam==obj,'max_degree':actual_degree,'degree_limit':degree,'classical_Moore_lower_bound':lower,'optimality_certified_by_counting':diam==lower})
 pd.DataFrame(rows).to_csv(c/'graph_certificates.csv',index=False);return {'graphs_verified':len(rows),'objective_mismatches':sum(not r['objective_tight']for r in rows),'classical_counting_certificates':sum(r['optimality_certified_by_counting']for r in rows),'missing_solution_files':1,'no_new_graph_bound_claimed':True}

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--data-root',type=Path,required=True);a.add_argument('--output',type=Path,required=True);args=a.parse_args();D=args.data_root
 for asset in json.loads((Path(__file__).parent/'graph_source_manifest.json').read_text())['assets']:
  p=D/asset['path']
  if not p.is_file()or p.stat().st_size!=asset['bytes']or hashlib.sha256(p.read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Missing or corrupt source: '+asset['path'])
 if args.output.exists():raise ValueError('Use a new output directory')
 args.output.mkdir(parents=True);result=graphs(args.output);(args.output/'receipt.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
