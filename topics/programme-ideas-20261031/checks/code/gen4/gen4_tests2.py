import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# Test 3 fixed: w_B vs 1/(K_n(B,B) - 2 T_n(x_B)^2) (defect in T_n(x) in RES convention)
for n in (4,6,15,30):
    P,w = padua(n); V,idx = cheb_basis(P[:,0],P[:,1],n); K=np.sum(V**2,axis=1)
    Tnx = np.cos(n*np.arccos(np.clip(P[:,0],-1,1)))
    c = 1/(K-2*Tnx**2); c2=1/(K-Tnx**2)
    print('T3fix n',n,'err(K-2Tn(x)^2)',np.max(np.abs(c/w-1)),'err(K-Tn(x)^2)',np.max(np.abs(c2/w-1)), 'err 1/K', np.max(np.abs((1/K)/w-1)))
# Test 2b: Ritz values of H_x^{(k)} alone vs Chebyshev x-nodes, equal weights and cubature weights
for weights in ('equal','cubature'):
  for n in (20,40):
    P,w = padua(n)
    if weights=='equal': w=np.ones(len(P))/len(P)
    xs = np.unique(np.round(P[:,0],12))
    for th in (0.5,0.8,0.95,1.0):
        k = int(round(th*n)) if th<1 else n
        V,idx = cheb_basis(P[:,0],P[:,1],k); Q,R=np.linalg.qr(np.sqrt(w)[:,None]*V)
        Hx = Q.T@(P[:,0][:,None]*Q); Hx=(Hx+Hx.T)/2
        ev = np.linalg.eigvalsh(Hx)
        d = np.min(np.abs(ev[:,None]-xs[None,:]),axis=1)
        print(weights,'n',n,'theta',th,'dim',len(idx),'conv<1e-8',int(np.sum(d<1e-8)),'conv<1e-4',int(np.sum(d<1e-4)),'maxRitz',ev.max())
# Test 1b: equispaced 2D grid total-degree (unisolvent?) -> use equispaced (n+1)x(n+1) grid as node set with M>N, equal weights; Christoffel ratio vs Legendre continuous kernel? Instead measure growth sup|p|_K / |p|_grid over total degree k=theta*n via SVD on fine Chebyshev mesh.
def cheb_mesh(m):
    g=np.cos(np.linspace(0,np.pi,m)); GX,GY=np.meshgrid(g,g); return GX.ravel(),GY.ravel()
GX,GY = cheb_mesh(161)
for name in ('equispaced','padua'):
  for n in (8,12,16,20):
    if name=='equispaced':
        g=np.linspace(-1,1,n+1); X,Y=np.meshgrid(g,g); X=X.ravel(); Y=Y.ravel()
    else:
        P,_=padua(n); X=P[:,0]; Y=P[:,1]
    for th in (0.5,0.75,1.0):
        k=int(round(th*n))
        V,idx=cheb_basis(X,Y,k); Vg,_=cheb_basis(GX,GY,k)
        # sup over p of ||p||_mesh,inf / ||p||_grid,inf  >= via 2-norm: sigma_max(Vg R^-1)/... use l2 proxy: sigma_max(Vg)/sigma_min(V) crude; better: solve least squares; use 2-norm ratio of ||Vg c||_inf / ||V c||_inf maximized by alternating; proxy: sigma_max(Vg B)/sqrt(M) where B=V^+ ... keep simple: 2-norm growth G2 = sigma_max(Vg (V^T V)^{-1/2}) / sqrt(#mesh)
        Q,R=np.linalg.qr(V); s=np.linalg.svd(Vg@np.linalg.inv(R),compute_uv=False)
        print(name,'n',n,'theta',th,'k',k,'N_k',len(idx),'M',len(X),'(1/n)log(smax/sqrt(M))',np.log(s[0]/np.sqrt(len(GX))*np.sqrt(len(X)))/n)
