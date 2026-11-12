#!/usr/bin/env python3
"""Independent auditor sanity checks for D1-01 identities (float64, not a proof).

Checks on product/non-group rules with boundary stabilizers and coordinate 0:
  sum delta_i = N - dim Pi_{n-1}, delta_i >= 0;
  lifted torus rule: E*E = I on A_n, sum eta_j = M - m_n, eta_j >= 0, M <= 2^d N;
  row identity sum_{l != j} v_j v_l |D_n(t_j-t_l)|^2 = q_j eta_j.
Plus a 2-D Padua scaled-lift separation/lattice check.
"""
import itertools, math, sys
import numpy as np


def cheb_gauss(n):
    i = np.arange(1, n + 1)
    return np.cos((2 * i - 1) * np.pi / (2 * n)), np.full(n, 1.0 / n)          # exact 2n-1


def cheb_lobatto(n):
    j = np.arange(0, n + 1)
    w = np.full(n + 1, 1.0 / n); w[0] = w[-1] = 0.5 / n
    return np.cos(j * np.pi / n), w                                               # exact 2n-1


def cheb_radau(n):
    j = np.arange(0, n + 1)
    w = np.full(n + 1, 2.0 / (2 * n + 1)); w[0] = 1.0 / (2 * n + 1)
    return np.cos(2 * j * np.pi / (2 * n + 1)), w                                 # exact 2n


def product(rules):
    pts = np.array(list(itertools.product(*[r[0] for r in rules])))
    w = np.array([np.prod(c) for c in itertools.product(*[r[1] for r in rules])])
    return pts, w


def padua(n):
    pts, w = [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2:
                continue
            x, y = math.cos(j * math.pi / n), math.cos(k * math.pi / (n + 1))
            c = 1.0 / (n * (n + 1))
            ej, ek = j in (0, n), k in (0, n + 1)
            wt = c * (0.5 if (ej and ek) else (1.0 if (ej or ek) else 2.0))
            pts.append((x, y)); w.append(wt)
    return np.array(pts), np.array(w)


def check_moments(pts, w, deg):
    d = pts.shape[1]; th = np.arccos(np.clip(pts, -1, 1)); worst = 0.0
    for a in itertools.product(range(deg + 1), repeat=d):
        if sum(a) > deg:
            continue
        val = np.sum(w * np.prod(np.cos(np.array(a) * th), axis=1))
        worst = max(worst, abs(val - (1.0 if not any(a) else 0.0)))
    return worst


def poly_defects(pts, w, n):
    d = pts.shape[1]; th = np.arccos(np.clip(pts, -1, 1)); K = np.zeros(len(w))
    for a in itertools.product(range(n), repeat=d):
        if sum(a) > n - 1:
            continue
        f = np.ones(len(w))
        for jj, aj in enumerate(a):
            if aj:
                f = f * 2 * np.cos(aj * th[:, jj]) ** 2
        K += f
    delta = 1 - w * K
    return delta, math.comb(n - 1 + d, d)


def lift(pts, w):
    d = pts.shape[1]; th = np.arccos(np.clip(pts, -1, 1)); atoms = {}; sizes = []
    for x, wt in zip(th, w):
        orb = set()
        for s in itertools.product((-1, 1), repeat=d):
            t = np.mod(np.array(s) * x, 2 * np.pi)
            t[np.abs(t - 2 * np.pi) < 1e-12] = 0.0
            orb.add(tuple(np.round(t, 11)))
        sizes.append(len(orb))
        for t in orb:
            assert t not in atoms, 'orbit collision'
            atoms[t] = wt / len(orb)
    T = np.array(list(atoms.keys())); v = np.array(list(atoms.values()))
    return T, v, sizes


def torus_checks(T, v, n):
    d = T.shape[1]
    A = np.array([k for k in itertools.product(range(1 - n, n), repeat=d) if sum(map(abs, k)) <= n - 1])
    E = np.sqrt(v)[:, None] * np.exp(1j * T @ A.T)
    gram_err = np.abs(E.conj().T @ E - np.eye(len(A))).max()
    m = len(A); q = m * v; eta = 1 - q
    P = E @ E.conj().T
    row_err = np.abs((np.abs(P) ** 2).sum(1) - np.abs(np.diag(P)) ** 2 - q * eta).max()
    return gram_err, m, eta, row_err


def report(name, pts, w, n, deg):
    d = pts.shape[1]
    mom = check_moments(pts, w, deg)
    delta, D = poly_defects(pts, w, n)
    T, v, sizes = lift(pts, w)
    g, m, eta, rerr = torus_checks(T, v, n)
    N, M = len(w), len(v)
    print(f"{name:28s} d={d} n={n} N={N} D={D} sumdelta={delta.sum():.10f} (N-D={N-D}) "
          f"mindelta={delta.min():.3e} | M={M} 2^dN={2**d*N} m={m} sumeta={eta.sum():.10f} (M-m={M-m}) "
          f"mineta={eta.min():.3e} gram_err={g:.1e} row_err={rerr:.1e} moment_err={mom:.1e} "
          f"orbit_sizes={sorted(set(sizes))}")
    ok = (abs(delta.sum() - (N - D)) < 1e-8 and delta.min() > -1e-10 and abs(eta.sum() - (M - m)) < 1e-8
          and eta.min() > -1e-10 and g < 1e-9 and rerr < 1e-9 and mom < 1e-10 and m <= M <= 2 ** d * N)
    return ok


def padua_lift_geometry(n):
    pts, w = padua(n)
    T, v, _ = lift(pts, w)
    X = n * T / (2 * np.pi)
    per = np.array([[a, b] for a in (-1, 0, 1) for b in (-1, 0, 1)]) * n
    Y = (X[None, :, :] + per[:, None, :]).reshape(-1, 2)
    # nearest distinct neighbour over periodic copies
    from scipy.spatial import cKDTree
    dist, _ = cKDTree(Y).query(X, k=2)
    lat = np.array([[1.0, 0.0], [0.5, n / (2 * (n + 1))]])
    coef = np.linalg.solve(lat.T, X.T).T
    lattice_err = np.abs(coef - np.round(coef)).max()
    return len(v), 2 * n * (n + 1), dist[:, 1].min(), lattice_err


def main():
    ok = True
    for n in (2, 3, 4, 5):
        ok &= report('3D Gauss-Cheb product', *product([cheb_gauss(n)] * 3), n, 2 * n - 1)
    for n in (2, 3, 4):
        ok &= report('3D Lobatto-Cheb product', *product([cheb_lobatto(n)] * 3), n, 2 * n - 1)
    for n in (2, 3, 4):
        ok &= report('3D Gauss x Lobatto x Radau', *product([cheb_gauss(n), cheb_lobatto(n), cheb_radau(n)]), n, 2 * n - 1)
    for n in (2, 3, 5, 8, 10):
        ok &= report('2D Padua', *padua(n), n, 2 * n - 1)
    for n in (10, 40):
        M, expect, mind, lerr = padua_lift_geometry(n)
        print(f"2D Padua scaled lift n={n}: M={M} (2n(n+1)={expect}) min periodic NN distance={mind:.6f} "
              f"(limit lattice NN=1/sqrt2={1/math.sqrt(2):.6f}) lattice-membership err={lerr:.1e}")
        ok &= (M == expect and lerr < 1e-9)
    print('ALL_OK' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
