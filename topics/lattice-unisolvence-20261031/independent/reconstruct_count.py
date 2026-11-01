#!/usr/bin/env python3
"""Independent C0 reconstruction: orbit graph, direct point counts, no developer imports."""
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import comb, gcd
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
C0 = ROOT / "topics/lattice-unisolvence-20261031/directions/C0"


def orbit(seed, lengths, modulus):
    seen, queue = {seed}, deque([seed])
    units = [u for u in range(modulus) if gcd(u, modulus) == 1]
    while queue:
        row = queue.popleft()
        aa, cc = row[:-1], row[-1]
        neighbors = [tuple(u * v % modulus for v in row) for u in units]
        for j, length in enumerate(lengths):
            bb = list(aa)
            bb[j] = -bb[j] % modulus
            neighbors.append(tuple(bb) + ((cc-aa[j]*(length-1)) % modulus,))
        for j in range(len(lengths)):
            for h in range(j):
                if lengths[j] == lengths[h]:
                    bb = list(aa)
                    bb[j], bb[h] = bb[h], bb[j]
                    neighbors.append(tuple(bb) + (cc,))
        for other in neighbors:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    return seen


def reconstruct():
    counts, details, raw_total = {}, {}, 0
    for d in (2, 3):
        for n in range(1, 7):
            for lengths in combinations_with_replacement(range(n+1, n+4), d):
                for k in range(2, 7):
                    raw = {
                        aa+(c,) for aa in product(range(1, k), repeat=d)
                        if gcd(k, *aa) == 1 for c in range(k)
                    }
                    raw_total += len(raw)
                    while raw:
                        seed = min(raw)
                        component = orbit(seed, lengths, k)
                        assert component <= raw
                        raw -= component
                        assert min(component) == seed
                        aa, c = seed[:-1], seed[-1]
                        count = sum(
                            sum(a*i for a, i in zip(aa, ii)) % k == c
                            for ii in product(*(range(length) for length in lengths))
                        )
                        key = (d, n, lengths, k, aa, c)
                        counts[key] = (count, comb(n+d, d), len(component))
                        details[key] = sorted(component)
    return counts, details, raw_total


def main():
    counts, details, raw_total = reconstruct()
    trials = json.loads((C0 / "count-trials.json").read_text())
    assert trials["columns"] == ["d", "n", "lengths", "k", "a", "c", "count", "target", "orbit_size"]
    recorded = {
        (d, n, tuple(lengths), k, tuple(aa), c): (count, target, size)
        for d,n,lengths,k,aa,c,count,target,size in trials["trials"]
    }
    assert len(recorded) == len(trials["trials"])
    assert counts == recorded
    admitted = {key for key, val in counts.items() if val[0] == val[1]}
    catalogue = json.loads((C0 / "catalogue.json").read_text())
    exported = set()
    for row in catalogue["patterns"]:
        assert len(row["residues"]) == 1
        key = (row["d"], row["n"], tuple(row["lengths"]), row["k"], tuple(row["a"]), row["residues"][0])
        exported.add(key)
        assert row["count"] == counts[key][0]
        assert [list(v) for v in details[key]] == row["equivalence_members"]
    assert exported == admitted
    assert len(exported) == len(catalogue["patterns"])
    residuals = {}
    for n in range(73):
        values = Counter(sum(ii) % 6 for ii in product(range(n+1), range(n+2), range(n+3)))
        delta = [values[c]-comb(n+3,3) for c in range(6)]
        if n < 6:
            residuals[n] = delta
        else:
            assert delta == residuals[n % 6]
    result = {
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": {name:sha256((C0/name).read_bytes()).hexdigest() for name in ("catalogue.json", "count-trials.json")},
        "all_checks_passed": True,
        "raw_parameters": raw_total,
        "canonical_parameters": len(counts),
        "admitted": len(admitted),
        "admitted_by_dimension": dict(Counter(key[0] for key in admitted)),
        "infinite6_correction_table": residuals,
        "direct_count_scope_n": [0,72],
        "method": "Fresh orbit graph closure and direct integer lattice-point enumeration; no developer code imports.",
    }
    out = Path(sys.argv[1])
    out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
