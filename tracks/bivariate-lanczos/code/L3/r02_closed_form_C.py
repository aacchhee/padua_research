"""R02 (MEASURED): test the closed-form candidate C1 = sum_{j=1}^{n} (e_j e_j^T - (e_{j-1}e_{j+1}^T + e_{j+1}e_{j-1}^T)/2),
i.e. p = sum_j (q_j^2 - q_{j-1} q_{j+1}) with the normalised Padua generators of PD-T?bivariate-lanczos-claude-309(c);
prints min over Padua nodes of lambda_min(G_i^T C1 G_i). Usage: python3 r02_closed_form_C.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from numpy.polynomial import chebyshev as Ch
from l3lib import padua
def cT(k): c=np.zeros(k+1); c[k]=1; return c
def T(k,t): return Ch.chebval(t,cT(k))
def dT(k,t): return Ch.chebval(t,Ch.chebder(cT(k))) if k>0 else 0*t
def lc(k): return 1.0 if k==0 else 2.0**(k-1)
def grads(n, z):
    x,y=z; G=[]
    for m in range(n+1):
        gx=dT(n-m,x)*T(m,y)-dT(m,x)*T(n+1-m,y)
        gy=T(n-m,x)*dT(m,y)-T(m,x)*dT(n+1-m,y)
        lam=lc(m)*lc(n+1-m)
        G.append([-gx/lam,-gy/lam])
    # omega=(x^2-1)U_{n-1}(x), U_{n-1}=T_n'/n ; derivative
    U=Ch.chebder(cT(n))/n
    om=Ch.chebmul(Ch.chebsub(Ch.chebmul([0,1],[0,1]),[1]),U)
    G.append([Ch.chebval(x,Ch.chebder(om))/2.0**(n-1),0.0])
    return np.array(G)
def test(n, C):
    worst=np.inf
    for z in padua(n):
        G=grads(n,z); H=G.T@C@G
        worst=min(worst,np.linalg.eigvalsh(0.5*(H+H.T))[0])
    return worst
for n in range(2,13):
    m=n+2
    C1=np.zeros((m,m))
    for j in range(1,m-1):
        C1[j,j]+=1; C1[j-1,j+1]-=0.5; C1[j+1,j-1]-=0.5
    # check Hankel-perp
    hp=max(abs(sum(C1[j,k] for j in range(m) for k in range(m) if j+k==s)) for s in range(2*m-1))
    print(f"n={n}: C1 hankel-perp resid {hp:.0e}  min eig over nodes of G^T C1 G = {test(n,C1):+.3e}")
