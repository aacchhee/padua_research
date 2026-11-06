# Numerical check of P3-02: sup_g int_0^T sin^2(pi t)|S(t)|^2 dt/t / E  vs (A_J^2/2+3/2) and 2/pi^2 H_J^2
import numpy as np, json, sys
from scipy.special import sici
from scipy.sparse.linalg import LinearOperator, eigsh
def cm(J, T):
    m=np.arange(1,J+1,dtype=float)
    up=np.minimum(m+1,T)
    # int_m^up sin^2(pi t)/t = 1/2 log(up/m) - 1/2 (Ci(2pi up)-Ci(2pi m))
    ci_up=sici(2*np.pi*up)[1]; ci_m=sici(2*np.pi*m)[1]
    return 0.5*np.log(up/m)-0.5*(ci_up-ci_m)
out=[]
for T in [10,100,1000,10**4,10**5,10**6, 10**6+0.5]:
    J=int(np.floor(T)); c=cm(J,T); k=np.arange(1,J+1,dtype=float)
    # h = g/sqrt(k);  g = sqrt(k) h ; S_m = cumsum(g_k/k) = cumsum(h/sqrt k)
    def mv(h):
        S=np.cumsum(h/np.sqrt(k)); y=c*S
        # adjoint: (T^T y)_k = sum_{m>=k} y_m /sqrt(k)
        r=np.cumsum(y[::-1])[::-1]/np.sqrt(k); return r
    op=LinearOperator((J,J),matvec=mv,dtype=float)
    lam=eigsh(op,k=1,which='LA',tol=1e-10)[0][0] if J>2 else None
    H=np.sum(1/k); A=2*H/np.pi+1
    out.append(dict(T=T,J=J,lam=lam,bound=A*A/2+1.5,ratio_to_bound=lam/(A*A/2+1.5),lam_over_H2=lam/H**2,two_over_pi2=2/np.pi**2))
    print(out[-1],flush=True)
json.dump(out,open('p302_primitive.json','w'),indent=1)
