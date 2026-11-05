#!/usr/bin/env python3
"""Exact rational enclosures for theory/t3-01. Standard library only.

Input m=cos(beta)^2 is rational. Fractions are exact; pi/log/sqrt are
outward enclosed by elementary series and integer square roots. No floats
are used for any scientific value or acceptance comparison.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path
import hashlib
import json
import platform


@dataclass(frozen=True)
class IV:
    lo: Q
    hi: Q

    def __post_init__(self):
        object.__setattr__(self, "lo", Q(self.lo))
        object.__setattr__(self, "hi", Q(self.hi))
        assert self.lo <= self.hi

    def __add__(self, other):
        b = iv(other)
        return IV(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return IV(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -iv(other)

    def __rsub__(self, other):
        return iv(other) + -self

    def __mul__(self, other):
        b = iv(other)
        v = [self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi]
        return IV(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = iv(other)
        assert b.lo*b.hi > 0
        return self * IV(1/b.hi, 1/b.lo)

    def __rtruediv__(self, other):
        return iv(other) / self


def iv(x):
    return x if isinstance(x, IV) else IV(x, x)


def sqrt_q(x, bits=256):
    x = Q(x)
    assert x >= 0
    scale = 1 << bits
    k = isqrt((x.numerator << (2*bits)) // x.denominator)
    lo = Q(k, scale)
    return IV(lo, lo if lo*lo == x else Q(k+1, scale))


def log_unit(x, terms=100):
    """For 1<=x<=2: positive atanh series with geometric tail."""
    assert 1 <= x <= 2
    y = (x-1)/(x+1)
    s = sum((y**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    err = 2*y**(2*terms+1)/(Q(2*terms+1)*(1-y*y))
    return IV(2*s, 2*s+err)


LOG2 = log_unit(Q(2))


def log_q(x):
    x = Q(x)
    assert x > 0
    power = 0
    while x < 1:
        x *= 2
        power -= 1
    while x > 2:
        x /= 2
        power += 1
    return log_unit(x) + power*LOG2


def log_iv(x):
    x = iv(x)
    return IV(log_q(x.lo).lo, log_q(x.hi).hi)


def atan_q(x, terms=100):
    # terms even gives an odd-index final negative term, hence a lower sum.
    assert 0 <= x <= 1 and terms % 2 == 0
    s = sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    return IV(s, s+x**(2*terms+1)/Q(2*terms+1))


PI = 16*atan_q(Q(1, 5)) - 4*atan_q(Q(1, 239))
PI2 = PI*PI
SQRT2 = sqrt_q(2)


def harmonic(n):
    return sum((Q(1, j) for j in range(1, n+1)), Q(0))


def central_binomial(k):
    return Q(comb(2*k, k), 4**k)


def f_polynomial(k):
    """Coefficients of P_k(z), low degree first, exactly."""
    out = [Q(0)]*(k+1)
    for j in range(k+1):
        a = Q(1, 2*j+1)+Q(1, 2*j+2)
        v = (-1)**j*comb(k, j)*a/Q(j+1)
        for l in range(j+1):
            out[l] += v
    return out


def vertical(m, n):
    # Keep the upper endpoint strictly below 1 even for rational m very
    # close to 1, so the exact atanh enclosure never divides by zero.
    p = sqrt_q(m, bits=max(256, m.denominator.bit_length()+8))
    q2 = 1-m
    pl = iv(0) if m == 0 else p*log_iv((1+p)/(1-p))/2
    # Store p*M_l as rational + rational*pL, avoiding interval cancellation.
    ma, mb = Q(0), Q(1)
    moments = []
    for l in range(n+1):
        if l:
            ma = m/Q(2*l)+Q(2*l-1, 2*l)*q2*ma
            mb = Q(2*l-1, 2*l)*q2*mb
        moments.append((Q(1, 2*l+1)+ma, mb))
    sa = sb = Q(0)
    for k in range(n+1):
        poly = f_polynomial(k)
        ck = central_binomial(k)/2**k
        sa += ck*sum((a*moments[l][0] for l, a in enumerate(poly)), Q(0))
        sb += ck*sum((a*moments[l][1] for l, a in enumerate(poly)), Q(0))
    low = 4*(sa+sb*pl)/(PI2*SQRT2)
    tail = 6*Q(1, 2**n)*(1+pl)/(PI2*SQRT2)
    return IV(low.lo, low.hi+tail.hi), tail.hi


def horizontal_centre(m, n):
    ra = rb = Q(0)
    for k in range(1, n+1):
        a = b = Q(0)
        for j in range(k):
            w = Q((-1)**j*comb(k-1, j), 2*j+1)
            a += w*central_binomial(j)
            b += w/Q(2*j+1)
        fac = central_binomial(k)*m**k
        ra += fac*a
        rb += fac*b
    val = 1+8*(PI*ra/2-rb)/PI2
    tail = m**(n+1)/(1-m)
    return IV(val.lo, val.hi+tail), tail


def endpoint_moments(k):
    if k == 0:
        return LOG2, -PI2/12+LOG2*LOG2
    # (1-y)^k (1+y)^(k-1), exact polynomial coefficients.
    poly = [Q(0)]*(2*k)
    for a in range(k+1):
        for b in range(k):
            poly[a+b] += (-1)**a*comb(k, a)*comb(k-1, b)
    ua = wa = wb = Q(0)
    # Q_j = const + log2 coefficient for int y^j/(1+y).
    qa, qb = Q(0), Q(1)
    for j, v in enumerate(poly):
        qa, qb = Q(1, j+1)-qa, -qb
        ua += v/Q(j+1)
        wa += v*(-harmonic(j+1)-qa)/Q(j+1)
        wb += v*(1-qb)/Q(j+1)
    return iv(ua), wa+wb*LOG2


def horizontal_endpoint(m, n):
    z = 1-m
    log4q = 2*LOG2-log_q(z)/2
    val = iv(0)
    for k in range(n+1):
        u, w = endpoint_moments(k)
        d = 2*(harmonic(2*k)-harmonic(k))
        val += central_binomial(k)**2*z**k*((log4q-d)*u-w/2)
    val = 8*val/PI2
    _, w0 = endpoint_moments(0)
    tail = z**(n+1)/(1-z)*8*(log4q*LOG2-w0/2)/PI2
    return IV(val.lo, val.hi+tail.hi), tail.hi


def decimal_enclosure(x, digits):
    scale = 10**digits
    lower = (x.lo.numerator*scale)//x.lo.denominator
    upper = -((-x.hi.numerator*scale)//x.hi.denominator)
    def fmt(k):
        sign = "-" if k < 0 else ""
        k = abs(k)
        return f"{sign}{k//scale}.{k%scale:0{digits}d}"
    return {"lower": fmt(lower), "upper": fmt(upper),
            "lower_rational": str(Q(lower, scale)),
            "upper_rational": str(Q(upper, scale))}


def run(m, n, digits):
    v, vt = vertical(m, n)
    method = horizontal_centre if m <= Q(1, 2) else horizontal_endpoint
    h, ht = method(m, n)
    return {"m_cos_beta_squared": str(m), "terms_through": n,
            "vertical": decimal_enclosure(v, digits),
            "horizontal": decimal_enclosure(h, digits),
            "horizontal_chart": "centre" if m <= Q(1, 2) else "endpoint",
            "vertical_tail_upper": decimal_enclosure(iv(vt), digits+5)["upper"],
            "horizontal_tail_upper": decimal_enclosure(iv(ht), digits+5)["upper"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", action="append", default=[])
    ap.add_argument("--terms", type=int, default=72)
    ap.add_argument("--digits", type=int, default=16)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    ms = [Q(s) for s in (args.m or ["0", "1/4", "1/2", "3/4", "99/100"])]
    assert args.terms >= 0 and args.digits > 0 and all(0 <= m < 1 for m in ms)
    result = {"status": "PASS", "arithmetic": "exact Fraction with outward elementary enclosures",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "python": platform.python_version(),
              "rows": [run(m, args.terms, args.digits) for m in ms]}
    out = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(out)
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
