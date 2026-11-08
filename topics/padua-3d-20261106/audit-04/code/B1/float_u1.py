#!/usr/bin/env python3
"""Auditor audit04-B1: independent floating reimplementation of the 24 U1 cases.

Own angle-space cosine basis (no chebvander recurrence, no producer code),
own parity enumeration, Haar formula, SVD pseudo-inverse OLS, own Leja.
Pivoted-QR selection uses scipy geqp3 on the own unscaled cosine basis.
Compares with the committed receipts u1-round1.json / u1-round2.json.
"""
import itertools as it, json, math, sys, time
import numpy as np
import scipy.linalg as la
from scipy.stats import qmc

SRC = sys.argv[1]  # extracted topic dir (read-only inputs)
OUT = sys.argv[2]
DEGREES = [int(v) for v in sys.argv[3].split(',')] if len(sys.argv) > 3 else [4, 8, 12, 16]
QRSEL = sys.argv[4] if len(sys.argv) > 4 else 'own'
FAMS = sys.argv[5].split(',') if len(sys.argv) > 5 else None

def exps(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]

def basis_theta(theta, n, normalized=True):
    E = np.array(exps(n))
    out = np.ones((len(theta), len(E)))
    for j in range(3):
        out *= np.cos(np.outer(theta[:, j], np.arange(n+1)))[:, E[:, j]]
    if normalized:
        out *= 2.0**((E > 0).sum(1)/2)
    return out

def f4(x):
    a, b, c = x.T
    return np.column_stack((np.exp((a+b+c)/3), 1/(1+16*(a*a+b*b+c*c)), np.abs(a+0.3*b-0.2*c), np.cos(4*a-3*b+2*c)))

def parity(n, equal):
    m = np.array((n+1,)*3 if equal else (n, n+1, n+1))
    ids = np.array([i for i in it.product(*(range(v+1) for v in m)) if len({t % 2 for t in i}) == 1])
    b = np.where((ids == 0) | (ids == m), 1, 2).prod(1)
    th = np.pi*ids/m
    return th, b/(2*m.prod())

def leja_order(vals, tol=0.0):
    rem = list(range(len(vals))); order = [rem.pop(0)]
    while rem:
        sc = np.array([np.prod([abs(vals[i]-vals[j]) for j in order]) for i in rem])
        best = sc.max()
        cand = [rem[k] for k in range(len(rem)) if sc[k] >= best*(1-tol)]
        pick = min(cand)
        order.append(pick); rem.remove(pick)
    return order

def nodes(n, fam):
    N = math.comb(n+3, 3)
    if fam in ('aniso', 'equal'):
        th, w = parity(n, fam == 'equal')
        return th, w, {}
    if fam == 'globalQR':
        L = 2*n+1
        ang = np.pi*np.arange(L)/(L-1)
        cand = np.array(list(it.product(ang, repeat=3)))
        raw = basis_theta(cand, n, normalized=False)
        _, _, piv = la.qr(raw.T, mode='economic', pivoting=True, check_finite=False)
        sel = piv[:N]
        own_sel = sel
        # sensitivity: same selection via numpy chebvander values
        x = np.cos(cand)
        tabs = [np.polynomial.chebyshev.chebvander(x[:, j], n) for j in range(3)]
        raw2 = np.array([tabs[0][:, a]*tabs[1][:, b]*tabs[2][:, c] for a, b, c in exps(n)]).T
        _, _, piv2 = la.qr(raw2.T, mode='economic', pivoting=True, check_finite=False)
        if QRSEL == 'cheb': sel = piv2[:N]
        return cand[sel], np.full(N, 1/N), {'qrsel': QRSEL, 'own_vs_cheb_trace_equal_set': None, 'same_selection_as_chebvander': bool(np.array_equal(np.sort(sel), np.sort(piv2[:N]))),
                                            'same_order_as_chebvander': bool(np.array_equal(sel, piv2[:N]))}
    ang = np.pi*np.arange(n+1)/n
    vals = np.cos(ang)
    o0 = leja_order(vals); o1 = leja_order(vals, 1e-12)
    th = np.array([[ang[o0[a]], ang[o0[b]], ang[o0[c]]] for a, b, c in exps(n)])
    return th, np.full(N, 1/N), {'leja_order': o0, 'tie_tolerant_same': o0 == o1}

def assessment():
    L = 21
    ang = np.pi*np.arange(L)/(L-1)
    tensor = np.array(list(it.product(ang, repeat=3)))
    u = qmc.Sobol(3, scramble=True, seed=20261107).random_base2(12)
    return np.vstack((tensor, np.pi*u)), len(tensor)

FAM = ('aniso', 'equal', 'globalQR', 'Leja')

def load_receipt(path):
    d = json.load(open(path))
    return {(r[0], r[1]): dict(zip(d['columns'], r)) for r in d['rows']}

r1 = load_receipt(f'{SRC}/evidence/u1-round1.json')
r2 = load_receipt(f'{SRC}/evidence/u1-round2.json')
A_th, split = assessment()
A_x = np.cos(A_th)
A_true = f4(A_x)

def rel(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(b), 1e-300)))

def evaluate(n, C, x_nodes, noise_seed, M):
    F = f4(x_nodes)
    coef = C @ F
    noise = np.random.default_rng(noise_seed).standard_normal(M)
    nc = C @ noise
    E = basis_theta(A_th, n)
    err = E @ coef - A_true
    mx = np.abs(err).max(0)
    rms = np.sqrt((err[split:]**2).mean(0))
    noisy = np.sqrt(((err[split:] + 1e-3*(E[split:] @ nc)[:, None])**2).mean(0))
    pv = np.max(np.sum((E @ C)**2, 1))
    return mx, rms, noisy, pv

rows = []
worst = {}
def upd(key, v):
    worst[key] = max(worst.get(key, 0.0), v)

for n in DEGREES:
    N = math.comb(n+3, 3)
    for fi, fam in enumerate(FAM):
        if FAMS and fam not in FAMS: continue
        t0 = time.process_time()
        th, w, meta = nodes(n, fam)
        sel_cpu = time.process_time()-t0
        x = np.cos(th)
        V = basis_theta(th, n)
        M = len(th)
        if fam in ('aniso', 'equal'):
            G = V.T @ (w[:, None]*V)
            pred = np.eye(N)
            if fam == 'aniso':
                pred[exps(n).index((n, 0, 0))]*0
                k = exps(n).index((n, 0, 0)); pred[k, k] = 2
            gram_res = float(np.abs(G-pred).max())
            C = (V*w[:, None]).T.copy()
            if fam == 'aniso':
                C[k] *= 0.5
        else:
            gram_res = None
            C = np.linalg.inv(V)
        repro = float(np.abs(C @ V - np.eye(N)).max())
        tr = float(np.sum(C*C))
        mx, rms, noisy, pv = evaluate(n, C, x, 20261107+100*n+fi, M)
        ref = r1[(n, fam)]
        row = {'round': 1, 'n': n, 'family': fam, 'M': M, 'N': N, 'gram_res': gram_res, 'repro': repro,
               'trace': tr, 'M_trace': M*tr, 'ref_M_trace': ref['budget_risk'],
               'rel_trace': rel(tr, ref['risk_trace']), 'rel_max': rel(mx, ref['max_error']),
               'rel_rms': rel(rms, ref['sobol_rms']), 'rel_noisy': rel(noisy, ref['noisy_sobol_rms']),
               'rel_pointvar': rel(pv, ref['pointwise_noise_variance_max_sample']),
               'fn_max': mx.tolist(), 'fn_rms': rms.tolist(), 'ref_fn_max': ref['max_error'], 'ref_fn_rms': ref['sobol_rms'],
               'M_match': M == ref['M'], 'selection_cpu': sel_cpu, **meta}
        rows.append(row); print(json.dumps({k: row[k] for k in ('round','n','family','M','M_trace','rel_trace','rel_max','rel_rms','rel_noisy')}), flush=True)
        for kk in ('rel_trace', 'rel_rms', 'rel_noisy', 'rel_pointvar'):
            upd(f'{fam}:{kk}', row[kk])
        if fam in ('aniso', 'equal'):
            # Round 2: OLS via SVD pseudo-inverse, Gauss-Markov identity in floating
            C0 = np.linalg.pinv(V, rcond=1e-13)
            D = C - C0
            ident = float(np.abs(C @ C.T - C0 @ C0.T - D @ D.T).max())
            tr0 = float(np.sum(C0*C0))
            mx0, rms0, noisy0, pv0 = evaluate(n, C0, x, 20261107+100*n+fi, M)
            ref2 = r2[(n, fam)]
            row2 = {'round': 2, 'n': n, 'family': fam, 'M': M, 'trace_ols': tr0, 'M_trace_ols': M*tr0,
                    'reduction_pct': 100*(1-tr0/tr), 'fn_max': mx0.tolist(), 'fn_rms': rms0.tolist(), 'ref_fn_max': ref2['max_error'], 'ref_fn_rms': ref2['sobol_rms'], 'diff_frob2': float(np.sum(D*D)), 'risk_diff': tr-tr0,
                    'identity_res': ident, 'repro': float(np.abs(C0 @ V - np.eye(N)).max()),
                    'rel_trace': rel(tr0, ref2['risk_trace']), 'rel_max': rel(mx0, ref2['max_error']),
                    'rel_rms': rel(rms0, ref2['sobol_rms']), 'rel_noisy': rel(noisy0, ref2['noisy_sobol_rms'])}
            rows.append(row2); print(json.dumps({k: row2[k] for k in ('round','n','family','M_trace_ols','reduction_pct','identity_res','rel_trace','rel_max','rel_rms')}), flush=True)

json.dump({'rows': rows}, open(OUT, 'w'), indent=1)
