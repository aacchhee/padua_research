"""Independent replay of a supplied n=5 A5 spatial certificate.

The degree-independent replay core is adapted from the frozen independent n4
checker (SHA256 1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143).
This verifier imports no producer code and performs no subdivision, Newton
iteration, root isolation, or search.  It reconstructs the exact interpolation
problem and checks only the partition and the supplied witnesses.  A partial
certificate can be inspected with --allow-partial; that never certifies a count.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache, cmp_to_key
import gzip
import hashlib
import json
from math import isqrt, lcm
from pathlib import Path
import platform
import sys
import time

import sympy as sp


class Rejected(Exception):
    pass


def require(condition, message):
    if not condition:
        raise Rejected(message)


def rational(value):
    require(isinstance(value, (str, int)) and not isinstance(value, bool),
            "rational must be a string or integer")
    return Fraction(value)


PRECISION = 96
UNIT = 1 << PRECISION


def floor_scaled(q):
    return q.numerator * UNIT // q.denominator


def ceil_div(numerator, denominator):
    return -((-numerator) // denominator)


@dataclass(frozen=True)
class Interval:
    """Closed outward dyadic interval; endpoints are integer multiples of 2^-96."""
    lo: int
    hi: int

    @staticmethod
    def bounds(lo, hi):
        lo, hi = Fraction(lo), Fraction(hi)
        require(lo <= hi, "reversed interval")
        return Interval(floor_scaled(lo),
                        ceil_div(hi.numerator * UNIT, hi.denominator))

    @staticmethod
    def point(q):
        return Interval.bounds(q, q)

    def __add__(self, other):
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products) // UNIT, ceil_div(max(products), UNIT))

    def power(self, exponent):
        if exponent == 0:
            return ONE
        divisor = UNIT ** (exponent - 1)
        if exponent & 1:
            low, high = self.lo ** exponent, self.hi ** exponent
        else:
            ends = (self.lo ** exponent, self.hi ** exponent)
            low = 0 if self.lo <= 0 <= self.hi else min(ends)
            high = max(ends)
        return Interval(low // divisor, ceil_div(high, divisor))

    def nonzero(self):
        return self.lo > 0 or self.hi < 0

    def scaled_sign(self, sign):
        return self if sign == 1 else -self


ZERO = Interval(0, 0)
ONE = Interval(UNIT, UNIT)
RADICALS = {}
for radicand in (3, 5, 15):
    lower = isqrt(radicand * UNIT * UNIT)
    require(lower * lower < radicand * UNIT * UNIT < (lower + 1) ** 2,
            "invalid radical bracket")
    RADICALS[radicand] = Interval(lower, lower + 1)


def interval_sum(values):
    lo = hi = 0
    for value in values:
        lo += value.lo
        hi += value.hi
    return Interval(lo, hi)


x, y = sp.symbols("x y")
SQRT3, SQRT5, SQRT15 = sp.sqrt(3), sp.sqrt(5), sp.sqrt(15)
FIELD = sp.QQ.algebraic_field(SQRT3, SQRT5)
require(sp.expand(FIELD.ext.as_expr()-SQRT3-SQRT5) == 0,
        "unexpected primitive field generator")
# alpha=sqrt(3)+sqrt(5): alpha^2=8+2sqrt(15),
# alpha^3=18sqrt(3)+14sqrt(5). The following exact native conversion
# avoids reparsing an expanded radical expression at every node breakpoint.
NATIVE_RADICALS = tuple(FIELD.from_sympy(q) for q in (sp.Integer(1), SQRT3, SQRT5, SQRT15))


def native(value):
    return value if FIELD.of_type(value) else FIELD.from_sympy(sp.sympify(value))


def parse_native_field(value):
    require(isinstance(value, list) and len(value) == 4, "FIELD needs four rational coefficients")
    coefficients = tuple(map(rational, value))
    return sum((FIELD.convert(sp.Rational(q.numerator, q.denominator))*basis
                for q, basis in zip(coefficients, NATIVE_RADICALS)), FIELD.zero)


@lru_cache(maxsize=65536)
def basis_coefficients(expression):
    coefficients = native(expression).to_list()
    require(len(coefficients) <= 4, "unexpected primitive field degree")
    coefficients = [Fraction(0)]*(4-len(coefficients)) + [Fraction(str(q)) for q in coefficients]
    a3, a2, a1, a0 = coefficients
    return a0+8*a2, a1+18*a3, a1+14*a3, 2*a2


def field_interval(coefficients):
    answer = Interval.point(coefficients[0])
    for coefficient, radicand in zip(coefficients[1:], (3, 5, 15)):
        answer += Interval.point(coefficient) * RADICALS[radicand]
    return answer


def parse_field(value):
    require(isinstance(value, list) and len(value) == 4,
            "FIELD must contain four rational coefficients")
    coefficients = tuple(map(rational, value))
    expression = sum(sp.Rational(q.numerator, q.denominator) * basis
                     for q, basis in zip(coefficients, (1, SQRT3, SQRT5, SQRT15)))
    return expression, field_interval(coefficients)


def polynomial_terms(poly):
    return tuple((i, j, field_interval(basis_coefficients(c)))
                 for (i, j), c in poly.terms() if c != 0)


def evaluate(terms, box):
    xx, yy = box
    # Each power is bounded directly, not by repeated interval multiplication.
    xp = tuple(xx.power(i) for i in range(6))
    yp = tuple(yy.power(i) for i in range(6))
    return interval_sum(c * (xp[i] * yp[j]) for i, j, c in terms)


def centered(terms, dx, dy, box):
    xx, yy = box
    cx = (xx.lo + xx.hi) // 2
    cy = (yy.lo + yy.hi) // 2
    center = (Interval(cx, cx), Interval(cy, cy))
    delta = (Interval(xx.lo - cx, xx.hi - cx),
             Interval(yy.lo - cy, yy.hi - cy))
    mean_value = (evaluate(terms, center) + evaluate(dx, box) * delta[0]
                  + evaluate(dy, box) * delta[1])
    natural = evaluate(terms, box)
    result = Interval(max(natural.lo, mean_value.lo),
                      min(natural.hi, mean_value.hi))
    require(result.lo <= result.hi, "empty intersection of proven enclosures")
    return result


def reconstruct():
    # Explicit exact node coordinates, independently of producer trigonometry.
    xs = [1, (1 + SQRT5) / 4, (SQRT5 - 1) / 4,
          (1 - SQRT5) / 4, -(1 + SQRT5) / 4, -1]
    ys = [1, SQRT3 / 2, sp.Rational(1, 2), 0,
          sp.Rational(-1, 2), -SQRT3 / 2, -1]
    nodes = [(sp.sympify(xs[j]), sp.sympify(ys[k]))
             for j in range(6) for k in range(7) if (j + k) % 2 == 0]
    powers = [(i, degree - i) for degree in range(6)
              for i in range(degree, -1, -1)]
    v = sp.polys.matrices.DomainMatrix.from_Matrix(
        sp.Matrix([[u ** i * w ** j for i, j in powers] for u, w in nodes])
    ).convert_to(FIELD)
    inverse = v.inv()
    require((v * inverse).to_Matrix() == sp.eye(21), "V inverse identity")
    entries = inverse.to_Matrix()
    cardinals = tuple(sp.Poly(sum(entries[k, b] * x ** i * y ** j
                                 for k, (i, j) in enumerate(powers)),
                              x, y, domain=FIELD) for b in range(21))
    require(sum(cardinals).as_expr() == 1, "partition of unity")
    for row, point in enumerate(nodes):
        for column, cardinal in enumerate(cardinals):
            value = FIELD.from_sympy(cardinal.as_expr().subs(dict(zip((x, y), point))))
            require(value == (FIELD.one if row == column else FIELD.zero),
                    "exact cardinal identity")
    return nodes, cardinals


def parse_rectangle(value):
    require(isinstance(value, list) and len(value) == 2, "rectangle dimension")
    bounds = []
    for coordinate in value:
        require(isinstance(coordinate, list) and len(coordinate) == 2,
                "coordinate interval dimension")
        low, high = map(rational, coordinate)
        require(low <= high, "reversed rational rectangle")
        bounds.append((low, high))
    return tuple(bounds), tuple(Interval.bounds(a, b) for a, b in bounds)


def parse_matrix(value):
    require(isinstance(value, list) and len(value) == 2 and
            all(isinstance(row, list) and len(row) == 2 for row in value),
            "preconditioner dimension")
    matrix = tuple(tuple(map(rational, row)) for row in value)
    require(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] != 0,
            "singular preconditioner")
    return matrix, tuple(tuple(Interval.point(q) for q in row) for row in matrix)


def contains_rational(outer, inner):
    return all(a <= c and d <= b for (a, b), (c, d) in zip(outer, inner))


def path_rectangle(path):
    require(isinstance(path, str) and set(path) <= {"0", "1"}, "invalid path")
    bounds = [[Fraction(-1), Fraction(1)], [Fraction(-1), Fraction(1)]]
    for bit in path:
        axis = 0 if bounds[0][1] - bounds[0][0] >= bounds[1][1] - bounds[1][0] else 1
        low, high = bounds[axis]
        midpoint = (low + high) / 2
        bounds[axis] = [low, midpoint] if bit == "0" else [midpoint, high]
    return tuple(map(tuple, bounds)), tuple(Interval.bounds(a, b) for a, b in bounds)


def partition(paths):
    require(len(paths) == len(set(paths)), "duplicate leaf path")
    ordered = sorted(paths)
    for previous, current in zip(ordered, ordered[1:]):
        require(not current.startswith(previous), "leaf paths are not prefix-free")
    mass = sum((Fraction(1, 1 << len(path)) for path in paths), Fraction(0))
    require(mass <= 1, "leaf partition mass exceeds one")
    return mass == 1


@lru_cache(maxsize=65536)
def exact_field_sign(expression):
    coefficients = basis_coefficients(expression)
    if not any(coefficients):
        return 0
    # Refine radical arithmetic only; this does not isolate geometric roots.
    bits = 96
    while bits <= 6144:
        unit = 1 << bits
        low = high = coefficients[0]
        for coefficient, radicand in zip(coefficients[1:], (3, 5, 15)):
            root = isqrt(radicand * unit * unit)
            a, b = Fraction(root, unit), Fraction(root + 1, unit)
            low += coefficient * (a if coefficient >= 0 else b)
            high += coefficient * (b if coefficient >= 0 else a)
        if low > 0:
            return 1
        if high < 0:
            return -1
        bits *= 2
    raise Rejected("exact algebraic sign not separated by radical refinement")


def rational_norm(poly):
    """Explicit product of four conjugates, independently of Poly.norm()."""
    require(not poly.is_zero, "zero norm input")
    variable = poly.gens[0]
    coefficients = [(monomial, basis_coefficients(c)) for monomial, c in poly.terms()]
    answer = sp.Poly(1, variable, domain=FIELD)
    for sign2, sign5 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        conjugate = 0
        for (degree,), cs in coefficients:
            signs = (1, sign2, sign5, sign2 * sign5)
            c = sum(sp.Rational(q.numerator, q.denominator) * sign * basis
                    for q, sign, basis in zip(cs, signs, (1, SQRT3, SQRT5, SQRT15)))
            conjugate += c * variable ** degree
        answer *= sp.Poly(conjugate, variable, domain=FIELD)
    rationals = {}
    for monomial, coefficient in answer.terms():
        cs = basis_coefficients(coefficient)
        require(not any(cs[1:]), "field norm is not rational")
        rationals[monomial] = sp.Rational(cs[0].numerator, cs[0].denominator)
    return sp.Poly.from_dict(rationals, variable, domain=sp.QQ).sqf_part().monic()


def verify_root_partition(poly, intervals):
    """Check given all-real root intervals by exact Sturm counts, without isolation."""
    require(not poly.is_zero, "zero root-partition polynomial")
    chain = [poly]
    if poly.degree() > 0:
        chain.append(poly.diff())
        while True:
            remainder = -chain[-2].rem(chain[-1])
            if remainder.is_zero:
                break
            chain.append(remainder)

    def variations(where):
        signs = []
        for q in chain:
            if where == "-inf":
                sign = sp.sign(q.LC()) * (-1 if q.degree() % 2 else 1)
            elif where == "+inf":
                sign = sp.sign(q.LC())
            else:
                sign = sp.sign(q.eval(sp.Rational(where.numerator, where.denominator)))
            if sign:
                signs.append(int(sign))
        return sum(a != b for a, b in zip(signs, signs[1:]))

    parsed = []
    for value in intervals:
        require(isinstance(value, list) and len(value) == 2, "root interval dimension")
        low, high = map(rational, value)
        require(low <= high, "reversed root interval")
        require(not parsed or parsed[-1][1] < low, "root intervals not strictly disjoint/ordered")
        if low == high:
            require(poly.eval(sp.Rational(low.numerator, low.denominator)) == 0,
                    "singleton is not an exact rational root")
        else:
            require(poly.eval(sp.Rational(low.numerator, low.denominator)) != 0 and
                    poly.eval(sp.Rational(high.numerator, high.denominator)) != 0,
                    "non-singleton root interval has root endpoint")
            require(variations(low) - variations(high) == 1,
                    "root interval does not contain exactly one root")
        parsed.append((low, high))
    require(len(parsed) == variations("-inf") - variations("+inf"),
            "root partition omits real roots")
    return tuple(parsed)


class Verifier:
    def __init__(self):
        self.nodes, self.cardinals = reconstruct()
        self.lterms = tuple(map(polynomial_terms, self.cardinals))
        self.ldx = tuple(polynomial_terms(p.diff(x)) for p in self.cardinals)
        self.ldy = tuple(polynomial_terms(p.diff(y)) for p in self.cardinals)
        self.monomials = tuple((i, degree - i) for degree in range(6)
                               for i in range(degree, -1, -1))
        raw = [[basis_coefficients(cardinal.coeff_monomial(x ** i * y ** j))
                for i, j in self.monomials] for cardinal in self.cardinals]
        self.denominator = lcm(*(q.denominator for row in raw for coefficient in row
                                 for q in coefficient))
        self.integer_cardinals = tuple(tuple(int(q * self.denominator)
                                               for coefficient in row for q in coefficient)
                                       for row in raw)
        self.negative_sum = tuple(-sum(row[k] for row in self.integer_cardinals)
                                  for k in range(84))
        self.roots = {}
        self.dispositions = Counter()
        self.patterns = 0
        self.implicit_masks = False
        self.flat_occurrences = []
        self.exception_occurrences = []
        self.edge_flat_values = []
        self.node_cones = {}
        self.node_leaves = 0
        self.node_statuses = Counter()
        self.lhessian = tuple(tuple(polynomial_terms(q) for q in
                                   (p.diff((x, 2)), p.diff(x).diff(y), p.diff((y, 2))))
                              for p in self.cardinals)

    def node_certificates(self, records):
        """Verify every supplied node gap and every accepted cone independently.

        Breakpoint coverage is derived from the reconstructed exact gradients.
        No supplied scalar minimum or sampled subset receives discard authority.
        """
        require(isinstance(records, list) and len(records) == 21,
                "all 21 ordered node-cone records are required")
        self.node_cones = {}
        self.node_statuses = Counter()

        @lru_cache(maxsize=16384)
        def canonical(expression):
            return native(expression)

        def exact_at(poly, node):
            return poly.rep.eval(node[0], 0).eval(node[1], 0)

        def equality(a, b):
            return native(a) == native(b)

        def sr(q):
            return native(sp.Rational(q.numerator, q.denominator))

        all_breakpoints = 0
        for index, (record, node) in enumerate(zip(records, self.nodes)):
            node = tuple(map(native, node))
            require(type(record.get("index")) is int and record["index"] == index,
                    "node indices missing, duplicated, or reordered")
            encoded_node = record["node"]
            require(isinstance(encoded_node, list) and len(encoded_node) == 2,
                    "node coordinate dimension")
            decoded_node = [parse_native_field(value) for value in encoded_node]
            require(all(equality(a, b) for a, b in zip(decoded_node, node)),
                    "supplied node differs from exact board")
            gradients = tuple((exact_at(p.diff(x), node), exact_at(p.diff(y), node))
                              for p in self.cardinals)
            require(all(equality(sum(g[axis] for g in gradients), 0) for axis in (0, 1)),
                    "exact node gradients do not reproduce constants")

            def gap(axis, fixed, t):
                dots = [canonical(fixed*g[axis] + t*g[1-axis]) for g in gradients]
                return canonical(dots[index] + sum(exact_field_sign(value)*value
                                                   for i, value in enumerate(dots) if i != index))

            expected_segments = []
            for axis in (0, 1):
                for fixed in (-1, 1):
                    if (equality(node[axis], -1) and fixed == -1) or \
                            (equality(node[axis], 1) and fixed == 1):
                        continue
                    low = sp.Integer(0) if equality(node[1-axis], -1) else sp.Integer(-1)
                    high = sp.Integer(0) if equality(node[1-axis], 1) else sp.Integer(1)
                    expected_segments.append((axis, fixed, low, high))
            segments = record["segments"]
            require(isinstance(segments, list) and len(segments) == len(expected_segments),
                    "feasible direction-side segments are incomplete")
            m = rational(record["gap_lower"])
            for segment, (axis, fixed, low, high) in zip(segments, expected_segments):
                require(type(segment.get("axis")) is int and segment["axis"] == axis and
                        type(segment.get("fixed")) is int and segment["fixed"] == fixed,
                        "feasible direction-side segments missing, duplicated, or reordered")
                supplied_bounds = segment["bounds"]
                require(isinstance(supplied_bounds, list) and len(supplied_bounds) == 2 and
                        tuple(map(rational, supplied_bounds)) == (Fraction(int(low)), Fraction(int(high))),
                        "incorrect feasible direction-side bounds")
                supplied = segment["breaks"]
                require(isinstance(supplied, list) and len(supplied) >= 2,
                        "direction segment endpoints/breakpoints missing")
                breaks = [parse_native_field(value) for value in supplied]
                require(equality(breaks[0], low) and equality(breaks[-1], high),
                        "direction breakpoint list omits segment endpoints")
                require(all(exact_field_sign(b-low) >= 0 and exact_field_sign(high-b) >= 0
                            for b in breaks), "direction breakpoint outside feasible side")
                require(all(exact_field_sign(b-a) > 0 for a, b in zip(breaks, breaks[1:])),
                        "direction breakpoints duplicate or are not exactly sorted")
                keys = {basis_coefficients(value) for value in breaks}
                for i, gradient in enumerate(gradients):
                    if i == index or equality(gradient[1-axis], 0):
                        continue
                    zero = canonical(-fixed*gradient[axis]/gradient[1-axis])
                    if exact_field_sign(zero-low) >= 0 and exact_field_sign(high-zero) >= 0:
                        require(basis_coefficients(zero) in keys,
                                "a cardinal directional zero breakpoint was omitted")
                for t in breaks:
                    require(exact_field_sign(gap(axis, fixed, t)-sr(m)) >= 0,
                            "claimed node gap lower bound exceeds a breakpoint value")
                all_breakpoints += len(breaks)

            zero = record.get("zero_witness")
            if zero is not None:
                axis, fixed = zero["axis"], zero["fixed"]
                require(type(axis) is int and type(fixed) is int,
                        "invalid zero-gap direction")
                matching = [q for q in expected_segments if q[0] == axis and q[1] == fixed]
                require(len(matching) == 1, "zero-gap direction is infeasible")
                t = parse_native_field(zero["t"])
                low, high = matching[0][2:]
                require(exact_field_sign(t-low) >= 0 and exact_field_sign(high-t) >= 0 and
                        equality(gap(axis, fixed, t), 0), "false exact zero-gap witness")
            status = record["status"]
            require(status in ("accepted", "zero_gap", "no_cube"), "unknown node-cone status")
            self.node_statuses[status] += 1
            if status == "zero_gap":
                require(m <= 0 or zero is not None, "unsupported zero-gap status")
                print(json.dumps({"verified_node": index, "status": status}), file=sys.stderr, flush=True)
                continue
            require(m > 0 and zero is None, "positive node-cone status has no positive certified gap")
            if status == "no_cube":
                # This status grants no exclusion and makes no universal
                # impossibility claim about other rectangles.
                print(json.dumps({"verified_node": index, "status": status}), file=sys.stderr, flush=True)
                continue

            bounds, box = parse_rectangle(record["B"])
            require(all(exact_field_sign(z-sr(a)) > 0 and exact_field_sign(sr(b)-z) > 0
                        for z, (a, b) in zip(node, bounds)), "node not strictly inside cone B")
            for z, (a, b) in zip(node, bounds):
                if equality(z, -1):
                    require(b < 1, "node cone meets an inactive opposite square face")
                elif equality(z, 1):
                    require(a > -1, "node cone meets an inactive opposite square face")
                else:
                    require(-1 < a and b < 1, "node cone meets an inactive square face")
            radius = rational(record["R"])
            require(radius > 0 and all(exact_field_sign(sr(radius)-(z-sr(a))) >= 0 and
                                      exact_field_sign(sr(radius)-(sr(b)-z)) >= 0
                                      for z, (a, b) in zip(node, bounds)),
                    "node cone R does not bound the entire supplied rectangle")
            positive = rational(record["Lq_lower"])
            bound = centered(self.lterms[index], self.ldx[index], self.ldy[index], box)
            require(positive > 0 and Fraction(bound.lo, UNIT) >= positive,
                    "node cardinal is not certified positive on entire B")
            h_i = tuple(map(rational, record["H_i"]))
            require(len(h_i) == 21 and all(h >= 0 for h in h_i), "node Hessian bounds incomplete")
            for bound_i, entries in zip(h_i, self.lhessian):
                xx, xy, yy = (evaluate(terms, box) for terms in entries)
                actual = (max(abs(xx.lo), abs(xx.hi)) + 2*max(abs(xy.lo), abs(xy.hi)) +
                          max(abs(yy.lo), abs(yy.hi)))
                require(Fraction(actual, UNIT) <= bound_i, "node Hessian quadratic-form bound failed")
            h = rational(record["H"])
            require(h >= sum(h_i) and radius*h < m,
                    "node radial remainder inequality R*H < m failed")
            self.node_cones[index] = bounds
            print(json.dumps({"verified_node": index, "status": status}), file=sys.stderr, flush=True)
        return {"node_status_counts": dict(sorted(self.node_statuses.items())),
                "verified_node_records": len(records), "verified_direction_breakpoints": all_breakpoints,
                "accepted_node_cones": len(self.node_cones)}

    @lru_cache(None)
    def exact_pattern(self, mask):
        p = sum((1 if mask & (1 << i) else -1) * cardinal
                for i, cardinal in enumerate(self.cardinals))
        a, b = p.diff(x), p.diff(y)
        polys = (p, a, b, a.diff(x), a.diff(y), b.diff(y))
        return polys, tuple(map(polynomial_terms, polys))

    @lru_cache(None)
    def coefficients(self, mask):
        if mask == 0:
            return self.negative_sum
        bit = mask & -mask
        previous = self.coefficients(mask ^ bit)
        row = self.integer_cardinals[bit.bit_length() - 1]
        return tuple(a + 2 * b for a, b in zip(previous, row))

    def integer_field_interval(self, numbers):
        denominator = self.denominator
        lo = numbers[0] * UNIT // denominator
        hi = ceil_div(numbers[0] * UNIT, denominator)
        for numerator, radicand in zip(numbers[1:], (3, 5, 15)):
            radical = RADICALS[radicand]
            low, high = ((numerator * radical.lo, numerator * radical.hi)
                         if numerator >= 0 else
                         (numerator * radical.hi, numerator * radical.lo))
            lo += low // denominator
            hi += ceil_div(high, denominator)
        return Interval(lo, hi)

    @lru_cache(None)
    def terms_for(self, mask, dx=0, dy=0):
        coefficients = self.coefficients(mask)
        terms = []
        for k, (i, j) in enumerate(self.monomials):
            if i < dx or j < dy:
                continue
            multiplier = 1
            for count in range(dx):
                multiplier *= i - count
            for count in range(dy):
                multiplier *= j - count
            coefficient = tuple(multiplier * q for q in coefficients[4*k:4*k+4])
            if any(coefficient):
                terms.append((i - dx, j - dy, self.integer_field_interval(coefficient)))
        return tuple(terms)

    def hessian_terms(self, mask):
        return (self.terms_for(mask, 2, 0), self.terms_for(mask, 1, 1),
                self.terms_for(mask, 0, 2))

    @lru_cache(None)
    def factor(self, mask):
        polys, _ = self.exact_pattern(mask)
        _, a, b, *_ = polys
        g = sp.gcd(a, b)
        require(g.total_degree() > 0, "factor witness has constant gcd")
        aa, bb = a.exquo(g), b.exquo(g)
        f = g.sqf_part()
        require(aa * g == a and bb * g == b, "gcd quotient identities")
        require(sp.gcd(f, sp.gcd(f.diff(x), f.diff(y))).total_degree() == 0,
                "factor is not squarefree")
        return tuple(map(polynomial_terms, (aa, bb, f.diff(x), f.diff(y))))

    def injection(self, mask, matrix, box):
        xx, xy, yy = (evaluate(t, box) for t in self.hessian_terms(mask))
        hessian = ((xx, xy), (xy, yy))
        error = tuple(tuple((ONE if i == j else ZERO) - interval_sum(
            matrix[i][k] * hessian[k][j] for k in range(2))
                            for j in range(2)) for i in range(2))
        row_bounds = [sum(max(abs(entry.lo), abs(entry.hi)) for entry in row)
                      for row in error]
        require(max(row_bounds) < UNIT, "injectivity norm is not strictly below one")
        return error

    def root(self, record):
        identifier, mask = record["id"], record["mask"]
        require(isinstance(identifier, int) and not isinstance(identifier, bool)
                and identifier not in self.roots, "duplicate/invalid root id")
        require(isinstance(mask, int) and not isinstance(mask, bool) and
                0 <= mask < (1 << 21), "invalid root mask")
        bounds, box = parse_rectangle(record["R"])
        require(all(-1 < a < b < 1 for a, b in bounds), "root box outside open square")
        _, c = parse_matrix(record["C"])
        e = self.injection(mask, c, box)
        midpoints = tuple((a + b) / 2 for a, b in bounds)
        center = tuple(Interval.point(q) for q in midpoints)
        delta = tuple(Interval.bounds(a - q, b - q)
                      for (a, b), q in zip(bounds, midpoints))
        gradient = (evaluate(self.terms_for(mask, 1, 0), center),
                    evaluate(self.terms_for(mask, 0, 1), center))
        krawczyk = tuple(center[i] - interval_sum(c[i][j] * gradient[j] for j in range(2))
                         + interval_sum(e[i][j] * delta[j] for j in range(2))
                         for i in range(2))
        require(all(a < Fraction(z.lo, UNIT) <= Fraction(z.hi, UNIT) < b
                    for (a, b), z in zip(bounds, krawczyk)), "Krawczyk inclusion failed")
        xx, xy, yy = (evaluate(t, box) for t in self.hessian_terms(mask))
        require(xx.hi < 0 and (xx * yy - xy.power(2)).lo > 0,
                "root Hessian not negative definite")
        require(all(evaluate(t, box).scaled_sign(1 if mask & (1 << i) else -1).lo > 0
                    for i, t in enumerate(self.lterms)), "root cardinal sign not strict")
        for other in self.roots.values():
            require(any(b < c0 or d < a for (a, b), (c0, d) in
                        zip(bounds, other["bounds"])), "root boxes are not disjoint")
        value = evaluate(self.terms_for(mask), box)
        self.roots[identifier] = {"mask": mask, "bounds": bounds, "C": c,
                                  "value": [str(Fraction(value.lo, UNIT)),
                                            str(Fraction(value.hi, UNIT))]}

    def disposition(self, mask, record, bounds, box):
        at, bt = self.terms_for(mask, 1, 0), self.terms_for(mask, 0, 1)
        code = record["code"]
        if code == "flat":
            require(not at or not bt, "false flat witness")
            self.flat_occurrences.append((mask, box))
            self.exception_occurrences.append((mask, box))
        elif code == "gradient":
            require(evaluate(at, box).nonzero() or evaluate(bt, box).nonzero(),
                    "gradient not separated from zero")
        elif code == "hessian":
            xx, xy, yy = (evaluate(t, box) for t in self.hessian_terms(mask))
            require(xx.lo > 0 or yy.lo > 0 or (xx * yy - xy.power(2)).hi < 0,
                    "no strict positive-curvature/negative-determinant exclusion")
        elif code == "factor":
            aa, bb, fx, fy = self.factor(mask)
            require((evaluate(aa, box).nonzero() or evaluate(bb, box).nonzero()) and
                    (evaluate(fx, box).nonzero() or evaluate(fy, box).nonzero()),
                    "common-gradient regular-curve witness failed")
            self.exception_occurrences.append((mask, box))
        elif code == "regular_point":
            polys, _ = self.exact_pattern(mask)
            _, a, b, *_ = polys
            point = [parse_field(q) for q in record["point"]]
            require(len(point) == 2, "point dimension")
            substitution = {x: point[0][0], y: point[1][0]}
            require(all(FIELD.from_sympy(poly.as_expr().subs(substitution)) == FIELD.zero
                        for poly in (a, b)), "point not exactly stationary")
            values = [FIELD.from_sympy(poly.as_expr().subs(substitution))
                      for poly in self.cardinals]
            node = values.count(FIELD.one) == 1 and values.count(FIELD.zero) == 20
            regular = any(value == FIELD.zero and any(
                FIELD.from_sympy(poly.diff(var).as_expr().subs(substitution)) != FIELD.zero
                for var in (x, y)) for value, poly in zip(values, self.cardinals))
            require(node or regular, "point is neither exact node nor regular cardinal zero")
            ubounds, ubox = parse_rectangle(record["U"])
            require(contains_rational(ubounds, bounds), "U does not contain leaf")
            require(all(low <= Fraction(z.lo, UNIT) and Fraction(z.hi, UNIT) <= high
                        for (low, high), (_, z) in zip(ubounds, point)),
                    "U does not enclose exact point")
            _, c = parse_matrix(record["C"])
            self.injection(mask, c, ubox)
        elif code == "root":
            require(record["id"] in self.roots, "unknown root reference")
            root = self.roots[record["id"]]
            require(root["mask"] == mask, "root mask mismatch")
            ubounds, ubox = parse_rectangle(record["U"])
            require(contains_rational(ubounds, bounds) and
                    contains_rational(ubounds, root["bounds"]), "root U containment failed")
            self.injection(mask, root["C"], ubox)
        else:
            raise Rejected("unknown or unresolved disposition: " + str(code))
        self.dispositions[code] += 1
        self.patterns += 1

    def leaf(self, leaf):
        bounds, box = path_rectangle(leaf["path"])
        if "node_cone" in leaf:
            require("patterns" not in leaf, "node-cone leaf also contains ordinary patterns")
            identifier = leaf["node_cone"]
            require(type(identifier) is int and identifier in self.node_cones,
                    "node leaf references a missing, zero-gap, or unaccepted cone")
            require(all(a < c and d < b for (a, b), (c, d) in
                        zip(self.node_cones[identifier], bounds)),
                    "whole node leaf is not strictly inside its verified cone")
            self.node_leaves += 1
            self.dispositions["node_cone"] += 1
            return
        cardinal_bounds = [centered(t, dx, dy, box)
                           for t, dx, dy in zip(self.lterms, self.ldx, self.ldy)]
        fixed_positive = sum((1 << i) for i, z in enumerate(cardinal_bounds) if z.lo > 0)
        ambiguous = [i for i, z in enumerate(cardinal_bounds) if z.lo <= 0 <= z.hi]
        expected = sorted(fixed_positive | sum((1 << bit) for k, bit in enumerate(ambiguous)
                                               if variation & (1 << k))
                          for variation in range(1 << len(ambiguous)))
        records = leaf["patterns"]
        require(len(records) == len(expected) and
                (self.implicit_masks or all("mask" in record for record in records)) and
                all(record.get("mask", mask) == mask for mask, record in zip(expected, records)),
                "compatible sign patterns missing, duplicated, reordered, or extraneous at "
                + leaf["path"])
        for mask, record in zip(expected, records):
            self.disposition(mask, record, bounds, box)

    def boundaries(self, edges, corners):
        require([(edge["axis"], edge["side"]) for edge in edges] ==
                [(0, -1), (0, 1), (1, -1), (1, 1)], "incomplete or reordered edges")
        edge_roots, corner_roots = [], []
        edge_dispositions = Counter()
        total_edge_patterns = 0
        for edge in edges:
            axis, side = edge["axis"], edge["side"]
            fixed, variable = (x, y) if axis == 0 else (y, x)
            restricted = tuple(sp.Poly(p.as_expr().subs(fixed, side), variable, domain=FIELD)
                               for p in self.cardinals)
            require(all(not p.is_zero for p in restricted), "identically zero edge cardinal")
            product = sp.Poly(1, variable, domain=FIELD)
            simple_cover = sp.Poly(1, variable, domain=FIELD)
            for p in restricted:
                product *= p
                for factor, multiplicity in p.sqf_list()[1]:
                    if multiplicity == 1:
                        simple_cover *= factor
            arrangement = product.sqf_part()
            require(simple_cover.rem(arrangement).is_zero,
                    "edge crease without a proved regular cardinal zero")
            arrangement_intervals = verify_root_partition(
                rational_norm(arrangement), edge["E_norm_intervals"])
            samples = tuple(map(rational, edge["samples"]))
            require(len(samples) == len(arrangement_intervals) + 1,
                    "edge gap sample count")
            if arrangement_intervals:
                require(samples[0] < arrangement_intervals[0][0] and
                        arrangement_intervals[-1][1] < samples[-1], "missing exterior gap sample")
                require(all(arrangement_intervals[k][1] < samples[k + 1] <
                            arrangement_intervals[k + 1][0]
                            for k in range(len(arrangement_intervals) - 1)),
                        "sample not strictly between norm-root intervals")
            masks = set()
            for sample in samples:
                q = sp.Rational(sample.numerator, sample.denominator)
                signs = [exact_field_sign(p.eval(q)) for p in restricted]
                require(all(signs), "sample is an edge crease")
                masks.add(sum(1 << i for i, sign in enumerate(signs) if sign > 0))
            masks = sorted(masks)
            require(edge["sample_masks"] == masks and
                    [record["mask"] for record in edge["patterns"]] == masks,
                    "edge sign-pattern coverage mismatch")
            total_edge_patterns += len(masks)

            def lift_terms(poly):
                return polynomial_terms(sp.Poly(poly.as_expr(), x, y, domain=FIELD))

            restricted_terms = tuple(map(lift_terms, restricted))

            def edge_box(interval):
                tangent = Interval.bounds(*interval)
                fixed_interval = Interval.point(side)
                return ((fixed_interval, tangent) if axis == 0 else
                        (tangent, fixed_interval))

            def evaluate_on(terms, interval):
                return evaluate(terms, edge_box(interval))

            accepted_here = []
            for row in edge["patterns"]:
                mask = row["mask"]
                signed = lambda i: 1 if mask & (1 << i) else -1
                q = sum(signed(i) * p for i, p in enumerate(restricted))
                derivative = q.diff()
                if derivative.is_zero:
                    require(row["kind"] == "flat", "constant edge polynomial not flat")
                    self.edge_flat_values.append(q.eval(0))
                    edge_dispositions["flat"] += 1
                    continue
                require(row["kind"] == "roots", "nonconstant edge polynomial missing roots")
                squarefree = derivative.sqf_part()
                reduced = squarefree.exquo(sp.gcd(squarefree, arrangement))
                root_intervals = verify_root_partition(
                    rational_norm(reduced), row["Dr_norm_intervals"])
                require(len(row["points"]) == len(root_intervals) and
                        [point["i"] for point in row["points"]] == list(range(len(root_intervals))),
                        "edge derivative root dispositions incomplete")
                dt = lift_terms(derivative)
                ddt = lift_terms(derivative.diff())
                reduced_terms = lift_terms(reduced)
                for interval, point in zip(root_intervals, row["points"]):
                    code = point["code"]
                    if code == "outside":
                        require(interval[1] <= -1 or interval[0] >= 1,
                                "edge outside witness intersects open edge")
                    elif code == "derivative":
                        require(evaluate_on(reduced_terms, interval).nonzero(),
                                "wrong-embedding derivative witness failed")
                    elif code == "sign":
                        index = point["b"]
                        require(isinstance(index, int) and 0 <= index < 21 and
                                evaluate_on(restricted_terms[index], interval).
                                scaled_sign(signed(index)).hi < 0, "false edge sign exclusion")
                    elif code == "minimum":
                        require(evaluate_on(ddt, interval).lo > 0,
                                "edge positive-curvature witness not strict")
                    elif code in ("root", "normal"):
                        u = tuple(map(rational, point["interval"]))
                        require(len(u) == 2 and -1 < u[0] < u[1] < 1 and
                                u[0] <= interval[0] <= interval[1] <= u[1],
                                "edge U does not contain candidate inside open edge")
                        require(all(evaluate_on(terms, u).scaled_sign(signed(i)).lo > 0
                                    for i, terms in enumerate(restricted_terms)),
                                "edge maximum signs not strict")
                        require(evaluate_on(ddt, u).hi < 0 and
                                evaluate_on(dt, (u[0], u[0])).lo > 0 and
                                evaluate_on(dt, (u[1], u[1])).hi < 0,
                                "edge simple tangent maximum not proved")
                        normal = sum(signed(i) * -side * cardinal.diff(fixed)
                                     for i, cardinal in enumerate(self.cardinals))
                        normal_bound = evaluate(polynomial_terms(normal), edge_box(u))
                        if code == "normal":
                            require(normal_bound.lo > 0, "edge inward ascent not proved")
                        else:
                            require(normal_bound.hi < 0, "edge inward descent not proved")
                            require(point["id"] == len(edge_roots), "edge root id not canonical/unique")
                            require(all(u[1] < other[0] or other[1] < u[0]
                                        for other in accepted_here), "overlapping edge root intervals")
                            accepted_here.append(u)
                            value = evaluate_on(lift_terms(q), u)
                            edge_roots.append({"id": point["id"], "axis": axis, "side": side,
                                               "mask": mask, "interval": list(map(str, u)),
                                               "value": [str(Fraction(value.lo, UNIT)),
                                                         str(Fraction(value.hi, UNIT))]})
                    else:
                        raise Rejected("unknown/unresolved edge disposition: " + str(code))
                    edge_dispositions[code] += 1

        expected_corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        require([tuple(row["point"]) for row in corners] == expected_corners,
                "incomplete or reordered corners")
        corner_active_patterns = 0
        for row in corners:
            u, v = row["point"]
            substitution = {x: u, y: v}
            values = [FIELD.from_sympy(p.as_expr().subs(substitution)) for p in self.cardinals]
            if row["kind"] == "node":
                require(values.count(FIELD.one) == 1 and values.count(FIELD.zero) == 20,
                        "false node corner")
                continue
            require(row["kind"] == "max", "unresolved/unknown corner kind")
            zeros = [i for i, value in enumerate(values) if value == FIELD.zero]
            require(row["zeros"] == zeros and row["id"] == len(corner_roots),
                    "corner zero coverage or id mismatch")
            base = sum(1 << i for i, value in enumerate(values)
                       if exact_field_sign(FIELD.to_sympy(value)) > 0)
            for variation in range(1 << len(zeros)):
                mask = base | sum(1 << bit for k, bit in enumerate(zeros)
                                  if variation & (1 << k))
                # Exact algebraic signs; all active zero-cardinal choices occur.
                polys, _ = self.exact_pattern(mask)
                require(exact_field_sign(-u * polys[1].as_expr().subs(substitution)) < 0 and
                        exact_field_sign(-v * polys[2].as_expr().subs(substitution)) < 0,
                        "corner all-active inward derivative not strictly negative")
                corner_active_patterns += 1
            value = field_interval(basis_coefficients(sum(
                exact_field_sign(FIELD.to_sympy(value)) * FIELD.to_sympy(value)
                for value in values)))
            corner_roots.append({"id": row["id"], "point": row["point"],
                                 "value": [str(Fraction(value.lo, UNIT)),
                                           str(Fraction(value.hi, UNIT))]})
        return {"verified_edge_maxima_enclosures": len(edge_roots),
                "verified_corner_maxima": len(corner_roots),
                "verified_edge_patterns": total_edge_patterns,
                "edge_dispositions": dict(sorted(edge_dispositions.items())),
                "corner_active_patterns": corner_active_patterns,
                "edge_roots": edge_roots, "corner_roots": corner_roots}

    def run(self, certificate, allow_partial=False):
        require(certificate.get("format") == "a5-n5-spatial-v1", "unknown format")
        require(certificate.get("n") == 5 and certificate.get("precision") == PRECISION,
                "wrong degree/precision")
        require(certificate.get("pattern_order") == "compatible-mask",
                "unknown pattern ordering")
        self.implicit_masks = certificate.get("pattern_order") == "compatible-mask"
        node_result = self.node_certificates(certificate["node_cones"])
        leaves = certificate["leaves"]
        for leaf in leaves:
            path_rectangle(leaf["path"])
        complete_partition = partition([leaf["path"] for leaf in leaves])
        require(allow_partial or complete_partition, "incomplete square leaf partition")
        for root in certificate["interior_roots"]:
            self.root(root)
        for number, leaf in enumerate(leaves, 1):
            try:
                self.leaf(leaf)
            except Rejected as error:
                raise Rejected("leaf " + leaf["path"] + ": " + str(error)) from error
            if number % 1000 == 0:
                print(json.dumps({"verified_leaves": number, "verified_patterns": self.patterns}),
                      flush=True)
        no_unresolved = not certificate.get("unresolved") and not certificate.get("pending_paths")
        interior_complete = complete_partition and no_unresolved
        boundary_result = {}
        boundary_complete = "edges" in certificate and "corners" in certificate
        if boundary_complete:
            boundary_result = self.boundaries(certificate["edges"], certificate["corners"])
        complete = interior_complete and boundary_complete
        summary = certificate["summary"]
        require(summary.get("node_leaves") == self.node_leaves, "node-leaf summary mismatch")
        if "mask_checks" in summary:
            require(summary["mask_checks"] == self.patterns, "ordinary-mask summary mismatch")
        require(summary.get("interior") == len(self.roots), "interior summary count mismatch")
        if "leaf_pattern_records" in summary:
            require(summary["leaf_pattern_records"] == self.patterns and
                    summary.get("leaf_counts") == dict(self.dispositions),
                    "actual leaf-record summary mismatch")
        if complete:
            expected_summary = {"interior": len(self.roots),
                                "edge": boundary_result["verified_edge_maxima_enclosures"],
                                "corner": boundary_result["verified_corner_maxima"]}
            expected_summary["total"] = sum(expected_summary.values())
            require(all(summary.get(key) == value for key, value in expected_summary.items())
                    and summary.get("complete") is True and
                    summary.get("interior_complete") is True,
                    "complete count summary mismatch")
            require(summary.get("leaf_pattern_records") == self.patterns and
                    summary.get("leaf_counts") == dict(self.dispositions),
                    "missing final actual leaf-record counts")
            boundary_summary = certificate["boundary_summary"]
            require(boundary_summary.get("complete") is True and
                    boundary_summary.get("unresolved") == 0 and
                    boundary_summary.get("edge") == expected_summary["edge"] and
                    boundary_summary.get("corner") == expected_summary["corner"] and
                    boundary_summary.get("counts") == boundary_result["edge_dispositions"],
                    "boundary summary mismatch")
        require(allow_partial or complete,
                "incomplete certificate: partition, unresolved regions, or boundary obligations")
        return {"accepted": complete, "verified_supplied_witnesses": True,
                "interior_complete": interior_complete, "boundary_complete": boundary_complete,
                "complete_prefix_partition": complete_partition,
                "verified_leaves": len(leaves), "verified_patterns": self.patterns,
                "dispositions": dict(sorted(self.dispositions.items())),
                "verified_interior_maxima_enclosures": len(self.roots),
                "root_values": {str(key): value["value"] for key, value in self.roots.items()},
                "count_certified": complete,
                "total_maxima": (len(self.roots) + boundary_result.get("verified_edge_maxima_enclosures", 0)
                                  + boundary_result.get("verified_corner_maxima", 0)) if complete else None,
                "verified_node_leaves": self.node_leaves, **node_result,
                **boundary_result}

    def global_values(self, certificate, global_certificate, certificate_sha256, count_result):
        """Additional value evidence excludes non-strict global plateaus."""
        require(count_result["count_certified"], "global proof requires complete count coverage")
        require(global_certificate.get("format") == "a5-n5-global-v1" and
                global_certificate.get("complete") is True and
                global_certificate.get("certificate_sha256") == certificate_sha256,
                "global format/completeness/count-certificate binding failed")
        require(global_certificate.get("bounded_codes") == ["flat", "factor"],
                "global exceptional disposition coverage changed")
        cut = rational(global_certificate["cut"])
        require(cut == Fraction(19, 4) and rational(global_certificate["node_value"]) == 1,
                "global cut or exact node value changed")
        upper = rational(global_certificate["exception_upper"])
        require(upper < cut and global_certificate["exception_leaf_occurrences"] ==
                len(self.exception_occurrences), "global flat/factor occurrence count or cut failed")
        observed = None
        for mask, box in self.exception_occurrences:
            own = Fraction(evaluate(self.terms_for(mask), box).hi, UNIT)
            require(own <= upper, "global exceptional flat/factor value bound failed")
            observed = own if observed is None else max(observed, own)
        require(global_certificate["edge_flat_patterns"] == len(self.edge_flat_values) and
                all(native(value) in (FIELD.one, -FIELD.one) for value in self.edge_flat_values),
                "constant edge restrictions are not all exactly plus/minus one")

        def verify_values(provided, recomputed, name):
            require(isinstance(provided, list) and [row["id"] for row in provided] ==
                    [row["id"] for row in recomputed], name+" global value IDs incomplete or reordered")
            for row, own in zip(provided, recomputed):
                supplied = tuple(map(rational, row["enclosure"]))
                bounds = tuple(map(rational, own["value"]))
                require(len(supplied) == 2 and supplied[0] <= bounds[0] <= bounds[1] <= supplied[1] < cut,
                        name+" global value enclosure or strict cut failed")

        verify_values(global_certificate["interior_values"],
                      [{"id": key, "value": root["value"]} for key, root in self.roots.items()],
                      "interior")
        verify_values(global_certificate["edge_values"], count_result["edge_roots"], "edge")
        corner_expression, corner_bound = parse_field(global_certificate["corner_value"])
        require(Fraction(corner_bound.lo, UNIT) > cut, "corner value is not strictly above global cut")
        points = []
        for row in certificate["corners"]:
            if row["kind"] != "max":
                continue
            substitution = dict(zip((x, y), row["point"]))
            values = [native(p.as_expr().subs(substitution)) for p in self.cardinals]
            actual = sum((exact_field_sign(value)*value for value in values), FIELD.zero)
            require(actual == native(corner_expression), "exact common nonnode corner value failed")
            points.append(row["point"])
        require(points == [[-1, -1], [-1, 1]], "global nonnode-corner locations changed")
        return {"global_argmax_verified": True, "global_argmax": points,
                "global_maximum_exact": global_certificate["corner_value"], "global_cut": str(cut),
                "exception_occurrences_bounded": len(self.exception_occurrences),
                "observed_exception_upper": str(observed),
                "node_leaf_global_exclusion_verified": True,
                "global_no_nonstrict_plateau_above_cut": True}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON object key")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    parser.add_argument("--allow-partial", action="store_true")
    parser.add_argument("--nodes-only", action="store_true",
                        help="verify local node witnesses only; never certify a maxima count")
    parser.add_argument("--global-file")
    arguments = parser.parse_args()
    start = time.monotonic()
    certificate_path = Path(arguments.certificate)
    raw = certificate_path.read_bytes()
    decompressed = gzip.decompress(raw) if certificate_path.suffix == ".gz" else raw
    result = {"certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "certificate_bytes": len(raw),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "python": platform.python_version(), "sympy": sp.__version__,
              "precision": PRECISION,
              "trusted_dependencies": ["CPython integers/Fraction", "SymPy exact field, linear and polynomial algebra"]}
    try:
        certificate = json.loads(decompressed, object_pairs_hook=unique_object)
        verifier = Verifier()
        if arguments.nodes_only:
            require(certificate.get("format") == "a5-n5-nodes-v1" and
                    certificate.get("n") == 5 and certificate.get("precision") == PRECISION,
                    "unknown local node-certificate format")
            result.update(verifier.node_certificates(certificate["nodes"]))
            result.update({"accepted": False, "count_certified": False,
                           "verified_supplied_node_witnesses": True,
                           "scope": "local exact node predicates only; no maxima count"})
        else:
            result.update(verifier.run(certificate, arguments.allow_partial))
        if arguments.global_file:
            require(not arguments.nodes_only, "local node replay cannot certify a global maximum")
            global_raw = Path(arguments.global_file).read_bytes()
            global_data = json.loads(global_raw, object_pairs_hook=unique_object)
            result.update(verifier.global_values(certificate, global_data,
                                                 result["certificate_sha256"], result))
            result["global_certificate_sha256"] = hashlib.sha256(global_raw).hexdigest()
        exit_code = 0
    except (Rejected, KeyError, ValueError, TypeError) as error:
        result.update({"accepted": False, "count_certified": False, "error": str(error)})
        exit_code = 1
    result["seconds"] = time.monotonic() - start
    Path(arguments.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True), flush=True)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
