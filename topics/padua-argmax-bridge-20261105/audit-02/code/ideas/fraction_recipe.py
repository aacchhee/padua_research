"""Rigorous rational-interval evaluation (Fractions) of the literal E14/E13/E15/E12 recipes
at fixed degrees.  Transcendental base values (log, pi, sin, sqrt, e, atan-free) are enclosed
by mpmath.iv at 90 digits and converted exactly to Fractions; all subsequent arithmetic is
exact rational interval arithmetic.  Output: ENCLOSED values of the recipe quantities
(formula evaluations, not Padua function values; the recipe failing is NOT a failure of the
theorem, only of that sufficient allocation).
Usage: python3 fraction_recipe.py 200 250 300 320
"""
import sys
from fractions import Fraction as Fr
import mpmath as mp
mp.iv.dps = 90


def mpf2fr(x):
    m, e = mp.mpf(x).man_exp
    return Fr(m) * (Fr(2) ** e) if e >= 0 else Fr(m, 2 ** (-e))


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        if hi is None:
            hi = lo
        lo, hi = Fr(lo), Fr(hi)
        assert lo <= hi, (lo, hi)
        self.lo, self.hi = lo, hi

    @staticmethod
    def of(v):
        return v if isinstance(v, I) else I(v)

    def __add__(s, o):
        o = I.of(o); return I(s.lo + o.lo, s.hi + o.hi)
    __radd__ = __add__

    def __neg__(s):
        return I(-s.hi, -s.lo)

    def __sub__(s, o):
        return s + (-I.of(o))

    def __rsub__(s, o):
        return I.of(o) - s

    def __mul__(s, o):
        o = I.of(o)
        c = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return I(min(c), max(c))
    __rmul__ = __mul__

    def inv(s):
        assert s.lo > 0 or s.hi < 0, 'division by interval containing 0'
        return I(1 / s.hi, 1 / s.lo)

    def __truediv__(s, o):
        return s * I.of(o).inv()

    def __rtruediv__(s, o):
        return I.of(o) * s.inv()

    def __pow__(s, k):
        assert isinstance(k, int) and k >= 1
        r = s
        for _ in range(k - 1):
            r = r * s
        return r

    def __repr__(s):
        return f"[{float(s.lo):.10g},{float(s.hi):.10g}]"


def E(ivval):
    """Fraction interval from an mpmath iv value."""
    return I(mpf2fr(ivval.a), mpf2fr(ivval.b))


iv = mp.iv
PI = E(iv.pi)
LOG2 = E(iv.log(2))
LOGPI = E(iv.log(iv.pi))
EUL = E(iv.e)
HR = E(iv.log(iv.mpf(5) / 2)) + Fr(1, 18)


def LOG(x):
    return E(iv.log(iv.mpf(x.numerator) / x.denominator if isinstance(x, Fr) else iv.mpf(x)))


def SQRT(x):
    # x is a Fraction interval
    return I(mpf2fr(iv.sqrt(iv.mpf(x.lo.numerator) / x.lo.denominator).a), mpf2fr(iv.sqrt(iv.mpf(x.hi.numerator) / x.hi.denominator).b))


def scal(n):
    n = Fr(n)
    L = LOG(n); H = 1 + L; m = n + 1
    s = dict(n=n, L=L, H=H, m=m)
    s['T'] = (4 * L ** 2 - 3 * L) / PI ** 2
    Da = ((52 / PI ** 2) * H + 7) / n + 20 * H / (PI * n ** 2)
    s['Da'] = Da
    s['D'] = Da + Fr(10) / n ** 2
    b = 4 / PI ** 2
    s['b'] = b
    s['Mesh'] = (b * (2 * L + 2 * HR) / n + (4 + b * (L + 1 / n)) / (4 * n ** 2 - 1)
                 + b / (2 * n - 1) ** 2 + (5 + b * (LOG(n + Fr(1, 2)) + 2)) / (4 * (n - Fr(1, 2)) ** 2))
    s['ebar'] = s['D'] + s['Mesh'] + 1 / n
    Borig = PI * (L + 25 * LOG(2 * m) + Fr(193, 3)) / (8 * m ** 2) + 1 / (8 * n ** 2)
    extra = Fr(71) / n ** 2 - Fr(22) / (45 * m)
    extra = max(extra, Fr(0))
    s['eminus'] = s['D'] + s['Mesh'] + Borig + extra
    s['e0'] = s['ebar'] if n >= 160 else s['eminus']
    s['j'] = Fr(23, 250)
    s['A4'] = 4 / n + 40 * H / (PI * n ** 2)
    s['C4'] = s['A4'] + Fr(20) / n ** 2
    s['JN'] = (Fr(3, 2) * H + Fr(16, 5)) / n + Fr(78) / n ** 2
    s['db'] = (17 * L + 27) / n ** 2
    s['kNx'] = (Fr(19, 2) * H + Fr(23, 3) * L + Fr(677, 10)) / n + Fr(82) / n ** 2
    s['kNy'] = s['kNx'] + s['db']
    s['kWx'] = (Fr(19, 2) * H + Fr(23, 3) * L + Fr(155, 2)) / n + Fr(152) / n ** 2
    s['kWy'] = s['kWx'] + s['db']
    s['kWy_old'] = (Fr(19, 2) * H + 15 * L + Fr(265, 3)) / n + (179 + 17 * L) / n ** 2
    s['KD'] = ((6 + 16 / (3 * PI)) * H + 2 / PI) / n
    return s


def fh_coeffs(n, wide=False):
    n = Fr(n)
    # Fh = Ah*a_r - Bh*r ; a_r=1-r^2/4 (E02 (8))
    if not wide:
        Ia, Ib = Fr(2303, 5000), Fr(471, 1250)
        Ra, Rb = Fr(4837, 1875), Fr(5, 3)
    else:
        Ia, Ib = Fr(5369, 15000), Fr(7379, 30000)
        Ra, Rb = Fr(37621, 15000), Fr(3, 2)
    c = Fr(539, 1936)
    Ah = c * Ia - 140 * Fr(97, 100) / (157 * n) - 400 * Ra / (157 * n) - 800 * Fr(97, 100) / (3 * n ** 2)
    Bh = c * Ib - 140 * Fr(1, 2) / (157 * n) - 400 * Rb / (157 * n) - 800 * Fr(1, 2) / (3 * n ** 2)
    return Ah, Bh


def quad_min(c0, c1, c2, lo, hi):
    """exact min of c0+c1 r+c2 r^2 over [lo,hi] (Fractions)."""
    cands = [lo, hi]
    if c2 > 0:
        v = -c1 / (2 * c2)
        if lo < v < hi:
            cands.append(v)
    vals = [(c0 + c1 * r + c2 * r * r, r) for r in cands]
    return min(vals)


def halfnear(n):
    s = scal(n)
    U = s['T'] - s['e0'] + s['A4'] + s['JN'] / 8 + s['j']
    c0 = Fr(47, 192)
    d1 = c0 * U - Fr(15, 32)
    d2 = c0 * U + Fr(1679, 8000)
    l1 = s['kNx'] + Fr(3, 40)
    l2 = s['kNy']
    e = d1 * d2 / (d1 + d2)
    f = (d2 * l1 + d1 * l2) / (d1 + d2)
    g = (l1 - l2) ** 2 / (4 * (d1 + d2))
    Ah, Bh = fh_coeffs(n)
    # gap_h(r) = Ah(1-r^2/4)-Bh r - (C4+g+f r - e r^2)
    lo_poly = (Ah - s['C4'].hi - g.hi, -(Bh + f.hi), e.lo - Ah / 4)
    hi_poly = (Ah - s['C4'].lo - g.lo, -(Bh + f.lo), e.hi - Ah / 4)
    mlo, rlo = quad_min(*lo_poly, Fr(1, 8), Fr(1, 2))
    mhi = hi_poly[0] + hi_poly[1] * rlo + hi_poly[2] * rlo * rlo
    return dict(e=e, f=f, g=g, C4=s['C4'], Ah=Ah, Bh=Bh, gap_Fh=I(mlo, mhi), r_star=rlo)


def wide(n):
    s = scal(n)
    base = s['T'] - s['e0'] + s['j']
    d1 = Fr(11, 48) * base - Fr(5, 12)
    d2 = Fr(11, 48) * base
    l1 = s['kWx'] + Fr(5, 48)
    l2 = s['kWy']
    e = d1 * d2 / (d1 + d2)
    f = (d2 * l1 + d1 * l2) / (d1 + d2)
    g = (l1 - l2) ** 2 / (4 * (d1 + d2))
    P = lambda r: s['C4'] + g + f * r - e * r * r
    Ah, Bh = fh_coeffs(n)
    half = Fr(1, 2)
    floor_half = Ah * (1 - half * half / 4) - Bh * half
    return dict(e=e, f=f, g=g, P_half=P(half), P_3_5=P(Fr(3, 5)), P_pi4=P(Fr(785398, 1000000)),
                Fh_half=floor_half, margin_half=floor_half - P(half))


def outer(n):
    s = scal(n)
    n = Fr(n); L, H, m = s['L'], s['H'], s['m']
    a0, p0, P0, w0, eta, u1 = Fr(337, 384), Fr(12, 25), Fr(24, 25), Fr(721, 384), Fr(3, 2), Fr(47, 384)
    b = s['b']
    eps_iv = 3 * iv.pi / (2 * (iv.mpf(int(m.numerator)) / int(m.denominator)))
    ell = E(-iv.log(iv.sin(eps_iv)))
    W = (3 * LOG(m) + LOG2 + 2 * LOGPI + 2) / (PI * m)
    C = 1 + 8 * a0 * m / (3 * PI)
    # log(1+C/p0)
    x = 1 + C / p0
    lg = I(mpf2fr(iv.log(iv.mpf(x.lo.numerator) / x.lo.denominator).a), mpf2fr(iv.log(iv.mpf(x.hi.numerator) / x.hi.denominator).b))
    Gamma_b = p0 * (1 + lg)
    gamma_b = 1 + lg - C / (p0 + C)
    MA_b = p0 / PI + 4 * a0 / PI ** 2
    VB_b = 23 + (3 * Gamma_b + (2 * p0 + 6 * P0) * ell + 26 * a0 + 20) / PI
    CB_b = 6 + (4 + 4 * a0 / EUL) / PI
    G_env = 7 * L * MA_b / m + VB_b / (2 * m) + (4 / I(m)) * (7 + (P0 / PI) * (5 + 2 * LOG(2 * m))) + 2 * CB_b / m
    D_env = a0 * s['Da'] + Fr(10) / n ** 2
    R6_env = (21 + 21 * a0 + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / PI) / n + (317 + Fr(5, 12)) / n ** 2
    Dmesh_b = 4 * w0 / PI + a0 * b * LOGPI
    Zmesh_b = Dmesh_b + a0 * b / n
    M_env = (a0 * b * (2 * L + 2 * HR) / n + (Dmesh_b + a0 * b * (L + 1 / n)) / (4 * n ** 2 - 1)
             + a0 * b / (2 * n - 1) ** 2 + (Zmesh_b + a0 * b * (LOG(n + Fr(1, 2)) + 2)) / (4 * (n - Fr(1, 2)) ** 2))
    Cb = D_env + G_env + R6_env + M_env
    Cs = eta * (7 * L / (PI * m) + (3 * gamma_b + 2 * ell) / (2 * PI * m) + (48 * H + 24) / (PI * n)) + 3 * ((LOG2 + 4 * LOGPI) / (PI * m) + W)
    Cl = (12 * ell + 16 * (5 + 2 * LOG(2 * m))) / (PI * m)
    KD = s['KD']
    jst, tst = Fr(23, 250), Fr(221, 500)
    Gb = u1 * (s['T'] + jst) - tst * p0 - Cb - P0 * KD - s['e0']
    K = s['T'] + jst - Cl - 4 * KD
    A = eta * tst + Cs
    F = Gb - A ** 2 / (4 * K)
    return dict(Gb=Gb, K=K, A=A, F=F, Cb=Cb, Cs=Cs, Cl=Cl, KD=KD, u1T=u1 * (s['T'] + jst), D_env=D_env, G_env=G_env,
                R6_env=R6_env, M_env=M_env, e0=s['e0'])


def corner(n, new_wide=False):
    s = scal(n)
    n = Fr(n); L, H, m = s['L'], s['H'], s['m']
    MA = 1 / PI + 4 / PI ** 2
    gx = 2 + 8 * m / (3 * PI)
    g = 1 + I(mpf2fr(iv.log(iv.mpf(gx.lo.numerator) / gx.lo.denominator).a), mpf2fr(iv.log(iv.mpf(gx.hi.numerator) / gx.hi.denominator).b))
    Gg = (7 * MA * L + Fr(111, 2) + (63 + LOG2 + 4 * LOGPI + 7 * LOG(m) + 16 * LOG(2 * m) + Fr(3, 2) * g) / PI) / m
    W = (3 * LOG(m) + LOG2 + 2 * LOGPI + 2) / (PI * m)
    CEbar = s['D'] + Gg + (64 + 16 * L) / n + Fr(318) / n ** 2 + s['Mesh'] + W
    KD = s['KD']
    M = (4 * L ** 2 + Fr(79, 5) * L) / PI ** 2 + Fr(9, 4) + CEbar + 2 * KD
    q0 = Fr(7, 48)
    h = PI / 4
    kW = s['kWy'] if new_wide else s['kWy_old']
    dA = q0 * (s['T'] - s['e0'] + s['j']) - Fr(1, 4) - s['C4'] - h * kW
    dD = 2 * q0 * (s['T'] + s['j']) - Fr(4, 15) - CEbar - Fr(3, 2) * KD - s['e0']
    rU = Fr(2, 125)
    FA = dA - rU * M
    FD = dD - 2 * rU * M
    return dict(dA=dA, dD=dD, M=M, FA=FA, FDhalf=FD * Fr(1, 2))


if __name__ == '__main__':
    ns = [int(a) for a in sys.argv[1:]] or [200, 250, 300, 320]
    for n in ns:
        print(f"===== n={n}")
        h = halfnear(n)
        print(f" halfnear recipe: e={h['e']} f={h['f']} g={h['g']} C4={h['C4']}")
        print(f"   Fh: Ah={float(h['Ah']):.8f} Bh={float(h['Bh']):.8f};  min_[1/8,1/2](Fh - upper) in {h['gap_Fh']} at r={float(h['r_star']):.5f}")
        w = wide(n)
        print(f" wide recipe: e={w['e']} f={w['f']} g={w['g']}; P(1/2) in {w['P_half']}, P(3/5) in {w['P_3_5']}, P(pi/4) in {w['P_pi4']}")
        print(f"   Fh(1/2) = {float(w['Fh_half']):.8f}; floor-P at r=1/2 in {w['margin_half']}")
        o = outer(n)
        print(f" outer E13: Gb in {o['Gb']}, K in {o['K']}, A in {o['A']}, F in {o['F']}")
        print(f"   u1(T+j)={o['u1T']} Cb={o['Cb']} [D_env {o['D_env']}, G_env {o['G_env']}, R6 {o['R6_env']}, M {o['M_env']}] KD={o['KD']} e0={o['e0']} Cs={o['Cs']} Cl={o['Cl']}")
        c = corner(n); c2 = corner(n, new_wide=True)
        print(f" corner E12: dA {c['dA']} dD {c['dD']} M {c['M']} FA {c['FA']} FD/2 {c['FDhalf']}; FA with E14 wide kWy {c2['FA']}")
