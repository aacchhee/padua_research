#!/usr/bin/env python3
"""Auditor audit04-B1: independent recomputation of U1 continuation C1 (38-design
fixed-map optimal integer replication at B=637) and C2 (24 GLS refits), own code.

Own parity nodes, own cosine/recurrence basis, SVD OLS, own allocation (heap),
own decision/gate code. QR selection replicated with numpy chebvander + scipy
geqp3 (the inherited library chain; tie-sensitive, see float_u1). Stored U2
nodes decoded from the committed payload. Compares with the committed receipts.
"""
import base64, hashlib, heapq, itertools as it, json, math, sys, time
import numpy as np
import scipy.linalg as la
from scipy.stats import qmc

SRC, OUT = sys.argv[1], sys.argv[2]
B = 637
SIG = np.array([0., 1e-5, 1e-4, 1e-3, .01, .1, 1.])

def exps(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]

def basis_theta(theta, n, normalized=True):
    E = np.array(exps(n)); out = np.ones((len(theta), len(E)))
    for j in range(3):
        out *= np.cos(np.outer(theta[:, j], np.arange(n+1)))[:, E[:, j]]
    if normalized: out *= 2.0**((E > 0).sum(1)/2)
    return out

def basis_x(x, n):
    E = np.array(exps(n)); out = np.ones((len(x), len(E)))
    for j in range(3):
        T = np.empty((len(x), n+1)); T[:, 0] = 1
        if n >= 1: T[:, 1] = x[:, j]
        for k in range(1, n): T[:, k+1] = 2*x[:, j]*T[:, k]-T[:, k-1]
        out *= T[:, E[:, j]]
    return out*2.0**((E > 0).sum(1)/2)

def targets_theta(th):
    a, b, c = np.cos(th).T
    return np.column_stack((np.exp((a+b+c)/3), 1/(1+16*(a*a+b*b+c*c)), np.abs(a+0.3*b-0.2*c), np.cos(4*a-3*b+2*c),
        np.sqrt(2)*np.cos(13*th[:, 0]), np.exp(10*(a-1)), np.exp(10*(c-1)),
        np.exp(-((a-.23)**2+(b+.11)**2+(c-.37)**2)/.04), np.tanh(12*(a+.23*b-.41*c-.07)),
        np.abs(a-b+.02*c-.15), np.cos(11*a+7*b-4*c), 1/(1+40*(1-a))))

def targets_x(x):
    return targets_theta(np.arccos(np.clip(x, -1, 1))) * 0 + _tx(x)

def _tx(x):
    a, b, c = x.T
    T13 = basis_x(np.column_stack((a, 0*a, 0*a)), 13)[:, exps(13).index((13, 0, 0))]  # sqrt2*T13(a)
    return np.column_stack((np.exp((a+b+c)/3), 1/(1+16*(a*a+b*b+c*c)), np.abs(a+0.3*b-0.2*c), np.cos(4*a-3*b+2*c),
        T13, np.exp(10*(a-1)), np.exp(10*(c-1)),
        np.exp(-((a-.23)**2+(b+.11)**2+(c-.37)**2)/.04), np.tanh(12*(a+.23*b-.41*c-.07)),
        np.abs(a-b+.02*c-.15), np.cos(11*a+7*b-4*c), 1/(1+40*(1-a))))

def parity(n):
    m = np.array((n, n+1, n+1))
    ids = np.array([i for i in it.product(*(range(v+1) for v in m)) if len({t % 2 for t in i}) == 1])
    b = np.where((ids == 0) | (ids == m), 1, 2).prod(1)
    return np.pi*ids/m, b/(2*m.prod())

def qr_nodes(n):
    N = math.comb(n+3, 3); L = 2*n+1
    ang = np.pi*np.arange(L)/(L-1)
    cand = np.array(list(it.product(ang, repeat=3)))
    x = np.cos(cand)
    tabs = [np.polynomial.chebyshev.chebvander(x[:, j], n) for j in range(3)]
    raw = np.array([tabs[0][:, a]*tabs[1][:, b]*tabs[2][:, c] for a, b, c in exps(n)]).T
    _, _, piv = la.qr(raw.T, mode='economic', pivoting=True, check_finite=False)
    return cand[piv[:N]]

def allocation(a):
    r = np.ones(len(a), dtype=np.int64)
    h = [(-(a[j]/2.0), j) for j in range(len(a))]
    heapq.heapify(h)
    for _ in range(B-len(a)):
        _, j = heapq.heappop(h); r[j] += 1
        heapq.heappush(h, (-(a[j]/(r[j]*(r[j]+1))), j))
    return r, float(np.sum(a/r))

designs = []  # (name, n, C, x or theta info)
t0 = time.process_time()
for n in range(1, 14):
    names = (['Haar', 'OLS'] if n <= 12 else []) + ['QR'] + (['storedU2'] if n == 12 else [])
    for name in names:
        N = math.comb(n+3, 3)
        if name in ('Haar', 'OLS'):
            th, w = parity(n); V = basis_theta(th, n); x = np.cos(th)
            if name == 'Haar':
                C = (V*w[:, None]).T.copy(); C[exps(n).index((n, 0, 0))] *= 0.5
            else:
                C = np.linalg.pinv(V, rcond=1e-13)
        elif name == 'QR':
            th = qr_nodes(n); V = basis_theta(th, n); x = np.cos(th); C = np.linalg.inv(V)
        else:
            p = json.load(open(f'{SRC}/evidence/u2-degree12-nodes.json'))
            raw = base64.b85decode(p['coordinates_base85'])
            assert hashlib.sha256(raw).hexdigest() == p['coordinates_sha256']
            x = np.frombuffer(raw, dtype='<f8').reshape(p['N'], 3).copy(); V = basis_x(x, n); C = np.linalg.inv(V)
        M = len(x)
        repro = float(np.abs(C @ V - np.eye(N)).max())
        a = np.sum(C*C, axis=0)
        r, risk = allocation(a)
        coef = C @ _tx(x)
        designs.append(dict(name=name, n=n, M=M, N=N, C=C, V=V, x=x, r=r, risk=risk, repro=repro, coef=coef,
                            eligible=bool(M <= B and repro <= 1e-9 and r.sum() == B and r.min() >= 1)))
build_cpu = time.process_time()-t0

def bias2(coefs_by_design, seed):
    th = np.pi*qmc.Sobol(3, scramble=True, seed=seed).random_base2(15)
    truth = targets_theta(th)
    out = np.zeros((len(coefs_by_design), 12))
    for n in sorted({d['n'] for d in designs}):
        E = basis_theta(th, n)
        for k, (dn, cf) in enumerate(coefs_by_design):
            if dn == n:
                out[k] = np.mean((E @ cf - truth)**2, axis=0)
    return out

def totals(b2, risk):
    return b2[:, :, None] + risk[:, None, None]*SIG[None, None, :]**2  # design,target,sigma

rec1 = json.load(open(f'{SRC}/evidence/u1c-budget.json'))
cols1 = rec1['columns']
rows1 = [dict(zip(cols1, r)) for r in rec1['rows']]
res = {'build_cpu': build_cpu}
res['all_eligible'] = all(d['eligible'] for d in designs) and len(designs) == 38
res['max_repro'] = max(d['repro'] for d in designs)
res['names_match'] = [(d['name'], d['n'], d['M']) for d in designs] == [(r['name'], r['n'], r['M']) for r in rows1]
res['risk_max_rel_diff'] = max(abs(d['risk']-r['risk'])/r['risk'] for d, r in zip(designs, rows1))
risk = np.array([d['risk'] for d in designs])
b_first = bias2([(d['n'], d['coef']) for d in designs], 2026110711)
b_second = bias2([(d['n'], d['coef']) for d in designs], 2026110712)
ref_b = np.array([r['bias_squared'] for r in rows1])  # design, cloud, target (6 s.f.)
relb = np.abs(np.stack((b_first, b_second), 1)-ref_b)/np.maximum(np.abs(ref_b), 1e-300)
res['bias_rel_diff_nonfloor_max'] = float(relb[ref_b > 1e-20].max())
tot1, tot2 = totals(b_first, risk), totals(b_second, risk)
w1, w2 = tot1.argmin(0), tot2.argmin(0)
refw = np.array(rec1['outcome']['winners'])
res['winners_cloud_agree'] = bool((w1 == w2).all())
mism = [(t, s, int(w1[t, s]), int(refw[0][t][s])) for t in range(12) for s in range(7) if w1[t, s] != refw[0][t][s]]
mism2 = [(t, s, int(w2[t, s]), int(refw[1][t][s])) for t in range(12) for s in range(7) if w2[t, s] != refw[1][t][s]]
gapinfo = []
for (t, s, mine, theirs) in mism + mism2:
    gapinfo.append((t, s, mine, theirs, float(abs(tot2[mine, t, s]-tot2[theirs, t, s])/tot2[theirs, t, s])))
res['winner_mismatches_vs_receipt'] = gapinfo
regret = np.array([[tot2[w1[t, s], t, s]/tot2[:, t, s].min()-1 for s in range(7)] for t in range(12)])
base = 33
pg = 1-tot2[:, 5, :].min(0)/tot2[base, 5, :]
res['primary_gain_vs_Haar12'] = pg.tolist()
res['ref_primary_gain'] = rec1['outcome']['primary_gain_over_Haar12_second_cloud']
res['primary_rms'] = np.sqrt(tot2[:, 5, :].min(0)).tolist()
res['primary_winner_names'] = [f"{designs[i]['name']}{designs[i]['n']}" for i in w1[5]]
res['gauss_winner_names'] = [f"{designs[i]['name']}{designs[i]['n']}" for i in w1[7]]
res['gate_c1'] = bool(len(set(w1[5])) > 1 and pg.max() >= .05 and regret[5].max() <= .05)
res['regret_max'] = float(regret.max())
# ideal balanced vs actual integer at B=637: compare sigma^2*M*tr/B with actual risk
res['balanced_vs_integer'] = [(d['name'], d['n'], d['M'], float(d['M']*np.sum(d['C']**2)/B), d['risk']) for d in designs if d['n'] in (4, 8, 12)]

# C2: GLS refits
g = []
for k, d in enumerate(designs):
    if d['name'] not in ('Haar', 'OLS'): continue
    r = d['r'].astype(float); V = d['V']
    A = V.T @ (r[:, None]*V)
    Cs = la.solve(A, V.T*r[None, :], assume_a='pos')
    D = d['C']-Cs
    ident = float(np.abs((d['C']/r) @ d['C'].T - (Cs/r) @ Cs.T - (D/r) @ D.T).max())
    rs = float(np.sum(Cs*Cs/r))
    g.append(dict(name='GLSafter'+d['name'], n=d['n'], parent=k, C=Cs, coef=Cs @ _tx(d['x']), risk=rs,
                  ident=ident, repro=float(np.abs(Cs @ V-np.eye(d['N'])).max()), gain=1-rs/d['risk']))
rec2 = json.load(open(f'{SRC}/evidence/u1c-gls.json'))
nr = [dict(zip(rec2['columns'], x)) for x in rec2['new_rows']]
res['gls_count'] = len(g)
res['gls_max_ident'] = max(x['ident'] for x in g); res['gls_max_repro'] = max(x['repro'] for x in g)
res['gls_risk_rel_diff'] = max(abs(x['risk']-y['risk'])/y['risk'] for x, y in zip(g, nr))
res['gls_cov_gain_range_pct'] = [100*min(x['gain'] for x in g), 100*max(x['gain'] for x in g)]
allc = [(d['n'], d['coef']) for d in designs]+[(x['n'], x['coef']) for x in g]
allrisk = np.concatenate((risk, [x['risk'] for x in g]))
c1 = bias2(allc, 2026110713); c2 = bias2(allc, 2026110714)
T1, T2 = totals(c1, allrisk), totals(c2, allrisk)
gain = 1-T2.min(0)/T2[:38].min(0)
win1 = T1.argmin(0)
reg = np.array([[T2[win1[t, s], t, s]/T2[:, t, s].min()-1 for s in range(7)] for t in range(12)])
res['gls_primary_gain'] = gain[5].tolist(); res['gls_secondary_gain'] = gain[7].tolist()
res['ref_gls_primary_gain'] = rec2['outcome']['primary_gain_second_cloud']
res['ref_gls_secondary_gain'] = rec2['outcome']['secondary_gain_second_cloud']
res['gls_max_gain_by_target'] = gain.max(1).tolist()
res['gls_gate'] = bool(max(gain[5].max(), gain[7].max()) >= .05 and reg[[5, 7]].max() <= .05)
res['gls_regret_max'] = float(reg.max())
# parent regressions quoted in u1-continuation.md (second fresh cloud, sigma=0)
def parent_change(pname, n, t):
    k = next(i for i, x in enumerate(g) if x['name'] == 'GLSafter'+pname and x['n'] == n)
    p = g[k]['parent']
    return float(c2[p, t]), float(c2[38+k, t]), float(c2[38+k, t]/c2[p, t]-1)
res['quoted_regressions'] = {'cos_Haar11': parent_change('Haar', 11, 3), 'exp_Haar5': parent_change('Haar', 5, 0),
                             'ridge_OLS2': parent_change('OLS', 2, 2)}
res['cpu_total'] = time.process_time()-t0
json.dump(res, open(OUT, 'w'), indent=1)
print(json.dumps(res, indent=1)[:6000])
