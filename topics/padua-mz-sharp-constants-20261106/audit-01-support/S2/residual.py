# Floating (non-rigorous) exploration of lambda_max(B_Q) for the S2 certificate residual. Auditor code.
import numpy as np, sys, time
from scipy.linalg import eigh
def Ifun(c,T):
    c=np.asarray(c,float); x=c*T; out=np.empty_like(c)
    sm=np.abs(x)<1e-3
    out[sm]=T*T*(0.5-x[sm]**2/8+x[sm]**4/144)
    cs=c[~sm]; xs=x[~sm]
    out[~sm]=T*np.sin(xs)/cs+(np.cos(xs)-1)/cs**2
    return out
def Hker(w,Y):
    x=w*Y; out=np.empty_like(w)
    sm=x<1e-3
    out[sm]=Y*Y*(0.5-x[sm]/3+x[sm]**2/8)
    ws=w[~sm]; xs=x[~sm]
    out[~sm]=(-np.expm1(-xs)-xs*np.exp(-xs))/ws**2
    return out
def BQ(T,Y,alpha,Q):
    s=(np.arange(1,Q+1)-0.5)/Q
    S,R=np.meshgrid(s,s,indexing='ij'); v=S+R; m=np.maximum(v,2-v); w=2-v
    b=0.5/m**2-0.5*Hker(w,Y)-alpha*0.5*(Ifun(S-R,T)+Ifun(S+R,T))
    return b/Q
def lam(T,Y,alpha,Q):
    B=BQ(T,Y,alpha,Q); return eigh(B,eigvals_only=True,subset_by_index=[Q-1,Q-1])[0]
if __name__=='__main__':
    Q=int(sys.argv[1]) if len(sys.argv)>1 else 1500
    for alpha in [0.0045,0.005,0.006,0.01,0.02,0.05]:
        for T in [5,10,20,40,80]:
            for Y in [5,10,20,40,80,160]:
                l=lam(T,Y,alpha,Q)
                A=1+Y**3/6+alpha*T**3/3
                print(f"alpha={alpha} T={T} Y={Y} Q={Q} lam_BQ={l:.6e} A={A:.3e} A/Q={A/Q:.3e} bound=1+alpha+u={1+alpha+max(0,l)+A/Q:.6f}",flush=True)
