#!/usr/bin/env python3
"""Fresh exact rank calculation and exhaustive catalogue/mapping checks."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "topics/lattice-unisolvence-20261031"


def independent_rank(rows, prime):
    # Incremental row-space basis. Monomials are lexicographic, not developer graded order.
    basis = {}
    for original in rows:
        row = [v % prime for v in original]
        for col in range(len(row)):
            if row[col] == 0:
                continue
            if col in basis:
                pivot = basis[col]
                scale = row[col]
                row = [(v-scale*w) % prime for v,w in zip(row,pivot)]
            else:
                inv = pow(row[col], prime-2, prime)
                basis[col] = [v*inv % prime for v in row]
                break
    return len(basis)


def main():
    rank_path = TOPIC / "directions/C3/ranks.json"
    catalogue_path = TOPIC / "directions/C0/catalogue.json"
    data = json.loads(rank_path.read_text())
    catalogue = json.loads(catalogue_path.read_text())
    source = {row["id"]:row for row in catalogue["patterns"] if row["d"] == 3}
    reps = {row["id"]:row for row in data["representatives"]}
    assert len(reps) == len(data["representatives"])
    assert {row["pattern_id"] for row in data["mapping"]} == set(source)
    assert len(data["mapping"]) == len(source)
    for mapped in data["mapping"]:
        original = source[mapped["pattern_id"]]
        ii = [index for index in product(*(range(v) for v in original["lengths"]))
              if sum(a*i for a,i in zip(original["a"],index)) % original["k"] in original["residues"]]
        transformed = sorted(tuple(L-1-v if (mapped["reversal_mask"]>>j)&1 else v
                                   for j,(v,L) in enumerate(zip(index,original["lengths"]))) for index in ii)
        record = reps[mapped["representative"]]
        assert transformed == [tuple(v) for v in record["points"]]
        assert original["n"] == record["n"]
        assert original["lengths"] == record["lengths"]
    tests, full = 0, 0
    for record in reps.values():
        n = record["n"]
        monomials = [exp for exp in product(range(n+1),repeat=3) if sum(exp)<=n]
        assert len(monomials) == comb(n+3,3) == len(record["points"])
        for test in record["tests"]:
            p = test["p"]
            assert all(p%d for d in range(2,int(p**0.5)+1))
            assert all(len(set(axis)) == len(axis) for axis in test["axes"])
            rows = []
            for index in record["points"]:
                xyz = [axis[j] for axis,j in zip(test["axes"],index)]
                rows.append([pow(xyz[0],a,p)*pow(xyz[1],b,p)*pow(xyz[2],c,p) % p for a,b,c in monomials])
            rank = independent_rank(rows,p)
            assert rank == test["rank"],(record["id"],p,rank,test["rank"])
            assert bool(test["det"]) == (rank == len(monomials))
            tests += 1
            full += rank == len(monomials)
    out = {
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256":{str(path.relative_to(ROOT)):sha256(path.read_bytes()).hexdigest() for path in (rank_path,catalogue_path)},
        "all_checks_passed":True,
        "source_patterns_checked":len(source),
        "representatives_checked":len(reps),
        "matrix_ranks_checked":tests,
        "full_rank_tests":full,
        "method":"Fresh lexicographic monomial matrix and incremental row-space basis; no developer code imports.",
    }
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))


if __name__ == "__main__":
    main()
