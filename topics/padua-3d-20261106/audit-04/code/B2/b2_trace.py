#!/usr/bin/env python3
"""Auditor B2: independent reconstruction of a U2-AB trial trace (own basis/objective code).

For every trial: displacement <= delta = r/(8 sqrt 3), separation >= 3r/4,
rho = ||(V_t - V_c) V_c^{-1}||_inf (basis-invariant) recomputed; for every
current iterate: own F, g; check direction = scaled clip(x-g)-x, trial = x+alpha d,
backtracking order, Armijo for accepted, Neumann decision consistency,
returned set == lowest-train-max accepted iterate, and stop reason.
"""
import sys, json, math, hashlib
import numpy as np
from scipy.special import logsumexp

raw = sys.argv[1]; n = int(sys.argv[2])
ev = json.load(open(f'{raw}/n{n}-optimization-events.json'))
T = np.load(f'{raw}/n{n}-optimization-trials.npz')['coordinates']
ret = np.load(f'{raw}/n{n}-joint_norm-nodes.npy')
init = np.load(f'{raw}/n{n}-localdet-nodes.npy')
N = (n + 1) * (n + 2) * (n + 3) // 6
EXP = np.array([(a, b, c) for c in range(n + 1) for b in range(n + 1 - c) for a in range(n + 1 - b - c)])


def tabs(x):
    t = np.ones((len(x), n + 1)); d = np.zeros((len(x), n + 1))
    if n:
        t[:, 1] = x; d[:, 1] = 1
    for e in range(1, n):
        t[:, e + 1] = 2 * x * t[:, e] - t[:, e - 1]
        d[:, e + 1] = 2 * t[:, e] + 2 * x * d[:, e] - d[:, e - 1]
    return t, d


def basis(P, grad=False):
    TT = [tabs(P[:, k]) for k in range(3)]
    Bm = TT[0][0][:, EXP[:, 0]] * TT[1][0][:, EXP[:, 1]] * TT[2][0][:, EXP[:, 2]]
    if not grad:
        return Bm
    G = []
    for ax in range(3):
        G.append(np.prod([TT[k][1][:, EXP[:, k]] if k == ax else TT[k][0][:, EXP[:, k]] for k in range(3)], axis=0))
    return Bm, G


ang = np.cos(np.pi * np.arange(21) / 20)
train = np.array(np.meshgrid(ang, ang, ang, indexing='ij')).reshape(3, -1).T
E = basis(train)


def FG(flat, beta):
    P = flat.reshape(-1, 3)
    Vm, G = basis(P, True)
    Vi = np.linalg.inv(Vm)
    C = E @ Vi
    sa = np.sqrt(C * C + 1e-16)
    s = sa.sum(1)
    lz = logsumexp(beta * s)
    w = np.exp(beta * s - lz)
    D = w[:, None] * C / sa
    GV = -(C.T @ D) @ Vi.T  # dF/dV
    g = np.stack([(GV * G[k]).sum(1) for k in range(3)], 1).ravel()
    return lz / beta, g, float(np.abs(C).sum(1).max()), Vm, Vi


def sep(P):
    dd = np.linalg.norm(P[:, None] - P[None], axis=2); np.fill_diagonal(dd, np.inf); return dd.min()


assert np.array_equal(T[0], init.ravel())
L0 = float(np.abs(E @ np.linalg.inv(basis(init))).sum(1).max())
beta = 40 / L0
x = T[0].copy()
F, g, tm, Vc, Vi = FG(x, beta)
out = {'n': n, 'events': len(ev), 'L0': L0, 'F0_diff': abs(F - ev[0]['objective'])}
mx = {'rho_diff': 0, 'F_diff': 0, 'trial_coord_diff': 0, 'disp_over_delta': 0, 'min_sep_ratio': 9, 'max_acc_rho': 0}
viol = []
best = (tm, 0); accepted = 0; i = 1; bt_expected = 0; armijo_margin_min = np.inf
while i < len(ev):
    e = ev[i]
    if e['backtrack'] == 0:
        proj = np.clip(x - g, -1, 1) - x
        pn = np.abs(proj).max()
        r = sep(x.reshape(-1, 3)); delta = r / (8 * math.sqrt(3))
        d = proj * min(1., delta / pn); slope = float(g @ d)
    if e['backtrack'] != bt_expected:
        viol.append(('backtrack order', i))
    alpha = 2.0 ** (-e['backtrack'])
    tr = T[i]
    mx['trial_coord_diff'] = max(mx['trial_coord_diff'], float(np.abs(tr - (x + alpha * d)).max()))
    disp = np.abs(tr - x).max(); mx['disp_over_delta'] = max(mx['disp_over_delta'], disp / delta)
    sr = sep(tr.reshape(-1, 3)) / r; mx['min_sep_ratio'] = min(mx['min_sep_ratio'], sr)
    if sr < 0.75:
        viol.append(('sep', i))
    rho = float(np.abs((basis(tr.reshape(-1, 3)) - Vc) @ Vi).sum(1).max())
    mx['rho_diff'] = max(mx['rho_diff'], abs(rho - e['rho']))
    if (rho > .5) != (e['reason'] == 'neumann_guard') and abs(rho - .5) > 1e-9:
        viol.append(('neumann decision', i, rho, e['reason']))
    if e['reason'] == 'neumann_guard':
        bt_expected += 1; i += 1; continue
    Ft, gt, tmt, Vt, Vit = FG(tr, beta)
    mx['F_diff'] = max(mx['F_diff'], abs(Ft - e['objective']))
    rhs = F + 1e-4 * alpha * slope
    acc = Ft <= rhs
    if acc != e['accepted']:
        viol.append(('armijo decision', i, Ft, rhs))
    if e['accepted']:
        armijo_margin_min = min(armijo_margin_min, rhs - Ft)
        mx['max_acc_rho'] = max(mx['max_acc_rho'], rho)
        x, F, g, tm, Vc, Vi = tr.copy(), Ft, gt, tmt, Vt, Vit
        accepted += 1; bt_expected = 0
        if tm < best[0]:
            best = (tm, i)
    else:
        bt_expected += 1
    i += 1
proj = np.clip(x - g, -1, 1) - x
out.update(mx)
out['violations'] = viol[:10]
out['n_violations'] = len(viol)
out['accepted'] = accepted
out['armijo_margin_min'] = armijo_margin_min
out['best_index'] = best[1]; out['best_train_max_recomputed'] = best[0]
out['returned_equals_best_trial'] = bool(np.array_equal(ret.ravel(), T[best[1]]))
out['final_projected_grad_inf'] = float(np.abs(proj).max())
acc_ev = [e for e in ev if e.get('accepted') and 'rho' in e]
tms = [ev[0]['train_max']] + [e['train_max'] for e in acc_ev]
out['train_max_first_last'] = [tms[0], tms[-1]]
out['train_max_decrease_last10'] = tms[-11] - tms[-1]
objs = [ev[0]['objective']] + [e['objective'] for e in acc_ev]
out['last_rel_decrease'] = (objs[-2] - objs[-1]) / max(1, abs(objs[-2]))
out['returned_sha256'] = hashlib.sha256(ret.astype('<f8').tobytes()).hexdigest()
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[3], 'w'), indent=1)
