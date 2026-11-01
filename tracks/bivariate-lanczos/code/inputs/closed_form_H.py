"""Closed-form (H_x, H_y) on Pad_n with cubature weights, built ONLY from
(i) discrete orthonormality of normalized product Chebyshev basis (T_n(x) has norm^2 2), and
(ii) the two-term ideal relations of Bos-De Marchi-Vianello-Xu (Numer. Math. 108, 2007, Thm 2.3):
    T_{n+1}(x) = T_{n-1}(x);  T_{n-k+1}(x)T_k(y) = s_k T_{k-1}(x)T_{n-k+1}(y) (1<=k<=n);  T_{n+1}(y) = s' T_n(x)
on Pad_n (signs s determined numerically for this convention). Compares with numerically computed H."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from padua_weights_check import padua, cheb_basis

def T(m, t): return np.cos(m*np.arccos(np.clip(t, -1, 1)))

for n in [5, 6, 20, 41]:
    P, w = padua(n); x, y = P[:, 0], P[:, 1]
    # signs of the ideal relations in this convention
    s = {}
    for k in range(1, n+1):
        a, b = T(n-k+1, x)*T(k, y), T(k-1, x)*T(n-k+1, y)
        sk = np.sign(a @ b); assert np.allclose(a, sk*b); s[k] = sk
    assert np.allclose(T(n+1, x), T(n-1, x))
    sp = np.sign(T(n+1, y) @ T(n, x)); assert np.allclose(T(n+1, y), sp*T(n, x))
    V, idx = cheb_basis(P, n); N = len(idx); pos = {ij: m for m, ij in enumerate(idx)}
    G = V.T @ (w[:, None]*V); d = np.sqrt(np.diag(G))      # norms (only T_n(x) has sqrt 2)
    nrm = lambda i, j: (np.sqrt(2) if i > 0 else 1)*(np.sqrt(2) if j > 0 else 1)  # T_i T_j = phat/nrm
    def reduce(i, j):
        """express T_i(x)T_j(y), i+j<=n+1, as list of (coef, (i',j')) with i'+j'<=n on Pad_n"""
        if i + j <= n: return [(1.0, (i, j))]
        if j == 0 and i == n+1: return [(1.0, (n-1, 0))]
        if i == 0 and j == n+1: return [(sp, (n, 0))]
        k = j; return [(s[k], (k-1, n-k+1))]
    def mult(var, i, j):
        """x or y times T_i(x)T_j(y) as combination of T's"""
        out = []
        if var == 0:
            terms = [(1.0, (1, j))] if i == 0 else [(0.5, (i+1, j)), (0.5, (i-1, j))]
        else:
            terms = [(1.0, (i, 1))] if j == 0 else [(0.5, (i, j+1)), (0.5, (i, j-1))]
        for c, (a, b) in terms:
            for c2, ij in reduce(a, b): out.append((c*c2, ij))
        return out
    for var, c in [(0, x), (1, y)]:
        Hc = np.zeros((N, N))
        for col, (i, j) in enumerate(idx):      # basis psi_col = nrm(i,j) T_i T_j / d_col
            for coef, (a, b) in mult(var, i, j):
                r = pos[(a, b)]
                Hc[r, col] += coef*nrm(i, j)/d[col] * d[r]/nrm(a, b)
        Q = np.sqrt(w)[:, None]*V/d
        Hn = Q.T @ (c[:, None]*Q)
        print(f"n={n} N={N} H_{'xy'[var]}: ||closed-form - numeric|| = {np.abs(Hc-Hn).max():.1e}, "
              f"max nnz/col = {(abs(Hc)>1e-14).sum(0).max()}, symmetric: {np.allclose(Hc, Hc.T)}")
    # joint spectrum of the closed-form pair reproduces Pad_n
    ev = np.linalg.eigvalsh(Hc + 0.0)   # H_y eigenvalues = y-coords
    print(f"   eig(H_y) matches y-coords: {np.allclose(np.sort(ev), np.sort(y))}")
