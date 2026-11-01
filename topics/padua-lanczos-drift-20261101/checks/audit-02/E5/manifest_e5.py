#!/usr/bin/env python3
"""Capture E5 audit-02 source identities, executed receipts and literal checks."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
TOPIC = Path("topics/padua-lanczos-drift-20261101")
THEORY = Path("tracks/bivariate-lanczos/theory")
CODE = Path("tracks/bivariate-lanczos/code/drift")
WORK = Path("/workspace/padua-drift-runs/reaudit-02/E5")
CANDIDATE = "cef79d66321a93d93d53e53efcb7e6744c387481"
OLD = "36c93794ce02f92c76c89e5a9ec8095eb238d91d"
MAIN = "28aaa20861d08074b77efc74eaef75cdcb36234d"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def ident(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


source_paths = [Path(x) for x in ("AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md",
                                "state/IDEAS.md", "literature/INDEX.md", "literature/records/blekherman-2012.md")]
source_paths += [TOPIC / x for x in ("handoffs/06-reaudit.md", "audit-01.md", "response-01.md",
                "checks/audit-01/E5-records-30-32.md", "checks/response-01/E5-developer-report.md",
                "checks/independent-math-01.md", "directions/E5.md", "ideas-e5.md",
                "proposed-record-changes.md", "report.md", "plan.md", "LOG.md",
                "local-results-entry.md", "evidence/response-01-e5-checks.json", "evidence/e5-exact-checks.json",
                "evidence/e5-manifest.json", "evidence/response-01-manifest.json")]
source_paths += [THEORY / name for name in (
    "drift-codex-e5-30-padua-positivity-radius-upper-bound.md",
    "drift-codex-e5-31-explicit-square-root-spread-family.md",
    "drift-codex-e5-32-failed-negative-witness-paths.md",
    "bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md",
    "bivariate-lanczos-claude-301-truncated-favard-sections.md",
    "bivariate-lanczos-claude-302-backward-reduction-moment-cone.md",
    "bivariate-lanczos-claude-303-moment-cone-rate-theorem.md",
    "bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md",
    "bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md",
    "bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md",
    "bivariate-lanczos-claude-N302-square-case-linear-rate-refuted.md")]
source_paths += [CODE / x for x in ("response01_e5_checks.py", "e5_exact_checks.py", "README.md")]
source_paths += [Path("topics/bivariate-lanczos-20261031/directions/L3/candidates.md")]
pins = {}
for path in source_paths:
    data = (ROOT / path).read_bytes()
    try:
        candidate = git("show", f"{CANDIDATE}:{path}")
    except subprocess.CalledProcessError:
        candidate = None  # Handoff06 was published immediately after candidate.
    pins[str(path)] = {**ident(data), "candidate_equal": candidate == data if candidate is not None else None,
                       "candidate_sha256": ident(candidate)["sha256"] if candidate is not None else None}

developer = json.loads((WORK / "response01-e5-rerun.json").read_text())
reference = json.loads((ROOT / TOPIC / "evidence/response-01-e5-checks.json").read_text())
differences = [k for k in sorted(set(developer) | set(reference)) if developer.get(k) != reference.get(k)]
old_run = json.loads((WORK / "e5-exact-rerun.json").read_text())
old_reference = json.loads((ROOT / TOPIC / "evidence/e5-exact-checks.json").read_text())
independent = json.loads((WORK / "independent-e5.json").read_text())

proposal = (ROOT / TOPIC / "proposed-record-changes.md").read_text()
blocks = list(re.finditer(r"OLD\n```text\n(.*?)\n```\s*NEW\n```text\n(.*?)\n```", proposal, re.S))
target = {
    "PD-T056": ("bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md", [2]),
    "PD-T075": ("bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md", [3, 4, 5, 8, 9, 10, 11]),
    "PD-T069": ("bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md", [12, 13]),
    "PD-T061_optional": ("bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md", [14]),
}
literal = {}
for key, (filename, ids) in target.items():
    path = THEORY / filename
    main_data = git("show", f"{MAIN}:{path}").decode()
    current = (ROOT / path).read_text()
    simulated = main_data
    checks = []
    for block_id in ids:
        match = blocks[block_id]
        old, new = match[1], match[2]
        count = simulated.count(old)
        checks.append({"proposal_line": proposal[:match.start()].count("\n") + 1,
                       "matches_main_before_any_replacement": main_data.count(old),
                       "matches_in_sequential_simulation": count})
        assert count == 1
        simulated = simulated.replace(old, new, 1)
    if key == "PD-T075":
        assert "(U2) stays OPEN" in simulated
        assert "(3) (U2) needs information" in simulated
        assert "Open questions: (U1) does ρ_n → 0" in simulated
    if key == "PD-T069":
        assert "A chosen radius may of course be taken nonincreasing in n." in simulated
        assert "(U2) of PD-T?…-319 remains OPEN" in simulated
    literal[key] = {"path": str(path), "current_equals_latest_main": current == main_data,
                    "blocks": checks, "simulated_result_identity": ident(simulated.encode()),
                    "simulation_only_no_source_write": True}

receipt_paths = ["response01-e5-rerun.json", "e5-exact-rerun.json", "independent-e5.json"]
scripts = [TOPIC / "checks/audit-02/E5/independent_e5.py", TOPIC / "checks/audit-02/E5/manifest_e5.py"]
commands = [
    "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/response01_e5_checks.py > /workspace/padua-drift-runs/reaudit-02/E5/response01-e5-rerun.json",
    "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py > /workspace/padua-drift-runs/reaudit-02/E5/e5-exact-rerun.json",
    "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B topics/padua-lanczos-drift-20261101/checks/audit-02/E5/independent_e5.py > /workspace/padua-drift-runs/reaudit-02/E5/independent-e5.json",
    "python3 -B topics/padua-lanczos-drift-20261101/checks/audit-02/E5/manifest_e5.py > topics/padua-lanczos-drift-20261101/evidence/audit-02-e5.json",
]
out = {
    "auditor": "Codex; requested gpt-6-astra xhigh; resolved runtime model/effort not independently exposed",
    "rules_read_sha": "2fd5456066de08094a35542f2ff6443c27d8c149",
    "rules_change_reread_sha": "7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b",
    "candidate_sha": CANDIDATE, "previous_candidate_sha": OLD,
    "latest_main_used_for_proposals": MAIN,
    "capture_head_sha": git("rev-parse", "HEAD").decode().strip(),
    "cwd": str(ROOT), "commands_actually_executed": commands,
    "exit_statuses": [0, 0, 0, 0], "randomness": "none",
    "source_files": pins,
    "audit_scripts": {str(p): ident((ROOT / p).read_bytes()) for p in scripts},
    "working_receipts": {str(WORK / p): ident((WORK / p).read_bytes()) for p in receipt_paths},
    "response_rerun": developer,
    "response_comparison": {"differing_keys": differences,
                              "scientific_fields_equal": set(differences) <= {"python", "elapsed_seconds"}},
    "old_exact_rerun": old_run, "old_exact_rerun_equals_committed_json": old_run == old_reference,
    "independent_checks": independent,
    "literal_proposal_checks": literal,
    "retention": "Compact necessary result/identity evidence committed here; raw receipts local, regenerable with listed commands; no cold-storage delivery claimed.",
    "limitations": "Symbolic checks corroborate the written analytic proof; numerical windows remain finite measurements. The one 384-bit Arb sign supplies a concrete finite counterexample to unqualified wording, not an all-n threshold.",
}
assert out["response_comparison"]["scientific_fields_equal"]
assert out["old_exact_rerun_equals_committed_json"]
assert independent["result"] == "PASS"
assert all(r["current_equals_latest_main"] for r in literal.values())
out["result"] = "PASS"
print(json.dumps(out, indent=2, sort_keys=True))
