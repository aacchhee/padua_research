"""Adversarial re-run (gen4-2): count local maxima of the Padua Lebesgue function lambda_n
with coarse-mesh detection + recursive local refinement + de-duplication, for n = 3..8.
Compares with the published table of Bialas-Ciez--De Marchi--Suder (arXiv 2605.23299):
interior/total = 7/15, 13/27, 14/25, 23/39, 27/42, 38/56 for n = 3..8.
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. Seconds to ~1 min per n. MEASURED in the stated scope only.
"""
import sys, time
import numpy as np
from scipy.ndimage import maximum_filter
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua, cheb_basis

PUBLISHED = {3: (7, 15), 4: (13, 27), 5: (14, 25), 6: (23, 39), 7: (27, 42), 8: (38, 56)}


class Leb:
    """Lebesgue function of Pad_n evaluated in Chebyshev angles (th, ph) in [0, pi]^2, x = cos th, y = cos ph."""

    def __init__(self, n):
        self.n = n
        P, w = padua(n)
        self.P, self.w = P, w
        V, _ = cheb_basis(P[:, 0], P[:, 1], n)
        self.V = V
        self.TnB = np.cos(n * np.arccos(np.clip(P[:, 0], -1, 1)))

    def __call__(self, th, ph):
        th = np.asarray(th, float).ravel(); ph = np.asarray(ph, float).ravel()
        X = np.cos(th); Y = np.cos(ph)
        out = np.empty(len(X)); ch = 4000
        for s in range(0, len(X), ch):
            Vg, _ = cheb_basis(X[s:s + ch], Y[s:s + ch], self.n)
            L = self.w[None, :] * (Vg @ self.V.T - np.outer(np.cos(self.n * th[s:s + ch]), self.TnB))
            out[s:s + ch] = np.sum(np.abs(L), axis=1)
        return out


def grid_maxima(f, th, ph):
    """Discrete strict-or-tie local maxima of f on the grid th x ph (3x3 neighbourhood). Returns (lam, mask)."""
    TH, PH = np.meshgrid(th, ph, indexing='ij')
    lam = f(TH, PH).reshape(TH.shape)
    mx = maximum_filter(lam, size=3, mode='nearest') == lam
    return lam, mx


def refine(f, t0, p0, h, depth=0, maxdepth=6, m=41, acc=None):
    """Recursive box refinement around (t0,p0) with half-width h in angle; collects converged maxima in acc."""
    if acc is None:
        acc = []
    th = np.linspace(max(0.0, t0 - h), min(np.pi, t0 + h), m)
    ph = np.linspace(max(0.0, p0 - h), min(np.pi, p0 + h), m)
    lam, mx = grid_maxima(f, th, ph)
    # interior maxima of the box only (box-boundary maxima mean the true max drifted out; follow the biggest one)
    inner = mx.copy(); inner[0, :] = inner[-1, :] = inner[:, 0] = inner[:, -1] = False
    I, J = np.where(inner)
    if len(I) == 0:
        # follow the global box max (on the box edge) with the same h, at most once per level
        i, j = np.unravel_index(np.argmax(lam), lam.shape)
        if depth < maxdepth:
            return refine(f, th[i], ph[j], h, depth + 1, maxdepth, m, acc)
        return acc
    hnew = 2.0 * (th[1] - th[0])
    for i, j in zip(I, J):
        if depth >= maxdepth or hnew < 1e-9:
            acc.append((th[i], ph[j], lam[i, j]))
        else:
            refine(f, th[i], ph[j], hnew, depth + 1, maxdepth, m, acc)
    return acc


def dedupe(pts, tol):
    out = []
    for t, p, v in sorted(pts, key=lambda z: -z[2]):
        if all(np.hypot(t - a, p - b) > tol for a, b, _ in out):
            out.append((t, p, v))
    return out


def is_local_max(f, t, p, r=2e-4, k=24):
    """Check f(t,p) >= f on a ring of radius r (in angle) restricted to [0,pi]^2."""
    ang = np.linspace(0, 2 * np.pi, k, endpoint=False)
    tt = np.clip(t + r * np.cos(ang), 0, np.pi); pp = np.clip(p + r * np.sin(ang), 0, np.pi)
    keep = (np.hypot(tt - t, pp - p) > 0.5 * r)
    v0 = f([t], [p])[0]; v = f(tt[keep], pp[keep])
    return bool(np.all(v <= v0 + 1e-12))


def count_interior(n, m_coarse, uniform=False):
    f = Leb(n)
    if uniform:
        g = np.arccos(np.linspace(1, -1, m_coarse))  # uniform in x,y -> angles
        g = np.sort(g)
    else:
        g = np.linspace(0, np.pi, m_coarse)
    lam, mx = grid_maxima(f, g, g)
    inner = mx.copy(); inner[0, :] = inner[-1, :] = inner[:, 0] = inner[:, -1] = False
    I, J = np.where(inner)
    coarse = len(I)
    h = 1.5 * max(np.diff(g).max(), 1e-6)
    acc = []
    for i, j in zip(I, J):
        refine(f, g[i], g[j], h, acc=acc)
    pts = dedupe(acc, tol=1e-4)
    # keep only interior points (angle strictly inside (0,pi)) that pass the ring test
    pts = [(t, p, v) for (t, p, v) in pts if 1e-3 < t < np.pi - 1e-3 and 1e-3 < p < np.pi - 1e-3]
    good = [(t, p, v) for (t, p, v) in pts if is_local_max(f, t, p)]
    return coarse, len(pts), len(good), good, lam.max()


def count_boundary(n, m1=40001):
    """Local maxima of lambda_n on the boundary of the square (edges + corners), as maxima of the closed-square function."""
    f = Leb(n)
    g = np.linspace(0, np.pi, m1)
    total = 0; details = []
    eps = 1e-4
    # four edges: th=0 (x=1), th=pi (x=-1), ph=0 (y=1), ph=pi (y=-1)
    edges = [('x=+1', lambda s: (np.zeros_like(s), s), lambda s: (np.full_like(s, eps), s)),
             ('x=-1', lambda s: (np.full_like(s, np.pi), s), lambda s: (np.full_like(s, np.pi - eps), s)),
             ('y=+1', lambda s: (s, np.zeros_like(s)), lambda s: (s, np.full_like(s, eps))),
             ('y=-1', lambda s: (s, np.full_like(s, np.pi)), lambda s: (s, np.full_like(s, np.pi - eps)))]
    corners = set()
    for name, on, off in edges:
        v = f(*on(g)); vin = f(*off(g))
        # 1D local maxima along the edge, interior of the edge
        loc = np.where((v[1:-1] >= v[:-2]) & (v[1:-1] >= v[2:]))[0] + 1
        # dedupe plateaus
        cnt = 0; kept = []
        for i in loc:
            if kept and i - kept[-1] <= 2:
                continue
            if vin[i] <= v[i] + 1e-12:
                kept.append(i); cnt += 1
        total += cnt; details.append((name, cnt))
        # corner endpoints: a corner is a max if it dominates both edge neighbours and the diagonal neighbour
        for idx, cname in ((0, name + '/start'), (m1 - 1, name + '/end')):
            nb = v[1] if idx == 0 else v[-2]
            if v[idx] >= nb and v[idx] >= vin[idx]:
                corners.add((name, idx))
    # corners counted once each: (x=+1,y=+1), (x=+1,y=-1), (x=-1,y=+1), (x=-1,y=-1)
    cpts = {(0.0, 0.0): 0, (0.0, np.pi): 0, (np.pi, 0.0): 0, (np.pi, np.pi): 0}
    ncorner = 0
    for (t, p) in cpts:
        v0 = f([t], [p])[0]
        tt = np.array([t + (eps if t == 0 else -eps), t, t + (eps if t == 0 else -eps)])
        pp = np.array([p, p + (eps if p == 0 else -eps), p + (eps if p == 0 else -eps)])
        if np.all(f(tt, pp) <= v0 + 1e-12):
            ncorner += 1
    return total, ncorner, details


if __name__ == '__main__':
    t0 = time.time()
    print('n | coarse mesh | coarse interior maxima | refined distinct | ring-verified interior | boundary(edges) | corners | total | published int/tot | time')
    for n in range(3, 9):
        rows = []
        for m_coarse, uni in ((401, False), (801, False), (801, True), (1601, False)):
            c, r, gd, good, lmax = count_interior(n, m_coarse, uni)
            b, nc, det = count_boundary(n)
            rows.append((m_coarse, 'uni' if uni else 'cheb', c, r, gd, b, nc, gd + b + nc))
            print(f'{n} | {m_coarse}^2 {"uniform" if uni else "cheb"} | {c} | {r} | {gd} | {b} | {nc} | {gd + b + nc} | {PUBLISHED[n][0]}/{PUBLISHED[n][1]} | {time.time() - t0:.0f}s   (edge detail {det}; Lambda_mesh {lmax:.4f})')
        if n == 8:
            # print the verified interior maxima for n = 8 (angles and values) for the record
            c, r, gd, good, lmax = count_interior(8, 1601, False)
            print('n=8 verified interior maxima (theta, phi, lambda), sorted by lambda:')
            for t, p, v in sorted(good, key=lambda z: -z[2]):
                print(f'   {t:.6f} {p:.6f} {v:.6f}   x={np.cos(t):+.5f} y={np.cos(p):+.5f}')
    print('elapsed', round(time.time() - t0, 1), 's')
