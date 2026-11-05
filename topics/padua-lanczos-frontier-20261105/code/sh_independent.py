#!/usr/bin/env python3
"""Supplemental exact finite checks of the analytic SH_n proof.

No developer mathematical code is imported. This is not a finite reduction of
the all-degree theorem. In the tensor sine basis, 2S and 2T are integer path
adjacency operators and the exact normalized columns are coordinate vectors.
We differentiate full projection and normalization, keeping coefficient
derivatives, and compare with a separately assembled frozen recurrence.
"""

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sy


PROOF_HASH = "9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d"


def ordered(n):
    return [(d - j, j) for d in range(n + 1) for j in range(d + 1)]


def creator(r, j, rule):
    if (rule == "BJ" and j == 0) or (rule == "mirror" and r > 0):
        return "S", (r - 1, j)
    return "Y", (r, j - 1)


def exact_jacobian(n, rule):
    cols = ordered(n)
    lookup = {v: k for k, v in enumerate(cols)}
    m = n + 2
    M, N = m * m, len(cols)
    H, K = N - 1, (N - 1) * M
    modes = [r * m + j for r, j in cols]
    degrees = [r + j for r in range(m) for j in range(m)]
    normal = [a for a, d in enumerate(degrees) if d > n]

    def twice(kind, v):
        out = np.zeros(v.shape, dtype=object)
        for a in range(m):
            for b in range(m):
                row = a * m + b
                if kind in ("S", "Y"):
                    scale = 2 if kind == "Y" else 1
                    if a:
                        out[row] += scale * v[row - m]
                    if a + 1 < m:
                        out[row] += scale * v[row + m]
                if kind in ("T", "Y"):
                    if b:
                        out[row] += v[row - 1]
                    if b + 1 < m:
                        out[row] += v[row + 1]
        return out

    def upoly(kind, degree, v):
        if degree == 0:
            return v.copy()
        old, now = v, twice(kind, v)
        for _ in range(1, degree):
            old, now = now, twice(kind, now) - old
        return now

    I = np.eye(M, dtype=object)
    D = [np.zeros((M, K), dtype=object)]
    V = [np.zeros((M, K), dtype=object)]
    sigma4 = []
    largest = 0
    for h, (r, j) in enumerate(cols[1:], 1):
        kind, parent = creator(r, j, rule)
        p = lookup[parent]
        a2 = twice(kind, I[:, modes[p]])
        residual2 = a2.copy()
        for l in range(h):
            residual2[modes[l]] -= a2[modes[l]]
        assert np.array_equal(residual2, I[:, modes[h]])
        s4 = sum(int(a) ** 2 for a in a2)
        sigma4.append(s4)
        if rule == "mirror":
            assert 0 < s4 <= 6
        da2 = twice(kind, D[p])
        da2[:, (h - 1) * M:h * M] += 2 * I
        dr2 = da2.copy()
        frozen = twice(kind, V[p])
        frozen[:, (h - 1) * M:h * M] += 2 * I
        for l in range(h):
            c2 = a2[modes[l]]
            # 2 dc_l = <dq_l, 2A q_parent> + <q_l, 2 da>.
            dc2 = da2[modes[l]].copy()
            for a, coefficient in enumerate(a2):
                if coefficient:
                    dc2 += coefficient * D[l][a]
            dr2[modes[l]] -= dc2
            if c2:
                dr2 -= c2 * D[l]
                frozen -= c2 * V[l]
        # beta=1/2, so dq = 2 dr - q <q,2 dr>.
        dr2[modes[h]] = 0
        error = dr2 - frozen
        assert not np.any(error[[a for a, d in enumerate(degrees) if d > r + j]])
        D.append(dr2)
        V.append(frozen)
        largest = max(largest, max(abs(int(a)) for a in dr2.flat))

    for k in range(N):
        for l in range(k + 1):
            assert not np.any(D[k][modes[l]] + D[l][modes[k]])
        assert np.array_equal(D[k][normal], V[k][normal])
        # Every source already in its degree space has zero final span image.
        for h, (r, j) in enumerate(cols[1:], 1):
            admissible = [(h - 1) * M + a for a, d in enumerate(degrees) if d <= r + j]
            assert not np.any(D[k][np.ix_(normal, admissible)])

    result = {"n": n, "rule": rule, "M": M, "N": N,
              "source_coordinate_directions": K,
              "exact_full_projection_derivative_matches_normal_frozen_map": True,
              "degree_bounded_correction_and_orthonormal_tangent": True,
              "degree_compatible_source_kernel": True,
              "largest_integer_derivative_entry": largest}
    if rule == "BJ":
        h = lookup[(n, 0)]
        assert sigma4[h - 1] == 2
        e = (n + 1) * m
        direction = (h - 1) * M + e
        norm_squared = 0
        for k, (r, j) in enumerate(cols):
            predicted = np.zeros(M, dtype=object)
            if r + j == n:
                predicted[e] = 2 * (-2) ** j
            assert np.array_equal(D[k][:, direction], predicted)
            norm_squared += sum(int(a) ** 2 for a in D[k][normal, direction])
        assert norm_squared // 2 == 2 * (4 ** (n + 1) - 1) // 3
        result["unit_relative_source_bj_gain_squared"] = norm_squared // 2
    else:
        for k, (r, j) in enumerate(cols):
            boundary = np.zeros((M, K), dtype=object)
            for b in range(1, j + 1):
                op = upoly("T", j - b, I)
                h0, h1 = lookup[(0, b)], lookup[(1, b - 1)]
                boundary[:, (h0 - 1) * M:h0 * M] += 2 * op
                boundary[:, (h1 - 1) * M:h1 * M] -= 4 * op
            closed = upoly("S", r, boundary)
            for a in range(1, r + 1):
                h = lookup[(a, j)]
                closed[:, (h - 1) * M:h * M] += 2 * upoly("S", r - a, I)
            assert np.array_equal(closed, V[k])
        hs4 = 0
        for h, s4 in enumerate(sigma4, 1):
            for column in D:
                block = column[normal, (h - 1) * M:h * M]
                hs4 += s4 * sum(int(a) ** 2 for a in block.flat)
        assert hs4 <= 96 * (n + 1) ** 4 * H ** 2
        result.update({"all_source_mirror_closed_form": True,
                       "relative_source_hilbert_schmidt_squared": str(Fraction(hs4, 4)),
                       "stated_upper_squared": 24 * (n + 1) ** 4 * H ** 2})
    return result


def symbolic_creators(n):
    x, y = sy.symbols("x y")
    cols = ordered(n)
    lookup = {pair: k for k, pair in enumerate(cols)}
    q = [sy.Poly(sy.chebyshevu(r, x) * sy.chebyshevu(j, y - 2 * x), x, y)
         for r, j in cols]
    checked = 0
    for rule in ("BJ", "mirror"):
        for h, (r, j) in enumerate(cols[1:], 1):
            kind, parent = creator(r, j, rule)
            a = x if kind == "S" else y
            raw = sy.Poly(a * q[lookup[parent]].as_expr(), x, y)
            coefficients = {}
            for l in range(h, -1, -1):
                u, v = cols[l]
                coefficient = raw.coeff_monomial(x ** u * y ** v) / 2 ** (u + v)
                if coefficient:
                    coefficients[l] = coefficient
                    raw -= coefficient * q[l]
            assert raw.is_zero
            assert coefficients[h] == sy.Rational(1, 2)
            s2 = sum(c * c for c in coefficients.values())
            u, v = parent
            expected = ((1 + int(u > 0)) / sy.Integer(4) if kind == "S"
                        else 1 + int(u > 0) + (1 + int(v > 0)) / sy.Integer(4))
            assert s2 == expected
            # The monic rescaling gives creator coefficient exactly one.
            monic_child = coefficients[h] * 2 ** (r + j) / 2 ** (u + v)
            assert monic_child == 1
            checked += 1
    return {"n": n, "creator_identities": checked,
            "physical_polynomial_triangularity_pivots_scales_and_monic_factors": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    topic = Path(__file__).resolve().parents[1]
    proof = topic / "theory/l1-01-sheared-U-aggregate-separation.md"
    actual_hash = hashlib.sha256(proof.read_bytes()).hexdigest()
    assert actual_hash == PROOF_HASH, "Proof changed; this audit needs an impact check."
    rows = [exact_jacobian(n, rule) for n in (2, 3, 4) for rule in ("BJ", "mirror")]
    symbolic = symbolic_creators(8)
    receipt = {
        "status": "PASS_SUPPLEMENTAL_EXACT_FINITE_CHECKS",
        "scope": "Exact finite diagnostics only; no all-degree finite reduction or IEEE run.",
        "proof_sha256": actual_hash,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "sympy": sy.__version__},
        "arithmetic": "Python arbitrary-precision integers in NumPy object arrays; SymPy rational polynomials",
        "command": "python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent.json",
        "representation": "Tensor Jacobi basis: 2S and 2T are path adjacency matrices, equivalent via the exact discrete sine transform to the weighted SH_n node basis.",
        "rows": rows,
        "symbolic": symbolic,
    }
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["status"])
    print(json.dumps({"jacobian_cases": len(rows), "symbolic": symbolic}))


if __name__ == "__main__":
    main()
