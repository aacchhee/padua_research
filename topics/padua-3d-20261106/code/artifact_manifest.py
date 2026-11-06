#!/usr/bin/env python3
"""Create or verify the topic's code/data identities; never pin prose."""
import argparse
import hashlib
import json
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def identity(path, base=TOP):
    raw = path.read_bytes()
    return {"path": path.relative_to(base).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def artifacts():
    return sorted([*TOP.joinpath("code").glob("*.py"),
                   *TOP.joinpath("evidence").glob("*.json")])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    target = TOP / "evidence-manifest.json"
    observed = [identity(path) for path in artifacts()]
    inherited = [identity(ROOT / "tracks/lattice-unisolvence/code" / name, ROOT)
                 for name in ("c3_lebesgue.py", "c3_rank.py")]
    if args.verify:
        saved = json.loads(target.read_text())
        if saved["artifacts"] != observed or saved.get("inherited_inputs") != inherited:
            raise SystemExit("FAIL: code/data set or identities changed")
        print(json.dumps({"verdict": "PASS", "artifacts": len(observed),
                          "bytes": sum(row["bytes"] for row in observed)}))
        return
    commands = []
    for path in sorted(TOP.joinpath("evidence").glob("*.json")):
        data = json.loads(path.read_text())
        command = data.get("command")
        if command is not None:
            commands.append({"receipt": path.relative_to(TOP).as_posix(),
                             "command_as_recorded": command})
    output = {
        "schema": "padua-3d-code-data-manifest-v1",
        "rules_input_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
        "generate": "python topics/padua-3d-20261106/code/artifact_manifest.py",
        "verify": "python topics/padua-3d-20261106/code/artifact_manifest.py --verify",
        "artifacts": observed,
        "inherited_inputs": inherited,
        "recorded_commands": commands,
        "limits": [
            "Identity verification is separate from mathematical verification.",
            "Prose is identified by audit commit, not acceptance hashes.",
            "Each receipt and attempt states its own executed scope and source inputs.",
            "Transient large catalogues are regeneration-only working outputs; see COLD_STORAGE.md.",
            "No archival delivery or independent Claude audit is implied."
        ]
    }
    raw = json.dumps(output, indent=2) + "\n"
    if len(raw.encode()) >= 16384:
        raw = json.dumps(output, separators=(",", ":"), ensure_ascii=False) + "\n"
    if len(raw.encode()) >= 16384:
        raise SystemExit("FAIL: compact manifest limit exceeded")
    target.write_text(raw)
    print(json.dumps({"manifest": str(target), "artifacts": len(observed),
                      "bytes": len(raw.encode())}))


if __name__ == "__main__":
    main()
