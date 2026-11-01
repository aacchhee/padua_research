"""Independent formal degree-twelve field construction for n7 verification.

No real embedding is selected here. An accepting checker must separately verify
the principal real brackets and all serialized field data. This module derives
the generators by a polynomial gcd rather than importing producer expressions.
"""
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import sympy as sp

Z, T = sp.symbols("z t")
THETA_SYMBOL = sp.Symbol("theta")
P3 = sp.Poly(Z**3-Z**2-2*Z+1, Z, domain=sp.QQ)
P4 = sp.Poly(Z**4-4*Z**2+2, Z, domain=sp.QQ)
MINPOLY = sp.Poly(sp.resultant(P3.as_expr(), P4.as_expr().subs(Z, T-Z), Z), T, domain=sp.QQ).monic()
def require(condition, message):
    if not condition:
        raise ValueError(message)


require(MINPOLY.degree() == 12 and MINPOLY.is_irreducible, "formal degree-twelve irreducibility failed")
FIELD = sp.QQ.algebraic_field((MINPOLY, THETA_SYMBOL))
THETA = FIELD.unit


def formal_from_sympy(value):
    if isinstance(value, sp.AlgebraicNumber):
        value = value.as_expr()
    numerator, denominator = sp.fraction(sp.cancel(sp.sympify(value)))
    p = sp.Poly(numerator, THETA_SYMBOL, domain=sp.QQ)
    q = sp.Poly(denominator, THETA_SYMBOL, domain=sp.QQ)
    return FIELD([FIELD.dom.from_sympy(c) for c in p.all_coeffs()]) / \
        FIELD([FIELD.dom.from_sympy(c) for c in q.all_coeffs()])


# Conversion is exact rational-function reduction in a formal quotient;
# no approximate real root selector participates.
FIELD.from_sympy = formal_from_sympy
LEFT = sp.Poly.from_dict({(3,): FIELD.one, (2,): -FIELD.one,
                          (1,): FIELD(-2), (0,): FIELD.one}, (Z,), domain=FIELD)
right = {}
for degree, coefficient in ((4, 1), (2, -4), (0, 2)):
    for k in range(degree+1):
        right[(k,)] = right.get((k,), FIELD.zero) + \
            int(coefficient*sp.binomial(degree, k)) * (-1)**k * THETA**(degree-k)
RIGHT = sp.Poly.from_dict(right, (Z,), domain=FIELD)
GCD = sp.gcd(LEFT, RIGHT).monic()
require(GCD.degree() == 1, "formal generator gcd is not linear")
A = -GCD.rep.nth(0)
B = THETA-A
require(A**3-A**2-2*A+FIELD.one == FIELD.zero, "formal cubic generator identity failed")
require(B**4-4*B**2+FIELD(2) == FIELD.zero, "formal quartic generator identity failed")
require(A+B == THETA, "formal primitive generator identity failed")
NATIVE_TENSOR = tuple(A**i*B**j for i in range(3) for j in range(4))


def native(value):
    return value if FIELD.of_type(value) else formal_from_sympy(value)


def power_coordinates(value):
    coefficients = [Fraction(str(q)) for q in reversed(native(value).to_list())]
    require(len(coefficients) <= 12, "formal quotient exceeds degree twelve")
    return tuple(coefficients + [Fraction(0)]*(12-len(coefficients)))


TO_NATIVE = sp.Matrix.hstack(*(sp.Matrix([sp.Rational(q.numerator, q.denominator)
                                        for q in power_coordinates(value)])
                              for value in NATIVE_TENSOR))
TO_TENSOR = TO_NATIVE.inv()
require(TO_TENSOR*TO_NATIVE == sp.eye(12) and TO_NATIVE*TO_TENSOR == sp.eye(12),
        "formal tensor inverse identities failed")
TRANSFORM = tuple(tuple(Fraction(str(q)) for q in row) for row in TO_TENSOR.tolist())


@lru_cache(maxsize=65536)
def basis_coefficients(value):
    coefficients = power_coordinates(value)
    return tuple(sum((row[k]*coefficients[k] for k in range(12)), Fraction(0))
                 for row in TRANSFORM)


for k, value in enumerate(NATIVE_TENSOR):
    require(basis_coefficients(value) == tuple(Fraction(int(i == k)) for i in range(12)),
            "formal tensor unit identity failed")


def receipt():
    return {"scope": "formal quotient and generator identities only; real embedding/count unverified",
            "degree": 12, "irreducible": True, "generator_gcd_degree": GCD.degree(),
            "minpoly": [str(q) for q in MINPOLY.all_coeffs()],
            "a_native_ascending": list(map(str, power_coordinates(A))),
            "b_native_ascending": list(map(str, power_coordinates(B))),
            "tensor_order": "a^i*b^j, i=0,1,2 then j=0,1,2,3",
            "native_to_tensor": [[str(q) for q in row] for row in TRANSFORM],
            "inverse_identities_verified": True, "tensor_basis_units_verified": True,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "sympy": sp.__version__}


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
