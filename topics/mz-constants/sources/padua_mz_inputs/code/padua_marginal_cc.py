import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
"""F7: the x-marginal of the interpolatory Padua rule (Lebesgue measure, degree m) is the
Clenshaw-Curtis rule with N = m (unique interpolatory rule on the m+1 Chebyshev-Lobatto x-nodes);
hence G_Padua restricted to univariate-in-x polynomials equals G_CC, eta_Padua(m,n) >= eta_CC(m,n)."""
import sys, numpy as np
from numpy.polynomial import chebyshev as C
sys.path.insert(0, ".")
from mz_padua_cc_check import padua, total_degree, cheb_hat
for m in (10, 20, 31):
    P, _ = padua(m); idx = total_degree(m)
    V = np.column_stack([cheb_hat(a, P[:, 0]) * cheb_hat(b, P[:, 1]) for a, b in idx])
    mom1 = lambda k: 0.0 if k % 2 else 2 / (1 - k * k)
    mom = np.array([mom1(a) * mom1(b) * (1 if a == 0 else np.sqrt(2)) * (1 if b == 0 else np.sqrt(2)) for a, b in idx])
    w = np.linalg.solve(V.T, mom)
    xs = np.cos(np.pi * np.arange(m + 1) / m)
    wx = np.array([w[np.abs(P[:, 0] - xv) < 1e-12].sum() for xv in xs])
    Vx = np.column_stack([C.chebval(xs, np.eye(m + 1)[k]) for k in range(m + 1)])
    wcc = np.linalg.solve(Vx.T, np.array([mom1(k) for k in range(m + 1)]) * 2 / 2)  # 1D moments of T_k
    wcc = np.linalg.solve(Vx.T, np.array([0.0 if k % 2 else 2 / (1 - k * k) for k in range(m + 1)]))
    print(f"m={m}: max|x-marginal Padua weights - CC weights| = {np.abs(2*wx/2 - wcc*1).max():.2e} (marginal includes factor int dy = 2: {np.abs(wx - 2*wcc).max():.2e})")
