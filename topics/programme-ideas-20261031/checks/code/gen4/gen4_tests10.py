import numpy as np, sys, time
from scipy.optimize import minimize
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
t=time.time()
def checker(X,Y):
    pts=[(X[j],Y[k]) for j in range(len(X)) for k in range(len(Y)) if (j+k)%2==0]
    return np.array(pts)
def logdet(X,Y,n):
    P=checker(X,Y); V,_=cheb_basis(P[:,0],P[:,1],n); s=np.linalg.svd(V,compute_uv=False); return np.sum(np.log(s))
def leb_const(P,n,m=201):
    V,_=cheb_basis(P[:,0],P[:,1],n); g=np.cos(np.linspace(0,np.pi,m)); GX,GY=np.meshgrid(g,g)
    Vg,_=cheb_basis(GX.ravel(),GY.ravel(),n); L=np.linalg.solve(V.T,Vg.T).T  # Lagrange basis values: Vg V^{-1}
    return np.max(np.sum(np.abs(L),axis=1))
for n in (4,6,8,10):
    X0=np.cos(np.arange(n+1)*np.pi/n); Y0=np.cos(np.arange(n+2)*np.pi/(n+1))
    P0=checker(X0,Y0); assert len(P0)==(n+1)*(n+2)//2
    # separability test: random perturbations of X with two different Y's
    rng=np.random.default_rng(1)
    dX=0.05*rng.standard_normal(n+1); dX[0]=dX[-1]=0
    Y1=Y0+0.05*np.r_[0,rng.standard_normal(n),0]
    sep = (logdet(X0+dX,Y0,n)-logdet(X0,Y0,n)) - (logdet(X0+dX,Y1,n)-logdet(X0,Y1,n))
    # optimise interior nodes (endpoints fixed) to maximise logdet
    def unpack(p):
        X=np.r_[1.0,p[:n-1],-1.0]; Y=np.r_[1.0,p[n-1:],-1.0]; return X,Y
    p0=np.r_[X0[1:-1],Y0[1:-1]]
    f=lambda p: -logdet(*unpack(p),n)
    r=minimize(f,p0,method='BFGS',options={'gtol':1e-8,'maxiter':2000})
    X,Y=unpack(r.x)
    # compare with Gauss-Lobatto-Legendre nodes
    from numpy.polynomial.legendre import Legendre
    gll=lambda m: np.sort(np.r_[1,Legendre.basis(m).deriv().roots(),-1])[::-1]
    Pf=checker(X,Y)
    print('n',n,'separability residual %.1e'%sep,'logdet Padua %.4f opt %.4f'%(-f(p0),-r.fun),'Lambda Padua %.3f opt %.3f'%(leb_const(P0,n),leb_const(Pf,n)))
    print('   X opt ',np.round(np.sort(X)[::-1],4)); print('   GLL(n)',np.round(gll(n),4)); print('   CL(n) ',np.round(X0,4))
    print('   Y opt ',np.round(np.sort(Y)[::-1],4)); print('   GLL(n+1)',np.round(gll(n+1),4))
print('elapsed',time.time()-t)
