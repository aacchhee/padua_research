# Variant: singular values of diag(sqrt w) P^T (orthonormal Legendre), plus mpmath high precision at small N.
import numpy as np, json, sys, time, mpmath as mp
sys.path.insert(0,sys.argv[0].rsplit('/',1)[0]); from ind_cc import cc_weights, legn  # own code
ref={r[0]:r for r in json.load(open(sys.argv[1]))['rows']}
res=[]
for N in [100,101,200,201,400,401,800,801]:
    x,w=cc_weights(N); B=(legn(N,x)*np.sqrt(w)).T
    s=np.linalg.svd(B,compute_uv=False); lo,hi=s[-1]**2,s[0]**2; r=ref[N]
    res.append(dict(N=N,svd_min=lo,svd_max=hi,rel_min=abs(lo-r[1])/r[1],rel_max=abs(hi-r[2])/r[2])); print(res[-1],flush=True)
mp.mp.dps=40
for N in [100,101]:
    t=time.time()
    th=[mp.pi*k/N for k in range(N+1)]; x=[mp.cos(a) for a in th]
    w=[]
    for k in range(N+1):
        s=mp.mpf(0)
        for j in range(1,N//2+1):
            s+=(1 if 2*j==N else 2)*mp.cos(2*j*th[k])/(4*j*j-1)
        w.append((1 if k in (0,N) else 2)*(1-s)/N)
    # orthonormal Legendre values
    P=mp.matrix(N,N+1)
    for k in range(N+1):
        p0,p1=mp.mpf(1),x[k]; vals=[p0,p1]
        for i in range(1,N-1):
            p0,p1=p1,((2*i+1)*x[k]*p1-i*p0)/(i+1); vals.append(p1)
        for i in range(N): P[i,k]=vals[i]*mp.sqrt(mp.mpf(2*i+1)/2)
    A=mp.matrix(N,N)
    for i in range(N):
        for j in range(i,N):
            v=mp.fsum(w[k]*P[i,k]*P[j,k] for k in range(N+1)); A[i,j]=v; A[j,i]=v
    E=mp.eigsy(A,eigvals_only=True); E=sorted(E)
    r=ref[N]; d=dict(N=N,mp_min=mp.nstr(E[0],25),mp_max=mp.nstr(E[-1],25),rel_min=float(abs(E[0]-r[1])/r[1]),rel_max=float(abs(E[-1]-r[2])/r[2]),sec=time.time()-t)
    res.append(d); print(d,flush=True)
json.dump(res,open(sys.argv[2],'w'),indent=1,default=float)
