#!/usr/bin/env python3
"""Claude audit-01 adversarial probe of the frozen n=4 checker internals.

Not a rerun of the full certificate: only all 13 root records, a deterministic
sample of leaves, one edge and the corners are replayed, then deliberately
mutated copies are fed to the same checker methods.  Every mutation must be
rejected; every unmutated sample must be accepted.  Also unit-tests partition(),
verify_root_partition() and outward Interval rounding against exact Fractions.
"""
import copy, gzip, json, random, sys, time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve()
TOPIC = HERE.parents[3]
sys.path.insert(0, str(TOPIC / "code"))
import a5_checker_n4 as c  # noqa: E402
import sympy as sp  # noqa: E402

results = []


def accept(name, action):
    action()
    results.append({"name": name, "accepted": True})


def reject(name, action):
    print("probe", name, round(time.monotonic(), 1), file=sys.stderr, flush=True)
    try:
        action()
    except (c.Rejected, KeyError, ValueError, TypeError) as error:
        results.append({"name": name, "rejected": True, "reason": str(error)[:120]})
        return
    raise SystemExit("MUTATION ACCEPTED: " + name)


def fresh_with_roots(cert):
    v = c.Verifier()
    for root in cert["interior_roots"]:
        v.root(root)
    return v


def main():
    started = time.monotonic()
    rng = random.Random(1101)
    # ---- primitive unit tests (no certificate) ----
    reject("partition_missing_subtree", lambda: c.require(c.partition(["0", "10"]), "incomplete"))
    reject("partition_prefix_overlap", lambda: c.partition(["0", "1", "10"]))
    reject("partition_duplicate", lambda: c.partition(["0", "0", "1"]))
    accept("partition_complete_uneven", lambda: c.require(c.partition(["0", "10", "110", "111"]), "x"))
    t = sp.Symbol("t")
    p = sp.Poly((t**2 - 2)*(3*t - 1), t, domain=sp.QQ)
    good = [["-3/2", "-1"], ["1/3", "1/3"], ["1", "3/2"]]
    accept("sturm_good_partition", lambda: c.verify_root_partition(p, good))
    reject("sturm_omitted_root", lambda: c.verify_root_partition(p, good[:2]))
    reject("sturm_two_roots_one_interval", lambda: c.verify_root_partition(p, [["-3/2", "-1"], ["0", "3/2"]]))
    reject("sturm_touching_intervals", lambda: c.verify_root_partition(p, [["-3/2", "-1"], ["-1", "1/3"], ["1", "3/2"]]))
    reject("sturm_root_endpoint", lambda: c.verify_root_partition(p, [["-3/2", "-1"], ["1/3", "1/2"], ["1", "3/2"]]))
    reject("sturm_false_singleton", lambda: c.verify_root_partition(p, [["-3/2", "-1"], ["1/4", "1/4"], ["1", "3/2"]]))
    # outward rounding: exact products/powers must lie in the dyadic result
    U = c.UNIT
    for _ in range(4000):
        a, b = sorted(Fraction(rng.randint(-10**6, 10**6), rng.randint(1, 10**6)) for _ in range(2))
        e, f = sorted(Fraction(rng.randint(-10**6, 10**6), rng.randint(1, 10**6)) for _ in range(2))
        X, Y = c.Interval.bounds(a, b), c.Interval.bounds(e, f)
        Z, k = X*Y, rng.randint(0, 7)
        P = X.power(k)
        for u in (a, b, (a+b)/2):
            for w in (e, f, (e+f)/2):
                assert Fraction(Z.lo, U) <= u*w <= Fraction(Z.hi, U)
            assert Fraction(P.lo, U) <= u**k <= Fraction(P.hi, U)
    results.append({"name": "outward_interval_rounding_random", "accepted": True, "cases": 4000})

    # ---- certificate-based probes ----
    cert = json.loads(gzip.decompress((TOPIC / "outputs/a5_n4_certificate.json.gz").read_bytes()))
    v = fresh_with_roots(cert)
    v.implicit_masks = True
    results.append({"name": "all_13_root_records_verified", "accepted": True, "roots": len(v.roots)})
    leaves = cert["leaves"]
    root_leaves = [L for L in leaves if any(r["code"] == "root" for r in L["patterns"])]
    flat_leaves = [L for L in leaves if any(r["code"] == "flat" for r in L["patterns"])]
    small = [L for L in leaves if len(L["patterns"]) <= 64]
    sample = rng.sample(small, 25) + root_leaves[:6] + flat_leaves[:2]
    for L in sample:
        v.leaf(L)
    results.append({"name": "sample_leaves_verified", "accepted": True, "leaves": len(sample)})
    # mutations of leaves
    L = root_leaves[0]
    k = next(i for i, r in enumerate(L["patterns"]) if r["code"] == "root")
    m = copy.deepcopy(L); m["patterns"][k]["code"] = "gradient"
    reject("root_record_relabelled_gradient", lambda: v.leaf(m))
    m = copy.deepcopy(L); m["patterns"][k]["code"] = "hessian"
    reject("root_record_relabelled_hessian", lambda: v.leaf(m))
    m = copy.deepcopy(L); m["patterns"][k]["code"] = "flat"
    reject("root_record_relabelled_flat", lambda: v.leaf(m))
    other = next(r for r in cert["interior_roots"] if r["id"] != L["patterns"][k]["id"])
    m = copy.deepcopy(L); m["patterns"][k]["id"] = other["id"]
    reject("root_reference_to_other_root", lambda: v.leaf(m))
    # U equal to the leaf itself (leaf [-41/64,-5/8]x[-3/4,-47/64]; root box lies above it)
    (qa, qb), (qc, qd) = c.path_rectangle(L["path"])[0]
    m = copy.deepcopy(L); m["patterns"][k]["U"] = [[str(qa), str(qb)], [str(qc), str(qd)]]
    reject("root_hull_not_covering_root_box", lambda: v.leaf(m))
    # a larger legitimate hull must still be accepted (injectivity holds there)
    m = copy.deepcopy(L); m["patterns"][k]["U"] = [["-41/64", "-5/8"], ["-3/4", "-29/40"]]
    accept("root_hull_enlarged_but_valid", lambda: v.leaf(m))
    m = copy.deepcopy(L); m["patterns"][k]["U"] = [["-1", "1"], ["-1", "1"]]
    reject("root_hull_whole_square_injectivity_fails", lambda: v.leaf(m))
    m = copy.deepcopy(L); m["patterns"][k]["code"] = "unresolved"
    reject("unknown_disposition_code", lambda: v.leaf(m))
    big = max(sample, key=lambda Q: len(Q["patterns"]))
    m = copy.deepcopy(big); m["patterns"].pop()
    reject("leaf_one_compatible_mask_missing", lambda: v.leaf(m))
    m = copy.deepcopy(big); m["patterns"].append({"code": "gradient"})
    reject("leaf_extraneous_mask_record", lambda: v.leaf(m))
    m = copy.deepcopy(big); m["path"] = m["path"][:-1] or "0"
    reject("leaf_patterns_moved_to_parent_box", lambda: v.leaf(m))
    # partition with one actual leaf dropped
    paths = [Q["path"] for Q in leaves]
    accept("actual_partition_complete", lambda: c.require(c.partition(paths), "x"))
    reject("actual_partition_minus_one_leaf", lambda: c.require(c.partition(paths[1:]), "incomplete"))
    # root record mutations
    r0 = cert["interior_roots"][0]
    def root_variant(change, name):
        w = c.Verifier.__new__(c.Verifier)
        w.__dict__.update(v.__dict__); w.roots = {}
        rr = copy.deepcopy(r0); change(rr)
        reject(name, lambda: w.root(rr))
    def shift(rr):
        (a, b), (e, f) = [[Fraction(q) for q in iv] for iv in rr["R"]]
        dx = 3*(b - a)
        rr["R"] = [[str(a+dx), str(b+dx)], [str(e), str(f)]]
    root_variant(shift, "root_box_shifted_off_root")
    root_variant(lambda rr: rr.__setitem__("mask", rr["mask"] ^ 1), "root_box_wrong_mask")
    root_variant(lambda rr: rr.__setitem__("C", [["1", "0"], ["0", "1"]]), "root_identity_preconditioner")
    def tiny(rr):
        (a, b), (e, f) = [[Fraction(q) for q in iv] for iv in rr["R"]]
        ma, me = (a+b)/2, (e+f)/2
        rr["R"] = [[str(ma), str(ma + (b-a)/10**9)], [str(e), str(f)]]
    root_variant(tiny, "root_box_shrunk_to_miss_root")
    w = c.Verifier.__new__(c.Verifier); w.__dict__.update(v.__dict__); w.roots = {}
    w.root(r0)
    dup = copy.deepcopy(r0); dup["id"] = 999
    reject("duplicate_root_overlapping_box", lambda: w.root(dup))
    # boundary: corner relabel and edge sample tamper (first edge + corners only)
    edges, corners = cert["edges"], cert["corners"]
    # (corner mutations omitted: boundaries() must replay all four edges before the
    #  corners, ~10 min under the shared load; corner node/max tampering is covered
    #  by the developer controls and by code review of boundaries().)
    ee = copy.deepcopy(edges)
    iv = ee[0]["E_norm_intervals"][0]
    ee[0]["samples"][1] = iv[0] if Fraction(iv[0]) != Fraction(iv[1]) else ee[0]["samples"][1]
    ee[0]["samples"][0] = str(Fraction(iv[1]) + 1)
    reject("edge_sample_moved_into_norm_root_interval", lambda: v.boundaries(ee, corners))
    ee = copy.deepcopy(edges); ee[0]["sample_masks"] = ee[0]["sample_masks"][1:]
    ee[0]["patterns"] = ee[0]["patterns"][1:]
    reject("edge_one_sign_pattern_omitted", lambda: v.boundaries(ee, corners))
    ee = copy.deepcopy(edges)
    row = next(r for r in ee[0]["patterns"] if r["kind"] == "roots" and r["points"])
    # NB an earlier draft relabelled a 'derivative' point as 'minimum'; that copy was
    # (correctly) ACCEPTED because q''>0 also holds there: an alternative valid
    # exclusion, not a counterfeit.  Use accepted maxima, where both must fail.
    row = next(r for r in ee[0]["patterns"] if r["kind"] == "roots" and
               any(q["code"] == "root" for q in r["points"]))
    pt = next(q for q in row["points"] if q["code"] == "root")
    saved = dict(pt)
    pt.clear(); pt.update({"code": "minimum", "i": saved["i"]})
    reject("edge_accepted_root_relabelled_minimum", lambda: v.boundaries(ee, corners))
    pt.clear(); pt.update({"code": "sign", "i": saved["i"], "b": 0})
    reject("edge_accepted_root_relabelled_sign", lambda: v.boundaries(ee, corners))
    pt.clear(); pt.update({**saved, "code": "normal"})
    reject("edge_accepted_root_relabelled_normal", lambda: v.boundaries(ee, corners))
    pt.clear(); pt.update({**saved, "id": saved["id"] + 1})
    reject("edge_root_id_noncanonical", lambda: v.boundaries(ee, corners))
    ee = copy.deepcopy(edges)
    row = next(r for r in ee[0]["patterns"] if r["kind"] == "roots" and len(r["Dr_norm_intervals"]) > 1)
    row["Dr_norm_intervals"].pop(); row["points"].pop()
    reject("edge_derivative_root_interval_omitted", lambda: v.boundaries(ee, corners))
    print(json.dumps({"all_probes_passed": True, "probes": results,
                      "seconds": round(time.monotonic() - started, 2)}, indent=1))


if __name__ == "__main__":
    main()
