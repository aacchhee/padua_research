import numpy as np
from numpy.polynomial import legendre as L, chebyshev as C
exec(open(__import__("os").path.join(__import__("os").path.dirname(__file__),"cc_asym.py")).read().split("for N in (40")[0])
N=60; n=N-1
x,w = cc_w(N); B=legmat(x,n); G=B.T@(w[:,None]*B)
# Legendre (orthonormal) -> Chebyshev connection matrix Cm (columns: cheb coeffs of p_j)
t=np.cos(np.pi*(np.arange(2*n+2)+0.5)/(2*n+2)); Cm=C.chebfit(t, legmat(t,n), n)
for j in range(n+1):
    pass
I=lambda k: 0.0 if k%2 else 2/(1-k*k)
Qk=lambda k: I(k) if k<=N else I(2*N-k)
K=np.arange(n+1)
Tq=np.array([[Qk(abs(i-j)) for j in K] for i in K]); Hq=np.array([[Qk(i+j) for j in K] for i in K])
Gf=Cm.T@((Tq+Hq)/2)@Cm
HD=np.array([[ (I(i+j)-Qk(i+j)) for j in K] for i in K])   # Hankel defect, zero for i+j<=N
E=Cm.T@(HD/2)@Cm
print("||G - formula||", np.abs(G-Gf).max(), " ||(I-G) - C^T(H_delta/2)C||", np.abs(np.eye(n+1)-G-E).max())
print("nonzeros of H_delta only for i+j>N:", np.all(HD[np.add.outer(K,K)<=N]==0))
