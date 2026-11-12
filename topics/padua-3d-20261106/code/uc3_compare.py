#!/usr/bin/env python3
"""Compare separately executed U3 evidence and inspect retained search rows.

Comparing retained M/R starts is record inspection, not a new optimizer run.
No prose is pinned; all code/data and raw identities checked here are actual.
"""
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def cubic_inverse(mode_order):
    half, quarter = Q(1, 2), Q(1, 4)
    # Independently hand-expanded product-to-sum columns for the inherited lead.
    columns = {(0, 0, 0): {0: 1}, (1, 0, 0): {1: 1}, (0, 1, 0): {4: 1},
               (0, 0, 1): {11: 1}, (2, 0, 0): {2: 1}, (0, 2, 0): {8: 1},
               (0, 0, 2): {18: -1}, (3, 0, 0): {3: 1}, (0, 3, 0): {12: 1},
               (0, 0, 3): {7: -1}, (1, 1, 0): {3: half, 5: half},
               (1, 0, 1): {10: half, 12: half}, (0, 1, 1): {7: half, 15: half},
               (2, 1, 0): {2: half, 6: half}, (1, 2, 0): {7: half, 9: half},
               (2, 0, 1): {9: half, 13: half}, (0, 2, 1): {3: half, 19: half},
               (1, 0, 2): {17: -half, 19: -half}, (0, 1, 2): {18: half, 14: -half},
               (1, 1, 1): {6: quarter, 8: quarter, 14: quarter, 16: quarter}}
    A = [[Q(columns[tuple(alpha)].get(r, 0)) for alpha in mode_order] for r in range(20)]
    augmented = [row+[Q(int(r == c)) for c in range(20)] for r, row in enumerate(A)]
    for col in range(20):
        pivot = next(r for r in range(col, 20) if augmented[r][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        factor = augmented[col][col]
        augmented[col] = [v/factor for v in augmented[col]]
        for r in range(20):
            if r != col:
                factor = augmented[r][col]
                augmented[r] = [x-factor*y for x, y in zip(augmented[r], augmented[col])]
    inverse = [row[20:] for row in augmented]
    assert all(sum(A[r][k]*inverse[k][c] for k in range(20)) == int(r == c)
               for r in range(20) for c in range(20))
    sums = [sum(abs(x) for x in row) for row in inverse]
    assert sum(sums) == 52 and max(sums) == 4
    assert sum(abs(row[0]) for row in inverse) == 1
    return [str(x) for x in sums]


def main():
    topic = Path(__file__).resolve().parents[1]
    evidence = topic/"evidence"
    inputs, data = [], {}
    names = ["u3-s", "u3-f", "u3-m", "u3-r", "u3-f-exact",
             "uc3-s-census", "uc3-s-matching", "uc3-f-census", "uc3-f-exact", "uc3-selected-check"]
    for name in names:
        path = evidence/(name+".json")
        value = json.loads(path.read_text())
        inputs.append({"path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)})
        raw = value.get("raw")
        if raw:
            assert Path(raw["path"]).stat().st_size == raw["bytes"]
            assert sha(raw["path"]) == raw["sha256"]
            inputs.append(raw)
        data[name] = value
    producer_s = {(r["n"], *r["z"][1:]): r for r in
                  map(json.loads, Path(data["u3-s"]["raw"]["path"]).read_text().splitlines())}
    independent_s = json.loads(Path(data["uc3-s-census"]["raw"]["path"]).read_text())
    support_cases = 0
    for degree in independent_s:
        for row in degree["details"]:
            source = producer_s[(degree["n"], row[0], row[1])]
            assert (source["support"] == "unique") == row[2]
            if row[2]:
                assert source["amp"] == row[3] and source["abs_det_C"] == row[4]
            support_cases += 1
    assert support_cases == len(producer_s)
    assert data["uc3-s-matching"]["casewise_matches"] == support_cases
    cubic_source = next(d for d in data["u3-s"]["degrees"] if d["n"] == 3)["cubic"]
    cubic_sums = cubic_inverse(cubic_source["mode_order"])
    assert cubic_sums == cubic_source["inverse_row_l1"]
    producer_f = {(r["n"], tuple(r["key"][1:])): r for r in
                  map(json.loads, Path(data["u3-f"]["raw"]["path"]).read_text().splitlines())}
    independent_f = json.loads(Path(data["uc3-f-census"]["raw"]["path"]).read_text())
    fold_cases = 0
    for degree in independent_f:
        for row in degree["details"]:
            source = producer_f[(degree["n"], tuple(row[0]))]
            assert source["count"] == row[1]
            assert (source["outcome"].startswith("modular-")) == (row[2] == "trace_compatible")
            fold_cases += 1
    assert fold_cases == len(producer_f)
    producer_exact = {(r["n"], tuple(r["key"][1:])): r["exact_rank"] for r in
                      map(json.loads, Path(data["u3-f-exact"]["raw"]["path"]).read_text().splitlines())
                      if "exact_rank" in r}
    independent_exact = json.loads(Path(data["uc3-f-exact"]["raw"]["path"]).read_text())
    assert len(producer_exact) == len(independent_exact)
    for row in independent_exact:
        assert producer_exact[(row["n"], tuple(row["parameters"]))] == row["rank_Q"]
        assert all(c[2] == row["rank_Q"] for c in row["actual_node_certificates"])
    positive_f = [r for r in independent_exact if r["rank_Q"] == math.comb(r["n"]+3, 3)]
    assert len(positive_f) == 2
    assert len({(r["L"], r["actual_nodes_sha256"]) for r in positive_f}) == 1
    selected, controls = {}, {}
    inspection = {}
    for route in ("s", "f", "m", "r"):
        for degree in data["u3-"+route]["degrees"]:
            if "selected" in degree:
                selected[degree["selected"]["id"]] = degree["selected"]
                controls[degree["n"]] = degree["controls"]
        if route in ("m", "r"):
            raw = list(map(json.loads, Path(data["u3-"+route]["raw"]["path"]).read_text().splitlines()))
            inspected = []
            for degree in data["u3-"+route]["degrees"]:
                n = degree["n"]
                starts = [r for r in raw if r["n"] == n and "outcome" in r]
                refined = [r for r in raw if r["n"] == n and "refined_from" in r]
                assert len(starts) == 512 == len({tuple(r["key"]) for r in starts})
                assert all(r["count"] == degree["selected"]["expected_count"] for r in starts+refined)
                assert len(refined) <= 3 and all(r["nfev"] <= 240 for r in refined)
                positive = [r for r in starts+refined if r.get("score") is not None]
                best = max(r["score"] for r in positive)
                expected = min((r for r in positive if best-r["score"] <= 1e-9), key=lambda r: r["key"])
                assert degree["selected"]["key"] == expected["key"]
                inspected.append({"n": n, "starts": len(starts), "refinements": len(refined),
                                  "refinement_nfev_actual_all": sum(r["nfev"] for r in refined)})
            inspection[route] = inspected
    quality_delta = 0.0
    for row in data["uc3-selected-check"]["rows"]:
        source = selected[row["id"]]
        assert row["node_count"] == source["expected_count"]
        assert all(c[2] == row["N"] for c in row["certificates"])
        for quality in row["qualities"]:
            quality_delta = max(quality_delta, abs(quality[1]-source["quality"][str(quality[0])]["sampled_lebesgue"]))
    control_delta = 0.0
    for n, row in data["uc3-selected-check"]["controls"].items():
        for name, values in row.items():
            for quality in values["qualities"]:
                control_delta = max(control_delta, abs(quality[1]-controls[int(n)][name][str(quality[0])]["sampled_lebesgue"]))
    assert quality_delta < 1e-8 and control_delta < 1e-10
    for name in ("uc3-s-census", "uc3-s-matching", "uc3-f-census", "uc3-f-exact", "uc3-selected-check"):
        pin = data[name]["code"]
        for code in pin if isinstance(pin, list) else [pin]:
            assert sha(code["path"]) == code["sha256"]
    scratch = Path(tempfile.mkdtemp(prefix="padua-uc3-compare-"))
    source_snapshot = scratch/Path(__file__).name
    source_snapshot.write_bytes(Path(__file__).read_bytes())
    receipt = {"command": " ".join(sys.argv), "code": {"path": str(Path(__file__).resolve()), "sha256": sha(__file__)},
               "source_snapshot": {"path": str(source_snapshot), "bytes": source_snapshot.stat().st_size,
                                   "sha256": sha(source_snapshot)}, "inputs": inputs,
               "S_casewise_support_matches": support_cases, "F_casewise_counts_and_pass_sets_match": fold_cases,
               "cubic_hand_table_inverse_row_l1": cubic_sums, "cubic_inverse_entry_l1": 52,
               "cubic_inverse_induced_infinity": 4, "cubic_coarse_Lebesgue_bound": 103,
               "F_casewise_exact_and_two_node_ranks_match": len(independent_exact),
               "F_labelled_full_rank_parameters": 2, "F_distinct_positive_physical_node_sets": 1,
               "selected_full_rank_two_prime_witnesses": len(selected),
               "max_selected_quality_difference": quality_delta, "max_control_quality_difference": control_delta,
               "M_R_raw_schedule_inspection_only": inspection, "current_code_pins": "PASS"}
    output = canonical(receipt)+b"\n"
    assert len(output) < 16384
    target = evidence/"uc3-comparison.json"
    target.write_bytes(output)
    print(json.dumps({"receipt": str(target), "bytes": len(output), "support_cases": support_cases,
                      "fold_cases": fold_cases, "exact_cases": len(independent_exact)}))


if __name__ == "__main__":
    main()
