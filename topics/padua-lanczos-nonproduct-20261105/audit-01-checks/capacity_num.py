#!/usr/bin/env python3
"""Auditor-authored numerical capacity brackets for the P5 Padua model.

Actual normalized perturbed full-projection Gram-Schmidt, forward-mode
Jacobian in float64; capacity = spectral norm of the 3-tensor
T[i,h,k] = (R dq_h / du)_{i,k}, bracketed by HOPM lower values and the
minimum top singular value over the three unfoldings (upper).
Independent of developer code.
"""
import json, math, sys, time
import numpy as np

rng = np.random.default_rng(20261106)


def padua(m):
    lam = lambda j, r: 0.5 / r if j in (0, r) else 1.0 / r
    X, Y, W, J = [], [], [], []
    for j in range(m + 1):
        for k in range(m + 2):
            if (j + k) % 2 == 0:
                X.append(math.cos(j * math.pi / m)); Y.append(math.cos(k * math.pi / (m + 1)))
                W.append(2 * lam(j, m) * lam(k, m + 1)); J.append(j)
    return np.array(X), np.array(Y), np.array(W), np.array(J)


def order(s):
    return [(d - b, b) for d in range(s + 1) for b in range(d + 1)]


def rule_parent(rule, a, b, choice=None):
    if rule == 'BJ':
        return ('X', (a - 1, b)) if b == 0 else ('Y', (a, b - 1))
    if rule == 'mirror':
        return ('X', (a - 1, b)) if a > 0 else ('Y', (a, b - 1))
    if rule == 'random':
        opts = []
        if a > 0: opts.append(('X', (a - 1, b)))
        if b > 0: opts.append(('Y', (a, b - 1)))
        return opts[choice[(a, b)] % len(opts)]
    raise ValueError


def base_and_jacobian(m, s, rule, choice=None):
    X, Y, W, Jn = padua(m)
    M = len(X)
    idx = order(s)
    loc = {ab: h for h, ab in enumerate(idx)}
    N = len(idx); H = N - 1
    sw = np.sqrt(W)
    Q = np.zeros((M, N)); Q[:, 0] = sw
    sig = np.zeros(N); beta = np.zeros(N); par = [None] * N
    for h in range(1, N):
        op, p = rule_parent(rule, *idx[h], choice)
        A = X if op == 'X' else Y
        a = A * Q[:, loc[p]]
        sig[h] = np.linalg.norm(a)
        r = a - Q[:, :h] @ (Q[:, :h].T @ a)
        r = r - Q[:, :h] @ (Q[:, :h].T @ r)
        beta[h] = np.linalg.norm(r); Q[:, h] = r / beta[h]
        par[h] = (A, loc[p])
    # Jacobian: dq_h as M x (M*H) matrices; source u_h block = columns (h-1)*M:(h)*M, f_h = sig_h u_h
    K = M * H
    dQ = [np.zeros((M, K))]
    for h in range(1, N):
        A, p = par[h]
        a = A * Q[:, p]
        da = A[:, None] * dQ[p]
        da[:, (h - 1) * M:h * M] += sig[h] * np.eye(M)
        Qp = Q[:, :h]
        c = Qp.T @ a
        # dc_l = a^T dq_l + q_l^T da
        dc = np.stack([a @ dQ[l] for l in range(h)]) + Qp.T @ da
        dr = da - sum(c[l] * dQ[l] for l in range(h)) - Qp @ dc
        q = Q[:, h]
        dbeta = q @ dr
        dQ.append((dr - np.outer(q, dbeta)) / beta[h])
    # exact polynomial projector of Pi_s: orthonormalize sqrt(w)*x^a y^b
    V = np.stack([sw * X ** a * Y ** b for a, b in idx], axis=1)
    U_, S_, _ = np.linalg.svd(V, full_matrices=False)
    rank = int((S_ > 1e-10 * S_[0]).sum())
    P = U_[:, :rank] @ U_[:, :rank].T
    R = np.eye(M) - P
    T = np.stack([R @ d for d in dQ[1:]], axis=1)  # M x H x K  (constant column derivative is 0)
    return dict(X=X, Y=Y, W=W, J=Jn, M=M, N=N, H=H, idx=idx, loc=loc, Q=Q, sig=sig, beta=beta,
                R=R, T=T, rankPi=rank, base_poly_err=np.linalg.norm(P @ Q - Q))


def tensor_bracket(T, starts=6, iters=150):
    M, H, K = T.shape
    ups = [np.linalg.norm(T.reshape(M, H * K), 2),
           np.linalg.norm(T.transpose(1, 0, 2).reshape(H, M * K), 2),
           np.linalg.norm(T.transpose(2, 0, 1).reshape(K, M * H), 2)]
    best = 0.0
    Th = np.ascontiguousarray(T.transpose(1, 0, 2).reshape(H, M * K))
    for t in range(starts):
        z = rng.standard_normal(H); z /= np.linalg.norm(z)
        val = 0
        for it in range(iters):
            G = np.tensordot(z, T, axes=([0], [1]))
            Uu, Ss, Vt = np.linalg.svd(G, full_matrices=False)
            y, u = Uu[:, 0], Vt[0]
            z = Th @ np.outer(y, u).ravel()
            nv = np.linalg.norm(z)
            if nv == 0: break
            z /= nv
            if abs(nv - val) < 1e-14 * max(1, nv): val = nv; break
            val = nv
        best = max(best, val)
    return best, min(ups), ups


def closed_form_V(D, rule, u):
    """Formula (6) and mirror transpose using U polynomials, for unit-scaled sources u_h."""
    X, Y, sig, idx, loc, M = D['X'], D['Y'], D['sig'], D['idx'], D['loc'], D['M']
    def U(l, z):
        a, b = np.ones_like(z), 2 * z
        if l == 0: return a
        for _ in range(l - 1): a, b = b, 2 * z * b - a
        return b
    def p(l, z):
        return np.ones_like(z) if l == 0 else math.sqrt(2) * np.cos(l * np.arccos(np.clip(z, -1, 1)))
    def K(a, c, z):
        return math.sqrt(2) * U(a - 1, z) if c == 1 else 2 * U(a - c, z)
    f = {ab: sig[loc[ab]] * u[(loc[ab] - 1) * M: loc[ab] * M] for ab in idx[1:]}
    V = {}
    for (a, b) in idx[1:]:
        if rule == 'BJ':
            va0 = sum((K(a, c, X) * f[(c, 0)] for c in range(1, a + 1)), np.zeros(M))
            V[(a, b)] = p(b, Y) * va0 + sum((K(b, d, Y) * f[(a, d)] for d in range(1, b + 1)), np.zeros(M))
        else:
            v0b = sum((K(b, d, Y) * f[(0, d)] for d in range(1, b + 1)), np.zeros(M))
            V[(a, b)] = p(a, X) * v0b + sum((K(a, c, X) * f[(c, b)] for c in range(1, a + 1)), np.zeros(M))
    return np.stack([V[ab] for ab in idx[1:]], axis=1)


def main(outpath):
    t0 = time.monotonic()
    rows = []
    for m in range(2, 8):
        for s in range(1, m + 1):
            for rule in ('BJ', 'mirror'):
                D = base_and_jacobian(m, s, rule)
                M, N, H = D['M'], D['N'], D['H']
                row = dict(m=m, s=s, rule=rule, M=M, N_s=N, normal_dim=M - D['rankPi'],
                           base_span_err=float(D['base_poly_err']))
                if s < m:
                    # exact base checks
                    betas = D['beta'][1:]
                    row['sigma_max'] = float(D['sig'].max()); row['beta_min'] = float(betas.min())
                    # closed form comparison for random u
                    err = 0
                    for _ in range(3):
                        u = rng.standard_normal(M * H)
                        Vcf = closed_form_V(D, rule, u)
                        Vjac = np.einsum('ihk,k->ih', D['T'], u)
                        err = max(err, np.abs(D['R'] @ Vcf - Vjac).max() / max(1, np.abs(Vjac).max()))
                    row['closed_form_vs_jacobian_relerr'] = float(err)
                    # witness: u at (1,0) = e_m (unit), f = sigma e_m = e_m/sqrt2
                    e = np.sqrt(D['W']) * (-1.0) ** D['J']
                    u = np.zeros(M * H); h10 = D['loc'][(1, 0)]
                    u[(h10 - 1) * M:h10 * M] = e
                    Wout = np.einsum('ihk,k->ih', D['T'], u)
                    row['witness_spectral'] = float(np.linalg.norm(Wout, 2))
                    row['witness_row_xaxis'] = [float(e @ Wout[:, D['loc'][(a, 0)] - 1]) for a in range(1, s + 1)]
                lo, up, ups = tensor_bracket(D['T'])
                row.update(kappa_lower=float(lo), kappa_upper=float(up))
                row['claimed_lower'] = math.sqrt(math.ceil(s / 2))
                row['claimed_upper'] = 2 * math.sqrt(2) * (s + 1) * (N - 1)
                if s < m:
                    assert row['closed_form_vs_jacobian_relerr'] < 1e-9, row
                    assert row['witness_spectral'] >= row['claimed_lower'] - 1e-9, row
                    assert lo >= row['claimed_lower'] - 1e-9 and up <= row['claimed_upper'], row
                    assert row['sigma_max'] <= 1 + 1e-12
                else:
                    assert row['normal_dim'] == 0 and up < 1e-8, row
                rows.append(row)
                print(time.monotonic() - t0, json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in row.items()
                                  if k not in ('witness_row_xaxis',)}), flush=True)
    # fixed random admissible rules: last-column floor and bracket
    floors = []
    for m in range(3, 8):
        s = m - 1
        for t in range(4):
            choice = {ab: int(rng.integers(0, 2)) for ab in order(s)}
            D = base_and_jacobian(m, s, 'random', choice)
            M, H = D['M'], D['H']
            e = np.sqrt(D['W']) * (-1.0) ** D['J']
            u = np.zeros(M * H); u[(H - 1) * M:H * M] = e
            Wout = np.einsum('ihk,k->ih', D['T'], u)
            fl = float(np.linalg.norm(Wout, 2))
            lo, up, _ = tensor_bracket(D['T'], starts=8)
            floors.append(dict(m=m, s=s, last_col_floor=fl, sigma_over_beta=float(D['sig'][-1] / D['beta'][-1]),
                               kappa_lower=float(lo), kappa_upper=float(up)))
            assert fl >= 1 - 1e-12
            print('random rule', floors[-1], flush=True)
    json.dump(dict(rows=rows, random_rules=floors, numpy=np.__version__, elapsed=time.monotonic() - t0),
              open(outpath, 'w'), indent=1)
    print('ALL PASS', time.monotonic() - t0)


if __name__ == '__main__':
    main(sys.argv[1])
