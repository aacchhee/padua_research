#!/usr/bin/env python3
"""Independent audit checks for PD-T?drift-codex-10/11 (Claude audit E34).
Own code; imports nothing from the campaign.
Part A (exact, Fraction): node-row identity E_i = -Lbar(z_i)^{-1} zeta_i and
  triangularity/nonzero leading coefficients of the computed-coefficient surrogate
  for ARBITRARY rational coefficients (no accuracy), arbitrary admissible parents.
Part B (float, MEASURED sanity only): inequality (2), (3) and E_+ refinement on random
  runs with arbitrary/inaccurate coefficients.
Part C (float, MEASURED illustration): record11 scores K_R, chi_R for all 2^(s-1)
  staircases on a small triangle and first-order behaviour of theta(t)/t.
"""
from fractions import Fraction as F
import random, json, itertools
import numpy as np

rng = random.Random(5)
out = {}

def monomials(s):
    return [(t, j) for t in range(s + 1) for j in range(t + 1)]  # x^(t-j) y^j

def parents_admissible(t, j):
    opts = []
    if j <= t - 1: opts.append(('X', (t - 1, j)))
    if j >= 1: opts.append(('Y', (t - 1, j - 1)))
    return opts

# ---------------- Part A: exact identity ----------------
def partA(m=4, s=3, trials=3):
    pts = [(F(i), F(j)) for i in range(m + 1) for j in range(m + 1 - i)]
    mons = monomials(s); N = len(mons); idx = {mn: k for k, mn in enumerate(mons)}
    res = []
    for tr in range(trials):
        par = {}; op = {}
        for k, (t, j) in enumerate(mons):
            if k == 0: continue
            o, p = rng.choice(parents_admissible(t, j)); par[k] = idx[p]; op[k] = o
        c = {(k, l): F(rng.randint(-40, 40), rng.randint(1, 7)) for k in range(1, N) for l in range(k)}
        beta = {k: F(rng.randint(1, 50), rng.randint(1, 9)) for k in range(1, N)}
        f = {k: [F(rng.randint(-5, 5), rng.randint(1, 100)) for _ in pts] for k in range(1, N)}
        Mn = len(pts)
        q = [[F(1)] * Mn]  # w_i = 1
        for k in range(1, N):
            a = [x if op[k] == 'X' else y for (x, y) in pts]
            v = [a[i] * q[par[k]][i] - sum((c[(k, l)] * q[l][i] for l in range(k)), F(0)) - f[k][i]
                 for i in range(Mn)]
            q.append([vi / beta[k] for vi in v])
        # surrogate polynomial coefficients in monomial basis (dict mon->coef)
        P = [{(0, 0): F(1)}]
        for k in range(1, N):
            newp = {}
            for (t, j), cf in P[par[k]].items():
                key = (t + 1, j) if op[k] == 'X' else (t + 1, j + 1)
                newp[key] = newp.get(key, F(0)) + cf
            for l in range(k):
                for mn, cf in P[l].items():
                    newp[mn] = newp.get(mn, F(0)) - c[(k, l)] * cf
            P.append({mn: cf / beta[k] for mn, cf in newp.items() if cf != 0})
        tri_ok = all(P[k].get(mons[k], 0) != 0 and all(idx[mn] <= k for mn in P[k]) for k in range(N))
        # E = Qhat - Vhat ; rows vs -Lbar^{-1} zeta
        def pval(k, x, y): return sum((cf * x**(t - j) * y**j for (t, j), cf in P[k].items()), F(0))
        ok = True
        for i, (x, y) in enumerate(pts):
            Ei = [q[k][i] - pval(k, x, y) for k in range(N)]
            # Lbar(z) E_i should equal -zeta_i
            for k in range(N):
                if k == 0:
                    lhs = Ei[0]; rhs = F(0)
                else:
                    a = x if op[k] == 'X' else y
                    lhs = Ei[k] + sum((c[(k, l)] / beta[k] * Ei[l] for l in range(k)), F(0)) - a / beta[k] * Ei[par[k]]
                    rhs = -f[k][i] / beta[k]
                if lhs != rhs: ok = False
        res.append({'trial': tr, 'surrogate_triangular_nonzero_leading': tri_ok, 'node_row_identity_exact': ok})
        assert tri_ok and ok
    return res
out['A_exact_identity_T4_s3'] = partA()

# ---------------- Part B: float certificate sanity ----------------
def grid_triangle(m):
    p = np.array([(i, j) for i in range(m + 1) for j in range(m + 1 - i)], float)
    return 2 * p / m - 1

def vander(pts, s):
    return np.column_stack([pts[:, 0]**(t - j) * pts[:, 1]**j for t, j in monomials(s)])

def sin_largest(Qa, Qb):
    Ua, _, _ = np.linalg.svd(Qa, full_matrices=False)
    Ub, _, _ = np.linalg.svd(Qb, full_matrices=False)
    return np.linalg.norm(Ub - Ua @ (Ua.T @ Ub), 2)

def run(pts, w, s, par, op, coefgen, fgen):
    mons = monomials(s); N = len(mons); M = len(pts)
    Q = np.zeros((M, N)); Q[:, 0] = np.sqrt(w)
    C = np.zeros((N, N)); B = np.ones(N); Fm = np.zeros((M, N))
    for k in range(1, N):
        a = pts[:, 0] if op[k] == 'X' else pts[:, 1]
        v = a * Q[:, par[k]]
        ck = coefgen(k, Q, v)  # length k
        fk = fgen(k, v)
        r = v - Q[:, :k] @ ck - fk
        bk = np.linalg.norm(r) if np.linalg.norm(r) > 0 else 1.0
        Q[:, k] = r / bk; C[k, :k] = ck; B[k] = bk; Fm[:, k] = fk
    return Q, C, B, Fm

def certificate(pts, s, par, op, Q, C, B, Fm):
    N = Q.shape[1]
    Khat = 0.0; Kplus = 0.0
    for (x, y) in pts:
        L = np.eye(N)
        for k in range(1, N):
            L[k, :k] += C[k, :k] / B[k]
            L[k, par[k]] -= (x if op[k] == 'X' else y) / B[k]
        Li = np.linalg.inv(L)
        Khat = max(Khat, np.linalg.norm(Li, 2)); Kplus = max(Kplus, np.linalg.norm(Li[:, 1:], 2))
    eps = np.sqrt(sum(np.linalg.norm(Fm[:, k])**2 / B[k]**2 for k in range(1, N)))
    smin = np.linalg.svd(Q, compute_uv=False).min()
    eta = np.linalg.norm(Q.T @ Q - np.eye(N), 2)
    return Khat, Kplus, eps, smin, eta

def partB(trials=300):
    m, s = 6, 4
    pts = grid_triangle(m); M = len(pts); w = np.full(M, 1.0 / M)
    mons = monomials(s); N = len(mons); idx = {mn: k for k, mn in enumerate(mons)}
    Vs = vander(pts, s) * np.sqrt(w)[:, None]
    nprng = np.random.default_rng(11)
    viol = 0; worst_ratio = 0.0; informative = 0; viol3 = 0; violp = 0
    for tr in range(trials):
        par = {}; op = {}
        for k, (t, j) in enumerate(mons):
            if k == 0: continue
            o, p = rng.choice(parents_admissible(t, j)); par[k] = idx[p]; op[k] = o
        mode = tr % 3
        def coefgen(k, Q, v):
            exact = np.linalg.lstsq(Q[:, :k], v, rcond=None)[0]
            if mode == 0: return exact * (1 + 0.3 * nprng.standard_normal(k))  # inaccurate
            if mode == 1: return nprng.standard_normal(k) * 2                   # arbitrary
            return exact + 1e-6 * nprng.standard_normal(k)
        def fgen(k, v):
            return 10.0**nprng.uniform(-12, -3) * nprng.standard_normal(M) * np.linalg.norm(v)
        Q, C, B, Fm = run(pts, w, s, par, op, coefgen, fgen)
        theta = sin_largest(Vs, Q)
        Khat, Kplus, eps, smin, eta = certificate(pts, s, par, op, Q, C, B, Fm)
        bound = Khat * eps / smin; boundp = Kplus * eps / smin
        if theta > bound * (1 + 1e-8) + 1e-13: viol += 1
        if theta > boundp * (1 + 1e-8) + 1e-13: violp += 1
        if eta < 1 and theta > Khat * eps / np.sqrt(1 - eta) * (1 + 1e-8) + 1e-13: viol3 += 1
        if bound < 1: informative += 1
        if bound > 0: worst_ratio = max(worst_ratio, theta / bound)
    return {'trials': trials, 'violations_(2)': viol, 'violations_E+refinement': violp,
            'violations_(3)': viol3, 'informative_(bound<1)': informative,
            'max_theta_over_bound': worst_ratio,
            'note': 'float64, MEASURED sanity; modes: 1/3 inaccurate coefs (30% rel noise), 1/3 arbitrary random coefs, 1/3 near-exact'}
out['B_float_certificate_T6_s4'] = partB()

# ---------------- Part C: record11 scores ----------------
def staircases(s):
    # s_1=0, s_{t+1}-s_t in {0,1}
    for incs in itertools.product([0, 1], repeat=s - 1):
        st = [0]
        for d in incs: st.append(st[-1] + d)
        yield st  # st[t-1] = s_t

def partC():
    m, s = 8, 5
    pts = grid_triangle(m); M = len(pts); w = np.full(M, 1.0 / M)
    mons = monomials(s); N = len(mons); idx = {mn: k for k, mn in enumerate(mons)}
    Vs = vander(pts, s) * np.sqrt(w)[:, None]
    rows = []
    for st in staircases(s):
        par = {}; op = {}
        for k, (t, j) in enumerate(mons):
            if k == 0: continue
            if j <= st[t - 1]: op[k] = 'X'; par[k] = idx[(t - 1, j)]
            else: op[k] = 'Y'; par[k] = idx[(t - 1, j - 1)]
        exactc = lambda k, Q, v: Q[:, :k].T @ v  # exact full projection (Q orthonormal)
        Q, C, B, Fm = run(pts, w, s, par, op, exactc, lambda k, v: 0 * v)
        Khat, _, _, _, _ = certificate(pts, s, par, op, Q, C, B, Fm)
        chi = max(np.linalg.norm((pts[:, 0] if op[k] == 'X' else pts[:, 1]) * Q[:, par[k]]) / B[k] for k in range(1, N))
        # first-order check: aggregate preprojection residual t*d, ||d_k|| = C_loc ||A_k q_p||
        Cloc = 1.0; tpar = 1e-7; nprng = np.random.default_rng(3)
        ds = {}
        def coefgen(k, Qc, v): return Qc[:, :k].T @ v  # exact projection onto computed columns...
        def run_pert():
            Qp = np.zeros((M, N)); Qp[:, 0] = np.sqrt(w)
            for k in range(1, N):
                a = pts[:, 0] if op[k] == 'X' else pts[:, 1]
                v = a * Qp[:, par[k]]
                if k not in ds:
                    d = nprng.standard_normal(M); ds[k] = d / np.linalg.norm(d)
                v = v + tpar * Cloc * np.linalg.norm(v) * ds[k]
                # exact projection onto previous computed columns (CGS2 to emulate exact)
                for _ in range(2): v = v - Qp[:, :k] @ (Qp[:, :k].T @ v)
                Qp[:, k] = v / np.linalg.norm(v)
            return Qp
        Qp = run_pert()
        theta = sin_largest(Vs, Qp)
        rows.append({'staircase_s_t': st, 'K_R': Khat, 'chi_R': chi,
                     'theta(t)/t_measured': theta / tpar,
                     'first_order_bound_Cloc*sqrt(N-1)*chi*K': Cloc * np.sqrt(N - 1) * chi * Khat})
    return {'grid': 'T_8 scaled to [-1,1], uniform', 's': s, 'num_staircases': len(rows), 'rows': rows,
            'note': 'float64 MEASURED illustration only; not a certified score'}
out['C_record11_scores'] = partC()
print(json.dumps(out, indent=1, default=float))
