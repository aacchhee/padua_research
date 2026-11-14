#!/usr/bin/env python3
"""Build/run the corner-energy producer and collect its small pending receipt."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys


def identity(path):
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--mpfr-include", type=Path, required=True)
    p.add_argument("--receipt", type=Path, required=True)
    p.add_argument("--degrees", type=int, nargs="+", default=[33, 64, 128])
    p.add_argument("--precision", type=int, default=256)
    a = p.parse_args()
    a.output_dir.mkdir(parents=True, exist_ok=True)
    code = Path(__file__).parent
    source, diagnostic = code / "n3_corner_bounds.c", code / "n3_corner_diagnostic.py"
    binary = a.output_dir / "n3_corner_bounds"
    build = ["cc", "-O2", "-std=c11", "-Wall", "-Wextra", "-Werror", "-I",
             str(a.mpfr_include), str(source), "-Wl,-l:libmpfr.so.6", "-lgmp", "-o", str(binary)]
    subprocess.run(build, check=True)
    records = []
    for n in a.degrees:
        command = [str(binary), str(n), str(a.precision)]
        raw = subprocess.check_output(command)
        path = a.output_dir / f"n{n}.json"
        path.write_bytes(raw)
        cert = json.loads(raw)
        ell, E, u, kappa, H, r = (Fraction(cert[k]) for k in
            ("corner_lower", "energy_upper", "global_norm_upper", "kappa",
             "physical_H_radius", "symmetric_scaled_phase_radius"))
        assert n == cert["degree"] and ell > 0 and E >= 0
        assert Fraction(cert["corner_upper"]) >= ell
        assert Fraction(cert["energy_lower"]) <= E
        assert cert["zero_cardinals_omitted"] == n // 2
        assert cert["nonzero_cardinals"] + n // 2 == (n + 1) * (n + 2) // 2
        b, K = E / (n**4 * ell), u / ell
        assert Fraction(cert["normalized_energy_upper"]) == b
        assert Fraction(cert["global_corner_ratio_upper"]) == K
        assert kappa == min(Fraction(1), 1 / (8 * (b + 3 * K)))
        assert H == kappa / n**2
        assert r*r * Fraction((n + 1)**2 + n*n, 2 * (n + 1)**2) <= kappa
        old = max(Fraction(1, 2 * (n * (n + 1))**3), Fraction(1, 10**11 * n*n))
        records.append({"command": command, "output": identity(path), "certificate": cert,
                        "physical_radius_gain_diagnostic": float(H / old)})
    diag_command = [sys.executable, str(diagnostic), str(binary)]
    diag_raw = subprocess.check_output(diag_command)
    diag_path = a.output_dir / "diagnostic.json"
    diag_path.write_bytes(diag_raw)
    diag = json.loads(diag_raw)
    receipt = {"schema": "n3-corner-pending-receipt-v1",
               "status": "PENDING independent exact/outward replay; no per-degree PROVED claim",
               "rules_input_sha": "714f3cad18859c07cd13f31561f2a185f9591a7f",
               "agent_model": "Codex parent-assigned gpt-6.1-sol xhigh; serving metadata unexposed",
               "build_command": build, "compiler": subprocess.check_output(
                   ["cc", "--version"], text=True).splitlines()[0],
               "platform": platform.platform(), "python": sys.version.split()[0],
               "source_files": [identity(x) for x in (source, diagnostic, Path(__file__))],
               "header": identity(a.mpfr_include / "mpfr.h"), "binary": identity(binary),
               "developer_exact_receipt_checks": "PASS: rational assembly, mask counts, phase-box inequality only",
               "runs": records, "diagnostic_command": diag_command,
               "diagnostic_output": identity(diag_path),
               "diagnostic_summary": {k: diag[k] for k in ("status", "method", "mpmath_version",
                   "decimal_precision", "degrees", "nonzero_cardinals_checked", "max_relative_midpoint_error")},
               "independent_replay": "PENDING; must use a separately implemented arithmetic path",
               "archival": "Bulk local output; Padua cold-storage transfer pending if needed"}
    a.receipt.parent.mkdir(parents=True, exist_ok=True)
    a.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"receipt": identity(a.receipt), "degrees": a.degrees,
                      "status": receipt["status"]}, indent=2))


if __name__ == "__main__":
    main()
