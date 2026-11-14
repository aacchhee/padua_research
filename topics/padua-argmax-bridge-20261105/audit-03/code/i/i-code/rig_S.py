"""PROTOTYPE rigorous binary64 interval enclosure of S_n(pi a, pi b) WITHOUT Arb/MPFR/libm.
Trust base: IEEE-754 round-to-nearest for numpy float64 +,-,*,/ (each result widened by one
ulp with np.nextafter, which contains the exact result of the operation on the float inputs),
Python integers/Fractions for exact argument reduction, and an own Taylor polynomial for sin
with an explicit Lagrange remainder.  Formula: paper ul:primitive with
G_n = R_{n+1}(S)R_{n+1}(T) + R_n(S)R_n(T) - cos(n u).
Status of results produced with this file: ENCLOSED only if the IEEE assumption holds; this is a
prototype for a proposal, not a frozen checker (no review, no corruption controls)."""
import numpy as np
from fractions import Fraction as F
from math import lcm, factorial
INF = np.inf
def dn(x): return np.nextafter(x, -INF)
def up(x): return np.nextafter(x, INF)
PI_LO, PI_HI = np.float64(np.pi), up(np.float64(np.pi))     # np.pi = RN(pi) < pi < next float
assert F(PI_LO) < F(355, 113) and F(PI_HI) > F(333, 106)
K = 12
COEF = []                                    # (-1)^k / (2k+1)!  as enclosing float pairs
for k in range(K + 1):
    c = F((-1) ** k, factorial(2 * k + 1)); f = float(c)
    COEF.append((dn(f), up(f)))
REM = float(F(2, 1) ** (2 * K + 3) / factorial(2 * K + 3))  # t^(2K+3)/(2K+3)! for t<=2
REM = up(REM)

def imul(al, ah, bl, bh):
    p = np.stack([al * bl, al * bh, ah * bl, ah * bh])
    return dn(p.min(0)), up(p.max(0))
def iadd(al, ah, bl, bh): return dn(al + bl), up(ah + bh)

def sin_t(tl, th):
    """enclosure of sin on [tl,th] subset [0, pi/2] (sin increasing there)."""
    def poly(t, lower):
        t2l, t2h = imul(t, t, t, t)
        sl, sh = np.full_like(t, COEF[K][0]), np.full_like(t, COEF[K][1])
        for k in range(K - 1, -1, -1):
            sl, sh = imul(sl, sh, t2l, t2h)
            sl, sh = iadd(sl, sh, np.full_like(t, COEF[k][0]), np.full_like(t, COEF[k][1]))
        sl, sh = imul(sl, sh, t, t)
        return dn(sl - REM) if lower else up(sh + REM)
    return np.maximum(poly(tl, True), 0.0), np.minimum(poly(th, False), 1.0)

def sinpi_i(num, den):
    """enclosure of sin(pi*num/den), exact integer reduction to x in [0,1/2]."""
    r = np.mod(num, 2 * den)
    neg = r >= den
    r = np.where(neg, r - den, r)
    r = np.where(2 * r > den, den - r, r)
    y = r / den                              # correctly rounded; r, den < 2^53
    yl, yh = dn(y), up(y)
    yl = np.where(r == 0, 0.0, yl); yh = np.where(r == 0, 0.0, yh)
    tl, th = dn(PI_LO * yl), up(PI_HI * yh)
    th = np.minimum(th, up(PI_HI / 2))
    sl, sh = sin_t(np.maximum(tl, 0.0), th)
    return np.where(neg, -sh, sl), np.where(neg, -sl, sh)

def idiv_pos_den(al, ah, bl, bh):
    """a / b where b interval does not contain 0."""
    assert np.all((bl > 0) | (bh < 0))
    q = np.stack([al / bl, al / bh, ah / bl, ah / bh])
    return dn(q.min(0)), up(q.max(0))

def Rk_i(k, num, den):
    sl, sh = sinpi_i(num, den); tl, th = sinpi_i(k * num, den)
    zero = np.mod(num, den) == 0
    j = num // den
    lim = (k * np.where(np.mod(j * (k - 1), 2) == 0, 1.0, -1.0)).astype(float)
    sl = np.where(zero, 1.0, sl); sh = np.where(zero, 1.0, sh)   # dummy, replaced below
    ql, qh = idiv_pos_den(tl, th, sl, sh)
    return np.where(zero, lim, ql), np.where(zero, lim, qh)

def S_enclose(n, a, b):
    a, b = F(a), F(b); m = n + 1
    Q = lcm(a.denominator, b.denominator)
    aQ, bQ = a.numerator * (Q // a.denominator), b.numerator * (Q // b.denominator)
    r = np.arange(2 * n, dtype=np.int64)[:, None]; s = np.arange(2 * m, dtype=np.int64)[None, :]
    mask = ((r + s) % 2 == 1)
    rr = np.broadcast_to(r, mask.shape)[mask]; ss = np.broadcast_to(s, mask.shape)[mask]
    U = (rr * Q + aQ) * m; V = (ss * Q + bQ) * n; den = 2 * n * m * Q
    assert 2 * (n + 1) * (abs(int(U.max())) + abs(int(V.max()))) < 2**62
    Sn, Tn = U + V, V - U
    A1 = Rk_i(n + 1, Sn, den); A2 = Rk_i(n + 1, Tn, den)
    B1 = Rk_i(n, Sn, den); B2 = Rk_i(n, Tn, den)
    D1 = imul(*A1, *A2); D2 = imul(*B1, *B2)
    Dl, Dh = iadd(*D1, *D2)
    cl, ch = sinpi_i(np.array([2 * aQ + Q], dtype=np.int64), 2 * Q)    # cos(pi a)
    sgn = np.where(rr % 2 == 0, 1.0, -1.0)
    Hl = dn(Dl - np.where(sgn > 0, ch[0], -cl[0])); Hh = up(Dh - np.where(sgn > 0, cl[0], -ch[0]))
    absl = np.where(Hl > 0, Hl, np.where(Hh < 0, -Hh, 0.0)); absh = np.maximum(np.abs(Hl), np.abs(Hh))
    N = absh.size; u = 2.0 ** -53; g = 2 * N * u           # gamma_{N-1} <= (N-1)u/(1-(N-1)u) < 2Nu
    sh_ = up(np.sum(absh) * (1 + g)); sl_ = dn(np.sum(absl) * (1 - g))
    d = float(2 * n * m)
    return dn(sl_ / d), up(sh_ / d)

if __name__ == "__main__":
    import json, time
    E = '/home/user/padua_research/topics/padua-argmax-bridge-20261105/evidence/compact-return/'
    for name in ['primary-n199', 'primary-n238']:
        d = json.load(open(E + name + '.json')); n = d['n']; t0 = time.process_time()
        worst_w = 0; cons = True; worst_hi_over = -1
        for a, b, h in d['S_upper_rows']:
            lo, hi = S_enclose(n, F(a), F(b)); nat = float.fromhex(h)
            worst_w = max(worst_w, hi - lo); cons &= (lo <= nat); worst_hi_over = max(worst_hi_over, hi - nat)
        lo0, hi0 = S_enclose(n, 0, 0)
        print(f"{name}: 45 rigorous-prototype enclosures, max width {worst_w:.2e}, lo<=native upper for all: {cons}, "
              f"max(hi - native upper) {worst_hi_over:.2e}; corner lo - native lower {lo0 - float.fromhex(d['origin_lower_hex']):.2e}; "
              f"CPU {time.process_time()-t0:.1f}s")
