import numpy as np, sys, time
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
from scipy.ndimage import maximum_filter
t=time.time()
def leb(n, m=401):
    P,w = padua(n)
    g = np.cos(np.linspace(0,np.pi,m)); GX,GY=np.meshgrid(g,g)
    X=GX.ravel(); Y=GY.ravel()
    V,idx = cheb_basis(P[:,0],P[:,1],n)
    Tn = lambda x: np.cos(n*np.arccos(np.clip(x,-1,1)))
    TnB = Tn(P[:,0])
    lam = np.empty(len(X))
    ch = 2000
    for s in range(0,len(X),ch):
        Vg,_ = cheb_basis(X[s:s+ch],Y[s:s+ch],n)
        K = Vg@V.T
        L = w[None,:]*(K - np.outer(Tn(X[s:s+ch]),TnB))
        lam[s:s+ch] = np.sum(np.abs(L),axis=1)
    Vb,_ = cheb_basis(P[:3,0],P[:3,1],n); Kb=Vb@V.T; Lb=w[None,:]*(Kb-np.outer(Tn(P[:3,0]),TnB))
    card = np.max(np.abs(Lb-np.eye(len(P))[:3]))
    return lam.reshape(m,m), g, card
for n in range(3,13):
    lam,g,card = leb(n, m=321)
    mx = (maximum_filter(lam, size=3, mode='nearest')==lam)
    interior = mx.copy(); interior[0,:]=interior[-1,:]=interior[:,0]=interior[:,-1]=False
    print('n',n,'Lambda',round(lam.max(),4),'interior maxima',int(interior.sum()),'total',int(mx.sum()),'bounds',n*(n-1)//2,(n+1)*(n+2)//2,'card err %.1e'%card, 'argmax', np.unravel_index(lam.argmax(),lam.shape))
for n in (10,20,30,40,60):
    lam,g,card = leb(n, m=4*n+1)
    print('n',n,'Lambda_mesh %.4f'%lam.max(), 'minus (4/pi^2)log^2 n %.4f'%(lam.max()-(4/np.pi**2)*np.log(n)**2), 'ratio to log n %.4f'%((lam.max()-(4/np.pi**2)*np.log(n)**2)/np.log(n)), 'argmax', np.unravel_index(lam.argmax(),lam.shape))
print('elapsed',time.time()-t)
