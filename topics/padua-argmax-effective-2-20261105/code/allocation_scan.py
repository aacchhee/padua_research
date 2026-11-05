#!/usr/bin/env python3
"""Reproduce the pinned complete-file allocation inventory; never reserves IDs.

Ledger endpoint maxima below are the separate human full-ledger review, not
the result of treating every numeric mention (e.g. next-free prose) as reserved.
PR population classification is supplied by the orchestrator's live API scan.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]
SOURCES = {
    "origin/main": "21dbfc90257b952d8923f6d01739d12aa8d6e0a1",
    "PR21": "890f56ccde35431b70b43141c224b0b8817fea7f",
    "PR22": "1de5891ee622e826d7553819152aa261b02faaa9",
    "PR24": "79c3d6a211325eca6e8311b3ae03187c100a1d8a",
}
REGISTRIES = ["PROOF_STATUS.md", "state/IDEAS.md", "literature/INDEX.md", "ID_CROSSWALK.md"]
PATTERNS = {"PD-T": r"PD-T(\d+)", "PD-N": r"PD-N(\d+)",
            "IDEA": r"IDEA-(\d+)", "LIT": r"LIT-(\d+)"}
FOREIGN_LIT = {1160, 1185, 1317, 1325, 1586, 1658, 1729, 1750}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    blobs = []
    blob_index = {}
    snapshots = {}
    registry_max = {ns: 0 for ns in PATTERNS}
    files_read = 0
    for label, sha in SOURCES.items():
        paths = sorted(p for p in git("ls-tree", "-r", "--name-only", sha).decode().splitlines()
                       if p.endswith("/ALLOCATIONS.md")) + REGISTRIES
        snapshot = []
        for path in paths:
            raw = git("show", f"{sha}:{path}")
            text = raw.decode("utf-8")
            digest = hashlib.sha256(raw).hexdigest()
            key = (path, digest)
            if key not in blob_index:
                blob_index[key] = len(blobs)
                blobs.append({"path": path, "sha256": digest, "bytes": len(raw)})
            snapshot.append(blob_index[key])
            files_read += 1
            if path in REGISTRIES:
                for ns, pattern in PATTERNS.items():
                    numbers = [int(m) for m in re.findall(pattern, text)]
                    if ns == "LIT":
                        # These exact aliases were context-reviewed as foreign BTTB IDs.
                        numbers = [n for n in numbers if n not in FOREIGN_LIT]
                    registry_max[ns] = max([registry_max[ns], *numbers])
        snapshots[label] = {"sha": sha, "files": snapshot}
    result = {
        "schema": "padua-allocation-scan-v1", "date_utc": "2026-11-05",
        "purpose": "Review only; no reservation or final-ID assignment",
        "rules_sha": "2fb2f7502bb8d1b46c0fe1089588c46a06df258d",
        "pr_population": {"source": "orchestrator live GitHub connector all-state scan",
                          "open": [21, 22, 24], "closed_merged_count": 21,
                          "closed_unmerged": []},
        "snapshots": snapshots, "files_read": files_read, "blobs": blobs,
        "registry_qualified_mention_max": registry_max,
        "human_reviewed_reserved_max": {"PD-T": 363, "PD-N": 131, "IDEA": 453, "LIT": 593},
        "suggested_only": {"PD-T": [364, 375], "PD-N": [132, 137],
                           "IDEA": [454, 465], "LIT": [594, 597]},
        "qualifications": [
            "Every complete ledger version reviewed; shared copies reconstructed by exact diff against the fully read main ledger.",
            "Namespace-column numeric ranges and abbreviated namespace/range endpoints reviewed manually.",
            "Permanent unused headroom and retired-reservation prose included; no closed-unmerged PR reported by parent scan.",
            "Explicit provisional IDs are not final IDs; old next-unreserved prose does not itself reserve a range.",
            "Foreign BTTB literature aliases excluded after context review: " + ",".join(map(str, sorted(FOREIGN_LIT))),
            "Scientific registries read completely by scanner for ID inventory; no novelty or mathematical audit is claimed.",
            "Pinned snapshot only; orchestrator must refresh population and heads immediately before publishing a reservation.",
        ],
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if len(encoded.encode()) >= 16384:
        raise RuntimeError("Receipt exceeds 16 KiB")
    output = TOPIC / "allocation-scan.json"
    output.write_text(encoded)
    print(json.dumps({"output": str(output), "bytes": len(encoded.encode()),
                      "files_read": files_read, "unique_file_versions": len(blobs),
                      "registry_max": registry_max}))


if __name__ == "__main__":
    main()
