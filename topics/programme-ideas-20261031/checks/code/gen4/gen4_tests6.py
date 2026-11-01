import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# Joint Ritz convergence: eigvecs v of H_x^{(k)}; residual of H_y on v; converged if ||H_y v - mu v||<1e-6 and (lambda,mu) near a node.
def joint(X,Y,w,k):
    V,idx=cheb_basis(X,Y,k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
    Hx=Q.T@(X[:,None]*Q); Hy=Q.T@(Y[:,None]*Q); Hx=(Hx+Hx.T)/2; Hy=(Hy+Hy.T)/2
    lam,U=np.linalg.eigh(Hx)
    mu=np.einsum('ij,ij->j',U,Hy@U); res=np.linalg.norm(Hy@U-U*mu[None,:],axis=0)
    conv = res<1e-6
    pts = np.c_[lam[conv],mu[conv]]
    return len(idx), int(conv.sum()), pts
for name in ('equispaced','padua','random'):
  for n in (16,24,32):
    if name=='equispaced':
        g=np.linspace(-1,1,n+1); XX,YY=np.meshgrid(g,g); X=XX.ravel(); Y=YY.ravel()
    elif name=='padua':
        P,_=padua(n); X=P[:,0]; Y=P[:,1]
    else:
        rng=np.random.default_rng(0); M=(n+1)**2; X=rng.uniform(-1,1,M); Y=rng.uniform(-1,1,M)
    w=np.ones(len(X))/len(X)
    for th in (0.5,0.75):
        k=int(round(th*n)); Nk,c,pts=joint(X,Y,w,k)
        rad = np.max(np.abs(pts),axis=1) if len(pts) else np.array([])
        print(name,'n',n,'M',len(X),'theta',th,'N_k',Nk,'converged joint Ritz',c, 'frac',round(c/Nk,3), 'min max-norm of converged pts', (rad.min() if len(rad) else None), 'frac converged with max-norm>0.9', (np.mean(rad>0.9) if len(rad) else None))
