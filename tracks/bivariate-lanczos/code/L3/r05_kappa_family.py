"""R05 (MEASURED): test the kappa-family certificate on Padua nodes.

C is defined by B_C(z,w) = sum c_jk z^j w^k = (z-w)^2 kappa(zw), kappa(t) = sum_a k_a t^a
(so C is Hankel-perp): c_{a+1,a+1} += -2 k_a, c_{a+2,a} += k_a, c_{a,a+2} += k_a.
Generators q_m: normalised two-term Padua generators of PD-T?bivariate-lanczos-claude-309(c)
(q_m = -g_m/lambda_m, q_{n+1} = omega/2^(n-1)). Hessian of p_C at a node = 2 G^T C G.
Reports min eigenvalue of G^T C G separately over interior and boundary nodes, and the
worst boundary node.

Usage: python3 r05_kappa_family.py nmax c1 [c2 ...]   (default kappa(t) = -(1-c) - c t)
       python3 r05_kappa_family.py nmax --coef k0 k1 ... (explicit kappa coefficients)
"""
import sys
import numpy as np
from numpy.polynomial import chebyshev as Ch
from l3lib import padua


def cT(k):
    c = np.zeros(k + 1); c[k] = 1; return c


def T(k, t):
    return Ch.chebval(t, cT(k))


def dT(k, t):
    return Ch.chebval(t, Ch.chebder(cT(k))) if k > 0 else 0 * t


def lc(k):
    return 1.0 if k == 0 else 2.0 ** (k - 1)


def grads(n, z):
    x, y = z
    G = []
    for m in range(n + 1):
        gx = dT(n - m, x) * T(m, y) - dT(m, x) * T(n + 1 - m, y)
        gy = T(n - m, x) * dT(m, y) - T(m, x) * dT(n + 1 - m, y)
        lam = lc(m) * lc(n + 1 - m)
        G.append([-gx / lam, -gy / lam])
    U = Ch.chebder(cT(n)) / n
    om = Ch.chebmul(Ch.chebsub(Ch.chebmul([0, 1], [0, 1]), [1]), U)
    G.append([Ch.chebval(x, Ch.chebder(om)) / 2.0 ** (n - 1), 0.0])
    return np.array(G)


def C_from_kappa(n, k):
    m = n + 2
    C = np.zeros((m, m))
    for a, ka in enumerate(k):
        C[a + 1, a + 1] += -2 * ka
        C[a + 2, a] += ka
        C[a, a + 2] += ka
    return C


def evaluate(n, C):
    wi, wb, worst = np.inf, np.inf, None
    for z in padua(n):
        G = grads(n, z)
        H = G.T @ C @ G
        e = np.linalg.eigvalsh(0.5 * (H + H.T))[0]
        interior = abs(abs(z[0]) - 1) > 1e-12 and abs(abs(z[1]) - 1) > 1e-12
        if interior:
            wi = min(wi, e)
        elif e < wb:
            wb, worst = e, z
    return wi, wb, worst


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    if len(sys.argv) > 2 and sys.argv[2] == '--coef':
        kap = [float(v) for v in sys.argv[3:]]
        fams = [('coef', None)]
    else:
        fams = [('c', float(v)) for v in (sys.argv[2:] or ['0.1', '0.2'])]
    for tag, c in fams:
        for n in range(2, nmax + 1):
            if tag == 'c':
                k = [-(1 - c), -c] + [0.0] * (n - 2)
            else:
                k = (kap + [0.0] * n)[:n]
            C = C_from_kappa(n, k[:n])
            m = n + 2
            hp = max(abs(sum(C[j, i - j] for j in range(m) if 0 <= i - j < m)) for i in range(2 * m - 1))
            wi, wb, worst = evaluate(n, C)
            print(f"{tag}={c if c is not None else kap} n={n}: Hankel-perp resid {hp:.0e}  "
                  f"min eig interior {wi:+.3e}  boundary {wb:+.3e} at {np.round(worst, 4) if worst is not None else None}",
                  flush=True)


if __name__ == '__main__':
    main()
