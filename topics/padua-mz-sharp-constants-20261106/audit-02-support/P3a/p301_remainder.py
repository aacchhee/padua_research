# Numerical operator norm of P3-01's E: l2(1/k) on support {k0..k0+n-1} -> L2(dt/t)
import numpy as np, json, sys, time
xg,wg=np.polynomial.legendre.leggauss(10); xg=(xg+1)/2; wg=wg/2
def norm_E(k0,n,tmaxfac=24):
    k=np.arange(k0,k0+n,dtype=float); kmax=k[-1]
    G=np.zeros((n,n))
    # t in (0,1): substitute fine grid (log) ; then unit cells to tmax; then tail log-grid with sin^2 kept
    def add(t,w):
        s=np.sin(np.pi*t)
        T=t[:,None]; K=k[None,:]
        B=T*T/(K*(T*T-K*K))-(K<T)/K
        Bm=(s[:,None]*B)*np.sqrt(K)   # column scaling: h=g/sqrt(k) => g=sqrt(k) h
        Bm*=np.sqrt(w/t)[:,None]
        nonlocal_G[0]+=Bm.T@Bm
    nonlocal_G=[G]
    # (0,1) cells in log scale
    edges=np.concatenate([np.geomspace(1e-6,1,60)])
    tt=[];ww=[]
    a=0.0
    for b in edges:
        tt.append(a+(b-a)*xg); ww.append((b-a)*wg); a=b
    t=np.concatenate(tt); w=np.concatenate(ww); add(t,w)
    tmax=int(tmaxfac*kmax)+2
    chunk=2000
    for m0 in range(1,tmax,chunk):
        m=np.arange(m0,min(m0+chunk,tmax),dtype=float)
        t=(m[:,None]+xg[None,:]).ravel(); w=np.tile(wg,len(m)); add(t,w)
    # tail: log cells of width ~ unit-aligned? use cells [a,b] with integer endpoints, 40 GL pts, geometric
    e=np.unique(np.round(np.geomspace(tmax,tmax*1e4,400)))
    x40,w40=np.polynomial.legendre.leggauss(40); x40=(x40+1)/2; w40=w40/2
    # for wide cells sin^2 oscillates; use many unit-subcells sampled? approximate sin^2 by 1/2 (tail is tiny, ~t^-5)
    for a,b in zip(e[:-1],e[1:]):
        t=a+(b-a)*x40; w=(b-a)*w40
        T=t[:,None]; K=k[None,:]
        B=(T*T/(K*(T*T-K*K))-(K<T)/K)*np.sqrt(K)*np.sqrt(0.5*w/t)[:,None]
        nonlocal_G[0]+=B.T@B
    G=nonlocal_G[0]
    lam=np.linalg.eigvalsh(G)[-1]
    return np.sqrt(lam)
res=[]
for (k0,n) in [(1,50),(1,200),(1,800),(100,200),(1000,200),(5000,200),(1,1500)]:
    t0=time.time(); v=norm_E(k0,n); res.append(dict(k0=k0,n=n,norm=v,claimed=40)); print(res[-1],round(time.time()-t0,1),flush=True)
json.dump(res,open('p301_remainder.json','w'),indent=1)
