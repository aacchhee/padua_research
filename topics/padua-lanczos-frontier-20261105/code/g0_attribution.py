"""Bounded G0 diagnostics; no gate verdict and no scientific-target execution.
Run OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell python -B this.py
  --output-dir <new external directory> --external <pinned polyrat>
  --snapshot <restored 8359bf7 tree> --receipt <JSON path>.
"""
import argparse, hashlib, importlib.util, json, os, pathlib, platform
import subprocess, sys, time
from fractions import Fraction
import numpy as np
import scipy
from scipy.linalg import svdvals
LD = np.longdouble
PINS = {'arnoldi.py':'e51f356170dc5e1403f1065daf5bc331e7ce470cac1b9161f5ecb9efccf68d86',
        'index.py':'84df400c73a2aacf922ff38c0a591b525c2ac1f9b7a9f958f4111d4ceb88d10d',
        'basis.py':'9ce50feba7cfaa706db3bb94bbe2b34f065d9dbde28a18a3eee021d11e8ec478',
        'version.py':'1d13b63cb7af46b37f80ac0d695be5f795c2db5ce6e66dea34143da4cb434439'}
LOCAL_PINS={'L2/l2_core.py':'e8c8fa3378b3531f4fc13faac9902757b97c92c281b2bcd2c02875e0b1c5638d','L1/l1_recurrence.py':'4b6014359d6cf50d2977ace0524846a5d0bf5498528a382e1c6abde2cb05b884','L1/l1_r04_checkerboard.py':'1a53cdc4c187edf5ae1e14a60d125b7e2846009134d2d390a68ceb8345506c20'}
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def load_e6(root):
    for name,pin in LOCAL_PINS.items():assert sha(pathlib.Path(root)/'tracks/bivariate-lanczos/code'/name)==pin
    p=pathlib.Path(root)/'tracks/bivariate-lanczos/code/drift/e6_benchmark.py'
    assert sha(p)=='e328b7d5d965637e986285cafe596ac15cdd9320c195d6f02162d883267baafe'
    spec=importlib.util.spec_from_file_location('e6',p); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def nodes():
    return np.array([(Fraction(i,12)-1,Fraction(j,12)-1) for i in range(25) for j in range(25-i)],dtype=float)

def cgs(V):
    Q=np.zeros_like(V,dtype=LD)
    for k in range(V.shape[1]):
        q=V[:,k].astype(LD).copy()
        for _ in range(2): q-=Q[:,:k]@(Q[:,:k].T@q)
        Q[:,k]=q/np.sqrt(np.sum(q*q))
    return Q

def jac(n,a,b,x):
    p=np.ones_like(x); q=((a-b)+(a+b+2)*x)/2
    if n==0:return p
    for k in range(1,n):
        h=LD(2*k+a+b)
        r=((h+1)*((h*(h+2)*x+a*a-b*b)*q)-2*(k+a)*(k+b)*(h+2)*p)/(2*(k+1)*(k+a+b+1)*h)
        p,q=q,r
    return q

def dubiner(P,mp=False):
    x,y=P.astype(LD).T; xi=(x+1)/2;et=(y+1)/2;om=1-et
    arg=(2*xi-om)/np.where(om>0,om,1)
    if not mp:
        return np.column_stack([jac(t-j,0,0,arg)*om**(t-j)*jac(j,2*(t-j)+1,0,2*et-1) for t in range(13) for j in range(t+1)])
    import mpmath as m
    m.mp.dps=50
    # Independent 50-digit Jacobi evaluations on the identical rounded nodes.
    V=np.empty((len(P),91),dtype=LD)
    for r,(xx,yy) in enumerate(P):
        xx=(m.mpf(float(xx))+1)/2; yy=(m.mpf(float(yy))+1)/2;o=1-yy
        aa=(2*xx-o)/o if o else m.mpf(0)
        for k,(t,j) in enumerate((t,j) for t in range(13) for j in range(t+1)):
            # hypergeometric Jacobi fails at some special nodes; finite exact sum.
            def jj(n,a,b,z):
                return sum(m.binomial(n+a,k)*m.binomial(n+b,n-k)*((z-1)/2)**(n-k)*((z+1)/2)**k for k in range(n+1))
            V[r,k]=LD(str(jj(t-j,0,0,aa)*o**(t-j)*jj(j,2*(t-j)+1,0,2*yy-1)))
    return V

def norm(A): return float(svdvals(np.asarray(A,dtype=float))[0])
def normal(Q,U): return Q-U@(U.T@Q)
def gap(Q,U): return norm(normal(cgs(Q),U))

def worker(a):
    e6=load_e6(a.snapshot);up=e6.load_upstream(a.external);P=nodes();out={}
    for label,order in [('xy',[0,1]),('yx',[1,0])]:
        for prec,dtype in [('double',float),('extended',LD)]:
            Q,H,idx=up.vandermonde_arnoldi_CGS(P[:,order].astype(dtype),12,weight=np.ones(325,dtype=dtype))
            out[label+'_'+prec+'_Q']=Q;out[label+'_'+prec+'_H']=H
    for label in ['alt','mirror','adapt']:
        for prec,dtype in [('double',float),('extended',LD)]:
            Q,info,_=e6.L2.run_sel(P[:,0],P[:,1],np.ones(325),12,sel=label,reorth='fullcgs2',dtype=dtype)
            out[label+'_'+prec+'_Q']=Q
            if label!='alt':continue
            H=np.zeros((91,91),dtype=dtype);parents=np.zeros((91,2),dtype=int)
            for k in range(1,91):
                op,par=info[k];axis=0 if op=='X' else 1;parents[k]=axis,par
                q=P[:,axis].astype(dtype)*Q[:,par];Qk=Q[:,:k]
                s1=Qk.T@q;r=q-Qk@s1;s2=Qk.T@r;r=r-Qk@s2
                H[:k,k]=s1+s2;H[k,k]=np.sqrt(r@r)
                assert np.array_equal(r/H[k,k],Q[:,k])
            out[label+'_'+prec+'_H']=H;out['alt_parents']=parents
    out['idx']=idx;np.savez(a.worker,**out)
    from threadpoolctl import threadpool_info
    runtime=threadpool_info()
    for lib in runtime:
        lib['sha256']=sha(lib['filepath'])
    pathlib.Path(a.worker+'.runtime.json').write_text(json.dumps(runtime,indent=2)+'\n')

def propagate(P,Q,H,idx,up,U,parents=None):
    Q=Q.astype(LD);H=H.astype(LD);N=Q.shape[1];F=np.zeros_like(Q);E=np.zeros_like(Q)
    for k in range(1,N):
        axis,p=up._update_rule(idx,idx[k]) if parents is None else parents[k];beta=H[k,k]
        F[:,k]=P[:,axis]*Q[:,p]-Q[:,:k]@H[:k,k]-beta*Q[:,k]
        E[:,k]=(P[:,axis]*E[:,p]-E[:,:k]@H[:k,k]-F[:,k])/beta
    # E solves the frozen unit-lower-triangular inverse, node by node.
    # Q-E is the computed-coefficient polynomial surrogate. Its scalar start
    # Q[:,0] is constant and therefore exactly in the reference polynomial space.
    direct=normal(Q,U);prop=normal(E,U)
    # 50-dps frozen surrogate evaluation is algebraically the same inverse solve,
    # avoiding amplification of the longdouble residual-reconstruction error.
    import mpmath as mp
    mp.mp.dps=50
    HH=[[mp.mpf(float(H[l,k])) for l in range(k)] for k in range(N)]
    bb=[mp.mpf(float(H[k,k])) for k in range(N)]
    EE=np.zeros_like(Q)
    relations=[None]+[up._update_rule(idx,idx[k]) if parents is None else parents[k] for k in range(1,N)]
    for r in range(len(P)):
        xx=[mp.mpf(float(z)) for z in P[r]];v=[mp.mpf(float(Q[r,0]))]
        for k in range(1,N):
            axis,p=relations[k]
            v.append((xx[axis]*v[p]-sum(h*z for h,z in zip(HH[k],v)))/bb[k])
            EE[r,k]=LD(str(mp.mpf(float(Q[r,k]))-v[k]))
    hpnormal=normal(EE,U)
    local=np.sqrt(np.sum(F*F,axis=0));beta=np.diag(H)[1:]
    return {'max_local_residual':float(max(local)), 'local_residual_fro':float(np.sqrt(np.sum(F*F))),
            'max_local_residual_over_u':float(max(local)/LD(2)**-53),
            'normalized_source_fro':float(np.sqrt(np.sum((F[:,1:]/beta)**2))),
            'propagated_error_norm':norm(E),'normal_error':norm(direct),'propagated_normal_error':norm(prop),
            'normal_reconstruction_discrepancy':norm(direct-prop),'frozen_inverse_50dps_normal_error':norm(hpnormal),'frozen_inverse_50dps_reconstruction_discrepancy':norm(direct-hpnormal),'ld_vs_50dps_propagation_discrepancy':norm(E-EE),
            'normal_amplification_over_residual_fro':norm(prop)/float(np.sqrt(np.sum(F*F))),
            'q0_constant':bool(np.all(Q[:,0]==Q[0,0]))},F,EE

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir');p.add_argument('--external',required=True);p.add_argument('--snapshot',required=True);p.add_argument('--receipt');p.add_argument('--worker');a=p.parse_args()
    for name,pin in PINS.items():assert sha(pathlib.Path(a.external)/'polyrat'/name)==pin
    if a.worker:return worker(a)
    assert os.getenv('OPENBLAS_NUM_THREADS')=='1' and os.getenv('OPENBLAS_CORETYPE')=='Haswell'
    d=pathlib.Path(a.output_dir);d.mkdir(parents=True,exist_ok=False);start=time.time();commands=[]
    for core in ['Haswell','Nehalem']:
        cmd=[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),'--external',a.external,'--snapshot',a.snapshot,'--worker',str(d/(core+'.npz'))]
        env=dict(os.environ,OPENBLAS_CORETYPE=core,OPENBLAS_NUM_THREADS='1');subprocess.run(cmd,env=env,check=True);commands.append({'env':{'OPENBLAS_CORETYPE':core,'OPENBLAS_NUM_THREADS':'1'},'argv':cmd})
    e6=load_e6(a.snapshot);up=e6.load_upstream(a.external);P=nodes();V=dubiner(P);U=cgs(V);Vm=dubiner(P,True);Um=cgs(Vm)
    ref=e6.reference(P,np.ones(325),12,'T24',P[:128])[0]
    result={'status':'MEASURED_DIAGNOSTICS_ONLY','rules_head':'f85c7b5c83822ff60b62c84bed1ec6ae31628422','source_snapshot':'8359bf7a047d9a212bd841224fb97a458cb7435e','upstream_commit':'6903d7af9995c9d88e661fb229626696e00fdfba','code_sha256':sha(__file__),'upstream_sha256':PINS,'local_dependency_sha256':LOCAL_PINS,'input_sha256':hashlib.sha256(P.tobytes()+np.ones(325).tobytes()).hexdigest(),'scope':{'set':'T24','n':12,'M':325,'N':91,'kernels':['Haswell','Nehalem']},'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'longdouble_mantissa':int(np.finfo(LD).nmant),'platform':platform.platform()},'reference':{'ld_vs_50dps_projector_gap':gap(U,Um),'double_vs_50dps_projector_gap':gap(ref,Um),'ld_orthogonality':norm(U.T@U-np.eye(91,dtype=LD)),'normalized_dubiner_condition':float(np.linalg.cond(np.asarray(V/np.sqrt(np.sum(V*V,axis=0)),float)))},'commands':commands,'cases':{}}
    np.savez(d/'references.npz',U=U,U50=Um,V=V,V50=Vm)
    for core in ['Haswell','Nehalem']:
        arr=np.load(d/(core+'.npz'));res={}
        for order in ['xy','yx','alt']:
            Q=arr[order+'_double_Q'];H=arr[order+'_double_H'];idx=arr['idx'];PP=P[:,[1,0] if order=='yx' else [0,1]].astype(LD)
            diag,F,E=propagate(PP,Q,H,idx,up,Um,arr['alt_parents'] if order=='alt' else None)
            legacy=e6.metrics(Q,ref)[0]['gap']
            diag.update({'legacy_e6_gap':legacy,'fixed_Q_gap_50dps_reference':gap(Q,Um),'fixed_Q_gap_ld_reference':gap(Q,U),'extended_original_algorithm_gap':gap(arr[order+'_extended_Q'],Um),'orthogonality':norm(Q.astype(LD).T@Q.astype(LD)-np.eye(91,dtype=LD))})
            np.savez(d/(core+'-'+order+'-propagation.npz'),F=F,E=E);res[order]=diag
        for order in ['mirror','adapt']:
            Q=arr[order+'_double_Q']
            res[order]={'legacy_e6_gap':e6.metrics(Q,ref)[0]['gap'],'fixed_Q_gap_50dps_reference':gap(Q,Um),'extended_original_algorithm_gap':gap(arr[order+'_extended_Q'],Um)}
        result['cases'][core]=res
    A=np.load(d/'Haswell.npz');B=np.load(d/'Nehalem.npz')
    result['kernel_comparison']={o:{'Q_entry_max_difference':float(np.max(abs(A[o+'_double_Q']-B[o+'_double_Q']))),'H_entry_max_difference':float(np.max(abs(A[o+'_double_H']-B[o+'_double_H']))),'computed_span_gap':gap(A[o+'_double_Q'],cgs(B[o+'_double_Q']))} for o in ['xy','yx','alt']}
    result['kernel_runtime']={core:json.loads((d/(core+'.npz.runtime.json')).read_text()) for core in ['Haswell','Nehalem']}
    result['elapsed_seconds']=time.time()-start
    result['artifacts']=[{'path':str(f),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(d.iterdir())]
    result['limits']=['No historical Q/H or dispatch/library binary pin is available; no exact historical causal reconstruction.','Longdouble residual and inverse computations are diagnostic, not interval certificates.','Alt H reconstructed by exact operation replay and checked entrywise; mirror/adapt only reference and precision controls.','No G0 disposition, tolerance change, new theorem, or G1-G4 run.']
    pathlib.Path(a.receipt).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result['cases'],indent=2))
if __name__=='__main__':main()
