# Claude audit: carrier energies Q_m(p^2) from weight formula (3) (validated against solved weights m<=30).
import numpy as np
def W(m):
    R=m//2; th=np.arange(m+1)*np.pi/m; ph=np.arange(m+2)*np.pi/(m+1)
    t=np.array([2.0]+[-4.0/(4*a*a-1) for a in range(1,R+1)])
    A=np.arange(R+1); M=np.outer(t,t)*((A[:,None]+A[None,:])<=R)
    S=np.cos(np.outer(th,2*A))@M@np.cos(np.outer(2*A,ph))
    hm=2.0/(1-m*m)
    B=S-2*hm*np.cos(m*th)[:,None]
    e=np.ones(m+1);e[[0,m]]=.5; f=np.ones(m+2);f[[0,m+1]]=.5
    w=2*np.outer(e,f)/(m*(m+1))*B
    J,K=np.meshgrid(np.arange(m+1),np.arange(m+2),indexing='ij'); w[(J+K)%2==1]=0
    return w,th,ph
def F(r,t):
    t=np.asarray(t,float); out=np.empty_like(t); z=np.abs(np.sin(t/2))<1e-14
    out[z]=r+1; out[~z]=np.sin((r+1)*t[~z]/2)**2/np.sin(t[~z]/2)**2/(r+1); return out
prev=None
import sys
for m in [int(x) for x in sys.argv[1:]]:
    w,th,ph=W(m)
    a,b=.2,.2; r,s=int(a*m),int(b*m)
    pn=np.cos(m//2*th)*F(r,th); qy=F(s,ph)
    Qn=(pn**2)@w@(qy**2)
    a2,b2=.1,.2; r2,s2=int(a2*m),int(b2*m)
    pp=np.sin(m*th/2)*np.sin(r2*th)*F(r2,th); qy2=F(s2,ph)
    Qp=(pp**2)@w@(qy2**2)
    print(m,"neg Q/logm=%.5f (lim %.5f)"%(Qn/np.log(m),-16*a*b/9),"pos Q/logm=%.5f (lim %.5f)"%(Qp/np.log(m),8*a2*b2/9),
          "" if prev is None else "slopes per log2: neg %.5f pos %.5f"%((Qn-prev[0])/np.log(2),(Qp-prev[1])/np.log(2)))
    prev=(Qn,Qp)
