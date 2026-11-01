"""Adversarial replay controls on an actual complete general certificate.

The fresh exact constructor result is cached for these repeated defect
checks only. Discovery/checker source files are never edited.
"""
import argparse
import copy
import gzip
import json
from pathlib import Path
import time
import finite_bernstein as b
import finite_general as g
import finite_general_check as checker


def controls(data):
    started = time.monotonic()
    n = data["n"]
    sources = {p.name: b.digest(p) for p in
               (Path(b.__file__), Path(g.__file__), Path(checker.__file__), Path(__file__))}
    original = g.setup
    cached = original(n)

    def setup(k):
        assert k == n
        return cached

    g.setup = setup
    rejected = []
    try:
        assert checker.check(data)["accepted"]

        def reject(name, mutate):
            changed = copy.deepcopy(data)
            mutate(changed)
            try:
                checker.check(changed)
            except (AssertionError, KeyError, ValueError):
                rejected.append(name)
            else:
                raise AssertionError("deliberate defect accepted: "+name)

        bound = next(i for i, row in enumerate(data["leaves"]) if row["kind"] == "bound")
        corner = next(i for i, row in enumerate(data["leaves"]) if row["kind"] == "corner")
        reject("missing_leaf", lambda d: d["leaves"].pop(bound))
        reject("duplicate_leaf", lambda d: d["leaves"].append(copy.deepcopy(d["leaves"][bound])))
        reject("forged_bound", lambda d: d["leaves"][bound].update(upper=0))
        reject("forged_corner", lambda d: d["leaves"][corner].update(corner=[1, 1]))
        reject("changed_threshold", lambda d: d["threshold_interval"].__setitem__(0, 1))
        reject("changed_pi_bracket", lambda d: d["pi_interval"].__setitem__(0, "3"))
        reject("changed_source", lambda d: d["source_sha256"].update({"finite_general.py": "0"*64}))
        reject("changed_dependency", lambda d: d.update(dependency_sha256="0"*64))
        reject("false_complete_flag", lambda d: d.update(complete=False))
        reject("producer_self_approval", lambda d: d.update(accepted=True))
        reject("pending_leaf_overlap", lambda d: d["pending"].append(d["leaves"][bound]["path"]))
        reject("ancestor_overlap", lambda d: d["pending"].append(""))
        reject("invalid_path_character", lambda d: d["leaves"][bound].update(path="X"))
        reject("wrong_counter", lambda d: d["statistics"].update(bound=-1))
        partial = copy.deepcopy(data)
        row = partial["leaves"].pop(bound)
        partial["pending"].append(row["path"])
        partial["statistics"]["bound"] -= 1
        partial["complete"] = False
        result = checker.check(partial)
        assert not result["accepted"] and result["all_supplied_bounds_verified"]
    finally:
        g.setup = original
    assert sources == {p.name: b.digest(p) for p in
                       (Path(b.__file__), Path(g.__file__), Path(checker.__file__), Path(__file__))}
    return {"format": "padua-part3-general-controls-v1", "n": n,
            "negative_cases_rejected": rejected, "negative_count": len(rejected),
            "positive_complete_accepted": True, "positive_partial_not_accepted": True,
            "source_hashes_unchanged": True, "source_sha256": sources,
            "seconds": time.monotonic()-started}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = args.certificate.read_bytes()
    if args.certificate.suffix == ".gz":
        payload = gzip.decompress(payload)
    result = controls(json.loads(payload))
    result["certificate_sha256"] = b.digest(args.certificate)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
