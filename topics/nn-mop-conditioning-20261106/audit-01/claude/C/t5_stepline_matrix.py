"""Independent step-line (coefficient matching), step-line gauge lower (3) of
c1-gauge-invariants, and c1-matrix-metric inequalities (1)-(3) with exact
box-to-spectral K_2 by vertex enumeration (convex maximum over a box)."""
import sys, json, itertools, time; sys.path.insert(0, '.')
import numpy as np
import mpmath as mp
from indep_nn import *
mp.mp.dps = 70
Hs = mp.mpf('1e-28')

def stepline(q):
    out, P = nn_map(*q)
    N = len(q[0])
    nu = lambda k: ((k+1)//2, k//2)
    Q = [P[nu(k)] for k in range(N+1)]
    res = {}
    worst = mp.mpf(0)
    for k in range(N):
        r = sub(polymul_x(Q[k]), Q[k+1])   # degree <= k
        coeffs = []
        for j in range(k, max(k-3, -1), -1):  # beta, gamma, delta via triangular peel
            c = r[j] if j < len(r) else mp.mpf(0)
            coeffs.append(c)
            r = sub(r, [c*v for v in Q[j]])
        worst = max([worst]+[abs(v) for v in r])
        res[('beta', k)] = coeffs[0]
        if k >= 1: res[('gamma', k)] = coeffs[1]
        if k >= 2: res[('delta', k)] = coeffs[2]
    # PD-T432 formula comparison
    f_err = mp.mpf(0)
    for k in range(N):
        n_, m_ = nu(k)
        bk = out[('b1', nu(k))] if k % 2 == 0 else out[('b2', nu(k))]
        f_err = max(f_err, abs(bk-res[('beta', k)]))
        if k >= 1:
            g = out.get(('a1', nu(k)), 0)+out.get(('a2', nu(k)), 0)
            f_err = max(f_err, abs(g-res[('gamma', k)]))
        if k >= 2:
            eta = (n_-1, m_-1)
            d = out[('b2', eta)]-out[('b1', eta)]
            dl = out[('a2', nu(k))]*d if k % 2 == 1 else -out[('a1', nu(k))]*d
            f_err = max(f_err, abs(dl-res[('delta', k)]))
    res['_resid'] = worst; res['_formula_err'] = f_err
    return res

def run(family, N):
    q = inputs(N, family)
    M = N-1; d = mp.mpf(M)/2
    base, J = jacobian(stepline, q, N, Hs)
    Kz, arg, per, sc = condition(base, J, q, N)
    x, w = q
    # terminal beta supports (z coordinates)
    row = J[('beta', M)]
    Tx = sum(abs(row[l]) for l in range(N))
    Tw = sum(abs(row[N+l])*w[0][l] for l in range(N))+sum(abs(row[2*N+l])*w[1][l] for l in range(N))
    par = sum(row[2*N+l]*w[1][l]*(-1)**l for l in range(N))
    rec = {'family': family, 'N': N, 'K_z': mp.nstr(Kz, 12), 'scales': {f: mp.nstr(v, 10) for f, v in sc.items()},
           'resid': mp.nstr(base['_resid'], 3), 'formula_err_vs_PD-T432': mp.nstr(base['_formula_err'], 3)}
    if family == 'krawtchouk' and N >= 3:
        lb = (4*mp.sqrt(6))**M/(4*M*(M-1))
        rec['step_parity_ratio'] = mp.nstr(abs(par)/sc['beta'], 12)
        rec['step_bound3'] = mp.nstr(lb, 12)
        rec['ok_step3'] = bool(abs(par)/sc['beta'] >= lb)
        rec['beta_scale_is_1/5'] = mp.nstr(abs(sc['beta']-mp.mpf(1)/5), 3)
    # integer-node H and its Jacobian; columns scaled by the box
    keys = [('beta', k) for k in range(N)]+[('gamma', k) for k in range(1, N)]+[('delta', k) for k in range(2, N)]
    pos = {('beta', k): (k, k) for k in range(N)}
    pos.update({('gamma', k): (k-1, k) for k in range(1, N)}); pos.update({('delta', k): (k-2, k) for k in range(2, N)})
    power = {'beta': 1, 'gamma': 2, 'delta': 3}
    Hx = np.zeros((N, N))
    for k in range(N-1): Hx[k+1, k] = 1
    for key in keys:
        v = d*(base[key]+1) if key[0] == 'beta' else d**power[key[0]]*base[key]
        Hx[pos[key]] = float(v)
    normH = np.linalg.norm(Hx, 2)
    out = {}
    for conv in ('integer', 'normalized'):
        C = np.zeros((3*N, N, N))
        for key in keys:
            for i in range(3*N):
                g = d**power[key[0]]*J[key][i]
                if i < N:   # node column; integer node displacement 1 = normalized 1/d
                    sc_i = 1/d if conv == 'integer' else mp.mpf(1)
                else:
                    sc_i = w[(i-N)//N][(i-N) % N]
                C[i][pos[key]] = float(g*sc_i)
        L = np.abs(C).sum(axis=0)
        # vertex enumeration of max ||sum_i h_i C_i||_2, h in {-1,1}^(3N), h_0=+1 by symmetry
        best = 0.0
        nv = 3*N-1
        signs = np.array(list(itertools.product((-1.0, 1.0), repeat=nv)))
        for chunk in np.array_split(signs, max(1, len(signs)//20000)):
            hh = np.concatenate([np.ones((len(chunk), 1)), chunk], axis=1)
            E = np.einsum('vi,ijk->vjk', hh, C)
            best = max(best, np.linalg.norm(E, ord=2, axis=(1, 2)).max())
        K2 = best/normH
        lower1 = L.max()/normH; upper1 = np.sqrt((L**2).sum())/normH
        if conv == 'integer':
            lower2 = float((Tx+d*Tw))/normH
        else:
            lower2 = float(d*(Tx+Tw))/normH
        upper2 = float(Kz*mp.sqrt(N*sum((d**power[f]*sc[f])**2 for f in ('beta', 'gamma', 'delta'))))/normH
        o = {'K2': K2, 'lower1': lower1, 'upper1': upper1, 'lower2': lower2, 'upper2': upper2,
             'ok1': bool(lower1 <= K2*(1+1e-12) and K2 <= upper1*(1+1e-12)),
             'ok2': bool(lower2 <= K2*(1+1e-12) and K2 <= upper2*(1+1e-12)),
             'terminal_entry_support_matches_lower2': abs(L[N-1, N-1]/normH-lower2)/lower2}
        if family == 'krawtchouk' and N >= 3:
            RN = mp.sqrt(N*(1+(6*d/5)**2+d**4+d**6/25))
            lb3 = float(d*(4*mp.sqrt(6))**M/(20*RN*M*(M-1)))
            o['bound3'] = lb3; o['ok3'] = bool(K2 >= lb3); o['frob_le_RN'] = bool(np.linalg.norm(Hx, 'fro') <= float(RN))
        out[conv] = o
    rec['matrix'] = out
    rec['normH'] = normH
    return rec

recs = []
for family in ('krawtchouk', 'hahn'):
    for N in (3, 4, 5, 6):
        t0 = time.time()
        r = run(family, N); r['seconds'] = round(time.time()-t0, 1)
        recs.append(r); print(json.dumps(r), flush=True)
json.dump(recs, open('t5_stepline_matrix.json', 'w'), indent=1)
ok = all(r['matrix'][c]['ok1'] and r['matrix'][c]['ok2'] and r['matrix'][c].get('ok3', True) for r in recs for c in r['matrix'])
ok = ok and all(r.get('ok_step3', True) for r in recs)
print('ALL_OK', ok)
