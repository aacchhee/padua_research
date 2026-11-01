import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# 1D analogue: Chebyshev-Lobatto nodes cos(j pi/n), j=0..n, equal weights vs CC (endpoint half) weights; Christoffel ratio at x=1 and at x=0 for degree k=theta n
def cheb1(X,k):
    T=[np.ones_like(X),X]
    for m in range(2,k+1): T.append(2*X*T[-1]-T[-2])
    return np.array([(np.sqrt(2) if i>0 else 1)*T[i] for i in range(k+1)]).T
def ratio1d(n,th,x):
    xs=np.cos(np.arange(n+1)*np.pi/n); w=np.ones(n+1)/(n+1)
    k=int(round(th*n)); V=cheb1(xs,k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
    Vg=cheb1(np.array([x]),k); Phi=np.linalg.solve(R.T,Vg.T).T
    return float(np.sum(Phi**2)/np.sum(Vg**2))
print('1D corner ratio g(theta) at x=1, n=40,80,160:')
for th in (0.5,0.8,0.95,1.0):
    print(' theta',th,[round(ratio1d(n,th,1.0),4) for n in (40,80,160)], ' at x=0:',[round(ratio1d(n,th,0.0),4) for n in (40,80,160)])
# 2D Padua equal weights corner (1,1), edge midpoint (1,0), centre, n=40,80
def ratio2d(n,th,pt):
    P,w=padua(n); w=np.ones(len(P))/len(P); k=int(round(th*n)) if th<1 else n
    V,_=cheb_basis(P[:,0],P[:,1],k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
    Vg,_=cheb_basis(np.array([pt[0]]),np.array([pt[1]]),k); Phi=np.linalg.solve(R.T,Vg.T).T
    return float(np.sum(Phi**2)/np.sum(Vg**2))
print('2D Padua equal-weight ratio: corner (1,1), edge (1,0), edge (0,1), centre; n=40,80')
for th in (0.5,0.8,0.95,1.0):
    for n in (40,80):
        print(' theta',th,'n',n,'corner %.4f edge(1,0) %.4f edge(0,1) %.4f centre %.4f'%(ratio2d(n,th,(1,1)),ratio2d(n,th,(1,0)),ratio2d(n,th,(0,1)),ratio2d(n,th,(0,0))), ' 1D g^2 %.4f g %.4f'%(ratio1d(n,th,1.0)**2, ratio1d(n,th,1.0)))
