#!/usr/bin/env python3
"""Exact scalar controls for frozen C02 proof; no board/backend evaluation."""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import time


def identity(path):
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": sha256(raw).hexdigest()}


def main():
    start = time.process_time()
    bernoulli = [F(1)]
    for degree in range(1, 65):
        bernoulli.append(-sum((F(comb(degree + 1, k)) * bernoulli[k]
                               for k in range(degree)), F(0)) / (degree + 1))
    geom = (1 + 11*F(1, 4) + 11*F(1, 4)**2 + F(1, 4)**3)/(1-F(1, 4))**5
    smooth = F(389120, 19683 * 3**5) * 195**4 / 4**96
    eta = abs(bernoulli[64]) / (64 * 64**64)
    eta_coarse = F(4 * factorial(63), 6**64 * 64**64)
    global_smooth_factor = F(7 * 4**4, 2880) * F(7, 24)
    global_harmonic_factor = 16 * (2 + F(4, 3) * 65)
    results = {
        "geometric_power_sum_constant": geom == F(1520, 81),
        "smooth_M96_lt_2m165": smooth < F(1, 2**165),
        "eta_exact_le_coarse": eta <= eta_coarse,
        "eta_coarse_lt_2m256": eta_coarse < F(1, 2**256),
        "global_smooth_factor_lt_one_fifth": global_smooth_factor < F(1, 5),
        "global_harmonic_factor_lt_2p11": global_harmonic_factor < 2**11,
        "global_E_lt_2m166": smooth/5 + eta_coarse*2**11 < F(1, 2**166),
    }
    assert all(results.values()), results
    topic = Path(__file__).resolve().parents[1]
    payload = {
        "status": "EXACT scalar arithmetic controls; no independent proof review",
        "results": results,
        "bernoulli_B64": str(bernoulli[64]),
        "cpu_seconds": time.process_time() - start,
        "sources": [identity(Path(__file__).resolve()),
                    identity(topic / "theory/C02-row-cotangent.md"),
                    identity(topic / "ideas/C02-row.md")],
        "limits": "No partial-sum backend, point/box test, degree extension, fit, cover or performance evidence.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
