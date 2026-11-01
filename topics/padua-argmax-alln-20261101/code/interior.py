"""Maximum of lambda_n over central angle boxes [pi/4,3pi/4]^2 and [pi/8,pi/2]^2 (grid ~6 points per pi/n, then Nelder-Mead) versus the corner value (float64, MEASURED)."""
import numpy as np, maj, sys
from scipy.optimize import minimize
for n in [int(v) for v in sys.argv[1:]]:
    S=maj.setup(n)
    Lc=maj.lam(n,[np.pi/n*0+np.pi],[0.0],S)[0][0]; Lc=max(Lc,maj.lam(n,[0.0],[np.pi],S)[0][0])
    res=[]
    for lo,hi in [(np.pi/4,3*np.pi/4),(np.pi/8,np.pi/2)]:
        M=int(6*n*(hi-lo)/np.pi)+2
        T=np.linspace(lo,hi,M); X,Y=np.meshgrid(T,T,indexing='ij')
        l,m=maj.lam(n,X.ravel(),Y.ravel(),S)
        i=l.argmax(); f=lambda z:-maj.lam(n,[z[0]],[z[1]],S)[0][0]
        r=minimize(f,(X.ravel()[i],Y.ravel()[i]),method='Nelder-Mead')
        res.append(-r.fun)
    print(n,"Lc %.4f"%Lc,"central [pi/4,3pi/4]^2 max %.4f gap %.4f"%(res[0],Lc-res[0]),"| [pi/8,pi/2]^2 max %.4f gap %.4f"%(res[1],Lc-res[1]), "gap/log n %.3f"%((Lc-res[0])/np.log(n)))
