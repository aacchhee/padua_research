"""Replay a general-kernel Bernstein prefix certificate, including partial ones."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import time
import finite_bernstein as b
import finite_general as g


def check(data):
    assert data["format"] == "padua-part3-general-certificate-v1"
    assert data["source_head"] == b.PINNED_HEAD
    folder = Path(__file__).parent
    assert data["source_sha256"] == {name: b.digest(folder/name) for name in
            ("finite_bernstein.py", "finite_general.py", "finite_general_run.py", "finite_n2_exact.py")}
    assert g.self_test()
    coeffs, metadata = g.setup(data["n"])
    assert all(data[key] == value for key, value in metadata.items())
    threshold = metadata["threshold_interval"][0]
    corners = tuple(map(tuple, metadata["corners"]))
    n = metadata["n"]
    leaves, pending = {}, set()
    for row in data["leaves"]:
        p = row["path"]
        assert isinstance(p, str) and set(p) <= {"0", "1"} and len(p) <= 100
        assert p not in leaves
        leaves[p] = row
    for p in data["pending"]:
        assert isinstance(p, str) and set(p) <= {"0", "1"} and len(p) <= 100
        assert p not in pending and p not in leaves
        pending.add(p)
    frontier = set(leaves) | pending
    assert frontier
    ancestors = set()
    for p in frontier:
        for k in range(len(p)):
            assert p[:k] not in frontier
            ancestors.add(p[:k])
    counts, reached, corner_leaves = Counter(), set(), set()
    stack = [("", ((F(-1), F(1)), (F(-1), F(1))), coeffs)]
    while stack:
        p, box, coefficients = stack.pop()
        if p in leaves:
            v = b.verdict(coefficients, n, box, threshold, corners)
            assert v is not None and leaves[p] == {"path": p, **v}
            counts[v["kind"]] += 1
            if v["kind"] == "corner":
                corner_leaves.add(tuple(v["corner"]))
            reached.add(p)
        elif p in pending:
            counts["pending"] += 1
            reached.add(p)
        else:
            assert p in ancestors, "uncovered box"
            axis = len(p) % 2
            left, right = b.subdivide(coefficients, n, axis)
            lbox, rbox = b.split_box(box, axis)
            stack.extend(((p+"1", rbox, right), (p+"0", lbox, left)))
            counts["splits"] += 1
    assert reached == frontier
    assert data["complete"] == (not pending)
    assert data["accepted"] is False
    for key in ("bound", "corner", "splits"):
        assert data["statistics"].get(key, 0) == counts[key]
    if not pending:
        assert corner_leaves == set(corners)
    return {"n": n, "accepted": not pending, "complete_partition": True,
            "all_supplied_bounds_verified": True, "counts": dict(counts),
            "verified_claim": ("only the two non-node corners attain the global maximum"
                               if not pending else "partial bounds only")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    payload = args.certificate.read_bytes()
    if args.certificate.suffix == ".gz":
        payload = gzip.decompress(payload)
    result = check(json.loads(payload))
    result.update(format="padua-part3-general-check-v1", certificate_sha256=b.digest(args.certificate),
                  checker_sha256=b.digest(Path(__file__)), seconds=time.monotonic()-started)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
