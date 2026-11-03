"""Independent bounded reference G0 replay; outputs remain outside Git."""
if not __debug__:
    raise RuntimeError("Scientific verification requires assertions; do not use -O or PYTHONOPTIMIZE.")

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

REPO = Path(__file__).resolve().parents[4]
REF = REPO / "topics/padua-argmax-alln-20261101/code/part3"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/workspace/padua-work/independent")
OUT.mkdir(parents=True, exist_ok=True)
started = time.monotonic()
deadline = started + 1800
records = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(name, argv):
    begin = time.monotonic()
    remaining = deadline - begin
    if remaining <= 0:
        raise TimeoutError("independent 30-minute wall-clock budget exhausted")
    with (OUT / (name + ".log")).open("w") as log:
        result = subprocess.run(argv, stdout=log, stderr=subprocess.STDOUT, timeout=remaining)
    elapsed = time.monotonic() - begin
    assert result.returncode == 0, (name, result.returncode)
    return {"command": argv, "wall_seconds": elapsed}


try:
    for n in range(17, 25):
        cert = OUT / f"reference-n{n}.json"
        check = OUT / f"reference-n{n}-check.json"
        producer = run(f"reference-n{n}-producer", [sys.executable, str(REF / "finite_general_run.py"),
                       "--n", str(n), "--seconds", "600", "--output", str(cert)])
        data = json.loads(cert.read_text())
        assert data["complete"] and not data["pending"]
        checker = run(f"reference-n{n}-checker", [sys.executable, str(REF / "finite_general_check.py"),
                      str(cert), "--output", str(check)])
        accepted = json.loads(check.read_text())
        assert accepted["accepted"]
        row = {"n": n, "producer": producer, "checker": checker, "certificate": str(cert),
               "certificate_sha256": digest(cert), "certificate_bytes": cert.stat().st_size,
               "checker_receipt_sha256": digest(check), "statistics": data["statistics"],
               "producer_internal_seconds": data["total_seconds"], "checker_internal_seconds": accepted["seconds"]}
        records.append(row)
        (OUT / "reference-g0-receipt.json").write_text(json.dumps(records, indent=2) + "\n")
        print(json.dumps(row), flush=True)
    controls = OUT / "reference-n17-controls.json"
    control_run = run("reference-n17-controls", [sys.executable, str(REF / "finite_general_controls.py"),
                      str(OUT / "reference-n17.json"), "--output", str(controls)])
    print(json.dumps({"controls": control_run, "receipt_sha256": digest(controls)}), flush=True)
finally:
    (OUT / "reference-g0-status.json").write_text(json.dumps({
        "completed_degrees": [r["n"] for r in records], "elapsed_seconds": time.monotonic() - started,
        "rule_input_sha": "8a1f394739293953e1566fd24a0a193cc78ff26f",
        "source_sha256": {p.name: digest(p) for p in REF.glob("*.py")}}, indent=2) + "\n")
