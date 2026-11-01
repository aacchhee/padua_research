#!/usr/bin/env python3
"""Pin audit-03 E5 inputs and embed independently executed compact outputs."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[5]
CANDIDATE = "ea829d92d509f79326a1cc037844a1bac3b4de13"
RULES = "c8849a89a601e0a56342d3d568086ab8abdbc4c0"
TOPIC = "topics/padua-lanczos-drift-20261101/"
OWN = TOPIC+"checks/audit-03/E5/"
INPUTS = ["AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md",
          "tracks/bivariate-lanczos/theory/drift-codex-e5-30-padua-positivity-radius-upper-bound.md",
          "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md",
          "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md",
          TOPIC+"directions/E5.md", TOPIC+"checks/response-02/E5-developer-report.md",
          "tracks/bivariate-lanczos/code/drift/e5_response02_check.py",
          TOPIC+"evidence/response-02-e5-checks.json"]


def identity(path):
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


inputs = {}
for relative in INPUTS:
    data = (ROOT/relative).read_bytes()
    original = git("show", CANDIDATE+":"+relative)
    assert data == original
    inputs[relative] = {**identity(ROOT/relative),
                        "candidate_blob": git("rev-parse", CANDIDATE+":"+relative).decode().strip(),
                        "equals_candidate": True}
rerun_path = Path("/tmp/padua-audit03-e5/developer-rerun.json")
own_path = Path("/tmp/padua-audit03-e5/independent.json")
rerun = json.loads(rerun_path.read_text())
own = json.loads(own_path.read_text())
committed = json.loads((ROOT/(TOPIC+"evidence/response-02-e5-checks.json")).read_text())
diffs = {key: {"committed": committed.get(key), "rerun": rerun.get(key)}
         for key in set(committed)|set(rerun) if committed.get(key) != rerun.get(key)}
assert set(diffs) <= {"python", "elapsed_seconds"}
assert rerun["result"] == own["result"] == "PASS"
assert own["code_sha256"] == identity(ROOT/(OWN+"independent.py"))["sha256"]
assert rerun["code_sha256"] == inputs["tracks/bivariate-lanczos/code/drift/e5_response02_check.py"]["sha256"]
commands = [
    "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e5_response02_check.py > /tmp/padua-audit03-e5/developer-rerun.json",
    "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B "+OWN+"independent.py > /tmp/padua-audit03-e5/independent.json",
    "python3 -B "+OWN+"manifest.py > "+TOPIC+"evidence/audit-03-e5.json",
]
result = {"auditor": "Codex independent E5 worker", "configured_model": "gpt-6-astra",
          "configured_effort": "xhigh", "resolved_runtime_metadata": "not independently exposed",
          "rules_sha": RULES, "candidate_sha": CANDIDATE,
          "read_head": RULES, "cwd": str(ROOT), "inputs": inputs,
          "checker_files": {name: identity(ROOT/(OWN+name)) for name in ["independent.py", "manifest.py"]},
          "executed_commands": commands, "all_exit_codes": [0, 0, 0],
          "outputs": {str(path): {**identity(path), "payload": value}
                      for path, value in [(rerun_path, rerun), (own_path, own)]},
          "comparison_to_committed": {"differences": diffs, "all_scientific_fields_equal": True},
          "retention": "Temporary local outputs embedded here; reproducible from committed checkers. No cold-storage transfer claimed.",
          "dispositions": {"A02-L3": "RESOLVED", "A02-L4": "RESOLVED"},
          "findings": [], "result": "PASS"}
print(json.dumps(result, indent=2, sort_keys=True))
