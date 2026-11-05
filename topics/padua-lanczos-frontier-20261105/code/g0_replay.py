#!/usr/bin/env python3
"""Replay G0 from a pinned Git snapshot; all generated data stays outside Git.

Requires the README's pinned packages and unchanged polyrat source. See
independent-checks-g0.md for installation/source acquisition. This script does
not install packages, access the network, change Git state, or upgrade claims.
Exit 1 requests disposition of differences or failed exact checks; it does not
automatically declare the G0 gate failed. Byte equality is a diagnostic, not a
new acceptance criterion. The checker records a separate evidence-based gate
disposition in independent-checks-g0.md.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tarfile
import time

SOURCE = "8359bf7a047d9a212bd841224fb97a458cb7435e"
UPSTREAM = "6903d7af9995c9d88e661fb229626696e00fdfba"
EVIDENCE = Path("topics/padua-lanczos-drift-20261101/evidence")
DRIFT = Path("tracks/bivariate-lanczos/code/drift")
RESTORE = {
    "audit-02-e1-checks.json", "e1-multinode-certificates.json",
    "e1-scalar-cgs2.json", "independent-scalar-01.json",
}
UPSTREAM_PINS = {
    "arnoldi.py": "e51f356170dc5e1403f1065daf5bc331e7ce470cac1b9161f5ecb9efccf68d86",
    "index.py": "84df400c73a2aacf922ff38c0a591b525c2ac1f9b7a9f958f4111d4ceb88d10d",
    "basis.py": "9ce50feba7cfaa706db3bb94bbe2b34f065d9dbde28a18a3eee021d11e8ec478",
    "version.py": "1d13b63cb7af46b37f80ac0d695be5f795c2db5ce6e66dea34143da4cb434439",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    p.add_argument("--output-dir", type=Path, required=True,
                   help="New directory outside repository; refuses existing path")
    p.add_argument("--external", type=Path, required=True, help="Pinned polyrat source root")
    p.add_argument("--pythonpath", required=True, help="Paths for pinned Python dependencies")
    p.add_argument("--diagnostics", action="store_true", help="Three repeat and three BLAS kernel probes")
    p.add_argument("--fresh-pythonpath", help="Optional independently installed pinned wheels for comparison")
    a = p.parse_args()
    repo, out, external = a.repo.resolve(), a.output_dir.resolve(), a.external.resolve()
    if out == repo or repo in out.parents:
        p.error("output-dir must be outside the repository")
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out / "replay"
    snapshot.mkdir()
    archive = subprocess.check_output(["git", "-C", str(repo), "archive", SOURCE])
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(snapshot, filter="data")
    manifest = read(snapshot / "topics/padua-lanczos-drift-20261101/cold-storage.json")
    restored = []
    for item in manifest["entries"]:
        if Path(item["path"]).name not in RESTORE:
            continue
        data = subprocess.check_output(["git", "-C", str(repo), "cat-file", "blob", item["git_blob"]])
        assert len(data) == item["bytes"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"]
        (snapshot / item["path"]).write_bytes(data)
        restored.append({k: item[k] for k in ("path", "git_blob", "bytes", "sha256")})
    assert len(restored) == len(RESTORE)
    upstream_hashes = {name: sha(external / "polyrat" / name) for name in UPSTREAM_PINS}
    assert upstream_hashes == UPSTREAM_PINS
    provenance = read(snapshot / EVIDENCE / "e6-provenance.json")
    local_hashes = {}
    for item in provenance["files"]:
        if item["path"].endswith(".py"):
            actual = sha(snapshot / item["path"])
            assert actual == item["sha256"]
            local_hashes[item["path"]] = actual
    env = dict(os.environ, PYTHONPATH=a.pythonpath, OPENBLAS_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    # Avoid inheriting an undisclosed kernel override in the baseline.
    env.pop("OPENBLAS_CORETYPE", None)
    version_code = "import importlib.metadata as m,json,platform; print(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'packages':{x:m.version(x) for x in ['numpy','scipy','sympy','mpmath','python-flint','backports.cached-property']}}))"
    versions = json.loads(subprocess.check_output([sys.executable, "-B", "-c", version_code], env=env))
    assert versions["packages"] == {"numpy": "2.3.5", "scipy": "1.17.0", "sympy": "1.14.0", "mpmath": "1.3.0", "python-flint": "0.9.0", "backports.cached-property": "1.0.2"}
    cases = [
        ("reproduce-triangle", "e1_reproduce.py", ["--set", "triangle"]),
        ("reproduce-rotated", "e1_reproduce.py", ["--set", "rotated"]),
        ("scalar-finite", "e1_scalar_finite_check.py", []),
        ("e5-exact", "e5_exact_checks.py", []),
        ("e6-T24", "e6_benchmark.py", ["--external", str(external), "--sets", "T24", "--grid-degree", "12"]),
    ]

    def run(case, custom_env=None):
        name, script, args = case
        output = out / (name + ".json")
        command = [sys.executable, "-B", str(snapshot / DRIFT / script), *args]
        if script != "e5_exact_checks.py":
            command += ["--output", str(output)]
        started = time.time()
        with (out / (name + ".stdout")).open("w") as stdout, (out / (name + ".stderr")).open("w") as stderr:
            result = subprocess.run(command, cwd=snapshot, env=custom_env or env, stdout=stdout, stderr=stderr)
        if script == "e5_exact_checks.py":
            output.write_bytes((out / (name + ".stdout")).read_bytes())
        receipt = {"name": name, "command": command, "start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)), "elapsed_seconds": time.time()-started, "exit_code": result.returncode, "code_sha256": sha(snapshot / DRIFT / script), "output": str(output), "output_bytes": output.stat().st_size if output.exists() else None, "output_sha256": sha(output) if output.exists() else None}
        write(out / (name + ".receipt.json"), receipt)
        assert result.returncode == 0, receipt
        print(name, "exit 0", flush=True)
        return receipt

    with ThreadPoolExecutor(max_workers=5) as pool:
        receipts = list(pool.map(run, cases))
    scalar = read(out / "scalar-finite.json")
    old_scalar = read(snapshot / EVIDENCE / "response-02-e1-scalar-finite.json")
    tri = read(out / "reproduce-triangle.json")
    old_tri = read(snapshot / EVIDENCE / "e1-reproduction-triangle.json")
    del tri["explicit_projection_check"]["input_sha256"]
    del old_tri["explicit_projection_check"]["input_sha256"]
    exact = {
        "triangle_regeneration_pass": tri["result"] == "PASS",
        "triangle_stable_receipt_equal": tri == old_tri,
        "rotated_regeneration_pass": read(out / "reproduce-rotated.json")["result"] == "PASS",
        "scalar_all_pass": scalar["all_pass"],
        "scalar_sets_equal": scalar["sets"] == old_scalar["sets"],
        "scalar_pins_equal": scalar["input_pins_verified"] == old_scalar["input_pins_verified"],
        "e5_json_equal": read(out / "e5-exact.json") == read(snapshot / EVIDENCE / "e5-exact-checks.json"),
    }
    baseline = read(out / "e6-T24.json")
    case = baseline["cases"][0]
    old = next(c for c in read(snapshot / EVIDENCE / "e6-frozen-grids12.json")["cases"] if c["name"] == "T24")
    rows = [{"method": name, "committed_gap": old["methods"][name]["gap"], "rerun_gap": metric["gap"], "relative_delta": metric["gap"]/old["methods"][name]["gap"]-1} for name, metric in case["methods"].items()]
    probes = []
    if a.diagnostics:
        for i in range(3):
            run((f"e6-repeat-{i}", cases[-1][1], cases[-1][2]))
            probes.append({"kind": "repeat", "index": i, "exact_baseline_equal": read(out / f"e6-repeat-{i}.json") == baseline})
        for core in ["Sandybridge", "Nehalem", "Prescott"]:
            probe_env = dict(env, OPENBLAS_CORETYPE=core)
            if a.fresh_pythonpath:
                probe_env["PYTHONPATH"] = a.fresh_pythonpath
            receipt = run((f"e6-{core}", cases[-1][1], cases[-1][2]), probe_env)
            data = read(out / f"e6-{core}.json")["cases"][0]
            probes.append({"kind": "kernel", "core": core, "command": receipt["command"], "pythonpath": probe_env["PYTHONPATH"], "exact_committed_case_equal": data == old, "output_sha256": receipt["output_sha256"], "gaps": {k:v["gap"] for k,v in data["methods"].items()}})
    if a.fresh_pythonpath:
        receipt = run(("e6-fresh", cases[-1][1], cases[-1][2]), dict(env, PYTHONPATH=a.fresh_pythonpath))
        probes.append({"kind": "fresh_wheels", "pythonpath": a.fresh_pythonpath, "command": receipt["command"], "output_sha256": receipt["output_sha256"], "exact_baseline_equal": read(out / "e6-fresh.json") == baseline})
    with (out / "blas-config.txt").open("w") as f:
        subprocess.run([sys.executable, "-B", "-c", "import numpy,scipy; numpy.show_config(); numpy.show_runtime(); scipy.show_config()"], env=env, stdout=f, check=True)
    identity = all(exact.values()) and case == old
    summary = {
        "source_commit": SOURCE, "harness_sha256": sha(__file__), "upstream_commit": UPSTREAM,
        "scope": "Supplementary independent replay only; no new target runs or theorem invalidation.",
        "automated_outcome": "EXACT_AND_E6_IDENTITY_PASS" if identity else "EXACT_CHECKS_PASS_E6_DIFF_REQUIRES_DISPOSITION" if all(exact.values()) else "EXACT_CHECK_FAILURE_REQUIRES_DISPOSITION",
        "outcome_note": "The README allows operation/library variation. Exact equality is only a diagnostic. A nonidentical case requires a separate evidence-based explanation/disposition; the script does not decide whether its cause is explained and imposes no automatic bit-equality acceptance criterion.",
        "environment": versions, "pythonpath": a.pythonpath, "blas_threads": 1,
        "restored_inputs": restored, "local_source_hashes": local_hashes, "upstream_hashes": upstream_hashes,
        "run_receipts": receipts, "exact_checks": exact,
        "scalar_display_ratios": {v["set"]:v["display"]["squared_ratio_lower_bound"] for v in scalar["sets"]},
        "e6": {"case_identity": {k:case[k] for k in ["name","n","M","N","input_sha256"]}, "input_hash_equal": case["input_sha256"] == old["input_sha256"], "exact_case_equal": case == old, "reference_before": old["reference"], "reference_now": case["reference"], "yx_dev_entry_max": case["upstream_yx_vs_dev_entry_max"], "gap_comparison": rows},
        "blas_receipt_sha256": sha(out / "blas-config.txt"),
        "limits": ["Comparator uppers checked from pinned records, not regenerated.", "Degree-12 wrappers; no degrees-2–6 sweep.", "T24 degree12 only; PD-T146 high-degree G4 rows not run.", "Historical runtime dispatch not pinned; no probed kernel exactly reproduces the frozen row."],
    }
    write(out / "g0-summary.json", summary)
    write(out / "g0-kernel-probes.json", {"source_commit": SOURCE, "scope": "Bounded G0 discrepancy diagnosis, not new target science", "probes": probes})
    print(summary["automated_outcome"], flush=True)
    return 0 if identity else 1


if __name__ == "__main__":
    sys.exit(main())
