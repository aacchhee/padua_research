import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/L3')
exec(open('drive2.py').read().split("# ------------------------------------------------------------------ T2 edge cases")[0])
from l3check import *
pts = [(0, 0)] + [(sx * a, sy * b) for a, b in [(1, 2), (2, 1)] for sx in (1, -1) for sy in (1, -1)] + [(3, 0), (-3, 0), (0, 3), (0, -3)]
pts = [(mp.mpf(a) / 3, mp.mpf(b) / 3) for a, b in pts]
instT = Inst(pts, [1] * len(pts), 3)
NT = instT.N
lamT = [None] + [mp.mpf(1)] * (NT - 1)
pathsT = all_paths(3)
cstT = {R: constants(instT, R, lamT) for R in pathsT}
for R,cc in cstT.items():
    print(''.join(o for p,o in R), mp.nstr(cc['rR'],5), [mp.nstr(cc['ex']['betas'][k],5) for k in range(1,NT)])
r_all = min(cc['rR'] for cc in cstT.values())
def pol_pivotmax(k, Q, o, inst_, u, lam_):
    if len(o) == 1: return o[0]
    vals = []
    for (p, op) in o:
        prod = [inst_.coord(op)[i] * Q[p][i] for i in range(inst_.M)]
        r, _ = proj_out(Q, prod)
        vals.append(nrm(r))
    return o[0] if vals[0] >= vals[1] else o[1]
u = r_all
for nm, adv in advs_std():
    res = run(instT, None, u, lamT, adv, policy=pol_pivotmax)
    R = res['path']
    o = check_run(instT, cstT[R], res, u, full=False)
    print(nm, ''.join(op for p, op in R), fmt(o))
def pol_hash(k, Q, o, inst_, u, lam_):
    if len(o) == 1: return o[0]
    z = int(mp.floor(abs(Q[-1][1]) * mp.mpf(10) ** 30)) % 2
    return o[z]
for frac in ['1','0.3']:
    u = r_all*mp.mpf(frac)
    for pname, pol in [('pivotmax', pol_pivotmax), ('hash', pol_hash)]:
        for nm, adv in advs_std() + [('zero', lambda k, Q, prod, i_, u_: ([ZERO] * i_.M, None))]:
            res = run(instT, None, u, lamT, adv, policy=pol)
            R = res['path']
            o = check_run(instT, cstT[R], res, u, full=False)
            bad = {kk: mp.nstr(v,6) for kk, v in o.items() if kk in ('q', 'beta', 'coef', 'eps', 'theta/B') and not v <= 1}
            if bad: print('FAIL', frac, pname, nm, ''.join(op for p, op in R), bad)
