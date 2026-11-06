# MEASURED sanity only (float64), not proof.
import numpy as np, math, sys
def f(a,b): return (1+np.cos(b))/np.abs(np.cos(a)-np.cos(b))
def Ln(n):
    r=np.arange(1,n+1,2); d=np.where(r==n,0.5,1.0)
    return 2/n*math.fsum(d/np.sin(r*np.pi/(2*n)))
def An(n): return 2/math.pi*(math.log(n)+0.5772156649015329+math.log(8/math.pi))
for n in (500000, 10**6):
    m=n+1; L=Ln(n); A=An(n); B=n*L*L/m+1/m; L0=math.log(n)
    eps=(L0+2)**2/n+(L0+2)/(2*n*n)
    print(n, "L_n-A_n=%.3e"%(L-A), "1/(4n^2)=%.3e"%(1/(4*n*n)), "B_n-(A^2-eps)=%.6e"%(B-(A*A-eps)), "B-A^2=%.6e"%(B-A*A))
    # retained adjacent pairs
    J=np.arange(math.ceil(n/10), math.floor(9*n/10))
    a=np.pi/n; b=np.pi/m
    d1=f(J*a,(J+1)*b)-f(J*a,(J+1)*a)
    d2=f((J+1)*a,J*b)-f((J+1)*a,J*a)
    ret=4/(n*m)*math.fsum(d1+d2)
    dn=(16/25*n-28000)/(n+1)
    print("   retained=%.6f d(n)=%.6f  min pair sum=%.3e"%(ret,dn,(d1+d2).min()))
# full Delta at moderate n, nonnegativity of unordered pairs
for n in (64, 501, 2000):
    m=n+1; j=np.arange(n+1)[:,None]; k=np.arange(n+1)[None,:]
    odd=((j+k)%2==1)
    eps=np.where((np.arange(n+1)==0)|(np.arange(n+1)==n),0.5,1.0)
    eta=eps.copy(); eta[n]=1.0
    with np.errstate(divide='ignore',invalid='ignore'):
        act=np.where(odd, eps[:,None]*eta[None,:]*f(j*np.pi/n,k*np.pi/m),0.0)
        ref=np.where(odd, eps[:,None]*eps[None,:]*f(j*np.pi/n,k*np.pi/n),0.0)
    ref=np.nan_to_num(ref); act=np.nan_to_num(act)
    Lam=4/(n*m)*act.sum()+1/m; L=Ln(n); B=n*L*L/m+1/m
    dd=np.where(odd, eps[:,None]*eps[None,:]*(np.nan_to_num(f(j*np.pi/n,k*np.pi/m))-np.nan_to_num(f(j*np.pi/n,k*np.pi/n))),0.0)
    pair=dd+dd.T; iu=np.triu_indices(n+1,1)
    print(n,"Lambda_c=%.6f B_n=%.6f Delta=%.6f min unordered pair=%.3e d(n)=%.3f"%(Lam,B,Lam-B,pair[iu][odd[iu]].min(),(16/25*n-28000)/(n+1)))
