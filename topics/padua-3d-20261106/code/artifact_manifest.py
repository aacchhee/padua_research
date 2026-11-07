#!/usr/bin/env python3
"""Create or verify the topic's code/data identities; never pin prose."""
import argparse
import base64
import hashlib
import json
import zlib
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def identity(path, base=TOP):
    raw = path.read_bytes()
    return {"path": path.relative_to(base).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def artifacts():
    # Recursive, suffix-independent coverage, excluding Python bytecode caches.
    return sorted(path for directory in ("code", "evidence")
                  for path in TOP.joinpath(directory).rglob("*")
                  if path.is_file() and "__pycache__" not in path.parts
                  and path.suffix != ".pyc")


def packed(rows):
    """Lossless compact identities: SHA-256 bytes in RFC1924 base85."""
    result = {"code": {}, "evidence": {}, "other": {}}
    for row in rows:
        path = Path(row["path"])
        expected = ".py" if path.parts[0] == "code" else ".json"
        if path.suffix == expected:
            group = path.parts[0]
            key = path.relative_to(group).with_suffix("").as_posix()
        else:
            group, key = "other", path.as_posix()
        result[group][key] = [row["bytes"], base64.b85encode(
            bytes.fromhex(row["sha256"])).decode("ascii")]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--list", action="store_true", help="Print the losslessly decoded identity map")
    args = parser.parse_args()
    target = TOP / "evidence-manifest.json"
    observed = [identity(path) for path in artifacts()]
    inherited = [identity(ROOT / "tracks/lattice-unisolvence/code" / name, ROOT)
                 for name in ("c3_lebesgue.py", "c3_rank.py")]
    if args.verify or args.list:
        saved = json.loads(target.read_text())
        decoded = (json.loads(zlib.decompress(base64.b85decode(saved["artifacts_payload"])))
                   if saved["schema"] == "padua-3d-code-data-manifest-v5"
                   else saved["artifacts"])
        if args.list:
            print(json.dumps(decoded, indent=2))
            return
        if decoded != packed(observed) or saved.get("inherited_inputs") != inherited:
            raise SystemExit("FAIL: code/data set or identities changed")
        print(json.dumps({"verdict": "PASS", "artifacts": len(observed),
                          "bytes": sum(row["bytes"] for row in observed)}))
        return
    output = {
        "schema": "padua-3d-code-data-manifest-v5",
        "rules_input_sha": "38227202bc6908d5a5a874950145761a8ca4312f",
        "historical_rules_input_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
        "generate": "python topics/padua-3d-20261106/code/artifact_manifest.py",
        "verify": "python topics/padua-3d-20261106/code/artifact_manifest.py --verify",
        "format": "code/evidence map relative stems to [bytes, RFC1924 base85 SHA-256]; append .py/.json. other keys are full topic-relative paths. Recursive scope excludes __pycache__ and .pyc only.",
        "artifacts_codec": "RFC1924 base85(zlib(level9, UTF8 compact JSON v4 identity map)); --list decodes",
        "artifacts_payload": base64.b85encode(zlib.compress(
            json.dumps(packed(observed), separators=(",", ":")).encode(), 9)).decode(),
        "inherited_inputs": inherited,
        "commands": "Commands and execution metadata are in the hash-pinned receipts and linked attempts; historical metadata companions preserve missing-field limits.",
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
