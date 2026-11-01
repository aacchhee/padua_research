import numpy as np, sys
from scipy.optimize import minimize, minimize_scalar
from scipy.special import eval_jacobi
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
def checker(X,Y): return np.array([(X[j],Y[k]) for j in range(len(X)) for k in range(len(Y)) if (j+k)%2==0])
def logdet(X,Y,n):
    P=checker(X,Y); V,_=cheb_basis(P[:,0],P[:,1],n); return np.sum(np.log(np.linalg.svd(V,compute_uv=False)))
def glj(m,a):
    # zeros of (1-x^2) d/dx P_m^{(a,a)} : interior zeros = zeros of P_{m-1}^{(a+1,a+1)}
    from numpy.polynomial import polynomial as Pn
    xs=np.cos(np.linspace(0,np.pi,4001)); f=eval_jacobi(m-1,a+1,a+1,xs); s=np.where(np.diff(np.sign(f))!=0)[0]
    roots=[]
    from scipy.optimize import brentq
    for i in s: roots.append(brentq(lambda x: eval_jacobi(m-1,a+1,a+1,x),xs[i+1],xs[i]))
    return np.sort(np.r_[1,roots,-1])[::-1]
for n in (6,8,10,12,16):
    X0=np.cos(np.arange(n+1)*np.pi/n); Y0=np.cos(np.arange(n+2)*np.pi/(n+1))
    def unpack(p): return np.r_[1.0,p[:n-1],-1.0], np.r_[1.0,p[n-1:],-1.0]
    r=minimize(lambda p:-logdet(*unpack(p),n), np.r_[X0[1:-1],Y0[1:-1]], method='BFGS',options={'gtol':1e-9,'maxiter':5000})
    X,Y=unpack(r.x); X=np.sort(X)[::-1]; Y=np.sort(Y)[::-1]
    # fit alpha for X against GLJ(n, alpha)
    fa=lambda a: np.sum((glj(n,a)-X)**2); ra=minimize_scalar(fa,bounds=(-0.9,2),method='bounded')
    # Y: check symmetry and fit
    fy=lambda a: np.sum((glj(n+1,a)-Y)**2); ry=minimize_scalar(fy,bounds=(-0.9,2),method='bounded')
    print('n',n,'X: best alpha %.4f resid %.2e'%(ra.x,ra.fun),'| X sym err %.1e'%np.max(np.abs(X+X[::-1])),'| Y: best alpha %.4f resid %.2e'%(ry.x,ry.fun),'Y sym err %.2e'%np.max(np.abs(Y+Y[::-1])), 'grad',np.linalg.norm(r.jac))
    print('   X',np.round(X,5)); print('   Y',np.round(Y,5))
    # separability check of optimum: optimise X alone with Y fixed at Y0 -> same X?
    r2=minimize(lambda p:-logdet(np.r_[1.0,p,-1.0],Y0,n), X0[1:-1], method='BFGS',options={'gtol':1e-9})
    print('   X-opt with Y=Y0 fixed, diff vs joint opt: %.2e'%np.max(np.abs(np.sort(np.r_[1,r2.x,-1])[::-1]-X)))
