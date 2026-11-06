#!/usr/bin/env python3
"""One independently executed changed-seed m=3000 minimum, MEASURED only."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time

HERE = Path(__file__).resolve().parent
SCAN = HERE / "S4_padua_scan.py"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert digest(SCAN) == "a392135e3a538d90f3d368f8172facabf5c63ab9f941cd0aba2727e5fbe7773b"
    spec = importlib.util.spec_from_file_location("independent_scan", SCAN)
    scan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scan)
    assert digest(scan.SOURCE) == "f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241"
    assert digest(scan.mod.FROZEN) == "623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76"
    proposal = json.loads(scan.PROPOSAL.read_text())
    expected = {"which": "SA", "ncv": 40, "tol": 2e-11, "maximum_matvecs": 500}
    assert proposal["solver"]["minimum"] == expected
    assert proposal["solver"]["maxiter"] == 20000
    report = {
        "status": "RUNNING; MEASURED only, no certified enclosure",
        "source_head": "2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861",
        "scan_preregistration_commit": "ec52c16569ea959dfe682fcd7985378a2ef1cd42",
        "command_argv": sys.argv, "cwd": str(Path.cwd()),
        "started_utc": scan.utc(), "pid": os.getpid(),
        "wrapper_sha256": digest(__file__), "scan_sha256": digest(SCAN),
        "operator_sha256": digest(scan.SOURCE),
        "frozen_code_sha256": digest(scan.mod.FROZEN),
        "proposal_sha256": digest(scan.PROPOSAL),
        "python": platform.python_version(), "numpy": scan.np.__version__,
        "scipy": scan.scipy.__version__, "platform": platform.platform(),
        "threads": {key: os.environ.get(key) for key in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "independence": "Separate process and seed 20261107; frozen solver/operator reused. Only matvec progress printing is added.",
        "residual_guard": "residual <= 1e-8*max(1,abs(value)); finite value and residual required",
        "limits": {"degrees": [3000], "extreme": "minimum", "maximum_matvecs": 500,
                   "wall_seconds": 21600, "peak_rss_gib": 6},
        "results": [],
    }

    def save():
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")

    # Preserve the numerical implementation and add only progress observations.
    original_operator = scan.mod.PaduaOperator
    started = time.monotonic()

    class ObservedOperator(original_operator):
        def _matvec(self, vector):
            result = super()._matvec(vector)
            if self.calls % 20 == 0:
                print(json.dumps({"m": 3000, "matvecs": self.calls,
                                  "elapsed_seconds": time.monotonic() - started}), flush=True)
            return result

    scan.mod.PaduaOperator = ObservedOperator
    save()
    print(json.dumps({"started": report["started_utc"], "pid": report["pid"],
                      "m": 3000, "seed": 20261107}), flush=True)
    row = scan.solve(3000, "minimum", proposal, seed=20261107)
    report["results"].append(row)
    report["status"] = "MEASURED" if row["status"] == "COMPLETED" else "FAILED"
    report["completed"] = row["status"] == "COMPLETED"
    report["finished_utc"] = scan.utc()
    report["developer_comparison"] = "PENDING developer m=3000 completion"
    save()
    print(json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
