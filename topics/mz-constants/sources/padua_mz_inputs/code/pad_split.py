import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz_padua_cc_check as M
def eigs(m, n):
    P,_ = M.padua(m); idx_m = M.total_degree(m)
    V = np.column_stack([M.cheb_hat(a,P[:,0])*M.cheb_hat(b,P[:,1]) for a,b in idx_m])
    mom1 = lambda k: 0.0 if k%2 else 2/(1-k*k)
    mom = np.array([mom1(a)*mom1(b)*(1 if a==0 else np.sqrt(2))*(1 if b==0 else np.sqrt(2)) for a,b in idx_m])
    w = np.linalg.solve(V.T, mom)
    idx = M.total_degree(n)
    B = np.column_stack([M.leg_hat(a,P[:,0])*M.leg_hat(b,P[:,1]) for a,b in idx])
    ev = np.linalg.eigvalsh(B.T@(w[:,None]*B))
    return ev[0], ev[-1], w.min()
for m in (10,20,30,40):
    for n in (m-2, m-1, m):
        lo,hi,wmin = eigs(m,n); print(f"m={m} n={n}: lmin={lo:.4f} lmax={hi:.4f}  (min weight {wmin:.2e})", flush=True)
