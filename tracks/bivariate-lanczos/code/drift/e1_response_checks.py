#!/usr/bin/env python3
"""Response-01 checks for the E1 records (audit findings E1-F1, E1-F2, E1-F3, E1-F4).

Decisions use exact arithmetic only (python-flint fmpq / fractions.Fraction); floats
appear only as display values next to the exact data.

This checker does NOT modify or replace the committed producers. It IMPORTS the
producer e1_exact.py (build/points/bounds) so that the pivot sequence and the basis
are the producer's own; the tie detection and the B^T B = D check are therefore
checks of the committed construction, not an independent reimplementation (the
independent reimplementation is the audit-01 work under checks/audit-01/scripts/E1/).
The producer's own `max` selection is observed through a module-level `max` hook
(the producer file stays byte-identical).

Checks
  a  E1-F1  exact pivot ties in the pivot-adaptive rule, both grids, degrees 2..12,
            the T24 minimum relative margin, the rotQ24 (2,1) tie and its symmetry
            cause, and the exact effect of resolving the tie to Y (degree 12).
  b  E1-F2  exact B^T B = D (pairwise orthogonality of the unnormalised columns,
            d_k = ||b_k||^2) and the recurrence identity at degree 12 for the four
            decisive cases (T24 bj, T24 pivot, rotQ24 bj, rotQ24 alt; plus extras).
  c  E1-F3  the six inequalities stated in record 04, their integer-threshold chain,
            the factor-100 criterion, and the original KHS-only INCONCLUSIVE verdict,
            from the committed rationals of e1-full-sweep.json.
  d  E1-F4  exact DEAD-clause history over all degrees (original KHS rule and the
            sharpened U = min(KHS, Urow) rule), plus committed-freeze provenance.
"""
import argparse
import builtins
import hashlib
import io
import contextlib
import json
import platform
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)

import flint  # noqa: E402
from flint import fmpq, fmpq_mat  # noqa: E402
import e1_exact  # noqa: E402  (producer; NOT independent)

REPO = Path(__file__).resolve().parents[4]
TOPIC = REPO / "topics" / "padua-lanczos-drift-20261101"
SWEEP = TOPIC / "evidence" / "e1-full-sweep.json"
DEFAULT_OUT = TOPIC / "evidence" / "response-01-e1-checks.json"
SETS = ["triangle", "rotated"]
SET_LABEL = {"triangle": "T24", "rotated": "rotQ24"}


def F(q):
    return Fraction(int(q.numerator), int(q.denominator))


def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def column_labels(degree):
    return [(t, j) for t in range(1, degree + 1) for j in range(t + 1)]


# ----------------------------------------------------------------------------
# (a) pivot ties
# ----------------------------------------------------------------------------
class SelectionRecorder:
    """Module-level `max` hook for e1_exact.build: observes every candidate
    selection (the only call of max with key=... inside build) and delegates
    the choice to the producer rule, or to the Y-on-tie variant if requested."""

    def __init__(self, prefer_y_on_tie=False):
        self.records = []
        self.prefer_y = prefer_y_on_tie

    def __call__(self, *args, **kw):
        if "key" not in kw:
            return builtins.max(*args)
        cands = list(args[0])
        self.records.append([(c[0], c[1], c[4], c[6]) for c in cands])
        if self.prefer_y:
            return builtins.max(cands, key=lambda c: (c[0], c[1]))
        return builtins.max(cands, key=kw["key"])


def pivot_build(set_name, degree, prefer_y=False):
    rec = SelectionRecorder(prefer_y)
    e1_exact.max = rec
    try:
        out = quiet(e1_exact.build, e1_exact.points(set_name), degree, "pivot")
    finally:
        del e1_exact.max
    return out, rec


def tie_analysis(set_name, sweep_rows):
    t0 = time.time()
    (coords, b, d, rec_rows, meta), rec = pivot_build(set_name, 12)
    labels = column_labels(12)
    assert len(rec.records) == len(labels) == len(b) - 1
    cols = []
    for (t, j), cands in zip(labels, rec.records):
        if len(cands) == 1:
            continue
        (sX, aX, sigX, dkX), (sY, aY, sigY, dkY) = cands
        assert aX == 0 and aY == 1
        assert dkX == dkY, "monic residual must coincide for both candidates"
        sx, sy = F(sigX), F(sigY)
        cols.append({"t": t, "j": j, "tie": bool(sigX == sigY and sX == sY),
                     "margin": abs(sx - sy) / (sx + sy)})
    per_degree = {}
    for n in range(2, 13):
        used = [c for c in cols if c["t"] <= n]
        tied = [c for c in used if c["tie"]]
        untied = [c for c in used if not c["tie"]]
        entry = {"two_candidate_columns": len(used),
                 "tied_columns": [[c["t"], c["j"]] for c in tied]}
        if untied:
            m = min(untied, key=lambda c: c["margin"])
            entry["min_relative_margin_over_untied_columns"] = {
                "float": float(m["margin"]), "column": [m["t"], m["j"]]}
            if n == 12:
                entry["min_relative_margin_over_untied_columns"]["exact"] = str(m["margin"])
        per_degree[str(n)] = entry
    # the producer's committed choices at each degree are prefixes of this sequence
    choices = ["XY"[r[0]] for r in rec_rows[1:]]
    prefix_ok = {}
    for n in range(2, 13):
        row = [r for r in sweep_rows if r["set"] == set_name and r["degree"] == n and r["rule"] == "pivot"]
        assert len(row) == 1
        N = (n + 1) * (n + 2) // 2
        prefix_ok[str(n)] = (row[0]["pivot_choices"] == choices[:N - 1])
    out = {"per_degree": per_degree,
           "tie_columns_at_degree_12": [[c["t"], c["j"]] for c in cols if c["tie"]],
           "producer_rebuilt_pivot_choices_equal_committed_sweep_for_every_degree": all(prefix_ok.values()),
           "elapsed_seconds": time.time() - t0}
    return out, (coords, b, d, rec_rows, meta), choices


def symmetry_cause(set_name, built):
    """Exact test of the cause of the rotQ24 (2,1) tie."""
    coords, b, d, rec_rows, meta = built
    pts = e1_exact.points(set_name)
    P = {(p[0], p[1]) for p in pts}
    rot = {(-p[1], p[0]) for p in pts}
    # columns: 0:(0,0) 1:(1,0)=x 2:(1,1)=y 3:(2,0) 4:(2,1) 5:(2,2)
    assert meta[1] == (1, 0) and meta[2] == (1, 1) and meta[4] == (2, 1)
    x = [p[0] for p in pts]
    y = [p[1] for p in pts]
    bx_is_x = all(b[1][0, i] == x[i] for i in range(len(pts)))
    by_is_y = all(b[2][0, i] == y[i] for i in range(len(pts)))
    # both candidate products for column (2,1): x*b_(1,1) and y*b_(1,0)
    prodX = [x[i] * b[2][0, i] for i in range(len(pts))]
    prodY = [y[i] * b[1][0, i] for i in range(len(pts))]
    return {"node_set_invariant_under_rotation_by_90_degrees": P == rot,
            "b_(1,0)_equals_x": bx_is_x,
            "b_(1,1)_equals_y": by_is_y,
            "candidate_products_x*b_(1,1)_and_y*b_(1,0)_identical_vectors": prodX == prodY}


def tie_break_effect(sweep_rows):
    """rotQ24 pivot degree 12 with the (2,1) tie resolved to Y instead of X:
    exact bounds from the producer's own bounds(), compared with committed X-tie values."""
    t0 = time.time()
    rec = SelectionRecorder(prefer_y_on_tie=True)
    e1_exact.max = rec
    try:
        res = quiet(e1_exact.bounds, e1_exact.points("rotated"), 12, "pivot", "all")
    finally:
        del e1_exact.max
    com = [r for r in sweep_rows if r["set"] == "rotated" and r["degree"] == 12 and r["rule"] == "pivot"][0]
    out = {"choices_Y_tie_break": "".join(res["pivot_choices"]),
           "choices_committed_X_tie_break": "".join(com["pivot_choices"])}
    diff = [i + 1 for i, (a, c) in enumerate(zip(out["choices_Y_tie_break"], out["choices_committed_X_tie_break"])) if a != c]
    out["differing_column_indices_1based"] = diff
    for key in ["Knode_squared", "KHS_squared", "Urow_squared", "upper_squared"]:
        y = Fraction(res[key]["exact"])
        x = Fraction(com[key]["exact"])
        out[key] = {"Y_tie_exact": str(y), "X_tie_committed_exact": str(x),
                    "ratio_Y_over_X_float": float(y / x),
                    "Y_tie_float": float(y), "X_tie_float": float(x)}
    out["elapsed_seconds"] = time.time() - t0
    return out


# ----------------------------------------------------------------------------
# (b) B^T B = D
# ----------------------------------------------------------------------------
def gram_check(set_name, rule):
    t0 = time.time()
    xy = e1_exact.points(set_name)
    coords, b, d, rec, meta = quiet(e1_exact.build, xy, 12, rule)
    M, N = len(xy), len(b)
    B = fmpq_mat(N, M, [b[k][0, i] for k in range(N) for i in range(M)])
    G = B * B.transpose()
    off_zero = all(G[k, l] == 0 for k in range(N) for l in range(N) if k != l)
    diag_ok = all(G[k, k] == d[k] for k in range(N))
    d_positive = all(d[k] > 0 for k in range(N))
    # recurrence identity b_k = A_k b_parent - sum_l alpha_kl b_l, exactly at all nodes
    rec_ok = True
    for k in range(1, N):
        axis, parent, alpha, _sigma = rec[k]
        for i in range(M):
            lhs = b[k][0, i]
            r = coords[axis][i] * b[parent][0, i]
            for l in range(k):
                if alpha[l]:
                    r -= alpha[l] * b[l][0, i]
            if lhs != r:
                rec_ok = False
                break
        if not rec_ok:
            break
    # consequence of B^T B = D: P = B D^-1 B^T is an orthogonal projector of rank N
    trace = sum((b[k][0, i] ** 2 / d[k] for i in range(M) for k in range(N)), fmpq(0))
    return {"set": SET_LABEL[set_name], "rule": rule, "points": M, "columns": N,
            "BtB_offdiagonal_all_zero": off_zero,
            "BtB_diagonal_equals_d_k": diag_ok,
            "all_d_k_positive": d_positive,
            "recurrence_identity_exact_at_all_nodes": rec_ok,
            "consequence_trace_of_projector_equals_N": trace == N,
            "result": "PASS" if (off_zero and diag_ok and d_positive and rec_ok and trace == N) else "FAIL",
            "elapsed_seconds": time.time() - t0}


# ----------------------------------------------------------------------------
# (c) record-04 inequalities
# ----------------------------------------------------------------------------
def decisive_inequalities(sweep_rows):
    R = {(r["set"], r["degree"], r["rule"]): r for r in sweep_rows}

    def q(s, rule, key, n=12):
        return Fraction(R[s, n, rule][key]["exact"])

    T, Q = "triangle", "rotated"
    LT = q(T, "bj", "Knode_squared")
    UTp = q(T, "pivot", "upper_squared")
    UTa = q(T, "alt", "upper_squared")
    KT_p = q(T, "pivot", "KHS_squared")
    LQ = q(Q, "bj", "Knode_squared")
    UQa = q(Q, "alt", "upper_squared")
    UQp = q(Q, "pivot", "upper_squared")
    UrowQa = q(Q, "alt", "Urow_squared")
    KQa = q(Q, "alt", "KHS_squared")
    KQp = q(Q, "pivot", "KHS_squared")

    stated = {
        "(1) T24: kappa_BJ^2 > 200000000000000  [L_BJ^2 = Knode^2 > 2e14]": LT > 200000000000000,
        "(2) T24: kappa_pivot^2 < 170000000  [U_pivot^2 < 1.7e8]": UTp < 170000000,
        "(3) T24: kappa_BJ > 1000 kappa_pivot  [exact: L_BJ^2 > 1000^2 U_pivot^2]": LT > 1000 ** 2 * UTp,
        "(4) rotQ24: kappa_BJ^2 > 88000000000  [L_BJ^2 > 8.8e10]": LQ > 88000000000,
        "(5) rotQ24: kappa_alt^2 < 642000000  [U_alt^2 < 6.42e8]": UQa < 642000000,
        "(6) rotQ24: kappa_BJ > 11 kappa_alt  [exact: L_BJ^2 > 11^2 U_alt^2]": LQ > 11 ** 2 * UQa,
    }
    chain = {
        "T24 integer chain: 2e14 > 1000^2 * 1.7e8": 200000000000000 > 1000 ** 2 * 170000000,
        "rotQ24 integer chain: 8.8e10 > 11^2 * 6.42e8": 88000000000 > 11 ** 2 * 642000000,
    }
    comparators = {
        "T24: best comparator by sharpened upper is pivot": UTp < UTa,
        "T24: pivot upper is the KHS bound (KHS <= Urow)": UTp == KT_p,
        "rotQ24: best comparator by sharpened upper is alt": UQa < UQp,
        "rotQ24: alt upper is the Urow bound (Urow < KHS)": UQa == UrowQa and UrowQa < KQa,
        "rotQ24: best comparator by KHS alone is alt": KQa < KQp,
    }
    factor100 = {
        "T24 sharpened: L_BJ^2 > 100 min(U_alt^2, U_pivot^2)": LT > 100 * min(UTa, UTp),
        "rotQ24 sharpened: L_BJ^2 > 100 min(U_alt^2, U_pivot^2)": LQ > 100 * min(UQa, UQp),
        "T24 original KHS-only: L_BJ^2 > 100 min(KHS_alt^2, KHS_pivot^2)":
            LT > 100 * min(q(T, "alt", "KHS_squared"), KT_p),
        "rotQ24 original KHS-only: L_BJ^2 > 100 min(KHS_alt^2, KHS_pivot^2) is FALSE (INCONCLUSIVE)":
            not (LQ > 100 * min(KQa, KQp)),
    }
    ratios = {
        "T24_Lsq_over_best_Usq": {"float": float(LT / UTp), "in_1269287_1269288": 1269287 < LT / UTp < 1269288,
                                   "kappa_ratio_exceeds_1126": LT > 1126 ** 2 * UTp,
                                   "kappa_ratio_below_1127": LT < 1127 ** 2 * UTp},
        "rotQ24_Lsq_over_best_Usq_sharpened": {"float": float(LQ / UQa),
                                               "in_137.36_137.37": Fraction(13736, 100) < LQ / UQa < Fraction(13737, 100),
                                               "kappa_ratio_exceeds_11.72": LQ * 10000 > 1172 ** 2 * UQa,
                                               "kappa_ratio_below_11.73": LQ * 10000 < 1173 ** 2 * UQa},
        "rotQ24_Lsq_over_best_KHS_only": {"float": float(LQ / KQa),
                                          "in_62.16_62.17": Fraction(6216, 100) < LQ / KQa < Fraction(6217, 100)},
    }
    margins = {
        "rotQ24_U_alt_sq_vs_6.42e8_relative_headroom": {
            "float": float((Fraction(642000000) - UQa) / 642000000),
            "note": "exact but only a few hundredths of a percent below the stated threshold"},
        "T24_U_pivot_sq_vs_1.7e8_relative_headroom": {"float": float((Fraction(170000000) - UTp) / 170000000)},
        "rotQ24_L_BJ_sq_vs_8.8e10_relative_headroom": {"float": float((LQ - 88000000000) / 88000000000)},
        "T24_L_BJ_sq_vs_2e14_relative_headroom": {"float": float((LT - 200000000000000) / 200000000000000)},
    }
    allbool = list(stated.values()) + list(chain.values()) + list(comparators.values()) + list(factor100.values())
    for r in ratios.values():
        allbool += [v for v in r.values() if isinstance(v, bool)]
    return {"stated_inequalities_record_04": stated, "integer_threshold_chain": chain,
            "best_comparator_identification": comparators, "factor_100_criterion": factor100,
            "ratios": ratios, "headroom": margins,
            "result": "PASS" if all(allbool) else "FAIL"}


# ----------------------------------------------------------------------------
# (d) DEAD-clause history and freeze provenance
# ----------------------------------------------------------------------------
def dead_history(sweep_rows):
    R = {(r["set"], r["degree"], r["rule"]): r for r in sweep_rows}

    def q(s, n, rule, key):
        return Fraction(R[s, n, rule][key]["exact"])

    out = {}
    for s in SETS:
        fired = {"original_KHS_DEAD_c1_or_c2": [], "original_KHS_DEAD_c1": [], "original_KHS_DEAD_c2": [],
                 "sharpened_U_DEAD_c1_or_c2": [], "sharpened_U_DEAD_c1": [], "sharpened_U_DEAD_c2": [],
                 "SURVIVES_original_KHS": [], "SURVIVES_sharpened_U": []}
        for n in range(2, 13):
            b_khs, b_u, b_l = (q(s, n, "bj", "KHS_squared"), q(s, n, "bj", "upper_squared"),
                               q(s, n, "bj", "Knode_squared"))
            goods = ["alt", "pivot"]
            c1o = any(b_khs <= q(s, n, g, "Knode_squared") for g in goods)
            c2o = all(b_khs < 100 * q(s, n, g, "Knode_squared") for g in goods)
            c1s = any(b_u <= q(s, n, g, "Knode_squared") for g in goods)
            c2s = all(b_u < 100 * q(s, n, g, "Knode_squared") for g in goods)
            so = b_l > 100 * min(q(s, n, g, "KHS_squared") for g in goods)
            ss = b_l > 100 * min(q(s, n, g, "upper_squared") for g in goods)
            for key, val in [("original_KHS_DEAD_c1_or_c2", c1o or c2o), ("original_KHS_DEAD_c1", c1o),
                             ("original_KHS_DEAD_c2", c2o), ("sharpened_U_DEAD_c1_or_c2", c1s or c2s),
                             ("sharpened_U_DEAD_c1", c1s), ("sharpened_U_DEAD_c2", c2s),
                             ("SURVIVES_original_KHS", so), ("SURVIVES_sharpened_U", ss)]:
                if val:
                    fired[key].append(n)
        out[SET_LABEL[s]] = fired
    return out


def freeze_provenance():
    info = {}
    def show(rev):
        return subprocess.run(["git", "show", f"{rev}:topics/padua-lanczos-drift-20261101/evidence/e1-freeze.json"],
                              cwd=REPO, capture_output=True, check=True).stdout
    try:
        for rev in ["6920ba6", "c89eb6a"]:
            raw = show(rev)
            js = json.loads(raw)
            info[rev] = {"blob_sha256": hashlib.sha256(raw).hexdigest(),
                         "frozen_before_run": js.get("frozen_before_run"),
                         "has_additional_upper_bound_Urow": "additional_upper_bound" in js,
                         "dead_field": js.get("dead")}
        head = json.loads((TOPIC / "evidence" / "e1-freeze.json").read_text())
        info["HEAD_working_tree"] = {"sha256": sha256_file(TOPIC / "evidence" / "e1-freeze.json"),
                                     "dead_field": head.get("dead"),
                                     "has_amendment_audit": "amendment_audit" in head}
        info["dead_field_changed_between_6920ba6_and_c89eb6a"] = info["6920ba6"]["dead_field"] != info["c89eb6a"]["dead_field"]
    except Exception as exc:  # git unavailable: provenance is informational only
        info = {"error": repr(exc)}
    return info


# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(DEFAULT_OUT))
    ap.add_argument("--skip-tie-break-bounds", action="store_true",
                    help="skip the ~4 minute rotQ24 degree-12 bounds run with the (2,1) tie resolved to Y")
    args = ap.parse_args()
    start = time.time()
    sweep = json.loads(SWEEP.read_text())
    rows = sweep["runs"]
    result = {
        "purpose": "Claude response-01 checks answering audit-01 E1-F1, E1-F2, E1-F3 (and the E1-F4 DEAD-history fact)",
        "independence": "imports the committed producer e1_exact.py (build/points/bounds); NOT an independent reimplementation",
        "command": "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 "
                   "tracks/bivariate-lanczos/code/drift/e1_response_checks.py --output " + str(args.output),
        "code_sha256": sha256_file(__file__),
        "producer_e1_exact_sha256": sha256_file(Path(e1_exact.__file__)),
        "producer_sha256_equals_committed_sweep_rows": all(r["code_sha256"] == sha256_file(Path(e1_exact.__file__)) for r in rows),
        "input_e1_full_sweep_sha256": sha256_file(SWEEP),
        "python": platform.python_version(), "python_flint": flint.__version__,
        "set_int_max_str_digits": "0 (unlimited)",
    }
    checks = {}

    # (a)
    ta = {}
    built_rot = None
    for s in SETS:
        res, built, _choices = tie_analysis(s, rows)
        ta[SET_LABEL[s]] = res
        if s == "rotated":
            built_rot = built
    expected_ok = (
        ta["T24"]["tie_columns_at_degree_12"] == []
        and ta["rotQ24"]["tie_columns_at_degree_12"] == [[2, 1]]
        and all(v["tied_columns"] == [[2, 1]] for v in ta["rotQ24"]["per_degree"].values())
        and all(v["tied_columns"] == [] for v in ta["T24"]["per_degree"].values())
        and ta["T24"]["producer_rebuilt_pivot_choices_equal_committed_sweep_for_every_degree"]
        and ta["rotQ24"]["producer_rebuilt_pivot_choices_equal_committed_sweep_for_every_degree"])
    sym = symmetry_cause("rotated", built_rot)
    sym_ok = all(sym.values())
    entry = {"description": "exact pivot ties in the pivot-adaptive rule (max d_k/sigma; ties go to X)",
             "tie_analysis": ta, "rotQ24_tie_symmetry_cause": sym,
             "result": "PASS" if (expected_ok and sym_ok) else "FAIL",
             "expected": "T24: no ties at any degree 2..12; rotQ24: exactly one tie, at column (2,1), at every degree 2..12"}
    if not args.skip_tie_break_bounds:
        entry["rotQ24_degree12_tie_resolved_to_Y"] = tie_break_effect(rows)
    checks["a_E1_F1_pivot_ties"] = entry

    # (b)
    gram = []
    for s, rule in [("triangle", "bj"), ("triangle", "pivot"), ("rotated", "bj"), ("rotated", "alt"),
                    ("rotated", "pivot"), ("triangle", "alt")]:
        gram.append(gram_check(s, rule))
    checks["b_E1_F2_BtB_equals_D_degree12"] = {
        "description": "exact B^T B = D (D = diag(d_k), d_k = ||b_k||^2), recurrence identity, and the consequence tr(P)=N; "
                       "replaces the projector-trace identity, which holds for any nonzero columns when d_k := ||b_k||^2",
        "decisive_cases": ["T24 bj", "T24 pivot", "rotQ24 bj", "rotQ24 alt"],
        "cases": gram,
        "result": "PASS" if all(g["result"] == "PASS" for g in gram) else "FAIL"}

    # (c)
    checks["c_E1_F3_record04_inequalities"] = decisive_inequalities(rows)

    # (d)
    dh = dead_history(rows)
    orig_never = all(not v["original_KHS_DEAD_c1_or_c2"] for v in dh.values())
    checks["d_E1_F4_dead_history"] = {
        "description": "exact degree-by-degree evaluation of the frozen DEAD clauses (original KHS-only at every degree, "
                       "and the same clauses with the sharpened U = min(KHS, Urow)); degrees are those where the clause fires",
        "per_set": dh,
        "original_any_degree_KHS_DEAD_never_fires": orig_never,
        "freeze_provenance_git_show": freeze_provenance(),
        "result": "PASS" if orig_never else "FAIL"}

    result["checks"] = checks
    result["overall"] = "PASS" if all(c["result"] == "PASS" for c in checks.values()) else "FAIL"
    result["elapsed_seconds"] = time.time() - start
    Path(args.output).write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({"overall": result["overall"], "elapsed_seconds": result["elapsed_seconds"],
                      "per_check": {k: v["result"] for k, v in checks.items()}, "output": str(args.output)}))


if __name__ == "__main__":
    main()
