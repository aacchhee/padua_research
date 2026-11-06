# Independent B_K spectrum from definition via Duffy-collapsed Gauss-Legendre. No repo imports.
import numpy as np, json, sys, time
from numpy.polynomial.legendre import leggauss
from scipy.special import j0
ref=json.load(open(sys.argv[1]))
refr={}
for run in ref['runs']:
    for r in run['results']: refr.setdefault(r['cut'],[]).append(r)
def grid(q,collapse):
    x,wx=leggauss(q); u=(x+1)/2; wu=wx/2
    U,V=np.meshgrid(u,u,indexing='ij'); WU=np.outer(wu,wu)
    if collapse=='a': a=U; b=(1-U)*V
    else: b=U; a=(1-U)*V
    W=WU*(1-U)*a*b  # Jacobian (1-U) times weight a b
    return a.ravel(),b.ravel(),W.ravel()
out=[]
for q in [int(s) for s in sys.argv[3].split(',')]:
  for col in ['a','b']:
    a,b,W=grid(q,col); sw=np.sqrt(W)
    for K in [16,32,64,128]:
        t=time.time()
        idx=[(j,k) for j in range(K) for k in range(K) if (1+j)*(1+k)<=K and (j+k)%2==0]
        js=sorted({j for j,_ in idx}); ks=sorted({k for _,k in idx})
        Ja={j:j0(np.pi*j*a)*sw for j in js}; Jb={k:j0(np.pi*k*b) for k in ks}
        Psi=np.array([Ja[j]*Jb[k] for j,k in idx])
        G=Psi@Psi.T
        c=np.array([-16*(0.5 if j==0 else 1)*(0.5 if k==0 else 1)*(-1)**j for j,k in idx])
        d,U=np.linalg.eigh(G); d=np.clip(d,0,None); H=(np.sqrt(d)[:,None]*U.T)@(c[:,None]*U*np.sqrt(d)[None,:])
        ev=np.linalg.eigvalsh((H+H.T)/2)
        r=refr[K]
        rec=dict(order=q,collapse=col,K=K,count=len(idx),gram_min=d[0],gram_max=d[-1],lam_min=ev[0],lam_max=ev[-1],
                 ref_lam_min=[x['lambda_min'] for x in r],ref_lam_max=[x['lambda_max'] for x in r],ref_nodes=[x['nodes'] for x in r],
                 absdiff_min=max(abs(ev[0]-x['lambda_min']) for x in r),absdiff_max=max(abs(ev[-1]-x['lambda_max']) for x in r),sec=time.time()-t)
        out.append(rec); print(rec,flush=True)
json.dump(out,open(sys.argv[2],'w'),indent=1,default=float)
