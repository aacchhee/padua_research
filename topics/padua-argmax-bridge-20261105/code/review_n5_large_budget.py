#!/usr/bin/env python3
"""Supplementary exact arithmetic only; no producer imports or measured Q runs."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

TOPIC = Path(__file__).resolve().parents[1]
PINS = {
    "theory/N5-large-budget.md": "0e86fe06ccf8845c5fa6e5715e7e35618775573c00bca69a7e9660ee02c76247",
    "code/n5_large_budget.py": "c7840ec6cfc801cbc353bf9f67d3831b9207b4b8d9d7da93009552b2f4bf8056",
    "evidence/n5-large-budget.json": "fc7582ff0375c0f55779aeb026f42a81228bb6c9dc479642f3d791fe64342c1e",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for rel, expected in PINS.items():
        assert sha(TOPIC / rel) == expected, rel
    a, c = F(15, 16), F(11, 15)
    assert a * (1-c) == F(1, 4)
    z = F(1, 3)
    log_upper = 2*sum(z**j/j for j in (1, 3, 5)) + 2*z**7/(7*(1-z*z))
    atanh_lower = sum(c**j/j for j in (1, 3, 5, 7, 9))
    assert log_upper == F(23581, 34020) < F(347, 500)
    assert atanh_lower == F(2253160124237, 2421931640625) > F(93, 100)
    # Independently check Machin's tangent identity by two doubling steps.
    tangent = F(1, 5)
    for _ in range(2):
        tangent = 2*tangent/(1-tangent*tangent)
    assert (tangent-F(1,239))/(1+tangent/F(239)) == 1
    pi_lower = 16*(F(1,5)-F(1,375))-F(4,239)
    assert pi_lower == F(281476, 89625) > F(157,50)
    coeff = 2*c*F(347,500)-1/c-1/(6*c**3)
    assert coeff == F(-1917599,2495625) < 0
    constant = 1+1/(6*c*c)+F(1,18)
    # Polynomial division for the integrated entropy envelope:
    # (-s²/c-s⁴/(6c³))/(1-s²)
    # = -(1/c+1/(6c³))/(1-s²)+1/c+(1+s²)/(6c³).
    # Check coefficients after multiplication by (1-s²).
    b0, b2 = 1/c+1/(6*c**3), 1/(6*c**3)
    assert b0-b0 == 0 and b2-b0 == -1/c and -b2 == -1/(6*c**3)
    assert b0*c+b2*c**3/3 == constant
    bracket = coeff*F(93,100)+constant
    bound = 4*a*bracket/F(157,50)**2
    assert bracket > 0
    assert bound == F(487302379,1968469140) < F(1,4)
    assert F(1,4)-bound == F(2407453,984234570)
    result = {
        "status": "PASS",
        "scope": "exact rational arithmetic supporting the analytic scoped obstruction; no actual Q counterexample or all-degree quarter-floor proof",
        "inputs_sha256": PINS,
        "review_source_sha256": sha(Path(__file__)),
        "values": {k: str(v) for k, v in {
            "log2_upper_series": log_upper,
            "atanh_c_lower_series": atanh_lower,
            "pi_lower_series": pi_lower,
            "negative_coefficient": coeff,
            "positive_bracket": bracket,
            "strict_limit_upper": bound,
            "quarter_minus_upper": F(1,4)-bound,
        }.items()},
        "machin_tangent_identity": True,
        "integrated_polynomial_division": True,
        "producer_imports": False,
        "measurement_replay": False,
        "python": sys.version.split()[0],
    }
    output = TOPIC / "evidence/n5-large-budget-review.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "PASS", "receipt": str(output), "sha256": sha(output)}))


if __name__ == "__main__":
    main()
