#!/usr/bin/env python3
"""Reproduce the handoff04 pinned full-file allocation union receipt."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

HEADS = {
    "main": "aff30e8ad5542c94fab642ae024dc9aab4fa7ad7",
    "PR21": "3ed6c94246f21353350f82712b6628b39db6f65a",
    "PR24": "60126006dcc7c814680ed87d4fef8d9f9404a3d7",
    "PR25": "3fe945e54a2666b8ec0004d90ec1dfa54ae80703",
    "PR26": "a930f32fbf4568fbc431ddcf0b0fd689f5fa8201",
}
PATTERNS = {
    "PD-T": r"PD-T(\d{3})\b", "PD-N": r"PD-N(\d{3})\b",
    "IDEA": r"IDEA-?(\d{3})\b", "LIT": r"LIT-?(\d{3})\b",
}
REGISTRIES = ["ID_CROSSWALK.md", "PROOF_STATUS.md", "literature/INDEX.md", "state/IDEAS.md"]
OWN = "topics/padua-mz-cleanup-20261105/ALLOCATIONS.md"
PUBLICATION = "ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90"


def git(*args):
    return subprocess.check_output(["git", *args])


def maxima(text, ledger):
    result = {ns: max(map(int, re.findall(pat, text)), default=0)
              for ns, pat in PATTERNS.items()}
    if ledger:
        for line in text.splitlines():
            cells = [c.strip().strip("*") for c in line.split("|")]
            if len(cells) > 2 and cells[1] in PATTERNS:
                values = [int(n) for n in re.findall(r"(?<!\d)\d{3}(?!\d)", cells[2])]
                result[cells[1]] = max([result[cells[1]], *values])
    return result


def main():
    # Every required copy is read in full, even if its blob was already seen.
    contents, files, by_head, bulk = {}, [], {}, []
    union = {ns: 0 for ns in PATTERNS}
    foreign = union.copy()
    for label, head in HEADS.items():
        paths = git("ls-tree", "-r", "--name-only", head).decode().splitlines()
        paths = [p for p in paths if p.endswith("ALLOCATIONS.md") or p in REGISTRIES]
        assert set(REGISTRIES) <= set(paths)
        by_head[label] = []
        for path in paths:
            data = git("show", head + ":" + path)
            blob = git("rev-parse", head + ":" + path).decode().strip()
            text = data.decode()
            mx = maxima(text, path.endswith("ALLOCATIONS.md"))
            if blob not in contents:
                contents[blob] = {"sha256": hashlib.sha256(data).hexdigest(),
                                  "bytes": len(data), "lines": len(text.splitlines()),
                                  "maxima": mx}
            row = [path, blob]
            if row not in files:
                files.append(row)
            by_head[label].append(files.index(row))
            bulk.append({"head": head, "path": path, "blob": blob, **contents[blob]})
            for ns in PATTERNS:
                union[ns] = max(union[ns], mx[ns])
                if path != OWN:
                    foreign[ns] = max(foreign[ns], mx[ns])
    assert union == {"PD-T": 391, "PD-N": 145, "IDEA": 489, "LIT": 597}
    assert foreign == {"PD-T": 375, "PD-N": 137, "IDEA": 465, "LIT": 597}
    for path in REGISTRIES:
        assert len({blob for p, blob in files if p == path}) == 1
    added = git("log", "--format=%H", "--diff-filter=A", HEADS["PR26"], "--", OWN).decode().splitlines()
    assert added == [PUBLICATION]
    first = git("show", PUBLICATION + ":" + OWN).decode()
    current = git("show", HEADS["PR26"] + ":" + OWN).decode()
    reservation = ["| PD-T | PD-T376–PD-T391 | 16 |", "| PD-N | PD-N138–PD-N145 | 8 |",
                   "| IDEA | IDEA-466–IDEA-489 | 24 |", "| LIT | no range | 0 |"]
    assert all(line in first and line in current for line in reservation)
    temp = Path("/tmp/mz-prep-allocation")
    temp.mkdir(exist_ok=True)
    inventory = json.dumps(bulk, sort_keys=True, separators=(",", ":")).encode() + b"\n"
    (temp / "full-inventory.json").write_bytes(inventory)
    report = {
        "date": "2026-11-05", "rules_sha": HEADS["PR26"],
        "worker": "Codex gpt-6.1-sol xhigh (inherited actual model)",
        "scope": "Administrative allocation check only; no science, novelty, reservation or assignment changes.",
        "heads": HEADS,
        "population": {"open_prs": [21, 24, 25, 26], "closed_unmerged": [],
                       "source": "Parent orchestrator live GitHub queries and fetched pins; not independently re-queried by this worker.",
                       "argmax_phase2": "PR25; no separate additional branch supplied by parent"},
        "method": "Read complete bytes of every ALLOCATIONS.md and four canonical registries at every pin. Scan all qualified three-digit namespace tokens and namespace-table bare ranges; manually review complete unique ledgers, including inherited history/permanent gaps/retired records. Foreign four-digit BTTB LIT aliases excluded. Next-free history is not a new reservation; conservative mention maxima agree with actual upper reserved bounds.",
        "copies_read": len(bulk), "distinct_blobs": len(contents),
        "files_columns": ["path", "git_blob"], "files": files,
        "head_file_indices": by_head, "blobs": contents,
        "canonical_registry_blobs_identical_across_all_heads": True,
        "union_maxima": union, "union_excluding_cleanup_maxima": foreign,
        "cleanup": {"reservation": {"PD-T": [376, 391], "PD-N": [138, 145], "IDEA": [466, 489], "LIT": None},
                    "first_published_commit": PUBLICATION, "pr": 26,
                    "priority_check": "Git addition commit and original/current range rows match; pushed-publication/PR locator attested in current ledger.",
                    "conflicts": [], "result": "PASS",
                    "eligible_assignment_only": {"PD-T": [376, 381], "IDEA": [466, 471]},
                    "not_assigned_by_scan": True},
        "bulk_inventory": {"path": str(temp / "full-inventory.json"), "bytes": len(inventory),
                           "sha256": hashlib.sha256(inventory).hexdigest(),
                           "retention": "Local temporary convenience only; complete durable source inventory is represented above by pinned Git heads, paths and blob identities. Regenerate with this script."},
    }
    output = Path(__file__).with_name("allocation-scan.json")
    encoded = json.dumps(report, separators=(",", ":")).encode() + b"\n"
    assert len(encoded) < 16384
    output.write_bytes(encoded)
    print(json.dumps({"result": "PASS", "copies": len(bulk), "blobs": len(contents),
                      "maxima": union, "foreign_maxima": foreign, "receipt_bytes": len(encoded)}))


if __name__ == "__main__":
    main()
