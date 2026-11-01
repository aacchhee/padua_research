"""Adversarial check gen1-3 (second, corrected run of approx_baseline.py).

Changes: (a) pole clustering eps_k = exp(-sigma (sqrt(m) - sqrt(k))) with sigma = 2.3, so the
closest pole sits at ~1e-3 for m = 9, i.e. at the resolution of the 32x32 Chebyshev grid
(the sigma = 2 pi lightning taper of the first run put poles at 1e-8 and the evaluated
bases lost rank in double precision for n >= 7; those rows were numerically meaningless);
(b) columns are scaled to unit norm before the SVD and the numerical rank is printed;
(c) besides the literal draft class V_n = Pi_n / pi_n (one finite line per degree, which
contains NO non-constant polynomial), the mixed class Pi_n / pi_m with m = floor(n/2) finite
lines and n - m "lines at infinity" (l_k = 1) is included, which is what lightning +
polynomial spaces look like in this framework.

Spaces of real dimension N = (n+1)(n+2)/2:
  P        polynomials Pi_n
  L1cone   Pi_n/pi_n, lines through the normal cone of the corner (1,1), random directions
  L1par    Pi_n/pi_n, all lines parallel (x = 1 + eps_k)                [BHH one-direction]
  L1prod   Pi_n/pi_n, lines alternating x = 1+eps, y = 1+eps            [product class]
  Mcone    Pi_n/pi_m, m = n//2, cone directions                          [draft class, mixed]
  Mpar     Pi_n/pi_m, m = n//2, parallel                                  [BHH-type, mixed]
  Mprod    Pi_n/pi_m, m = n//2, alternating x/y                           [product, mixed]
  L1pt     Pi_n / prod_{j<=n/2} |z - zeta_j|^2  (conjugate pairs of complex lines = point poles)
  Mpt      Pi_n / prod_{j<=m/2} |z - zeta_j|^2,  m = n//2
  Zc       analytic rational in z: 1, z, .., z^{N-1-p} and 1/(z - zeta_k), k <= p = N//2,
           zeta_k clustered at the corner along the outward diagonal; complex dim N
  Zr       Re/Im parts of the first ceil(N/2) such functions: real dim N
Targets about the corner (1,1): f1 = r, f2 = r^{1/2}, f3 = Re sqrt(w) (harmonic),
f4 = log r (harmonic), f7 = r^{1/2}(1 + 0.5 sin 3 theta) (non-harmonic);
f5 = |x-y| with lines parallel to the diagonal (cone = slightly rotated), f6 = the
draft's sqrt((x-1.01)^2 + y^2) with vertical lines x = 1.01 + eps_k (cone = random
directions through (1.01,0) shifted by 1e-3, which cross the square).
Scope: n <= 9, N <= 55, one grid, one seed; seconds. MEASURED within this scope only.
"""
import numpy as np
from numpy.polynomial import chebyshev as C

rng = np.random.default_rng(7)
m1 = 32
xc = np.cos(np.pi * (2 * np.arange(1, m1 + 1) - 1) / (2 * m1))
X, Y = np.meshgrid(xc, xc)
x, y = X.ravel(), Y.ravel()
M = len(x)
z = x + 1j * y
r = np.hypot(x - 1, y - 1)
theta = np.arctan2(1 - y, 1 - x)
w = (1 - x) + 1j * (1 - y)
SIG = 2.3

targets = {
    'f1 r': r,
    'f2 r^1/2': np.sqrt(r),
    'f3 Re sqrt(w) harm': np.real(np.sqrt(w)),
    'f4 log r harm': np.log(r),
    'f7 r^1/2(1+.5sin3th)': np.sqrt(r) * (1 + 0.5 * np.sin(3 * theta)),
    'f5 |x-y|': np.abs(x - y),
    'f6 sqrt((x-1.01)^2+y^2)': np.sqrt((x - 1.01) ** 2 + y ** 2),
}


def poly_cols(n):
    cols = []
    for t in range(n + 1):
        for a in range(t + 1):
            cols.append(C.chebval(x, [0] * a + [1]) * C.chebval(y, [0] * (t - a) + [1]))
    return np.column_stack(cols)


def taper(m):
    j = np.arange(1, m + 1)
    return np.exp(-SIG * (np.sqrt(m) - np.sqrt(j))) if m > 0 else np.zeros(0)


def lines_den(thetas, eps, p0):
    d = np.ones(M)
    for th, e in zip(thetas, eps):
        d *= np.cos(th) * (x - p0[0]) + np.sin(th) * (y - p0[1]) - e
    assert np.min(np.abs(d)) > 0
    return d


def best_rel_err(A, f):
    nrm = np.linalg.norm(A, axis=0)
    A = A[:, nrm > 1e-14 * nrm.max()]          # drop zero columns (Im of the constant 1)
    A = A / np.linalg.norm(A, axis=0)
    U, S, _ = np.linalg.svd(A, full_matrices=False)
    rk = int(np.sum(S > 1e-12 * S[0]))
    U = U[:, :rk]
    res = f - U @ (U.conj().T @ f)
    return np.linalg.norm(res) / np.linalg.norm(f), rk, A.shape[1]


def analytic_space(N, zetas):
    p = len(zetas)
    cols = [z ** k for k in range(N - p)] + [1.0 / (z - zt) for zt in zetas]
    return np.column_stack(cols)


print(f"grid {m1}x{m1}, M = {M}, sigma = {SIG}; rel. best-LS error (rank deficiency marked *)")
hdr = "  n   N |     P     L1cone    L1par   L1prod |   Mcone    Mpar     Mprod  |  L1pt     Mpt    |   Zc(N)    Zr(N)"


def point_den(k, zetas_fn):
    """product of k/2 conjugate complex-line pairs = prod |z - zeta_j|^2 (real, no real zeros);
    k odd: one extra real line far away (l = x - 3)."""
    e = taper(k // 2)
    d = np.ones(M)
    for zt in zetas_fn(e):
        d *= np.abs(z - zt) ** 2
    if k % 2 == 1:
        d *= (x - 3.0)
    return d
for name, f in targets.items():
    print(f"\n--- {name} ---")
    print(hdr)
    for n in range(2, 10):
        N = (n + 1) * (n + 2) // 2
        m = n // 2
        Pn = poly_cols(n)
        if name.startswith('f5'):
            def den(k, rot):
                e = taper(k); sg = rng.choice([-1, 1], k)
                th = np.pi / 4 + (rng.uniform(-0.17, 0.17, k) if rot else np.zeros(k))
                return np.prod([np.cos(t) * x - np.sin(t) * y - s * ee for t, s, ee in zip(th, sg, e)], axis=0)
            spaces = [Pn, Pn / den(n, True)[:, None], Pn / den(n, False)[:, None], Pn / den(n, False)[:, None],
                      Pn / den(m, True)[:, None], Pn / den(m, False)[:, None], Pn / den(m, False)[:, None]]
            p = N // 2; e = taper(p)
            zetas = np.concatenate([(1 + 1j) + e[: p // 2] * (1 + 1j) / np.sqrt(2), (-1 - 1j) - e[p // 2:] * (1 + 1j) / np.sqrt(2)])
            # conjugate pairs of complex lines x - y = +- i eps (BHH imaginary shifts)
            def pden(k):
                e2 = taper(k // 2); d = np.ones(M)
                for ee in e2:
                    d *= ((x - y) / np.sqrt(2)) ** 2 + ee ** 2
                if k % 2 == 1:
                    d *= (x - 3.0)
                return d
            spaces += [Pn / pden(n)[:, None], Pn / pden(m)[:, None]]
        elif name.startswith('f6'):
            p0 = (1.01, 0.0)
            def den(k, kind):
                e = taper(k)
                if kind == 'cone':
                    th = rng.uniform(0, 2 * np.pi, k); return lines_den(th, [1e-3] * k, p0)
                if kind == 'par':
                    return lines_den([0.0] * k, e, p0)
                return np.prod([((x - p0[0]) - ee) if i % 2 == 0 else (y - 1 - ee) for i, ee in enumerate(e)], axis=0)
            spaces = [Pn] + [Pn / den(k, kind)[:, None] for k in (n,) for kind in ('cone', 'par', 'prod')] \
                   + [Pn / den(k, kind)[:, None] for k in (m,) for kind in ('cone', 'par', 'prod')]
            p = N // 2
            zetas = 1.01 + 0j + taper(p)
            spaces += [Pn / point_den(k, lambda e: 1.01 + e)[:, None] for k in (n, m)]
        else:
            def den(k, kind):
                e = taper(k)
                th = {'cone': rng.uniform(0, np.pi / 2, k), 'par': [0.0] * k,
                      'prod': [0.0 if i % 2 == 0 else np.pi / 2 for i in range(k)]}[kind]
                return lines_den(th, e, (1.0, 1.0))
            spaces = [Pn] + [Pn / den(n, kind)[:, None] for kind in ('cone', 'par', 'prod')] \
                   + [Pn / den(m, kind)[:, None] for kind in ('cone', 'par', 'prod')]
            p = N // 2
            zetas = (1 + 1j) + taper(p) * (1 + 1j) / np.sqrt(2)
            spaces += [Pn / point_den(k, lambda e: (1 + 1j) + e * (1 + 1j) / np.sqrt(2))[:, None] for k in (n, m)]
        Zc = analytic_space(N, zetas)
        kc = (N + 1) // 2
        Zh = analytic_space(kc + 1, zetas[: max(1, (kc + 1) // 2)])
        Zr = np.column_stack([Zh.real, Zh.imag])
        Zr = Zr[:, np.linalg.norm(Zr, axis=0) > 1e-14][:, :N]      # real dimension N
        cells = []
        for A in spaces + [Zc, Zr]:
            err, rk, nc = best_rel_err(A, f.astype(complex) if np.iscomplexobj(A) else f)
            cells.append(f"{err:7.1e}{'*' if rk < nc else ' '}")
        print(f"{n:3d} {N:3d} | " + " ".join(cells[:4]) + "| " + " ".join(cells[4:7]) + "| " + " ".join(cells[7:9]) + "| " + " ".join(cells[9:]))
