# Independent Clenshaw-Curtis Lebesgue extremal ratio check. No repo imports.
import numpy as np, json, time, sys
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh
def cc_weights(N):
    k=np.arange(N+1); th=k*np.pi/N
    w=np.zeros(N+1)
    for kk in range(N+1):
        s=0.0
        for j in range(1,N//2+1):
            b=1.0 if 2*j==N else 2.0
            s+=b/(4*j*j-1)*np.cos(2*j*th[kk])
        c=1.0 if kk in (0,N) else 2.0
        w[kk]=c/N*(1-s)
    return np.cos(th),w
def legn(n,x):  # orthonormal Legendre P_0..P_{n-1} at x, three-term recurrence
    P=np.zeros((n,len(x))); P[0]=1.0
    if n>1: P[1]=x
    for i in range(1,n-1): P[i+1]=((2*i+1)*x*P[i]-i*P[i-1])/(i+1)
    return P*np.sqrt((2*np.arange(n)+1)/2)[:,None]
ref={r[0]:r for r in json.load(open(sys.argv[1]))['rows']}
out=[]
for N in [100,101,200,201,400,401,800,801]:
    t=time.time(); x,w=cc_weights(N); n=N  # degree N-1 -> N basis functions
    # moment check: integral of T_j for j<=N
    Tj=np.cos(np.outer(np.arange(N+1),np.arccos(np.clip(x,-1,1))))
    mom=np.array([2/(1-j*j) if j%2==0 else 0.0 for j in range(N+1)])
    merr=np.max(np.abs(Tj@w-mom))
    gx,gw=leggauss(N+2)   # exact for degree 2N+1 >= 2(N-1)
    Pg=legn(n,gx); G=(Pg*gw)@Pg.T
    P=legn(n,x); A=(P*w)@P.T
    ev=eigh(A,G,eigvals_only=True)
    r=ref[N]; out.append(dict(N=N,weight_sum=w.sum(),moment_err=merr,gram_offdiag=np.max(np.abs(G-np.eye(n))),
        lam_min=ev[0],lam_max=ev[-1],ref_min=r[1],ref_max=r[2],
        rel_min=abs(ev[0]-r[1])/r[1],rel_max=abs(ev[-1]-r[2])/r[2],sec=time.time()-t))
    print(out[-1],flush=True)
json.dump(out,open(sys.argv[2],'w'),indent=1)
