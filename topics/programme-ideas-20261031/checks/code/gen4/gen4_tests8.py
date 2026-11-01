import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# (A) Lambda(Pad_n) at the corner (1,1) exactly (corner is argmax per mesh runs) for n up to 400 via closed-form Lagrange basis, O(N) per n
def lam_corner(n, pt=(1.0,1.0)):
    P,w=padua(n); V,_=cheb_basis(P[:,0],P[:,1],n); Vg,_=cheb_basis(np.array([pt[0]]),np.array([pt[1]]),n)
    Tn=lambda x: np.cos(n*np.arccos(np.clip(x,-1,1)))
    L = w*((Vg@V.T).ravel() - Tn(pt[0])*Tn(P[:,0]))
    return np.sum(np.abs(L))
ns=[10,20,40,80,160]; L=[lam_corner(n) for n in ns]
for n,l in zip(ns,L): print('n',n,'Lambda(corner) %.5f'%l,' minus (4/pi^2)log^2 n = %.4f'%(l-(4/np.pi**2)*np.log(n)**2))
A=np.c_[np.log(ns)**2,np.log(ns),np.ones(len(ns))]; coef=np.linalg.lstsq(A,L,rcond=None)[0]; print('free fit a,b,c =',coef,' (4/pi^2 = %.4f)'%(4/np.pi**2))
A2=np.c_[np.log(ns),np.ones(len(ns))]; coef2=np.linalg.lstsq(A2,np.array(L)-(4/np.pi**2)*np.log(ns)**2,rcond=None)[0]; print('fixed-a fit b,c =',coef2, 'resid',np.max(np.abs(A2@coef2-(np.array(L)-(4/np.pi**2)*np.log(ns)**2))))
# compare: also other corner (-1,1) and (1,-1)
print('corners n=80:',[round(lam_corner(80,pt),4) for pt in [(1,1),(-1,1),(1,-1),(-1,-1)]])
# (B) Fekete-stationarity gradient scaling: max |grad log det| per node, bulk vs near-boundary, n=8..32
def grad(n):
    P,w=padua(n); V,_=cheb_basis(P[:,0],P[:,1],n); Tn=lambda x: np.cos(n*np.arccos(np.clip(x,-1,1)))
    h=1e-6; G=np.zeros((len(P),2))
    for d in range(2):
        for sgn in (1,-1):
            S=P.copy(); S[:,d]+=sgn*h; Vs,_=cheb_basis(S[:,0],S[:,1],n)
            G[:,d]+=sgn*w*(np.sum(Vs*V,axis=1)-Tn(S[:,0])*Tn(P[:,0]))/(2*h)
    return P,G
for n in (8,12,16,24,32):
    P,G=grad(n); r=np.maximum(np.abs(P[:,0]),np.abs(P[:,1])); interior=r<0.999999
    layer = interior & (r>np.cos(1.5*np.pi/n))   # within ~1 Chebyshev spacing of boundary
    bulk = interior & ~layer
    print('n',n,'max|G| layer %.3e'%np.abs(G[layer]).max(),'max|G| bulk %.3e'%np.abs(G[bulk]).max(),'rms|G| bulk %.3e'%np.sqrt(np.mean(G[bulk]**2)), 'n*max bulk %.3f'%(n*np.abs(G[bulk]).max()), 'n^2*max bulk %.3f'%(n*n*np.abs(G[bulk]).max()))
