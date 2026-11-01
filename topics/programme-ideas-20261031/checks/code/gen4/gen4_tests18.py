import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
def cheb1(X,k):
    T=[np.ones_like(X),X]
    for m in range(2,k+1): T.append(2*X*T[-1]-T[-2])
    return np.array(T).T
# 1D sanity: equispaced n+1 grid, equal weights, degree k=theta n: Ritz values of Jacobi section vs grid points
for n in (40,80,160):
    g=np.linspace(-1,1,n+1); w=np.ones(n+1)/(n+1)
    for th in (0.5,0.75,0.9):
        k=int(round(th*n)); V=cheb1(g,k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V); J=Q.T@(g[:,None]*Q); ev=np.linalg.eigvalsh((J+J.T)/2)
        d=np.min(np.abs(ev[:,None]-g[None,:]),axis=1); conv=d<1e-8
        r=np.sqrt(1-th**2)
        print('1D n',n,'theta',th,'k',k,'converged Ritz',int(conv.sum()),'of',k+1,'min|converged|',round(np.abs(ev[conv]).min(),3) if conv.any() else None,'predicted r=%.3f'%r, 'frac grid pts in [r,1]: %.3f'%np.mean(np.abs(g)>=r), 'converged/(k+1) %.3f'%(conv.sum()/(k+1)))
# 2D equispaced grid, total degree k: joint Ritz via simultaneous diagonalisation attempt: eigen-decompose Hx + c*Hy for random c, check residuals for both
rng=np.random.default_rng(0)
for n in (24,32,40):
    g=np.linspace(-1,1,n+1); XX,YY=np.meshgrid(g,g); X=XX.ravel(); Y=YY.ravel(); w=np.ones(len(X))/len(X)
    for th in (0.5,0.75,0.9):
        k=int(round(th*n)); V,idx=cheb_basis(X,Y,k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
        Hx=Q.T@(X[:,None]*Q); Hy=Q.T@(Y[:,None]*Q); Hx=(Hx+Hx.T)/2; Hy=(Hy+Hy.T)/2
        c=rng.standard_normal(); lam,U=np.linalg.eigh(Hx+c*Hy)
        mx=np.einsum('ij,ij->j',U,Hx@U); my=np.einsum('ij,ij->j',U,Hy@U)
        rx=np.linalg.norm(Hx@U-U*mx,axis=0); ry=np.linalg.norm(Hy@U-U*my,axis=0)
        conv=(rx<1e-6)&(ry<1e-6)
        # also: how many Ritz values of Hx alone coincide with grid x-values (ignoring joint)
        evx=np.linalg.eigvalsh(Hx); dx=np.min(np.abs(evx[:,None]-g[None,:]),axis=1)
        pts=np.c_[mx[conv],my[conv]]
        print('2D n',n,'theta',th,'N_k',len(idx),'joint converged',int(conv.sum()),'Hx-Ritz on grid x (1e-8)',int(np.sum(dx<1e-8)),'of',len(idx), 'max-norm of joint conv pts: min %.3f'%(np.max(np.abs(pts),axis=1).min() if len(pts) else -1), 'predicted r=%.3f'%np.sqrt(1-th**2))
