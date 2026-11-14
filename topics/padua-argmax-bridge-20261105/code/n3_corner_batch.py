#!/usr/bin/env python3
"""Bounded outward producer sweep of n=2..128; bulk endpoints stay local.

The unchanged C producer supplies intervals. This wrapper checks only exact
assembly, controls, counts and the predeclared common candidate threshold.
A distinct implementation must independently reconstruct the range before
the finite corner claim may be marked PROVED.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

FIRST, LAST = 2, 128
COMMON_KAPPA = Fraction(1, 16000)
PHASE_RADIUS = Fraction(1, 128)
CPU_CAP = 1200
SOURCE_SHA = "a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd"
INPUT_SHA = "c000899f3fb10d6ba0f1725341a045fe11ec943a"


def identity(path):
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size}


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def capped_child(remaining):
    def apply():
        seconds = max(1, math.ceil(remaining))
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds + 1))
    return apply


def check(cert, n):
    assert cert["schema"] == "n3-corner-energy-v1"
    assert cert["degree"] == n and cert["precision_bits"] == 256
    ell, high, low_E, E, u, kappa, H, r = (Fraction(cert[k]) for k in
        ("corner_lower", "corner_upper", "energy_lower", "energy_upper",
         "global_norm_upper", "kappa", "physical_H_radius", "symmetric_scaled_phase_radius"))
    assert 0 < ell <= high and 0 <= low_E <= E
    assert cert["zero_cardinals_omitted"] == n // 2
    assert cert["nonzero_cardinals"] + n // 2 == (n + 1) * (n + 2) // 2
    assert u == 110 * (1 + n.bit_length())**2
    b, K = E / (n**4 * ell), u / ell
    assert Fraction(cert["normalized_energy_upper"]) == b
    assert Fraction(cert["global_corner_ratio_upper"]) == K
    assert kappa == min(Fraction(1), 1 / (8 * (b + 3 * K)))
    assert H == kappa / n**2
    factor = Fraction((n + 1)**2 + n*n, 2 * (n + 1)**2)
    assert r*r*factor <= kappa
    assert PHASE_RADIUS**2 * factor < COMMON_KAPPA
    if n == 2:
        assert ell <= 3 <= high
        assert low_E <= Fraction(331, 18) <= E
    return kappa


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--mpfr-include", type=Path, required=True)
    p.add_argument("--receipt", type=Path, required=True)
    a = p.parse_args()
    a.output_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).with_name("n3_corner_bounds.c")
    if identity(source)["sha256"] != SOURCE_SHA:
        raise RuntimeError("Unchanged accepted producer source hash required")
    binary = a.output_dir / "n3_corner_bounds"
    rawpath = a.output_dir / "corner-bounds-n2-128.jsonl"
    if rawpath.exists():
        raise FileExistsError(f"Use a fresh output directory; will not replace {rawpath}")
    build = ["cc", "-O2", "-std=c11", "-Wall", "-Wextra", "-Werror", "-I",
             str(a.mpfr_include), str(source), "-Wl,-l:libmpfr.so.6", "-lgmp", "-o", str(binary)]
    initial_cpu, start = child_cpu(), time.monotonic()
    subprocess.run(build, check=True, preexec_fn=capped_child(CPU_CAP))
    counters = {"requested": LAST - FIRST + 1, "attempted": 0, "completed": 0,
                "passed_common_target": 0, "failed_common_target": 0,
                "arithmetic_or_process_errors": 0, "unrun": LAST - FIRST + 1,
                "nonzero_cardinals": 0, "zero_cardinals_omitted": 0}
    minimum, minimum_degree, failure = None, None, None
    native_cpu, versions = 0.0, None
    with rawpath.open("x") as rawfile:
        for n in range(FIRST, LAST + 1):
            remaining = CPU_CAP - (child_cpu() - initial_cpu)
            if remaining <= 0:
                failure = {"degree": n, "outcome": "total_cpu_cap_before_case"}
                break
            counters["attempted"] += 1
            command = [str(binary), str(n), "256"]
            try:
                proc = subprocess.run(command, capture_output=True, text=True,
                                      preexec_fn=capped_child(remaining))
                if proc.returncode != 0:
                    raise RuntimeError(f"producer exit {proc.returncode}: {proc.stderr[:1000]}")
                cert = json.loads(proc.stdout)
                kappa = check(cert, n)
                if versions is None:
                    versions = {k: cert[k] for k in ("gmp_version", "mpfr_version")}
                assert versions == {k: cert[k] for k in versions}
                counters["completed"] += 1
                counters["unrun"] -= 1
                counters["nonzero_cardinals"] += cert["nonzero_cardinals"]
                counters["zero_cardinals_omitted"] += cert["zero_cardinals_omitted"]
                native_cpu += cert["cpu_seconds_diagnostic"]
                if minimum is None or kappa < minimum:
                    minimum, minimum_degree = kappa, n
                passed = kappa >= COMMON_KAPPA
                key = "passed_common_target" if passed else "failed_common_target"
                counters[key] += 1
                rawfile.write(json.dumps({"degree": n, "command": command,
                    "outcome": "PASS" if passed else "FAILED_COMMON_TARGET", "certificate": cert},
                    sort_keys=True, separators=(",", ":")) + "\n")
                rawfile.flush()
                if not passed:
                    failure = {"degree": n, "outcome": "failed_predeclared_kappa_ge_1_over_16000",
                               "exact_kappa": str(kappa)}
                    break
            except (AssertionError, ValueError, RuntimeError, KeyError) as exc:
                counters["arithmetic_or_process_errors"] += 1
                failure = {"degree": n, "outcome": "arithmetic_or_process_error", "detail": str(exc)}
                rawfile.write(json.dumps(failure, sort_keys=True) + "\n")
                break
            if child_cpu() - initial_cpu > CPU_CAP:
                failure = {"degree": n, "outcome": "total_cpu_cap_after_case"}
                break
    total_cpu = child_cpu() - initial_cpu
    complete = (failure is None and counters["completed"] == LAST - FIRST + 1
                and counters["passed_common_target"] == LAST - FIRST + 1)
    receipt = {"schema": "n3-corner-batch-producer-v1", "rules_input_sha": INPUT_SHA,
        "status": "COMPLETE PRODUCER; independent range replay PENDING" if complete else "STOPPED; see failure",
        "claim_status": "CONDITIONAL pending distinct exact/outward range reconstruction",
        "input_range": {"first": FIRST, "last": LAST, "step": 1, "count": LAST - FIRST + 1},
        "predeclared_common_kappa": str(COMMON_KAPPA), "scaled_phase_square_radius": str(PHASE_RADIUS),
        "precision_bits": 256, "total_child_cpu_cap_seconds": CPU_CAP,
        "counters": counters, "all_ran_and_passed": complete, "failure": failure,
        "minimum_producer_kappa": str(minimum) if minimum is not None else None,
        "minimum_degree": minimum_degree, "minimum_kappa_decimal_diagnostic": float(minimum) if minimum else None,
        "total_child_cpu_seconds_diagnostic": total_cpu,
        "summed_native_cpu_seconds_diagnostic": native_cpu,
        "wall_seconds_diagnostic": time.monotonic() - start,
        "source": identity(source), "wrapper": identity(Path(__file__)),
        "binary": identity(binary), "official_mpfr_header": identity(a.mpfr_include / "mpfr.h"),
        "build_command": build, "producer_argv_template": [str(binary), "{n=2..128}", "256"],
        "runtime_versions": versions, "compiler": subprocess.check_output(["cc", "--version"], text=True).splitlines()[0],
        "python": sys.version.split()[0], "platform": platform.platform(), "bulk_raw_output": identity(rawpath),
        "developer_checks": "exact rational assembly, complete integer input iteration, mask counts, n2 mass3/energy331/18 control, common-kappa and phase-square predicates",
        "independent_replay": "PENDING; reconstruct from integer range and fixed threshold with distinct arithmetic, not bulk endpoint replay",
        "storage": "Full per-degree endpoints local only; short aggregate receipt only in Git",
        "model": "Codex parent-assigned gpt-6.1-sol xhigh; serving metadata unexposed"}
    a.receipt.parent.mkdir(parents=True, exist_ok=True)
    a.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"receipt": identity(a.receipt), "all_ran_and_passed": complete,
                      "total_child_cpu_seconds_diagnostic": total_cpu,
                      "minimum_exact_producer_kappa": receipt["minimum_producer_kappa"],
                      "minimum_degree": minimum_degree, "failure": failure}, indent=2))
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
