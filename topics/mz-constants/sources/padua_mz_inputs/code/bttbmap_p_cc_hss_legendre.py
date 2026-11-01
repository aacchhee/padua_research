import numpy as np
from numpy.polynomial import legendre as L
def offrank(A,tol):
    n=A.shape[0]; r=[]
    def rec(lo,hi,d):
        if hi-lo<64 or d>4: return
        mid=(lo+hi)//2; B=A[lo:mid,mid:hi]; s=np.linalg.svd(B,compute_uv=False)
        r.append(int((s>tol*np.linalg.norm(A,2)).sum())); rec(lo,mid,d+1); rec(mid,hi,d+1)
    rec(0,n,0); return max(r)
for N in [256,512,1024]:
    k=np.arange(N+1); x=np.cos(k*np.pi/N)
    # CC weights via Lagrange/DCT
    cc=np.ones(N+1); cc[0]=cc[-1]=2; th=k*np.pi/N
    A=(2/N)*np.cos(np.outer(k,th))/np.outer(cc,cc); h=np.zeros(N+1); ev=np.arange(0,N+1,2); h[ev]=2/(1-ev.astype(float)**2); w=h@A
    n=N-1; V=np.array([L.legval(x,[0]*j+[1])*np.sqrt((2*j+1)/2) for j in range(n+1)]).T  # orthonormal Legendre
    G=V.T@(w[:,None]*V)
    # even/odd split (parity) then HSS off-diagonal rank of each block, natural degree order
    for par in (0,1):
        Gp=G[par::2,par::2]
        print(N,'parity',par,'size',Gp.shape[0],'offrank@1e-12 =',offrank(Gp-np.eye(Gp.shape[0]),1e-12),
              ' lmin,lmax=',np.round(np.linalg.eigvalsh(Gp)[[0,-1]],6))
