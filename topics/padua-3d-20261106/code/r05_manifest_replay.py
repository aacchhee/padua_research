#!/usr/bin/env python3
"""Run current manifest/codec controls in a disposable tree, never live master."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]
INHERITED = ["tracks/lattice-unisolvence/code/c3_lebesgue.py",
             "tracks/lattice-unisolvence/code/c3_rank.py",
             "topics/padua-3d-20261106/audit-04/code/A1/aud_enum.cpp"]


def identity(path, base=ROOT):
    raw = path.read_bytes()
    return {"path": path.relative_to(base).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    before = (TOP / "evidence-manifest.json").read_bytes()
    started = datetime.now(timezone.utc).isoformat()
    commands = []
    with tempfile.TemporaryDirectory(prefix="padua-r05-manifest-") as temp:
        root = Path(temp)
        topic = root / TOP.relative_to(ROOT)
        for directory in ("code", "evidence"):
            shutil.copytree(TOP / directory, topic / directory,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for name in INHERITED:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

        def run(script, *flags, reject=False):
            command = [sys.executable, "-B", str(topic / "code" / script), *flags]
            done = subprocess.run(command, capture_output=True, text=True)
            commands.append({"argv": command, "returncode": done.returncode})
            if (done.returncode == 0) == reject:
                raise RuntimeError(done.stdout + done.stderr)
            return done.stdout

        generated = json.loads(run("artifact_manifest.py"))
        verified = json.loads(run("artifact_manifest.py", "--verify"))
        inherited = json.loads((topic / "evidence-manifest.json").read_text())["inherited_inputs"]
        if inherited != [identity(ROOT / name) for name in INHERITED]:
            raise ValueError("current inherited inputs not covered")
        audit_source = root / INHERITED[-1]
        original = audit_source.read_bytes()
        audit_source.write_bytes(original + b"\n// disposable mutation\n")
        run("artifact_manifest.py", "--verify", reject=True)
        audit_source.write_bytes(original)
        run("artifact_manifest.py", "--verify")
        control_path = root / "codec-controls.json"
        run("pdpr_manifest_check.py", "--output", str(control_path))
        controls = json.loads(control_path.read_text())
    if (TOP / "evidence-manifest.json").read_bytes() != before:
        raise RuntimeError("live master changed during disposable verification")
    compiler_command = ["g++", "--version"]
    compiler_utc = datetime.now(timezone.utc).isoformat()
    compiler = subprocess.run(compiler_command, check=True, capture_output=True, text=True)
    record = {"schema": "r05-manifest-replay-v1", "verdict": "PASS",
              "started_utc": started, "command": [sys.executable, *sys.orig_argv[1:]],
              "scope": "Current code/data snapshot; disposable generation/verification and existing codec controls; zero research rounds.",
              "python": sys.version, "platform": platform.platform(),
              "commands": commands, "generated": generated, "verified": verified,
              "inherited_inputs": inherited, "audit04_source_mutation_rejected": True,
              "live_master_unchanged": True,
              "current_compiler_observation": {"observed_utc": compiler_utc, "command": compiler_command, "stdout": compiler.stdout,
                  "limitation": "Current observation only. Historical g++ version unrecoverable. Each implementation's binary was identical between fd4-lee and fdq-lee-replay; producer and auditor binaries differ."},
              "historical_records": [identity(TOP / "evidence" / name) for name in
                                     ("fd4-manifest.json", "fdr-d2-quality-replay.json")],
              "source": identity(Path(__file__).resolve()),
              "controls": controls,
              "controls_metadata_note": "Nested input_head is the existing checker's historical constant, not this run's head; current source hashes and snapshot identities are recorded here."}
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"verdict": "PASS", "codec_controls": len(controls["checks"]),
                      "audit04_source_mutation_rejected": True, "live_master_unchanged": True}))


if __name__ == "__main__":
    main()
