"""G2: true local corner remainder K = sup (lambda_n(z_n(alpha,beta)) - a Lambda_c)/(rho^2 log(n+1)), rho<=1/64, at the corner (-1,-1). Pilot gate script (float64, MEASURED). Uses the PD-T206 evaluator maj.py of topic padua-argmax-alln-20261101."""
import sys, numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'padua-argmax-alln-20261101', 'code'))
from maj import setup, lam
for n in [int(v) for v in sys.argv[1:]]:
    S=setup(n); m=n+1
    Lc=lam(n,[np.pi],[np.pi],S)[0][0]
    best=-1e9; arg=None; rows=[]
    for rho in [1/64, 1/256, 1/1024]:
        for f in np.linspace(0,1,21):
            a_,b_=f*rho,(1-f)*rho
            th=np.pi-a_/n; ph=np.pi-b_/m
            l=lam(n,[th],[ph],S)[0][0]
            a=(np.cos(a_)+np.cos(b_))/2
            K=(l-a*Lc)/(rho**2*np.log(n+1))
            if K>best: best,arg=K,(rho,f)
            if f in (0.0,0.5,1.0): rows.append((rho,f,(l-Lc)/rho**2,K))
    print("n=%d Lc=%.4f  K_true=max (lam-a*Lc)/(rho^2 log(n+1)) = %.4f at rho=%.5f f=%.2f ; axis budget Lc/(4log(n+1))=%.3f (diagonal: K and budget both halve)"%(n,Lc,best,arg[0],arg[1],Lc/(4*np.log(n+1))))
    for r in rows: print("    rho=%.5f f=%.1f (lam-Lc)/rho^2=%.4f K=%.4f"%r)
