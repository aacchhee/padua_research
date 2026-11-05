"""Actual high-n G4 attribution controls; external arrays, no suite or verdict."""
import argparse,contextlib,hashlib,io,json,os,pathlib,platform,subprocess,sys,time
import numpy as np
import scipy
from scipy.linalg import qr,svdvals
ROOT=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tracks/bivariate-lanczos/code/drift'))
import e6_benchmark as e6
LD=np.longdouble

def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def norm(A):return float(svdvals(np.asarray(A,float))[0])
def cgs(V):
 Q=np.zeros(V.shape,dtype=LD)
 for k in range(V.shape[1]):
  q=V[:,k].astype(LD).copy()
  for _ in range(2):q-=Q[:,:k]@(Q[:,:k].T@q)
  Q[:,k]=q/np.sqrt(q@q)
 return Q

def jac(k,a,x):
 p=np.ones_like(x)
 if not k:return p
 q=(a+(a+2)*x)/2
 for j in range(1,k):
  h=LD(2*j+a)
  r=((h+1)*(h*(h+2)*x+a*a)*q-2*(j+a)*j*(h+2)*p)/(2*(j+1)*(j+a+1)*h)
  p,q=q,r
 return q

def independent_reference(P,n,name):
 x,y=P.astype(LD).T
 if name=='rotpi4':
  # Any nonsingular linear frame spans the same total-degree space. Retain
  # the historical binary64 trigonometric constants, promoted before products.
  co=LD(np.cos(np.pi/4));si=LD(np.sin(np.pi/4));x,y=co*x+si*y,-si*x+co*y
  def cheb(z):
   z=(z-(z.max()+z.min())/2)/((z.max()-z.min())/2);v=[np.ones_like(z),z]
   for k in range(2,n+1):v.append(2*z*v[-1]-v[-2])
   return v
  a,b=cheb(x),cheb(y);V=np.column_stack([a[t-j]*b[j] for t in range(n+1) for j in range(t+1)])
 else:
  xi=(x+1)/2;et=(y+1)/2;om=1-et;arg=(2*xi-om)/om
  V=np.column_stack([jac(t-j,0,arg)*om**(t-j)*jac(j,2*(t-j)+1,2*et-1) for t in range(n+1) for j in range(t+1)])
 V/=np.sqrt(np.sum(V*V,axis=0));return cgs(V)

def normal(A,U):return A-U@(U.T@A)
def propagate(P,Q,H,idx,up,U,parents=None):
 Q=Q.astype(LD);H=H.astype(LD);F=np.zeros_like(Q);E=np.zeros_like(Q);ops=[]
 for k in range(1,Q.shape[1]):
  axis,p=up._update_rule(idx,idx[k]) if parents is None else parents[k];beta=H[k,k];a=P[:,axis]*Q[:,p];b=Q[:,:k]@H[:k,k];c=beta*Q[:,k]
  F[:,k]=a-b-c
  E[:,k]=(P[:,axis]*E[:,p]-E[:,:k]@H[:k,k]-F[:,k])/beta
  ops.append(float(np.sqrt(a@a)+np.sqrt(b@b)+np.sqrt(c@c)))
 local=np.sqrt(np.sum(F[:,1:]*F[:,1:],axis=0));NQ=normal(Q,U);NE=normal(E,U);W=cgs(Q)
 return {'actual_gap_against_ld_reference':norm(normal(W,U)),'raw_normal_Q_norm':norm(NQ),'propagated_normal_norm':norm(NE),'normal_reconstruction_discrepancy':norm(NQ-NE),'max_local_residual_norm':float(max(local)),'local_residual_fro':float(np.sqrt(np.sum(F*F))),'max_local_residual_over_u':float(max(local)/LD(2)**-53),'max_local_residual_over_u_operation_norm_sum':float(max(local/(LD(2)**-53*np.array(ops,LD)))),'local_operation_norm_sum_max':max(ops),'normalized_source_fro':float(np.sqrt(np.sum((F[:,1:]/np.diag(H)[1:])**2))),'normal_amplification_over_residual_fro':norm(NE)/float(np.sqrt(np.sum(F*F))),'q0_constant':bool(np.all(Q[:,0]==Q[0,0]))}

def worker(a):
 up=e6.load_upstream(a.external);frozen=np.load(a.input);P,w,n=frozen['P'],frozen['w'],int(frozen['n']);dtype=LD if a.precision=='extended' else float
 Q,H,idx=up.vandermonde_arnoldi_CGS(P[:,[1,0]].astype(dtype),n,weight=np.sqrt(w).astype(dtype));np.savez(a.worker,Q=Q,H=H,idx=idx,P=P,w=w)
 from threadpoolctl import threadpool_info
 libs=threadpool_info()
 for z in libs:z['sha256']=sha(z['filepath'])
 write(pathlib.Path(str(a.worker)+'.runtime.json'),{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'OPENBLAS_CORETYPE':os.getenv('OPENBLAS_CORETYPE'),'libraries':libs})

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--external',required=True);ap.add_argument('--output-dir',type=pathlib.Path);ap.add_argument('--receipt',type=pathlib.Path);ap.add_argument('--worker',type=pathlib.Path);ap.add_argument('--name');ap.add_argument('--precision');ap.add_argument('--input',type=pathlib.Path);ap.add_argument('--resume',action='store_true');a=ap.parse_args()
 from g4_replay import PINS
 assert {k:sha(pathlib.Path(a.external)/'polyrat'/k) for k in PINS}==PINS
 if a.worker:return worker(a)
 assert os.getenv('OPENBLAS_NUM_THREADS')=='1';d=a.output_dir;d.mkdir(parents=True,exist_ok=a.resume);started=time.time();commands=[];rows=[];up=e6.load_upstream(a.external)
 for name in ['rotpi4','triangle']:
  P,w,n=e6.L2.benchmark(name);frozen=d/(name+'-input.npz');np.savez(frozen,P=P,w=w,n=n);U=independent_reference(P,n,name);Ud=e6.reference(P,w,n,name,P[:128])[0];refnoise=norm(normal(Ud.astype(LD),U));controls=[];Qs=[]
  for core,prec in [('Haswell','double'),('Nehalem','double'),('Haswell','extended')]:
   dest=d/(name+'-'+core+'-'+prec+'.npz');cmd=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),'--external',a.external,'--worker',str(dest),'--name',name,'--precision',prec,'--input',str(frozen)];env=dict(os.environ,OPENBLAS_CORETYPE=core,OPENBLAS_NUM_THREADS='1');t=time.time();reuse=False
   if dest.exists():
    saved=np.load(dest);reuse=np.array_equal(saved['P'],P) and np.array_equal(saved['w'],w)
    if not reuse:
     dest.rename(dest.with_name(dest.stem+'-REJECTED-INPUT.npz'));pathlib.Path(str(dest)+'.runtime.json').rename(pathlib.Path(str(dest)+'.REJECTED-INPUT.runtime.json'))
   if not reuse:subprocess.run(cmd,env=env,check=True,timeout=1800)
   commands.append({'argv':cmd,'core':core,'precision':prec,'elapsed_seconds':None if reuse else time.time()-t,'reused_valid_preexisting_QH':reuse})
   z=np.load(dest);Q,H,idx=z['Q'],z['H'],z['idx'];assert np.array_equal(z['P'],P) and np.array_equal(z['w'],w);t=time.time();val=propagate(P[:,[1,0]].astype(LD),Q,H,idx,up,U);val.update(core=core,precision=prec,diagnostic_seconds=time.time()-t,orth_max=float(np.max(abs(Q.T@Q-np.eye(Q.shape[1])))),raw={'path':str(dest),'sha256':sha(dest),'bytes':dest.stat().st_size},runtime=json.loads(pathlib.Path(str(dest)+'.runtime.json').read_text()));controls.append(val);Qs.append(Q.astype(LD));print(name,core,prec,val['raw_normal_Q_norm'],val['normal_reconstruction_discrepancy'],flush=True)
  delta=norm(normal(Qs[0]-Qs[1],U));rows.append({'name':name,'n':n,'input_sha256':hashlib.sha256(P.tobytes()+w.tobytes()).hexdigest(),'reference_double_vs_ld_projector_gap':refnoise,'reference_ld_gram_norm':norm(U.T@U-np.eye(U.shape[1],dtype=LD)),'kernel_normal_Q_difference':delta,'controls':controls})
  result={'status':'MEASURED_DIAGNOSTICS_REVIEW_PENDING','code_sha256':sha(__file__),'commands':commands,'cases':rows,'elapsed_seconds':time.time()-started,'longdouble_nmant':np.finfo(LD).nmant,'limitations':'Historical Q/H and dispatch absent; no historical trajectory reconstruction or kernel enclosure claim.'};write(a.receipt,result)
if __name__=='__main__':main()
