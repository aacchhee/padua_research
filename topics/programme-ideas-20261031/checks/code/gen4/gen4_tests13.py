import numpy as np, sys, time
from scipy.optimize import linprog
sys.path.insert(0,'.')
from gen4_tests import cheb_basis
t=time.time()
def cheb1(X,k):
    T=[np.ones_like(X),X]
    for m in range(2,k+1): T.append(2*X*T[-1]-T[-2])
    return np.array(T).T
def growth1d(n,k):
    g=np.linspace(-1,1,n+1); V=cheb1(g,k)
    # max p(x) s.t. |p(g_j)|<=1 at x in candidate set between last two grid pts and beyond? within [-1,1]: x in (g[-2],1)
    best=0
    for x in np.linspace(g[-2]+1e-3,1-1e-3,25):
        c=-cheb1(np.array([x]),k).ravel()
        r=linprog(c,A_ub=np.r_[V,-V],b_ub=np.ones(2*(n+1)),bounds=[(None,None)]*(k+1),method='highs')
        best=max(best,-r.fun)
    return best
def growth2d(n,k):
    g=np.linspace(-1,1,n+1); XX,YY=np.meshgrid(g,g); V,idx=cheb_basis(XX.ravel(),YY.ravel(),k)
    best=0; arg=None
    cand=[(x,y) for x in np.linspace(g[-2]+1e-3,1-1e-3,9) for y in [0.0,g[-2]/2, g[-2]+1e-3, (g[-2]+1)/2, 1-1e-3]]
    for (x,y) in cand:
        c=-cheb_basis(np.array([x]),np.array([y]),k)[0].ravel()
        r=linprog(c,A_ub=np.r_[V,-V],b_ub=np.ones(2*V.shape[0]),bounds=[(None,None)]*len(idx),method='highs')
        if -r.fun>best: best=-r.fun; arg=(round(x,3),round(y,3))
    return best,arg
C=lambda a: ((1+a)*np.log(1+a)+(1-a)*np.log(1-a))/2
for th in (0.5,0.75):
    for n in (8,12,16,20,24):
        k=int(round(th*n)); g1=growth1d(n,k); g2,arg=growth2d(n,k)
        print('theta',th,'n',n,'k',k,'1D: (1/n)log %.4f'%(np.log(g1)/n),'2D total-degree: (1/n)log %.4f'%(np.log(g2)/n),'argmax',arg,'ratio 2D/1D %.3f'%(g2/g1),'Kuijlaars C(theta)=%.4f'%C(th),'time %.0f'%(time.time()-t))
