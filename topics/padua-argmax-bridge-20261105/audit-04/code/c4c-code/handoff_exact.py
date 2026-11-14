#!/usr/bin/env python3
"""C4C independent exact-rational interval recomputation of the comparison
hand-off constants and the two scalar gates (companion 4.2-4.3).

Written by the auditor from the displayed formulas in
companion-paper/sections/comparison-unified.tex (uc:constants,
uc:uniform-allowance, uc:absolute-gate-formula, uc:relative-gate) at
24a98db.  Uses only Python Fraction.  pi, log, sin, cos are enclosed by
the auditor's own series with explicit tail bounds (no code from the repo).
"""
from fractions import Fraction as F
import sys

PREC = 10**45  # outward rounding granularity


def rd(x):  # round down
    return F((x.numerator * PREC) // x.denominator, PREC)


def ru(x):  # round up
    return F(-((-x.numerator * PREC) // x.denominator), PREC)


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = F(lo)
        hi = lo if hi is None else F(hi)
        assert lo <= hi, (lo, hi)
        self.lo, self.hi = rd(lo), ru(hi)

    def __add__(s, o):
        o = o if isinstance(o, I) else I(o)
        return I(s.lo + o.lo, s.hi + o.hi)
    __radd__ = __add__

    def __neg__(s):
        return I(-s.hi, -s.lo)

    def __sub__(s, o):
        o = o if isinstance(o, I) else I(o)
        return I(s.lo - o.hi, s.hi - o.lo)

    def __rsub__(s, o):
        return I(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, I) else I(o)
        p = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return I(min(p), max(p))
    __rmul__ = __mul__

    def inv(s):
        assert s.lo > 0 or s.hi < 0, "division by interval containing 0"
        return I(1 / s.hi, 1 / s.lo)

    def __truediv__(s, o):
        o = o if isinstance(o, I) else I(o)
        return s * o.inv()

    def __rtruediv__(s, o):
        return I(o) * s.inv()

    def __pow__(s, k):
        r = I(1)
        for _ in range(k):
            r = r * s
        return r

    def __repr__(s):
        return f"[{float(s.lo):.9f}, {float(s.hi):.9f}]"


def atan_inv(q, terms=80):
    """atan(1/q), q>1 integer: alternating series, bracket by partial sums."""
    x = F(1, q)
    s = F(0)
    for k in range(terms):
        s += (-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
    nxt = x ** (2 * terms + 1) / (2 * terms + 1)
    # alternating with decreasing terms: true value between s and s+(-1)^terms*nxt
    a, b = s, s + (-1) ** terms * nxt
    return I(min(a, b), max(a, b))


PI = 16 * atan_inv(5) - 4 * atan_inv(239)
assert PI.lo > F(314159265358979, 10**14) and PI.hi < F(314159265358980, 10**14)


def atanh_series(z, terms=120):
    """atanh(z) for 0<=z<=1/2 rational; positive series, tail <= z^(2K+1)/((2K+1)(1-z^2))."""
    s = F(0)
    for k in range(terms):
        s += z ** (2 * k + 1) / (2 * k + 1)
    tail = z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return I(s, s + tail)


LOG2 = 2 * atanh_series(F(1, 3))


def log_rat(x):
    x = F(x)
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    z = (x - 1) / (x + 1)
    return k * LOG2 + 2 * atanh_series(z)


def log_I(X):  # monotone
    return I(log_rat(X.lo).lo, log_rat(X.hi).hi)


def sin_rat(x, terms=40):
    x = F(x)
    s = F(0)
    for k in range(terms):
        s += (-1) ** k * x ** (2 * k + 1) / fact(2 * k + 1)
    nxt = x ** (2 * terms + 1) / fact(2 * terms + 1)
    return I(min(s, s + (-1) ** terms * nxt), max(s, s + (-1) ** terms * nxt))


def cos_rat(x, terms=40):
    x = F(x)
    s = F(0)
    for k in range(terms):
        s += (-1) ** k * x ** (2 * k) / fact(2 * k)
    nxt = x ** (2 * terms) / fact(2 * terms)
    return I(min(s, s + (-1) ** terms * nxt), max(s, s + (-1) ** terms * nxt))


def fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r


# 1/sqrt2 bracket
def inv_sqrt2():
    lo, hi = F(7071067811865475, 10**16), F(7071067811865476, 10**16)
    assert 2 * lo * lo < 1 < 2 * hi * hi
    return I(lo, hi)


S2 = inv_sqrt2()
E_EULER_INV = None  # not needed here


def constants(n):
    n = F(n)
    m = n + 1
    L = log_rat(n)
    Lb = 1 + L
    pi = PI
    pi2 = pi * pi
    b0 = 4 / pi2
    r0 = log_rat(F(5, 2)) + F(1, 18)
    T = (4 * L * L - 3 * L) / pi2
    D = ((52 / pi2) * Lb + 7) / n + F(10) / (n * n) + 20 * Lb / (pi * n * n)
    M = (b0 * (2 * L + 2 * r0) / n + (4 + b0 * (L + 1 / n)) / (4 * n * n - 1)
         + b0 / ((2 * n - 1) ** 2)
         + (5 + b0 * (log_rat(n + F(1, 2)) + 2)) / (4 * (n - F(1, 2)) ** 2))
    ebar = D + M + 1 / n
    KD = ((6 + 16 / (3 * pi)) * Lb + 2 / pi) / n
    A4 = 4 / n + 40 * Lb / (pi * n * n)
    C4 = A4 + F(20) / (n * n)
    dbeta = (17 * L + 27) / (n * n)
    JW = (F(3, 2) * Lb + 6) / n + F(148) / (n * n)
    kWx = (F(19, 2) * Lb + F(23, 3) * L + F(155, 2)) / n + F(152) / (n * n)
    kWy = kWx + dbeta
    logm = log_rat(m)
    log2m = log_rat(2 * m)
    logpi = log_I(pi)
    Wn = (3 * logm + LOG2 + 2 * logpi + 2) / (pi * m)
    gn = 1 + log_I(2 + 8 * m / (3 * pi))
    MA = 1 / pi + 4 / pi2
    Gg = (7 * MA * L + F(111, 2)
          + (63 + LOG2 + 4 * logpi + 7 * logm + 16 * log2m + F(3, 2) * gn) / pi) / m
    CEbar = D + Gg + (64 + 16 * L) / n + F(318) / (n * n) + M + Wn
    Mn = (4 * L * L + F(79, 5) * L) / pi2 + F(9, 4) + CEbar + 2 * KD
    return dict(n=n, m=m, L=L, Lb=Lb, T=T, D=D, M=M, ebar=ebar, KD=KD, A4=A4,
                C4=C4, dbeta=dbeta, JW=JW, kWx=kWx, kWy=kWy, Wn=Wn, gn=gn,
                Gg=Gg, CEbar=CEbar, Mn=Mn)


jstar = F(23, 250)
tstar = F(221, 500)


def gate_G(c, half_sin, half_cos):
    Theta = c["T"] + jstar
    C = tstar + 2 * c["KD"]
    # lower bound: adverse terms use upper sin/cos
    one_minus_cos = 1 - I(half_cos.hi)
    G = (Theta * one_minus_cos - C * I(half_sin.hi)
         - (tstar * tstar) * I(half_cos.hi) / (2 * Theta) - c["CEbar"] - c["ebar"])
    ratio = C / Theta
    return G, ratio


def relative(c):
    U = c["T"] - c["ebar"] + c["A4"] + jstar
    lx = c["kWx"] + F(5, 48)
    ly = c["kWy"]
    dx = 11 * U / 48 - F(5, 12)
    dy = 11 * U / 48
    S0 = dx + dy
    e = dx * dy / S0
    f = (dy * lx + dx * ly) / S0
    g = (lx - ly) ** 2 / (4 * S0)
    maxP = c["C4"] + lx * lx / (4 * dx) + ly * ly / (4 * dy)
    maxP2 = c["C4"] + g + f * f / (4 * e)
    vert = lx / (2 * dx) + ly / (2 * dy)
    vert2 = f / (2 * e)
    Phalf = c["C4"] + g + f / 2 - e / 4
    return dict(U=U, lx=lx, ly=ly, dx=dx, dy=dy, e=e, f=f, g=g, maxP=maxP,
                maxP2=maxP2, vert=vert, vert2=vert2, Phalf=Phalf)


def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        chk.fails += 1


chk.fails = 0

if __name__ == "__main__":
    print("pi", PI, "log2", LOG2)
    out = {}
    for n in (32, 160, 192, 256, 295, 320, 512):
        c = constants(n)
        out[n] = c
        print(f"\n== n={n}")
        for k in ("L", "T", "D", "M", "ebar", "KD", "A4", "C4", "dbeta", "JW", "kWx",
                  "kWy", "Wn", "gn", "Gg", "CEbar", "Mn"):
            print(f"  {k:6s} {c[k]}")
    c512, c192, c256 = out[512], out[192], out[256]
    # absolute gate (512,1)
    s05, c05 = sin_rat(F(1, 2)), cos_rat(F(1, 2))
    G512, r512 = gate_G(c512, s05, c05)
    print("\nG(512,1) lower", G512, " (t*+2KD)/Theta", r512, " tan(1/2)", s05 / c05)
    chk("G(512,1) > 534264/10^6", G512.lo > F(534264, 10**6))
    chk("G(512,1) > 1/2", G512.lo > F(1, 2))
    chk("ratio(512) < 3/50", r512.hi < F(3, 50))
    chk("tan(1/2) > 1/2", (s05 / c05).lo > F(1, 2))
    # absolute gate (192, pi/2)
    G192, r192 = gate_G(c192, S2, S2)
    print("G(192,pi/2) lower (1/sqrt2 bracket)", G192, " ratio", r192)
    G192b, _ = gate_G(c192, I(F(707107, 10**6)), I(F(707107, 10**6)))
    print("G(192,pi/2) lower (707107/10^6 as in text)", G192b)
    chk("707107/10^6 > 1/sqrt2", 2 * F(707107, 10**6) ** 2 > 1)
    chk("G(192,pi/2) > 98316/10^6 (text substitution)", G192b.lo > F(98316, 10**6))
    chk("G(192,pi/2) > 3/100", G192b.lo > F(3, 100))
    chk("ratio(192) < 1/10", r192.hi < F(1, 10))
    # relative polynomial at 512
    R = relative(c512)
    print("\nrelative at 512:")
    for k, v in R.items():
        print(f"  {k:6s} {v}")
    chk("d_x(512) > 1", R["dx"].lo > 1)
    chk("0 < d_beta(512) < 5/48", c512["dbeta"].lo > 0 and c512["dbeta"].hi < F(5, 48))
    chk("vertex(512) < 3/20", R["vert"].hi < F(3, 20))
    chk("vertex identity f/(2e) == l_x/(2d_x)+l_y/(2d_y) (interval overlap)",
        R["vert"].lo <= R["vert2"].hi and R["vert2"].lo <= R["vert"].hi)
    chk("max identity overlap", R["maxP"].lo <= R["maxP2"].hi and R["maxP2"].lo <= R["maxP"].hi)
    chk("max P512 < 40786/10^6", R["maxP"].hi < F(40786, 10**6))
    chk("max P512 < 41/1000", R["maxP"].hi < F(41, 1000))
    chk("P512(1/2) < -143069/10^6", R["Phalf"].hi < F(-143069, 10**6))
    chk("P512(1/2) < -1/7", R["Phalf"].hi < F(-1, 7))
    # J01 receipt intervals
    chk("J01 receipt maxP in [0.040785,0.040786]", R["maxP"].lo > F(40785, 10**6) and R["maxP"].hi < F(40786, 10**6))
    chk("J01 receipt P(1/2) in [-0.143070,-0.143069]", R["Phalf"].lo > F(-143070, 10**6) and R["Phalf"].hi < F(-143069, 10**6))
    chk("J01 receipt vertex in [0.147341,0.147342]", R["vert"].lo > F(147341, 10**6) and R["vert"].hi < F(147342, 10**6))
    chk("J01 receipt G(512,1) in [0.534264,0.534265]", G512.lo > F(534264, 10**6) and G512.hi < F(534265, 10**6) + F(1, 10**6))
    chk("J01 receipt G(192) in [0.098316,0.098317]", G192b.lo > F(98316, 10**6) and G192b.hi < F(98317, 10**6))
    # y*, x* positive at rho=1/2
    dl = R["lx"] - R["ly"]
    xs = (R["dy"] / 2 + dl / 2) / (R["dx"] + R["dy"])
    ys = (R["dx"] / 2 - dl / 2) / (R["dx"] + R["dy"])
    chk("x*,y* > 0 at rho=1/2", xs.lo > 0 and ys.lo > 0)
    chk("0 < l_x - l_y < 5/48", dl.lo > 0 and dl.hi < F(5, 48))
    # n=256 localization constants (fed by this range)
    c = c256
    chk("n=256: T > 107/10", c["T"].lo > F(107, 10))
    chk("n=256: ebar < 1/5", c["ebar"].hi < F(1, 5))
    chk("n=256: KD < 1/5", c["KD"].hi < F(1, 5))
    chk("n=256: CEbar < 3/2", c["CEbar"].hi < F(3, 2))
    chk("n=256: C4 < 9/500", c["C4"].hi < F(9, 500))
    chk("n=256: kWy < 93/100", c["kWy"].hi < F(93, 100))
    chk("n=256: M(256) < 26", c["Mn"].hi < 26)
    # n=160 origin: 160 B_out < 1 and bracket
    n = F(160); m = n + 1; L = log_rat(n)
    K = L + 25 * log_rat(2 * m) + F(193, 3)
    Bout = PI * K / (8 * m * m) + F(1) / (8 * n * n)
    print("\n160*B_out", 160 * Bout)
    chk("160 B_out < 1", (160 * Bout).hi < 1)
    # bracket [71/n^2-22/(45m)]_+ vanishes from n0
    n0 = next(k for k in range(2, 1000) if F(71, k * k) <= F(22, 45 * (k + 1)))
    print("bracket vanishes from n =", n0)
    chk("bracket vanishes for all n>=148 (first n0<=148)", n0 <= 148)
    print("\nfails:", chk.fails)
    sys.exit(1 if chk.fails else 0)
