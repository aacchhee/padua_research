"""Adversarial check gen1-3: does rational Krylov on N = X + iY with complex poles
(analytic rational functions of z = x+iy, lightning-clustered) beat the pair's
line-pole spaces, and does the genuinely two-dimensional line class (lines in many
directions) beat the parallel-line / product classes already used by
Boulle-Herremans-Huybrechs (arXiv:2312.13202)?

Discrete setting: M = 32 x 32 Chebyshev grid on [-1,1]^2, uniform weights. For each
target f and each space S of (real) dimension N we report the relative best
least-squares error min_{r in S} ||f - r|| / ||f|| (the orthogonal projection error,
which is what a Galerkin/Krylov approximation of f(X,Y)u attains up to a constant for
normal matrices). Spaces are orthonormalised by SVD so conditioning plays no role.

Spaces (N = (n+1)(n+2)/2, n = 2..9):
  P      polynomials Pi_n                                       (HL / polynomial Krylov)
  Lcone  Pi_n / prod l_k, l_k = cos(th_k)(x-1) + sin(th_k)(y-1) - eps_k, th_k random in
         [0, pi/2] (normal cone of the corner (1,1)), eps_k tapered-clustered   (draft class)
  Lpar   same with all th_k = 0        (parallel lines x = 1 + eps_k: BHH one-direction class)
  Ldiag  same with all th_k = pi/4     (parallel lines x + y = 2 + sqrt2 eps_k: BHH corner class)
  Lprod  th_k alternating 0, pi/2      (product-type poles, dropped from the novelty claim)
  Zc     analytic rational in z: {1, z, .., z^m} + {1/(z - zeta_k)}, zeta_k clustered at the
         corner (1,1) along the outward diagonal; complex dimension N (real dim 2N)
  Zr     real span of Re/Im of the same functions, real dimension N
Targets (r, theta polar about the corner (1,1); w = (1-x) + i(1-y)):
  f1 = r            f2 = r^{1/2}            f3 = Re sqrt(w) (harmonic)   f4 = log r (harmonic)
  f5 = |x - y|      f6 = sqrt((x-1.01)^2 + y^2)   (draft's entry-point-3 function)
  f7 = r^{1/2} (1 + 0.5 sin(3 theta))  (non-harmonic corner singularity)
For f5 the line class uses lines x - y = +-eps_k (parallel to the singular line); the
analytic class uses poles clustered on both sides of the diagonal's end point (1,1)...
(see code); for f6 the line classes use lines through / near (1.01, 0).

Also: fraction of random lines through (1.01, 0) that intersect the square.
Scope: n <= 9 (N <= 55), one grid; seconds. MEASURED within this scope only.
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
corner = (1.0, 1.0)
r = np.hypot(x - 1, y - 1)
theta = np.arctan2(1 - y, 1 - x)
w = (1 - x) + 1j * (1 - y)

targets = {
    'f1 r': r,
    'f2 r^1/2': np.sqrt(r),
    'f3 Re sqrt(w) harm': np.real(np.sqrt(w)),
    'f4 log r harm': np.log(r),
    'f5 |x-y|': np.abs(x - y),
    'f6 sqrt((x-1.01)^2+y^2)': np.sqrt((x - 1.01) ** 2 + y ** 2),
    'f7 r^1/2(1+.5sin3th)': np.sqrt(r) * (1 + 0.5 * np.sin(3 * theta)),
}


def poly_cols(n):
    cols = []
    for t in range(n + 1):
        for a in range(t + 1):
            b = t - a
            cols.append(C.chebval(x, [0] * a + [1]) * C.chebval(y, [0] * b + [1]))
    return np.column_stack(cols)


def taper(n, sigma=2 * np.pi, scale=1.0):
    j = np.arange(1, n + 1)
    return scale * np.exp(-sigma * (np.sqrt(n) - np.sqrt(j)))


def line_space(n, thetas, eps, p0=(1.0, 1.0)):
    pi_n = np.ones(M)
    for th, e in zip(thetas, eps):
        pi_n *= np.cos(th) * (x - p0[0]) + np.sin(th) * (y - p0[1]) - e
    assert np.min(np.abs(pi_n)) > 0
    return poly_cols(n) / pi_n[:, None]


def analytic_space(N, zetas):
    """complex columns: polynomials of degree m plus 1/(z - zeta_k); total N columns."""
    npole = len(zetas)
    m = N - npole - 1
    cols = [z ** k for k in range(m + 1)] + [1.0 / (z - zt) for zt in zetas]
    return np.column_stack(cols)


def best_rel_err(A, f):
    U, S, _ = np.linalg.svd(A, full_matrices=False)
    rk = int(np.sum(S > 1e-13 * S[0]))
    U = U[:, :rk]
    res = f - U @ (U.conj().T @ f)
    return np.linalg.norm(res) / np.linalg.norm(f), rk


print(f"grid {m1}x{m1}, M = {M}; rel. best-LS error per space; N = real dimension (Zc: complex dim N)")
hdr = "  n   N |     P      Lcone     Lpar     Ldiag    Lprod  |    Zc(N)    Zr(N)"
for name, f in targets.items():
    print(f"\n--- {name} ---")
    print(hdr)
    for n in range(2, 10):
        N = (n + 1) * (n + 2) // 2
        eps = taper(n)
        if name.startswith('f5'):
            # singular line x = y through the domain: parallel lines x - y = +-eps (BHH),
            # cone = random directions through points near the diagonal end (1,1) is
            # meaningless here; use: Lcone -> lines x - y = s_k eps_k with random signs
            # and random small rotations (<= 10 deg) about the centre (0,0)
            th = np.pi / 4 + rng.uniform(-0.17, 0.17, n)   # normal direction near (1,-1)/sqrt2
            sg = rng.choice([-1, 1], n)
            Lc = poly_cols(n) / np.prod([np.cos(t) * x - np.sin(t) * y - s * e * 1.0 for t, s, e in zip(th, sg, eps)], axis=0)[:, None]
            Lp = poly_cols(n) / np.prod([(x - y) / np.sqrt(2) - s * e for s, e in zip(sg, eps)], axis=0)[:, None]
            Ld = Lp
            Lpr = poly_cols(n) / np.prod([((x - y) / np.sqrt(2) - s * e) if k % 2 == 0 else ((x + y) / np.sqrt(2) - 1.5 - e) for k, (s, e) in enumerate(zip(sg, eps))], axis=0)[:, None]
            npole = max(1, N // 2)
            ep = taper(npole)
            zetas = np.concatenate([(1 + 1j) + ep[: npole // 2] * (1 + 1j) / np.sqrt(2) * 1.0,
                                    (-1 - 1j) - ep[npole // 2:] * (1 + 1j) / np.sqrt(2)])
        elif name.startswith('f6'):
            p0 = (1.01, 0.0)
            th = rng.uniform(0, 2 * np.pi, n)            # the draft's "random angles through (1.01,0)"
            # lines through (1.01,0) cross the square; shift them out by eps to keep nodes off
            Lc = poly_cols(n) / np.prod([np.cos(t) * (x - p0[0]) + np.sin(t) * (y - p0[1]) - 1e-3 for t in th], axis=0)[:, None]
            Lp = line_space(n, [0.0] * n, eps, p0)        # vertical lines x = 1.01 + eps_k
            Ld = line_space(n, [np.pi / 4] * n, eps + 0.0, (1.01 + 0.0, 0.0))  # oblique lines through near (1.01,0): cross the square
            Lpr = poly_cols(n) / np.prod([((x - p0[0]) - e) if k % 2 == 0 else (y - 1.0 - e) for k, e in enumerate(eps)], axis=0)[:, None]
            npole = max(1, N // 2)
            zetas = 1.01 + 0j + taper(npole) * 1.0
        else:
            th = rng.uniform(0, np.pi / 2, n)
            Lc = line_space(n, th, eps)
            Lp = line_space(n, [0.0] * n, eps)
            Ld = line_space(n, [np.pi / 4] * n, eps)
            Lpr = line_space(n, [0.0 if k % 2 == 0 else np.pi / 2 for k in range(n)], eps)
            npole = max(1, N // 2)
            zetas = (1 + 1j) + taper(npole) * (1 + 1j) / np.sqrt(2)
        P = poly_cols(n)
        Zc = analytic_space(N, zetas)
        Zr = np.column_stack([Zc.real, Zc.imag])[:, : N] if False else None
        # real span with real dimension N: take the first ceil(N/2) complex functions' Re and Im
        kc = (N + 1) // 2
        Zc_half = analytic_space(kc, zetas[: max(1, kc // 2)])
        Zr = np.column_stack([Zc_half.real, Zc_half.imag])[:, :N]
        errs = [best_rel_err(A, f.astype(complex) if np.iscomplexobj(A) else f)[0]
                for A in (P, Lc, Lp, Ld, Lpr, Zc, Zr)]
        print(f"{n:3d} {N:3d} | " + "  ".join(f"{e:7.1e}" for e in errs[:5]) + " | " + "  ".join(f"{e:7.1e}" for e in errs[5:]))

# fraction of random lines through (1.01, 0) that cross the square
ths = rng.uniform(0, np.pi, 20000)
cross = 0
for t in ths:
    # line through (1.01,0) direction (cos t, sin t); crosses square iff some s with |1.01+s cos t|<=1, |s sin t|<=1
    if abs(np.cos(t)) < 1e-12:
        continue
    s_lo = (-1 - 1.01) / np.cos(t); s_hi = (1 - 1.01) / np.cos(t)
    s1, s2 = min(s_lo, s_hi), max(s_lo, s_hi)
    # need s in [s1,s2] with |s sin t| <= 1
    if abs(np.sin(t)) < 1e-12:
        cross += 1; continue
    a, b = -1 / abs(np.sin(t)), 1 / abs(np.sin(t))
    if max(s1, a) <= min(s2, b):
        cross += 1
print(f"\nlines through (1.01, 0) at uniformly random angles: fraction crossing the square = {cross / len(ths):.4f}")
