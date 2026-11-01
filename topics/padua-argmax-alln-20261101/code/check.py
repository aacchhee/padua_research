"""Check the kernel formula of maj.py against direct monomial-Chebyshev Vandermonde inversion (float64, MEASURED)."""
import numpy as np
from maj import setup
def nodes(n):
    P=[];w=[]
    th,ph,W,C,a=setup(n)
    for j in range(n+1):
        for k in range(n+2):
            if (j+k)%2==0: P.append((np.cos(th[j]),np.cos(ph[k]))); w.append(W[j,k])
    return np.array(P),np.array(w)
def vand(n,P):
    cols=[(i,d-i) for d in range(n+1) for i in range(d+1)]
    T=lambda m,x: np.cos(m*np.arccos(np.clip(x,-1,1)))
    return np.array([[T(i,p[0])*T(j,p[1]) for (i,j) in cols] for p in P])
for n in [3,4]:
    P,w=nodes(n); V=vand(n,P); Vi=np.linalg.inv(V)
    def lamv(x): 
        v=vand(n,np.array([x]))[0]; return np.abs(v@Vi).sum()
    print(n,len(P),w.sum(), [round(lamv(c),6) for c in [(1,1),(1,-1),(-1,1),(-1,-1)]])
    # compare kernel formula
    th,ph,W,C,a=setup(n)
    import maj
    for (t,p) in [(0.3,1.1),(0,np.pi),(np.pi,0),(np.pi,np.pi)]:
        l,m=maj.lam(n,[t],[p],setup(n)); print('  ',t,p,'kernel',round(l[0],6),'vand',round(lamv((np.cos(t),np.cos(p))),6))
print(17/6+2/3*np.sqrt(2))
