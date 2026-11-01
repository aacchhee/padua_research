import numpy as np, sys, time
sys.path.insert(0,'.')
from gen4_tests import padua
t=time.time()
def lam_at(n, s, u):
    """Lebesgue function of Pad_n at corner (s,u), s,u in {+1,-1}; O(N n) via cumulative sums."""
    P,w=padua(n); X=P[:,0]; Y=P[:,1]; N=len(P)
    th_x=np.arccos(np.clip(X,-1,1)); th_y=np.arccos(np.clip(Y,-1,1))
    i=np.arange(n+1)
    Tx=np.cos(np.outer(th_x,i)); Ty=np.cos(np.outer(th_y,i))
    c=np.where(i>0,2.0,1.0)           # (sqrt2)^2 normalisation squared
    Cy=np.cumsum(c[None,:]*(u**i)[None,:]*Ty,axis=1)   # Cy[:,m]=sum_{j<=m}
    K=np.sum(c[None,:]*(s**i)[None,:]*Tx*Cy[:,::-1],axis=1)  # Cy[:,n-i]
    Tn_corner=s**n; Tn_B=np.cos(n*th_x)
    L=w*(K-Tn_corner*Tn_B)
    return np.sum(np.abs(L))
ns=[10,20,40,80,160,320,640]; L=[]
for n in ns:
    vals=[lam_at(n,s,u) for (s,u) in [(1,1),(-1,1),(1,-1),(-1,-1)]]
    L.append(max(vals)); print('n',n,'corner values',np.round(vals,4),'max %.5f'%max(vals),'minus (4/pi^2)log^2 n = %.4f'%(max(vals)-(4/np.pi**2)*np.log(n)**2), 'time %.1f'%(time.time()-t))
L=np.array(L); ln=np.log(ns)
coef=np.linalg.lstsq(np.c_[ln**2,ln,np.ones(len(ns))],L,rcond=None)[0]; print('free fit a,b,c =',np.round(coef,4),' (4/pi^2 = %.4f, 2/pi=%.4f)'%(4/np.pi**2,2/np.pi))
coef2=np.linalg.lstsq(np.c_[ln,np.ones(len(ns))],L-(4/np.pi**2)*ln**2,rcond=None)[0]; r=L-(4/np.pi**2)*ln**2-np.c_[ln,np.ones(len(ns))]@coef2; print('fixed-a fit b,c =',np.round(coef2,4),'max resid %.4f'%np.max(np.abs(r)))
# tail-only fit (n>=80)
m=ns.index(80); coef3=np.linalg.lstsq(np.c_[ln[m:]**2,ln[m:],np.ones(len(ns)-m)],L[m:],rcond=None)[0]; print('free fit n>=80: a,b,c =',np.round(coef3,4))
