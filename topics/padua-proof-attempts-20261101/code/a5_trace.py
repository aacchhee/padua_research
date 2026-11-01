"""Log every degenerate_max call in the frozen T3 search, n=3,...,8.

Only imports the original scripts; never executes their __main__ output writers.
This is a floating execution trace, not a certified count or rigorous proof.
Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 and redirect stdout to JSON.
"""
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np
import scipy

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
SOURCE = ROOT / "topics/programme-ideas-20261031/checks/code"
sys.path.insert(0, str(SOURCE / "gen4"))
sys.path.insert(0, str(SOURCE / "decisive/gen4-2"))
from t3_certify import Certifier  # noqa: E402


class LoggedCertifier(Certifier):
    def __init__(self, n):
        self.degenerate_calls = []
        super().__init__(n)

    def degenerate_max(self, zs, Z, d):
        result = super().degenerate_max(zs, Z, d)
        nodes = [(j, k) for j in range(self.n + 1)
                 for k in range(self.n + 2) if (j + k) % 2 == 0]
        accepted, rho, mu, eps = result
        self.degenerate_calls.append({
            "call": len(self.degenerate_calls) + 1,
            "zs_angles_IEEE_double": [float(z) for z in zs],
            "Z_zero_based": [int(b) for b in Z],
            "Z_grid_labels": [list(nodes[int(b)]) for b in Z],
            "accepted_by_frozen_code": bool(accepted),
            "rho0_float": None if rho is None else float(rho),
            "mu0_float": float(mu), "eps1_float": float(eps),
        })
        return result


if __name__ == "__main__":
    reference = json.loads((SOURCE / "decisive/gen4-2/t3_maxima.json").read_text())
    result = []
    for n in range(3, 9):
        certifier = LoggedCertifier(n)
        summary = certifier.run(verbose=False)
        recorded = {key: len(reference[str(n)][key])
                    for key in ("interior", "edge", "corner")}
        actual = {key: summary[key] for key in recorded}
        assert actual == recorded, (n, actual, recorded)
        result.append({"n": n, "all_degenerate_max_calls": certifier.degenerate_calls,
                       "accepted_degenerate_count": summary["stats"]["max_degenerate"],
                       "floating_candidate_counts": actual,
                       "matches_stored_candidate_counts": True,
                       "boxes": summary["stats"]["boxes"],
                       "elapsed_seconds": summary["time"]})
    sources = [SOURCE / "gen4/gen4_tests.py"] + [
        SOURCE / "decisive/gen4-2" / name for name in
        ("t3_certify.py", "t3_degenerate.py", "leb_common.py", "t3_maxima.json", "t3_certify.log")]
    print(json.dumps({"status": "MEASURED execution trace; counts are not certified",
                      "source_commit": "cadb35066160e466cb1704b9791ad6f374446422",
                      "python": platform.python_version(), "numpy": np.__version__,
                      "scipy": scipy.__version__,
                      "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                       for p in sources},
                      "scope": "all calls to degenerate_max; separate corner/edge-node handlers excluded",
                      "results": result}, indent=2))
