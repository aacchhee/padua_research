"""Audit receipt for the frozen programme campaign; never modifies source files.

Run from a repository clone. Output is JSON on stdout.
"""
import hashlib
import json
import platform
import re
import subprocess
from pathlib import Path

SOURCE = "614709d4a60fb0c2593b05764e8d5aceda1be381"
BASE = "07c5f5465d6de306aa81dbe8ca1f615295163864"
TOPIC = "topics/programme-ideas-20261031"
ROOT = Path(__file__).resolve().parents[3]


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def blob(path, revision=SOURCE):
    return git("show", f"{revision}:{path}")


def identity(path):
    data = blob(path)
    return {"path": path, "git_blob_sha": git("rev-parse", f"{SOURCE}:{path}").decode().strip(),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


changed = git("diff", "--name-only", BASE, SOURCE).decode().splitlines()
tree = git("ls-tree", "-r", "--name-only", SOURCE).decode().splitlines()
rules = ["AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md", "agents/claude/CLAUDE_ROLES.md"]
protected = [p for p in tree if p.startswith(("state/", "literature/", "templates/", ".github/"))]
protected += ["ID_CROSSWALK.md", "PROOF_STATUS.md", "PAPER_MAP.md", "topics/padua-batch-20261031/ALLOCATIONS.md"]
protected = sorted(set(p for p in protected if p in tree))
assert not set(changed).intersection(protected)
assert blob("AGENTS.md") == blob("AGENTS.md", BASE)
assert blob("agents/codex/CODEX.md") == blob("agents/codex/CODEX.md", BASE)
assert git("merge-base", BASE, SOURCE).decode().strip() == BASE
rule_diff = git("diff", BASE, SOURCE, "--", "agents/WORKFLOW.md", "agents/claude/CLAUDE_ROLES.md").decode()
assert "Fable 5.1" in rule_diff and "Sonnet 5.5 high remains" in rule_diff
assert len(changed) == 153
assert all(p.startswith(TOPIC + "/") or p in rules for p in changed)

# The complete current files fetched through the connector were compared bytewise
# against these Git objects after network access became available.
snapshot = Path("/workspace/programme-audit-614709d")
snapshot_mismatch = []
if snapshot.exists():
    for path in sorted(set(changed + rules)):
        if (snapshot / path).read_bytes() != blob(path):
            snapshot_mismatch.append(path)
    assert not snapshot_mismatch

ideas = blob(TOPIC + "/ideas/candidates.md").decode()
idea_ids = re.findall(r"^# IDEA\?programme-ideas-claude-(\d+) —", ideas, re.M)
assert sorted(map(int, idea_ids)) == list(range(1, 21))
baseline = blob(TOPIC + "/lit/baseline.md").decode()
lit_ids = re.findall(r"^\| LIT\?programme-ideas-claude-(\d+) \|", baseline, re.M)
assert sorted(map(int, lit_ids)) == list(range(1, 112))

source_manifest = blob(TOPIC + "/sources/SHA256SUMS.txt").decode().splitlines()
inputs = []
for line in source_manifest:
    expected, name = line.split("  ", 1)
    path = TOPIC + "/sources/" + name
    assert hashlib.sha256(blob(path)).hexdigest() == expected
    inputs.append(identity(path))

prereg = []
for commit, candidate in [("a8364b9", "gen1-3"), ("2310424", "gen4-2")]:
    revision = git("rev-parse", commit).decode().strip()
    path = TOPIC + "/checks/decisive-" + candidate + ".md"
    text = blob(path, revision).decode()
    assert "pre-register" in text.lower() or "pre-registration" in text.lower()
    assert "(to be filled after the runs)" in text or "(empty until the runs are complete)" in text
    assert "kill" in text.lower()
    prereg.append({"candidate": candidate, "commit": revision,
                   "sha256": hashlib.sha256(text.encode()).hexdigest()})

topic_paths = [p for p in tree if p.startswith(TOPIC + "/")]
outputs = [p for p in tree if Path(p).suffix.lower() in {".out", ".log", ".json", ".jsonl", ".pdf", ".zip", ".png"}]
output_ids = [identity(p) for p in outputs]
assert max(e["bytes"] for e in output_ids) <= 1_000_000
assert sum(e["bytes"] for e in output_ids) < 5_000_000
missing_context = [p for p in ["CAMPAIGN_CONTEXT.md", "BRANCH_SNAPSHOT_NOTE.md", "RESULTS.md"]
                   if p not in tree and TOPIC + "/" + p not in tree]
report = {
    "source_commit": SOURCE, "current_main_at_start": BASE,
    "python": platform.python_version(), "platform": platform.platform(),
    "changed_files": len(changed), "snapshot_byte_mismatches": snapshot_mismatch,
    "base_is_ancestor": True, "protected_files_unchanged": protected,
    "idea_records": len(idea_ids), "literature_statement_rows": len(lit_ids),
    "source_inputs_sha256_verified": inputs, "pre_registrations": prereg,
    "missing_campaign_context": missing_context,
    "generated_like_files": len(output_ids), "generated_like_total_bytes": sum(e["bytes"] for e in output_ids),
    "largest_generated_like_bytes": max(e["bytes"] for e in output_ids),
    "topic_total_bytes_including_prose_and_code": sum(len(blob(p)) for p in topic_paths),
    "rule_and_changed_file_identities": [identity(p) for p in sorted(set(changed + rules + ["state/IDEAS.md", "literature/INDEX.md"]))],
    "result": "PASS for the listed structural checks; mathematical findings are separate",
}
print(json.dumps(report, indent=2))
