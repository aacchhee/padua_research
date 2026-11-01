"""Independent audit-02 source and registration identity checks; no Git mutations."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

SHA = "cadb35066160e466cb1704b9791ad6f374446422"
ROOT = Path(__file__).resolve().parents[3]
TOPIC = "topics/programme-ideas-20261031/"
INPUTS = TOPIC + "sources/campaign-inputs/"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def source(path):
    return git("show", SHA + ":" + path)

manifest = json.loads(source(INPUTS + "provenance.json"))
sources = []
for row in manifest["rows"]:
    b = git("cat-file", "blob", row["git_blob"])
    assert len(b) == row["bytes"]
    assert hashlib.sha256(b).hexdigest() == row["sha256"]
    exact = []
    for h in row["repo_history"]:
        proc = subprocess.run(["git", "rev-parse", h["commit"] + ":" + h["path"]],
                              cwd=ROOT, capture_output=True, text=True)
        if proc.returncode == 0 and proc.stdout.strip() == row["git_blob"]:
            exact.append({"commit": h["commit"], "path": h["path"]})
    if row["repo_history"]:
        assert exact, row["snapshot"]
    else:
        assert source(INPUTS + row["snapshot"]) == b
    sources.append({"snapshot": row["snapshot"], "git_blob": row["git_blob"],
                    "sha256": row["sha256"], "bytes": len(b),
                    "exact_commit_path": exact[-1] if exact else None,
                    "committed_input": not bool(row["repo_history"])})

hash_checks = []
for line in source(INPUTS + "SHA256SUMS.txt").decode().splitlines():
    wanted, path = line.split("  ", 1)
    actual = hashlib.sha256(source(INPUTS + path)).hexdigest()
    assert wanted == actual
    hash_checks.append({"path": path, "sha256": actual})

proof = source("PROOF_STATUS.md").decode()
crosswalk = source("ID_CROSSWALK.md").decode()
state = source("state/IDEAS.md").decode()
ideas = source(TOPIC + "ideas/candidates.md").decode()
baseline = source(TOPIC + "lit/baseline.md").decode()
allpaths = git("ls-tree", "-r", "--name-only", SHA).decode().splitlines()
theories = [p for p in allpaths if p.startswith(TOPIC + "theory/") and p.endswith(".md")]
records = []
for p in theories:
    text = source(p).decode()
    rid = re.search(r"^# (PD-[TN]\?programme-ideas-claude-[N]?\d+)", text)[1]
    status = re.search(r"^Overall status: (PROVED|MEASURED|OPEN|CONDITIONAL|PARTIAL)", text, re.M)[1]
    prows = [l for l in proof.splitlines() if l.startswith("| " + rid + " |")]
    crows = [l for l in crosswalk.splitlines() if l.startswith("| " + rid + " |")]
    assert len(prows) == len(crows) == 1, rid
    assert prows[0].split("|")[3].strip() == status, rid
    assert "(" + p + ")" in prows[0] and "(" + p + ")" in crows[0], rid
    records.append({"id": rid, "status": status, "path": p,
                    "sha256": hashlib.sha256(text.encode()).hexdigest()})

idea_ids = re.findall(r"^# IDEA\?programme-ideas-claude-(\d+) —", ideas, re.M)
state_ids = re.findall(r"^\| IDEA\?programme-ideas-claude-(\d+);", state, re.M)
assert len(idea_ids) == len(set(idea_ids)) == len(state_ids) == len(set(state_ids)) == 20
assert set(idea_ids) == set(state_ids)
litrows = [l for l in baseline.splitlines() if re.match(r"\| LIT\?programme-ideas-claude-\d+ \|", l)]
assert len(litrows) == 111
assert len(theories) == 11
assert len(sources) == 164
assert sum(bool(r["exact_commit_path"]) for r in sources) == 159

print(json.dumps({
    "candidate_sha": SHA,
    "auditor_model_effort_requested": "gpt-6-astra xhigh; runtime metadata unexposed",
    "command": "python topics/programme-ideas-20261031/audit-02-support/literature-check.py",
    "scope": "Byte identity, exact Git retrieval and registry/status consistency; not independent proof validation or Windows archive retrieval.",
    "source_count": len(sources), "git_history_sources_verified": 159,
    "committed_context_inputs_verified": 5, "source_rows": sources,
    "input_hash_checks": hash_checks, "theory_records": records,
    "idea_records": 20, "shared_idea_rows": 20, "literature_rows": 111,
    "windows_archive": "Manifest reviewed only; not independently retrieved or rehashed.",
    "original_reading_history": "Content identity verified, not original agent execution or reading attested.",
}, indent=2, ensure_ascii=False))
