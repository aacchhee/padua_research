"""Auditor-D replay of D4-05 with an independent EXACT reference.

Algorithm under test uses the pinned C4 baseline (imported read-only, it is the
object being benchmarked); reference coefficients, transport and error metric are
auditor code. Usage: python -I check_predivide.py REPO_ROOT N...
"""
import importlib.util, json, sys, time
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from exact_core import nn_exact, check_nn, indices

root = Path(sys.argv[1]); sizes = [int(v) for v in sys.argv[2:]]
spec = importlib.util.spec_from_file_location('c4', root / 'topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
C4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C4)

def sh(nu, j, d=1):
    return tuple(v + d * (i == j) for i, v in enumerate(nu))

def transport(co, N, c):  # own float/exact transport (same algebra as check_integrable)
    R = {}
    for nu in indices(N - 1):
        for j in range(2):
            low = sum(co[nu]['a%d' % (s+1)] / R[sh(nu, s, -1), s] for s in range(2) if nu[s])
            R[nu, j] = c - co[nu]['b%d' % (j+1)] - low
    new = {}
    for nu in indices(N - 1):
        r = {}
        for j in range(2):
            A, B = 'a%d' % (j+1), 'b%d' % (j+1)
            r[A] = co[nu][A] * R[nu, j] / R[sh(nu, j, -1), j] if nu[j] else 0.0
            r[B] = c - R[nu, j] if sum(nu) == N - 1 else co[sh(nu, j)][B] + R[sh(nu, j), j] - R[nu, j]
        new[nu] = r
    return new

def E(got, ref):
    worst = Q(0)
    for f in ('a1', 'a2', 'b1', 'b2'):
        scale = max(abs(r[f]) for r in ref.values())
        err = max(abs(Q(float(got[nu][f])) - r[f]) for nu, r in ref.items())
        worst = max(worst, err / scale)
    return float(worst)

rows = []
for fam in ('krawtchouk', 'hahn'):
    for N in sizes:
        t0 = time.monotonic()
        x, w = C4.inputs(N, fam)
        P, D, ref = nn_exact(x, w)          # exact target; raises if any |nu|<=N nonnormal
        if N <= 8: check_nn(x, P, ref)
        pre = [[v / (xx + 2) for xx, v in zip(x, row)] for row in w]
        _, _, ref_pre = nn_exact(x, pre)    # exact source normality and exact source array
        assert transport(ref_pre, N, Q(-2)) == ref   # exact restoration identity at this size
        cv = lambda q: C4.convert(q, float)
        xf = [cv(v) for v in x]
        direct, _ = C4.layers(N, *(C4.marginal(xf, [cv(v) for v in row]) for row in w))
        src, _ = C4.layers(N, *(C4.marginal(xf, [cv(v) for v in row]) for row in pre))
        cand = transport(src, N, -2.0)
        iso = transport({nu: {k: float(v) for k, v in r.items()} for nu, r in ref_pre.items()}, N, -2.0)
        rows.append(dict(family=fam, N=N, E_C4=E(direct, ref), E_predivide_restore=E(cand, ref),
                         E_isolated_from_rounded_exact_source=E(iso, ref),
                         exact_target_and_source_normal=True, seconds=round(time.monotonic() - t0, 2)))
        print(json.dumps(rows[-1]), flush=True)
