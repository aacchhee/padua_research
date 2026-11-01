"""Reviewer (L3 reconstruction 02) helper: exact rational interval arithmetic and certified
enclosures of Chebyshev nodes. Written independently; imports no developer module.

Interval endpoints are Fractions rounded OUTWARD to the dyadic grid 2^-PREC after every
multiplication, so every operation is a rigorous enclosure (no floating point is used in
any accepted bound).
"""
from fractions import Fraction as Fr
import mpmath as mp

PREC_BITS = 256
SCALE = 1 << PREC_BITS


def _down(q):
    q = Fr(q)
    return Fr((q.numerator * SCALE) // q.denominator, SCALE)


def _up(q):
    q = Fr(q)
    return Fr(-((-q.numerator * SCALE) // q.denominator), SCALE)


class Iv:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        lo = Fr(lo)
        hi = lo if hi is None else Fr(hi)
        assert lo <= hi, (lo, hi)
        self.lo, self.hi = lo, hi

    def __add__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self):
        return Iv(-self.hi, -self.lo)

    def __sub__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, o):
        return Iv(o) - self

    def __mul__(self, o):
        if not isinstance(o, Iv):
            o = Fr(o)
            if o >= 0:
                return Iv(_down(self.lo * o), _up(self.hi * o))
            return Iv(_down(self.hi * o), _up(self.lo * o))
        ps = (self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi)
        return Iv(_down(min(ps)), _up(max(ps)))
    __rmul__ = __mul__

    def mid(self):
        return (self.lo + self.hi) / 2

    def __repr__(self):
        return f"[{float(self.lo):.6e}, {float(self.hi):.6e}]"


def horner_univ(coeffs, z):
    """coeffs[i] = coefficient of z^i (Fractions or Iv); z an Iv."""
    acc = Iv(0)
    for c in reversed(coeffs):
        acc = acc * z + c
    return acc


def eval_poly2(pdict, xi, yi):
    """Rigorous enclosure of sum c_ab x^a y^b at intervals xi, yi (Horner in y, then x)."""
    if not pdict:
        return Iv(0)
    da = max(a for a, b in pdict)
    rows = []
    for a in range(da + 1):
        bs = {b: c for (aa, b), c in pdict.items() if aa == a}
        if not bs:
            rows.append(Iv(0)); continue
        db = max(bs)
        rows.append(horner_univ([Fr(bs.get(b, 0)) for b in range(db + 1)], yi))
    return horner_univ(rows, xi)


def eval_univ_exact(coeffs, q):
    acc = Fr(0)
    for c in reversed(coeffs):
        acc = acc * q + c
    return acc


def cheb_U_coeffs(k):
    """Integer coefficient list (ascending) of the Chebyshev polynomial U_k."""
    if k < 0:
        return [0]
    a, b = [1], [0, 2]
    if k == 0:
        return a
    for _ in range(k - 1):
        c = [0] + [2 * v for v in b]
        for i, v in enumerate(a):
            c[i] -= v
        a, b = b, c
    return b


def certified_cos_nodes(N, digits=60, halfwidth_exp=45):
    """Enclosures I_j of cos(j pi / N), j = 0..N, certified exactly:
    j = 0, N are exact (+1, -1); for 1 <= j <= N-1 the rational interval
    [c_j - 10^-e, c_j + 10^-e] is checked to contain a sign change of U_{N-1} (exact Fraction
    evaluation). The N-1 intervals are pairwise disjoint and U_{N-1} has degree N-1 with roots
    exactly {cos(j pi/N)}, so each interval contains exactly one root; ordering identifies it."""
    mp.mp.dps = digits
    U = cheb_U_coeffs(N - 1)
    eps = Fr(1, 10 ** halfwidth_exp)
    out = {0: Iv(1), N: Iv(-1)}
    prev_lo = Fr(2)
    for j in range(1, N):
        D = 10 ** (digits - 5)
        c = Fr(int(mp.floor(mp.cos(mp.pi * j / N) * D)), D)
        lo, hi = c - eps, c + eps
        s1, s2 = eval_univ_exact(U, lo), eval_univ_exact(U, hi)
        assert s1 * s2 < 0, ("no certified sign change", N, j)
        assert hi < prev_lo, "intervals not ordered/disjoint"
        prev_lo = lo
        out[j] = Iv(lo, hi)
    return out
