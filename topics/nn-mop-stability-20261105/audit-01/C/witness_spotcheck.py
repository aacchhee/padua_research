#!/usr/bin/env python3
"""Auditor C: exact spot-check of returned rational witnesses (producer receipts
regenerated locally at /tmp/backward-projection-{family}-r2-160.json).

For each requested (family, N, method): read the rational common-data input,
rebuild the full NN array with auditor's own Fraction moment code
(native_exact_ref.exact_nn; no developer AD/C4/independent_check_moments),
regenerate the binary64 raw array with developer native/C4 code, and compute
exactly: positivity/order/mass, normality of all systems |nu|<=N, eta_d, eta_c,
fieldwise corrections, sqrt(Q). Compare against receipt floats.
Optional: exact one-sided directional probe of Q around the witness (N4 only).
"""
import json, sys, importlib.util, random, math, time
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from native_exact_ref import exact_nn, my_inputs, det_nonzero

ROOT = Path('/home/user/padua_research/topics/nn-mop-stability-20261105/code')
spec = importlib.util.spec_from_file_location('nm', ROOT / 'native_mixed.py')
nm = importlib.util.module_from_spec(spec); spec.loader.exec_module(nm)
F = ('a1', 'a2', 'b1', 'b2')
U = Q(1, 2 ** 53)


def normal_all(x, W):
    N = len(x)
    mom = [[sum(w * xi ** k for w, xi in zip(r, x)) for k in range(2 * N + 1)] for r in W]
    cnt = 0
    for s in range(1, N + 1):
        for n in range(s + 1):
            m = s - n
            A = [[mom[0][i + j] for j in range(s)] for i in range(n)] + [[mom[1][i + j] for j in range(s)] for i in range(m)]
            assert det_nonzero(A), ('nonnormal', n, m)
            cnt += 1
    return cnt


def Qobj(raw, arr, scale):
    return sum(((Q(raw[nu][f]) - arr[nu][f]) / scale[f]) ** 2 for nu in arr for f in F)


def check(family, N, method, probe=False):
    t0 = time.time()
    rec = json.loads(Path(f'/tmp/backward-projection-{family}-r2-160.json').read_text())
    row = next(r for r in rec['cases'] if r['N'] == N and r['method'] == method)
    x = [Q(s) for s in row['rational_input']['nodes']]
    W = [[Q(s) for s in r] for r in row['rational_input']['normalized_weights']]
    assert all(a < b for a, b in zip(x, x[1:])) and all(w > 0 for r in W for w in r) and all(sum(r) == 1 for r in W)
    x0, W0 = my_inputs(N, family)
    W0 = [[a / sum(r) for a in r] for r in W0]
    raw = nm.c4.compute(N, family)[0] if method == 'c4' else nm.compute(N, family, method)[0]
    truth, _ = exact_nn(x0, W0)
    scale = {f: max(abs(r[f]) for r in truth.values()) for f in F}
    arr, _ = exact_nn(x, W)
    ncount = normal_all(x, W)
    fields = {f: max(abs(Q(raw[nu][f]) - arr[nu][f]) for nu in arr) / scale[f] for f in F}
    eta_c = max(fields.values())
    eta_d = max(max(abs(a - b) for a, b in zip(x, x0)),
                max(abs(a - b) / b for r, r0 in zip(W, W0) for a, b in zip(r, r0)))
    Qw = Qobj(raw, arr, scale)
    Q0 = Qobj(raw, truth, scale)
    trivial_eta_c = max(max(abs(Q(raw[nu][f]) - truth[nu][f]) for nu in truth) / scale[f] for f in F)
    out = dict(family=family, N=N, method=method, normal_systems=ncount, entries=4 * len(arr),
               eta_d_u=float(eta_d / U), eta_c_u=float(eta_c / U), sqrtQ=math.sqrt(float(Qw)),
               receipt_eta_d_u=row['input_in_units_u'], receipt_eta_c_u=row['correction_in_units_u'],
               receipt_sqrtQ=row['coefficient_SPD_norm'],
               rel_diff=max(abs(float(eta_d / U) / row['input_in_units_u'] - 1),
                            abs(float(eta_c / U) / row['correction_in_units_u'] - 1),
                            abs(math.sqrt(float(Qw)) / row['coefficient_SPD_norm'] - 1)),
               fields_u={f: float(v / U) for f, v in fields.items()},
               trivial_witness_sqrtQ=math.sqrt(float(Q0)), trivial_witness_eta_c_u=float(trivial_eta_c / U),
               witness_sha=row['rational_input_sha256'])
    if probe:
        random.seed(7)
        worse = 0; trials = 0; mindelta = None
        for t in (Q(1, 10 ** 17), Q(1, 10 ** 18)):
            for _ in range(12):
                dx = [Q(random.randint(-1000, 1000), 1000) for _ in range(N)]
                dW = []
                for r in W:
                    d = [Q(random.randint(-1000, 1000), 1000) * w for w in r]
                    sd = sum(d)
                    dW.append([di - sd * w for di, w in zip(d, r)])  # zero mass change, relative scale
                for sgn in (1, -1):
                    xx = [a + sgn * t * b for a, b in zip(x, dx)]
                    WW = [[a + sgn * t * b for a, b in zip(r, dr)] for r, dr in zip(W, dW)]
                    Qt = Qobj(raw, exact_nn(xx, WW)[0], scale)
                    trials += 1
                    if Qt < Qw:
                        worse += 1
                    dl = (Qt - Qw) / Qw
                    mindelta = dl if mindelta is None else min(mindelta, dl)
        out.update(probe_trials=trials, probe_decrease_count=worse, probe_min_relative_increase=float(mindelta))
    out['seconds'] = round(time.time() - t0, 2)
    return out


if __name__ == '__main__':
    jobs = [('krawtchouk', 4, 'lu', True), ('hahn', 4, 'lu', True), ('krawtchouk', 4, 'nodeqr', False),
            ('hahn', 8, 'lu', False)]
    if len(sys.argv) > 1 and sys.argv[1] == 'all8':
        jobs = [(f, 8, m, False) for f in ('krawtchouk', 'hahn') for m in ('c4', 'lu', 'nodeqr')]
    for j in jobs:
        print(json.dumps(check(*j)), flush=True)
