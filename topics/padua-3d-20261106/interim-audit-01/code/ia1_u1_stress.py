#!/usr/bin/env python3
"""Independent interim U1 stress audit; frozen recipe, no new method/round.

Audited head 5440555cf326afdbd66b75bed195802013901c2d. All floating
results are MEASURED. Targets, degrees, noises and seeds below are fixed
before execution. This is neither a novelty test nor a formal Claude audit.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import shutil
import sys
import time

import numpy as np
import scipy
from scipy import linalg
from scipy.stats import qmc

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / "topics/padua-3d-20261106"
sys.path.insert(0, str(TOPIC / "code"))
import u1_usable as frozen

HEAD = "5440555cf326afdbd66b75bed195802013901c2d"
EXPECTED = {
    "topics/padua-3d-20261106/code/u1_usable.py": "50da9061b5ec4a5a0735664450d62e7e8e2f19675eed66aca0eb463ff193b0d4",
    "tracks/lattice-unisolvence/code/c3_lebesgue.py": "bf9cdb7c057f6ddf1793d99e6d338b1c1cfa37a274e5a6ac9689085f6bb3d66e",
    "tracks/lattice-unisolvence/code/c3_rank.py": "a95afbb764838662358dc70d2fd5a7eddf335d3ae48254d29b717fa015143332",
    "topics/padua-3d-20261106/evidence/u1-round1.json": "7e6b257ccc894260f54910334560d8b283d67dfe0c7d1f14c66a3501df7e436e",
    "topics/padua-3d-20261106/evidence/u1-round2.json": "0498f2aa38adecbe61a5b9f6db908dcb9e454b3876c3491c2c55ebee74d7da52",
    "topics/padua-3d-20261106/evidence/u1-api.json": "bd8aa38b0c4dbdea22ad3ad91ec6e1b3fb06c344052d6401e8271dfbaa991966",
    "topics/padua-3d-20261106/evidence/u2-degree12-nodes.json": "ade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f",
}
SEEDS = {"api": 202611070101, "chebyshev": 202611070102,
         "volume": 202611070103, "noise": 202611070104}
TARGETS = ["orthonormal T_(n+1)(x)", "exp(10*(x-1))",
           "exp(10*(z-1))", "exp(-((x-.23)^2+(y+.11)^2+(z-.37)^2)/.04)",
           "tanh(12*(x+.23*y-.41*z-.07))", "abs(x-y+.02*z-.15)",
           "cos(11*x+7*y-4*z)", "1/(1+40*(1-x))"]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def identity(path):
    path = Path(path)
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": digest(path)}


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, separators=(",", ":"), allow_nan=False) + "\n")


def independent_exponents(n):
    return sorted(((a, b, c) for a in range(n+1) for b in range(n+1-a)
                   for c in range(n+1-a-b)), key=lambda a: (sum(a), a[0], a[1]))


def independent_basis(points, n):
    """Cosine definition, independent of producer chebvander recurrence."""
    angle = np.arccos(np.asarray(points))
    t = [np.cos(angle[:, j, None] * np.arange(n+1)) for j in range(3)]
    return np.column_stack([t[0][:, a]*t[1][:, b]*t[2][:, c]*
                            2**(sum(v > 0 for v in (a,b,c))/2)
                            for a,b,c in independent_exponents(n)])


def target_values(points, base_n):
    x, y, z = points.T
    return np.column_stack((np.sqrt(2)*np.cos((base_n+1)*np.arccos(x)),
        np.exp(10*(x-1)), np.exp(10*(z-1)),
        np.exp(-((x-.23)**2+(y+.11)**2+(z-.37)**2)/.04),
        np.tanh(12*(x+.23*y-.41*z-.07)), np.abs(x-y+.02*z-.15),
        np.cos(11*x+7*y-4*z), 1/(1+40*(1-x))))


def api_checks(raw):
    rng = np.random.default_rng(SEEDS["api"])
    query = rng.uniform(-1, 1, (97, 3))
    rows = []
    for n in (1, 2, 3, 5, 9, 17):
        for equal in (False, True):
            nodes, weights, recipe = frozen.parity_nodes(n, equal)
            orders = ((n+1,)*3 if equal else (n,n+1,n+1))
            ids = [(a,b,c) for a in range(orders[0]+1)
                   for b in range(orders[1]+1) for c in range(orders[2]+1)
                   if (a-b) % 2 == 0 and (a-c) % 2 == 0]
            integer_mult = [math.prod(1 if i == 0 or i == m else 2
                                     for i,m in zip(row, orders)) for row in ids]
            exact_weights = [Fraction(v, 2*math.prod(orders)) for v in integer_mult]
            assert sum(exact_weights) == 1
            assert recipe["indices"] == list(map(list, ids))
            assert recipe["multiplicities"] == integer_mult
            assert np.array_equal(weights, np.array(list(map(float, exact_weights))))
            assert len(set(ids)) == len(nodes)
            if not equal:
                numerator = ((n+1)*(n+2)**2 if n % 2 == 0 else (n+1)*(n*n+4*n+5))
                assert len(nodes) == numerator // 4
            V = independent_basis(nodes,n)
            alpha = independent_exponents(n)
            coefficient = rng.normal(size=(len(alpha),3)) / np.sqrt(len(alpha))
            coefficient[:,2] = 0
            coefficient[alpha.index((n,0,0)),2] = 1
            Y = V @ coefficient
            fitted = frozen.parity_fit(n,Y,equal)
            single = frozen.parity_fit(n,Y[:,2],equal)
            E = independent_basis(query,n)
            error = float(np.max(np.abs(E @ (fitted-coefficient))))
            top_error = float(np.max(np.abs(single-coefficient[:,2])))
            pred = np.eye(len(alpha))
            if not equal: pred[alpha.index((n,0,0)),alpha.index((n,0,0))] = 2
            gram_error = float(np.linalg.norm(V.T @ (weights[:,None]*V)-pred, np.inf))
            assert error < 1e-10 and top_error < 1e-11 and gram_error < 1e-9
            rows.append({"n": n,"equal":equal,"M":len(nodes),"N":len(alpha),
                         "random_all_degree_prediction_error":error,
                         "top_axis_coefficient_error":top_error,"gram_residual_inf":gram_error})
    # Deliberate malformed-input probes, not valid-input scientific failures.
    malformed = []
    for label, values in (("one-element vector",np.array([2.])),
                          ("one-row matrix",np.array([[2.,3.]])),
                          ("length M-1",np.ones(len(frozen.parity_nodes(4)[0])-1))):
        try:
            c = frozen.parity_fit(4,values)
            malformed.append({"input":label,"accepted":True,"output_shape":list(c.shape),
                              "prediction":(independent_basis(np.zeros((1,3)),4) @ c).tolist()})
        except Exception as exc:
            malformed.append({"input":label,"accepted":False,"exception":type(exc).__name__})
    return rows,malformed


def allocation_risk(C, budget):
    """Exact greedy integer optimum for separable sum a_i/r_i, r_i>=1."""
    a = np.sum(C*C,axis=0)
    reps = np.ones(C.shape[1],dtype=np.int64)
    assert budget >= len(reps)
    for _ in range(budget-len(reps)):
        j = int(np.argmax(a/(reps*(reps+1))))
        reps[j] += 1
    return float(np.sum(a/reps)), reps


def build_case(base_n, name, raw):
    start = time.perf_counter()
    degree = base_n+1 if name == "QRhigher" else base_n
    if name in ("Haar", "OLS"):
        nodes, weights, recipe = frozen.parity_nodes(degree)
    elif name == "storedU2":
        payload = json.loads((TOPIC/"evidence/u2-degree12-nodes.json").read_text())
        decoded = base64.b85decode(payload["coordinates_base85"])
        assert hashlib.sha256(decoded).hexdigest() == payload["coordinates_sha256"]
        nodes = np.frombuffer(decoded,dtype="<f8").reshape(payload["N"],3).copy()
        assert degree == payload["n"]
        weights = np.full(len(nodes),1/len(nodes)); recipe = {"stored":True}
    else:
        nodes, weights, recipe = frozen.select_nodes(degree,"globalQR")
    select_seconds = time.perf_counter()-start
    V = independent_basis(nodes,degree)
    basis_difference = float(np.max(np.abs(V-frozen.basis(nodes,degree))))
    setup = time.perf_counter()
    if name == "Haar":
        # Actual frozen API on all observation columns; no auditor solver substitution.
        C = frozen.parity_fit(degree,np.eye(len(nodes)))
    else:
        Q,R = linalg.qr(V,mode="economic")
        C = linalg.solve_triangular(R,Q.T)
    solver_seconds = time.perf_counter()-setup
    repro = float(np.linalg.norm(C @ V-np.eye(V.shape[1]),np.inf))
    assert repro < 1e-9 and basis_difference < 1e-10
    singular = linalg.svdvals(V)
    budget = len(frozen.parity_nodes(base_n)[0])
    iid_risk = float(np.sum(C*C))
    feasible_risk, rep = allocation_risk(C,budget)
    coefficients = C @ target_values(nodes,base_n)
    if degree < base_n+1:
        exact_alias_L2 = math.sqrt(1+float(np.sum(coefficients[:,0]**2)))
    else:
        expected = np.zeros(V.shape[1]); expected[independent_exponents(degree).index((base_n+1,0,0))] = 1
        exact_alias_L2 = float(np.linalg.norm(coefficients[:,0]-expected))
    row = {"base_n":base_n,"name":name,"degree":degree,"M":len(nodes),"N":V.shape[1],
           "selection_seconds":select_seconds,"solver_seconds":solver_seconds,
           "basis_difference_max":basis_difference,"reproduction_inf":repro,
           "condition2_unweighted":float(singular[0]/singular[-1]),
           "risk_iid":iid_risk,"uniform_replication_coefficient":len(nodes)*iid_risk,
           "feasible_total_observations":budget,"optimal_integer_replication_risk":feasible_risk,
           "replication_min":int(rep.min()),"replication_max":int(rep.max()),
           "degree_n_plus_1_target_exact_model_L2":exact_alias_L2}
    if name in ("Haar","OLS"):
        variance = (1/weights); variance /= variance.mean()
        row["reciprocal_weight_variance_ratio"] = float(variance.max()/variance.min())
        row["reciprocal_weight_noise_risk"] = float(np.sum(C*C*variance))
        noise_rng = np.random.default_rng(SEEDS["noise"]+base_n)
        draws = noise_rng.choice(np.array([-1.,1.]),size=(len(nodes),512))
        energies = np.sum((C @ draws)**2,axis=0)
        row["iid_energy_trials"] = len(energies)
        row["iid_energy_mean"] = float(energies.mean())
        row["iid_energy_standard_error"] = float(energies.std(ddof=1)/np.sqrt(len(energies)))
    np.savez_compressed(raw/f"case-n{base_n}-{name}.npz",nodes=nodes,weights=weights,
                        operator=C,coefficients=coefficients,integer_replicates=rep)
    dump(raw/f"recipe-n{base_n}-{name}.json",recipe)
    return row,C,coefficients


def assess(row, coefficients, clouds):
    for cloud_name, query in clouds.items():
        summed = np.zeros(len(TARGETS)); max_error = np.zeros(len(TARGETS))
        for begin in range(0,len(query),512):
            points = query[begin:begin+512]
            err = independent_basis(points,row["degree"]) @ coefficients-target_values(points,row["base_n"])
            summed += np.sum(err*err,axis=0)
            max_error = np.maximum(max_error,np.max(np.abs(err),axis=0))
        row[cloud_name+"_rms"] = np.sqrt(summed/len(query)).tolist()
        row[cloud_name+"_max_sample"] = max_error.tolist()


def main(args):
    assert not args.raw.exists(), "Use a unique raw directory"
    assert not args.out.exists(), "Do not overwrite a receipt"
    args.raw.mkdir(parents=True)
    source_before = digest(__file__)
    for rel, expected in EXPECTED.items(): assert digest(ROOT/rel) == expected, rel
    shutil.copyfile(__file__,args.raw/"executed-source.py")
    started = datetime.now(timezone.utc).isoformat()
    api, malformed = api_checks(args.raw)
    clouds = {
        "chebyshev":np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=SEEDS["chebyshev"]).random_base2(14)),
        "volume":2*qmc.Sobol(3,scramble=True,seed=SEEDS["volume"]).random_base2(14)-1,
    }
    np.savez_compressed(args.raw/"assessment.npz",**clouds)
    cases=[]
    for base_n in (8,12):
        names = ["Haar","OLS","QRsame","QRhigher"]+(["storedU2"] if base_n == 12 else [])
        for name in names:
            row,C,coef = build_case(base_n,name,args.raw)
            assess(row,coef,clouds)
            cases.append(row)
            print(json.dumps({"n":base_n,"case":name,"iid":row["risk_iid"],
                              "feasible_budget_risk":row["optimal_integer_replication_risk"],
                              "reproduction_inf":row["reproduction_inf"]}),flush=True)
    result={"api":api,"malformed_inputs":malformed,"cases":cases}
    dump(args.raw/"all-results.json",result)
    for rel, expected in EXPECTED.items(): assert digest(ROOT/rel) == expected, rel
    assert digest(__file__) == source_before
    inventory=[identity(p) for p in sorted(args.raw.iterdir())]
    dump(args.raw/"inventory.json",inventory)
    receipt={"schema":"ia1-u1-stress-v1","status":"MEASURED interim independent audit",
        "formal_claude_audit":"PENDING; not replaced", "head":HEAD,
        "model":"assigned gpt-6-astra xhigh; runtime metadata unexposed",
        "command":sys.argv,"started_utc":started,"ended_utc":datetime.now(timezone.utc).isoformat(),
        "environment":{"python":sys.version,"numpy":np.__version__,"scipy":scipy.__version__,
                       "platform":platform.platform(),"threads":{k:os.environ.get(k) for k in
                         ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}},
        "sources":EXPECTED,"audit_source":identity(__file__),"identities_rechecked_after":True,
        "seeds":SEEDS,"assessment_points_per_cloud":16384,"targets":TARGETS,
        "noise_scope":"iid unit variance; endpoint heteroscedastic variance normalized to mean one; no target bias included",
        "budget_scope":"B equals parity M, integer repetition at every comparator node >=1; risk-minimizing allocation for fixed map",
        "api":api,"malformed_inputs":malformed,
        "cases":cases,"raw":{"directory":str(args.raw),"inventory":identity(args.raw/"inventory.json"),
                               "results":identity(args.raw/"all-results.json"),"policy":"unique /tmp; regenerate-only"}}
    # Full maxima/timings/precision remain in raw. Compact receipt never removes a case/target.
    for row in receipt["cases"]:
        row.pop("chebyshev_max_sample");row.pop("volume_max_sample")
    columns=list(dict.fromkeys(key for row in cases for key in row))
    receipt["case_columns"]=columns
    receipt["cases"]=[[row.get(key) for key in columns] for row in cases]
    def compact(obj):
        if isinstance(obj,float): return float(format(obj,".10g"))
        if isinstance(obj,list): return [compact(item) for item in obj]
        if isinstance(obj,dict): return {key:compact(value) for key,value in obj.items()}
        return obj
    receipt=compact(receipt)
    dump(args.out,receipt)
    assert args.out.stat().st_size < 16384, "Receipt too large; retain raw and report failure"
    print(json.dumps({"receipt":identity(args.out),"api_cases":len(api),"comparison_cases":len(cases)}),flush=True)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    main(parser.parse_args())
