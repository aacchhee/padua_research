#!/usr/bin/env python3
"""T1: constants for every admissible path of a small s=3 instance, and
fixed-path adversarial checks at and inside the radius."""
import sys, time, json, random
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3')
from l3check import *

t0 = time.time()
# deterministic rational nodes in the unit triangle, nonuniform positive weights
rng = random.Random(20261105)
nodes = []
while len(nodes) < 14:
    a, b = rng.randrange(0, 23), rng.randrange(0, 23)
    if a + b <= 22 and (a, b) not in nodes:
        nodes.append((a, b))
nodes = [(mp.mpf(a) / 22, mp.mpf(b) / 22) for a, b in nodes]
weights = [1 + (i % 3) for i in range(14)]
inst = Inst(nodes, weights, 3)
N = inst.N
lam = [None] + [mp.mpf(1)] * (N - 1)
paths = all_paths(3)
print('N', N, 'M', inst.M, 'paths', len(paths))
csts = []
for P in paths:
    c = constants(inst, P, lam)
    csts.append(c)
    print(''.join(op for p, op in P), 'b=%s Delta=%s K=%s F=%s J=%s d=%s rR=%s chi=%s B(rR)=%s' % tuple(
        mp.nstr(z, 5) for z in (c['b'], c['Delta'], c['K'], c['F'], c['J'], c['d'], c['rR'], c['chi'], B(c, c['rR']))))
    # identities: F <= sqrt(N-1) chi (lambda=1), B - uKF exact formula
    u = c['rR']
    lhs = B(c, u) - u * c['K'] * c['F']
    rhs = u**2 * c['K'] * (c['J'] + c['F'] * (c['b'] + c['d']) - u * c['F'] * c['b'] * c['d']) / ((1 - u*c['b'])*(1 - u*c['d']))
    assert abs(lhs - rhs) <= abs(rhs) * mp.mpf(10)**(-40)
    assert c['F'] <= mp.sqrt(N - 1) * c['chi'] * (1 + mp.mpf(10)**-40)
    assert B(c, u) <= 4 * u * c['K'] * (c['F'] + c['J']) * (1 + mp.mpf(10)**-40)
print('constants time %.1fs' % (time.time() - t0))

# pick the path with largest radius and the one with smallest
order = sorted(range(len(paths)), key=lambda i: csts[i]['rR'])
sel = [order[0], order[-1]]
summary = {}
for si in sel:
    c = csts[si]
    name = ''.join(op for p, op in c['path'])
    acc_all = {}
    for frac in ['1', '0.999', '0.5', '0.1', '0.001']:
        u = c['rR'] * mp.mpf(frac)
        acc = {}
        advs = [('shrink', adv_shrink), ('mix', make_adv_mix(mp.mpf('0.5'), 1)), ('hist', make_adv_hist(2))]
        advs += [('out%d' % sd, make_adv_out(sd)) for sd in range(3)]
        advs += [('rnd%d' % sd, make_adv_random_nonsmooth(sd)) for sd in range(3)]
        for nm, adv in advs:
            res = run(inst, c['path'], u, lam, adv)
            assert res['ok'], (name, frac, nm)
            o = check_run(inst, c, res, u, full=(frac in ('1', '0.1')))
            merge(acc, o)
        acc_all[frac] = {k2: mp.nstr(v2, 6) for k2, v2 in acc.items()}
        print(name, 'u/rR=', frac, acc_all[frac])
    summary[name] = acc_all
print('fixed-path time %.1fs' % (time.time() - t0))
json.dump(summary, open('/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3/out_T1.json', 'w'), indent=1)
