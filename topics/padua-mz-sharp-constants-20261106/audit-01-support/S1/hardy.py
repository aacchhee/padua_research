"""S1 audit (liminf route): sharp discrete log-Hardy constant
 sup_g sum_{m=1}^{M} S_m^2 log(1+1/m) / sum_{k=1}^{M} g_k^2/k,  S_m=sum_{k<=m} g_k/k,
 compared with (2/pi)^2 (log M + s)^2: report the effective shift s."""
import sys, json
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
out=[]
for M in [10**3, 10**4, 10**5, 10**6]:
    k = np.arange(1, M+1, dtype=float); D = np.log1p(1/k); sk = np.sqrt(k)
    def mv(h):
        g = h.ravel()*sk                 # g = sqrt(k) h  => sum g^2/k = |h|^2
        S = np.cumsum(g/k)
        y = S*D
        z = np.cumsum(y[::-1])[::-1]     # A^T: (A^T y)_k = (1/k) sum_{m>=k} y_m
        return (z/k)*sk
    op = LinearOperator((M, M), matvec=mv, dtype=float)
    lam = eigsh(op, k=1, which='LA', tol=1e-10)[0][0]
    s = np.sqrt(lam)*np.pi/2 - np.log(M)
    out.append(dict(M=M, constant=float(lam), shift=float(s))); print(out[-1], flush=True)
json.dump(out, open(sys.argv[1],'w'), indent=1)
