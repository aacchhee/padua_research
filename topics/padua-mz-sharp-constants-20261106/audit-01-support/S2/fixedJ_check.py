# Check fixed-J bounds (1),(2) of S2-fixed-trial-limit and the closed-form Gram, auditor code.
import numpy as np, sys
from scipy.special import sici
def model(J):
    j=np.arange(1,J+1,dtype=float); a=np.pi*j; s=(-1.)**j
    si2,ci2=sici(2*a); d=np.euler_gamma+np.log(2*a)-ci2
    C=np.empty((J,J))
    for p in range(J):
        for q in range(J):
            if p==q: C[p,p]=2*(a[p]*si2[p]+d[p])
            else: C[p,q]=2*s[p]*s[q]*(a[p]**2*d[q]-a[q]**2*d[p])/(a[p]**2-a[q]**2)
    om=2*(s+a*sici(a)[0])
    return C,np.diag(om)+4*np.outer(s,s)
def finite(N,J):
    k=np.arange(N); ck=np.ones(N); ck[0]=0.5
    A=np.array([(2/N)*ck*(np.cos(np.pi*j*k/N)-(-1)**j) for j in range(1,J+1)])  # Chebyshev coeffs 0..N-1
    m=np.arange(2*N); mu=np.where(m%2==0,2/(1-m.astype(float)**2),0.0)
    M=0.5*(mu[np.abs(k[:,None]-k[None,:])]+mu[k[:,None]+k[None,:]])
    CN=N*N*A@M@A.T
    th=np.pi*np.arange(N+1)/N; c=np.ones(N+1); c[0]=c[N]=.5
    w=np.array([2*c[q]/N*(1-sum((1.0 if 2*jj==N else 2.0)*np.cos(2*jj*th[q])/(4*jj*jj-1) for jj in range(1,N//2+1))) for q in range(J+1)])
    s=(-1.)**np.arange(1,J+1)
    DN=N*N*(np.diag(w[1:J+1])+4*w[0]*np.outer(s,s))
    return CN,DN
for J in [1,2,3,5]:
    C,D=model(J); mJ=np.linalg.eigvalsh(C)[0]
    import scipy.linalg as sl
    lamJ=sl.eigh(D,C,eigvals_only=True)[-1]
    for N in [50,51,200,201,800,801]:
        A=np.pi*J
        if N<np.ceil(2*A): continue
        CN,DN=finite(N,J)
        e=1000*J*(1+A**4)/N**2; dd=20*(1+8*A**3)/N+4*J/(N*N-1)
        ce=np.linalg.norm(CN-C,2); de=np.linalg.norm(DN-D,2)
        lamN=sl.eigh(DN,CN,eigvals_only=True)[-1]
        print(f"J={J} N={N} |CN-C|={ce:.3e} (bound {e:.3e}) |DN-D|={de:.3e} (bound {dd:.3e}) m_J={mJ:.4f} lamJ={lamJ:.10f} lamNJ={lamN:.10f} diff={abs(lamN-lamJ):.2e}")
