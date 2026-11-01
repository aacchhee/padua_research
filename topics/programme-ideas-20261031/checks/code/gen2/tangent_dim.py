"""Probe for gen2-draft-2: tangent dimension of the commuting symmetric block-tridiagonal
pattern variety at a generic discrete-measure pair, vs Jacobian rank of (nodes,weights)->(Hx,Hy)."""
import numpy as np
from numpy.polynomial import chebyshev as C
def sections(x,y,w,n):
    cols=[]
    for k in range(n+1):
        for i in range(k,-1,-1):
            cols.append(C.chebval(x,np.eye(i+1)[i])*C.chebval(y,np.eye(k-i+1)[k-i]))
    V=np.sqrt(w)[:,None]*np.array(cols).T
    Q,R=np.linalg.qr(V); 
    # fix signs: make diag(R)>0
    s=np.sign(np.diag(R)); Q=Q*s
    return Q.T@(x[:,None]*Q), Q.T@(y[:,None]*Q)
for n in [3,4,5,6]:
    N=(n+1)*(n+2)//2
    rng=np.random.default_rng(n)
    x=rng.uniform(-1,1,N); y=rng.uniform(-1,1,N); w=rng.uniform(0.5,1.5,N)
    Hx,Hy=sections(x,y,w,n)
    deg=np.array([k for k in range(n+1) for _ in range(k+1)])
    pat=(np.abs(deg[:,None]-deg[None,:])<=1)
    # basis of symmetric pattern matrices
    pairs=[(i,j) for i in range(N) for j in range(i,N) if pat[i,j]]
    m=len(pairs)
    # linear map (Ex,Ey) -> [Ex,Hy]+[Hx,Ey] (antisymmetric output)
    rows=[]
    def basis(i,j):
        E=np.zeros((N,N)); E[i,j]=1; E[j,i]=1; return E
    cols=[]
    for (i,j) in pairs:
        E=basis(i,j); cols.append((E@Hy-Hy@E).ravel())
    for (i,j) in pairs:
        E=basis(i,j); cols.append((Hx@E-E@Hx).ravel())
    A=np.array(cols).T
    sv=np.linalg.svd(A,compute_uv=False)
    rank=(sv>1e-9*sv[0]).sum()
    tdim=2*m-rank
    # Jacobian of (x,y,w)->pattern entries
    def f(p):
        xx,yy,ww=p[:N],p[N:2*N],p[2*N:]
        hx,hy=sections(xx,yy,ww,n)
        return np.r_[hx[pat],hy[pat]]
    p0=np.r_[x,y,w]; h=1e-6
    J=np.array([(f(p0+h*e)-f(p0-h*e))/(2*h) for e in np.eye(3*N)]).T
    sj=np.linalg.svd(J,compute_uv=False); jr=(sj>1e-7*sj[0]).sum()
    # gap report
    print(f"n={n} N={N}: sym pattern entries per matrix={m}, tangent dim of commuting pattern variety={tdim}, "
          f"Jacobian rank={jr} (3N-1={3*N-1}), top-block freedoms (n+1)(n+2)={(n+1)*(n+2)}; sv gap J: {sj[jr-1]:.1e}/{sj[jr] if jr<len(sj) else 0:.1e}")
