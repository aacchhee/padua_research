# Finite-N adversarial check of P3-03 sections 2-3,5 on actual CC weights.
# R = I_N u - P(u), P = extracted endpoint primitives (eq. 7), inputs on 1..M and N-M..N-1.
import numpy as np, json, sys, time
from scipy.linalg import eigh
xg,wg=np.polynomial.legendre.leggauss(10); xg=(xg+1)/2; wg=wg/2
def ccw(N):
    th=np.pi*np.arange(N+1)/N; j=np.arange(1,N//2+1); b=np.where(2*j==N,1.0,2.0)
    s=1-np.sum((b/(4*j*j-1))[None,:]*np.cos(2*np.outer(th,j)),axis=1)
    c=np.where((np.arange(N+1)==0)|(np.arange(N+1)==N),1.0,2.0)
    return c*s/N
def left_rows(N):
    J=N//2; e=list(np.pi*np.arange(J+1)/N)
    if N%2: e.append(np.pi/2)
    th=[];w=[]
    for a,b in zip(e[:-1],e[1:]): th.append(a+(b-a)*xg); w.append((b-a)*wg)
    th=np.concatenate(th); w=np.concatenate(w)
    return th, w*np.sin(th)   # dx = sin(theta) dtheta
def card(N,th,ks):
    tk=np.pi*np.asarray(ks)/N; ck=np.where((np.asarray(ks)==0)|(np.asarray(ks)==N),2.0,1.0)
    T=th[:,None]
    den=-2*np.sin((T+tk[None,:])/2)*np.sin((T-tk[None,:])/2)
    sg=(-1.0)**(np.asarray(ks)+1)
    return sg[None,:]*np.sin(T)*np.sin(N*T)/(ck[None,:]*N*den)
def run(N,M):
    w=ccw(N); th,mu=left_rows(N); t=N*th/np.pi
    L=np.log(N)
    left=np.arange(1,M+1); right=N-left; ks=np.concatenate([left,right])
    C=card(N,th,ks)
    P=np.zeros_like(C)
    sincfac=2*np.sin(np.pi*t)/(np.pi*t)
    P[:,:M]=sincfac[:,None]*((-1.0)**left)[None,:]*(left[None,:]<t[:,None])
    R=C-P
    sc=1/np.sqrt(w[ks]); sq=np.sqrt(mu)[:,None]
    def gram(X):
        Y=(X*sq)*sc[None,:]; G=Y.T@Y
        perm=np.concatenate([np.arange(M,2*M),np.arange(0,M)])
        return G+G[np.ix_(perm,perm)]
    out={}
    for name,X in [('remainder',R),('primitive',P),('interp',C)]:
        out[name]=float(np.sqrt(np.linalg.eigvalsh(gram(X))[-1]))
    H=np.sum(1/np.arange(1,N//2+1)); A=2*H/np.pi+1
    kk=left; rho=np.max(kk/(N*N*w[kk]))
    out.update(N=N,M=M,L=L,claimed_remainder=80+6*np.sqrt(L+1),
               primitive_bound=float(np.sqrt((2*A*A+6)*rho)),
               primitive_over_L=out['primitive']/L, remainder_over_sqrtL=out['remainder']/np.sqrt(L),
               target_2sqrt2_over_pi2=2*np.sqrt(2)/np.pi**2)
    return out
if __name__=="__main__":
  res=[]
  for N in [256,257,512,513,1024,1025,2048,2049,4096,4097]:
      for Mrule in ['N/L','N/4-1']:
          L=np.log(N); M=int(np.floor(N/L)) if Mrule=='N/L' else (N-1)//4 - (1 if (N-1)//4>=N/4 else 0)
          M=min(M, int(np.ceil(N/4))-1)
          t0=time.time(); o=run(N,M); o['Mrule']=Mrule; res.append(o)
          print({k:(round(v,4) if isinstance(v,float) else v) for k,v in o.items()}, round(time.time()-t0,1),flush=True)
  json.dump(res,open('p303_cc.json','w'),indent=1)
