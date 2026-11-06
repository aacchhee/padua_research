import numpy as np
from scipy.special import sici
def sinc(z): return np.sinc(z/np.pi)
worst6=0;worst7=0;worst12=0;worstw0=0
for J in [1,2,3,5,8]:
  A=np.pi*J
  for N in range(int(np.ceil(2*A)),400,7):
    for j in range(1,J+1):
      a=np.pi*j
      t=np.linspace(0,N*np.pi,20001)
      R=sinc(a/(2*N))**2*np.cos(t/(2*N))/(sinc((t+a)/(2*N))*sinc((t-a)/(2*N))*sinc(t/(2*N)))
      # direct: p_{N,j}(cos(t/N)) via Chebyshev series vs f_j
      k=np.arange(N); ck=np.ones(N); ck[0]=.5
      coef=(2/N)*ck*(np.cos(np.pi*j*k/N)-(-1)**j)
      tt=t[(np.abs(t-a)>1e-3)&(t>1e-3)][::50]
      p=np.cos(np.outer(tt/N,k))@coef
      f=2*(-1)**j*a*a*np.sin(tt)/(tt*(tt*tt-a*a))
      Rt=sinc(a/(2*N))**2*np.cos(tt/(2*N))/(sinc((tt+a)/(2*N))*sinc((tt-a)/(2*N))*sinc(tt/(2*N)))
      ident=np.max(np.abs(p-f*Rt))
      m=t<=N
      worst6=max(worst6,np.max(np.abs(R[m]-1)/((t[m]**2+a*a)/N**2)))
      worst7=max(worst7,R.max()); assert R.min()>=-1e-12
      if ident>1e-10: print("identity fail",J,N,j,ident)
for N in range(2,600):
  th=np.pi*np.arange(N+1)/N; c=np.ones(N+1); c[0]=c[N]=.5
  jj=np.arange(1,N//2+1); b=np.where(2*jj==N,1.0,2.0)
  for j in range(0,min(N,30)):
    w=2*c[j]/N*(1-np.sum(b*np.cos(2*jj*th[j])/(4*jj*jj-1)))
    if j==0: worstw0=max(worstw0,abs(N*N*w-1)*(N*N-1)); continue
    om=2*((-1)**j+np.pi*j*sici(np.pi*j)[0])
    worst12=max(worst12,abs(N*N*w-om)/(20*(1+(2*np.pi*j)**3)/N))
print("max |R-1|/((t^2+a^2)/N^2) on t<=N:",worst6,"(claim<=1)")
print("max R on [0,N pi]:",worst7,"(claim <9)")
print("max ratio |N^2 w_j-omega_j| / bound(12):",worst12,"(claim<=1)")
print("max |N^2w0-1|*(N^2-1):",worstw0,"(claim<=1)")
