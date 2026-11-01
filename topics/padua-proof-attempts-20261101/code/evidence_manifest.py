"""Print reproducibility identities; never modifies scientific inputs.

Run from any directory after the topic evidence is complete. The manifest itself
and mutable administrative LOG are excluded to avoid self-reference. This is a
provenance/size check, not a mathematical checker or independent audit.
"""
import hashlib
import json
import platform
import subprocess
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
BASE = "cadb35066160e466cb1704b9791ad6f374446422"
SOURCE = "topics/programme-ideas-20261031/"
INPUTS = [
    "AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md",
    "state/IDEAS.md", "literature/INDEX.md", "templates/TOPIC_LOG.md",
    "templates/THEORY.md", "templates/COLD_STORAGE.md",
    SOURCE + "OPEN_TARGETS.md", SOURCE + "audit-01.md",
    SOURCE + "audit-support/proposal-review.md",
    SOURCE + "checks/decisive-gen4-2.md",
    SOURCE + "theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md",
    SOURCE + "theory/programme-ideas-claude-04-padua-corner-expansion.md",
    SOURCE + "theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md",
    SOURCE + "theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md",
    SOURCE + "checks/code/decisive/gen4-2/t2_onepage.py",
    SOURCE + "checks/code/decisive/gen4-2/leb_common.py",
    SOURCE + "checks/code/decisive/gen4-2/t3_certify.py",
    SOURCE + "checks/code/decisive/gen4-2/t3_degenerate.py",
    SOURCE + "checks/code/decisive/gen4-2/t3_maxima.json",
    SOURCE + "checks/code/decisive/gen4-2/t3_certify.log",
    SOURCE + "checks/code/gen4/gen4_tests.py",
    SOURCE + "checks/code/adv/M2/m2_common.py",
    SOURCE + "checks/code/adv/M2/m2_favard_commutant.py",
    SOURCE + "checks/code/response-02/padua_pattern_commutant.py",
    SOURCE + "checks/code/response-02/padua_n3_edge_identity.py",
    SOURCE + "ideas/candidates.md",
    SOURCE + "theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md",
    SOURCE + "checks/adversarial-gen1-3.md",
    "tracks/mz-constants/theory/m2-l1-obstruction.md",
]


def identity(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


if __name__ == "__main__":
    inputs = []
    for name in INPUTS:
        item = identity(ROOT / name)
        expected = subprocess.check_output(
            ["git", "show", BASE + ":" + name], cwd=ROOT)
        assert hashlib.sha256(expected).hexdigest() == item["sha256"], name
        item["base_git_blob"] = subprocess.check_output(
            ["git", "rev-parse", BASE + ":" + name], cwd=ROOT, text=True).strip()
        inputs.append(item)
    files = [p for p in TOPIC.rglob("*") if p.is_file()
             and "__pycache__" not in p.parts
             and p.name not in {"evidence-manifest.json", "LOG.md"}]
    artifacts = [identity(p) for p in sorted(files)]
    outputs = [a for a in artifacts if "/outputs/" in a["path"]]
    assert all(a["bytes"] <= 1_000_000 for a in outputs)
    assert sum(a["bytes"] for a in outputs) <= 5_000_000
    print(json.dumps({"rules_and_base": BASE, "python": platform.python_version(),
                      "input_identity_check": "all current bytes match pinned base",
                      "inputs": inputs, "topic_artifacts": artifacts,
                      "generated_output_bytes": sum(a["bytes"] for a in outputs),
                      "limitations": "No external Windows delivery or Claude audit attested."},
                     indent=2))
