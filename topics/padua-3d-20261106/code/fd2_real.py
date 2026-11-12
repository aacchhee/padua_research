"""D2 round 2: exact real calibrations, ORSV probes, Jacobi extensions."""
import argparse
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np
from scipy.optimize import least_squares
import sympy as s

ORSV=np.array([
 [[18,6,6,-6],[6,2,2,-2],[6,2,2,-2],[-6,-2,-2,4]],
 [[4,-6,6,4],[-6,13,-9,-8],[6,-9,9,6],[4,-8,6,5]],
 [[1,0,-3,0],[0,4,0,6],[-3,0,9,0],[0,6,0,9]],
 [[9,-3,0,0],[-3,10,9,-6],[0,9,9,-6],[0,-6,-6,4]]],dtype=float)


def monomials(n):
    return sorted([a for a in it.product(range(n+1),repeat=3) if sum(a)<=n],key=lambda a:(sum(a),a))


def vandermonde(P,n):
    mm=monomials(n)
    return np.array([np.prod(P**np.array(a),axis=1) for a in mm]).T


def natural(n):
    ts=list(range(n+3)); ids=list(it.combinations(ts,3))
    P=[(a*b*c,-(a*b+a*c+b*c),a+b+c) for a,b,c in ids]
    ll=lambda t,p:p[0]+t*p[1]+t*t*p[2]-t**3
    assert len(set(P))==math.comb(n+3,3)
    # Cardinal products prove rational unisolvence independently of a determinant.
    den=[]
    for I,p in zip(ids,P):
        omit=[t for t in ts if t not in I]
        d=math.prod(ll(t,p) for t in omit); assert d!=0; den.append(d)
        for J,q in zip(ids,P):
            assert math.prod(ll(t,q) for t in omit)==(d if I==J else 0)
    # Check every triple normal determinant and every four-plane augmented det.
    for I in ids: assert s.Matrix([[1,t,t*t] for t in I]).det()!=0
    for I in it.combinations(ts,4):
        assert s.Matrix([[-t**3,1,t,t*t] for t in I]).det()!=0
    arr=np.array(P,float); lo=arr.min(0); hi=arr.max(0)
    Q=2*(arr-lo)/(hi-lo)-1
    V=vandermonde(Q,n)
    return {'n':n,'count':len(P),'raw_integer_nodes':P,'plane_t':ts,
        'box_min':list(map(int,lo)),'box_max':list(map(int,hi)),
        'cardinal_products_exact':True,'denominators':den,
        'all_triple_normals_independent':True,'no_four_projective_planes_meet':True,
        'real_in_cube':bool(np.max(np.abs(Q))<=1),
        'vandermonde_numerical_rank':int(np.linalg.matrix_rank(V)),
        'vandermonde_condition':float(np.linalg.cond(V)),
        'radicality_exact':'distinct rational zeros plus R1 quotient dimension=N',
        'en_and_sym_same_geometry':True}


def orsv_probe(n):
    rng=np.random.default_rng(202611120202+n)
    k=n+2
    A=np.zeros((4,k,k)); A[:,:4,:4]=ORSV
    # Affine chart x0+2*x1+4*x2+8*x3=1, source projective coordinates.
    A[1:,:4,:4]-=np.array([2,4,8])[:,None,None]*ORSV[0]
    for j in range(4,k):
        t=j+1
        A[:,j,j]=[-t**3,1,t,t*t]
        A[0,j,:j]=A[0,:j,j]=.1
        A[1,j,:j]=A[1,:j,j]=.03
    roots=[]; calls=0; t0=time.monotonic()
    # Rank k-2 locus in principal Schur charts. All results are lower counts.
    for pair in it.combinations(range(k),2):
        rest=[j for j in range(k) if j not in pair]
        def residual(p,want_jac=False):
            nonlocal calls
            calls+=1; M=A[0]+np.einsum('i,ijk->jk',p,A[1:])
            B=M[np.ix_(rest,rest)]; C=M[np.ix_(rest,pair)]
            try: Z=np.linalg.solve(B,C)
            except np.linalg.LinAlgError: return None
            S=M[np.ix_(pair,pair)]-C.T@Z
            f=S[np.triu_indices(2)]
            if not want_jac:return f
            J=[]
            for E in A[1:]:
                D=E[np.ix_(pair,pair)]-E[np.ix_(pair,rest)]@Z-Z.T@E[np.ix_(rest,pair)]+Z.T@E[np.ix_(rest,rest)]@Z
                J.append(D[np.triu_indices(2)])
            return f,np.array(J).T
        starts=[np.zeros(3)]+list(rng.uniform(-3,3,(31,3)))
        for p in starts:
            p=p.copy()
            for _ in range(20):
                v=residual(p,True)
                if v is None:break
                f,J=v
                if np.linalg.norm(f)<1e-9:break
                try:d=np.linalg.solve(J,-f)
                except np.linalg.LinAlgError:break
                if np.linalg.norm(d)>100:break
                old=np.linalg.norm(f); accepted=False
                for scale in (1,.5,.25,.125,.0625,.03125):
                    ff=residual(p+scale*d)
                    if ff is not None and np.linalg.norm(ff)<old:
                        p+=scale*d;accepted=True;break
                if not accepted:break
            M=A[0]+np.einsum('i,ijk->jk',p,A[1:])
            sv=np.linalg.svd(M,compute_uv=False)
            if sv[-2]<1e-7 and sv[-3]>1e-6 and np.linalg.norm(p)<1e4:
                if not any(np.linalg.norm(p-q)<1e-5 for q in roots):roots.append(p)
    return {'n':n,'size':k,'source':'ORSV1311.3675v2 p7 (rho,sigma)=(10,10)',
        'source_input_sha256':hashlib.sha256(ORSV.astype('<f8').tobytes()).hexdigest(),
        'extension':'none' if k==4 else 'border .1 constant/.03 x, moment-curve diagonal',
        'seed':202611120202+n,'schur_starts_per_patch':32,'newton_iterations':20,
        'real_distinct_nodes_found':len(roots),'expected_count':math.comb(n+3,3),
        'nodes':[p.tolist() for p in roots], 'full_count_verified':False,
        'residual_calls':calls,'wall_seconds':time.monotonic()-t0}


def jacobi(n,start,progress):
    resource.setrlimit(resource.RLIMIT_CPU,(60,61))
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    mm=monomials(n); pos={a:i for i,a in enumerate(mm)}; N=len(mm)
    top=[i for i,a in enumerate(mm) if sum(a)==n]
    prev=[i for i,a in enumerate(mm) if sum(a)==n-1]
    H=np.zeros((3,N,N))
    for axis in range(3):
        for i,a in enumerate(mm):
            b=list(a);b[axis]+=1;b=tuple(b)
            if b in pos:
                val=1/np.sqrt(2) if a[axis]==0 else .5
                H[axis,i,pos[b]]=H[axis,pos[b],i]=val
    # Only Pi_(n-1) sections fixed; compatibility forces lower-to-extra zeros.
    pairs=[(i,j) for i in prev for j in top]+[(i,j) for i in top for j in top if i<=j]
    D=np.zeros((len(pairs),N,N))
    for h,(i,j) in enumerate(pairs):D[h,i,j]=D[h,j,i]=1
    P=len(pairs); tri=np.triu_indices(N,1); L=len(tri[0]); pp=[(0,1),(0,2),(1,2)]
    v=np.array([[H[a,i,j] for i,j in pairs] for a in range(3)]).ravel()
    for i,j in pairs:H[:,i,j]=H[:,j,i]=0
    seed=202611120202+n; rng=np.random.default_rng(seed+1000*start)
    v+=rng.normal(0,.02 if start==0 else .2,len(v))
    best=float('inf');calls=0;c0=time.process_time();t0=time.monotonic()
    def unpack(v):return H+np.einsum('ap,pij->aij',v.reshape(3,P),D)
    def fun(v):
        nonlocal best,calls
        W=unpack(v);calls+=1
        f=np.concatenate([(W[a]@W[b]-W[b]@W[a])[tri] for a,b in pp])
        norm=float(np.linalg.norm(f))
        if norm<best:
            best=norm
            Path(progress).write_text(json.dumps({'n':n,'start':start,'seed':seed+1000*start,
                'residual_norm':norm,'function_calls':calls,'variables':len(v),
                'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,
                'status':'progress','nodes_extracted':False}))
        return f
    def jac(v):
        W=unpack(v);J=np.zeros((3*L,3*P))
        for h,(a,b) in enumerate(pp):
            Ja=np.einsum('pij,jk->pik',D,W[b])-np.einsum('ij,pjk->pik',W[b],D)
            Jb=np.einsum('ij,pjk->pik',W[a],D)-np.einsum('pij,jk->pik',D,W[a])
            J[h*L:(h+1)*L,a*P:(a+1)*P]=Ja[:,tri[0],tri[1]].T
            J[h*L:(h+1)*L,b*P:(b+1)*P]=Jb[:,tri[0],tri[1]].T
        return J
    sol=least_squares(fun,v,jac=jac,tr_solver='lsmr',max_nfev=150,ftol=1e-10,xtol=1e-10,gtol=1e-10)
    row=json.loads(Path(progress).read_text());row.update(status='completed',nfev=sol.nfev,termination=sol.message)
    W=unpack(sol.x)
    if np.linalg.norm(fun(sol.x))<1e-8:
        _,U=np.linalg.eigh(W[0]+2*W[1]+3*W[2])
        Q=np.array([np.diag(U.T@E@U) for E in W]).T
        off=max(np.linalg.norm(U.T@E@U-np.diag(np.diag(U.T@E@U))) for E in W)
        rank=int(np.linalg.matrix_rank(vandermonde(Q,n)))
        weights=U[0,:]**2
        row.update(joint_offdiagonal_norm=float(off),cube_max=float(np.max(np.abs(Q))),
                   evaluation_rank=rank,minimum_weight=float(weights.min()))
        if off<1e-7 and rank==N and np.max(np.abs(Q))<=1+1e-7 and weights.min()>1e-10:
            row.update(nodes_extracted=True,nodes=Q.tolist(),weights=weights.tolist())
    row.update(cpu_seconds=time.process_time()-c0,wall_seconds=time.monotonic()-t0)
    Path(progress).write_text(json.dumps(row))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--child',nargs=3);ap.add_argument('--output');a=ap.parse_args()
    if a.child:jacobi(int(a.child[0]),int(a.child[1]),a.child[2]);return
    rec={'schema':'fd2-real-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'python':sys.version,'numpy':np.__version__,'natural':[],'orsv':[],'jacobi':[]}
    for n in (2,3,4):rec['natural'].append(natural(n))
    for n in (2,3,4):rec['orsv'].append(orsv_probe(n))
    for n,start in it.product((3,4),(0,1)):
        tmp=f'/tmp/fd2-jacobi-{n}-{start}.json'
        cmd=[sys.executable,__file__,'--child',str(n),str(start),tmp]
        try:
            p=subprocess.run(cmd,capture_output=True,text=True,timeout=75,
                env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
            outcome='completed' if p.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:outcome='wall_timeout';p=None
        row=json.loads(Path(tmp).read_text()) if Path(tmp).exists() else {'n':n,'start':start}
        row.update(process_outcome=outcome,returncode=None if p is None else p.returncode)
        if p is not None and p.returncode:row['stderr']=p.stderr[-500:]
        rec['jacobi'].append(row)
        Path(a.output).write_text(json.dumps(rec,separators=(',',':'),sort_keys=True)+'\n')
        print(json.dumps(row),flush=True)


if __name__=='__main__':main()
