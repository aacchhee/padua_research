"""Adversarial re-run (gen4-2), second pass: n = 8 (and n = 5, 7) with tighter de-duplication (2e-6 rad), smaller
ring radius (1e-5 rad), deeper refinement, and a 3201^2 starting mesh; plus a crease diagnostic for n = 8: for each
verified interior maximum, the nearest partner maximum and the smallest |l_B| / ||grad l_B|| (distance to a crease).
Also prints the n = 7 edge maxima (positions/values) to compare with the published boundary count (42 - 27 = 15).
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED in the stated scope only.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2')
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
import adv_maxima_count as A
from gen4_tests import cheb_basis

PUB = A.PUBLISHED


def count_interior_tight(n, m_coarse, uniform=False, ring=1e-5, tol=2e-6, maxdepth=7):
    f = A.Leb(n)
    g = np.sort(np.arccos(np.linspace(1, -1, m_coarse))) if uniform else np.linspace(0, np.pi, m_coarse)
    lam, mx = A.grid_maxima(f, g, g)
    inner = mx.copy(); inner[0, :] = inner[-1, :] = inner[:, 0] = inner[:, -1] = False
    I, J = np.where(inner)
    h = 1.5 * np.diff(g).max()
    acc = []
    for i, j in zip(I, J):
        A.refine(f, g[i], g[j], h, maxdepth=maxdepth, acc=acc)
    pts = A.dedupe(acc, tol=tol)
    pts = [(t, p, v) for (t, p, v) in pts if 1e-3 < t < np.pi - 1e-3 and 1e-3 < p < np.pi - 1e-3]
    good = [(t, p, v) for (t, p, v) in pts if A.is_local_max(f, t, p, r=ring, k=32)]
    return len(I), len(pts), len(good), good


def crease_diag(n, good):
    """For each maximum: distance to nearest other maximum; min over B of |l_B|/|grad l_B| (angle units) = crease distance."""
    f = A.Leb(n)
    out = []
    for (t, p, v) in good:
        d_pair = min([np.hypot(t - a, p - b) for (a, b, _) in good if (a, b) != (t, p)] + [np.inf])
        # Lagrange values and finite-difference gradients in angles
        def lag(th, ph):
            X = np.cos([th]); Y = np.cos([ph])
            Vg, _ = cheb_basis(X, Y, n)
            return (f.w * (Vg @ f.V.T - np.outer(np.cos(n * np.array([th])), f.TnB)))[0]
        e = 1e-6
        L0 = lag(t, p); Lt = (lag(t + e, p) - lag(t - e, p)) / (2 * e); Lp = (lag(t, p + e) - lag(t, p - e)) / (2 * e)
        gnorm = np.hypot(Lt, Lp) + 1e-300
        dist = np.abs(L0) / gnorm
        out.append((t, p, v, d_pair, dist.min(), int(np.argmin(dist))))
    return out


if __name__ == '__main__':
    t0 = time.time()
    for n in (5, 7, 8):
        print(f'--- n = {n}: published interior/total {PUB[n]}')
        for m_coarse, uni in ((801, False), (801, True), (1601, False), (1601, True), (3201, False)):
            c, r, gd, good = count_interior_tight(n, m_coarse, uni)
            print(f'  coarse {m_coarse}^2 {"uniform" if uni else "cheb"}: coarse {c}, refined distinct {r}, ring-verified {gd}   [{time.time() - t0:.0f}s]')
        if n == 8:
            diag = crease_diag(8, good)
            print('  n=8 maxima from the 3201^2 start: theta, phi, lambda, dist to nearest other max, crease distance |l_B|/|grad l_B| (min over B), B index')
            for row in sorted(diag, key=lambda z: z[3]):
                print('   %.6f %.6f %.5f  pair %.2e  crease %.2e  B=%d' % row)
            print('  union of verified maxima over all five starts (dedupe 2e-6):')
            allpts = []
            for m_coarse, uni in ((801, False), (801, True), (1601, False), (1601, True), (3201, False)):
                allpts += count_interior_tight(8, m_coarse, uni)[3]
            U = A.dedupe(allpts, tol=2e-6)
            print('   union count', len(U))
    # n = 7 edge maxima detail
    print('--- n = 7 edge maxima (1D grid 40001 per edge, must also decrease into the interior):')
    f = A.Leb(7); g = np.linspace(0, np.pi, 40001); eps = 1e-4
    for name, on, off in (('x=+1', lambda s: (0 * s, s), lambda s: (0 * s + eps, s)),
                          ('x=-1', lambda s: (0 * s + np.pi, s), lambda s: (0 * s + np.pi - eps, s)),
                          ('y=+1', lambda s: (s, 0 * s), lambda s: (s, 0 * s + eps)),
                          ('y=-1', lambda s: (s, 0 * s + np.pi), lambda s: (s, 0 * s + np.pi - eps))):
        v = f(*on(g)); vin = f(*off(g))
        loc = np.where((v[1:-1] >= v[:-2]) & (v[1:-1] >= v[2:]))[0] + 1
        print('  ', name, [(round(float(g[i]), 5), round(float(v[i]), 5), bool(vin[i] <= v[i] + 1e-12)) for i in loc])
    print('elapsed %.0f s' % (time.time() - t0))
