"""All-degree rigorous cardinal enclosures from the proved PD-T101 kernel.

Rational Machin/Taylor bounds replace algebraic-field construction. This
new module leaves the separately frozen n8 field certificate untouched.
Every interval operation is outward-rounded integer arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import finite_bernstein as b

PRECISION = 192
S = 1 << PRECISION
DEPENDENCY = (b.REPO / "topics/padua-proof-attempts-20261101/theory/"
              "proof-attempts-codex-01-padua-corner.md")


def rat(q):
    q = F(q)*S
    return q.numerator//q.denominator, b.ceil(q)


def add(a, c):
    return a[0]+c[0], a[1]+c[1]


def scale(a, k):
    return (a[0]*k, a[1]*k) if k >= 0 else (a[1]*k, a[0]*k)


def multiply(a, c):
    products = [x*y for x in a for y in c]
    return min(products)//S, -((-max(products))//S)


def atan_bounds(denominator):
    x = F(1, denominator)
    term = x
    total = F(0)
    k = 0
    tolerance = F(1, S << 32)
    while True:
        signed = term/F(2*k+1)
        total += signed if k % 2 == 0 else -signed
        k += 1
        term *= x*x
        remainder = term/F(2*k+1)
        if remainder < tolerance:
            other = total + (remainder if k % 2 == 0 else -remainder)
            return (min(total, other), max(total, other)), k


@lru_cache(None)
def pi_bounds():
    a, ka = atan_bounds(5)
    c, kc = atan_bounds(239)
    return (16*a[0]-4*c[1], 16*a[1]-4*c[0]), (ka, kc)


def cos_point_bounds(x):
    assert 0 <= x <= 2
    term = F(1)
    total = F(1)
    k = 0
    while True:
        k += 1
        term *= x*x/F((2*k-1)*(2*k))
        total += term if k % 2 == 0 else -term
        remainder = term*x*x/F((2*k+1)*(2*k+2))
        if remainder < F(1, S << 32):
            other = total + (remainder if k % 2 == 1 else -remainder)
            return min(total, other), max(total, other)


def cosine_axis(n):
    pi, counts = pi_bounds()
    lower = cos_point_bounds(pi[1]/n)[0]
    upper = cos_point_bounds(pi[0]/n)[1]
    seed = (rat(lower)[0], rat(upper)[1])
    values = [(S, S), seed]
    for j in range(2, n+1):
        values.append(add(scale(multiply(seed, values[-1]), 2), scale(values[-2], -1)))
    # These endpoints/midpoint are exact trigonometric identities, avoiding
    # unnecessary enclosure width in structurally zero cardinal values.
    values[0], values[n] = (S, S), (-S, -S)
    if n % 2 == 0:
        values[n//2] = (0, 0)
    return values, seed


def mode(values, j, p):
    n = len(values)-1
    r = (j*p) % (2*n)
    return values[min(r, 2*n-r)]


def chebyshev_polynomials(n):
    polys = [{0: 1}, {1: 1}]
    for k in range(2, n+1):
        out = {i+1: 2*c for i, c in polys[-1].items()}
        for i, c in polys[-2].items():
            out[i] = out.get(i, 0)-c
        polys.append({i: c for i, c in out.items() if c})
    return polys[:n+1]


def construct(n):
    assert 2 <= n <= 100
    xvalues, xseed = cosine_axis(n)
    yvalues, yseed = cosine_axis(n+1)
    chebyshev = chebyshev_polynomials(n)
    cardinals = []
    nodes = []
    for j in range(n+1):
        for k in range(n+2):
            if (j+k) % 2:
                continue
            weight = F(2, n*(n+1))
            if j in (0, n):
                weight /= 2
            if k in (0, n+1):
                weight /= 2
            polynomial = {}
            for p in range(n+1):
                for q in range(n-p+1):
                    h = (1 if p == 0 else 2)*(1 if q == 0 else 2)
                    if (p, q) == (n, 0):
                        h = 1  # Exceptional corrected x mode in PD-T101.
                    coefficient = multiply(multiply(mode(xvalues, j, p), mode(yvalues, k, q)), rat(weight*h))
                    for a, ca in chebyshev[p].items():
                        for c, cc in chebyshev[q].items():
                            polynomial[a, c] = add(polynomial.get((a, c), (0, 0)), scale(coefficient, ca*cc))
            cardinals.append(polynomial)
            nodes.append((j, k))
    assert len(cardinals) == (n+1)*(n+2)//2
    return cardinals, nodes, {"x_cosine_seed": list(xseed), "y_cosine_seed": list(yseed)}


def bernstein_coefficients(polynomials, n):
    # Two exact rational linear transforms instead of one quartic-size sum.
    result = []
    for polynomial in polynomials:
        intermediate = {}
        for j in range(n+1):
            row = [(i, interval) for (i, k), interval in polynomial.items() if k == j]
            for k in range(n+1):
                intermediate[k, j] = b.linearly_combine(
                    [interval for i, interval in row],
                    [b.monomial_to_bernstein(n, i, k) for i, interval in row])
        result.append([b.linearly_combine(
            [intermediate[k, j] for j in range(n+1)],
            [b.monomial_to_bernstein(n, j, l) for j in range(n+1)])
            for k in range(n+1) for l in range(n+1)])
    return result


def corner_interval(polynomials, corner):
    lower = upper = 0
    for p in polynomials:
        value = (0, 0)
        for (i, j), coefficient in p.items():
            value = add(value, scale(coefficient, corner[0]**i*corner[1]**j))
        lower += min(abs(v) for v in value) if value[0]*value[1] > 0 else 0
        upper += max(abs(v) for v in value)
    return lower, upper


def setup(n):
    polynomials, nodes, seeds = construct(n)
    corners = ((-1, -1), (1, -1)) if n % 2 == 0 else ((-1, -1), (-1, 1))
    bounds = [corner_interval(polynomials, e) for e in corners]
    # Equality of the two actual values follows from exact node symmetry
    # and cardinal uniqueness; intersect their valid enclosures.
    threshold = [max(z[0] for z in bounds), min(z[1] for z in bounds)]
    assert S < threshold[0] <= threshold[1]
    coeffs = bernstein_coefficients(polynomials, n)
    pi, counts = pi_bounds()
    return coeffs, {"n": n, "precision": PRECISION, "scale": S,
                    "threshold_interval": threshold, "corners": [list(e) for e in corners],
                    "cardinal_constructor": "PD-T101 corrected kernel; rigorous rational cosine intervals",
                    "cardinals": len(polynomials), "pi_interval": [str(z) for z in pi],
                    "machin_terms": list(counts), "dependency_sha256": b.digest(DEPENDENCY), **seeds}


def self_test():
    assert b.self_test()
    import finite_n2_exact as exact
    inv, det = exact.inverse([[x**i*y**j for i, j in exact.MONOMIALS] for x, y in exact.NODES])
    actual, nodes, seeds = construct(2)
    expected_nodes = [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
    assert nodes == expected_nodes
    for cardinal, p in enumerate(actual):
        for row, monomial in enumerate(exact.MONOMIALS):
            q = inv[row][cardinal]*S
            z = p.get(monomial, (0, 0))
            assert z[0] <= q <= z[1]
    return True


if __name__ == "__main__":
    assert self_test()
    print("exact general-constructor controls passed")
