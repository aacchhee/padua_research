"""D2 round 3: bounded full symmetric-pencil parameter search (MEASURED)."""
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
from scipy.spatial.distance import pdist


def basis(P,n):
    v=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    return np.array([v[0][:,a]*v[1][:,b]*v[2][:,c]
        for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]).T


def mesh(m):
    t=np.cos(np.arange(m)*np.pi/(m-1))
    return np.array(list(it.product(t,repeat=3)))


def normalize(A,P):
    lo=P.min(0);hi=P.max(0);half=(hi-lo)/2;center=(hi+lo)/2
    if half.min()<1e-9:return None
    A=A.copy();A[0]+=np.einsum('i,ijk->jk',center,A[1:]);A[1:]*=half[:,None,None]
    A/=np.linalg.norm(A)
    return A,(P-center)/half


def initial(n):
    k=n+2;A=np.zeros((4,k,k))
    for j in range(k):A[:,j,j]=[-j**3,1,j,j*j]
    t=k;A+=np.array([-t**3,1,t,t*t])[:,None,None]*np.ones((k,k))
    P=np.array([(a*b*c,-a*b-a*c-b*c,a+b+c)
                for a,b,c in it.combinations(range(n+3),3)],float)
    return normalize(A,P)


def charts(A,P):
    N,k=len(P),A.shape[1]
    M=A[0]+np.einsum('ni,ijk->njk',P,A[1:]);opts=list(it.combinations(range(k),2))
    det=[]
    for pair in opts:
        rest=[j for j in range(k) if j not in pair]
        det.append(np.abs(np.linalg.det(M[:,rest][:,:,rest])))
    choice=np.argmax(np.array(det),axis=0)
    pairs=np.array([opts[j] for j in choice]);rest=np.array([[j for j in range(k) if j not in p] for p in pairs])
    return pairs,rest


def track(A,P):
    P=P.copy();N=len(P);pair,rest=charts(A,P);batch=np.arange(N)[:,None,None]
    def blocks(M):
        return (M[batch,rest[:,:,None],rest[:,None,:]],
                M[batch,rest[:,:,None],pair[:,None,:]],
                M[batch,pair[:,:,None],pair[:,None,:]])
    for _ in range(12):
        M=A[0]+np.einsum('ni,ijk->njk',P,A[1:]);B,C,D=blocks(M)
        try:Z=np.linalg.solve(B,C)
        except np.linalg.LinAlgError:return None
        S=D-np.einsum('nri,nrj->nij',C,Z)
        F=S[:,(0,0,1),(0,1,1)]
        if np.max(np.abs(F))<1e-10:break
        J=[]
        for E in A[1:]:
            Eb,Ec,Ed=blocks(np.broadcast_to(E,M.shape))
            T=Ed-np.einsum('nri,nrj->nij',Ec,Z)-np.einsum('nri,nrj->nij',Z,Ec)+np.einsum('nri,nrs,nsj->nij',Z,Eb,Z)
            J.append(T[:,(0,0,1),(0,1,1)])
        J=np.transpose(np.array(J),(1,2,0))
        try:step=np.linalg.solve(J,-F[...,None])[...,0]
        except np.linalg.LinAlgError:return None
        if not np.all(np.isfinite(step)) or np.max(np.abs(step))>2:return None
        P+=step
    else:return None
    M=A[0]+np.einsum('ni,ijk->njk',P,A[1:]);sv=np.linalg.svd(M,compute_uv=False)
    if np.max(sv[:,-2])>1e-7 or np.min(sv[:,-3])<1e-7:return None
    if pdist(P).min()<1e-6:return None
    return normalize(A,P)


def estimate(A,P,n,Q):
    V=basis(P,n);cond=np.linalg.cond(V)
    if not np.isfinite(cond) or cond>1e12:return None
    C=np.linalg.inv(V);vals=np.sum(np.abs(basis(Q,n)@C),axis=1)
    return float(vals.max()),float(cond)


def child(n,start,path):
    resource.setrlimit(resource.RLIMIT_CPU,(50,51))
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    seed=202611120203+n+1000*start;rng=np.random.default_rng(seed)
    A,P=initial(n);Q=mesh(13);cost,cond=estimate(A,P,n,Q)
    first=cost;accept=0;rejected=0;step=.002;evals=1;t0=time.monotonic();c0=time.process_time()
    slots=[(a,i,j) for a in range(4) for i in range(n+2) for j in range(i,n+2)]
    def save(status):
        Path(path).write_text(json.dumps({'n':n,'start':start,'seed':seed,'status':status,
            'evaluations':evals,'accepted':accept,'guard_rejections':rejected,
            'initial_train':first,'best_train':cost,'condition':cond,
            'matrix':A.tolist(),'nodes':P.tolist(),'step':step,
            'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0},separators=(',',':')))
    save('progress')
    # The failed driver evaluated the baseline once per path before a NumPy2
    # batched-RHS shape error. Deduct that call from the original500 budget.
    while evals<499:
        B=A.copy();a,i,j=slots[int(rng.integers(len(slots)))];delta=rng.normal()*step
        B[a,i,j]+=delta
        if i!=j:B[a,j,i]+=delta
        candidate=track(B,P);evals+=1
        if candidate is None:rejected+=1
        else:
            BA,BP=candidate;v=estimate(BA,BP,n,Q)
            if v is None:rejected+=1
            elif v[0]<cost:
                A,P=BA,BP;cost,cond=v;accept+=1
        if evals%50==0:
            step*=.85
            save('progress')
        elif evals%10==0:save('progress')
    save('completed')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--child',nargs=3);ap.add_argument('--output');a=ap.parse_args()
    if a.child:child(int(a.child[0]),int(a.child[1]),a.child[2]);return
    rec={'schema':'fd2-optimize-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'python':sys.version,'numpy':np.__version__,'training_mesh':13,'assessment_mesh':41,'degrees':[]}
    for n in (3,4):
        degree={'n':n,'GT_benchmark':4.05 if n==3 else 5.09,'starts':[]};best=None
        Q=np.vstack([mesh(41),np.random.default_rng(202611120204+n).uniform(-1,1,(512,3))])
        A0,P0=initial(n);degree['baseline_assessment']=estimate(A0,P0,n,Q)[0]
        for start in range(4):
            tmp=f'/tmp/fd2-optimize-{n}-{start}.json';cmd=[sys.executable,__file__,'--child',str(n),str(start),tmp]
            try:
                p=subprocess.run(cmd,capture_output=True,text=True,timeout=60,
                    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
                outcome='completed' if p.returncode==0 else 'failed'
            except subprocess.TimeoutExpired:p=None;outcome='wall_timeout'
            if not Path(tmp).exists():
                degree['starts'].append({'start':start,'process_outcome':outcome,
                    'returncode':None if p is None else p.returncode,'stderr':None if p is None else p.stderr[-500:]});continue
            row=json.loads(Path(tmp).read_text());A=np.array(row.pop('matrix'));P=np.array(row.pop('nodes'))
            val,cond=estimate(A,P,n,Q);row.update(assessment=val,assessment_condition=cond,process_outcome=outcome,
                                               returncode=None if p is None else p.returncode)
            if p is not None and p.returncode:row['stderr']=p.stderr[-500:]
            row['raw_progress_sha256']=hashlib.sha256(Path(tmp).read_bytes()).hexdigest()
            degree['starts'].append(row)
            if best is None or val<best['assessment']:
                sv=np.linalg.svd(A[0]+np.einsum('ni,ijk->njk',P,A[1:]),compute_uv=False)
                best={'assessment':val,'start':start,'matrix':A.tolist(),'nodes':P.tolist(),
                    'count':len(P),'cube_max':float(np.max(np.abs(P))),
                    'minimum_node_distance':float(pdist(P).min()),'max_second_smallest_singular':float(sv[:,-2].max()),
                    'minimum_third_smallest_singular':float(sv[:,-3].min()),'condition':cond}
            print(json.dumps({'n':n,'start':start,'process_outcome':outcome,'assessment':val,'evaluations':row['evaluations']}),flush=True)
        degree['best']=best;rec['degrees'].append(degree)
        Path(a.output).write_text(json.dumps(rec,separators=(',',':'),sort_keys=True)+'\n')


if __name__=='__main__':main()
