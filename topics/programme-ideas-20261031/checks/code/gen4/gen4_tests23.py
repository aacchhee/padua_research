import numpy as np, sys, time
from numpy.polynomial import legendre as Lg
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
t=time.time()
def leg_basis(X,Y,k):
    idx=[(i,j) for d in range(k+1) for i in range(d,-1,-1) for j in [d-i]]
    Px=[np.ones_like(X),X]; Py=[np.ones_like(Y),Y]
    for m in range(2,k+1):
        Px.append(((2*m-1)*X*Px[-1]-(m-1)*Px[-2])/m); Py.append(((2*m-1)*Y*Py[-1]-(m-1)*Py[-2])/m)
    return np.array([np.sqrt((2*i+1)*(2*j+1))*Px[i]*Py[j] for (i,j) in idx]).T, idx   # orthonormal for uniform prob. measure on square (dx dy/4)
# Deterministic design: Pad_{n'} nodes with Christoffel-type weights for Legendre Pi_n; Gram condition number; compare n'=n+1 (M~N), n'=2n (M~4N)
for n in (10,20,40):
    for ratio in (1,2,3):
        np_=ratio*n + (1 if ratio==1 else 0)
        P,wc=padua(np_)
        V,idx=leg_basis(P[:,0],P[:,1],n)
        # (i) Padua cubature weights (Chebyshev measure) reweighted by 1/density: w = wc * (pi^2/4) sqrt(1-x^2) sqrt(1-y^2)  -> approximates uniform measure
        wu = wc*(np.pi**2/4)*np.sqrt(1-P[:,0]**2)*np.sqrt(1-P[:,1]**2)
        G=V.T@(wu[:,None]*V); ev=np.linalg.eigvalsh(G)
        # (ii) Christoffel weights: w = 1/K_n^{Leg}(B,B) normalised
        K=np.sum(V**2,axis=1); wk=1/K; wk/=wk.sum(); Gk=V.T@(wk[:,None]*V); evk=np.linalg.eigvalsh(Gk)
        # (iii) exact-cubature weights for Chebyshev basis: cond of Chebyshev Gram (for reference, Chebyshev measure)
        Vc,_=cheb_basis(P[:,0],P[:,1],n); Gc=Vc.T@(wc[:,None]*Vc); evc=np.linalg.eigvalsh(Gc)
        print('n',n,"n'",np_,'M/N %.2f'%(len(P)/len(idx)),'| uniform-target: density-reweighted Padua lam_min %.3f lam_max %.3f'%(ev.min(),ev.max()),'| Christoffel-weighted lam_min %.3f lam_max %.3f'%(evk.min(),evk.max()),'| Chebyshev-target exact: lam_min %.3f lam_max %.3f'%(evc.min(),evc.max()),'time %.0f'%(time.time()-t))
