#!/usr/bin/env python3
"""Independent, certificate-driven verifier for the degree-three A5 reduction.

No producer imports, numerical roots, root isolation, subdivision, or search.
Supplied root partitions are checked by exact Sturm counts; every supplied
Cartesian pair must have a verified disposition. See a5_schema.md.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import sympy as s

x, y = s.symbols("x y")
r2 = s.sqrt(2)
FIELD = s.QQ.algebraic_field(r2)


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def frac(value):
    require(isinstance(value, str), "rationals must be strings")
    return F(value)


def symq(value):
    value = F(value)
    return s.Rational(value.numerator, value.denominator)


def rat(value):
    return F(int(value.p), int(value.q))


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        require(self.lo <= self.hi, "reversed interval")

    @staticmethod
    def point(q):
        return I(F(q), F(q))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -as_i(other)

    def __rsub__(self, other):
        return as_i(other) + -self

    def __mul__(self, other):
        other = as_i(other)
        values = (self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi)
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __pow__(self, degree):
        require(isinstance(degree, int) and degree >= 0, "bad interval power")
        if degree == 0:
            return I.point(1)
        if degree % 2:
            return I(self.lo ** degree, self.hi ** degree)
        a, b = self.lo ** degree, self.hi ** degree
        return I(F(0) if self.lo <= 0 <= self.hi else min(a, b), max(a, b))

    def contains(self, other):
        other = as_i(other)
        return self.lo <= other.lo and other.hi <= self.hi

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def excludes_zero(self):
        return self.lo > 0 or self.hi < 0

    def json(self):
        return [str(self.lo), str(self.hi)]


def as_i(value):
    return value if isinstance(value, I) else I.point(value)


# A checked rational enclosure. Its endpoints are never read from a certificate.
SQRT2 = I(F(14142135623730950488016887242096980785696718753769, 10**49),
          F(14142135623730950488016887242096980785696718753770, 10**49))
require(SQRT2.lo > 0 and SQRT2.lo**2 < 2 < SQRT2.hi**2,
        "invalid built-in sqrt(2) bracket")


def field_parts(expr):
    expr = s.expand(FIELD.to_sympy(FIELD.from_sympy(expr)))
    b = s.expand(expr).coeff(r2)
    a = s.expand(expr - b * r2)
    require(a.is_Rational and b.is_Rational, "not in Q(sqrt(2))")
    return rat(a), rat(b)


def qsign(expr):
    a, b = field_parts(expr)
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    # sqrt(2) is irrational, so the nontrivial comparison cannot be equality.
    if a > 0:
        return 1 if a*a > 2*b*b else -1
    return 1 if 2*b*b > a*a else -1


def field_value(data):
    require(isinstance(data, list) and len(data) == 2, "bad field scalar")
    return symq(frac(data[0])) + symq(frac(data[1])) * r2


def poly(expr):
    return s.Poly(expr, x, y, domain=FIELD)


def decode_poly(data):
    require(isinstance(data, list), "bad polynomial encoding")
    terms = {}
    for term in data:
        require(isinstance(term, list) and len(term) == 4, "bad polynomial term")
        i, j, a, b = term
        require(type(i) is int and type(j) is int and i >= 0 and j >= 0,
                "bad polynomial exponent")
        require((i, j) not in terms, "duplicate polynomial monomial")
        c = symq(frac(a)) + symq(frac(b)) * r2
        require(c != 0, "zero encoded polynomial term")
        terms[i, j] = c
    return poly(sum(c*x**i*y**j for (i, j), c in terms.items()))


def interval(data):
    require(isinstance(data, list) and len(data) == 2, "bad interval encoding")
    return I(frac(data[0]), frac(data[1]))


def box(data):
    require(isinstance(data, list) and len(data) == 2, "bad box encoding")
    return (interval(data[0]), interval(data[1]))


def exact_point(data):
    require(isinstance(data, list) and len(data) == 2, "bad point encoding")
    return tuple(field_value(c) for c in data)


def point_in(point, domain):
    return all(qsign(t - symq(v.lo)) >= 0 and
               qsign(symq(v.hi) - t) >= 0 for t, v in zip(point, domain))


class Encloser:
    """Exact, inclusion-preserving monomial interval evaluation."""
    def __init__(self):
        self.cache = {}

    def terms(self, p):
        if p not in self.cache:
            self.cache[p] = [(ij, I.point(a) + b * SQRT2)
                             for ij, c in p.terms()
                             for a, b in [field_parts(c)]]
        return self.cache[p]

    def __call__(self, p, domain):
        u, v = domain
        return sum((c*(u**i)*(v**j) for (i, j), c in self.terms(p)), I.point(0))


def reconstruct():
    # Independent monomial Vandermonde, with explicitly exact Chebyshev nodes.
    xs = [s.Integer(1), s.Rational(1, 2), s.Rational(-1, 2), s.Integer(-1)]
    ys = [s.Integer(1), r2/2, s.Integer(0), -r2/2, s.Integer(-1)]
    nodes = [(xs[j], ys[k]) for j in range(4) for k in range(5) if (j+k) % 2 == 0]
    monomials = [x**i*y**(d-i) for d in range(4) for i in range(d, -1, -1)]
    V = s.Matrix([[m.subs({x: a, y: b}) for m in monomials] for a, b in nodes])
    inverse = V.inv()
    require(V*inverse == s.eye(10), "Vandermonde inverse identity failed")
    cardinals = [poly(sum(m*inverse[i, j] for i, m in enumerate(monomials)))
                 for j in range(10)]
    require(sum(cardinals, poly(0)) == poly(1), "partition of unity failed")
    return cardinals


def qq_norm_resultant(a, b, eliminated, retained):
    result = s.Poly(s.resultant(a.as_expr(), b.as_expr(), eliminated,
                               domain=FIELD.poly_ring(retained)),
                    retained, domain=FIELD)
    require(not result.is_zero, "zero residual resultant")
    conjugate = 0
    for (i,), c in result.terms():
        u, v = field_parts(c)
        conjugate += (symq(u) - symq(v)*r2) * retained**i
    norm = s.Poly(s.expand(result.as_expr()*conjugate), retained, domain=s.QQ)
    require(not norm.is_zero, "zero resultant norm")
    return norm.sqf_part().monic()


def variations(values):
    signs = [1 if v > 0 else -1 for v in values if v != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def check_roots(p, supplied):
    require(isinstance(supplied, list), "root partition must be a list")
    sturm = p.sturm() if p.degree() else [p]

    def variation_at(q):
        return variations([term.eval(symq(q)) for term in sturm])

    at_minus_inf = variations([term.LC()*(-1)**term.degree() for term in sturm])
    at_plus_inf = variations([term.LC() for term in sturm])
    total = at_minus_inf - at_plus_inf
    roots = [interval(entry) for entry in supplied]
    for k, item in enumerate(roots):
        if k:
            require(roots[k-1].hi <= item.lo, "root intervals out of order or overlap")
            if roots[k-1].hi == item.lo:
                require(p.eval(symq(item.lo)) != 0, "duplicate root on touching intervals")
        if item.lo == item.hi:
            require(p.eval(symq(item.lo)) == 0, "singleton is not an exact root")
        else:
            require(p.eval(symq(item.lo)) != 0 and p.eval(symq(item.hi)) != 0,
                    "nonsingleton interval has a root endpoint")
            require(variation_at(item.lo) - variation_at(item.hi) == 1,
                    "supplied interval does not contain exactly one root")
    require(len(roots) == total, "root partition omits or adds a real root")
    return roots


def hessian(p):
    xx, xy, yy = p.diff((x, 2)), p.diff(x).diff(y), p.diff((y, 2))
    return xx, xy, yy, xx*yy - xy*xy


def matrix(data):
    require(isinstance(data, list) and len(data) == 2 and
            all(isinstance(row, list) and len(row) == 2 for row in data),
            "bad preconditioner")
    C = [[frac(q) for q in row] for row in data]
    require(C[0][0]*C[1][1] - C[0][1]*C[1][0] != 0, "singular preconditioner")
    return C


def contraction(H, domain, C, enclose):
    xx, xy, yy, _ = H
    J = [[enclose(xx, domain), enclose(xy, domain)],
         [enclose(xy, domain), enclose(yy, domain)]]
    R = [[I.point(int(i == j)) - sum((C[i][k]*J[k][j] for k in range(2)), I.point(0))
          for j in range(2)] for i in range(2)]
    require(max(sum(entry.abs_upper() for entry in row) for row in R) < 1,
            "gradient injectivity/contraction bound failed")
    return R


def krawczyk(A, B, H, domain, C, enclose):
    require(all(v.lo < v.hi for v in domain), "Krawczyk box has zero width")
    centre = [I.point((v.lo + v.hi)/2) for v in domain]
    value = [enclose(A, centre), enclose(B, centre)]
    R = contraction(H, domain, C, enclose)
    displacement = [v - c for v, c in zip(domain, centre)]
    for i in range(2):
        image = centre[i] - sum((C[i][k]*value[k] for k in range(2)), I.point(0))
        image += sum((R[i][k]*displacement[k] for k in range(2)), I.point(0))
        require(domain[i].lo < image.lo and image.hi < domain[i].hi,
                "Krawczyk image is not strictly inside supplied box")


def evaluate_exact(p, point):
    return s.expand(p.as_expr().subs({x: point[0], y: point[1]}))


def disjoint(a, b):
    return any(u.hi < v.lo or v.hi < u.lo for u, v in zip(a, b))


def restrict(p, axis, side):
    """Keep a univariate restriction encoded as a bivariate polynomial."""
    return poly(p.as_expr().subs((x, y)[axis], side))


def edge_domain(axis, side, tangent):
    return (I.point(side), tangent) if axis == 0 else (tangent, I.point(side))


def univariate_norm(p, retained):
    pp = s.Poly(p.as_expr(), retained, domain=FIELD)
    require(not pp.is_zero, "zero polynomial has no finite root partition")
    conjugate = 0
    for (i,), c in pp.terms():
        a, b = field_parts(c)
        conjugate += (symq(a)-symq(b)*r2)*retained**i
    return s.Poly(s.expand(pp.as_expr()*conjugate), retained, domain=s.QQ).sqf_part().monic()


def edge_fullmask(cards, restricted, zero_indices, mask, axis, side, tangent, enclose):
    derived = mask
    normal_factor = poly((x, y)[axis] - side)
    domain = edge_domain(axis, side, tangent)
    for k, L in enumerate(restricted):
        if k not in zero_indices:
            sign = 1 if mask & (1 << k) else -1
            require((sign*enclose(L, domain)).lo > 0,
                    "edge cardinal signs are not strictly consistent")
        else:
            quotient, remainder = cards[k].div(normal_factor)
            require(remainder.is_zero, "false edge normal-factor identity")
            q = enclose(restrict(quotient, axis, side), domain)
            require(q.excludes_zero(), "edge factor quotient sign is unresolved")
            sign = -side * (1 if q.lo > 0 else -1)
            if sign > 0:
                derived |= 1 << k
            else:
                derived &= ~(1 << k)
    return derived


def check_edges(records, cards, enclose):
    expected = [(0, -1), (0, 1), (1, -1), (1, 1)]
    require(isinstance(records, list) and len(records) == 4, "all four edges required")
    maxima, counts = [], Counter()
    for edge, (axis, side) in zip(records, expected):
        require(edge.get("axis") == axis and edge.get("side") == side,
                "edge coverage missing, duplicated, or out of order")
        restricted = [restrict(L, axis, side) for L in cards]
        zeros = [k for k, L in enumerate(restricted) if L.is_zero]
        require(edge.get("zeros") == zeros, "incorrect identically-zero edge cardinal list")
        canonical_masks = [mask for mask in range(1024)
                           if not any(mask & (1 << k) for k in zeros)]
        patterns = edge["patterns"]
        require(isinstance(patterns, list) and len(patterns) == len(canonical_masks),
                "incomplete canonical edge sign-pattern coverage")
        tangent = (y, x)[axis]
        edge_maxima = []
        for record, mask in zip(patterns, canonical_masks):
            require(type(record.get("mask")) is int and record["mask"] == mask,
                    "edge canonical masks missing, duplicated, or out of order")
            signs = [1 if mask & (1 << k) else -1 for k in range(10)]
            q = sum((sign*L for sign, L in zip(signs, restricted)), poly(0))
            D, DD = q.diff(tangent), q.diff((tangent, 2))
            kind = record.get("kind")
            counts["pattern_" + str(kind)] += 1
            if kind == "flat":
                require(D.is_zero, "false constant edge-pattern claim")
                require(q.as_expr() in (s.Integer(-1), s.Integer(1)),
                        "constant edge polynomial is not its required nodal value +/-1")
                continue
            require(kind == "roots" and not D.is_zero, "bad edge-pattern kind")
            intervals = check_roots(univariate_norm(D, tangent), record["roots"])
            points = record["points"]
            require(isinstance(points, list) and len(points) == len(intervals),
                    "edge root dispositions are incomplete")
            for k, (item, projected) in enumerate(zip(points, intervals)):
                require(type(item.get("i")) is int and item["i"] == k,
                        "edge root dispositions missing, duplicated, or out of order")
                Q = edge_domain(axis, side, projected)
                code = item.get("code")
                counts["point_" + str(code)] += 1
                if code == "outside":
                    require(projected.hi <= -1 or projected.lo >= 1, "false edge outside claim")
                elif code == "derivative":
                    require(enclose(D, Q).excludes_zero(), "false edge derivative exclusion")
                elif code == "hessian":
                    require(enclose(DD, Q).lo >= 0, "false edge second-derivative exclusion")
                elif code == "sign":
                    b = item["b"]
                    require(type(b) is int and 0 <= b < 10 and b not in zeros,
                            "bad edge sign-exclusion cardinal")
                    require((signs[b]*enclose(restricted[b], Q)).hi < 0,
                            "false edge sign exclusion")
                elif code == "regular":
                    t = field_value(item["point"])
                    point = (symq(side), t) if axis == 0 else (t, symq(side))
                    require(point_in(point, Q), "exact edge crease point is outside interval")
                    require(evaluate_exact(D, point) == 0, "exact edge crease point not stationary")
                    require(any(not L.is_zero and evaluate_exact(L, point) == 0 and
                                evaluate_exact(L.diff(tangent), point) != 0
                                for L in restricted), "no regular tangent crease at exact edge point")
                    require(enclose(DD, Q).excludes_zero(), "edge stationary-root uniqueness unresolved")
                elif code in ("root", "normal"):
                    larger = interval(item["interval"])
                    require(larger.lo < larger.hi and larger.contains(projected),
                            "edge root interval has zero width or fails to cover projection")
                    require(-1 < larger.lo and larger.hi < 1, "edge root interval crosses a corner")
                    larger_domain = edge_domain(axis, side, larger)
                    fullmask = edge_fullmask(cards, restricted, zeros, mask, axis,
                                             side, larger, enclose)
                    require(type(item.get("fullmask")) is int and item["fullmask"] == fullmask,
                            "incorrect one-sided full sign mask")
                    Pfull = sum(((1 if fullmask & (1 << b) else -1)*L
                                 for b, L in enumerate(cards)), poly(0))
                    inward = -side * enclose(Pfull.diff((x, y)[axis]), larger_domain)
                    require(enclose(DD, larger_domain).hi < 0,
                            "edge root has no certified strict tangent concavity")
                    if "point" in item:
                        t = field_value(item["point"])
                        point = (symq(side), t) if axis == 0 else (t, symq(side))
                        require(point_in(point, Q) and evaluate_exact(D, point) == 0,
                                "supplied exact edge root is outside interval or not stationary")
                    else:
                        left_domain = edge_domain(axis, side, I.point(larger.lo))
                        right_domain = edge_domain(axis, side, I.point(larger.hi))
                        require(enclose(D, left_domain).lo > 0 and
                                enclose(D, right_domain).hi < 0,
                                "edge derivative has no certified endpoint sign change")
                    if code == "normal":
                        require(inward.lo > 0, "false positive-inward-derivative exclusion")
                        continue
                    require(inward.hi < 0, "edge inward derivative is not strictly negative")
                    require(type(item.get("id")) is int and item["id"] == len(maxima),
                            "edge maximum IDs must be contiguous in traversal order")
                    require(all(larger.hi < prev.lo or prev.hi < larger.lo for prev in edge_maxima),
                            "accepted root intervals on one edge overlap")
                    edge_maxima.append(larger)
                    maxima.append({"id": item["id"], "axis": axis, "side": side,
                                   "mask": mask, "fullmask": fullmask,
                                   "interval": larger.json(),
                                   "value": enclose(q, larger_domain).json()})
                else:
                    raise Invalid(f"unknown edge root disposition {code!r}")
        print(f"verified edge axis={axis} side={side}", file=sys.stderr, flush=True)
    return {"edge": len(maxima), "edge_patterns": dict(sorted(counts.items())),
            "edge_roots": maxima}


def check_corners(records, cards, enclose):
    points = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    require(isinstance(records, list) and len(records) == 4, "all four corners required")
    maxima = []
    for record, point in zip(records, points):
        require(record.get("point") == list(point), "corner coverage missing or out of order")
        vals = [evaluate_exact(L, point) for L in cards]
        if record.get("kind") == "node":
            require(sum(v == 1 for v in vals) == 1 and sum(v == 0 for v in vals) == 9,
                    "claimed node corner is not a cardinal node")
        else:
            require(record.get("kind") == "max", "unclassified corner")
            zeros = [i for i, v in enumerate(vals) if v == 0]
            require(record.get("zeros") == zeros, "incorrect zero-cardinal corner list")
            base = sum((1 << k) for k, v in enumerate(vals) if qsign(v) > 0)
            # Independently enumerate all active masks; the certificate cannot
            # suppress an outward failure by omitting an active sign pattern.
            for subset in range(1 << len(zeros)):
                mask = base | sum(1 << b for j, b in enumerate(zeros) if subset & (1 << j))
                P = sum(((1 if mask & (1 << b) else -1)*L
                         for b, L in enumerate(cards)), poly(0))
                require(all(qsign(-point[axis]*evaluate_exact(P.diff(variable), point)) < 0
                            for axis, variable in enumerate((x, y))),
                        "corner has an active polynomial without strict inward descent")
            require(type(record.get("id")) is int and record["id"] == len(maxima),
                    "corner maximum IDs must be contiguous in corner order")
            domain = tuple(I.point(q) for q in point)
            value = sum((qsign(v)*enclose(L, domain) for v, L in zip(vals, cards)), I.point(0))
            maxima.append({"id": record["id"], "point": list(point), "value": value.json()})
    return {"corner": len(maxima), "corner_roots": maxima}


def check_patterns(records, cards, enclose):
    require(isinstance(records, list) and len(records) == 1024,
            "all 1024 sign patterns are required")
    counts = Counter()
    roots = []
    for mask, record in enumerate(records):
        require(type(record.get("mask")) is int and record["mask"] == mask,
                "sign patterns missing, duplicated, or out of order")
        signs = [1 if mask & (1 << i) else -1 for i in range(10)]
        P = sum((sign*L for sign, L in zip(signs, cards)), poly(0))
        A, B = P.diff(x), P.diff(y)
        kind = record.get("kind")
        counts[kind] += 1
        if kind == "flat":
            require(A.is_zero or B.is_zero, f"mask {mask}: false flat claim")
            continue
        require(kind in ("unit", "residual"), f"mask {mask}: unknown kind")
        g = decode_poly(record["g"])
        require(not g.is_zero, f"mask {mask}: zero divisor")
        a, ra = A.div(g)
        b, rb = B.div(g)
        require(ra.is_zero and rb.is_zero, f"mask {mask}: false exact gradient division")
        if kind == "unit":
            require((not a.is_zero and a.total_degree() == 0) or
                    (not b.is_zero and b.total_degree() == 0),
                    f"mask {mask}: false unit residual claim")
            continue
        require(not A.is_zero and not B.is_zero, "residual with a zero gradient")
        xr = check_roots(qq_norm_resultant(a, b, y, x), record["xroots"])
        yr = check_roots(qq_norm_resultant(a, b, x, y), record["yroots"])
        pairs = record["pairs"]
        require(isinstance(pairs, list) and len(pairs) == len(xr)*len(yr),
                f"mask {mask}: incomplete Cartesian pair coverage")
        H = hessian(P)
        for position, pair in enumerate(pairs):
            i, j = divmod(position, len(yr))
            require(pair.get("ij") == [i, j], f"mask {mask}: wrong Cartesian pair index")
            Q = (xr[i], yr[j])
            code = pair.get("code")
            counts["pair_" + str(code)] += 1
            if code == "outside":
                require(any(v.hi <= -1 or v.lo >= 1 for v in Q), "false outside claim")
            elif code == "gradient":
                require(enclose(A, Q).excludes_zero() or enclose(B, Q).excludes_zero(),
                        "false gradient exclusion")
            elif code == "sign":
                k = pair["b"]
                require(type(k) is int and 0 <= k < 10, "bad cardinal index")
                require((signs[k]*enclose(cards[k], Q)).hi < 0, "false cardinal-sign exclusion")
            elif code == "hessian":
                require(enclose(H[0], Q).lo >= 0 or enclose(H[2], Q).lo >= 0 or
                        enclose(H[3], Q).hi <= 0, "false nonnegative-definite exclusion")
            elif code == "regular":
                point = exact_point(pair["point"])
                require(point_in(point, Q), "regular exact point is outside pair box")
                require(evaluate_exact(A, point) == 0 and evaluate_exact(B, point) == 0,
                        "regular exact point is not stationary")
                require(any(evaluate_exact(L, point) == 0 and
                            (evaluate_exact(L.diff(x), point) != 0 or
                             evaluate_exact(L.diff(y), point) != 0) for L in cards),
                        "no exact regular crease at stationary point")
                contraction(H, Q, matrix(pair["C"]), enclose)
            elif code == "root":
                big = box(pair["box"])
                require(all(v.lo < v.hi for v in big), "root box has zero width")
                require(all(v.contains(q) for v, q in zip(big, Q)), "root box does not cover pair box")
                require(all(-1 < v.lo and v.hi < 1 for v in big), "interior root box crosses boundary")
                C = matrix(pair["C"])
                if "point" in pair:
                    point = exact_point(pair["point"])
                    require(point_in(point, Q), "exact root is outside pair box")
                    require(evaluate_exact(A, point) == 0 and evaluate_exact(B, point) == 0,
                            "exact root is not stationary")
                    contraction(H, big, C, enclose)
                else:
                    krawczyk(A, B, H, big, C, enclose)
                require(enclose(H[0], big).hi < 0 and enclose(H[3], big).lo > 0,
                        "root Hessian is not certified negative definite")
                require(all((sign*enclose(L, big)).lo > 0 for sign, L in zip(signs, cards)),
                        "root cardinal signs are not strictly consistent")
                require(type(pair.get("id")) is int and pair["id"] >= 0, "bad root id")
                require(all(disjoint(big, previous["domain"]) for previous in roots),
                        "accepted interior root boxes are not pairwise disjoint")
                roots.append({"id": pair["id"], "mask": mask, "domain": big,
                              "box": [v.json() for v in big],
                              "value": enclose(P, big).json()})
            else:
                raise Invalid(f"mask {mask}: unknown pair disposition {code!r}")
        if mask % 128 == 127:
            print(f"verified patterns {mask+1}/1024", file=sys.stderr, flush=True)
    require(sorted(item["id"] for item in roots) == list(range(len(roots))),
            "interior root IDs must be unique and contiguous from zero")
    for item in roots:
        del item["domain"]
    return {"interior": len(roots), "patterns": dict(sorted(counts.items())),
            "interior_roots": sorted(roots, key=lambda item: item["id"])}


def signed_polynomial(cards, mask):
    return sum(((1 if mask & (1 << b) else -1)*L
                for b, L in enumerate(cards)), poly(0))


def check_global(data, result, cards, enclose):
    """Check the extra evidence needed to exclude non-strict global plateaus."""
    global_data = data["global"]
    flat_bound, cut = frac(global_data["flat_bound"]), frac(global_data["cut"])
    require(flat_bound == 3 and cut == F(15, 4), "incorrect global separation constants")
    flat_patterns = [record for record in data["patterns"] if record["kind"] == "flat"]
    for record in data["patterns"]:
        if record["kind"] != "flat":
            require(decode_poly(record["g"]).total_degree() == 0,
                    "global proof requires constant nonflat gradient factor")
    flat_records = global_data["flat"]
    require(isinstance(flat_records, list) and len(flat_records) == len(flat_patterns),
            "global flat-pattern bounds are incomplete")
    flat_upper = -F(10**100)
    for item, pattern in zip(flat_records, flat_patterns):
        require(type(item.get("mask")) is int and item["mask"] == pattern["mask"],
                "global flat masks missing, duplicated, or out of order")
        axis = item["axis"]
        require(type(axis) is int and axis in (0, 1), "invalid flat univariate axis")
        P = signed_polynomial(cards, item["mask"])
        require(P.diff((y, x)[axis]).is_zero, "flat bound uses the wrong coordinate")
        panels = item["panels"]
        require(isinstance(panels, list) and len(panels) == 32,
                "global flat bound needs all 32 supplied panels")
        previous = F(-1)
        for panel in panels:
            T = interval(panel["interval"])
            require(T.lo == previous and T.lo < T.hi and T.hi <= 1,
                    "flat panels do not form an ordered partition of [-1,1]")
            previous = T.hi
            domain = (T, I.point(0)) if axis == 0 else (I.point(0), T)
            supplied_upper = frac(panel["upper"])
            require(enclose(P, domain).hi <= supplied_upper < flat_bound,
                    "global flat-panel upper bound failed")
            flat_upper = max(flat_upper, supplied_upper)
        require(previous == 1, "flat panels omit the right endpoint")

    def value_rows(rows, accepted, name):
        require(isinstance(rows, list) and len(rows) == len(accepted),
                f"global {name} value rows incomplete")
        upper = -F(10**100)
        for row, root in zip(rows, accepted):
            require(type(row.get("id")) is int and row["id"] == root["id"],
                    f"global {name} IDs missing, duplicated, or out of order")
            value = interval(row["enclosure"])
            require(value.contains(interval(root["value"])) and value.hi < cut,
                    f"global {name} value enclosure failed")
            upper = max(upper, value.hi)
        return upper

    interior_upper = value_rows(global_data["interior_values"], result["interior_roots"], "interior")
    edge_upper = value_rows(global_data["edge_values"], result["edge_roots"], "edge")
    C = field_value(global_data["corner_value"])
    require(C == s.Rational(17, 6) + s.Rational(2, 3)*r2,
            "incorrect exact nonnode-corner value")
    C_interval = I.point(field_parts(C)[0]) + field_parts(C)[1]*SQRT2
    require(C_interval.lo > cut > flat_bound > 1, "global value separation failed")
    require(result["corner"] == 2, "global corner certificate needs both nonnode corners")
    for corner in result["corner_roots"]:
        vals = [evaluate_exact(L, corner["point"]) for L in cards]
        actual = s.expand(sum(qsign(v)*v for v in vals))
        require(actual == C, "exact corner value identity failed")

    representatives = global_data["part1_representatives"]
    require(representatives == [{"edge_id": 2, "sigma": 1}, {"edge_id": 3, "sigma": -1}],
            "part-1 representative map incomplete or altered")
    for item in representatives:
        root = result["edge_roots"][item["edge_id"]]
        require(root["axis"] == 0 and root["side"] == 1,
                "part-1 representative is not on the edge x=1")
        T = interval(root["interval"])
        require((T.lo > 0 if item["sigma"] == 1 else T.hi < 0),
                "part-1 representative has the wrong exact root sign")
        q = restrict(signed_polynomial(cards, root["fullmask"]), 0, 1)
        quotient, remainder = q.diff(y).div(poly(1 - 3*y*y))
        require(remainder.is_zero and not quotient.is_zero and quotient.total_degree() == 0,
                "part-1 tangent root is not exactly sigma/sqrt(3)")
    return {"global_maximum": {"points": [root["point"] for root in result["corner_roots"]],
                               "value_exact": ["17/6", "2/3"],
                               "value_interval": C_interval.json(),
                               "flat_upper": str(flat_upper),
                               "interior_upper": str(interior_upper),
                               "edge_upper": str(edge_upper),
                               "strict_separation_cut": str(cut),
                               "part1_representatives_verified": True}}


def check_certificate(data, interior_only=False):
    require(isinstance(data, dict), "certificate is not an object")
    require(data.get("format") == "a5-n3-v1" and data.get("n") == 3,
            "only a5-n3-v1 degree three is supported")
    cards = reconstruct()
    enclose = Encloser()
    result = check_patterns(data["patterns"], cards, enclose)
    if interior_only:
        result["scope"] = "interior only; closed-square count NOT verified"
        return result
    result.update(check_edges(data["edges"], cards, enclose))
    result.update(check_corners(data["corners"], cards, enclose))
    result["total"] = result["interior"] + result["edge"] + result["corner"]
    result["scope"] = "strict local maxima on the closed square at degree three"
    if "global" in data:
        result.update(check_global(data, result, cards, enclose))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--interior-only", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    raw = args.certificate.read_bytes()
    payload = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    try:
        data = json.loads(payload)
        result = check_certificate(data, args.interior_only)
    except (Invalid, KeyError, ValueError, TypeError, ZeroDivisionError) as error:
        print(json.dumps({"verified": False, "error": str(error)}, indent=2))
        return 1
    result.update({"verified": True, "certificate_sha256": hashlib.sha256(raw).hexdigest(),
                   "certificate_bytes": len(raw),
                   "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   "python": platform.python_version(), "sympy": s.__version__,
                   "elapsed_seconds": round(time.monotonic()-started, 3)})
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
