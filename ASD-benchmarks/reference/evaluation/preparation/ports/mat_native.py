import struct,zlib,numpy as np
DT={1:'i1',2:'u1',3:'<i2',4:'<u2',5:'<i4',6:'<u4',7:'<f4',9:'<f8',12:'<i8',13:'<u8',16:'u1',17:'<u2',18:'<u4'}
def tag(b,o):
 t,n=struct.unpack_from('<II',b,o)
 if t>>16:return t&65535,b[o+4:o+4+(t>>16)],o+8
 return t,b[o+8:o+8+n],o+8+(n+7)//8*8

def matrix(b):
 o=0;t,v,o=tag(b,o);flags=struct.unpack('<II',v);kind=flags[0]&255
 t,v,o=tag(b,o);dims=tuple(np.frombuffer(v,dtype='<i4'))
 t,v,o=tag(b,o);name=v.decode('utf-8',errors='replace')
 if kind==2:
  t,v,o=tag(b,o);l=struct.unpack('<I',v[:4])[0];t,v,o=tag(b,o);fields=[v[i:i+l].split(b'\0')[0].decode('utf-8')for i in range(0,len(v),l)];values=[]
  for _ in range(int(np.prod(dims))):
   d={}
   for f in fields:
    t,v,o=tag(b,o);assert t==14,(t,name,f);_,d[f]=matrix(v)
   values.append(d)
  return name,values[0]if len(values)==1 else values
 if kind==1:
  vals=[]
  for _ in range(int(np.prod(dims))):t,v,o=tag(b,o);assert t==14;vals.append(matrix(v)[1])
  return name,vals
 t,v,o=tag(b,o)
 if kind==4:
  # Octave strings may store UTF-8 bytes despite character-count dimensions.
  return name,v.decode('utf-8',errors='replace')if t in[1,2,16]else v.decode('utf-16le'if t in[3,4,17]else'utf-32le',errors='replace')
 if t in DT:
  a=np.frombuffer(v,dtype=DT[t]).copy();assert a.size==np.prod(dims),(name,t,dims,a.size)
  return name,a.reshape(dims,order='F')
 raise ValueError((name,kind,t,dims))
def load(p):
 b=p.read_bytes();assert b[126:128]==b'IM';o=128;result={}
 while o<len(b):
  t,v,o=tag(b,o)
  if t==15:t,v,_=tag(zlib.decompress(v),0)
  assert t==14;t,x=matrix(v);result[t]=x
 return result
if __name__=='__main__':
 from pathlib import Path
 import json
 def info(x,d=0):
  if isinstance(x,dict):return {k:info(v,d+1)for k,v in x.items()}
  if isinstance(x,list):return ['LIST',len(x),info(x[0],d+1)]if x else []
  if isinstance(x,np.ndarray):return dict(shape=x.shape,dtype=str(x.dtype),first=x.flat[:3].tolist())
  return x
 p=next(Path('../local-datas/60_acoustics_ultrasonic_transmission/raw').glob('*.mat'))
 print(json.dumps(info(load(p)),indent=2))
