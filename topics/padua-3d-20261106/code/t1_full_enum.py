#!/usr/bin/env python3
"""Developer D3(b) census of the full classified reflection-invariant class.

For target N, every projection has <=N cosine levels, hence canonical torus
order m_j<=2N, including inactive half phases. Enumerate all ordered m_j,
every admissible binary code, every affine syndrome, and inactive half phase.
Only exact int64 arithmetic is used (the supported n<=6 keeps products small).
This evaluates the accepted count/screen formulas; it does not test ranks or
replace the separately accepted hand proof. No audit code is imported.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np

from t1_reflection_enum import binary_subspaces, affine_parity_codes


def census(n, cap=None):
    target = math.comb(n + 3, 3)
    cap = 2 * target if cap is None else cap
    orders = [np.arange(1, cap + 1, dtype=np.int64).reshape(shape)
              for shape in ((cap, 1), (1, cap))]
    classes = []
    for code in binary_subspaces(3):
        if any(1 << j in code for j in range(3)):
            continue
        active = [j for j in range(3) if any(b & (1 << j) for b in code)]
        inactive = [j for j in range(3) if j not in active]
        count = short_count = alias_count = survivor_count = 0
        for affine in affine_parity_codes(code, 3):
            patterns = sorted({tuple((p >> j) & 1 for j in active)
                               for p in affine})
            for phase in itertools.product((0, 1), repeat=len(inactive)):
                phase_map = dict(zip(inactive, phase))
                for first in range(1, cap + 1):
                    ms = [first, *orders]
                    valid = True
                    projections = []
                    for j, m in enumerate(ms):
                        if j in active:
                            valid = valid & (m % 2 == 0)
                            projections.append(m // 2 + 1)
                        elif phase_map[j] == 0:
                            projections.append(m // 2 + 1)
                        else:
                            projections.append((m + 1) // 2)
                    coupled = 0
                    for pattern in patterns:
                        term = 1
                        for j, bit in zip(active, pattern):
                            q = ms[j] // 2
                            term = term * ((q + 1) // 2 if bit else q // 2 + 1)
                        coupled = coupled + term
                    folded = coupled
                    for j in inactive:
                        folded = folded * projections[j]
                    hit = np.broadcast_to(valid & (folded == target), (cap, cap))
                    short = False
                    for level in projections:
                        short = short | (level <= n)
                    # The only 2-dimensional admissible code is the even plane;
                    # two q_j<=n then give the accepted pair Chebyshev alias.
                    alias = False
                    if len(code) == 4:
                        low = sum(np.asarray(ms[j] // 2 <= n, dtype=np.int8)
                                  for j in range(3))
                        alias = low >= 2
                    count += int(np.count_nonzero(hit))
                    short_count += int(np.count_nonzero(hit & short))
                    alias_count += int(np.count_nonzero(hit & ~np.asarray(short) & alias))
                    survivor_count += int(np.count_nonzero(
                        hit & ~np.asarray(short) & ~np.asarray(alias)))
        classes.append({"binary_code": sorted(code), "target_count_cosets": count,
                        "short_projection": short_count, "pair_alias_after_short": alias_count,
                        "surviving_necessary_screens": survivor_count})
    totals = {key: sum(row[key] for row in classes) for key in
              ("target_count_cosets", "short_projection", "pair_alias_after_short",
               "surviving_necessary_screens")}
    if totals["target_count_cosets"] != sum(totals[key] for key in
            ("short_projection", "pair_alias_after_short", "surviving_necessary_screens")):
        raise RuntimeError("screen partition does not cover target cases")
    if totals["surviving_necessary_screens"]:
        raise RuntimeError("counterexample to the necessary-screen obstruction")
    return {"degree": n, "target": target, "projection_order_cap": cap,
            "full_class": cap >= 2 * target, "classes": classes, **totals}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # First reconcile the independently enumerated torus-point diagnostic's
    # bounded counts before extending its parameter cap.
    old = json.loads(Path(__file__).parents[1].joinpath(
        "evidence/t1-reflection-enum.json").read_text())
    bounded = [census(n, 12) for n in range(2, 7)]
    prior = {row["degree"]: row["target_count_cosets"]
             for row in old["dimensions"][0]["degree_rows"]}
    if any(row["target_count_cosets"] != prior[row["degree"]] for row in bounded):
        raise RuntimeError("bounded formula counts disagree with actual folded-point census")
    rows = [census(n) for n in range(2, 7)]
    receipt = {
        "schema": "padua-3d-T1-full-class-formula-census-v1",
        "date": "2026-11-06", "rules_sha": "e5b64450fce42262dafc88ee357b72e5f203916b",
        "command": ["python", "topics/padua-3d-20261106/code/t1_full_enum.py",
                    "--output", str(args.output)],
        "claim_status": "MEASURED finite census; accepted analytic theorem is separate",
        "arithmetic": "exact numpy int64; n=2..6 only",
        "python": platform.python_version(), "numpy": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_sha256": hashlib.sha256(Path(__file__).with_name(
            "t1_reflection_enum.py").read_bytes()).hexdigest(),
        "bounded_control_receipt_sha256": hashlib.sha256(Path(__file__).parents[1].joinpath(
            "evidence/t1-reflection-enum.json").read_bytes()).hexdigest(),
        "bounded_control_target_counts": [row["target_count_cosets"] for row in bounded],
        "bound_reason": "each axis has <=N cosine levels; active m=2q<2N; "
                        "inactive m<=2N for either half phase",
        "rows": rows, "verdict": "PASS", "claim": "finite full-class necessary-screen census; "
            "the analytic theorem and classification remain separate proof premises"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": "PASS", "counts": [r["target_count_cosets"] for r in rows],
                      "survivors": [r["surviving_necessary_screens"] for r in rows],
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
