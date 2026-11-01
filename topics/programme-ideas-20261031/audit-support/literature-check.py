"""Bounded source/retention checks for audit of pinned programme campaign.

No mathematical experiments or source verification is inferred from this script.
Read-only Git operations inspect the full clone supplied by the root orchestrator.
"""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "topics/programme-ideas-20261031"
CLONE = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/programme-integration")
SHA = "614709d4a60fb0c2593b05764e8d5aceda1be381"
DRAFT_SHA = "25161235fe430ec05723796afe0f20a923a69ebd"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=CLONE, text=True)

baseline = (TOPIC / "lit/baseline.md").read_text()
rows = [l for l in baseline.splitlines() if re.match(r"\| LIT\?programme-ideas-claude-\d+ \|", l)]
ids = [int(re.search(r"claude-(\d+)", l)[1]) for l in rows]
verified = [i for i, l in zip(ids, rows) if re.search(r"\| VERIFIED", l)]
ideas = (TOPIC / "ideas/candidates.md").read_text()
heads = re.findall(r"^# IDEA\?programme-ideas-claude-(\d+) — (.+)", ideas, re.M)
paths = git("ls-tree", "-r", "--name-only", DRAFT_SHA,
            "topics/programme-ideas-20261031/checks/state").splitlines()
drafts = []
for p in paths:
    content = git("show", DRAFT_SHA + ":" + p)
    drafts.append({"path": p, "title": next(l[2:] for l in content.splitlines() if l.startswith("# ")),
                   "status": re.search(r"Status:\s*([^\n]+)", content)[1],
                   "sha256": hashlib.sha256(content.encode()).hexdigest()})
source_checks = []
for line in (TOPIC / "sources/SHA256SUMS.txt").read_text().splitlines():
    wanted, path = line.split("  ", 1)
    b = (TOPIC / "sources" / path).read_bytes()
    source_checks.append({"path": path, "sha256": hashlib.sha256(b).hexdigest(),
                          "manifest_matches": hashlib.sha256(b).hexdigest() == wanted})
topic_paths = git("ls-tree", "-r", "--name-only", SHA).splitlines()
inputs = ["CAMPAIGN_CONTEXT.md", "BRANCH_SNAPSHOT_NOTE.md", "RESULTS.md", "MAP.txt"]
inputs_present = {p: [x for x in topic_paths if x == p or x.endswith("/" + p)] for p in inputs}
result = {
    "candidate_sha": SHA, "draft_sha": DRAFT_SHA,
    "commands": ["python topics/programme-ideas-20261031/audit-support/literature-check.py /workspace/programme-integration",
                 "git ls-tree -r --name-only " + DRAFT_SHA + " topics/programme-ideas-20261031/checks/state",
                 "git show <draft-sha>:<each-of-the-20-draft-paths>",
                 "git ls-tree -r --name-only " + SHA],
    "literature_rows": len(rows), "unique_lit_ids": len(set(ids)),
    "missing_lit_ids": sorted(set(range(1, 112)) - set(ids)),
    "verified_row_labels": verified, "verified_count": len(verified),
    "unverified_count": len(rows) - len(verified),
    "idea_headings": len(heads), "unique_idea_ids": len(set(i for i, _ in heads)),
    "missing_idea_ids": sorted(set(range(1, 21)) - {int(i) for i, _ in heads}),
    "draft_count": len(drafts),
    "draft_status_counts": dict(collections.Counter("not returned" if d["status"].startswith("not returned") else "returned" for d in drafts)),
    "drafts": drafts, "source_hash_checks": source_checks,
    "unrecorded_input_paths_at_candidate": inputs_present,
    "scope": "Record-count and byte-identity checks only; no independent mathematical result or exhaustive novelty review."
}
print(json.dumps(result, indent=2, ensure_ascii=False))
assert len(rows) == len(set(ids)) == 111 and set(ids) == set(range(1, 112))
assert len(heads) == len(set(i for i, _ in heads)) == 20
assert len(drafts) == 20
assert result["draft_status_counts"] == {"returned": 12, "not returned": 8}
assert all(c["manifest_matches"] for c in source_checks)
