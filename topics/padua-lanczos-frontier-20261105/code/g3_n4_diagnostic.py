#!/usr/bin/env python3
"""One U1/q2 n4 proposer scaling diagnostic; original exact acceptance."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import hashlib,json,math,pathlib,resource,signal,sys,time
from fractions import Fraction as F
import g3_n4_producer as p

PIN='15b1e8803bd74d3b7da7f134c1bdbc46cc5abde54183ba93be4e779913e00fcb'
def main():
 start=time.monotonic();out=pathlib.Path('/tmp/padua-lanczos-frontier-g3-n4-diagnostic');out.mkdir(parents=True,exist_ok=False)
 receipt={'status':'RUNNING','scope':'n4 U1 q2 only; proposer conditioning diagnostic; no mathematical infeasibility claim','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(pathlib.Path(p.__file__).read_bytes()).hexdigest(),'command':[sys.executable,*sys.argv]}
 resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
 def expired(*_):raise TimeoutError('28s internal cap')
 signal.signal(signal.SIGALRM,expired);signal.alarm(28)
 try:
  assert receipt['producer_sha256']==PIN
  p.DEADLINE=p.GLOBAL_DEADLINE=start+28
  p.node_identities()
  J=[p.values(x,y,dx,dy) for _,_,x,y in p.NODES for dx,dy in [(0,0),(1,0),(0,1)]]
  B,piv=p.kernel(J);d=len(B)
  assert all(not p.dot(row,col) for row in J for col in B)
  assert len(p.rref(B)[1])==d==55-len(piv)
  receipt['kernel']={'rank_J':len(piv),'dimension':d,'elapsed_seconds':time.monotonic()-start}
  q=2;U=F(1);rows=[];pts=[];seen=set()
  offsets=[(a,b)for a in range(-q,q+1)for b in range(-q,q+1)if 0<a*a+b*b<=q*q]
  for node,(_,_,x,y)in enumerate(p.NODES):
   for a,b in offsets:
    p.checkcap();xx=x+F(a,q);yy=y+F(b,q);key=tuple(xx.data()+yy.data())
    if key in seen:continue
    seen.add(key);v=p.values(xx,yy);ev=[p.dot(v,c)for c in B]
    if any(ev):rows.append(ev);pts.append([node,str(F(a,q)),str(F(b,q))])
  basis=p.independent_rows(rows);assert len(basis)==d
  import numpy as np
  from scipy.optimize import linprog
  A=np.asarray([[float(x)for x in r]for r in rows]).T
  norm=np.max(np.abs(A),axis=1);assert np.all(norm>0)
  A=A/norm[:,None];pointnorm=np.max(np.abs(A),axis=0);assert np.all(pointnorm>0)
  exponents=[1-math.frexp(float(x))[1]for x in pointnorm]
  exactscales=[F(2)**k for k in exponents];scales=np.asarray([float(x)for x in exactscales])
  scaled=A*scales[None,:]
  receipt['matrix']={'points':len(rows),'kernel_coordinate_maxima':norm.tolist(),'normalized_point_max_norm_range':[float(min(pointnorm)),float(max(pointnorm))],'coordinate_normalized_singular_values':np.linalg.svd(A,compute_uv=False).tolist(),'point_scaled_singular_values':np.linalg.svd(scaled,compute_uv=False).tolist(),'exact_point_scale_exponents_base2':exponents,'conversion':'A_scaled[:,i]=2^e_i*A[:,i]; lambda_original_i=2^e_i*lambda_scaled_i; same positive coordinate normalization'}
  receipt['proposals']=[]
  for name,matrix,conversion in [('original',A,np.ones(len(rows))),('point_rescaled',scaled,scales)]:
   p.checkcap();t=time.monotonic()
   lp=linprog(np.ones(len(rows)),A_eq=matrix,b_eq=np.zeros(d),bounds=[(1,None)if i in basis else(0,None)for i in range(len(rows))],method='highs',options={'time_limit':5.0})
   rec={'name':name,'lp_status':int(lp.status),'lp_message':str(lp.message),'status':'INCONCLUSIVE','elapsed_seconds':time.monotonic()-t};receipt['proposals'].append(rec)
   if lp.success:
    exact=p.reconstruct(rows,lp.x*conversion,basis)
    if exact:
     support,lamb=exact
     assert len(p.independent_rows([rows[i]for i in support]))==d
     assert all(F(pts[i][1])**2+F(pts[i][2])**2<=1 for i in support)
     assert all(x.sign()>0 for x in lamb)
     assert all(not sum((lamb[t]*rows[i][c]for t,i in enumerate(support)),p.Q())for c in range(d))
     cert={'U':'1','q':2,'points':[pts[i]for i in support],'weights':[v.data()for v in lamb]}
     raw=json.dumps(cert,indent=2)+'\n';assert len(raw.encode())<16384
     (out/(name+'-upper.json')).write_text(raw);rec['status']='EXACT ACCEPTED producer candidate; independent check PENDING'
  receipt['status']='COMPLETED bounded diagnostic'
 except Exception as e:receipt.update(status='INCONCLUSIVE_OR_CAP',error=repr(e))
 finally:
  signal.alarm(0);receipt['elapsed_seconds']=time.monotonic()-start;receipt['peak_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
