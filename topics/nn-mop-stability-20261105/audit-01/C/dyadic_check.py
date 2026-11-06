#!/usr/bin/env python3
"""Auditor C: independent exact check of the five-field dyadic obstruction.

1. Derive the necessary identity symbolically (exact polynomial algebra over Q
   with sympy-free generic check): for random exact rational normal inputs the
   identity d00*(b01_1-b00_1)+a10_1-a01_2 == 0 holds exactly (sanity, not proof;
   the proof is written in report.md).
2. Evaluate the residual on the displayed strings with Fractions/integers.
3. Confirm each displayed value is an exactly representable binary64 dyadic.
4. Regenerate the native N4 Krawtchouk LU array on this platform, compare.
5. Also evaluate residual on the exact (true) N4 Krawtchouk array -> must be 0.
"""
import sys, json, importlib.util, random
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from native_exact_ref import exact_nn, my_inputs

S = ['0', '-3602879701896397/18014398509481984', '-4803839602528527/36028797018963968',
     '5764607523034235/18014398509481984', '6004799503160661/18014398509481984']
CLAIM = Q(25700541873527631, 649037107316853453566312041152512)


def resid(b2_00, b1_00, b1_01, a1_10, a2_01):
    return (b2_00 - b1_00) * (b1_01 - b1_00) + a1_10 - a2_01


def fields(c):
    return [c[0, 0]['b2'], c[0, 0]['b1'], c[0, 1]['b1'], c[1, 0]['a1'], c[0, 1]['a2']]


out = {}
v = [Q(s) for s in S]
# integer-only evaluation (common denominator 2^55)
D = 2 ** 55
ints = [int(q * D) for q in v]
assert all(Q(i, D) == q for i, q in zip(ints, v))
num = (ints[0] - ints[1]) * (ints[2] - ints[1]) + (ints[3] - ints[4]) * D
r_int = Q(num, D * D)
r = resid(*v)
out['residual'] = str(r)
out['residual_integer_route'] = str(r_int)
out['matches_claim'] = (r == CLAIM == r_int)
out['nonzero'] = r != 0
out['denominator_is_power_of_two'] = (r.denominator & (r.denominator - 1)) == 0
out['all_binary64_exact'] = all(Q(float(q)) == q for q in v)
out['float_residual_approx'] = float(r)

# exact truth at N4 Krawtchouk, and exact identity on random normal positive inputs
ref, _ = exact_nn(*my_inputs(4, 'krawtchouk'))
out['exact_true_array_residual'] = str(resid(*fields(ref)))
out['true_minus_witness'] = [float(Q(a) - b) for a, b in zip(fields(ref), v)]
random.seed(1)
bad = 0
for trial in range(50):
    N = random.choice([2, 3, 4, 5])
    x = sorted(set(Q(random.randint(-50, 50), random.randint(1, 9)) for _ in range(3 * N)))[:N]
    if len(x) < N:
        continue
    W = [[Q(random.randint(1, 40), random.randint(1, 40)) for _ in range(N)] for _ in range(2)]
    try:
        ref2, _ = exact_nn(x, W)
    except (StopIteration, ZeroDivisionError):
        continue  # nonnormal draw
    out["random_exact_identity_tested"] = out.get("random_exact_identity_tested", 0) + 1
    if resid(*[ref2[0, 0]['b2'], ref2[0, 0]['b1'], ref2[0, 1]['b1'], ref2[1, 0]['a1'], ref2[0, 1]['a2']]) != 0:
        bad += 1
out['random_exact_identity_failures'] = bad

spec = importlib.util.spec_from_file_location('nm', '/home/user/padua_research/topics/nn-mop-stability-20261105/code/native_mixed.py')
nm = importlib.util.module_from_spec(spec); spec.loader.exec_module(nm)
c, _ = nm.compute(4, 'krawtchouk', 'lu')
q = [Q.from_float(float(t)) for t in fields(c)]
out['platform_regenerated_equal'] = q == v
out['platform_regenerated_residual'] = str(resid(*q))
print(json.dumps(out, indent=1))
