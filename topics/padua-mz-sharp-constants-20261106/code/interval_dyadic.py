"""Integer endpoint intervals, with elementary series for P4.

Trusted arithmetic: Python arbitrary-precision integers and Fraction. Each
endpoint is an integer times 2**(-BITS). No floating arithmetic is used.
See attempts/P4.md for the mathematical finite reduction and limitations.
"""
from fractions import Fraction
from math import factorial

BITS = 256
SCALE = 1 << BITS
TAIL_BITS = 128


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo, self.hi = int(lo), int(lo if hi is None else hi)
        assert self.lo <= self.hi

    @classmethod
    def rational(cls, numerator, denominator=1):
        q = Fraction(numerator, denominator)
        return cls(q.numerator*SCALE//q.denominator,
                   ceildiv(q.numerator*SCALE, q.denominator))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, I) else I.rational(x)

    def __add__(self, other):
        other = self.coerce(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        p = [a*b for a in (self.lo, self.hi)
             for b in (other.lo, other.hi)]
        return I(min(p)//SCALE, ceildiv(max(p), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        assert other.lo > 0 or other.hi < 0, 'division interval contains zero'
        if other.hi < 0:
            return (-self)/(-other)
        lower = [a*SCALE//b for a in (self.lo,self.hi)
                 for b in (other.lo,other.hi)]
        upper = [ceildiv(a*SCALE,b) for a in (self.lo,self.hi)
                 for b in (other.lo,other.hi)]
        return I(min(lower), max(upper))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result, base = I.rational(1), self
        while n:
            if n % 2:
                result = result*base
            base = base*base
            n //= 2
        return result

    def absolute_upper(self):
        return max(abs(self.lo),abs(self.hi))

    def widen(self, radius):
        assert radius >= 0
        return I(self.lo-radius,self.hi+radius)

    def record(self):
        # Exact endpoints, plus outward decimal strings for human reading.
        places = 24
        unit = 10**places
        a = self.lo*unit//SCALE
        b = ceildiv(self.hi*unit,SCALE)
        def dec(v):
            sign = '-' if v < 0 else ''
            v = abs(v)
            return f'{sign}{v//unit}.{v%unit:0{places}d}'
        return dict(lo_integer=str(self.lo),hi_integer=str(self.hi),
                    binary_scale_bits=BITS,decimal_lo=dec(a),decimal_hi=dec(b))


def atan_reciprocal(n):
    """Alternating atan(1/n), remainder bounded by first omitted term."""
    total = I.rational(0)
    power, k, sign = n, 0, 1
    while True:
        term = I.rational(1,(2*k+1)*power)
        total = total+sign*term
        power *= n*n
        k += 1
        sign = -sign
        nxt = I.rational(1,(2*k+1)*power)
        if nxt.hi <= 2:
            # Remainder has the next term's sign.
            return I(total.lo-(nxt.hi if sign<0 else 0),
                     total.hi+(nxt.hi if sign>0 else 0))


def pi_interval():
    # Machin: pi/4=4 atan(1/5)-atan(1/239).
    return 16*atan_reciprocal(5)-4*atan_reciprocal(239)


def taylor_integral(x, kind):
    """Si or Cin entire series, with absolute geometric tail enclosure.

    Once ratios are <=1/2, the ratios decrease thereafter. The unsigned
    remaining terms are bounded by twice the first omitted one. Rounding
    interval widths are retained even during severe cancellation.
    """
    assert x.lo >= 0 and kind in ('si','cin')
    square = x*x
    if kind == 'si':
        k, term = 0, x
    else:
        k, term = 1, square/4
    total, sign = I.rational(0), 1
    while True:
        total = total+sign*term
        if kind == 'si':
            ratio = square*(2*k+1)/((2*k+2)*(2*k+3)**2)
        else:
            ratio = square*(2*k)/((2*k+2)**2*(2*k+1))
        nxt = term*ratio
        if ratio.hi*2 <= SCALE and 2*nxt.hi <= SCALE >> TAIL_BITS:
            return total.widen(2*nxt.hi)
        k += 1
        term, sign = nxt, -sign
        assert k < 2000, 'Taylor safety limit'


def laplace_fg(x, terms=20):
    """Finite geometric integral expansion; positive even-order remainder.

    F=∫ exp(-xt)/(1+t²), G=∫ t exp(-xt)/(1+t²).
    Since 1/(1+t²)=sum_(k<m)(-t²)^k+(-1)^m t^(2m)/(1+t²),
    the even-m remainders are positive and bounded by factorial integrals.
    """
    assert x.lo > 0 and terms > 0 and terms % 2 == 0
    inv = I.rational(1)/x
    inv2 = inv*inv
    tf, tg = inv, inv2
    f, g = I.rational(0), I.rational(0)
    for k in range(terms):
        sign = (-1)**k
        f, g = f+sign*tf, g+sign*tg
        tf = tf*inv2*((2*k+1)*(2*k+2))
        tg = tg*inv2*((2*k+2)*(2*k+3))
    return I(f.lo,f.hi+tf.hi), I(g.lo,g.hi+tg.hi)


def si_multiple(n, pi):
    assert n >= 1
    x = n*pi
    if n < 16:
        return taylor_integral(x,'si')
    f,_ = laplace_fg(x)
    return pi/2-((-1)**n)*f


def ci_multiple(n, pi):
    assert n >= 16
    _,g = laplace_fg(n*pi)
    return -((-1)**n)*g


def log_unit(q):
    """log(q) for rational 1<=q<=2, via atanh series."""
    assert 1 <= q <= 2
    z = I.rational((q-1)/(q+1))
    z2, term, total, k = z*z, z, I.rational(0), 0
    while True:
        total = total+2*term/(2*k+1)
        k += 1
        term = term*z2
        tail = 2*term/((2*k+1)*(I.rational(1)-z2))
        if tail.hi <= SCALE >> TAIL_BITS:
            return I(total.lo,total.hi+tail.hi)
        assert k < 2000


def log_rational(q):
    q = Fraction(q)
    assert q > 0
    exponent = 0
    while q < 1:
        q *= 2
        exponent -= 1
    while q > 2:
        q /= 2
        exponent += 1
    return log_unit(q)+exponent*log_unit(Fraction(2))


def model_scalars(J):
    pi = pi_interval()
    anchor = taylor_integral(16*pi,'cin')
    anchor_ci = ci_multiple(16,pi)
    d, si, si2 = [],[],[]
    for j in range(1,J+1):
        d.append(taylor_integral(2*j*pi,'cin') if j<8 else
                 anchor+log_rational(Fraction(j,8))+anchor_ci-ci_multiple(2*j,pi))
        si.append(si_multiple(j,pi))
        si2.append(si_multiple(2*j,pi))
    return pi,d,si,si2
