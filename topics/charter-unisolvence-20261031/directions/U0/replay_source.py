"""Replay unchanged supplied scripts; preserve each exit status absent from run_all.

No import repair is needed: the supplied child scripts insert their own directory.
This wrapper runs a cold-storage byte-identical source copy and never imports it.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import time

SCRIPTS = ("padua_ff.py", "fast_transform.py", "quadratic_padua.py",
           "discriminant_real.py", "hs_ff.py", "padua_codes.py")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_copy", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    records = []
    for name in SCRIPTS:
        script = args.source_copy / name
        command = [sys.executable, "-I", str(script)]
        start = time.monotonic()
        result = subprocess.run(command, capture_output=True, text=True)
        log = args.output / name.replace(".py", ".log")
        log.write_text(result.stdout + result.stderr)
        no_exception = "Traceback (most recent call last)" not in log.read_text()
        marker = {"padua_ff.py": "ALL CHECKS PASSED",
                  "quadratic_padua.py": "ALL OK"}.get(name)
        marker_ok = marker is None or marker in result.stdout
        records.append({"script": name, "command": command,
                        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
                        "returncode": result.returncode,
                        "elapsed_seconds": time.monotonic() - start,
                        "log": str(log), "no_traceback": no_exception,
                        "required_marker": marker, "marker_ok": marker_ok})
        print(name, "rc", result.returncode, "marker_ok", marker_ok, flush=True)
    (args.output / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
    assert all(r["returncode"] == 0 and r["no_traceback"] and r["marker_ok"] for r in records)


if __name__ == "__main__":
    main()
