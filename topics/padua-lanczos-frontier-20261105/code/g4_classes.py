"""Remaining four G4 arithmetic classes, fixed inputs; no suite or verdict."""
import argparse,json,os,pathlib,subprocess,sys,time,hashlib
import numpy as np
from g4_attribution import e6,LD,sha,write,independent_reference,propagate,norm,normal

def worker(a):
 frozen=np.load(a.input);P,w,n=frozen['P'],frozen['w'],int(frozen['n']);dtype=LD if a.precision=='extended' else float;up=e6.load_upstream(a.external)
 if a.method=='upstream_xy':
  Q,H,idx=up.vandermonde_arnoldi_CGS(P.astype(dtype),n,weight=np.sqrt(w).astype(dtype));parents=np.array([[-1,-1]]+[list(up._update_rule(idx,idx[k])) for k in range(1,len(idx))]);path_equal=None
 else:
  Q,info,_=e6.L2.run_sel(P[:,0],P[:,1],w,n,sel=a.method,reorth='fullcgs2',dtype=dtype);N=Q.shape[1];H=np.zeros((N,N),dtype=dtype);H[0,0]=np.sqrt(np.sum(w.astype(dtype)));parents=np.array([[-1,-1]]+[[0 if op=='X' else 1,p] for op,p in info[1:]]);idx=np.arange(N)
  for k in range(1,N):
   axis,p=parents[k];raw=P[:,axis].astype(dtype)*Q[:,p];Qk=Q[:,:k];h1=Qk.T@raw;r=raw-Qk@h1;h2=Qk.T@r;r=r-Qk@h2;beta=np.sqrt(r@r);assert np.array_equal(r/beta,Q[:,k]),(a.method,k)
   H[:k,k]=h1+h2;H[k,k]=beta
 np.savez(a.worker,Q=Q,H=H,idx=idx,parents=parents,P=P,w=w)
 from threadpoolctl import threadpool_info
 libs=threadpool_info()
 for z in libs:z['sha256']=sha(z['filepath'])
 write(pathlib.Path(str(a.worker)+'.runtime.json'),{'OPENBLAS_CORETYPE':os.getenv('OPENBLAS_CORETYPE'),'libraries':libs})

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--external',required=True);ap.add_argument('--input-dir',type=pathlib.Path);ap.add_argument('--output-dir',type=pathlib.Path);ap.add_argument('--receipt',type=pathlib.Path);ap.add_argument('--worker',type=pathlib.Path);ap.add_argument('--input',type=pathlib.Path);ap.add_argument('--method');ap.add_argument('--precision');a=ap.parse_args()
 if a.worker:return worker(a)
 a.output_dir.mkdir(parents=True,exist_ok=False);up=e6.load_upstream(a.external);rows=[];commands=[];t0=time.time()
 for name in ['rotpi4','triangle']:
  inp=a.input_dir/(name+'-input.npz');frozen=np.load(inp);P,w,n=frozen['P'],frozen['w'],int(frozen['n']);U=independent_reference(P,n,name);Ud=e6.reference(P,w,n,name,P[:128])[0]
  for method in ['upstream_xy','mirror','alt','adapt']:
   controls=[];Qs=[];paths=[]
   for core,prec in [('Haswell','double'),('Nehalem','double'),('Haswell','extended')]:
    dest=a.output_dir/(name+'-'+method+'-'+core+'-'+prec+'.npz');cmd=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),'--external',a.external,'--worker',str(dest),'--input',str(inp),'--method',method,'--precision',prec];start=time.time();subprocess.run(cmd,env=dict(os.environ,OPENBLAS_CORETYPE=core,OPENBLAS_NUM_THREADS='1'),check=True,timeout=1800);commands.append({'argv':cmd,'elapsed_seconds':time.time()-start});z=np.load(dest);Q,H,idx,parents=z['Q'],z['H'],z['idx'],z['parents'];assert np.array_equal(P,z['P']) and np.array_equal(w,z['w']);val=propagate(P.astype(LD),Q,H,idx,up,U,parents=parents);val.update(core=core,precision=prec,parent_sha256=hashlib.sha256(parents.tobytes()).hexdigest(),raw={'path':str(dest),'bytes':dest.stat().st_size,'sha256':sha(dest)},runtime=json.loads(pathlib.Path(str(dest)+'.runtime.json').read_text()));controls.append(val);Qs.append(Q.astype(LD));paths.append(parents);print(name,method,core,prec,val['raw_normal_Q_norm'],val['normal_reconstruction_discrepancy'],flush=True)
   rows.append({'name':name,'method':method,'n':n,'input_sha256':hashlib.sha256(P.tobytes()+w.tobytes()).hexdigest(),'reference_double_vs_ld_projector_gap':norm(normal(Ud.astype(LD),U)),'kernel_normal_Q_difference':norm(normal(Qs[0]-Qs[1],U)),'kernel_parent_path_equal':bool(np.array_equal(paths[0],paths[1])),'extended_parent_path_equal':bool(np.array_equal(paths[0],paths[2])),'controls':controls})
   write(a.receipt,{'status':'MEASURED_CLASS_CONTROLS_REVIEW_PENDING','code_sha256':sha(__file__),'helper_sha256':sha(pathlib.Path(__file__).with_name('g4_attribution.py')),'commands':commands,'cases':rows,'elapsed_seconds':time.time()-t0})
if __name__=='__main__':main()
