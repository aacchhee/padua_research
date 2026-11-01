"""Corner gap Lc - max lambda_n on strips at distance i cells (i = 0..5) from
the vertical edge x=+1 (theta in [i pi/n,(i+1) pi/n]) and from the horizontal
edge y=+1 (phi in [i pi/(n+1),(i+1) pi/(n+1)]), maximised over the whole other
coordinate (8x8 grid per cell + Nelder-Mead from the best point; MEASURED)."""
import numpy as np, sys
from maj import setup, lam
from scipy.optimize import minimize
for n in [int(v) for v in sys.argv[1:]]:
    S=setup(n)
    Lc=max(lam(n,[0.0],[np.pi],S)[0][0],lam(n,[np.pi],[0.0],S)[0][0])
    hx,hy=np.pi/n,np.pi/(n+1)
    rows=[]
    for orient in ("vertical x=+1","horizontal y=+1"):
        res=[]
        for i in range(6):
            if orient.startswith("v"):
                A=np.linspace(i*hx,(i+1)*hx,8); B=np.linspace(0,np.pi,8*(n+1)+1)
            else:
                A=np.linspace(0,np.pi,8*n+1); B=np.linspace(i*hy,(i+1)*hy,8)
            X,Y=np.meshgrid(A,B,indexing='ij'); l=lam(n,X.ravel(),Y.ravel(),S)[0]
            k=l.argmax(); x0=(X.ravel()[k],Y.ravel()[k])
            lo=(i*hx,0) if orient.startswith("v") else (0,i*hy); hi=((i+1)*hx,np.pi) if orient.startswith("v") else (np.pi,(i+1)*hy)
            f=lambda z: 1e3 if (z[0]<lo[0] or z[0]>hi[0] or z[1]<lo[1] or z[1]>hi[1]) else -lam(n,[z[0]],[z[1]],S)[0][0]
            r=minimize(f,x0,method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-11})
            v=max(-r.fun,l.max()); zz=r.x if -r.fun>=l.max() else x0
            res.append("%d:%.3f@(%.2f,%.2f)"%(i,Lc-v,zz[0]/np.pi,zz[1]/np.pi))
        rows.append(orient+"  "+"  ".join(res))
    print("n=%d Lc=%.4f  [gap@(theta/pi,phi/pi) per strip index]"%(n,Lc)); [print("   ",r) for r in rows]
