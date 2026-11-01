"""Cell-wise maxima of lambda_n along the four edges versus the corner value
(float64 grid with 24 points per cell + golden refinement; MEASURED).
Prints, for each edge, the corner gap Lc - (cell max) at macroscopic positions."""
import numpy as np, sys
from maj import setup, lam
from scipy.optimize import minimize_scalar
for n in [int(v) for v in sys.argv[1:]]:
    S=setup(n)
    Lc=max(lam(n,[0.0],[np.pi],S)[0][0],lam(n,[np.pi],[0.0],S)[0][0])
    out=[]
    for name,fix,var_steps in [("x=+1",(0,0.0),n+1),("x=-1",(0,np.pi),n+1),("y=+1",(1,0.0),n),("y=-1",(1,np.pi),n)]:
        h=np.pi/var_steps; gaps=[]
        for c in range(var_steps):
            g=np.linspace(c*h,(c+1)*h,25)
            if fix[0]==0: X=np.full_like(g,fix[1]); Y=g
            else: X=g; Y=np.full_like(g,fix[1])
            v=lam(n,X,Y,S)[0]; i=v.argmax()
            f=(lambda t: -lam(n,[fix[1]],[t],S)[0][0]) if fix[0]==0 else (lambda t: -lam(n,[t],[fix[1]],S)[0][0])
            r=minimize_scalar(f,bounds=(g[max(i-1,0)],g[min(i+1,24)]),method='bounded',options={'xatol':1e-12})
            gaps.append(Lc+r.fun)
        gaps=np.array(gaps)
        # exclude the corner cells themselves (gap 0 at the non-node corner)
        inner=gaps[1:-1]
        pos=[0.1,0.25,0.5]
        prof=" ".join("%.3f"%inner[int(p*(len(inner)-1))] for p in pos)
        out.append("%s min_inner_gap=%.4f at cell %d/%d; gaps at 10/25/50%%: %s; first 3 cells: %s"%(name,inner.min(),inner.argmin()+1,var_steps,prof," ".join("%.3f"%x for x in gaps[:3])))
    print("n=%d Lc=%.5f"%(n,Lc)); [print("   ",o) for o in out]
