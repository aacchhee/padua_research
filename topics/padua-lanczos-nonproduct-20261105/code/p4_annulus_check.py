#!/usr/bin/env python3
"""Exact low-degree annulus moments and monic Gram check, no rate scan."""
from fractions import Fraction as F
from math import factorial
import hashlib
import json
from pathlib import Path
import platform
import sys


def latent_moment(a, b, epsilon):
    if a % 2 or b % 2:
        return F(0)
    a, b = a//2, b//2
    p = a+b
    angular = F(factorial(2*a)*factorial(2*b),
                4**p*factorial(a)*factorial(b)*factorial(p))
    radial = ((1+epsilon)**(p+1)-(1-epsilon)**(p+1))/(2*epsilon*(p+1))
    return angular*radial


def poly_add(a, factor, b):
    result = a.copy()
    for key, value in b.items():
        result[key] = result.get(key, F(0))+factor*value
    return {key: value for key, value in result.items() if value}


def poly_mul(a, b):
    result = {}
    for (ax, ay), av in a.items():
        for (bx, by), bv in b.items():
            key = (ax+bx, ay+by)
            result[key] = result.get(key, F(0))+av*bv
    return result


def poly_pow(a, n):
    result = {(0, 0): F(1)}
    for _ in range(n):
        result = poly_mul(result, a)
    return result


def check(epsilon, shear):
    # Polynomials are represented in latent S,T coordinates, but the
    # monomial order is the physical x,y order throughout the Gram graph.
    x = {(1, 0): F(1)}
    y = {(1, 0): F(shear), (0, 1): F(2)}

    def integral(p):
        return sum((v*latent_moment(a, b, epsilon)
                    for (a, b), v in p.items()), F(0))

    def inner(a, b):
        return integral(poly_mul(a, b))

    base, norms = [], []
    for degree in range(3):
        for j in range(degree+1):
            raw = poly_mul(poly_pow(x, degree-j), poly_pow(y, j))
            residual = raw.copy()
            for older, norm in zip(base, norms):
                residual = poly_add(residual, -inner(raw, older)/norm, older)
            base.append(residual)
            norms.append(inner(residual, residual))
    tau = epsilon*epsilon
    expected_last = 16*tau*(3+tau)/(9*(1+tau))
    source = poly_mul(y, base[2])
    source_squared = inner(source, source)
    expected_source = F(4*(shear*shear+12), 24)*(3+tau)
    expected_lower = F(3*(shear*shear+12), 32)*(1+tau)/tau
    assert norms[-1] == expected_last > 0
    assert source_squared == expected_source
    assert source_squared/norms[-1] == expected_lower
    covariance = [[inner(x, x), inner(x, y)],
                  [inner(y, x), inner(y, y)]]
    assert covariance == [[F(1, 2), F(shear, 2)],
                          [F(shear, 2), F(shear*shear+4, 2)]]
    return {"epsilon": str(epsilon), "shear": shear,
            "covariance": [[str(v) for v in row] for row in covariance],
            "last_pivot_squared": str(norms[-1]),
            "last_raw_scale_squared": str(source_squared),
            "capacity_squared_lower": str(expected_lower), "status": "PASS"}


rows = [check(F(1, divisor), shear)
        for shear in (0, 1) for divisor in (1, 2, 4, 8)]
report = {"status": "PASS", "scope": "exact degree2 moment/Gram check only",
          "rows": rows, "python": sys.version.split()[0],
          "platform": platform.platform(),
          "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "independent_rerun": "NOT CLAIMED",
          "cross_family_degree_12_16_gate": "NOT RUN"}
print(json.dumps(report, indent=2))
