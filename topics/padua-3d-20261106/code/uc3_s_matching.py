#!/usr/bin/env python3
"""Independent augmenting-path test of the nonunique/no-perfect S split."""
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile
import time

import uc3_structure as structure


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def perfect(rows):
    N = len(rows)
    column_rows = [[] for _ in rows]
    for r, row in enumerate(rows):
        for c in row:
            column_rows[c].append(r)
    assigned = [-1]*N

    def augment(c, seen):
        for r in column_rows[c]:
            if r in seen:
                continue
            seen.add(r)
            if assigned[r] < 0 or augment(assigned[r], seen):
                assigned[r] = c
                return True
        return False

    return all(augment(c, set()) for c in range(N))


def main():
    began = time.perf_counter()
    source_paths = [Path(__file__).resolve(), Path(structure.__file__).resolve()]
    source_bytes = {p: p.read_bytes() for p in source_paths}
    topic = Path(__file__).resolve().parents[1]
    producer_path = topic/"evidence"/"u3-s.json"
    producer = json.loads(producer_path.read_text())
    producer_raw = Path(producer["raw"]["path"])
    assert sha(producer_raw) == producer["raw"]["sha256"]
    expected = {(r["n"], *r["z"][1:]): r["support"] for r in
                map(json.loads, producer_raw.read_text().splitlines())}
    scratch = Path(tempfile.mkdtemp(prefix="padua-uc3-s-match-"))
    snapshots = []
    for path, data in source_bytes.items():
        snapshot = scratch/path.name
        snapshot.write_bytes(data)
        snapshots.append({"path": str(snapshot), "bytes": len(data), "sha256": sha(snapshot)})
    rows, raw = [], []
    for n in (3, 5, 7):
        N, histogram = math.comb(n+3, 3), Counter()
        for b in range(1, 2*N):
            for c in range(b+1, 2*N):
                matrix = structure.coefficient_rows(n, (1, b, c))
                unique = structure.unique_matching(matrix) is not None
                has_matching = perfect(matrix)
                assert not unique or has_matching
                outcome = "unique" if unique else "alternating-cycle" if has_matching else "no-perfect-matching"
                assert outcome == expected[(n, b, c)]
                histogram[outcome] += 1
                raw.append([n, b, c, outcome])
        rows.append({"n": n, "histogram": dict(histogram)})
    assert len(raw) == len(expected)
    raw_path = scratch/"all-matching-classes.json"
    raw_path.write_bytes(canonical(raw)+b"\n")
    assert all(p.read_bytes() == data for p, data in source_bytes.items())
    receipt = {"command": " ".join(sys.argv), "code": [{"path": str(p), "sha256": sha(p)} for p in source_paths],
               "source_snapshots": snapshots, "producer_input": {"path": str(producer_path), "sha256": sha(producer_path)},
               "producer_raw_input": producer["raw"], "rows": rows, "casewise_matches": len(raw),
               "raw": {"path": str(raw_path), "bytes": raw_path.stat().st_size, "sha256": sha(raw_path)},
               "seconds": time.perf_counter()-began}
    data = canonical(receipt)+b"\n"
    assert len(data) < 16384
    target = topic/"evidence"/"uc3-s-matching.json"
    target.write_bytes(data)
    print(json.dumps({"receipt": str(target), "bytes": len(data), "seconds": receipt["seconds"]}))


if __name__ == "__main__":
    main()
