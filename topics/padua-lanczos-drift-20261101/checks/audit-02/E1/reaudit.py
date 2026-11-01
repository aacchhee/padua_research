#!/usr/bin/env python3
"""E1 re-audit harness: new comparisons/structural checks, reused audit-01 algebra.

No producer import. ind_basis / ind_aggregate / ind_scalar are unchanged code
authored by the independent Claude audit-01 reviewer, reused explicitly here.
"""
import argparse
import hashlib
import json
import platform
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
TOPIC = REPO / "topics/padua-lanczos-drift-20261101"
EVID = TOPIC / "evidence"
AUDIT1 = TOPIC / "checks/audit-01/scripts/E1"
sys.path.insert(0, str(AUDIT1))
sys.set_int_max_str_digits(0)
import flint
from flint import fmpq, fmpq_mat, ctx
import ind_basis as basis
import ind_aggregate as aggregate
import ind_scalar as scalar


def read(name):
    return json.loads((EVID / name).read_text())


def exact(value):
    return F(value["exact"] if isinstance(value, dict) else value)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def membership(value, rational):
    q = fmpq(str(rational))
    if isinstance(value, fmpq):
        return value == q
    return value.contains(q)


def structure():
    out = {}
    sweep = read("e1-full-sweep.json")["runs"]
    for name in ("triangle", "rotated"):
        pts = basis.nodes(name)
        mons, V, B, D = basis.exact_basis(pts, 12)
        M, N = len(pts), len(mons)
        gram = B.transpose() * B
        assert all(gram[k, l] == (D[k] if k == l else 0)
                   for k in range(N) for l in range(N))
        choices, ties, margins = [], [], []
        idx = {m: k for k, m in enumerate(mons)}
        for k, (t, j) in enumerate(mons[1:], 1):
            candidates = []
            if j < t:
                p = idx[t - 1, j]
                candidates.append((sum((pts[i][0] * B[i, p])**2 for i in range(M)), "X"))
            if j > 0:
                p = idx[t - 1, j - 1]
                candidates.append((sum((pts[i][1] * B[i, p])**2 for i in range(M)), "Y"))
            choices.append(min(candidates)[1])  # equal residual d_k: minimize product norm, X on tie
            if len(candidates) == 2:
                sx, sy = candidates[0][0], candidates[1][0]
                if sx == sy:
                    ties.append([t, j])
                else:
                    margins.append((abs(sx-sy)/(sx+sy), [t, j]))
        minimum, column = min(margins)
        prefixes = {}
        for degree in range(2, 13):
            row = next(r for r in sweep if r["set"] == name and r["degree"] == degree and r["rule"] == "pivot")
            prefixes[str(degree)] = choices[:(degree+1)*(degree+2)//2-1] == row["pivot_choices"]
        pointset = set(pts)
        out[name] = {"gram_exact": True, "positive_pivots": all(d > 0 for d in D),
                     "choices": "".join(choices), "prefix_matches": prefixes,
                     "ties": ties, "minimum_untied_margin": str(minimum),
                     "minimum_margin_column": column,
                     "rotation90_invariant": {(-y, x) for x, y in pts} == pointset,
                     "b1_equals_x": all(B[i, 1] == pts[i][0] for i in range(M)),
                     "b2_equals_y": all(B[i, 2] == pts[i][1] for i in range(M)),
                     "candidate_products_equal_at_2_1": all(pts[i][0]*B[i, 2] == pts[i][1]*B[i, 1] for i in range(M))}
        assert all(prefixes.values())
        assert ties == ([] if name == "triangle" else [[2, 1]])
    return out


def aggregate_case(name, rule, mode):
    r = aggregate.run(name, 12, rule, mode, prec=512)
    result = {k: aggregate.ser(v) for k, v in r.items()}
    if rule == "pivotY":
        reference = read("response-01-e1-checks.json")["checks"]["a_E1_F1_pivot_ties"]["rotQ24_degree12_tie_resolved_to_Y"]
        refvals = [reference[k]["Y_tie_exact"] for k in ("Knode_squared", "KHS_squared", "Urow_squared")]
        expected_choices = reference["choices_Y_tie_break"]
    else:
        reference = next(x for x in read("e1-full-sweep.json")["runs"] if x["set"] == name and x["degree"] == 12 and x["rule"] == rule)
        refvals = [reference[k]["exact"] for k in ("Knode_squared", "KHS_squared", "Urow_squared")]
        expected_choices = "".join(reference["pivot_choices"])
    keys = ("Knode2", "KHS2", "Urow2") if mode == "exact" else ("Knode2_ball", "KHS2", "Urow2_ball")
    result["reference_exact_equal_or_in_ball"] = {k: membership(r[k], q) for k, q in zip(keys, refvals)}
    result["choices_match"] = r["choices"] == expected_choices
    assert all(result["reference_exact_equal_or_in_ball"].values()) and result["choices_match"]
    return result


def scalar_case(name, mode):
    rule = "pivot" if name == "triangle" else "alt"
    upper, choice = scalar.upper(name, rule, mode)
    cert = next(x for x in read("e1-multinode-certificates.json")["witnesses"] if x["set"] == name)
    lower, greedy, signs, ambiguous, expected = scalar.bj_lower(name, cert["target_column"], cert["node_signs"], mode)
    uref = next(x for x in read("e1-scalar-cgs2.json")["full_graph_upper_runs"] if x["set"] == name)["upper_squared"]["exact"]
    checks = {"upper": membership(upper, uref),
              "lower": membership(lower, cert["explicit_greedy_sign_lower_squared"]["exact"]),
              "expected": membership(expected, cert["expected_random_sign_lower_squared"]["exact"]),
              "greedy_equals_committed": signs == cert["node_signs"],
              "no_ambiguous_signs": ambiguous == 0}
    assert all(checks.values())
    ratio = lower / upper
    if mode == "exact":
        ratio_lower, ratio_upper = ratio, ratio
    else:
        ratio_lower, ratio_upper = ratio.lower(), ratio.upper()
    assert ratio_lower > (640000 if name == "triangle" else 49)
    if name == "rotated":
        assert ratio_upper < 100
    return {"set": name, "mode": mode, "checks": checks, "ratio": aggregate.ser(ratio),
            "upper": aggregate.ser(upper), "lower": aggregate.ser(lower),
            "own_greedy_lower": aggregate.ser(greedy), "expected": aggregate.ser(expected),
            "comparator_choices": "".join(choice[1:]), "sign_count": len(signs),
            "ambiguous_signs": ambiguous, "posthoc_ratio_threshold": 640000 if name == "triangle" else 49,
            "threshold_pass": True, "rotated_bound_ratio_below100": name != "rotated" or bool(ratio_upper < 100)}


def arithmetic_and_provenance():
    rows = {(x["set"], x["degree"], x["rule"]): x for x in read("e1-full-sweep.json")["runs"]}
    def q(name, degree, rule, key):
        return exact(rows[name, degree, rule][key])
    decisive = {}
    dead = {}
    for name, comp, Lth, Uth, ratio in (("triangle", "pivot", 200000000000000, 170000000, 1000),
                                        ("rotated", "alt", 88000000000, 642000000, 11)):
        L, U = q(name, 12, "bj", "Knode_squared"), q(name, 12, comp, "upper_squared")
        decisive[name] = {"lower_threshold": L > Lth, "upper_threshold": U < Uth,
                          "ratio_threshold": L > ratio*ratio*U, "ratio_squared": str(L/U)}
        assert all(decisive[name][k] for k in ("lower_threshold", "upper_threshold", "ratio_threshold"))
        dead[name] = {}
        for field in ("KHS_squared", "upper_squared"):
            c1, c2 = [], []
            for d in range(2,13):
                u = q(name,d,"bj",field)
                lows = [q(name,d,r,"Knode_squared") for r in ("alt","pivot")]
                if u <= max(lows): c1.append(d)
                if u < 100*min(lows): c2.append(d)
            dead[name][field] = {"original_first_clause": c1, "simultaneous_second_clause": c2}
    revisions = {}
    raw = {}
    for rev in ("6920ba6", "c89eb6a"):
        b = subprocess.check_output(["git","show",rev+":topics/padua-lanczos-drift-20261101/evidence/e1-freeze.json"],cwd=REPO)
        raw[rev]=json.loads(b)
        revisions[rev]={"sha256":hashlib.sha256(b).hexdigest(),"fields":raw[rev],
                        "commit_time":subprocess.check_output(["git","show","-s","--format=%H %cI",rev],cwd=REPO,text=True).strip()}
    changed = [k for k in raw["c89eb6a"] if raw["6920ba6"].get(k)!=raw["c89eb6a"][k]]
    return {"decisive":decisive,"dead":dead,"freeze":revisions,"changed_freeze_fields":changed}


def compare_response(path):
    old, new = read("response-01-e1-checks.json"), json.loads(Path(path).read_text())
    differences=[]
    def walk(a,b,p=""):
        if isinstance(a,dict) and isinstance(b,dict):
            assert a.keys()==b.keys(),p
            for k in a:walk(a[k],b[k],p+"/"+k)
        elif isinstance(a,list) and isinstance(b,list):
            assert len(a)==len(b),p
            for i,(x,y) in enumerate(zip(a,b)):walk(x,y,p+"/"+str(i))
        elif a!=b:differences.append({"path":p,"committed":a,"rerun":b})
    walk(old,new)
    allowed=lambda p:p in ("/command","/python") or p.endswith("/elapsed_seconds")
    assert all(allowed(d["path"]) for d in differences)
    return {"mathematical_fields_identical":True,"ignored_volatile_metadata":differences,
            "committed_sha256":sha(EVID/"response-01-e1-checks.json"),"rerun_sha256":sha(path)}


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("task",choices=("structure","aggregate","scalar","arithmetic","compare"))
    ap.add_argument("--set",choices=("triangle","rotated"))
    ap.add_argument("--rule")
    ap.add_argument("--mode",choices=("exact","arb"),default="arb")
    ap.add_argument("--rerun")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    if args.task=="structure": result=structure()
    elif args.task=="aggregate":result=aggregate_case(args.set,args.rule,args.mode)
    elif args.task=="scalar":result=scalar_case(args.set,args.mode)
    elif args.task=="arithmetic":result=arithmetic_and_provenance()
    else:result=compare_response(args.rerun)
    out={"task":vars(args),"result":result,"python":platform.python_version(),"python_flint":flint.__version__,
         "code_sha256":sha(__file__),"reused_audit01_code":{p.name:sha(p) for p in (AUDIT1/"ind_basis.py",AUDIT1/"ind_aggregate.py",AUDIT1/"ind_scalar.py")}}
    Path(args.output).write_text(json.dumps(out,indent=1)+"\n")
    print(json.dumps({"task":args.task,"set":args.set,"rule":args.rule,"result":"PASS","output":args.output}),flush=True)
