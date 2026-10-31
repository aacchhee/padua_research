"""R05 (MEASURED end-to-end cross-check of theory file 313): build
P_n(x,y) = 9*(g1^2 - g0*g2/2) + (g2^2 - g1*g3),  g_m = T_{n-m}(x)T_m(y) - T_m(x)T_{n+1-m}(y),
symbolically (sympy, exact polynomial), check deg P_n <= 2n+1, and evaluate P_n, grad P_n and the
Hessian at every Padua node {(cos j pi/n, cos k pi/(n+1)) : j+k even} in floating point.
Usage: python3 r05_direct_check.py nmin nmax
"""
import sys
import numpy as np
import sympy as sp

x, y = sp.symbols('x y')


def g(m, n):
    return sp.chebyshevt(n - m, x) * sp.chebyshevt(m, y) - sp.chebyshevt(m, x) * sp.chebyshevt(n + 1 - m, y)


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    for n in range(nmin, nmax + 1):
        G = [sp.expand(g(m, n)) for m in range(4)]
        P = sp.expand(9 * (G[1] ** 2 - G[0] * G[2] / 2) + (G[2] ** 2 - G[1] * G[3]))
        deg = sp.Poly(P, x, y).total_degree()
        f = sp.lambdify((x, y), [P, sp.diff(P, x), sp.diff(P, y), sp.diff(P, x, 2), sp.diff(P, x, y), sp.diff(P, y, 2)], 'numpy')
        worst_val = worst_grad = 0.0; lam_min = np.inf; scale = 0.0
        for j in range(n + 1):
            for k in range(n + 2):
                if (j + k) % 2:
                    continue
                v = f(np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1)))
                worst_val = max(worst_val, abs(v[0])); worst_grad = max(worst_grad, abs(v[1]), abs(v[2]))
                H = np.array([[v[3], v[4]], [v[4], v[5]]], float)
                lam_min = min(lam_min, np.linalg.eigvalsh(H)[0]); scale = max(scale, np.abs(H).max())
        print(f"n={n}: deg P_n = {deg} (<= {2*n+1}: {deg <= 2*n+1}); max|P| at nodes {worst_val:.1e}; "
              f"max|grad P| {worst_grad:.1e}; min Hessian eigenvalue over nodes {lam_min:.4e} "
              f"(max |Hess entry| {scale:.2e}; ratio {lam_min/scale:.2e})", flush=True)


if __name__ == '__main__':
    main()
