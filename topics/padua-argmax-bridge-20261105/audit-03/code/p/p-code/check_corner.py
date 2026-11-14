"""Referee checks for paper Sections 2-3 (P-audit, Claude Opus 5.5).
Numerical (MEASURED) checks of: Lemma 2.1 cardinal kernel, (cu:positive),
(cu:exact), (cu:square), L_n midpoint form, (cu:deform), kappa series and
coarse input, (cu:cancel), S_u, and the sharp expansion residual.
Run: PYTHONPATH=<pylib> python3 -I? no: python3 check_corner.py
"""
import sys, math, time
import numpy as np
import mpmath as mp
mp.mp.dps = 40
t0 = time.process_time()
out = {}

# ---------- Lemma 2.1 by an independent linear solve ----------
def padua_nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]

def cardinal_matrix_direct(n, pts):
    """Cardinals by solving Vandermonde in the T_p T_q basis (independent of Lemma 2.1)."""
    m = n + 1
    nodes = padua_nodes(n)
    X = np.array([math.cos(j * math.pi / n) for j, k in nodes])
    Y = np.array([math.cos(k * math.pi / m) for j, k in nodes])
    modes = [(p, q) for p in range(n + 1) for q in range(n + 1 - p)]
    V = np.array([[math.cos(p * math.acos(max(-1, min(1, x)))) * math.cos(q * math.acos(max(-1, min(1, y))))
                   for (p, q) in modes] for x, y in zip(X, Y)])
    Vinv = np.linalg.inv(V)  # columns -> cardinal coefficients
    res = []
    for (x, y) in pts:
        row = np.array([math.cos(p * math.acos(x)) * math.cos(q * math.acos(y)) for (p, q) in modes])
        res.append(row @ Vinv)  # values L_B(x,y) for all nodes B
    return nodes, np.array(res)

def cardinal_lemma(n, x, y):
    m = n + 1
    nodes = padua_nodes(n)
    vals = []
    for j, k in nodes:
        th, ph = j * math.pi / n, k * math.pi / m
        eps = 0.5 if j in (0, n) else 1.0
        eta = 0.5 if k in (0, m) else 1.0
        w = 2 * eps * eta / (n * m)
        K = 0.0
        for p in range(n + 1):
            for q in range(n + 1 - p):
                nu = (1 if p == 0 else 2) * (1 if q == 0 else 2)
                K += nu * math.cos(p * math.acos(x)) * math.cos(p * th) * math.cos(q * math.acos(y)) * math.cos(q * ph)
        K -= math.cos(n * math.acos(x)) * math.cos(n * th)
        vals.append(w * K)
    return np.array(vals)

errs = []
for n in range(1, 9):
    pts = [(-1.0, -1.0), (0.3, -0.7), (0.91, 0.2)]
    nodes, D = cardinal_matrix_direct(n, pts)
    for i, (x, y) in enumerate(pts):
        errs.append(np.max(np.abs(D[i] - cardinal_lemma(n, x, y))))
out['lemma2.1_maxdiff_n1..8'] = float(max(errs))

# ---------- corner value, exact identities ----------
def lam_corner_direct(n):
    return float(np.sum(np.abs(cardinal_lemma(n, -1.0, -1.0))))

def lam_corner_positive(n):  # (cu:positive), mpmath
    m = n + 1
    s = mp.mpf(0)
    for j in range(n + 1):
        for k in range(n + 1):
            if (j + k) % 2 == 1:
                eps = mp.mpf(1) / 2 if j in (0, n) else 1
                eta = mp.mpf(1) / 2 if k in (0, m) else 1
                u, v = j * mp.pi / n, k * mp.pi / m
                s += eps * eta * (1 + mp.cos(v)) / abs(mp.cos(u) - mp.cos(v))
    return 4 * s / (n * m) + mp.mpf(1) / m

def wfun(x): return mp.cot(mp.pi * x / 2)
def Bfun(x): return mp.cot(mp.pi * x) - 1 / (mp.pi * x) + 1 / (mp.pi * (1 - x))

def exact_ids(n):
    m = n + 1
    first = 1 - mp.mpf(2 * n) / m
    Hm = mp.mpf(0); V = mp.mpf(0); tsum = mp.mpf(0)
    for r in range(1, m):
        x = mp.mpf(r) / m; s = m - r; al = (1 - x) / 2
        T = mp.fsum(mp.cot(mp.pi * (l + al) / n) for l in range(r))
        tsum += wfun(x) * T
        D = mp.digamma(r + al) + mp.digamma(s - al) - mp.digamma(m - al) - mp.digamma(al)
        Hm += wfun(x) * D
        V += wfun(x) * mp.fsum(Bfun((l + al) / n) for l in range(r))
    first += 4 * tsum / (n * m)
    second = -1 + mp.mpf(2) / m + 4 * Hm / (mp.pi * m) + 4 * V / (n * m)
    return first, second

idiff = []
for n in [2, 3, 4, 5, 8, 11, 16, 25]:
    d = lam_corner_direct(n) if n <= 8 else None
    p = lam_corner_positive(n)
    f, s = exact_ids(n)
    idiff.append((n, None if d is None else float(abs(d - p)), float(abs(p - f)), float(abs(f - s))))
out['corner_identities(n,|direct-positive|,|positive-exact1|,|exact1-exact2|)'] = idiff

# (cu:square) and L_n forms
sq = []
for n in [2, 3, 6, 7, 20, 21]:
    s = mp.mpf(0)
    for j in range(n + 1):
        for k in range(n + 1):
            if (j + k) % 2 == 1:
                ej = mp.mpf(1) / 2 if j in (0, n) else 1
                ek = mp.mpf(1) / 2 if k in (0, n) else 1
                u, v = j * mp.pi / n, k * mp.pi / n
                s += ej * ek * (1 + mp.cos(v)) / abs(mp.cos(u) - mp.cos(v))
    lhs = 4 * s / n**2
    Ln = 2 * mp.fsum((mp.mpf(1) / 2 if r == n else 1) / mp.sin(r * mp.pi / (2 * n)) for r in range(1, n + 1, 2)) / n
    Ln2 = mp.fsum(mp.cot((2 * r - 1) * mp.pi / (4 * n)) for r in range(1, n + 1)) / n
    sq.append((n, float(abs(lhs - Ln**2)), float(abs(Ln - Ln2))))
out['square_ref(n,|sum-L^2|,|L-midpointform|)'] = sq

# (cu:deform): max over (j,k) of |f(th_j,ph_k)-f(th_j,th_k)| * 2 l^2/(pi^2 n)
def deform_ratio(n):
    m = n + 1
    j = np.arange(n + 1)[:, None]; k = np.arange(n + 1)[None, :]
    mask = ((j + k) % 2 == 1)
    u = j * np.pi / n; v1 = k * np.pi / m; v0 = k * np.pi / n
    with np.errstate(divide='ignore', invalid='ignore'):
        f1 = (1 + np.cos(v1)) / np.abs(np.cos(u) - np.cos(v1))
        f0 = (1 + np.cos(v0)) / np.abs(np.cos(u) - np.cos(v0))
        d = np.abs(f1 - f0)
        l = np.abs(j - k)
        r = d * 2 * l**2 / (np.pi**2 * n)
    r = np.where(mask & np.isfinite(r), r, 0)
    return float(r.max())
out['deform_max_ratio(<=1 required)'] = {n: deform_ratio(n) for n in [2, 3, 5, 10, 41, 100, 400, 1000]}

# ---------- kappa ----------
def kappa_integral():
    def integrand(t):
        if t == 0: return mp.mpf(0)
        S = mp.nsum(lambda l: 1 / ((2 * l + 1) * ((2 * l + 1)**2 - t**2)), [0, mp.inf])
        return t**2 * mp.cot(mp.pi * t / 2) * S
    return 8 / mp.pi * mp.quad(integrand, [0, mp.mpf(1) / 2, 1])

def kappa_series(K):
    a = [mp.mpf(1)] + [1 - 2 * mp.fsum(mp.zeta(2 * r) / 4**r for r in range(1, p + 1)) for p in range(1, K + 1)]
    b = [7 * mp.zeta(3) / 8] + [(1 - mp.mpf(2)**(-2 * q - 3)) * mp.zeta(2 * q + 3) - (1 - mp.mpf(2)**(-2 * q - 1)) * mp.zeta(2 * q + 1) for q in range(1, K + 1)]
    c = [mp.fsum(a[p] * b[k - p] for p in range(k + 1)) for k in range(K + 1)]
    S = 8 / mp.pi**2 * mp.fsum(c[k] / (k + 1) for k in range(K + 1))
    tail = mp.mpf(8) / (3 * (K + 2) * 4**(K + 1))
    return S, tail, c

kI = kappa_integral()
kS, tail64, c = kappa_series(64)
out['kappa_integral'] = mp.nstr(kI, 20)
out['kappa_series64'] = mp.nstr(kS, 20)
out['c_k first 7'] = [mp.nstr(x, 12) for x in c[:7]]
d = mp.euler + mp.log(8 / mp.pi)
Cstar = 4 * d**2 / mp.pi**2 + kI
out['Cstar'] = mp.nstr(Cstar, 15)
out['coarse_input_margins(k-0.9, 0.92-k, 1.847-C*)'] = [mp.nstr(kI - mp.mpf(9) / 10, 6), mp.nstr(mp.mpf(23) / 25 - kI, 6), mp.nstr(mp.mpf(1847) / 1000 - Cstar, 6)]
# how many series terms suffice by hand for the coarse input?
small = []
for K in range(2, 9):
    S, tl, _ = kappa_series(K)
    small.append((K, mp.nstr(S, 10), mp.nstr(tl, 4), bool(S - tl > mp.mpf(9) / 10 and S + tl < mp.mpf(23) / 25 and 4 * d**2 / mp.pi**2 + S + tl < mp.mpf(1847) / 1000)))
out['K_needed(K,partial,tailbound,coarse input implied)'] = small
# interval version for the smallest K that works
mp.iv.dps = 30
def kappa_series_iv(K):
    iv = mp.iv
    zeta = lambda s: iv.mpf([mp.zeta(s, ) - mp.mpf(10)**-25, mp.zeta(s) + mp.mpf(10)**-25])
    a = [iv.mpf(1)] + [1 - 2 * sum((zeta(2 * r) / 4**r for r in range(1, p + 1)), iv.mpf(0)) for p in range(1, K + 1)]
    b = [7 * zeta(3) / 8] + [(1 - iv.mpf(2)**(-2 * q - 3)) * zeta(2 * q + 3) - (1 - iv.mpf(2)**(-2 * q - 1)) * zeta(2 * q + 1) for q in range(1, K + 1)]
    cc = [sum((a[p] * b[k - p] for p in range(k + 1)), iv.mpf(0)) for k in range(K + 1)]
    S = 8 / iv.pi**2 * sum((cc[k] / (k + 1) for k in range(K + 1)), iv.mpf(0))
    tl = iv.mpf(8) / (3 * (K + 2) * 4**(K + 1))
    return S - tl, S + tl
lo, hi = kappa_series_iv(5)
out['iv K=5 kappa enclosure'] = (mp.nstr(lo.a, 12), mp.nstr(hi.b, 12))

# ---------- (cu:cancel), S_u, beta constants ----------
a_ = 2 / mp.pi
I1 = mp.quad(lambda x: wfun(x) / (1 - x) - a_ / x, [0, 1])
I2 = mp.quad(lambda x: x * wfun(x), [0, 1])
IB = mp.quad(lambda x: x * wfun(x) * Bfun(x), [0, mp.mpf(1) / 2, 1])
out['cancel_identity_diff'] = mp.nstr(2 * IB - a_ * I1 - (a_**2 - 1 + a_**2 * mp.log(mp.pi / 2)), 5)
Su = mp.nsum(lambda r: mp.psi(1, r + mp.mpf(1) / 2) - 1 / r, [1, mp.inf])
out['S_u_diff'] = mp.nstr(Su - (1 + 2 * mp.log(2) - mp.pi**2 / 4), 5)
out['psi(1/2) check'] = mp.nstr(mp.digamma(mp.mpf(1) / 2) + mp.euler + 2 * mp.log(2), 5)

# ---------- sharp expansion residual ----------
def lam_corner_fast(n):
    """(cu:exact) first identity in float64, O(n^2)."""
    m = n + 1
    r = np.arange(1, m)
    x = r / m
    al = (1 - x) / 2
    w = 1 / np.tan(np.pi * x / 2)
    tot = 0.0
    for rr, a_r, ww in zip(r, al, w):
        tot += ww * np.sum(1 / np.tan(np.pi * (np.arange(rr) + a_r) / n))
    return 1 - 2 * n / m + 4 * tot / (n * m)

kf = float(kI); af = 2 / math.pi; df = float(d)
res = []
for n in [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
    N = n + 0.5
    L = lam_corner_fast(n)
    A = af * (math.log(N) + df)
    r_n = L - A * A - kf + 1 / N
    res.append((n, L, r_n, r_n * N * N / math.log(N)))
out['expansion_residual(n,Lambda_c,r_n,r_n*N^2/logN)'] = res
out['check_fast_vs_mp(n=25)'] = float(abs(lam_corner_fast(25) - lam_corner_positive(25)))
out['cpu_s'] = time.process_time() - t0
for k, v in out.items():
    print(k, ':', v)
