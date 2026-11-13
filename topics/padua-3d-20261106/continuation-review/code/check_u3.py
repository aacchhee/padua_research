#!/usr/bin/env python3
"""Independent n7 half-shift nodes, modular ranks, and complete mesh rerun."""
import argparse, hashlib, itertools, json, os, platform, time
from pathlib import Path
import numpy as np
import scipy
from scipy import linalg
import sympy

TOP=Path(__file__).resolve().parents[2]
AA=np.array([(a,b,d-a-b) for d in range(8) for a in range(d+1) for b in range(d-a+1)])
PAIRS=((13,98),(13,142),(16,93),(16,147),(17,28),(17,212),(26,37),(26,203),
 (28,223),(37,214),(44,113),(44,127),(66,85),(66,155),(76,99),(76,141),
 (85,174),(93,224),(98,227),(99,164),(113,196),(127,196),(141,164),
 (142,227),(147,224),(155,174),(203,214),(212,223))
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def basis(x):
 t=[np.polynomial.chebyshev.chebvander(x[:,j],7) for j in range(3)]
 return t[0][:,AA[:,0]]*t[1][:,AA[:,1]]*t[2][:,AA[:,2]]
def rank(a,p):
 a=a.copy();r=0
 for j in range(a.shape[1]):
  candidates=np.flatnonzero(a[r:,j])
  if not len(candidates):continue
  k=r+int(candidates[0]);a[[r,k]]=a[[k,r]]
  a[r]=a[r]*pow(int(a[r,j]),-1,p)%p
  for i in range(r+1,len(a)):a[i]=(a[i]-a[i,j]*a[r])%p
  r+=1
  if r==len(a):break
 return r
def certificate(z):
 # Enumerate the full 240-element coset and fold integer numerators /480.
 residues=(np.arange(240)[:,None]*2+1)*np.array(z)[None,:]%480
 folded=np.unique(np.minimum(residues,480-residues),axis=0)
 assert len(folded)==120
 result=[];p=1000000
 for _ in range(2):
  p=((p-1)//480+1)*480+1
  while not sympy.isprime(p):p+=480
  w=pow(int(sympy.primitive_root(p)),(p-1)//480,p)
  assert pow(w,480,p)==1 and all(pow(w,480//q,p)!=1 for q in (2,3,5))
  coords=np.array([[(pow(w,int(v),p)+pow(w,int(-v%480),p))*pow(2,-1,p)%p for v in row] for row in folded],dtype=np.int64)
  t=[np.ones((120,8),dtype=np.int64) for _ in range(3)]
  for j in range(3):
   t[j][:,1]=coords[:,j]
   for k in range(2,8):t[j][:,k]=(2*coords[:,j]*t[j][:,k-1]-t[j][:,k-2])%p
  a=t[0][:,AA[:,0]]*t[1][:,AA[:,1]]%p*t[2][:,AA[:,2]]%p
  r=rank(a,p);assert r==120;result.append([p,w,r])
 return np.cos(np.pi*folded/240),result
def mesh(x):
 v=basis(x);inverse=linalg.solve(v,np.eye(120));s=linalg.svdvals(v)
 result={'condition2':float(s[0]/s[-1]),'residual':float(np.linalg.norm(v@inverse-np.eye(120),np.inf)),'values':[],'maximizers':[]}
 for q in (21,41):
  a=np.cos(np.pi*np.arange(q)/(q-1));best=(-1,None)
  # Chunk differently from producer; complete physical tensor grid.
  query=np.array(list(itertools.product(a,repeat=3)))
  for j in range(0,len(query),777):
   xx=query[j:j+777];vals=np.abs(basis(xx)@inverse).sum(axis=1);k=int(vals.argmax())
   if vals[k]>best[0]:best=(float(vals[k]),xx[k].tolist())
  result['values'].append(best[0]);result['maximizers'].append(best[1])
 return result
def controls():
 a=np.cos(np.pi*np.arange(15)/14);x=np.array(list(itertools.product(a,repeat=3)))
 piv=linalg.qr(basis(x).T,pivoting=True,mode='economic')[2]
 qr=x[piv[:120]]
 a=np.cos(np.pi*np.arange(8)/7);order=[0]
 while len(order)<8:
  left=[j for j in range(8) if j not in order]
  order.append(max(left,key=lambda j:(float(np.prod(abs(a[j]-a[order]))),-j)))
 leja=a[order][AA]
 return {'QR':mesh(qr),'Leja':mesh(leja)}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 t=time.process_time();producer=TOP/'evidence/u3c-nonunique-quality.json'
 original=json.loads(producer.read_text());source=identity(Path(__file__))
 assert [(r[0],r[1]) for r in original['rows']]==list(PAIRS)
 ctr=controls();rows=[];max_error=0
 for pair,saved in zip(PAIRS,original['rows']):
  nodes,checks=certificate((1,*pair));m=mesh(nodes)
  error=max(abs(x-y) for x,y in zip(m['values'],saved[4:6]));max_error=max(max_error,error)
  assert np.allclose(m['values'],saved[4:6],rtol=1e-10,atol=1e-9)
  q=max(x/y for x,y in zip(m['values'],ctr['QR']['values']))
  rows.append({'pair':pair,'rank_checks':checks,**m,'q':q});print(pair,q,flush=True)
 assert all(r['q']>1 for r in rows)==(original['result']['passes']==0)
 out={'scope':'independently implemented full28 count/two-prime rank and both complete meshes; control construction independently coded with same frozen ordering',
  'source':source,'input':identity(producer),'versions':[platform.python_version(),np.__version__,scipy.__version__,sympy.__version__],
  'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
  'controls':ctr,'rows':rows,'maximum_absolute_mesh_difference':max_error,'cpu_seconds':time.process_time()-t}
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<16384;a.output.write_text(payload)
if __name__=='__main__':main()
