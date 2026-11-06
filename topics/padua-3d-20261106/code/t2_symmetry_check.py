#!/usr/bin/env python3
"""Exact folded-residue node-set equivalence under coordinate permutations.

For odd M, cos(2*pi*r/M)=cos(2*pi*s/M) iff r=+/-s mod M.
Thus canonical residues min(r,M-r) identify coordinates exactly; no floats.
This developer addendum checks the audit's equivalences and finite class counts.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform


def canonical_nodes(z, modulus):
    nodes = {tuple(min((k * a) % modulus, (-k * a) % modulus) for a in z)
             for k in range(modulus)}
    return min(tuple(sorted(tuple(node[j] for j in perm) for node in nodes))
               for perm in itertools.permutations(range(3)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for n in (2, 3, 4):
        target = math.comb(n + 3, 3)
        modulus = 2 * target - 1
        groups = {}
        for b, c in itertools.combinations(range(1, target), 2):
            z = (1, b, c)
            key = canonical_nodes(z, modulus)
            if len(key) != target:
                raise RuntimeError("unexpected folded cardinality")
            groups.setdefault(key, []).append(z)
        rows.append({"degree": n, "modulus": modulus,
                     "normalized_pairs": sum(map(len, groups.values())),
                     "node_set_classes_under_axis_permutations": len(groups)})
        if n == 2:
            required = [(1, 3, 7), (1, 4, 6), (1, 5, 8)]
            if len({canonical_nodes(z, modulus) for z in required}) != 1:
                raise RuntimeError("quadratic equivalence failed")
        if n == 4:
            for pair in [[(1, 15, 19), (1, 21, 29)], [(1, 11, 15), (1, 25, 30)]]:
                if len({canonical_nodes(z, modulus) for z in pair}) != 1:
                    raise RuntimeError("quartic equivalence failed")
    receipt = {"schema": "padua-3d-T2-exact-node-equivalence-v1", "date": "2026-11-06",
               "command": ["python", "topics/padua-3d-20261106/code/t2_symmetry_check.py",
                           "--output", str(args.output)],
               "python": platform.python_version(),
               "rules_sha": "e5b64450fce42262dafc88ee357b72e5f203916b",
               "claim_status": "MEASURED finite census; exact node-equivalence check",
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "arithmetic": "exact Python integer residues; full cyclic nodes; all axis permutations",
               "rows": rows, "equivalences": {"n2": [[1, 3, 7], [1, 4, 6], [1, 5, 8]],
                   "n4_better": [[1, 15, 19], [1, 21, 29]],
                   "n4_other": [[1, 11, 15], [1, 25, 30]]}, "verdict": "PASS"}
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
