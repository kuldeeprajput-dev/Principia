"""Transparent arithmetic/graph/polytope predictors. No observation lookup."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations,product
from functools import lru_cache
import json,math,hashlib,sys
import numpy as np,pandas as pd
from scipy.optimize import linprog
from scipy.spatial import ConvexHull
C=Path(__file__).resolve().parent

def read_table(p):return pd.read_csv(p,dtype={'sample_id':str,'group':str})
def rational_solve(A,b):
 rows=[[Fraction(v)for v in a]+[Fraction(v)]for a,v in zip(A,b)];n=len(rows[0])-1;r=0;cols=[]
 for c in range(n):
  q=next((i for i in range(r,len(rows))if rows[i][c]),None)
  if q is None:continue
  rows[r],rows[q]=rows[q],rows[r];v=rows[r][c];rows[r]=[x/v for x in rows[r]]
  for i in range(len(rows)):
   if i!=r and rows[i][c]:v=rows[i][c];rows[i]=[x-v*y for x,y in zip(rows[i],rows[r])]
  cols.append(c);r+=1
  if r==len(rows):break
 if any(not any(a[:-1])and a[-1]for a in rows):return None
 if len(cols)<n:return None
 out=[Fraction(0)]*n
 for i,c in enumerate(cols):out[c]=rows[i][-1]
 return out

def extend_poly(a,h,maxdegree=5):
 layers=[list(map(Fraction,a))]
 for deg in range(maxdegree+1):
  if len(set(layers[-1]))==1:
   for _ in range(h):
    layers[-1].append(layers[-1][-1])
    for k in range(len(layers)-2,-1,-1):layers[k].append(layers[k][-1]+layers[k+1][-1])
   return layers[0][-1]
  layers.append([y-x for x,y in zip(layers[-1],layers[-1][1:])])
 return None

def extend_rec(a,h,forcing=False):
 a=list(map(Fraction,a))
 for order in range(1,5):
  A=[[a[i-j-1]for j in range(order)]+([1,i]if forcing else[])for i in range(order,len(a))];b=a[order:];s=rational_solve(A,b)
  if s is None:continue
  for i in range(len(a),len(a)+h):a.append(sum(s[j]*a[i-j-1]for j in range(order))+(s[-2]+s[-1]*i if forcing else 0))
  return a[-1]
 return None

def extend_hyper(a,h):
 a=list(map(Fraction,a));A=[];b=[]
 # (c*n+1) a[n+1] = (u*n+v) a[n]
 for i in range(len(a)-1):A.append([i*a[i],a[i],-i*a[i+1]]);b.append(a[i+1])
 s=rational_solve(A,b)
 if s is None:return None
 for i in range(len(a)-1,len(a)+h-1):
  if s[2]*i+1==0:return None
  a.append((s[0]*i+s[1])*a[-1]/(s[2]*i+1))
 return a[-1]

def extend_quasi(a,h):
 for period in range(2,5):
  idx=len(a)+h-1;part=a[idx%period::period];remaining=(idx-(idx%period+period*(len(part)-1)))//period
  if all(extend_poly(a[k::period],1,2)is not None for k in range(period)):
   return extend_poly(part,remaining,2)
 return None

def seq_predict(kind,a,h):
 fallback=Fraction(a[-1]);funcs={'polynomial':lambda:extend_poly(a,h),'recurrence':lambda:extend_rec(a,h),'quasipolynomial':lambda:extend_quasi(a,h),'hypergeometric':lambda:extend_hyper(a,h),'forced_recurrence':lambda:extend_rec(a,h,True)}
 if kind=='linear':return Fraction(a[-1]+h*(a[-1]-a[-2]))
 if kind=='persist':return fallback
 if kind in funcs:v=funcs[kind]();return fallback if v is None else v
 if kind in['cascade','guarded_cascade']:
  for name in ['polynomial','recurrence','quasipolynomial','hypergeometric','forced_recurrence']:
   if kind=='guarded_cascade':
    try:test=seq_predict(name,a[:12],4)
    except (ZeroDivisionError,OverflowError):continue
    if test!=a[15]:continue
   v=funcs[name]()
   if v is not None:return v
  return fallback
 raise ValueError(kind)

def decode(g):
 vals=[ord(c)-63 for c in g.strip()];n=vals[0];bits=''.join(format(v,'06b')for v in vals[1:]);A=np.zeros((n,n),int);k=0
 for j in range(1,n):
  for i in range(j):A[i,j]=A[j,i]=int(bits[k]);k+=1
 return A

def graph_bound(kind,g):
 A=decode(g);n=len(A);edges=list(zip(*np.where(np.triu(A,1))))
 if kind=='vertices':return float(n)
 if kind=='caro_wei':return float(np.ceil(sum(1/(1+A.sum(1)))-1e-10))
 if kind=='inertia':
  e=np.linalg.eigvalsh(A);return float(n-min(sum(e>1e-7),sum(e< -1e-7)))
 if kind=='clique_cover':
  remain=set(range(n));count=0
  while remain:
   v=max(remain,key=lambda i:(sum(A[i,j]for j in remain),-i));clique=[v]
   for u in sorted(remain-{v},key=lambda i:(-A[i].sum(),i)):
    if all(A[u,j]for j in clique):clique.append(u)
   remain.difference_update(clique);count+=1
  return float(count)
 if kind=='greedy_lower':
  remain=set(range(n));count=0
  while remain:
   v=min(remain,key=lambda i:(sum(A[i,j]for j in remain),i));remain.difference_update({v}|{j for j in remain if A[v,j]});count+=1
  return float(count)
 if kind=='exact':
  # Independent combinatorial enumeration, not branch-and-bound native target reader.
  for size in range(n,0,-1):
   for sub in combinations(range(n),size):
    if all(not A[i,j]for i,j in combinations(sub,2)):return float(size)
  return 0.
 if kind in['edge_lp','triangle_lp','oddcycle_lp','interval_midpoint']:
  rows=[];rhs=[]
  for i,j in edges:q=np.zeros(n);q[[i,j]]=1;rows.append(q);rhs.append(1)
  if kind!='edge_lp':
   for tri in combinations(range(n),3):
    if all(A[i,j]for i,j in combinations(tri,2)):q=np.zeros(n);q[list(tri)]=1;rows.append(q);rhs.append(1)
  if kind in['oddcycle_lp','interval_midpoint']:
   for sub in combinations(range(n),5):
    H=A[np.ix_(sub,sub)]
    if np.all(H.sum(1)==2):q=np.zeros(n);q[list(sub)]=1;rows.append(q);rhs.append(2)
  opt=linprog(-np.ones(n),A_ub=np.array(rows),b_ub=rhs,bounds=(0,1),method='highs')
  if not opt.success:raise ValueError('LP failed')
  upper=float(np.floor(-opt.fun+1e-7))
  return (upper+graph_bound('greedy_lower',g))/2 if kind=='interval_midpoint'else upper
 raise ValueError(kind)

PAIRS=list(combinations(range(5),2))
def metric_matrix(s):
 a=[Fraction(v)for v in json.loads(s)];scale=math.lcm(*(v.denominator for v in a));a=[int(v*scale)for v in a];g=math.gcd(*a);a=[v//g for v in a];M=np.zeros((5,5),dtype=np.int64)
 for(i,j),v in zip(PAIRS,a):M[i,j]=M[j,i]=v
 return M

def metric_features(s):
 M=metric_matrix(s);ties=0;rows=[]
 for sub in combinations(range(5),4):
  a,b,c,d=sub;match=[[(a,b),(c,d)],[(a,c),(b,d)],[(a,d),(b,c)]];sums=[sum(M[i,j]for i,j in x)for x in match]
  for i,j in combinations(range(3),2):
   if sums[i]==sums[j]:
    ties+=1;q=np.zeros(10)
    for pair in match[i]:q[PAIRS.index(tuple(sorted(pair)))]+=1
    for pair in match[j]:q[PAIRS.index(tuple(sorted(pair)))]-=1
    rows.append(q)
 rank=int(np.linalg.matrix_rank(rows))if rows else 0
 return np.array([1.,ties,rank,ties*ties],float)

@lru_cache(None)
def trees():
 ans=[]
 # Prüfer encodings produce all625 labeled spanning trees.
 for seq in product(range(5),repeat=3):
  degree=[1]*5
  for v in seq:degree[v]+=1
  edges=[]
  for v in seq:
   u=next(i for i in range(5)if degree[i]==1);edges.append((u,v));degree[u]-=1;degree[v]-=1
  u,v=[i for i in range(5)if degree[i]==1];edges.append((u,v));ans.append(edges)
 return ans

def polar_facets(s,star=False):
 M=metric_matrix(s);vertices=set()
 iterable=[[(i,j)for j in range(5)if j!=i]for i in range(5)]if star else trees()
 for edges in iterable:
  for signs in product([-1,1],repeat=4):
   val={0:0}
   while len(val)<5:
    for(i,j),sign in zip(edges,signs):
     if i in val and j not in val:val[j]=val[i]+sign*int(M[i,j])
     elif j in val and i not in val:val[i]=val[j]-sign*int(M[i,j])
   if all(abs(val[i]-val[j])<=M[i,j]for i,j in PAIRS):vertices.add(tuple(val[i]for i in range(5)))
 return float(len(vertices))

def qhull_facets(s):
 M=metric_matrix(s);points=[]
 for i,j in PAIRS:
  p=np.zeros(5);p[i]=1/M[i,j];p[j]=-1/M[i,j];points.extend([p[:4],-p[:4]])
 h=ConvexHull(np.array(points));equations=np.round(h.equations,9);return float(len(np.unique(equations,axis=0)))

def predict(model,d):
 if isinstance(model,str):model=json.loads((C/'rules.json').read_text())['models'][model]
 case=model['case'];kind=model['kind'];out=[]
 if case==1:
  for a,h in zip(d.prefix_json,d.horizon):
   v=seq_predict(kind,json.loads(a),int(h));out.append(float(np.arcsinh(float(v))))
 elif case==5:out=[graph_bound(kind,str(g))for g in d.graph6]
 elif case==98:
  for s in d.metric_json:
   if kind=='generic':v=70.
   elif kind=='qhull':v=qhull_facets(s)
   elif kind=='polar':v=polar_facets(s)
   elif kind=='star':v=polar_facets(s,True)
   else:
    f=metric_features(s);ix=model['feature_indices'];v=float(f[ix]@np.asarray(model['coefficients']))
   out.append(v)
 else:raise ValueError('Unknowncase')
 y=np.asarray(out,float)
 if not np.isfinite(y).all():raise ValueError('Nonfinite arithmetic')
 return y

def main():
 mp=C/'MANIFEST.json'
 if not mp.is_file():raise ValueError('Required standalone integrity manifest is missing')
 m=json.loads(mp.read_text());assets=m.get('assets',m.get('files',[]));assets=[dict(path=k,sha256=v)for k,v in assets.items()]if isinstance(assets,dict)else assets
 if not assets:raise ValueError('Empty standalone integrity manifest')
 seen=set()
 for a in assets:
  name=a['path'];rel=Path(name)
  if rel.is_absolute()or '..'in rel.parts or name in seen:raise ValueError('Unsafe or duplicate manifest asset')
  seen.add(name);p=C/rel
  if not p.resolve().is_relative_to(C.resolve())or not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=a['sha256']:raise ValueError('Integrity failure '+name)
 rules=json.loads((C/'rules.json').read_text());x=read_table(C/'data/inputs.csv.gz');p=read_table(C/'evidence/predictions.csv.gz')
 for name,state in rules['models'].items():
  if not np.allclose(predict(state,x),p[name],rtol=1e-8,atol=1e-8):raise ValueError('Replaymismatch '+name)
 print('PASS',rules['case_id'],len(x),'rows',len(rules['models']),'models')
if __name__=='__main__':main()
