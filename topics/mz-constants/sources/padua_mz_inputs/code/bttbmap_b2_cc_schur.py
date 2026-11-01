# B2: CC rule on N+1 Chebyshev-Lobatto nodes, Lebesgue measure on [-1,1], space Pi_N.
# Node (Lagrange) coordinates: discrete Gram = W=diag(CC weights); continuous Gram Mc = ∫ l_k l_m dx.
# 1/lambda_min(G_CC) = lambda_max(W^{-1/2} Mc W^{-1/2}) = 1 + lambda_max(Mt),  Mt := W^{-1/2}(Mc-W)W^{-1/2}.
# C4-T03(ii) template: |Mt_kl| <= C (1+log(N/d_kl)) / sqrt(m_k m_l),  m_k = max(min(k,N-k),1),
# d_kl = |k-l| (no wrap: interval, two endpoint zeros of sin).  Schur sum with weights m^{-1/2} ~ log^2 N.
import numpy as np, sys
def run(N):
    k=np.arange(N+1); th=k*np.pi/N; x=np.cos(th)
    # Chebyshev coeffs of Lagrange basis: A[j,k] (DCT-I inverse)
    cc=np.ones(N+1); cc[0]=cc[-1]=2
    A=(2/N)*np.cos(np.outer(k,th))/np.outer(cc,cc)   # A[j,k]= 2/(N c_j c_k) cos(j th_k)
    h=np.zeros(2*N+1); ev=np.arange(0,2*N+1,2); h[ev]=2/(1-ev.astype(float)**2)  # ∫T_k
    I=np.add.outer(k,k); J=np.abs(np.subtract.outer(k,k))
    Gam=0.5*(h[I]+h[J])                                  # ∫T_iT_j
    Mc=A.T@Gam@A
    w=h[:N+1]@A                                           # CC weights = ∫ l_k
    s=1/np.sqrt(w); Mt=s[:,None]*(Mc-np.diag(w))*s[None,:]
    lam=np.linalg.eigvalsh(Mt); 
    m=np.maximum(np.minimum(k,N-k),1).astype(float)
    d=np.maximum(np.abs(np.subtract.outer(k,k)),1).astype(float)
    B=np.abs(Mt)*np.sqrt(np.outer(m,m))/(1+np.log(N/d))
    off=~np.eye(N+1,dtype=bool)
    schur=(np.abs(Mt)@(m**-0.5))*m**0.5
    wfloor=(w*N/np.maximum(np.sin(th),1/N)).min()
    print(f"N={N:5d} 1/lmin(G)={1+lam.max():.4f} lmin(G)={1/(1+lam.max()):.4f} lmax(G)={1/(1+lam.min()):.6f} "
          f"maxB_off={B[off].max():.3f} maxB_diag={B[~off].max():.3f} Schur={schur.max():.2f} Schur/log^2={schur.max()/np.log(N)**2:.3f} w-floor={wfloor:.3f}")
for N in [40,80,160,320,640,1280]: run(N)
