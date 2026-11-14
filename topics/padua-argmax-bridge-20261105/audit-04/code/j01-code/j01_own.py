#!/usr/bin/env python3
"""Audit-04 J01: independent exact-rational evaluation of the J01 gates.

Written from the J01 definitions only (theory/J01-onset512-gates.md and
paper comparison-unified.tex), not importing or copying check.py.
Independent choices: pi from Euler's arctan(1/2)+arctan(1/3) with
alternating brackets; log via 2^k reduction to [2/3,4/3] and atanh series
with geometric tail; log2 = 2 atanh(1/3); sin/cos by Taylor with Lagrange
remainder; 1/sqrt2 by exact rational square bracket; decimal outward
rounding grid 10^-60.  All comparisons are exact Fraction comparisons.
"""
from fractions import Fraction as F
import sys

GRID = 10**60


def dn(x):
    return F((x.numerator * GRID) // x.denominator, GRID)


def upr(x):
    return -dn(-x)


class Iv:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = F(lo)
        hi = lo if hi is None else F(hi)
        if lo > hi:
            raise ValueError("bad interval")
        self.lo, self.hi = dn(lo), upr(hi)

    def __add__(s, o):
        o = iv(o)
        return Iv(s.lo + o.lo, s.hi + o.hi)

    __radd__ = __add__

    def __neg__(s):
        return Iv(-s.hi, -s.lo)

    def __sub__(s, o):
        return s + (-iv(o))

    def __rsub__(s, o):
        return iv(o) - s

    def __mul__(s, o):
        o = iv(o)
        p = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return Iv(min(p), max(p))

    __rmul__ = __mul__

    def inv(s):
        if not (s.lo > 0 or s.hi < 0):
            raise ZeroDivisionError("interval contains 0")
        return Iv(1 / s.hi, 1 / s.lo)

    def __truediv__(s, o):
        return s * iv(o).inv()

    def __rtruediv__(s, o):
        return iv(o) * s.inv()

    def sq(s):
        if s.lo >= 0:
            return Iv(s.lo**2, s.hi**2)
        if s.hi <= 0:
            return Iv(s.hi**2, s.lo**2)
        return Iv(0, max(s.lo**2, s.hi**2))

    def __repr__(s):
        return f"[{float(s.lo):.12g}, {float(s.hi):.12g}]"


def iv(x):
    return x if isinstance(x, Iv) else Iv(x)


def atan_inv(q, terms=60):
    # alternating series sum_{k} (-1)^k /((2k+1) q^(2k+1)); q>1
    s, prev = F(0), F(0)
    for k in range(terms):
        prev = s
        s = s + F((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
    return Iv(min(prev, s), max(prev, s))


PI = 4 * (atan_inv(2, 120) + atan_inv(3, 80))


def atanh_series(s, terms=80):
    # 2*atanh(s) for |s|<=1/3 rational; tail <= 2|s|^(2N+1)/((2N+1)(1-s^2))
    s = F(s)
    tot = sum(2 * s ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail = 2 * abs(s) ** (2 * terms + 1) / ((2 * terms + 1) * (1 - s * s))
    return Iv(tot - tail, tot + tail)


LOG2 = atanh_series(F(1, 3))


def log_q(z):
    z = F(z)
    if z <= 0:
        raise ValueError
    k = 0
    while z > F(4, 3):
        z /= 2
        k += 1
    while z < F(2, 3):
        z *= 2
        k -= 1
    return k * LOG2 + atanh_series((z - 1) / (z + 1))


def log(x):
    x = iv(x)
    return Iv(log_q(x.lo).lo, log_q(x.hi).hi)


def fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r


def sin_q(x, N=30):
    x = F(x)
    s = sum((-1) ** k * x ** (2 * k + 1) / fact(2 * k + 1) for k in range(N))
    r = abs(x) ** (2 * N + 1) / fact(2 * N + 1)
    return Iv(s - r, s + r)


def cos_q(x, N=30):
    x = F(x)
    s = sum((-1) ** k * x ** (2 * k) / fact(2 * k) for k in range(N))
    r = abs(x) ** (2 * N) / fact(2 * N)
    return Iv(s - r, s + r)


def sqrt_iv(x, bits=200):
    x = iv(x)
    assert x.lo >= 0

    def root_lo(v):
        # largest k/2^bits with (k/2^bits)^2 <= v
        from math import isqrt
        sc = 2**bits
        return F(isqrt((v.numerator * sc * sc) // v.denominator), sc)

    lo = root_lo(x.lo)
    hi = root_lo(x.hi) + F(1, 2**bits)
    assert lo * lo <= x.lo and hi * hi >= x.hi
    return Iv(lo, hi)


INV_SQRT2 = Iv(*(lambda r: (r.lo, r.hi))(sqrt_iv(Iv(F(1, 2)))))


def consts(nv):
    n = iv(nv)
    m = n + 1
    L = log(n)
    H = 1 + L
    b = 4 / PI.sq()
    r0 = log(F(5, 2)) + F(1, 18)
    T = (4 * L.sq() - 3 * L) / PI.sq()
    D = ((52 / PI.sq()) * H + 7) / n + 10 / n.sq() + 20 * H / (PI * n.sq())
    Mesh = (b * (2 * L + 2 * r0) / n + (4 + b * (L + 1 / n)) / (4 * n.sq() - 1)
            + b / (2 * n - 1).sq()
            + (5 + b * (log(n + F(1, 2)) + 2)) / (4 * (n - F(1, 2)).sq()))
    ebar = D + Mesh + 1 / n
    KD = ((6 + 16 / (3 * PI)) * H + 2 / PI) / n
    MA = 1 / PI + 4 / PI.sq()
    gn = 1 + log(2 + 8 * m / (3 * PI))
    Gg = (7 * MA * L + F(111, 2)
          + (63 + LOG2 + 4 * log(PI) + 7 * log(m) + 16 * log(2 * m)
             + F(3, 2) * gn) / PI) / m
    W = (3 * log(m) + LOG2 + 2 * log(PI) + 2) / (PI * m)
    CE = D + Gg + (64 + 16 * L) / n + 318 / n.sq() + Mesh + W
    A4 = 4 / n + 40 * H / (PI * n.sq())
    C4 = A4 + 20 / n.sq()
    db = (17 * L + 27) / n.sq()
    kx = (F(19, 2) * H + F(23, 3) * L + F(155, 2)) / n + 152 / n.sq()
    ky = kx + db
    JW = (F(3, 2) * H + 6) / n + 148 / n.sq()
    return dict(T=T, D=D, Mesh=Mesh, ebar=ebar, KD=KD, Gg=Gg, W=W, CE=CE,
                A4=A4, C4=C4, db=db, kx=kx, ky=ky, JW=JW, L=L)


J0, T0 = F(23, 250), F(221, 500)


def relative(nv):
    c = consts(nv)
    U = c["T"] - c["ebar"] + c["A4"] + J0
    d1 = F(11, 48) * U - F(5, 12)
    d2 = F(11, 48) * U
    l1 = c["kx"] + F(5, 48)
    l2 = c["ky"]
    S0 = d1 + d2
    e = d1 * d2 / S0
    f = (d2 * l1 + d1 * l2) / S0
    g = (l1 - l2).sq() / (4 * S0)
    peak_a = c["C4"] + g + f.sq() / (4 * e)
    peak_b = c["C4"] + l1.sq() / (4 * d1) + l2.sq() / (4 * d2)
    half = c["C4"] + g + f / 2 - e / 4
    vert_a = f / (2 * e)
    vert_b = l1 / (2 * d1) + l2 / (2 * d2)
    # P(1/2) as maximum over the segment: direct optimizer coordinates
    dl = l1 - l2
    xs = (d2 / 2 + dl / 2) / S0
    ys = (d1 / 2 - dl / 2) / S0
    return dict(U=U, d1=d1, d2=d2, l1=l1, l2=l2, e=e, f=f, g=g,
                peak_a=peak_a, peak_b=peak_b, half=half, vert_a=vert_a,
                vert_b=vert_b, xs=xs, ys=ys, dl=dl, C4=c["C4"], db=c["db"])


def gate(nv, sinh, cosh):
    c = consts(nv)
    Th = c["T"] + J0
    C = T0 + 2 * c["KD"]
    Glin = Th * (1 - cosh) - C * sinh - T0**2 * cosh / (2 * Th) - c["CE"] - c["ebar"]
    A = Th * cosh + C * sinh
    B = T0 * cosh
    Gsqrt = Th - sqrt_iv(A.sq() + B.sq()) - c["CE"] - c["ebar"]
    return dict(Theta=Th, C=C, ratio=C / Th, Glin=Glin, Gsqrt=Gsqrt,
                CE=c["CE"], ebar=c["ebar"], KD=c["KD"])


def floor_band(n):
    # J01 (5) / paper Fh(n): exact rationals
    A = F(97, 100) * F(15, 16) - F(1, 4)
    Ih = F(2303, 5000) * F(15, 16) - F(471, 2500)
    Rh = F(4837, 1875) * F(15, 16) - F(5, 6)
    return F(539, 1936) * Ih - (140 * A + 400 * Rh) / (157 * F(n)) - 800 * A / (3 * F(n) ** 2), A, Ih, Rh


def tan_q(x):
    return sin_q(x) / cos_q(x)


def band_elementary():
    out = {}
    # bounds on pi-dependent arguments are handled by monotonicity on [lo,hi]
    p_lo, p_hi = PI.lo, PI.hi
    out["sin(pi/100)>3/100"] = sin_q(p_lo / 100).lo > F(3, 100)
    out["11/4<4log2<14/5"] = (4 * LOG2).lo > F(11, 4) and (4 * LOG2).hi < F(14, 5)
    out["cos(pi/4)>707/1000"] = INV_SQRT2.lo > F(707, 1000)
    out["sin(pi/4)<71/100"] = INV_SQRT2.hi < F(71, 100)
    out["6pi/25>471/625"] = 6 * p_lo / 25 > F(471, 625)
    out["157/50<pi<22/7"] = p_lo > F(157, 50) and p_hi < F(22, 7)
    # tan(pi/8)/tan(pi/200): tan increasing; upper uses tan(p_hi/8)/tan(p_lo/200)
    num = tan_q(p_hi / 8)
    den = tan_q(p_lo / 200)
    ratio_hi = num.hi / den.lo
    out["log(tan(pi/8)/tan(pi/200))<10/3"] = log_q(ratio_hi).hi < F(10, 3)
    out["log_ratio_hi"] = float(log_q(ratio_hi).hi)
    out["cos(pi/100)<1"] = True
    # A(b)>=15/16(1-sin(pi/4))-1/4 = 7/320 using sin(pi/4)<71/100
    out["A(b)>=7/320"] = F(15, 16) * (1 - F(71, 100)) - F(1, 4) == F(7, 320)
    # true band ingredients (interval) for slack report
    a, C = F(15, 16), F(11, 16)
    bm_lo, bm_hi = p_lo / 100, p_hi / 100
    bp_lo, bp_hi = p_lo / 4, p_hi / 4
    I_true = C * (PI / 4 - PI / 100) + a * (INV_SQRT2 - Iv(cos_q(bm_hi).lo, cos_q(bm_lo).hi))
    Ab_true = C - a * Iv(sin_q(bm_lo).lo, sin_q(bm_hi).hi)
    lr = Iv(log_q(tan_q(p_lo / 8).lo / tan_q(p_hi / 200).hi).lo, log_q(ratio_hi).hi)
    R_true = C * lr - a * (PI / 4 - PI / 100)
    out["I_true"], out["Ab_true"], out["R_true"] = I_true, Ab_true, R_true
    return out


def band_true_Q(n, I, Ab, R):
    Tc = 4 * LOG2
    sinb = Iv(sin_q(PI.lo / 100).lo, sin_q(PI.hi / 100).hi)
    return Tc * I / PI.sq() - Tc * Ab / (PI * n) - 8 * R / (PI * n) - 8 * Ab / (n * n * sinb)


def dec(x):
    return float(x)


if __name__ == "__main__":
    res = {}
    print("pi", PI, "width", float(PI.hi - PI.lo))
    print("log2", LOG2)
    r = relative(512)
    for k in ("U", "d1", "d2", "l1", "l2", "e", "f", "g", "peak_a", "peak_b", "half",
              "vert_a", "vert_b", "xs", "ys", "dl", "db", "C4"):
        print(f"rel512 {k:7s}", r[k])
    chk = {}
    chk["peak<41/1000"] = r["peak_a"].hi < F(41, 1000) and r["peak_b"].hi < F(41, 1000)
    chk["half<-1/7"] = r["half"].hi < -F(1, 7)
    chk["vertex<1/2"] = r["vert_a"].hi < F(1, 2) and r["vert_b"].hi < F(1, 2)
    chk["vertex<3/20"] = r["vert_b"].hi < F(3, 20)
    chk["d1>1"] = r["d1"].lo > 1
    chk["0<db<5/48"] = r["db"].lo > 0 and r["db"].hi < F(5, 48)
    chk["xs,ys>0"] = r["xs"].lo > 0 and r["ys"].lo > 0
    print("slack peak  41/1000 - hi =", dec(F(41, 1000) - r["peak_b"].hi))
    print("slack half  -1/7 - hi    =", dec(-F(1, 7) - r["half"].hi))
    print("slack vertex 1/2 - hi    =", dec(F(1, 2) - r["vert_b"].hi))
    # G(512,1)
    s12, c12 = sin_q(F(1, 2)), cos_q(F(1, 2))
    g1 = gate(512, s12, c12)
    chk["tan(1/2)>=C/Theta @512"] = (s12 / c12).lo > g1["ratio"].hi
    chk["G(512,1)>1/2"] = g1["Glin"].lo > F(1, 2)
    print("G512,1 lin", g1["Glin"], "sqrt", g1["Gsqrt"], "ratio", g1["ratio"],
          "tan(1/2)", s12 / c12)
    print("slack G(512,1) lo-1/2   =", dec(g1["Glin"].lo - F(1, 2)))
    # G(192,pi/2): exact 1/sqrt2, and paper's 707107/10^6 substitution
    g2 = gate(192, INV_SQRT2, INV_SQRT2)
    chk["tan(pi/4)=1>=C/Theta @192"] = g2["ratio"].hi < 1
    chk["G(192,pi/2)>3/100"] = g2["Glin"].lo > F(3, 100)
    rh = F(707107, 10**6)
    chk["2*(707107e-6)^2>1"] = 2 * rh * rh > 1
    c192 = consts(192)
    Th = c192["T"] + J0
    Cc = T0 + 2 * c192["KD"]
    g2sub = Th * (1 - rh) - Cc * rh - T0**2 * rh / (2 * Th) - c192["CE"] - c192["ebar"]
    chk["G(192,pi/2) with 707107 subst >3/100"] = g2sub.lo > F(3, 100)
    print("G192,pi/2 lin(exact 1/sqrt2)", g2["Glin"], "subst", g2sub, "sqrt", g2["Gsqrt"],
          "ratio", g2["ratio"])
    print("slack G(192,pi/2) subst lo - 3/100 =", dec(g2sub.lo - F(3, 100)))
    # floor
    fl, A_, I_, R_ = floor_band(295)
    chk["A*,I*,R*>0"] = A_ > 0 and I_ > 0 and R_ > 0
    chk["Fh(295)>1/20"] = fl > F(1, 20)
    chk["Fh(294)>1/20 ?"] = floor_band(294)[0] > F(1, 20)
    print("Fh(295) =", fl, float(fl), " slack", float(fl - F(1, 20)))
    print("Fh(294) =", float(floor_band(294)[0]), " Fh(512)=", float(floor_band(512)[0]))
    print("A*,I*,R* =", A_, I_, R_, float(A_), float(I_), float(R_))
    be = band_elementary()
    for k, v in be.items():
        print("band", k, v)
    chk["I_true>I*"] = be["I_true"].lo > I_
    chk["Ab_true<A*"] = be["Ab_true"].hi < A_
    chk["R_true<R*"] = be["R_true"].hi < R_
    qt = band_true_Q(295, be["I_true"], be["Ab_true"], be["R_true"])
    print("band formula with true constants at 295:", qt)
    for k in ("sin(pi/100)>3/100", "11/4<4log2<14/5", "cos(pi/4)>707/1000",
              "sin(pi/4)<71/100", "6pi/25>471/625", "157/50<pi<22/7",
              "log(tan(pi/8)/tan(pi/200))<10/3", "A(b)>=7/320"):
        chk["band " + k] = be[k]
    # j0 / t chain inputs (J02-supplied premises; elementary parts only)
    gam_lo_M = 2000
    Hm = sum(F(1, k) for k in range(1, gam_lo_M + 1))
    gamma = Iv((Hm - log(gam_lo_M + 1)).lo, (Hm - log(F(2 * gam_lo_M + 1, 2))).hi)
    k0 = 2 * gamma + 4 * LOG2 - 2 * log(PI)
    print("gamma", gamma, "k0", k0)
    chk["t0=2log2/pi<221/500"] = (2 * LOG2 / PI).hi < T0
    C0 = 2 * gamma + 4 * LOG2
    bstar = C0 - F(7, 2)
    dstar = C0 * bstar / PI.sq()
    g0 = 4 * (log(PI).sq() - LOG2.sq()) / PI.sq()
    chk["d*>39/250"] = dstar.lo > F(39, 250)
    chk["g0<43/125"] = g0.hi < F(43, 125)
    # H0 = kappa/2 + (2 k0/pi^2) log(2/pi); kappa>9/10 is the J02 premise
    H0_lo = F(9, 20) + (2 * k0 / PI.sq() * (-log(PI / 2))).lo
    chk["H0>7/25 given kappa>9/10"] = H0_lo > F(7, 25)
    print("dstar", dstar, "g0", g0, "H0_lo(kappa=9/10)", float(H0_lo),
          "j_lo", float(H0_lo + dstar.lo - g0.hi))
    ok = all(v is True for k, v in chk.items() if not k.endswith("?"))
    for k, v in chk.items():
        print("CHECK", k, v)
    print("ALL_REQUIRED_PASS", ok)
    sys.exit(0 if ok else 1)
