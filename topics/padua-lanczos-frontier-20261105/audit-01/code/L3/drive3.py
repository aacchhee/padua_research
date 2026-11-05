#!/usr/bin/env python3
"""T8: asserted fixed-path checks for s=2,3,4 (all paths for s<=3, sampled paths
for s=4), plus the adaptive pivot-max policy over all 64 admissible s=4 paths."""
import sys, time, json, random
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3')
from l3check import *

TOL = mp.mpf(10) ** -40
t0 = time.time()
OUT = {}

def tri_instance(seed, M, s, den):
    rng = random.Random(seed)
    nodes = []
    while len(nodes) < M:
        a, b = rng.randrange(0, den + 1), rng.randrange(0, den + 1)
        if a + b <= den and (a, b) not in nodes:
            nodes.append((a, b))
    nodes = [(mp.mpf(a) / den, mp.mpf(b) / den) for a, b in nodes]
    weights = [1 + (i % 3) for i in range(M)]
    return Inst(nodes, weights, s)

def advs():
    a = [('shrink', adv_shrink), ('mix', make_adv_mix(mp.mpf('0.3'), 4)), ('hist', make_adv_hist(5))]
    a += [('out%d' % sd, make_adv_out(sd)) for sd in range(2)]
    a += [('rnd%d' % sd, make_adv_random_nonsmooth(sd)) for sd in range(2)]
    return a

def assert_ok(o):
    for kk in ('q', 'beta', 'coef', 'eps', 'theta/B', 'B/Bquad', 'Lentry', 'Lspec', 'Khat', 'T142'):
        if kk in o:
            assert o[kk] <= 1 + TOL, (kk, o[kk])
    assert o['beta_lower_margin'] >= 1 - TOL
    assert o['min_pivot_ratio'] >= mp.mpf(1) / 2 - TOL
    assert o['orth_defect'] <= mp.mpf(10) ** -45

for s, M, den, seed in [(2, 9, 13, 1), (3, 14, 22, 20261105), (4, 20, 29, 3)]:
    inst = tri_instance(seed, M, s, den)
    N = inst.N
    lam = [None] + [mp.mpf(1)] * (N - 1)
    paths = all_paths(s)
    rng = random.Random(s)
    chosen = paths if len(paths) <= 8 else rng.sample(paths, 4)
    rec = {'N': N, 'M': M, 'n_paths': len(paths), 'checked_paths': len(chosen), 'runs': 0}
    worst = {}
    radii = []
    for P in chosen:
        c = constants(inst, P, lam)
        radii.append(c['rR'])
        for frac in ['1', '0.999', '0.25']:
            u = c['rR'] * mp.mpf(frac)
            for nm, adv in advs():
                res = run(inst, P, u, lam, adv)
                assert res['ok']
                o = check_run(inst, c, res, u, full=(frac != '0.999'))
                assert_ok(o)
                merge(worst, o)
                rec['runs'] += 1
    rec['radii'] = [mp.nstr(r, 4) for r in radii]
    rec['worst'] = {k: mp.nstr(v, 6) for k, v in worst.items()}
    OUT['s%d' % s] = rec
    print('s=%d' % s, json.dumps(rec), 'time %.1f' % (time.time() - t0), flush=True)

# adaptive over all 64 admissible paths at s = 4
inst = tri_instance(3, 20, 4, 29)
N = inst.N
lam = [None] + [mp.mpf(1)] * (N - 1)
paths = all_paths(4)
cst = {}
for P in paths:
    cst[P] = constants(inst, P, lam)
print('s=4 all-path constants time %.1f' % (time.time() - t0), flush=True)
r_all = min(c['rR'] for c in cst.values())
maxB = lambda u: max(B(c, u) for c in cst.values())
rhs9 = lambda u: u * max(c['K'] * c['F'] for c in cst.values()) + 4 * u ** 2 * max(
    c['K'] * (c['J'] + c['F'] * (c['b'] + c['d'])) for c in cst.values())

def pol_pivotmax(k, Q, o, inst_, u, lam_):
    if len(o) == 1:
        return o[0]
    vals = []
    for (p, op) in o:
        prod = [inst_.coord(op)[i] * Q[p][i] for i in range(inst_.M)]
        r, _ = proj_out(Q, prod)
        vals.append(nrm(r))
    return o[0] if vals[0] >= vals[1] else o[1]

def pol_hash(k, Q, o, inst_, u, lam_):
    if len(o) == 1:
        return o[0]
    return o[int(mp.floor(abs(Q[-1][2]) * mp.mpf(10) ** 25)) % 2]

real = set()
nrun = 0
for frac in ['1', '0.5']:
    u = r_all * mp.mpf(frac)
    for pname, pol in [('pivotmax', pol_pivotmax), ('hash', pol_hash)]:
        for nm, adv in advs():
            res = run(inst, None, u, lam, adv, policy=pol)
            assert res['ok']
            R = res['path']
            assert R in cst
            real.add(R)
            th = inst.theta(res['Q'])
            assert th <= B(cst[R], u) <= maxB(u) <= rhs9(u)
            o = check_run(inst, cst[R], res, u, full=False)
            assert_ok(o)
            nrun += 1
OUT['s4_adaptive'] = dict(r_all=mp.nstr(r_all, 5), runs=nrun, distinct_realized=len(real),
                          maxB_at_r_all=mp.nstr(maxB(r_all), 5))
print('adaptive s=4', OUT['s4_adaptive'], 'time %.1f' % (time.time() - t0), flush=True)
json.dump(OUT, open('/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3/out_T8.json', 'w'), indent=1)
