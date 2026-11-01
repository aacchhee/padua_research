import numpy as np
def mats(N):
    k=np.arange(N+1); th=k*np.pi/N
    cc=np.ones(N+1); cc[0]=cc[-1]=2
    A=(2/N)*np.cos(np.outer(k,th))/np.outer(cc,cc)
    h=np.zeros(2*N+1); ev=np.arange(0,2*N+1,2); h[ev]=2/(1-ev.astype(float)**2)
    Gam=0.5*(h[np.add.outer(k,k)]+h[np.abs(np.subtract.outer(k,k))])
    Mc=A.T@Gam@A; w=h[:N+1]@A; s=1/np.sqrt(w)
    return s[:,None]*(Mc-np.diag(w))*s[None,:]
def offrank(A,tol):
    n=A.shape[0]; r=[]; nrm=np.linalg.norm(A,2)
    def rec(lo,hi,d):
        if hi-lo<64 or d>4: return
        mid=(lo+hi)//2; s=np.linalg.svd(A[lo:mid,mid:hi],compute_uv=False)
        r.append(int((s>tol*nrm).sum())); rec(lo,mid,d+1); rec(mid,hi,d+1)
    rec(0,n,0); return r
for N in [256,512,1024,2048]:
    Mt=mats(N); print(N,'node-order Mt off-diag ranks @1e-12 (top..):',offrank(Mt,1e-12)[:7],' @1e-8:',offrank(Mt,1e-8)[:3])
