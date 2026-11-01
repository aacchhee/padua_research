"""M2 adversarial script 4: the 'rim' coordinates of the monic border basis (coefficients of the degree-(n+1) border
polynomials on the degree-n standard monomials, 2N numbers) as local coordinates of the point set: Jacobian rank of
nodes -> rim coefficients. This checks our reading of Kreuzer-Robbiano, arXiv 2503.01752 (2025), Prop. 5.6 / Cor. 5.5
(planar simplicial border basis scheme = affine cell A^{2N} on the rim indeterminates) in the measured scope.

Model: claude-fable-5-1, effort max (as requested by the orchestrator) . Adversarial check . 2026-11-01
Scope: random real nodes, n = 2..6, floating point (monomial basis, nodes in [-1,1]^2); MEASURED only.
Run: python3 -I m2_rim_chart_check.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from m2_common import monomials, dim_pi, random_nodes

def mono_vander(x, y, mons):
    return np.array([[xx**a * yy**b for (a, b) in mons] for xx, yy in zip(x, y)])

def border_coeffs(x, y, n):
    """Monic border basis of I(X) for the order ideal of all monomials of degree <= n: for each degree-(n+1) monomial
    m, the normal form NF(m) = sum_t c_{t,m} t over standard monomials t; returns the (N x (n+2)) matrix c and the
    degree of each standard monomial."""
    mons = monomials(n); N = len(mons)
    V = mono_vander(x, y, mons)                 # N x N
    border = [(n + 1 - b, b) for b in range(n + 2)]
    Vb = mono_vander(x, y, border)              # N x (n+2)
    C = np.linalg.solve(V, Vb)                  # V C = Vb  -> m = sum_t c_t t on X
    deg = np.array([a + b for a, b in mons])
    return C, deg

def jac_rank_rim(x, y, n, h=1e-6):
    C0, deg = border_coeffs(x, y, n)
    rim = deg == n
    def f(xx, yy):
        C, _ = border_coeffs(xx, yy, n)
        return C[rim, :].ravel()
    cols = []
    for t in range(len(x)):
        for which in (0, 1):
            xp, yp = x.copy(), y.copy(); xm, ym = x.copy(), y.copy()
            if which == 0:
                xp[t] += h; xm[t] -= h
            else:
                yp[t] += h; ym[t] -= h
            cols.append((f(xp, yp) - f(xm, ym)) / (2 * h))
    J = np.array(cols).T
    s = np.linalg.svd(J, compute_uv=False)
    r = int(np.sum(s > 1e-6 * s[0]))
    return J.shape, r, s[0], s[r-1], (s[r] if r < len(s) else 0.0)

def main():
    rng = np.random.default_rng(3)
    for n in range(2, 7):
        N = dim_pi(n)
        x, y, w = random_nodes(n, rng)
        shape, r, s0, sr, snext = jac_rank_rim(x, y, n)
        print(f"n={n} N={N}: rim coefficients {shape[0]} (=2N={2*N}), node parameters {shape[1]}; Jacobian rank {r}; "
              f"s_1={s0:.1e}, s_r={sr:.1e}, s_(r+1)={snext:.1e}")

if __name__ == '__main__':
    main()
