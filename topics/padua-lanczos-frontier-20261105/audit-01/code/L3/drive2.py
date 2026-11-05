#!/usr/bin/env python3
"""T2 edge cases, T3 tolerance/finite selection, T4 adaptive policies with an
exact-data tie, T5 hill-climbing adversaries, T6 out-of-hypothesis break tests,
T7 structural radius identities (d >= sqrt2 b; 5^{(k-1)/2} growth of H)."""
import sys, time, json, random
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3')
from l3check import *

OUT = {}
t0 = time.time()
def log(*a):
    print(*a, flush=True)

def tri_instance(seed, M, s, den=22):
    rng = random.Random(seed)
    nodes = []
    while len(nodes) < M:
        a, b = rng.randrange(0, den + 1), rng.randrange(0, den + 1)
        if a + b <= den and (a, b) not in nodes:
            nodes.append((a, b))
    nodes = [(mp.mpf(a) / den, mp.mpf(b) / den) for a, b in nodes]
    weights = [1 + (i % 3) for i in range(M)]
    return Inst(nodes, weights, s)

def advs_std():
    a = [('shrink', adv_shrink), ('mix', make_adv_mix(mp.mpf('0.5'), 1)), ('hist', make_adv_hist(2))]
    a += [('out%d' % sd, make_adv_out(sd)) for sd in range(2)]
    a += [('rnd%d' % sd, make_adv_random_nonsmooth(sd)) for sd in range(2)]
    return a

def fmt(d):
    return {k: mp.nstr(v, 6) for k, v in d.items()}

# ------------------------------------------------------------------ T2 edge cases
log('== T2 edge cases')
# s = 1 (minimal degree): N = 3, a single admissible path
inst1 = Inst([(0, 0), (1, 0), (0, 1), (mp.mpf(1) / 3, mp.mpf(1) / 2)], [1, 2, 3, 4], 1)
P1 = all_paths(1)
assert len(P1) == 1
lam1 = [None, mp.mpf(1), mp.mpf(1)]
c1 = constants(inst1, P1[0], lam1)
log('s=1 constants', fmt({k: c1[k] for k in ('b', 'Delta', 'K', 'F', 'J', 'd', 'rR')}))
acc = {}
for frac in ['1', '0.5', '0.01']:
    u = c1['rR'] * mp.mpf(frac)
    for nm, adv in advs_std():
        res = run(inst1, P1[0], u, lam1, adv)
        assert res['ok']
        merge(acc, check_run(inst1, c1, res, u))
log('s=1 max ratios', fmt(acc))
OUT['T2_s1'] = dict(constants=fmt({k: c1[k] for k in ('b', 'Delta', 'K', 'F', 'J', 'd', 'rR')}), ratios=fmt(acc))
# lambda = 0: zero errors, radius 1, B = 0, theta = 0
inst = tri_instance(20261105, 14, 3)
N = inst.N
lam0 = [None] + [ZERO] * (N - 1)
P = all_paths(3)[0]
c0 = constants(inst, P, lam0)
res = run(inst, P, c0['rR'], lam0, adv_shrink)
th0 = inst.theta(res['Q'])
log('lambda=0: b', c0['b'], 'Delta', c0['Delta'], 'rR', c0['rR'], 'B(1)', B(c0, c0['rR']), 'theta', mp.nstr(th0, 3))
assert c0['rR'] == 1 and B(c0, mp.mpf(1)) == 0 and th0 < mp.mpf(10) ** -25  # sqrt(1-sigma^2) floor ~1e-30 at 60 digits
# lambda > 0 but zero actual errors: theta = 0 <= B
lam = [None] + [mp.mpf(1)] * (N - 1)
c = constants(inst, P, lam)
zero_adv = lambda k, Q, prod, inst_, u: ([ZERO] * inst_.M, None)
res = run(inst, P, c['rR'], lam, zero_adv)
log('lambda=1, zero errors: theta', mp.nstr(inst.theta(res['Q']), 3), 'B', mp.nstr(B(c, c['rR']), 5))
# mixed budgets: some columns exactly zero
lamm = [None] + [mp.mpf(1) if k % 3 else ZERO for k in range(1, N)]
cm = constants(inst, P, lamm)
acc = {}
for frac in ['1', '0.1']:
    u = cm['rR'] * mp.mpf(frac)
    for nm, adv in advs_std():
        res = run(inst, P, u, lamm, adv)
        assert res['ok']
        merge(acc, check_run(inst, cm, res, u))
log('mixed zero budgets rR', mp.nstr(cm['rR'], 5), 'ratios', fmt(acc))
OUT['T2_mixed'] = fmt(acc)
log('T2 time %.1f' % (time.time() - t0))

# ------------------------------------------------------------------ T7 structural identities
log('== T7 structural')
paths = all_paths(3)
csts = [constants(inst, R, lam) for R in paths]
for cc in csts:
    assert cc['d'] >= mp.sqrt(2) * cc['b'] * (1 - mp.mpf(10) ** -40), 'd < sqrt2 b'
    assert cc['Kexact'] >= 1
    h = cc['h']
    Hs = [mp.sqrt(mp.fsum(h[l] ** 2 for l in range(k + 1))) for k in range(N)]
    for k in range(1, N):
        assert Hs[k] >= mp.mpf(5) ** (mp.mpf(k - 1) / 2) * 2 * lam[1] * (1 - mp.mpf(10) ** -40)
    assert cc['rR'] <= mp.mpf(5) ** (-mp.mpf(N - 3) / 2) / (4 * lam[1])
log('d/b ratios', [mp.nstr(cc['d'] / cc['b'], 4) for cc in csts])
log('rR vs 5^{-(N-3)/2}/4:', [mp.nstr(cc['rR'], 3) for cc in csts], mp.nstr(mp.mpf(5) ** (-mp.mpf(N - 3) / 2) / 4, 3))
OUT['T7'] = dict(d_over_b=[mp.nstr(cc['d'] / cc['b'], 4) for cc in csts])

# ------------------------------------------------------------------ T3 tolerance / finite selection
log('== T3 tolerance and finite selection')
t3 = {}
for eta in [mp.mpf('0.5'), mp.mpf('1e-3'), mp.mpf('1e-9')]:
    reta = [rR_eta(cc, eta) for cc in csts]
    u = max(reta)
    accepted = [i for i, cc in enumerate(csts) if u <= cc['rR'] and B(cc, u) <= eta]
    assert accepted, 'no accepted path at u = max r_R(eta)'
    best = min(accepted, key=lambda i: (B(csts[i], u), i))
    cc = csts[best]
    worst = ZERO
    for nm, adv in advs_std():
        res = run(inst, cc['path'], u, lam, adv)
        assert res['ok']
        worst = max(worst, inst.theta(res['Q']))
    # slightly larger u than every radius: nothing accepted by the u<=r_R clause
    u2 = max(cc2['rR'] for cc2 in csts) * (1 + mp.mpf(10) ** -6)
    none = [i for i, cc2 in enumerate(csts) if u2 <= cc2['rR']]
    t3[mp.nstr(eta, 3)] = dict(u=mp.nstr(u, 5), n_accepted=len(accepted), best=''.join(o for p, o in cc['path']),
                               B=mp.nstr(B(cc, u), 5), worst_theta=mp.nstr(worst, 5), accepted_above_max_radius=len(none))
    assert worst <= eta and not none
    log('eta', mp.nstr(eta, 3), t3[mp.nstr(eta, 3)])
OUT['T3'] = t3
log('T3 time %.1f' % (time.time() - t0))

# ------------------------------------------------------------------ T4 adaptive with exact tie
log('== T4 adaptive')
pts = [(0, 0)] + [(sx * a, sy * b) for a, b in [(1, 2), (2, 1)] for sx in (1, -1) for sy in (1, -1)] \
      + [(3, 0), (-3, 0), (0, 3), (0, -3)]
pts = [(mp.mpf(a) / 3, mp.mpf(b) / 3) for a, b in pts]
instT = Inst(pts, [1] * len(pts), 3)
NT = instT.N
lamT = [None] + [mp.mpf(1)] * (NT - 1)
ms, opts = options(3)
# exact-data tie at column (2,1) = xy for the common prefix
k21 = ms.index((2, 1))
pre = run(instT, all_paths(3)[0])
Qp = pre['Q'][:k21]
cand = []
for (p, op) in opts[k21]:
    prod = [instT.coord(op)[i] * Qp[p][i] for i in range(instT.M)]
    r, _ = proj_out(Qp, prod)
    cand.append(nrm(r))
log('exact candidate pivots at (2,1):', [mp.nstr(z, 20) for z in cand], 'diff', mp.nstr(cand[0] - cand[1], 3))
pathsT = all_paths(3)
cstT = {R: constants(instT, R, lamT) for R in pathsT}
r_all = min(cc['rR'] for cc in cstT.values())
maxB = lambda u: max(B(cc, u) for cc in cstT.values())
maxRHS9 = lambda u: u * max(cc['K'] * cc['F'] for cc in cstT.values()) + 4 * u ** 2 * max(
    cc['K'] * (cc['J'] + cc['F'] * (cc['b'] + cc['d'])) for cc in cstT.values())

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
    z = int(mp.floor(abs(Q[-1][1]) * mp.mpf(10) ** 30)) % 2
    return o[z]

t4 = []
realized_set = set()
for frac in ['1', '0.3']:
    u = r_all * mp.mpf(frac)
    for pname, pol in [('pivotmax', pol_pivotmax), ('hash', pol_hash)]:
        for nm, adv in advs_std() + [('zero', lambda k, Q, prod, i_, u_: ([ZERO] * i_.M, None))]:
            res = run(instT, None, u, lamT, adv, policy=pol)
            assert res['ok']
            R = res['path']
            assert R in cstT
            realized_set.add(R)
            th = instT.theta(res['Q'])
            o = check_run(instT, cstT[R], res, u, full=False)
            row = dict(u=frac, policy=pname, adv=nm, path=''.join(op for p, op in R),
                       theta=mp.nstr(th, 5), BRhat=mp.nstr(B(cstT[R], u), 5), maxB=mp.nstr(maxB(u), 5))
            assert th <= B(cstT[R], u) <= maxB(u) <= maxRHS9(u)
            assert all(v <= 1 + mp.mpf(10) ** -40 for kk, v in o.items() if kk in ('q', 'beta', 'coef', 'eps', 'theta/B'))  # beta is tight (equality) at k=1 under shrink
            t4.append(row)
log('r_all', mp.nstr(r_all, 5), 'distinct realized paths', sorted(''.join(op for p, op in R) for R in realized_set))
OUT['T4'] = dict(r_all=mp.nstr(r_all, 5), tie=[mp.nstr(z, 20) for z in cand],
                 realized=sorted(''.join(op for p, op in R) for R in realized_set), rows=len(t4))
log('T4 time %.1f' % (time.time() - t0))

# ------------------------------------------------------------------ T5 hill-climbing adversaries (fixed path)
log('== T5 climbs')
cc = min(csts, key=lambda z: z['rR'])
u = cc['rR']
t5 = {}
best, G = climb(inst, cc, u, lambda res: inst.theta(res['Q']) / B(cc, u), 150, 7)
res = run(inst, cc['path'], u, lam, make_adv_param(G))
o = check_run(inst, cc, res, u)
t5['max theta/B'] = fmt(o)
log('climb theta/B', fmt(o))
best, G = climb(inst, cc, u, lambda res: -min(res['betas'][k] / cc['ex']['betas'][k] for k in range(1, N)), 150, 8)
res = run(inst, cc['path'], u, lam, make_adv_param(G))
o = check_run(inst, cc, res, u)
t5['min pivot'] = fmt(o)
log('climb min pivot', fmt(o))
best, G = climb(inst, cc, u, lambda res: max(nrm(axpy(-1, cc['ex']['Q'][k], res['Q'][k])) / (u * cc['h'][k]) for k in range(1, N)), 150, 9)
res = run(inst, cc['path'], u, lam, make_adv_param(G))
o = check_run(inst, cc, res, u)
t5['max q ratio'] = fmt(o)
log('climb q ratio', fmt(o))
OUT['T5'] = t5
log('T5 time %.1f' % (time.time() - t0))

# ------------------------------------------------------------------ T6 break tests outside hypotheses
log('== T6 break tests')
t6 = {}
# (a) budget-respecting pivot shrinking: first breakdown u* (bisection), compared with r_R
def breaks(u, kappa=1):
    # capped pivot-shrinking source: e_k = -min(budget, ||rp||) rp/||rp||, which obeys (1)
    # (with lambda scaled by kappa) and gives betahat_k = max(||rp|| - budget, 0) exactly.
    lamk = [None] + [kappa * l for l in lam[1:]]
    def adv(k, Q, prod, i_, uu):
        r, _ = proj_out(Q, prod)
        budget = uu * lamk[k] * nrm(prod)
        nr = nrm(r)
        if budget >= nr:   # exact cancellation of the residual
            return scal(-1, r), scal(budget * 0, r)  # direction -r; magnitude fixed below
        return scal(-1, r), None
    # run() scales the direction to the full budget; to cap it we pass the exact cancelling
    # error through a dedicated path instead:
    N_, M_ = inst.N, inst.M
    Q = [list(inst.q0)]
    for k in range(1, N_):
        p, op = cc['path'][k - 1]
        prod = [inst.coord(op)[i] * Q[p][i] for i in range(M_)]
        r, _ = proj_out(Q, prod)
        budget = u * lamk[k] * nrm(prod)
        nr = nrm(r)
        if budget >= nr:
            return True
        yv = axpy(-budget / nr, r, prod)
        r2, _ = proj_out(Q, yv)
        Q.append(scal(1 / nrm(r2), r2))
    return False
lo, hi = cc['rR'], mp.mpf(1)
assert not breaks(lo) and breaks(hi)
for _ in range(80):
    mid = mp.sqrt(lo * hi)
    if breaks(mid):
        hi = mid
    else:
        lo = mid
t6['shrink_breakdown_u_over_rR'] = mp.nstr(hi / cc['rR'], 6)
t6['column1_breakdown_u'] = mp.nstr(cc['ex']['betas'][1] / (lam[1] * cc['v'][1]), 6)
t6['shrink_breakdown_u'] = mp.nstr(hi, 6)
log('shrink adversary first breakdown u =', mp.nstr(hi, 6), '=', mp.nstr(hi / cc['rR'], 6), 'x r_R')
# (b) at u = r_R, the source-budget multiplier needed for breakdown
lo, hi = mp.mpf(1), mp.mpf(10) ** 30
assert not breaks(cc['rR'], lo) and breaks(cc['rR'], hi)
for _ in range(120):
    mid = mp.sqrt(lo * hi)
    if breaks(cc['rR'], mid):
        hi = mid
    else:
        lo = mid
t6['budget_multiplier_for_breakdown_at_rR'] = mp.nstr(hi, 6)
log('budget multiplier for breakdown at r_R:', mp.nstr(hi, 6))
# (c) Hres-type family: first-order part respects (1) with lambda=1 (hence Hres with C_loc=1),
#     plus an unconstrained second-order term u^2 * G * g_k (outside S_s).  Violates (1) for large G.
u = cc['rR'] / 2
outd = make_adv_out(11)
def hres_adv(Gs):
    def f(k, Q, prod, i_, uu):
        d, _ = outd(k, Q, prod, i_, uu)
        g = scal(uu ** 2 * Gs / nrm(d), d)
        return d, g
    return f
rows = []
for Gs in [mp.mpf(0), mp.mpf(10) ** 6, mp.mpf(10) ** 9, mp.mpf(10) ** 12, mp.mpf(10) ** 13, mp.mpf(10) ** 14]:
    res = run(inst, cc['path'], u, lam, hres_adv(Gs))
    th = inst.theta(res['Q']) if res['ok'] else mp.nan
    # realized budget ratio max_k ||e_k|| / (u lam ||A qhat_p||)
    rows.append(dict(G=mp.nstr(Gs, 3), theta=mp.nstr(th, 5), B=mp.nstr(B(cc, u), 5),
                     theta_over_B=mp.nstr(th / B(cc, u), 5), approx_budget_violation_1_plus_uG_over_normAq=mp.nstr(1 + u * Gs, 5)))
    log(rows[-1])
t6['hres_second_order'] = rows
OUT['T6'] = t6
log('total time %.1f' % (time.time() - t0))
json.dump(OUT, open('/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3/out_T2_T7.json', 'w'), indent=1, default=str)
