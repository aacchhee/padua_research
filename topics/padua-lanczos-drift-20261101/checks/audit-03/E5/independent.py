#!/usr/bin/env python3
"""Audit-03 E5: raw cosine series and independent exact P4 polynomial/Arb check.

No developer/reviewer checker imports. Output is a compact audit receipt; the
universal claims are checked analytically in E5.md, not inferred from samples.
"""
import hashlib
import json
import platform
from pathlib import Path

import flint
from flint import arb, ctx
import sympy as s

ORDER = 8  # coefficients h^0 through h^7
h, a, p = s.symbols("h a p", real=True)


def coeffs(expr):
    poly = s.Poly(s.expand(expr), h)
    return [poly.nth(i) for i in range(ORDER)]


def mul(v, w):
    return [s.expand(sum(v[j] * w[k-j] for j in range(k+1)))
            for k in range(ORDER)]


def cosine(expr):
    v = coeffs(expr)
    v2 = mul(v, v)
    v4 = mul(v2, v2)
    v6 = mul(v4, v2)
    return [s.expand(int(k == 0) - v2[k]/2 + v4[k]/24 - v6[k]/720)
            for k in range(ORDER)]


def raw_series():
    # h=1/n, theta=pi*h, phi=pi*h/(1+h), t=a*h^4. Reduce only
    # the exact pi in each high-angle cosine; all remaining angles are O(h).
    ph = p*sum((-1)**(k-1)*h**k for k in range(1, ORDER))
    rows = []
    leading = []
    for m in range(4):
        arg1 = -m*p*h + a*h**3 - m*a*h**4   # (n-m)*(theta+t)-pi
        arg2 = m*ph + m*a*h**4              # m*(phi+t)
        arg3 = m*p*h + m*a*h**4             # m*(theta+t)
        arg4 = -m*ph + a*h**3+(1-m)*a*h**4  # (n+1-m)*(phi+t)-pi
        c1, c2 = mul(cosine(arg1), cosine(arg2)), mul(cosine(arg3), cosine(arg4))
        g = [s.expand(c2[k]-c1[k]) for k in range(ORDER)]
        expected = -a**2-s.Rational(2, 3)*a*p**3*m**3
        assert all(v == 0 for v in g[:7])
        assert s.expand(g[7]-expected) == 0
        rows.append({"m": m, "coefficients_h0_through_h7": list(map(str, g))})
        leading.append(g[7])
    q = s.expand(9*(leading[1]**2-leading[0]*leading[2]/2)
                 + leading[2]**2-leading[1]*leading[3])
    lo, hi = 4*p**3*(5-s.sqrt(2))/9, 4*p**3*(5+s.sqrt(2))/9
    assert s.expand(q - s.Rational(9, 2)*a**2*(a-lo)*(a-hi)) == 0
    assert s.simplify(q.subs(a,20*p**3/9) + 6400*p**12/729) == 0
    for base in (p*h, ph):
        shifted, original = cosine(base+a*h**4), cosine(base)
        d = [s.expand(u-v) for u, v in zip(shifted, original)]
        assert all(v == 0 for v in d[:5]) and s.expand(d[5]+a*p) == 0
    return {"raw_generators": rows, "Q": str(s.factor(q)),
            "a_minus": str(lo), "a_plus": str(hi),
            "both_distance_h5_coefficients": str(-a*p), "pass": True}


def finite_check():
    ctx.prec = 384
    x, y = s.symbols("x y")
    g = [s.chebyshevt(4-m,x)*s.chebyshevt(m,y)
         -s.chebyshevt(m,x)*s.chebyshevt(5-m,y) for m in range(4)]
    poly = s.Poly(9*(g[1]**2-g[0]*g[2]/2)+g[2]**2-g[1]*g[3], x, y)
    pi = arb.pi()
    positive_a, astar = 20*pi**3/9, 20*pi**3/9-512*pi
    alpha, beta = pi/4+astar/256, pi/5+astar/256
    xx, yy = alpha.cos(), beta.cos()
    value = arb(0)
    for (i,j), c in poly.terms():
        value += (arb(int(s.numer(c)))/int(s.denom(c)))*xx**i*yy**j
    # Separate product-to-sum representation, no Chebyshev recurrence.
    gt = []
    for m in range(4):
        u, v, w, z = (4-m)*alpha, m*beta, m*alpha, (5-m)*beta
        gt.append(((u+v).cos()+(u-v).cos()-(w+z).cos()-(w-z).cos())/2)
    other = 9*(gt[1]**2-gt[0]*gt[2]/2)+gt[2]**2-gt[1]*gt[3]
    qstar = astar**2*(81*astar**2-360*pi**3*astar+368*pi**6)/18
    assert astar < 0 and value < 0 and other < 0 and qstar > 0
    assert value.overlaps(other)
    assert value > -arb(104219)/1000000 and value < -arb(104218)/1000000
    assert s.expand((20*s.pi**3/9-512*s.pi)/256-(20*s.pi**3/9)/256+2*s.pi) == 0
    for base, coordinate in ((pi/4,xx),(pi/5,yy)):
        assert coordinate.overlaps((base+positive_a/256).cos())
    return {"precision_bits": ctx.prec, "P4_exact_polynomial": str(poly.as_expr()),
            "P4_degree": poly.total_degree(), "P4_term_count": len(poly.terms()),
            "a_star": astar.str(45, radius=True),
            "P4_expanded_polynomial": value.str(45, radius=True),
            "P4_expanded_polynomial_radius": str(value.rad()),
            "P4_product_to_sum": other.str(45, radius=True),
            "certified_rational_bounds": "-104219/1000000 < P4 < -104218/1000000 < 0",
            "Q_astar_positive": str(qstar), "pass": True}


if __name__ == "__main__":
    result = {"producer": "Codex audit-03 E5; configured gpt-6-astra xhigh",
              "resolved_runtime_metadata": "not independently exposed",
              "python": platform.python_version(), "sympy": s.__version__,
              "python_flint": flint.__version__,
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "series": raw_series(), "finite": finite_check(), "result": "PASS"}
    print(json.dumps(result, indent=2, sort_keys=True))
