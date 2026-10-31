"""Check audit-response identities and registry integration; not a math proof."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDITED = "fdf0648cbaa9fb722c611d709e638de7dfe86368"
DELIVERY = "6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994"
MAIN = "08fafe62d9798385dfafaacc9a41344272737e68"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read(name: str) -> str:
    return (ROOT / name).read_text()


def check(require_targets: bool) -> dict:
    mapping = json.loads(read("topics/mz-constants/final-id-map.json"))
    original = json.loads(git("show", AUDITED + ":topics/mz-constants/final-id-map.json"))
    assert len(original["mappings"]) == 65
    assert all(mapping["mappings"][k] == v for k, v in original["mappings"].items())
    assert len(mapping["mappings"]) == len(set(mapping["mappings"].values())) == 70
    additions = set(mapping["mappings"]) - set(original["mappings"])
    assert {mapping["mappings"][k] for k in additions} == {f"LIT-{i:03}" for i in range(61, 66)}
    for old, final in mapping["mappings"].items():
        text = read(mapping["canonical"][old]["path"])
        assert re.search(r"^#{1,6} " + re.escape(final) + r"\b", text, re.M), final

    registry = read("PROOF_STATUS.md")
    rows = {m.group(1): m.group(0) for m in re.finditer(r"^\| (PD-[TN]\d{3}) \|[^\n]+", registry, re.M)}
    all_row_ids = re.findall(r"^\| (PD-[TN]\d{3}) \|", registry, re.M)
    expected = {f"PD-T{i:03}" for i in range(1, 29)} | {f"PD-N{i:03}" for i in range(1, 7)}
    assert set(rows) == expected and len(all_row_ids) == len(rows) == 34
    for p in (ROOT / "tracks/mz-constants/theory").glob("*.md"):
        text = p.read_text()
        rid = text.splitlines()[0].split()[1]
        status = re.search(r"Overall status:\s*(?:\*\*)?(PROVED|PARTIAL|CONDITIONAL|MEASURED|OPEN)", text).group(1)
        before = git("show", AUDITED + ":" + str(p.relative_to(ROOT))).decode()
        assert re.search(r"Overall status:\s*(?:\*\*)?" + status + r"\b", before)
        assert f"| {status} |" in rows[rid]
        assert "explicit local dependencies in file" not in rows[rid]
        assert "exact statement in canonical theory" not in rows[rid]
    for rid, idea, reason in [("PD-N002", 60, "refuted"), ("PD-N003", 61, "failed"),
                             ("PD-N004", 68, "refuted"), ("PD-N005", 69, "failed"),
                             ("PD-N006", 70, "failed")]:
        assert f"IDEA-{idea:03} REJECTED: {reason}" in rows[rid]
        assert f"[{rid}](" in rows[rid]
    policy = git("show", "d367228:PROOF_STATUS.md").decode()
    policy = policy[policy.index("Use repository-global IDs"):policy.index("| ID |")]
    assert policy in registry

    idea_text = read("state/IDEAS.md")
    current = idea_text.split("## Current MZ dispositions", 1)[1]
    ids = re.findall(r"^\| (IDEA-\d{3}) \|", current, re.M)
    assert len(ids) == len(set(ids)) == 25
    assert set(ids) == {f"IDEA-{i:03}" for i in range(52, 77)}
    literature = re.findall(r"^\| (LIT-\d{3}) \|", read("literature/INDEX.md"), re.M)
    assert len(literature) == len(set(literature)) == 65

    preserved = git("ls-tree", "-r", "--name-only", MAIN, "tracks/unisolvence", "topics/charter-unisolvence-20261031").decode().splitlines()
    for name in preserved:
        assert (ROOT / name).read_bytes() == git("show", MAIN + ":" + name), name
    charter_rows = 0
    for name in ["PROOF_STATUS.md", "literature/INDEX.md"]:
        for line in git("show", MAIN + ":" + name).decode().splitlines():
            if re.match(r"^\| (?:PD-[TN]\d{3}|LIT-\d{3}) \|", line):
                assert line in read(name), line
                charter_rows += 1
    assert charter_rows == 54
    assert not git("diff", MAIN, "--name-only", "--", "AGENTS.md", "agents", "templates", ".github").strip()

    receipt = json.loads(read("topics/mz-constants/ledger-reconciliation-01.json"))
    ledger = (ROOT / "topics/padua-batch-20261031/ALLOCATIONS.md").read_bytes()
    assert digest(ledger) == receipt["ledger_sha256"]
    for member in receipt["members"]:
        ref = "origin/" + member["branch"]
        assert git("show", ref + ":topics/padua-batch-20261031/ALLOCATIONS.md") == ledger
        commit = member["published_ledger_commit"]
        paths = git("diff", commit + "^", commit, "--name-only").decode().splitlines()
        assert paths == ["topics/padua-batch-20261031/ALLOCATIONS.md"]

    audit_files = ["topics/mz-constants/audit-01.md",
                   "tracks/mz-constants/evidence/claude-audit-01-check.py",
                   "tracks/mz-constants/evidence/claude-audit-01-check.json"]
    for name in audit_files:
        assert (ROOT / name).read_bytes() == git("show", DELIVERY + ":" + name)
    historical = json.loads(read("topics/mz-constants/audit-targets.json"))
    for item in historical["files"]:
        before = git("show", AUDITED + ":" + item["path"])
        assert digest(before) == item["sha256"] and len(before) == item["bytes"]
    unchanged = git("ls-tree", "-r", "--name-only", AUDITED,
                    "topics/mz-constants/sources", "tracks/mz-constants/code").decode().splitlines()
    for name in unchanged:
        assert (ROOT / name).read_bytes() == git("show", AUDITED + ":" + name), name

    src = ROOT / "topics/mz-constants/sources/padua_mz_inputs"
    verified, unavailable = [], []
    for line in (src / "SHA256SUMS.txt").read_text().splitlines():
        h, name = line.split("  ", 1)
        p = src / name
        if p.exists():
            assert digest(p.read_bytes()) == h, name
            verified.append(name)
        else:
            assert not name.startswith("./code/"), name
            unavailable.append(name)

    manifest_path = ROOT / "topics/mz-constants/response-01-targets.json"
    checked_targets = 0
    if manifest_path.exists():
        for item in json.loads(manifest_path.read_text())["files"]:
            p = ROOT / item["path"]
            assert digest(p.read_bytes()) == item["sha256"] and p.stat().st_size == item["bytes"], item["path"]
            checked_targets += 1
    elif require_targets:
        raise AssertionError("Final response manifest is required")

    public_names = set(git("ls-files", "--cached", "--others", "--exclude-standard").decode().splitlines())
    public = [ROOT / n for n in public_names if (ROOT / n).is_file()]
    assert not any(p.suffix.lower() == ".pdf" for p in public)
    assert max(p.stat().st_size for p in public) < 1_000_000
    assert sum(p.stat().st_size for p in public) < 5_000_000
    return {"result": "PASS", "head": git("rev-parse", "HEAD").decode().strip(),
            "checker_sha256": digest(Path(__file__).read_bytes()), "unchanged_original_mappings": 65,
            "current_mz_mappings": 70, "combined_result_rows": len(rows),
            "combined_literature_rows": len(literature), "current_mz_idea_dispositions": len(ids),
            "preserved_charter_files": len(preserved), "preserved_charter_registry_rows": charter_rows,
            "historical_audit_targets_verified": len(historical["files"]),
            "current_response_targets_verified": checked_targets,
            "unchanged_producer_source_files": len(unchanged), "verified_source_payloads": len(verified),
            "original_upload_payloads_unavailable": unavailable, "ledger_blob": receipt["ledger_git_blob"],
            "propagated_member_heads": [m["published_ledger_commit"] for m in receipt["members"]],
            "public_bytes_conservative": sum(p.stat().st_size for p in public),
            "limit": "Identity, metadata and integration checks only; no numerical extrapolation or novelty proof."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--require-targets", action="store_true")
    args = parser.parse_args()
    result = check(args.require_targets)
    data = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end="")
