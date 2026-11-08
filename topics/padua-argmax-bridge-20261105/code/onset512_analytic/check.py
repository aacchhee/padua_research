#!/usr/bin/env python3
"""J01/J02: tiny standard-library exact-rational base checker.

All outward rounding is rational on a 2^-128 grid. The mathematical
reductions and proofs of every series bracket are in J01/J02. No Arb,
floating-point, repository evaluator, certificate or native code is used.
"""
from fractions import Fraction as F
import json
import platform

SCALE = 2**128


def down(x):
    return F(x.numerator * SCALE // x.denominator, SCALE)


def up(x):
    return -down(-x)


class I:
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo, self.hi = down(lo), up(hi)

    def __add__(self, other):
        o = as_i(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -as_i(other)

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        o = as_i(other)
        ends = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = as_i(other)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self

    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        ans = I(1)
        for _ in range(k):
            ans = ans * self
        return ans

    def widen(self, radius):
        return I(self.lo-radius, self.hi+radius)


def as_i(x):
    return x if isinstance(x, I) else I(x)


def atan_inv(q):
    part, prev = F(0), F(0)
    for k in range(40):
        prev, part = part, part + F((-1)**k, (2*k+1)*q**(2*k+1))
    return I(min(prev, part), max(prev, part))


PI = 16*atan_inv(5)-4*atan_inv(239)


def log_small(z):
    assert 1 <= z <= 2
    x = (z-1)/(z+1)
    part = sum(2*x**(2*k+1)/(2*k+1) for k in range(48))
    tail = 2*x**97/(97*(1-x*x))
    return I(part, part+tail)


LOG2 = log_small(F(2))


def log_rational(z):
    assert z > 0
    if z < 1:
        return -log_rational(1/z)
    power = 0
    while z >= 2:
        z /= 2
        power += 1
    return power*LOG2 + log_small(z)


def log(x):
    x = as_i(x)
    return I(log_rational(x.lo).lo, log_rational(x.hi).hi)


def zeta(s):
    m = 10
    part = sum(F(1, k**s) for k in range(1, m+1))
    lo = part + F(1, (s-1)*m**(s-1))-F(1, 2*m**s)
    hi = part + F(2**(s-1), (s-1)*(2*m+1)**(s-1))
    return I(lo, hi)


def elementary_constants():
    # A single convex-tail argument treats even and odd zeta values alike.
    # Thus no Bernoulli table or special-value identity is a trusted input.
    ze = [I(0), zeta(2), zeta(4), zeta(6)]
    zo = {s: zeta(s) for s in (3, 5, 7, 9)}
    aa = [I(1)]
    for p in range(1, 4):
        aa.append(aa[-1]-2*ze[p]/4**p)
    bb = [F(7, 8)*zo[3]]
    for q in range(1, 4):
        bb.append((1-F(1, 2**(2*q+3)))*zo[2*q+3]
                  -(1-F(1, 2**(2*q+1)))*zo[2*q+1])
    ss = I(0)
    for k in range(4):
        ss += sum(aa[p]*bb[k-p] for p in range(k+1))/(k+1)
    kap = (8*ss/PI**2).widen(F(1, 480))
    harmonic = sum(F(1, k) for k in range(1, 257))
    gamma = I((harmonic-log(I(257))).lo,
              (harmonic-log(I(F(513, 2)))).hi)
    cstar = 4*(gamma+3*LOG2-log(PI))**2/PI**2+kap
    assert kap.lo > F(9, 10)
    assert gamma.lo > F(23, 40) and gamma.hi < F(3, 5)
    assert LOG2.lo > F(69, 100) and LOG2.hi < F(6932, 10000)
    assert log(PI).hi < F(23, 20)
    assert PI.lo**2 > F(197, 20) and PI.hi**2 < 10
    assert PI.lo > F(157, 50) and PI.hi < F(22, 7)
    k0 = 2*gamma+4*LOG2-2*log(PI)
    assert k0.lo > F(161, 100) and k0.hi < F(9, 5)
    assert log(PI/2).hi < F(23, 50)
    assert cstar.hi < F(4629, 2500)
    assert 2*LOG2.hi/PI.lo < F(221, 500)
    # The proof derives j from H0>7/25, d0>39/250, g0<43/125.
    assert F(7, 25)+F(39, 250)-F(43, 125) == F(23, 250)
    delta = F(249, 625)
    assert delta**2+delta*F(23, 250)-F(221, 500)**2 == F(71, 6250000)
    return kap, cstar


def constants(n):
    n = I(n)
    m, ll = n+1, log(n)
    hh, b = 1+ll, 4/PI**2
    r0 = log(I(F(5, 2)))+F(1, 18)
    tt = (4*ll**2-3*ll)/PI**2
    dd = ((52/PI**2)*hh+7)/n+10/n**2+20*hh/(PI*n**2)
    mesh = (b*(2*ll+2*r0)/n+(4+b*(ll+1/n))/(4*n**2-1)
            +b/(2*n-1)**2+(5+b*(log(n+F(1, 2))+2))/(4*(n-F(1, 2))**2))
    ebar = dd+mesh+1/n
    kd = ((6+16/(3*PI))*hh+2/PI)/n
    gn = 1+log(2+8*m/(3*PI))
    ma = 1/PI+4/PI**2
    gg = (7*ma*ll+F(111, 2)+(63+LOG2+4*log(PI)+7*log(m)
          +16*log(2*m)+F(3, 2)*gn)/PI)/m
    wn = (3*log(m)+LOG2+2*log(PI)+2)/(PI*m)
    ce = dd+gg+(64+16*ll)/n+318/n**2+mesh+wn
    a4 = 4/n+40*hh/(PI*n**2)
    c4 = a4+20/n**2
    kx = (F(19, 2)*hh+F(23, 3)*ll+F(155, 2))/n+152/n**2
    ky = kx+(17*ll+27)/n**2
    return tt, ebar, kd, ce, a4, c4, kx, ky


def trig_half():
    x = F(1, 2)
    fact, sine, cosine, sp, cp = 1, F(0), F(0), F(0), F(0)
    for k in range(24):
        if k:
            fact *= k
        if k % 2:
            sp, sine = sine, sine+(-1)**((k-1)//2)*x**k/fact
        else:
            cp, cosine = cosine, cosine+(-1)**(k//2)*x**k/fact
    return I(min(sp, sine), max(sp, sine)), I(min(cp, cosine), max(cp, cosine))


def gates():
    tt, eb, kd, ce, a4, c4, kx, ky = constants(512)
    uu = tt-eb+a4+F(23, 250)
    d1, d2 = F(11, 48)*uu-F(5, 12), F(11, 48)*uu
    l1, l2 = kx+F(5, 48), ky
    ee = d1*d2/(d1+d2)
    ff = (d2*l1+d1*l2)/(d1+d2)
    gg = (l1-l2)**2/(4*(d1+d2))
    peak = c4+l1**2/(4*d1)+l2**2/(4*d2)
    half = c4+gg+ff/2-ee/4
    vertex = l1/(2*d1)+l2/(2*d2)
    assert peak.hi < F(41, 1000)
    assert half.hi < -F(1, 7)
    assert vertex.hi < F(1, 2)
    assert d1.lo > 1
    assert ((17*log(I(512))+27)/512**2).hi < F(5, 48)
    sine, cosine = trig_half()
    theta, cc, t0 = tt+F(23, 250), F(221, 500)+2*kd, F(221, 500)
    assert (sine/cosine).lo > (cc/theta).hi
    outer = theta*(1-cosine)-cc*sine-t0**2*cosine/(2*theta)-ce-eb
    assert outer.lo > F(1, 2)
    tt, eb, kd, ce, *_ = constants(192)
    theta, cc = tt+F(23, 250), F(221, 500)+2*kd
    assert (cc/theta).hi < 1
    root_half = F(707107, 1000000)
    assert 2*root_half**2 > 1
    far = theta*(1-root_half)-cc*root_half-t0**2*root_half/(2*theta)-ce-eb
    assert far.lo > F(3, 100)
    ar, rr = F(15, 16), F(1, 2)
    aa = F(97, 100)*ar-rr/2
    ih = F(2303, 5000)*ar-F(471, 1250)*rr
    rh = F(4837, 1875)*ar-F(5, 3)*rr
    floor = F(539, 1936)*ih-(140*aa+400*rh)/(157*295)-800*aa/(3*295**2)
    assert floor > F(1, 20)
    return peak, half, vertex, outer, far, I(floor)


def decimal_enclosure(iv):
    # Rational rounding to six decimal places, then string formatting only.
    scale = 10**6
    lo = iv.lo.numerator*scale//iv.lo.denominator
    hi = -((-iv.hi).numerator*scale//(-iv.hi).denominator)
    def dec(k):
        sign = '-' if k < 0 else ''
        return sign+str(abs(k)//scale)+'.'+str(abs(k)%scale).zfill(6)
    return [dec(lo), dec(hi)]


if __name__ == '__main__':
    kap, cstar = elementary_constants()
    values = gates()
    names = ['P512_max', 'P512_half', 'P512_vertex', 'G512_one', 'G192_halfpi_lower', 'floor295']
    receipt = dict(zip(names, map(decimal_enclosure, values)))
    receipt.update(kappa_K3=decimal_enclosure(kap), Cstar=decimal_enclosure(cstar),
                   arithmetic='Fraction; outward 2^-128 grid; no floating-point',
                   python=platform.python_version(), assertions='PASS')
    print(json.dumps(receipt, indent=2, sort_keys=True))
