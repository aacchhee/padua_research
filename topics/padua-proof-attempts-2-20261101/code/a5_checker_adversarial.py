#!/usr/bin/env python3
"""Small negative controls for the independent A5 certificate checker.

Each mutation destroys a required completeness or algebraic obligation.
This complements, and does not replace, verification of the unaltered artifact.
"""
import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import sys

import a5_checker as checker


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    data = json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
    cards = checker.reconstruct()
    results = []

    def reject(name, action):
        try:
            action()
        except (checker.Invalid, KeyError, ValueError, TypeError, ZeroDivisionError) as error:
            results.append({"mutation": name, "rejected": True, "reason": str(error)})
        else:
            raise AssertionError(f"invalid certificate mutation was accepted: {name}")

    def pattern_case(name, change):
        records = copy.deepcopy(data["patterns"])
        change(records)
        reject(name, lambda: checker.check_patterns(records, cards, checker.Encloser()))

    residual_index = next(i for i, p in enumerate(data["patterns"])
                          if p["kind"] == "residual")
    pattern_case("one complete sign pattern omitted", lambda ps: ps.pop())
    pattern_case("ordered sign pattern replaced by a duplicate", lambda ps: ps.__setitem__(0, ps[1]))
    pattern_case("gradient factor identity altered", lambda ps: ps[residual_index].__setitem__(
        "g", [[10, 0, "1", "0"], [0, 0, "1", "0"]]))
    pattern_case("one real projected coordinate root omitted",
                 lambda ps: ps[residual_index]["xroots"].pop())
    pattern_case("one Cartesian pair disposition omitted",
                 lambda ps: ps[residual_index]["pairs"].pop())
    pattern_case("pair disposition changed to unknown assertion",
                 lambda ps: ps[residual_index]["pairs"][0].__setitem__("code", "assume_empty"))

    edges = copy.deepcopy(data["edges"])
    edges.pop()
    reject("one entire edge omitted", lambda: checker.check_edges(edges, cards, checker.Encloser()))
    edges = copy.deepcopy(data["edges"])
    edges[0]["patterns"].pop()
    reject("one canonical edge sign pattern omitted",
           lambda: checker.check_edges(edges, cards, checker.Encloser()))
    edges = copy.deepcopy(data["edges"])
    j = next(j for j, p in enumerate(edges[0]["patterns"]) if p["kind"] == "roots")
    edges[0]["patterns"][j]["points"].pop()
    reject("one edge root disposition omitted",
           lambda: checker.check_edges(edges, cards, checker.Encloser()))

    corners = copy.deepcopy(data["corners"])
    corners.pop()
    reject("one corner omitted", lambda: checker.check_corners(corners, cards, checker.Encloser()))
    corners = copy.deepcopy(data["corners"])
    j = next(j for j, corner in enumerate(corners) if corner["kind"] == "max")
    corners[j]["kind"] = "node"
    reject("a nonnode corner asserted to be a node",
           lambda: checker.check_corners(corners, cards, checker.Encloser()))

    if "global" in data:
        altered = copy.deepcopy(data)
        altered["global"]["flat"].pop()
        reject("one flat-pattern global bound omitted",
               lambda: checker.check_global(altered, {}, cards, checker.Encloser()))
        altered = copy.deepcopy(data)
        altered["global"]["flat"][0]["panels"].pop()
        reject("one flat-bound covering panel omitted",
               lambda: checker.check_global(altered, {}, cards, checker.Encloser()))
        altered = copy.deepcopy(data)
        altered["global"]["flat"][0]["panels"][0]["upper"] = "-100"
        reject("a false flat-panel numerical upper bound supplied",
               lambda: checker.check_global(altered, {}, cards, checker.Encloser()))

    output = {"all_mutations_rejected": True, "negative_controls": results,
              "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "checker_sha256": hashlib.sha256(Path(checker.__file__).read_bytes()).hexdigest(),
              "adversarial_runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
