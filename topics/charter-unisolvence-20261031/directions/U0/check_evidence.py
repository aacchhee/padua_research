"""Verify U0 cold artifacts and their identity against committed supplied inputs."""
from pathlib import Path
import argparse
import hashlib
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cold", type=Path)
    parser.add_argument("committed_inputs", type=Path)
    args = parser.parse_args()
    manifest_path = args.cold / "artifact-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    for row in manifest["artifacts"]:
        path = Path(row["path"])
        assert path.stat().st_size == row["bytes"], str(path)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], str(path)
    identities = json.loads((args.cold / "source-identities.json").read_text())
    for row in identities:
        copy = Path(row["copy"])
        committed = args.committed_inputs / copy.name
        assert hashlib.sha256(copy.read_bytes()).hexdigest() == row["sha256"]
        assert copy.read_bytes() == committed.read_bytes(), str(committed)
    replay = json.loads((args.cold / "child-replay/execution.json").read_text())
    assert len(replay) == 6
    assert all(r["returncode"] == 0 and r["no_traceback"] and r["marker_ok"] for r in replay)
    observations = [json.loads(line) for line in (args.cold / "verify_exact.jsonl").read_text().splitlines()]
    assert len(observations) == 10
    assert {(r["q"], r["degree"], r["distance"]) for r in observations[2:]} == {
        (7, 1, 7), (7, 2, 4), (11, 1, 17), (11, 2, 13),
        (13, 1, 23), (13, 2, 18), (17, 1, 39), (17, 2, 33)}
    print(json.dumps({"result": "PASS", "artifacts_verified": len(manifest["artifacts"]),
                      "source_scripts_verified": len(identities), "child_statuses_zero": 6,
                      "exact_checker_rows": 10,
                      "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
