"""C3 independent checks: reflection geometry, odd-center cover, S_n identity,
pair projections, symmetries, divided-difference kernel, A(u,v) numerator.
Auditor-written; float64 numerics (MEASURED-type sanity checks) plus exact
Fraction enumeration for the cover geometry."""
import numpy as np, itertools, random
from fractions import Fraction as Fr

rng = np.random.default_rng(20261108)

def Gn(n, u, v):
    u = np.asarray(u, float); v = np.asarray(v, float)
    tot = np.zeros(np.broadcast(u, v).shape)
    for p in range(n + 1):
        nup = 1.0 if p == 0 else 2.0
        cu = np.cos(p * u)
        for q in range(n + 1 - p):
            nuq = 1.0 if q == 0 else 2.0
            tot = tot + nup * nuq * cu * np.cos(q * v)
    return tot - np.cos(n * u)

def Gn_dd(n, u, v):
    """divided-difference form [P(cos u)-P(cos v)]/(cos u - cos v) - cos(nu), P=T_{n+1}+T_n"""
    X, Y = np.cos(u), np.cos(v)
    P = lambda t: np.cos((n + 1) * t) + np.cos(n * t)
    return (P(u) - P(v)) / (X - Y) - np.cos(n * u)

def nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]

def ew(j, n):
    return 0.5 if j in (0, n) else 1.0

def cardinals(n, th, ph):
    m = n + 1; N = n * m
    vals = []
    for (j, k) in nodes(n):
        w = 2 * ew(j, n) * ew(k, m) / N
        g = [Gn(n, th + s * j * np.pi / n, ph + e * k * np.pi / m) for s in (1, -1) for e in (1, -1)]
        vals.append((w, g))
    return vals

def S_n(n, al, be):
    m = n + 1; N = n * m
    tot = 0.0
    for r in range(2 * n):
        for s in range(2 * m):
            if (r + s) % 2 == 1:
                tot += abs(Gn(n, (r * np.pi + al) / n, (s * np.pi + be) / m))
    return tot / (2 * N)

def H(n, r, s, al, be):
    m = n + 1
    return Gn(n, (r * np.pi + al) / n, (s * np.pi + be) / m)

def dfun(z, w):
    return abs(z) + abs(w) - abs(z + w)

def Qv(n, K, al, be):
    m = n + 1; N = n * m
    tot = 0.0
    for r in range(2 * n):
        for s in range(2 * m):
            if (r + s) % 2 == 1:
                tot += dfun(H(n, r, s, al, be), H(n, r, (2 * K - s) % (2 * m), al, be))
    return tot / (4 * N)

def Qh(n, J, al, be):
    m = n + 1; N = n * m
    tot = 0.0
    for r in range(2 * n):
        for s in range(2 * m):
            if (r + s) % 2 == 1:
                tot += dfun(H(n, r, s, al, be), H(n, (2 * J - r) % (2 * n), s, al, be))
    return tot / (4 * N)

report = []
def rec(msg):
    print(msg); report.append(msg)

# 1. cardinal property at nodes and divided-difference agreement
for n in (2, 3, 4, 5):
    m = n + 1
    nd = nodes(n)
    maxerr = 0.0
    for (j0, k0) in nd:
        th, ph = j0 * np.pi / n, k0 * np.pi / m
        for idx, (w, g) in enumerate(cardinals(n, th, ph)):
            val = w / 4 * sum(g)
            maxerr = max(maxerr, abs(val - (1.0 if nd[idx] == (j0, k0) else 0.0)))
    uu = rng.uniform(0, 7, 200); vv = rng.uniform(0, 7, 200)
    dd = np.max(np.abs(Gn(n, uu, vv) - Gn_dd(n, uu, vv)))
    rec(f"n={n}: cardinal delta max err {maxerr:.2e}; divided-difference form max diff {dd:.2e}; #nodes={len(nd)} dim={(n+1)*(n+2)//2}")

# 2. odd-center cover: exact enumeration of rectangles and fine rational grid
for n in range(2, 9):
    m = n + 1
    # each mesh rectangle [J,J+1]x[K,K+1] in index units
    for J in range(n):
        for K in range(m):
            verts = [(J, K), (J + 1, K), (J, K + 1), (J + 1, K + 1)]
            odd = [v for v in verts if (v[0] + v[1]) % 2 == 1]
            assert len(odd) == 2 and odd[0][0] != odd[1][0] and odd[0][1] != odd[1][1], (n, J, K)
            # distances in fractional units sum to 2 at sample points
            for t in [Fr(i, 7) for i in range(8)]:
                for v in [Fr(i, 5) for i in range(6)]:
                    P = (J + t, K + v)
                    ds = [abs(P[0] - o[0]) + abs(P[1] - o[1]) for o in odd]
                    assert ds[0] + ds[1] == 2, (n, J, K, t, v)
    # every point of a fine grid is covered by some odd center at L1 index distance <=1
    D = 12
    bad = 0; ties = 0
    for a in range(n * D + 1):
        for b in range(m * D + 1):
            P = (Fr(a, D), Fr(b, D))
            c = [(J, K) for J in range(n + 1) for K in range(m + 1) if (J + K) % 2 == 1 and abs(P[0] - J) + abs(P[1] - K) <= 1]
            if not c: bad += 1
            if len(c) > 1: ties += 1
    rec(f"n={n}: every mesh rectangle has exactly two odd vertices, opposite; L1 distances sum to 2 (exact); fine-grid uncovered points={bad}; tie points={ties}")

# 3. lambda_n = S_n - Delta, Delta >= max(Qh,Qv) (eligible) for random points/charts, small n
for n in (2, 3, 4, 5, 6):
    m = n + 1; N = n * m
    worst_id = 0.0; worst_proj = 1e9; cnt = 0
    for trial in range(25):
        th = rng.uniform(0, np.pi); ph = rng.uniform(0, np.pi)
        # choose an odd center covering the point
        tt, vv = n * th / np.pi, m * ph / np.pi
        cands = [(J, K) for J in range(n + 1) for K in range(m + 1) if (J + K) % 2 == 1 and abs(tt - J) + abs(vv - K) <= 1 + 1e-12]
        J, K = random.Random(trial).choice(cands)
        al, be = n * th - J * np.pi, m * ph - K * np.pi
        cv = cardinals(n, th, ph)
        lam = sum(abs(w / 4 * sum(g)) for w, g in cv)
        Sdir = sum(w / 4 * sum(abs(x) for x in g) for w, g in cv)
        Delta = Sdir - lam
        Sper = S_n(n, al, be)
        worst_id = max(worst_id, abs(Sdir - Sper))
        projs = []
        if 0 < J < n: projs.append(Qh(n, J, al, be))
        if 0 < K < m: projs.append(Qv(n, K, al, be))
        for pj in projs:
            worst_proj = min(worst_proj, Delta - pj); cnt += 1
    rec(f"n={n}: max |sum_jk w/4 sum|g| - S_n(periodic)|={worst_id:.2e}; min(Delta - eligible projection) over {cnt} = {worst_proj:.3e} (>= -1e-12 expected)")

# 4. S_n symmetries and corner identity
for n in (3, 4, 6):
    m = n + 1
    errs = []
    for t in range(6):
        al, be = rng.uniform(-4, 4), rng.uniform(-4, 4)
        base = S_n(n, al, be)
        errs.append(abs(S_n(n, -al, be) - base)); errs.append(abs(S_n(n, al, -be) - base))
        errs.append(abs(S_n(n, al + 2 * np.pi, be) - base))
        errs.append(abs(S_n(n, al + np.pi, be + np.pi) - base))
        errs.append(abs(S_n(n, np.pi - al, np.pi - be) - base))
    # corner: nonnode corner (-1,-1) => theta=phi=pi, center (n,m)
    cv = cardinals(n, np.pi, np.pi)
    lam_c = sum(abs(w / 4 * sum(g)) for w, g in cv)
    rec(f"n={n}: S_n symmetry max err {max(errs):.2e}; S_n(0,0)={S_n(n,0,0):.12f} vs Lambda_c={lam_c:.12f}")

# 5. numerator identity A(u,v) for vertical half-kernels
worst = 0.0
for n in (5, 8, 13):
    m = n + 1
    for t in range(200):
        K = int(rng.integers(1, m)); J = int(rng.integers(0, n + 1))
        if (J + K) % 2 == 0: J = (J + 1) % (n + 1) if J < n else J - 1
        if (J + K) % 2 == 0: continue
        al, be = rng.uniform(-1, 1), rng.uniform(-1, 1)
        k = int(rng.integers(0, m + 1)); r = int(rng.integers(0, 2 * n))
        if (r + k) % 2 != J % 2: r = (r + 1) % (2 * n)
        u = (r * np.pi + al) / n
        phi = (K * np.pi + be) / m
        for sgn in (1, -1):
            v = phi + sgn * k * np.pi / m
            if abs(np.cos(u) - np.cos(v)) < 1e-3: continue
            Vh = (-1) ** r * Gn(n, u, v) / 2
            a = (np.cos(al) + np.cos(be)) / 2
            A = a * (1 + np.cos(v)) - np.sin(al) / 2 * np.sin(u) + np.sin(be) / 2 * np.sin(v)
            worst = max(worst, abs(Vh - A / (np.cos(u) - np.cos(v))))
rec(f"vertical half-kernel V = A(u,v)/(cos u - cos v) with a=(cos al+cos be)/2: max err {worst:.2e}")

# horizontal version
worst = 0.0
for n in (5, 8, 13):
    m = n + 1
    for t in range(200):
        J = int(rng.integers(1, n)); K = int(rng.integers(0, m + 1))
        if (J + K) % 2 == 0: K = K + 1 if K < m else K - 1
        al, be = rng.uniform(-1, 1), rng.uniform(-1, 1)
        j = int(rng.integers(0, n + 1)); s = int(rng.integers(0, 2 * m))
        if (s + j) % 2 != K % 2: s = (s + 1) % (2 * m)
        v = (s * np.pi + be) / m
        th = (J * np.pi + al) / n
        for sgn in (1, -1):
            u = th + sgn * j * np.pi / n
            if abs(np.cos(u) - np.cos(v)) < 1e-3: continue
            Vh = (-1) ** (J + j) * Gn(n, u, v) / 2
            a = (np.cos(al) + np.cos(be)) / 2
            A = a * (1 + np.cos(v)) - np.sin(al) / 2 * np.sin(u) + np.sin(be) / 2 * np.sin(v)
            worst = max(worst, abs(Vh - A / (np.cos(u) - np.cos(v))))
rec(f"horizontal half-kernel with common sign (-1)^(J+j): max err {worst:.2e}")

# 6. endpoint identity sum_{j,sigma: sigma j = r mod 2n} e_j = 1
okall = True
for n in range(1, 12):
    for r in range(2 * n):
        tot = sum(ew(j, n) for j in range(n + 1) for sg in (1, -1) if (sg * j - r) % (2 * n) == 0)
        okall &= (tot == 1)
        tot1 = sum(ew(j, n) for j in range(n + 1) if (j - r) % (2 * n) == 0)  # sigma fixed +1
rec(f"endpoint identity (sum over j AND sigma) holds for n<=11: {okall}; with sigma fixed at +1 it fails at r=0 (value {sum(ew(j,3) for j in range(4) if j%6==0)})")
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(report) + '\n')
