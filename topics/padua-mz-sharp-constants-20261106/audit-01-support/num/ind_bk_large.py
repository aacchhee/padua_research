# Extension: B_K at K beyond committed range, chunked Gram accumulation. No repo imports.
import numpy as np, json, sys, time
from numpy.polynomial.legendre import leggauss
from scipy.special import j0
out=[]
for K in [int(s) for s in sys.argv[2].split(',')]:
  for q in [int(s) for s in sys.argv[3].split(',')]:
    t=time.time(); c0=time.process_time()
    idx=[(j,k) for j in range(K) for k in range(K) if (1+j)*(1+k)<=K and (j+k)%2==0]
    J=np.array([j for j,_ in idx]); Kk=np.array([k for _,k in idx])
    x,wx=leggauss(q); u=(x+1)/2; wu=wx/2
    G=np.zeros((len(idx),len(idx)))
    for i in range(q):   # a=u_i fixed, b=(1-u_i)v
        a=u[i]; b=(1-a)*u; W=wu[i]*wu*(1-a)*a*b
        Ja=j0(np.pi*J*a)                      # per row scalar
        Jb=j0(np.pi*np.outer(Kk,b))*np.sqrt(W) # rows x q
        P=Ja[:,None]*Jb; G+=P@P.T
    c=np.array([-16*(0.5 if j==0 else 1)*(0.5 if k==0 else 1)*(-1)**j for j,k in idx])
    d,U=np.linalg.eigh(G); d=np.clip(d,0,None); H=(np.sqrt(d)[:,None]*U.T)@(c[:,None]*U*np.sqrt(d)[None,:])
    ev=np.linalg.eigvalsh((H+H.T)/2)
    rec=dict(K=K,order=q,count=len(idx),gram_min=d[0],lam_min=ev[0],lam_max=ev[-1],wall=time.time()-t,cpu=time.process_time()-c0)
    out.append(rec); print(rec,flush=True)
json.dump(out,open(sys.argv[1],'w'),indent=1,default=float)
