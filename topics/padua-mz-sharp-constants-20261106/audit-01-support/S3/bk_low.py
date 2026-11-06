import numpy as np
from scipy.special import j0, roots_legendre
from scipy.linalg import eigh
for order in (128,):
    z,w=roots_legendre(order); a,wa=(z+1)/2,w/2
    aa=np.repeat(a,order); bb=((1-a[:,None])*a[None,:]).ravel()
    ww=(wa[:,None]*wa[None,:]*a[:,None]*(1-a[:,None])**2*a[None,:]).ravel()
    for K in (16,32,64,128):
        nodes=[(j,k) for j in range(K) for k in range(K//(1+j)) if (j+k)%2==0 and (1+j)*(1+k)<=K]
        F=np.array([j0(np.pi*j*aa)*j0(np.pi*k*bb) for j,k in nodes])*np.sqrt(ww)
        G=F@F.T; c=np.array([-16*(.5 if j==0 else 1)*(.5 if k==0 else 1)*(-1)**j for j,k in nodes])
        ev,V=eigh(G); keep=ev>ev[-1]*1e-13; r=np.sqrt(ev[keep]); V=V[:,keep]
        H=(V.T*c)@V*r[:,None]*r[None,:]; s=eigh(H,eigvals_only=True)
        print(K,len(nodes),'low',np.round(s[:4],6),'high',np.round(s[-3:],6))
