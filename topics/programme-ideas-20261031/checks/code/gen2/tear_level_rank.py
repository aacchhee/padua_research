"""Per-level composite factor: eigenvectors of blkdiag(D1,D2)+E (rank-b tear) in the
basis of the block eigenvectors, rows sorted by block eigenvalues d, columns by final
eigenvalues. Off-diagonal numerical ranks vs b (tol 1e-10, 1e-8)."""
import numpy as np, sys
exec(open('tear_factor_ranks.py').read().split('def run(')[0])
def run(name,x,y,w,n):
    N=len(x); Hx,Hy=sections(x,y,w,n)
    deg=np.array([k for k in range(n+1) for _ in range(k+1)])
    bnds=[int((deg==k).argmax()) for k in range(1,n+1)]
    m=min(bnds,key=lambda t:abs(t-N/2))
    A=Hx.copy(); A[:m,m:]=0; A[m:,:m]=0; E=Hx-A
    b=int((np.linalg.svd(E,compute_uv=False)>1e-12).sum())
    d1,U1=np.linalg.eigh(A[:m,:m]); d2,U2=np.linalg.eigh(A[m:,m:])
    U=np.zeros((N,N)); U[:m,:m]=U1; U[m:,m:]=U2; d=np.r_[d1,d2]
    lam,Qf=np.linalg.eigh(Hx)          # final eigenvectors (nodes' x-coords, distinct for random; clustered for Padua)
    F=U.T@Qf                            # composite level factor
    F=F[np.argsort(d)][:,np.argsort(lam)]
    for tol in [1e-10,1e-8]:
        out=[]
        for (r0,r1,c0,c1) in [(0,N//2,N//2,N),(N//2,N,0,N//2)]:
            s=np.linalg.svd(F[r0:r1,c0:c1],compute_uv=False); out.append(int((s>tol*s[0]).sum()))
        for (a,bb) in [(0,N//2),(N//2,N)]:
            mm=(a+bb)//2
            for (r0,r1,c0,c1) in [(a,mm,mm,bb),(mm,bb,a,mm)]:
                s=np.linalg.svd(F[r0:r1,c0:c1],compute_uv=False); out.append(int((s>tol*s[0]).sum()))
        print(f"{name}: N={N} b={b} tol={tol:.0e}: composite factor off-diag ranks lvl1={out[:2]} lvl2={out[2:]}  (b+log2N={b+int(np.log2(N))})")
n=int(sys.argv[1]); rng=np.random.default_rng(0); N=(n+1)*(n+2)//2
x=rng.uniform(-1,1,N); y=rng.uniform(-1,1,N); w=rng.uniform(0.5,1.5,N); run("random",x,y,w,n)
xp,yp,wp=padua(n); run("padua",xp,yp,wp,n)
# also: Hx eigenvalue multiplicity for padua
print("padua distinct x:", len(np.unique(np.round(xp,12))), "of", len(xp))
