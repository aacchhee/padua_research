"""Draft-1 entry point 1, quick version: tear Hx at a degree boundary, do the rank-b
update as b sequential rank-one updates, store each eigenvector factor (Cauchy-like),
and measure off-diagonal numerical ranks (tol 1e-10) in eigenvalue-sorted order,
at the top level and one level down. Random nodes and Padua (cubature weights)."""
import numpy as np, sys
from numpy.polynomial import chebyshev as C
def sections(x,y,w,n):
    cols=[]
    for k in range(n+1):
        for i in range(k,-1,-1):
            cols.append(C.chebval(x,np.eye(i+1)[i])*C.chebval(y,np.eye(k-i+1)[k-i]))
    V=np.sqrt(w)[:,None]*np.array(cols).T
    Q,R=np.linalg.qr(V); s=np.sign(np.diag(R)); Q=Q*s
    return Q.T@(x[:,None]*Q), Q.T@(y[:,None]*Q)
def padua(n):
    pts=[];wts=[]
    for j in range(n+1):
        for k in range(n+2):
            if (j+k)%2==0:
                ex=0.5 if j in (0,n) else 1.0; ey=0.5 if k in (0,n+1) else 1.0
                pts.append((np.cos(j*np.pi/n),np.cos(k*np.pi/(n+1)))); wts.append(2*ex*ey/(n*(n+1)))
    p=np.array(pts); return p[:,0],p[:,1],np.array(wts)
def offdiag_ranks(F,tol=1e-10):
    N=F.shape[0]; out=[]
    for (r0,r1,c0,c1) in [(0,N//2,N//2,N),(N//2,N,0,N//2)]:
        s=np.linalg.svd(F[r0:r1,c0:c1],compute_uv=False); out.append(int((s>tol*s[0]).sum()) if s[0]>0 else 0)
    # level 2: four off-diagonal blocks within each half
    for (a,b) in [(0,N//2),(N//2,N)]:
        m=(a+b)//2
        for (r0,r1,c0,c1) in [(a,m,m,b),(m,b,a,m)]:
            s=np.linalg.svd(F[r0:r1,c0:c1],compute_uv=False); out.append(int((s>tol*s[0]).sum()) if s[0]>0 else 0)
    return out
def run(name,x,y,w,n):
    N=len(x); Hx,Hy=sections(x,y,w,n)
    deg=np.array([k for k in range(n+1) for _ in range(k+1)])
    # tear at degree boundary nearest N/2
    bnds=[int((deg==k).argmax()) for k in range(1,n+1)]
    m=min(bnds,key=lambda t:abs(t-N/2))
    A=Hx.copy(); A[:m,m:]=0; A[m:,:m]=0
    E=Hx-A; sv=np.linalg.svd(E,compute_uv=False); b=int((sv>1e-12*sv[0]).sum())
    # block eigendecomposition
    d1,U1=np.linalg.eigh(A[:m,:m]); d2,U2=np.linalg.eigh(A[m:,m:])
    U=np.zeros((N,N)); U[:m,:m]=U1; U[m:,m:]=U2; d=np.r_[d1,d2]
    # symmetric rank-b E = sum sigma_i v_i v_i^T  (eigendecomposition of E)
    ev,V=np.linalg.eigh(E); idx=np.argsort(-np.abs(ev))[:b]
    D=np.diag(d); Qacc=U; ranks=[]; total=0
    for i in idx:
        v=Qacc.T@V[:,i]; Dn=D+ev[i]*np.outer(v,v)
        lam,F=np.linalg.eigh(Dn)           # F is the Cauchy-like factor (in the current basis)
        # sort current basis by eigenvalue so clustering is spatial
        order=np.argsort(np.diag(D)); F2=F[order][:,np.argsort(lam)]
        r=offdiag_ranks(F2); ranks.append(r)
        total+= N*max(r)*int(np.log2(N))
        Qacc=Qacc@F; D=np.diag(lam)
    Qfin=Qacc
    err=np.linalg.norm(Qfin.T@Hx@Qfin-D)
    print(f"{name}: N={N}, tear rank b={b}, ||Q^T Hx Q - D||={err:.1e}; factor off-diag ranks (lvl1 x2, lvl2 x4), first 3 and last 3 factors:")
    import collections; print("   top-level rank histogram:", sorted(collections.Counter(max(r[:2]) for r in ranks).items()))
    print(f"   max rank over factors={max(max(r) for r in ranks)}, crude storage sum N*maxrank*log2N = {total:.2e} vs N^2={N*N:.2e}, N^1.5={N**1.5:.2e}")
n=int(sys.argv[1]) if len(sys.argv)>1 else 20
rng=np.random.default_rng(0); N=(n+1)*(n+2)//2
x=rng.uniform(-1,1,N); y=rng.uniform(-1,1,N); w=rng.uniform(0.5,1.5,N)
run("random",x,y,w,n)
xp,yp,wp=padua(n); run("padua",xp,yp,wp,n)
