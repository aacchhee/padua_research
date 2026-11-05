#!/usr/bin/env python3
"""Outward Arb evaluation of the proved T4 geometric series.

The finite-reduction and exact tail bound are in theory/t4-01, §4.
No quadrature or floating-point fit is used for the enclosure. Optional finite-n
regressions are explicitly MEASURED and do not enter the enclosure proof.
"""

import argparse
import hashlib
import json
import platform
from pathlib import Path

import flint
from flint import arb, ctx


def enclosure(order, bits):
    ctx.prec = bits
    aa = [arb(1)]
    for p in range(1, order + 1):
        aa.append(aa[-1] - 2 * arb(2 * p).zeta() / (4**p))
    bb = [arb(7) * arb(3).zeta() / 8]
    for q in range(1, order + 1):
        bb.append(
            (1 - arb(1) / (2 ** (2 * q + 3))) * arb(2 * q + 3).zeta()
            - (1 - arb(1) / (2 ** (2 * q + 1))) * arb(2 * q + 1).zeta()
        )
    cc = [sum((aa[p] * bb[k - p] for p in range(k + 1)), arb(0))
          for k in range(order + 1)]
    partial = 8 / arb.pi()**2 * sum(
        (cc[k] / (k + 1) for k in range(order + 1)), arb(0)
    )
    tail = arb(8) / (3 * (order + 2) * (4 ** (order + 1)))
    kappa = partial + arb(0, tail)
    c1 = 2 / arb.pi() * (arb.const_euler() + (8 / arb.pi()).log())
    corner_c = c1**2 + kappa
    kappa_bracket = ["0.919710118388492535099518225790",
                     "0.919710118388492535099518225791"]
    corner_c_bracket = ["1.846160310423926079759838737947",
                        "1.846160310423926079759838737948"]
    assert arb(kappa_bracket[0]) < kappa < arb(kappa_bracket[1])
    assert arb(corner_c_bracket[0]) < corner_c < arb(corner_c_bracket[1])
    return {
        "method": "Arb zeta coefficient arithmetic plus analytic rational tail",
        "status": "OUTWARD_ENCLOSURE_DEVELOPER_RUN",
        "precision_bits": bits,
        "order_inclusive": order,
        "tail_bound_exact": {"numerator": 8,
                             "denominator": 3 * (order + 2) * 4 ** (order + 1)},
        "tail_bound_ball": tail.str(50),
        "kappa_ball": kappa.str(50),
        "kappa_certified_decimal_bracket": kappa_bracket,
        "c1_ball": c1.str(50),
        "corner_c_ball": corner_c.str(50),
        "corner_c_certified_decimal_bracket": corner_c_bracket,
        "rational_bracket_checks": True,
    }


def regressions():
    """Direct finite corner formula, independent of coefficient evaluation."""
    import mpmath as mp
    mp.mp.dps = 45
    rows = []
    for n in [2, 3, 8, 9, 16, 17, 32, 33, 64, 65]:
        total = mp.mpf(0)
        for j in range(n + 1):
            a = mp.pi * j / n
            wj = mp.mpf(1) / 2 if j in (0, n) else 1
            for k in range(n + 1):
                if (j + k) % 2 == 0:
                    continue
                b = mp.pi * k / (n + 1)
                wk = mp.mpf(1) / 2 if k == 0 else 1
                total += wj * wk * (1 + mp.cos(b)) / abs(mp.cos(a) - mp.cos(b))
        corner = 4 * total / (n * (n + 1)) + mp.mpf(1) / (n + 1)
        ll = 2 * mp.fsum(
            (mp.mpf(1) / 2 if r == n else 1) / mp.sin(mp.pi * r / (2 * n))
            for r in range(1, n + 1, 2)
        ) / n
        aa = 2 / mp.pi * (mp.log(n) + mp.euler + mp.log(8 / mp.pi))
        assert abs(ll - aa) <= mp.mpf(1) / (4 * n * n)
        rows.append({"n": n, "corner": str(corner), "L_n": str(ll),
                     "corner_minus_square": str(corner - ll * ll),
                     "n2_times_1d_error": str((ll - aa) * n * n)})
    return {"status": "MEASURED_ONLY", "mpmath_version": mp.__version__,
            "decimal_precision": mp.mp.dps, "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=64)
    parser.add_argument("--bits", type=int, default=320)
    parser.add_argument("--regressions", action="store_true")
    args = parser.parse_args()
    if args.order < 52 or args.bits < 256:
        parser.error("the fixed 30-decimal bracket requires order >=52, bits >=256")
    result = enclosure(args.order, args.bits)
    result["python_version"] = platform.python_version()
    result["python_flint_version"] = flint.__version__
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["theory_sha256"] = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted((Path(__file__).resolve().parent.parent / "theory").glob("t4-*.md"))
    }
    if args.regressions:
        result["finite_regressions"] = regressions()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
