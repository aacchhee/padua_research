# High-precision Rayleigh lower bounds for Lambda_edge from the closed-form Gram (auditor code).
import numpy as np, mpmath as mp, sys
from scipy.special import sici
from scipy.linalg import eigh
sys.path.insert(0,sys.path[0]); from fixedJ_check import model
mp.mp.dps=40
def mp_model(J):
    a=[mp.pi*j for j in range(1,J+1)]; s=[(-1)**j for j in range(1,J+1)]
    d=[2*mp.quad(lambda v: mp.sin(v)**2/v,[0,x]) if False else mp.euler+mp.log(2*x)-mp.ci(2*x) for x in a]
    Si2=[mp.si(2*x) for x in a]; Si=[mp.si(x) for x in a]
    C=mp.matrix(J,J)
    for p in range(J):
        for q in range(J):
            C[p,q]=2*(Si2[p]*a[p]+d[p]) if p==q else 2*s[p]*s[q]*(a[p]**2*d[q]-a[q]**2*d[p])/(a[p]**2-a[q]**2)
    om=[2*(s[p]+a[p]*Si[p]) for p in range(J)]
    return C,om,s
for J in [int(x) for x in sys.argv[1:]]:
    C,D=model(J); w,V=eigh(D,C); u=V[:,-1]
    print("J",J,"float lam",repr(w[-1]),"cond C",np.linalg.cond(C), "min eig C", np.linalg.eigvalsh(C)[0],flush=True)
    Cm,om,s=mp_model(J)
    um=[mp.mpf(float(x)) for x in u]
    num=(sum(s[p]*um[p] for p in range(J)))**2*4+sum(om[p]*um[p]**2 for p in range(J))
    den=mp.mpf(0)
    for p in range(J):
        row=mp.fsum(Cm[p,q]*um[q] for q in range(J)); den+=um[p]*row
    print("  mp Rayleigh quotient (lower bound for lambda_J, hence Lambda_edge):", mp.nstr(num/den,20),flush=True)
