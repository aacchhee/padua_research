"""Bounded finite global-max certificate from rigorous all-n kernel enclosures."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import time
import finite_bernstein as b
import finite_general as g


def sources():
    folder = Path(__file__).parent
    return {name: b.digest(folder/name) for name in
            ("finite_bernstein.py", "finite_general.py", "finite_general_run.py", "finite_n2_exact.py")}


def run(n, seconds, boxes, depth):
    started = time.monotonic()
    assert g.self_test()
    coeffs, metadata = g.setup(n)
    setup_seconds = time.monotonic()-started
    pending = [("", ((F(-1), F(1)), (F(-1), F(1))), coeffs)]
    leaves, stats = [], Counter()
    threshold = metadata["threshold_interval"][0]
    corners = tuple(map(tuple, metadata["corners"]))
    search_started = time.monotonic()
    depth_limited = False
    while pending and stats["visited"] < boxes and time.monotonic()-search_started < seconds:
        path, box, coefficients = pending.pop()
        stats["visited"] += 1
        stats["maximum_depth"] = max(stats["maximum_depth"], len(path))
        v = b.verdict(coefficients, n, box, threshold, corners)
        if v is not None:
            leaves.append({"path": path, **v})
            stats[v["kind"]] += 1
        else:
            if len(path) >= depth:
                pending.append((path, box, coefficients))
                depth_limited = True
                break
            axis = len(path) % 2
            left, right = b.subdivide(coefficients, n, axis)
            lbox, rbox = b.split_box(box, axis)
            pending.extend(((path+"1", rbox, right), (path+"0", lbox, left)))
            stats["splits"] += 1
    return {"format": "padua-part3-general-certificate-v1", "source_head": b.PINNED_HEAD,
            "source_sha256": sources(), "setup_seconds": setup_seconds,
            "search_seconds": time.monotonic()-search_started, "total_seconds": time.monotonic()-started,
            "limits": {"seconds": seconds, "boxes": boxes, "depth": depth},
            "statistics": dict(stats), "leaves": leaves,
            "pending": [p for p, box, c in pending], "depth_limited": depth_limited,
            "complete": not pending, "accepted": False, **metadata}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--seconds", type=float, default=100)
    parser.add_argument("--boxes", type=int, default=200000)
    parser.add_argument("--depth", type=int, default=48)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert args.seconds > 0 and args.boxes > 0 and 0 < args.depth <= 100
    data = run(args.n, args.seconds, args.boxes, args.depth)
    payload = (json.dumps(data, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if args.output.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    args.output.write_bytes(payload)
    print(json.dumps({k: v for k, v in data.items() if k not in ("leaves", "pending", "pi_interval")}, sort_keys=True))
    print(json.dumps({"output_sha256": b.digest(args.output), "bytes": len(payload),
                      "pending_count": len(data["pending"])}))


if __name__ == "__main__":
    main()
