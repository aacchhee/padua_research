# Independent CC Gram on Pi_{N-1}, orthonormal Legendre basis (auditor code).
import sys, json, numpy as np
from mpmath import mp
def cc_weights(N):
    # Waldvogel/Trefethen-style formula, written from scratch
    th=np.pi*np.arange(N+1)/N
    w=np.zeros(N+1)
    c=np.ones(N+1); c[0]=c[N]=0.5
    for k in range(N+1):
        s=1.0
        for j in range(1,N//2+1):
            b=1.0 if 2*j==N else 2.0
            s-=b*np.cos(2*j*th[k])/(4*j*j-1)
        w[k]=2*c[k]*s/N
    return np.cos(th),w
def legendre_on(x,n):
    P=np.zeros((n,len(x))); P[0]=1
    if n>1: P[1]=x
    for k in range(1,n-1):
        P[k+1]=((2*k+1)*x*P[k]-k*P[k-1])/(k+1)
    return P*np.sqrt((2*np.arange(n)+1)/2)[:,None]
out=[]
for N in map(int,sys.argv[1:]):
    x,w=cc_weights(N)
    # exactness check on T_m, m<=N
    m=np.arange(N+1); Tm=np.cos(np.outer(m,np.arccos(np.clip(x,-1,1))))
    mu=np.where(m%2==0,2/(1-m.astype(float)**2+(m%2)),0.0)
    exact_err=float(np.max(np.abs(Tm@w-mu)))
    P=legendre_on(x,N)
    G=(P*w)@P.T
    ev=np.linalg.eigvalsh(G)
    out.append(dict(N=N,min=float(ev[0]),max=float(ev[-1]),min_w=float(w.min()),exact_err=exact_err))
    print(out[-1],flush=True)
