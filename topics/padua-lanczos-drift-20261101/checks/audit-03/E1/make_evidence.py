#!/usr/bin/env python3
"""Compact receipt for actual E1 audit-03 executions; no producer mutation.

Run the commands listed in COMMANDS first. This script compares their fresh
outputs, including the independent reconstruction and the degree-4 replay.
It also records the deliberately missing-regeneration negative test.
"""
import datetime
import hashlib
import json
import platform
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
REPO = Path(__file__).resolve().parents[5]
TOP = REPO / "topics/padua-lanczos-drift-20261101"
RUN = Path("/workspace/padua-drift-runs/audit-03/E1")
CANDIDATE = "ea829d92d509f79326a1cc037844a1bac3b4de13"
RULE_HEAD = "c8849a89a601e0a56342d3d568086ab8abdbc4c0"
ENV = "PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 "
COMMANDS = {
    "replay-n4.json": ENV.replace("PYTHONDONTWRITEBYTECODE=1 ", "") + "python3 tracks/bivariate-lanczos/code/drift/e1_replay_n4.py --output " + str(RUN / "replay-n4.json"),
    "scalar-triangle.json": ENV + "python3 topics/padua-lanczos-drift-20261101/checks/audit-02/E1/reaudit.py scalar --set triangle --mode exact --output " + str(RUN / "scalar-triangle.json"),
    "scalar-rotated.json": ENV + "python3 topics/padua-lanczos-drift-20261101/checks/audit-02/E1/reaudit.py scalar --set rotated --mode arb --output " + str(RUN / "scalar-rotated.json"),
    "finite.json": ENV.replace("PYTHONDONTWRITEBYTECODE=1 ", "") + "python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --output " + str(RUN / "finite.json"),
    "finite-missing-regeneration.json": ENV.replace("PYTHONDONTWRITEBYTECODE=1 ", "") + "python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --regenerated " + str(RUN / "nonexistent") + " --output " + str(RUN / "finite-missing-regeneration.json"),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    raw = {name: read(RUN / name) for name in COMMANDS}
    ev = TOP / "evidence"
    old_replay = read(ev / "response-02-e1-replay-n4.json")
    old_scalar = read(ev / "audit-02-e1-checks.json")["checks"]
    cases = []
    for row in raw["replay-n4.json"]["cases"]:
        prior = next(p for p in old_replay["cases"] if (p["degree"], p["rule"]) == (row["degree"], row["rule"]))
        checks = {k: row[k] == prior[k] for k in ("points", "A_record01", "C_record03", "checks")}
        assert all(checks.values()) and row["pass"]
        receipt = row["audit02_receipt_comparison"]
        assert receipt["points_equal"] and receipt["A_record01_equal"]
        if row["degree"] == 3:
            assert receipt["C_record03_equal"]
        else:
            assert receipt["C_record03_in_receipt"] is False
        cases.append({"degree": row["degree"], "rule": row["rule"], "M": row["M"],
                      "point_seed": row["point_seed"], "partA_seed": row["partA_seed"], "partC_seed": row["partC_seed"],
                      "normal_derivative_equals_frozen_V": row["A_record01"]["normal_derivative_equals_frozen_V"],
                      "C_record03": row["C_record03"], "checks": row["checks"],
                      "equals_response02": checks, "audit02_comparison": receipt})
    scalar = {}
    for name in ("triangle", "rotated"):
        r = raw[f"scalar-{name}.json"]["result"]
        identical = r == old_scalar[f"scalar-{name}"]["result"]
        assert identical and all(r["checks"].values()) and r["ambiguous_signs"] == 0
        if name == "triangle":
            ratio = F(r["ratio"])
            extra = {"ratio_gt_800_squared": ratio > 800**2,
                     "ratio_between_657331_and_657332": 657331 < ratio < 657332}
        else:
            committed_ratio = F(next(x for x in read(ev / "e1-multinode-certificates.json")["comparisons"]
                                     if x["set"] == name)["squared_ratio_lower_exact"])
            extra = {"ratio_lower_gt_49": F(r["ratio"]["lower"]) > 49,
                     "ratio_upper_lt_100": F(r["ratio"]["upper"]) < 100,
                     "ratio_interval_contains_committed_exact_ratio": F(r["ratio"]["lower"]) <= committed_ratio <= F(r["ratio"]["upper"])}
        assert all(extra.values())
        scalar[name] = {"fresh_result": r, "equals_audit02_result": identical, "extra_exact_decisions": extra}
    f = raw["finite.json"]
    assert f["all_pass"] and all(s["pass"] for s in f["sets"])
    missing = raw["finite-missing-regeneration.json"]
    missing_checks = {"directory_absent": not (RUN / "nonexistent").exists(),
                      "all_four_expected_outputs_absent": len(missing["new_regeneration"]["files"]) == 4 and all(
                          r == {"exists": False} for r in missing["new_regeneration"]["files"].values()),
                      "incorrect_regeneration_pass": missing["new_regeneration"]["pass"],
                      "incorrect_all_pass": missing["all_pass"]}
    assert all(missing_checks.values())
    # Logical counterexample to the printed implication, not actual grid capacities.
    bj, alt, pivot = F(9), F(1), F(1, 10)
    reversal = {"illustrative_capacities_only": {"BJ": str(bj), "alt": str(alt), "pivot": str(pivot)},
                "printed_reversal_holds": bj**2 < 100 * alt**2,
                "min_target_still_holds": bj > 10 * min(alt, pivot)}
    assert reversal["printed_reversal_holds"] and reversal["min_target_still_holds"]
    paths = [
        "AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md", "state/IDEAS.md", "literature/INDEX.md",
        *["tracks/bivariate-lanczos/theory/" + p for p in (
            "drift-codex-e1-01-span-derivative.md", "drift-codex-e1-03-scalar-operation-bridge.md",
            "drift-codex-e1-04-finite-aggregate-separation.md", "drift-codex-e1-05-finite-scalar-cgs2-capacities.md",
            "drift-codex-e1-06-finite-scalar-cgs2-separation.md")],
        *["tracks/bivariate-lanczos/code/drift/" + p for p in (
            "e1_scalar_finite_check.py", "e1_replay_n4.py", "e1_cgs2.py", "e1_cgs2_multinode.py", "e1_exact.py")],
        "topics/padua-lanczos-drift-20261101/checks/audit-02/E1/reaudit.py",
        *["topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E1/" + p for p in (
            "first_principles.py", "ind_basis.py", "ind_aggregate.py", "ind_scalar.py")],
        *["topics/padua-lanczos-drift-20261101/evidence/" + p for p in (
            "e1-scalar-cgs2.json", "e1-multinode-certificates.json", "independent-scalar-01.json",
            "audit-02-e1-checks.json", "response-02-e1-replay-n4.json", "response-02-e1-scalar-finite.json")],
    ]
    inputs = []
    for p in paths:
        b = (REPO / p).read_bytes()
        pinned = subprocess.check_output(["git", "show", f"{CANDIDATE}:{p}"], cwd=REPO)
        assert b == pinned, p
        inputs.append({"path": p, "sha256": sha(b), "bytes": len(b), "equals_candidate": True})
    out = {
        "auditor": "Codex independent E1 audit-03 agent; requested/inherited gpt-6-astra xhigh; runtime resolved variant and effort unexposed",
        "candidate": CANDIDATE, "rules_head": RULE_HEAD, "receipt_generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "script_sha256": sha(Path(__file__).read_bytes()), "python": platform.python_version(),
        "environment": {"PYTHONPATH": "/workspace/padua-drift-runs/python-deps", "OPENBLAS_NUM_THREADS": "1",
                        "python_flint": raw["scalar-triangle.json"]["python_flint"], "mpmath": raw["replay-n4.json"]["mpmath"],
                        "Arb_bits": 512, "replay_decimal_digits": raw["replay-n4.json"]["mp_dps"]},
        "inputs": inputs,
        "executions": [{"command": command, "raw_output": str(RUN / name), "sha256": sha((RUN / name).read_bytes()),
                        "bytes": (RUN / name).stat().st_size, "exit_code": 0} for name, command in COMMANDS.items()],
        "raw_output_label_caveat": "Producer scripts hard-code Claude developer in checker/executor labels; these files were freshly executed by this Codex auditor. No developer execution is relabeled as an auditor run.",
        "scalar_reconstructions": scalar,
        "degree_replay": {"started_utc": raw["replay-n4.json"]["started_utc"], "finished_utc": raw["replay-n4.json"]["finished_utc"],
                          "elapsed_seconds": raw["replay-n4.json"]["elapsed_seconds_total"], "cases": cases, "all_pass": True},
        "finite_checker": {"all_pass": f["all_pass"], "sets": f["sets"]},
        "finding_missing_regeneration": {"checks": missing_checks, "observed": missing["new_regeneration"]},
        "finding_reversal_logic": reversal,
        "conclusion": {"finite_mathematics_pass": True, "degree4_replay_pass": True, "PARTIAL_target_supported": True,
                       "new_low_findings": 2, "new_medium_or_high_findings": 0},
        "retention": "Compact essential results committed here; raw working outputs are regenerable and not claimed as permanent cold storage. No external input required.",
    }
    target = ev / "audit-03-e1-checks.json"
    target.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({"output": str(target), "bytes": target.stat().st_size, "sha256": sha(target.read_bytes()), "all_mathematical_checks_pass": True, "low_findings": 2}))


if __name__ == "__main__":
    main()
