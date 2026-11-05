"""G3: true constant C = sup (S_n - a Lambda_c)/log(n+1) over |alpha|+|beta|<=pi (61x61 phase grid) and the far-from-coset majorant margin sup_{rho>=0.5}(S_n - Lambda_c). Pilot gate script (float64, MEASURED). Uses the PD-T206 evaluator maj.py of topic padua-argmax-alln-20261101."""
import sys, numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'padua-argmax-alln-20261101', 'code'))
from maj import setup, lam
for n in [int(v) for v in sys.argv[1:]]:
    S=setup(n); m=n+1
    Lc=lam(n,[np.pi],[np.pi],S)[0][0]
    A=np.linspace(-np.pi,np.pi,61); X,Y=np.meshgrid(A,A,indexing='ij'); mask=(np.abs(X)+np.abs(Y))<=np.pi+1e-12
    a=(np.cos(X)+np.cos(Y))/2
    _,Sv=lam(n,(np.pi+X[mask]/n),(np.pi+Y[mask]/m),S)
    C=(Sv-a[mask]*Lc)/np.log(n+1); i=C.argmax()
    D=Sv-Lc
    far=(np.abs(X[mask])+np.abs(Y[mask]))>=0.5
    print("n=%d Lc=%.3f  C_true=sup(S-a*Lc)/log(n+1)=%.4f at (a,b)=(%.2f,%.2f);  sup S-Lc=%.2e; sup_{rho>=0.5}(S-Lc)=%.3f"%(n,Lc,C[i],X[mask][i],Y[mask][i],D.max(),D[far].max()))
