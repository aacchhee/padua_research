"""Replay every n=8 Bernstein leaf and the full binary prefix partition.

This checker reconstructs the exact cardinals/embedding and outward
coefficients; it does not trust stored bounds, counters, or complete flags.
It shares arithmetic with the producer but does not call its search.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import time
import finite_bernstein as b


def check(data):
    assert data["format"] == "padua-part3-bernstein-certificate-v1"
    assert data["source_head"] == b.PINNED_HEAD
    assert data["source_sha256"] == {
        "finite_bernstein.py": b.digest(Path(b.__file__)),
        "finite_bernstein_run.py": b.digest(Path(__file__).with_name("finite_bernstein_run.py")),
        "a5_n8_field.py": b.digest(b.PART2 / "a5_n8_field.py")}
    assert b.self_test()
    coeffs, metadata = b.setup_n8()
    assert all(data[key] == value for key, value in metadata.items())
    threshold = metadata["threshold_interval"][0]
    corners = tuple(map(tuple, metadata["corners"]))
    n = metadata["n"]
    leaves = data["leaves"]
    assert isinstance(leaves, list)
    by_path = {}
    for row in leaves:
        path = row["path"]
        assert isinstance(path, str) and set(path) <= {"0", "1"}
        assert path not in by_path
        by_path[path] = row
    pending = data["pending"]
    assert isinstance(pending, list) and len(pending) == len(set(pending))
    assert all(isinstance(p, str) and set(p) <= {"0", "1"} for p in pending)
    assert not set(pending) & set(by_path)
    frontier = set(pending) | set(by_path)
    assert frontier
    ancestors = set()
    for path in frontier:
        assert len(path) <= 100
        for k in range(len(path)):
            assert path[:k] not in frontier, "frontier is not prefix-free"
            ancestors.add(path[:k])
    counts = Counter()
    stack = [("", ((F(-1), F(1)), (F(-1), F(1))), coeffs)]
    reached = set()
    corner_leaves = set()
    while stack:
        path, box, coefficients = stack.pop()
        if path in by_path:
            row = by_path[path]
            v = b.verdict(coefficients, n, box, threshold, corners)
            assert v is not None and row == {"path": path, **v}, "invalid/relabelled bound"
            counts[v["kind"]] += 1
            if v["kind"] == "corner":
                corner_leaves.add(tuple(v["corner"]))
            reached.add(path)
        elif path in pending:
            counts["pending"] += 1
            reached.add(path)
        else:
            assert path in ancestors, "uncovered box"
            left, right = b.subdivide(coefficients, n, len(path) % 2)
            lbox, rbox = b.split_box(box, len(path) % 2)
            stack.extend(((path+"1", rbox, right), (path+"0", lbox, left)))
            counts["splits"] += 1
    assert reached == frontier
    assert data["complete"] == (not pending)
    accepted = not pending
    if accepted:
        assert corner_leaves == set(corners)
    assert data["accepted"] is False  # Producer must never self-approve.
    # Search may have popped/reinserted one unresolved depth-limit box.
    assert data["statistics"]["bound"] == counts["bound"]
    assert data["statistics"].get("corner", 0) == counts["corner"]
    assert data["statistics"]["splits"] == counts["splits"]
    return {"accepted": accepted, "complete_partition": True,
            "all_supplied_bounds_verified": True, "counts": dict(counts),
            "verified_claim": ("lambda_8 maximum occurs only at the two non-node corners"
                               if accepted else "partial bounds only; no global maximum claim")}


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
    result.update(format="padua-part3-bernstein-check-v1",
                  certificate_sha256=b.digest(args.certificate),
                  checker_sha256=b.digest(Path(__file__)),
                  seconds=time.monotonic()-started)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
