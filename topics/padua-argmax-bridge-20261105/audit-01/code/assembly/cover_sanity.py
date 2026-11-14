"""Auditor float sanity check (MEASURED only, not a proof premise).

Independently written from the definitions in PD-T364 phase-structure.md
and C13 statements. Checks, for small n:
 1. cardinal property of the corrected kernel at Padua nodes;
 2. rectangle-based odd-vertex chart exists with rho<=pi and physical phases;
 3. lambda = S(alpha,beta) - Delta, Delta>=0, at random, boundary, node,
    collision points, for EVERY physical odd centre with rho<=pi (not only
    the chosen one);
 4. node points have min rho over odd centres exactly pi;
 5. corner values, parity-correct equality set and reflection symmetry;
 6. endpoint odd centres: all physical phases are inward.
"""
import itertools, math, random, sys
import numpy as np

def G(n, u, v):
    a = np.arange(n + 1)
    cu = np.cos(np.outer(a, np.atleast_1d(u)))   # (n+1, P)
    cv = np.cos(np.outer(a, np.atleast_1d(v)))
    h = np.where(a == 0, 1.0, 2.0)
    H = np.outer(h, h)
    mask = (a[:, None] + a[None, :]) <= n
    C = H * mask
    val = np.einsum('ap,ab,bp->p', cu, C, cv)
    return val - np.cos(n * np.atleast_1d(u))

def nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]

def weight(n, j, k):
    m = n + 1; N = n * m
    e = 0.5 if j in (0, n) else 1.0
    f = 0.5 if k in (0, m) else 1.0
    return 2 * e * f / N

def cardinals(n, th, ph):
    m = n + 1
    out = []
    for (j, k) in nodes(n):
        aj, bk = j * math.pi / n, k * math.pi / m
        g = [G(n, np.array([th + s * aj]), np.array([ph + t * bk]))[0]
             for s in (1, -1) for t in (1, -1)]
        out.append((weight(n, j, k), g))
    return out

def lam_delta(n, th, ph):
    L = 0.0; M = 0.0
    for w, g in cardinals(n, th, ph):
        L += abs(w / 4 * sum(g)); M += w / 4 * sum(abs(x) for x in g)
    return L, M - L

def S(n, al, be):
    m = n + 1; N = n * m
    r, s = np.meshgrid(np.arange(2 * n), np.arange(2 * m), indexing='ij')
    sel = ((r + s) % 2 == 1)
    u = (r[sel] * math.pi + al) / n; v = (s[sel] * math.pi + be) / m
    return np.abs(G(n, u, v)).sum() / (2 * N)

def phys_odd_charts(n, th, ph, rmax=math.pi + 1e-12):
    m = n + 1; res = []
    for J in range(n + 1):
        for K in range(m + 1):
            if (J + K) % 2 == 1:
                al = n * th - J * math.pi; be = m * ph - K * math.pi
                if abs(al) + abs(be) <= rmax:
                    res.append((J, K, al, be))
    return res

def rect_chart(n, th, ph):
    m = n + 1
    X, Y = th * n / math.pi, ph * m / math.pi
    j = min(int(math.floor(X)), n - 1); k = min(int(math.floor(Y)), m - 1)
    x, y = X - j, Y - k
    cands = [(j, k, x + y), (j + 1, k + 1, 2 - x - y), (j + 1, k, 1 - x + y), (j, k + 1, 1 + x - y)]
    odd = [c for c in cands if (c[0] + c[1]) % 2 == 1]
    assert len(odd) == 2 and abs(odd[0][2] + odd[1][2] - 2) < 1e-12
    return min(odd, key=lambda c: c[2])

def main():
    random.seed(1)
    worst = dict(card=0, ident=0, negdelta=0, rho=0, sym=0)
    for n in (2, 3, 4, 5, 6, 7, 8):
        m = n + 1
        # 1 cardinal property
        nd = nodes(n)
        for (j, k) in nd:
            th, ph = j * math.pi / n, k * math.pi / m
            vals = [w / 4 * sum(g) for w, g in cardinals(n, th, ph)]
            for idx, (jj, kk) in enumerate(nd):
                worst['card'] = max(worst['card'], abs(vals[idx] - (1.0 if (jj, kk) == (j, k) else 0.0)))
        # points: random, boundary, nodes, collisions, mesh points
        pts = [(random.uniform(0, math.pi), random.uniform(0, math.pi)) for _ in range(150)]
        pts += [(0.0, random.uniform(0, math.pi)) for _ in range(10)] + [(math.pi, random.uniform(0, math.pi)) for _ in range(10)]
        pts += [(random.uniform(0, math.pi), 0.0) for _ in range(10)] + [(random.uniform(0, math.pi), math.pi) for _ in range(10)]
        pts += [(j * math.pi / n, k * math.pi / m) for j in range(n + 1) for k in range(m + 1)]
        pts += [(t, t) for t in np.linspace(0, math.pi, 7)] + [(t, math.pi - t) for t in np.linspace(0, math.pi, 7)]
        # tie points x+y=1 in a rectangle
        pts += [((0.3 + 1) * math.pi / n, (0.7 + 1) * math.pi / m)]
        for th, ph in pts:
            J, K, rho_n = rect_chart(n, th, ph)
            worst['rho'] = max(worst['rho'], rho_n - 1)
            lam, dl = lam_delta(n, th, ph)
            worst['negdelta'] = max(worst['negdelta'], -dl)
            charts = phys_odd_charts(n, th, ph)
            assert any(c[0] == J and c[1] == K for c in charts)
            for (J2, K2, al, be) in charts:
                assert -1e-12 <= th <= math.pi + 1e-12
                worst['ident'] = max(worst['ident'], abs(lam - (S(n, al, be) - dl)))
        # 4 nodes: min rho = pi
        for (j, k) in nd:
            th, ph = j * math.pi / n, k * math.pi / m
            rr = min(abs(n * th - J * math.pi) + abs(m * ph - K * math.pi)
                     for J in range(n + 1) for K in range(m + 1) if (J + K) % 2)
            assert abs(rr - math.pi) < 1e-9, (n, j, k, rr)
        # 5 corners
        corners = {(-1, -1): (math.pi, math.pi), (1, -1): (0.0, math.pi), (-1, 1): (math.pi, 0.0), (1, 1): (0.0, 0.0)}
        vals = {c: lam_delta(n, *tp)[0] for c, tp in corners.items()}
        Lc = vals[(-1, -1)]
        eq = sorted(c for c, v in vals.items() if abs(v - Lc) < 1e-9)
        expect = sorted([(-1, -1), (1, -1)] if n % 2 == 0 else [(-1, -1), (-1, 1)])
        assert eq == expect, (n, vals)
        assert abs(S(n, 0, 0) - Lc) < 1e-9
        # reflection symmetry at random points
        for _ in range(30):
            th, ph = random.uniform(0, math.pi), random.uniform(0, math.pi)
            a = lam_delta(n, th, ph)[0]
            b = lam_delta(n, math.pi - th, ph)[0] if n % 2 == 0 else lam_delta(n, th, math.pi - ph)[0]
            worst['sym'] = max(worst['sym'], abs(a - b))
        # 6 endpoint odd centres: physical phases inward
        ends = [(n, m), (0, m) if n % 2 == 0 else (n, 0)]
        for (J, K) in ends:
            for _ in range(200):
                al, be = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
                th, ph = (J * math.pi + al) / n, (K * math.pi + be) / m
                physical = 0 <= th <= math.pi and 0 <= ph <= math.pi
                inward = (al >= 0 if J == 0 else al <= 0) and (be >= 0 if K == 0 else be <= 0)
                assert physical == inward
        print(n, 'Lc=%.12f' % Lc, 'max-over-square-sample=%.12f' % max(lam_delta(n, *p)[0] for p in pts))
    print('worst', worst)

if __name__ == '__main__':
    main()
