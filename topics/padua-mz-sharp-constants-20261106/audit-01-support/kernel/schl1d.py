import numpy as np
from scipy.special import j0, ellipk
from numpy.polynomial.legendre import leggauss
# 1D check of Schlomilch closed forms for S_all, S_alt
n=400
x,w=leggauss(n); a=(x+1)/2; wa=w/2*a   # measure a da
u=np.exp(-a)*(1+a**2); v=np.cos(2*a)+0.3
J=4000
c=lambda f,j: np.sum(wa*f*j0(np.pi*j*a))
cu=np.array([c(u,j) for j in range(J)]); cv=np.array([c(v,j) for j in range(J)])
e=np.ones(J); e[0]=0.5
sgn=(-1.0)**np.arange(J)
print('series all', np.sum(e*cu*cv), ' alt', np.sum(e*sgn*cu*cv))
# closed forms with phi quadrature, singular handled by many points
phi,wp=leggauss(2000); phi=(phi+1)/2*np.pi; wp=wp/2*np.pi
A=a[:,None]; Ap=a[None,:]
# S_all via elliptic K: int_0^pi dphi/sqrt(a^2+a'^2-2aa'cos) = 2/(a+a') K(m=4aa'/(a+a')^2)
m=4*A*Ap/(A+Ap)**2
Sall=2*ellipk(np.minimum(m,1-1e-16))/(np.pi**2*(A+Ap))
# S_alt
Salt=np.zeros((n,n))
for i in range(n):
  r2=a[i]**2+a[:,None]**2-2*a[i]*a[:,None]*np.cos(phi)[None,:]
  val=np.where(r2>1, 1/np.sqrt(np.maximum(r2-1,1e-300)),0.0)
  Salt[i]=(2/np.pi**2)*np.sum(val*wp,axis=-1)
print('closed all', (wa*u)@Sall@(wa*v), ' alt', (wa*u)@Salt@(wa*v))
