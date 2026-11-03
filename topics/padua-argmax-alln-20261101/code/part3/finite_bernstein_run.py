"""Bounded n=8 global-max-only Bernstein search; no stationary-point count."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import platform
import time
import finite_bernstein as b


def save(data, path):
    payload = (json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    path.write_bytes(payload)


def run(args):
    started = time.monotonic()
    assert b.self_test()
    coeffs, metadata = b.setup_n8()
    setup_seconds = time.monotonic()-started
    if args.setup_only:
        return {"format": "padua-part3-bernstein-preparation-v1", "source_head": b.PINNED_HEAD,
                "setup_seconds": setup_seconds, "mathematical_search_run": False,
                "initial_coefficient_intervals": sum(map(len, coeffs)), **metadata}
    threshold = metadata["threshold_interval"][0]
    corners = tuple(map(tuple, metadata["corners"]))
    n = metadata["n"]
    root = ((F(-1), F(1)), (F(-1), F(1)))
    pending = [("", root, coeffs)]
    leaves = []
    stats = Counter()
    search_started = time.monotonic()
    depth_limited = False
    while pending and stats["visited"] < args.boxes and time.monotonic()-search_started < args.seconds:
        path, box, coefficients = pending.pop()
        stats["visited"] += 1
        stats["maximum_depth"] = max(stats["maximum_depth"], len(path))
        accepted = b.verdict(coefficients, n, box, threshold, corners)
        if accepted is not None:
            stats[accepted["kind"]] += 1
            leaves.append({"path": path, **accepted})
        else:
            if len(path) >= args.depth:
                pending.append((path, box, coefficients))
                depth_limited = True
                break
            axis = len(path) % 2
            left, right = b.subdivide(coefficients, n, axis)
            lbox, rbox = b.split_box(box, axis)
            pending.extend(((path+"1", rbox, right), (path+"0", lbox, left)))
            stats["splits"] += 1
    complete = not pending
    sources = {"finite_bernstein.py": b.digest(Path(b.__file__)),
               "finite_bernstein_run.py": b.digest(Path(__file__)),
               "a5_n8_field.py": metadata["part2_field_sha256"]}
    return {"format": "padua-part3-bernstein-certificate-v1", "source_head": b.PINNED_HEAD,
            "python": platform.python_version(), "source_sha256": sources,
            "setup_seconds": setup_seconds, "search_seconds": time.monotonic()-search_started,
            "total_seconds": time.monotonic()-started,
            "limits": {"seconds": args.seconds, "boxes": args.boxes, "depth": args.depth},
            "statistics": dict(stats), "leaves": leaves,
            "pending": [path for path, box, c in pending],
            "depth_limited": depth_limited, "complete": complete,
            "accepted": False, "acceptance_requires_independent_replay": True,
            **metadata}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--boxes", type=int, default=200000)
    parser.add_argument("--depth", type=int, default=48)
    parser.add_argument("--setup-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert args.seconds > 0 and args.boxes > 0 and 0 < args.depth <= 100
    result = run(args)
    save(result, args.output)
    print(json.dumps({k: v for k, v in result.items() if k not in ("leaves", "pending")}, sort_keys=True))
    print(json.dumps({"output": str(args.output), "output_sha256": b.digest(args.output),
                      "bytes": args.output.stat().st_size,
                      "pending_count": len(result.get("pending", []))}))


if __name__ == "__main__":
    main()
