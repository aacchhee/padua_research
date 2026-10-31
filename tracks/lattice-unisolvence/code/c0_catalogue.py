#!/usr/bin/env python3
"""Exact finite single-fiber counting catalogue; see C0/frozen-scope.md.

No rank or generic-unisolvence inference is made. Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform


def orbit(lengths, k, a, c):
    """All (a,c) reached by units, reversals, and equal-length permutations."""
    d = len(lengths)
    units = [u for u in range(1, k) if math.gcd(u, k) == 1]
    perms = [p for p in it.permutations(range(d))
             if all(lengths[j] == lengths[p[j]] for j in range(d))]
    out = set()
    for mask in range(1 << d):
        aa = tuple((-a[j] if mask >> j & 1 else a[j]) % k
                   for j in range(d))
        cc = (c - sum(a[j] * (lengths[j] - 1)
                      for j in range(d) if mask >> j & 1)) % k
        for p in perms:
            ap = tuple(aa[p[j]] for j in range(d))
            for u in units:
                out.add(tuple((u * x) % k for x in ap) + ((u * cc) % k,))
    return out


def fiber_counts(lengths, k, a):
    """Integer convolution of the one-axis residue histograms."""
    counts = [1] + [0] * (k - 1)
    for length, aj in zip(lengths, a):
        h = [0] * k
        q, r = divmod(length, k)
        for j in range(k):
            h[(aj * j) % k] += q + (j < r)
        counts = [sum(counts[t] * h[(c - t) % k] for t in range(k))
                  for c in range(k)]
    assert sum(counts) == math.prod(lengths)
    return counts


def enumerate_catalogue():
    patterns, trials, summary = [], [], []
    idea_by_d = {2: "IDEA?lattice-c0-codex-01", 3: "IDEA?lattice-c0-codex-02"}
    for d in (2, 3):
        for n in range(1, 7):
            target = math.comb(n + d, d)
            raw_count = canonical_count = admissible_count = 0
            for lengths in it.combinations_with_replacement(range(n + 1, n + 4), d):
                for k in range(2, 7):
                    seen = set()
                    for a in it.product(range(1, k), repeat=d):
                        if math.gcd(k, *a) != 1:
                            continue
                        counts = fiber_counts(lengths, k, a)
                        for c in range(k):
                            raw_count += 1
                            key = a + (c,)
                            if key in seen:
                                continue
                            members = orbit(lengths, k, a, c)
                            assert min(members) == key, (key, min(members))
                            seen.update(members)
                            canonical_count += 1
                            count = counts[c]
                            row = [d, n, list(lengths), k, list(a), c,
                                   count, target, len(members)]
                            trials.append(row)
                            if count != target:
                                continue
                            admissible_count += 1
                            pid = f"C0-d{d}-n{n}-{admissible_count:03d}"
                            patterns.append({
                                "id": pid, "idea_id": idea_by_d[d], "n": n,
                                "d": d, "lengths": list(lengths), "k": k,
                                "a": list(a), "residues": [c], "count": count,
                                "orbit_size": len(members),
                                "equivalence_members": [list(x) for x in sorted(members)],
                                "properties": {
                                    "periodic": "yes, single congruence fiber",
                                    "axis_factorization_or_structure": "unknown",
                                    "lebesgue_growth": "unknown"},
                            })
                    assert len(seen) == sum(k for a in it.product(range(1, k), repeat=d)
                                            if math.gcd(k, *a) == 1)
            summary.append({"d": d, "n": n, "raw_parameters": raw_count,
                            "canonical_parameters": canonical_count,
                            "cardinality_admissible": admissible_count})
    return patterns, trials, summary


def direct_count(lengths, k, a, c):
    return sum(sum(aj * j for aj, j in zip(a, index)) % k == c
               for index in it.product(*(range(length) for length in lengths)))


def self_check(patterns, trials):
    # Separate direct point enumeration checks every canonical row, not only survivors.
    for d, n, lengths, k, a, c, count, target, orbit_size in trials:
        assert direct_count(lengths, k, a, c) == count
        members = orbit(lengths, k, a, c)
        assert len(members) == orbit_size
        for member in members:
            assert fiber_counts(lengths, k, member[:-1])[member[-1]] == count
    # Two concrete small boxes independently check the uniform-family calculation.
    for n in (3, 4, 5, 9, 10, 11):
        lengths = (n + 1, n + 2, n + 3)
        assert fiber_counts(lengths, 6, (1, 1, 1)) == [math.comb(n + 3, 3)] * 6


def write_json(path, data):
    path.write_text(json.dumps(data, separators=(",", ":"), sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--no-self-check", action="store_true")
    args = parser.parse_args()
    patterns, trials, summary = enumerate_catalogue()
    if not args.no_self_check:
        self_check(patterns, trials)
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    meta = {
        "schema_version": 1, "rules_source_sha": "e949ef06895acd5463cdf8df7e0e5f795218f70f",
        "source_sha256": source_sha, "python": platform.python_version(),
        "scope": "C0/frozen-scope.md; positive lengths<=n+3, L<=n analytically excluded; single fibers, nonzero coefficients, primitive characters, d2/d3,n1..6,k2..6",
        "equivalence_member_schema": "[a_1,...,a_d,c] for the same lengths,k",
        "equivalences": "unit scaling; independent axis reversals with c shift; permutations of equal-length axes; lengths sorted",
        "rank_claim": "none", "independent_rerun": "pending",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "catalogue.json", {"metadata": meta,
               "summary": summary, "patterns": patterns})
    write_json(args.output_dir / "count-trials.json", {"metadata": meta,
               "columns": ["d", "n", "lengths", "k", "a", "c", "count", "target", "orbit_size"],
               "trials": trials})
    result = {"summary": summary, "total_patterns": len(patterns),
              "total_canonical_trials": len(trials), "self_check": not args.no_self_check,
              "source_sha256": source_sha}
    write_json(args.output_dir / "count-result.json", result)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
