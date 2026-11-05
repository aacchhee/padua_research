#!/usr/bin/env python3
"""Direct outward Darboux quadrature of the positive T2 one-dimensional formulas.

This does not use the T3 series for F or K. Decimal arithmetic is directed;
Decimal sqrt/ln are correctly rounded to nearest and one adjacent decimal
on each side encloses them. Pi comes from t3_series's exact Machin bounds.
The receipt records coarse quadrature enclosures containing the separate
exact-series enclosures. This validates numerical implementation; T2's
analytic change-of-variable proof remains necessary.
"""
import argparse
from dataclasses import dataclass
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import t3_series as exact

PREC = 42


def rounded(op, mode):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = mode
        return op()


@dataclass(frozen=True)
class DI:
    lo: D
    hi: D

    def __post_init__(self):
        assert self.lo <= self.hi

    def __add__(self, other):
        b = di(other)
        return DI(rounded(lambda: self.lo+b.lo, ROUND_FLOOR),
                  rounded(lambda: self.hi+b.hi, ROUND_CEILING))

    __radd__ = __add__

    def __neg__(self):
        # copy_negate is exact, independent of the default decimal context.
        return DI(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -di(other)

    def __rsub__(self, other):
        return di(other) + -self

    def __mul__(self, other):
        b = di(other)
        pairs = [(self.lo, b.lo), (self.lo, b.hi), (self.hi, b.lo), (self.hi, b.hi)]
        lower = [rounded(lambda a=a, b=b: a*b, ROUND_FLOOR) for a, b in pairs]
        upper = [rounded(lambda a=a, b=b: a*b, ROUND_CEILING) for a, b in pairs]
        return DI(min(lower), max(upper))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = di(other)
        assert b.lo*b.hi > 0
        return self*DI(rounded(lambda: D(1)/b.hi, ROUND_FLOOR),
                       rounded(lambda: D(1)/b.lo, ROUND_CEILING))

    def __rtruediv__(self, other):
        return di(other)/self


def di(x):
    if isinstance(x, DI):
        return x
    if isinstance(x, Q):
        return DI(rounded(lambda: D(x.numerator)/D(x.denominator), ROUND_FLOOR),
                  rounded(lambda: D(x.numerator)/D(x.denominator), ROUND_CEILING))
    return DI(D(x), D(x))


def elementary(x, name):
    x = di(x)
    with localcontext() as c:
        c.prec = PREC
        lo = getattr(x.lo, name)().next_minus()
        hi = getattr(x.hi, name)().next_plus()
    return DI(lo, hi)


def sqrt(x):
    return elementary(x, "sqrt")


def log(x):
    return elementary(x, "ln")


PI = DI(di(exact.PI.lo).lo, di(exact.PI.hi).hi)
PI2 = PI*PI
LOG2 = log(2)


def f_value(r):
    if r.lo == r.hi == 0:
        return 2*LOG2
    if r.lo == r.hi == 1:
        return log(1+sqrt(2))+1/(1+sqrt(2))
    a = sqrt(1+r*r)
    return 2*(log(1+a)-r*log(r+a))/(1-r*r)


def vertical_quad(m, cells):
    # F(r) decreases, and F(sqrt(q²+p²x²))/sqrt(...) decreases in x.
    p2, q2 = di(m), di(1-m)
    values = [f_value(di(Q(j, cells))) for j in range(cells+1)]
    central = DI(directed_sum((x.lo for x in values[1:]), ROUND_FLOOR),
                 directed_sum((x.hi for x in values[:-1]), ROUND_CEILING))/cells
    if m == 0:
        return 4*central/PI2
    values = []
    for j in range(cells+1):
        r = di(1) if j == cells else sqrt(q2+p2*di(Q(j*j, cells*cells)))
        values.append(f_value(r)/r)
    excess = DI(directed_sum((x.lo for x in values[1:]), ROUND_FLOOR),
                directed_sum((x.hi for x in values[:-1]), ROUND_CEILING))/cells
    return 4*(central+p2*excess)/PI2


def k_quad(t, cells):
    # K(sqrt(1-t²))=2 int_0^(t^-1/2) [(1+x²)(1+t²x²)]^-1/2 dx.
    # The integrand decreases in x, so endpoint sums enclose the integral.
    radius = 1/sqrt(t)
    low, high = di(0), di(0)
    old = di(1)
    for j in range(1, cells+1):
        x = radius*di(Q(j, cells))
        new = 1/sqrt((1+x*x)*(1+t*t*x*x))
        low += new
        high += old
        old = new
    return DI((2*radius*low/cells).lo, (2*radius*high/cells).hi)


def horizontal_quad(m, outer_cells, inner_cells, epsilon):
    q = sqrt(di(1-m))
    end = 1-epsilon
    ks = []
    for j in range(outer_cells+1):
        y = di(end*Q(j, outer_cells))
        t = q*sqrt(1-y*y)
        ks.append(k_quad(t, inner_cells))
    low, high = di(0), di(0)
    for j in range(outer_cells):
        left = di(end*Q(j, outer_cells))
        right = di(end*Q(j+1, outer_cells))
        # K increases with y; independently bound the decreasing 1/(1+y).
        low += di(ks[j].lo)/(1+right)
        high += di(ks[j+1].hi)/(1+left)
    low *= di(end/Q(outer_cells))
    high *= di(end/Q(outer_cells))
    # On y in [1-eps,1], K <= log(4/q)-log(1-y)/2+q/2.
    tail = di(epsilon)/(1+di(end))*(log(4/q)+q/2+(1-log(di(epsilon)))/2)
    return DI((8*low/PI2).lo, (8*(high+tail)/PI2).hi)


def directed_sum(items, mode):
    total = D(0)
    for x in items:
        total = rounded(lambda: total+x, mode)
    return total


def show(x):
    # Scientific decimal strings are exact endpoints, not float conversions.
    return {"lower": str(x.lo), "upper": str(x.hi)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--series-receipt", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--vertical-cells", type=int, default=512)
    ap.add_argument("--outer-cells", type=int, default=64)
    ap.add_argument("--inner-cells", type=int, default=128)
    args = ap.parse_args()
    src = json.loads(args.series_receipt.read_text())
    rows = []
    for row in src["rows"]:
        m = Q(row["m_cos_beta_squared"])
        v = vertical_quad(m, args.vertical_cells)
        h = horizontal_quad(m, args.outer_cells, args.inner_cells, Q(1, 4096))
        for key, enclosure in [("vertical", v), ("horizontal", h)]:
            assert enclosure.lo <= D(row[key]["lower"])
            assert D(row[key]["upper"]) <= enclosure.hi
        rows.append({"m_cos_beta_squared": str(m), "vertical": show(v),
                     "horizontal": show(h), "contains_exact_series_enclosures": True})
    result = {"status": "PASS", "arithmetic": "outward Decimal Darboux quadrature",
              "precision": PREC, "python": platform.python_version(),
              "vertical_cells": args.vertical_cells,
              "outer_cells": args.outer_cells, "inner_cells": args.inner_cells,
              "endpoint_tail_width": "1/4096",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "series_receipt_sha256": hashlib.sha256(args.series_receipt.read_bytes()).hexdigest(),
              "rows": rows}
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
