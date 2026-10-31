import numpy as np, sys, time
from collections import Counter
from scipy.ndimage import maximum_filter
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
t=time.time()
def leb(n, m, uniform=False):
    P,w=padua(n)
    g = np.linspace(-1,1,m) if uniform else np.cos(np.linspace(0,np.pi,m))
    GX,GY=np.meshgrid(g,g); X=GX.ravel(); Y=GY.ravel()
    V,_=cheb_basis(P[:,0],P[:,1],n); Tn=lambda x: np.cos(n*np.arccos(np.clip(x,-1,1))); TnB=Tn(P[:,0])
    lam=np.empty(len(X)); ch=2000
    for s in range(0,len(X),ch):
        Vg,_=cheb_basis(X[s:s+ch],Y[s:s+ch],n); L=w[None,:]*(Vg@V.T-np.outer(Tn(X[s:s+ch]),TnB)); lam[s:s+ch]=np.sum(np.abs(L),axis=1)
    return lam.reshape(m,m), GX, GY
def cell(n,x,y):
    th=np.arccos(np.clip(x,-1,1)); ph=np.arccos(np.clip(y,-1,1))
    u=(n+1)*th-n*ph; v=(n+1)*th+n*ph
    return (int(np.floor(u/(2*np.pi))), int(np.floor(v/(2*np.pi))))
for n in range(3,13):
    for uniform in (False,True):
        lam,GX,GY=leb(n,641,uniform)
        mx=(maximum_filter(lam,size=3,mode='nearest')==lam)
        inter=mx.copy(); inter[0,:]=inter[-1,:]=inter[:,0]=inter[:,-1]=False
        I,J=np.where(inter); cells=Counter(cell(n,GX[i,j],GY[i,j]) for i,j in zip(I,J))
        # number of interior cells of the curve: count distinct cells over the whole interior mesh
        allcells=set(cell(n,GX[i,j],GY[i,j]) for i in range(1,640,2) for j in range(1,640,2))
        print('n',n,'mesh','uniform' if uniform else 'cheb','interior maxima',int(inter.sum()),'total',int(mx.sum()),'n(n-1)/2',n*(n-1)//2,'(n+1)(n+2)/2',(n+1)*(n+2)//2,'| cells seen',len(allcells),'cells with max',len(cells),'max per cell dist',dict(Counter(cells.values())),'time %.0f'%(time.time()-t))
