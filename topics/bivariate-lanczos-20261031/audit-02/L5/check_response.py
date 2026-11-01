"""Focused L5 audit-02: independently recompute paired size-level summaries.

No experiment is regenerated. Run from the repository root with Python -B -I.
Only audit-02/L5 files are written. Developer modules are not imported.
"""
from pathlib import Path
import collections
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np
import scipy
from scipy.stats import t

ROOT = Path(__file__).resolve().parents[4]
TOP = Path("topics/bivariate-lanczos-20261031")
OUT = ROOT / TOP / "audit-02/L5"
LOG = ROOT / TOP / "directions/L5/logs"
HEAD = "50b0d304001b48607527e5086a67045f534d9472"
CANDIDATE = "075d4074017445a0fd4d7443ffac97cd7f8c106b"
BASE = "5f523313b7b388cb114103734028f0a850dfeaad"
METHODS = {"G": "givens-scheme", "HL": "hl", "CGS2": "cgs2", "HH": "hh"}
PAIRS = [("G", "HL"), ("G", "CGS2"), ("G", "HH"),
         ("HL", "HH"), ("CGS2", "HH"), ("HL", "CGS2")]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fit(sizes, values):
    # Explicit centered sums, independent of scipy.stats.linregress.
    x = np.log10(np.asarray(sizes, dtype=float))
    y = np.asarray(values, dtype=float)
    xc, yc = x - x.mean(), y - y.mean()
    sxx = float(xc @ xc)
    slope = float(xc @ yc) / sxx
    residual = yc - slope * xc
    df = len(x) - 2
    se = math.sqrt(float(residual @ residual) / df / sxx)
    halfwidth = float(t.ppf(.975, df)) * se
    return [slope, slope - halfwidth, slope + halfwidth], df


def main():
    checkout_head = git("rev-parse", "HEAD").decode().strip()
    old = json.loads((ROOT / TOP / "audit-01/L5/audited_manifest.json").read_text())
    paths = {r["path"] for r in old["files"]}
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / TOP / "audit-01/L5").iterdir() if p.is_file())
    paths.update([str(TOP / "audit-01/L5.md"), str(TOP / "response-01.md"),
                  str(TOP / "directions/L5/response-audit-01.md"),
                  str(TOP / "directions/L5/logs/analysis_r01d.txt"),
                  "tracks/bivariate-lanczos/code/L5/analyze_r01d.py"])
    files = []
    for name in sorted(paths):
        b = (ROOT / name).read_bytes()
        row = {"path": name, "sha256": sha(b), "bytes": len(b)}
        for label, rev in [("head", HEAD), ("candidate", CANDIDATE), ("baseline", BASE)]:
            p = subprocess.run(["git", "show", rev + ":" + name], cwd=ROOT, capture_output=True)
            row[label + "_identical"] = p.returncode == 0 and b == p.stdout
        assert row["head_identical"], name
        if name != str(TOP / "response-01.md"):
            assert row["candidate_identical"], name
        files.append(row)
    baseline_map = {r["path"]: r for r in files}
    reused = ["AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md", "state/IDEAS.md", "literature/INDEX.md"]
    for name in reused:
        assert baseline_map[name]["baseline_identical"], name
        oldrow = next(r for r in old["files"] if r["path"] == name)
        assert oldrow["sha256"] == baseline_map[name]["sha256"], name
    # The top-level response has bookkeeping updates after the scientific
    # candidate, so it is separately checked below rather than required equal.
    (OUT / "input_manifest.json").write_text(json.dumps({"head": HEAD, "candidate": CANDIDATE,
        "baseline": BASE, "files": files}, indent=2) + "\n")

    rows = []
    for family in ["padua_cub", "padua_rand", "padua_unif", "random", "random_cheb"]:
        data = [json.loads(s) for s in (LOG / ("r01_" + family + ".jsonl")).read_text().splitlines()]
        data = [r for r in data if not r.get("meta")]
        assert all(r["family"] == family and all(math.isfinite(r[m]) and r[m] > 0 for m in METHODS.values()) for r in data)
        assert len({(r["M"], r["order"]) for r in data}) == len(data)
        classes = {"all5" if family.startswith("padua") else "all": data}
        if family.startswith("padua"):
            classes["structured"] = [r for r in data if r["order"] in ("given", "sortx")]
            classes["random"] = [r for r in data if r["order"].startswith("rand")]
        for name, crs in classes.items():
            sizes = sorted({r["M"] for r in crs})
            groups = [[r for r in crs if r["M"] == M] for M in sizes]
            for a, b in PAIRS:
                ma, mb = METHODS[a], METHODS[b]
                # Subtract the logs before averaging; the driver logs ratios.
                paired = [np.mean([math.log10(r[ma]) - math.log10(r[mb]) for r in group]) for group in groups]
                f, df = fit(sizes, paired)
                marginal_a, _ = fit(sizes, [np.mean([math.log10(r[ma]) for r in g]) for g in groups])
                marginal_b, _ = fit(sizes, [np.mean([math.log10(r[mb]) for r in g]) for g in groups])
                norm = [np.mean([math.log10(r[ma] / r["hh"]) - math.log10(r[mb] / r["hh"]) for r in g]) for g in groups]
                normfit, _ = fit(sizes, norm)
                assert abs(f[0] - marginal_a[0] + marginal_b[0]) < 1e-13
                assert max(abs(u - v) for u, v in zip(f, normfit)) < 1e-13
                rows.append({"family": family, "class": name, "pair": [a, b], "sizes": sizes,
                    "replicates_per_size": [len(g) for g in groups], "df": df,
                    "slope_ci": f, "slope_difference": marginal_a[0] - marginal_b[0],
                    "hh_normalized_difference_fit": normfit})
    # Compare every displayed triple and df from the independently rerun driver.
    printed = (OUT / "analysis_r01d_rerun.txt").read_text()
    parsed = {}
    for line in printed.splitlines():
        m = re.match(r"== (\S+) / (\S+):", line)
        if m:
            family, name = m.groups()
        m = re.match(r"\s+(\S+) - (\S+)\s+([-\d.]+) \[\s*([-\d.]+),\s*([-\d.]+)\] \(df (\d+)\)", line)
        if m:
            a, b, sl, lo, hi, df = m.groups()
            parsed[family, name, a, b] = ([float(sl), float(lo), float(hi)], int(df))
    assert len(parsed) == len(rows) == 66
    for row in rows:
        v, df = parsed[row["family"], row["class"], *row["pair"]]
        assert df == row["df"] and v == [float(f"{x:.3f}") for x in row["slope_ci"]]
    # Verify all 27 slope/interval triples in the current theory table.
    theory = (ROOT / "tracks/bivariate-lanczos/theory/givens-deficit-slopes-measured.md").read_text()
    table = theory.split("**Paired slope differences**", 1)[1].split("| family / class |", 1)[1].split("\n\n", 1)[0].replace("−", "-")
    triples = re.findall(r"(-?\d+\.\d+) \[(-?\d+\.\d+), (-?\d+\.\d+)\]", table)
    expected = [r for r in rows if r["pair"][0] == "G" and (r["family"] != "padua_unif" or r["class"] == "all5")]
    assert len(triples) == len(expected) == 27
    actual_triples = collections.Counter(tuple(float(v) for v in x) for x in triples)
    expected_triples = collections.Counter(tuple(float(f"{v:.3f}") for v in r["slope_ci"]) for r in expected)
    assert actual_triples == expected_triples, {"table_only": actual_triples - expected_triples, "calculation_only": expected_triples - actual_triples}
    decreases = []
    for line in (LOG / "r02_dual.jsonl").read_text().splitlines():
        r = json.loads(line)
        if r.get("meta") or r["order"] != "gepp":
            continue
        dec = [{"from_i": i, "to_i": j, "from_error": a, "to_error": b}
               for i, j, a, b in zip(r["ckpt"], r["ckpt"][1:], r["relfro"], r["relfro"][1:]) if b < a]
        f, _ = fit(r["ckpt"], np.log10(r["relfro"]))
        assert abs(f[0] - r["slope_in_i"]) < 1e-12
        decreases.append({"n": r["size"], "count": len(dec), "decreases": dec, "slope_in_i": f[0]})
    assert {r["n"]: r["count"] for r in decreases} == {15: 3, 20: 3, 30: 1, 40: 0}
    results = {"utc": datetime.now(timezone.utc).isoformat(), "head": HEAD, "checkout_head": checkout_head,
        "checkout_changes_since_head": git("diff", "--name-only", HEAD, checkout_head).decode().splitlines(),
        "environment": {"python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
            "platform": platform.platform(), "OPENBLAS_NUM_THREADS": os.environ.get("OPENBLAS_NUM_THREADS")},
        "driver_output_matches_committed": (OUT / "analysis_r01d_rerun.txt").read_bytes() == (LOG / "analysis_r01d.txt").read_bytes(),
        "paired_rows_checked": len(rows), "theory_table_triples_checked": len(triples),
        "paired": rows, "gepp_decreases": decreases}
    assert results["driver_output_matches_committed"]
    (OUT / "paired_checks.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({k: v for k, v in results.items() if k not in ("paired", "gepp_decreases")}, indent=2))
    print("PASS: 66 paired intervals; common-HH invariance; 27 theory triples; GEPP decline counts/slopes; reused full-read identities.")


if __name__ == "__main__":
    main()
