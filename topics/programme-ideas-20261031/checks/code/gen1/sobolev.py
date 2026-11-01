import numpy as np
rng=np.random.default_rng(1)
def run(M=12,s=2,deg=3,seed=0):
    rng=np.random.default_rng(seed)
    x=rng.uniform(-1,1,M); y=rng.uniform(-1,1,M)
    idx=[(a,b) for t in range(deg+1) for a in range(t,-1,-1) for b in [t-a]]
    N=len(idx)
    # rows: M values, then for j<s: dx row, dy row
    rows=M+2*s
    V=np.zeros((rows,N)); 
    for c,(a,b) in enumerate(idx):
        V[:M,c]=x**a*y**b
        for j in range(s):
            V[M+2*j,c]=a*x[j]**(a-1)*y[j]**b if a>0 else 0
            V[M+2*j+1,c]=b*x[j]**a*y[j]**(b-1) if b>0 else 0
    # node operators: Xt acting on row vectors of (value, dx, dy) data: (x p)(z)=x p(z); d_x(xp)=p+x d_x p; d_y(xp)= x d_y p
    Xt=np.diag(np.r_[x, np.repeat(x[:s],2)]); Yt=np.diag(np.r_[y, np.repeat(y[:s],2)])
    for j in range(s):
        Xt[M+2*j, j]=1.0   # dx row gets value
        Yt[M+2*j+1, j]=1.0
    Q,R=np.linalg.qr(V)
    Hx=Q.T@Xt@Q; Hy=Q.T@Yt@Q
    degs=np.array([a+b for a,b in idx])
    def above(H):
        mask=(degs[:,None] < degs[None,:]-1)
        return np.linalg.matrix_rank(H*mask,tol=1e-10)
    def skew(H): return np.linalg.matrix_rank(H-H.T,tol=1e-10)
    comm=np.linalg.matrix_rank(Hx@Hy-Hy@Hx,tol=1e-10)
    # check node ops commute and are consistent: V_x-column relation
    return above(Hx),skew(Hx),above(Hy),skew(Hy),comm, np.linalg.norm(Xt@Yt-Yt@Xt), np.linalg.norm(Xt@V - V_times(V,idx,x,y,'x')) 
def V_times(V,idx,x,y,var):
    # build Vandermonde of x*p columns to check Xt@V equals data of x*monomials (only for cols with deg+1<=deg): skip -> return Xt@V
    return None
