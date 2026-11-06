import numpy as np, sys
from scipy.special import ellipk
from scipy.linalg import eigh
def Sall(a,b,h=None):
    m=4*a*b/(a+b)**2
    out=2*ellipk(np.minimum(m,1.0))/(np.pi**2*(a+b))
    if h is not None:  # replace diagonal by cell average of log singularity
        d=np.isclose(a,b)
        aa=a[d] if np.ndim(a) else a
        out[d]=(1/(np.pi**2*aa))*(np.log(16*aa/h)+1)
    return out
def Salt(a,b):
    s=a+b; m=(s**2-1)/(4*a*b)
    out=np.where(s>1, 2*ellipk(np.clip(m,0,1-1e-15))/(np.pi**2*np.sqrt(a*b)),0.0)
    return out
def spec(n):
    h=1.0/n; x=(np.arange(n)+.5)*h
    A=x[:,None]; Ap=x[None,:]
    S1=Sall(A*np.ones_like(Ap),Ap*np.ones_like(A),h); S2=Salt(A,Ap)
    I,Jg=np.meshgrid(np.arange(n),np.arange(n),indexing='ij')
    keep=(x[I]+x[Jg])<1   # centers in D
    ia=I[keep]; ib=Jg[keep]
    wt=x[ia]*x[ib]*h*h
    Kmat=-8*(S2[np.ix_(ia,ia)]*S1[np.ix_(ib,ib)]+S1[np.ix_(ia,ia)]*S2[np.ix_(ib,ib)])
    sw=np.sqrt(wt)
    M=sw[:,None]*Kmat*sw[None,:]
    ev=eigh(M,eigvals_only=True)
    return ev[0],ev[-1],len(wt)
for n in [int(v) for v in sys.argv[1:]]:
    print(n,*spec(n),flush=True)
