# MEASURED float64 sanity of C07 (1)/(2)-type inequality at moderate n (outside claimed domain n>=500000). Not proof.
import numpy as np, math
def Dn_direct(n,u,v):
    m=n+1
    return (np.cos(m*u)+np.cos(n*u)-np.cos(m*v)-np.cos(n*v))/(np.cos(u)-np.cos(v))
def U(k,z):
    s=np.sin(z); out=np.empty_like(z)
    small=np.abs(s)<1e-9
    out[~small]=np.sin(k*z[~small])/s[~small]
    out[small]=k*np.cos((k-1)*z[small])*np.sign(np.cos(z[small]))  # limit near 0 (sign of cos handles pi)
    return out
def V(n,z): return np.cos((n+0.5)*z)/np.cos(z/2)
def Dn_UV(n,u,v):
    m=n+1; x=np.pi-u; y=np.pi-v; X=(x+y)/2; T=(x-y)/2
    return (-1)**n*(V(n,X)*U(m,T)+U(n,X)*V(n,T))
# identity check at random generic points
rng=np.random.default_rng(1)
for n in (7,8,101):
    u=rng.uniform(0,np.pi,1000); v=rng.uniform(0,np.pi,1000)
    print("identity n=%d max rel err %.2e"%(n, np.max(np.abs(Dn_direct(n,u,v)-Dn_UV(n,u,v))/(1+np.abs(Dn_direct(n,u,v))))))
def setup(n):
    m=n+1; j=np.arange(n+1)[:,None]; r=np.arange(m+1)[None,:]
    O=((j+r)%2==1)
    e=np.where((np.arange(n+1)==0)|(np.arange(n+1)==n),0.5,1.0)[:,None]
    f=np.where((np.arange(m+1)==0)|(np.arange(m+1)==m),0.5,1.0)[None,:]
    Bm=(r==j+1)&(j>=n/2)
    return m,j,r,O,e*f,Bm
def F(n,setupd,g,d):
    m,j,r,O,w,Bm=setupd
    u=(j*np.pi+g)/n; v=(r*np.pi+d)/m
    u=np.broadcast_to(u,O.shape); v=np.broadcast_to(v,O.shape)
    D=np.empty(O.shape)
    with np.errstate(divide='ignore',invalid='ignore'):
        D[~Bm]=Dn_direct(n,u[~Bm],v[~Bm])
    D[Bm]=Dn_UV(n,u[Bm],v[Bm])
    sgn=np.where(j%2==0,1.0,-1.0)
    Fv=sgn*(D-np.cos(n*u))/2
    return np.where(O,Fv,0.0)
for n in (2000,2001):
    sd=setup(n); m,j,r,O,w,Bm=sd; N=n*m
    F0=F(n,sd,0.0,0.0); Lam=4/N*np.sum(w*np.abs(F0))
    worst=1e9; worst2=-1e9
    for (al,be) in [(0.5,0),(0,0.5),(0.25,0.25),(0.1,0.05),(0.01,0.0),(0.3,0.2),(1e-3,1e-3)]:
        S4=F(n,sd,al,be)+F(n,sd,al,-be)+F(n,sd,-al,be)+F(n,sd,-al,-be)
        lam=1/N*np.sum(w*np.abs(S4)); r2=al*al+be*be; a=(math.cos(al)+math.cos(be))/2
        rhs=a*Lam+(math.log(m)/3+16)*r2
        worst=min(worst,(rhs-lam)/r2); worst2=max(worst2,(lam-Lam)/r2)
        print(n,(al,be),"Lam=%.6f lam=%.6f (aLam+c r2-lam)/r2=%.4f (lam-Lam)/r2=%.4f"%(Lam,lam,(rhs-lam)/r2,(lam-Lam)/r2))
