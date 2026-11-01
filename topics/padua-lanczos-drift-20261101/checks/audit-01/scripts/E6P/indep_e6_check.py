"""Auditor's independent E6 check (does not import any campaign code).

1. Rebuilds the L2 rotpi4 / triangle node sets from their written definition
   (rng seed 11, M=1681) and confirms identity by the recorded input_sha256.
2. Calls polyrat's vandermonde_arnoldi_CGS directly (own loader) in [y,x] and [x,y].
3. Re-implements BJ-dev and reversed-order mirror full CGS2 independently and
   compares entrywise with polyrat (order/selection check by execution).
4. Builds an independent reference orthonormal basis of Pi_n on the nodes in
   80-bit long double (product Legendre in the inverse-rotated frame for the
   square, product Legendre on the bounding box for the triangle; MGS twice),
   and computes the largest principal-angle sine between span(Q) and Pi_n.
5. Generic smooth targets (not ridge functions) and off-sample random interior
   test points, comparing polyrat fit error with reference-span fit error.
"""
import sys, json, hashlib, types, importlib, pathlib
import numpy as np
from numpy.polynomial import legendre as Lg

EXT = pathlib.Path('/workspace/padua-drift-external/polyrat')
sys.path.insert(0, str(EXT.parent / 'deps'))
pkg = types.ModuleType('polyrat'); pkg.__path__ = [str(EXT / 'polyrat')]
sys.modules['polyrat'] = pkg
arn = importlib.import_module('polyrat.arnoldi')
LD = np.longdouble

def sets():
    rng = np.random.default_rng(11); M = 1681
    sq = rng.uniform(-1, 1, (M, 2))
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1: dk.append(p)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1: tr.append(2 * p - 1)
    return sq, np.array(tr)

def rot(P, th):
    c, s = np.cos(th), np.sin(th)
    return P @ np.array([[c, s], [-s, c]])

def mgs2_ld(V):
    V = np.array(V, dtype=LD); M, N = V.shape; Q = np.zeros((M, N), dtype=LD)
    for k in range(N):
        q = V[:, k].copy()
        for _ in range(2):
            for j in range(k):
                q -= (Q[:, j] @ q) * Q[:, j]
        Q[:, k] = q / np.sqrt(q @ q)
    return Q

def mgs2_ld_fast(V):
    # block CGS2 in long double (vectorised); then one more MGS-free CGS pass
    V = np.array(V, dtype=LD); M, N = V.shape; Q = np.zeros((M, N), dtype=LD)
    for k in range(N):
        q = V[:, k].copy()
        for _ in range(3):
            s = Q[:, :k].T @ q; q -= Q[:, :k] @ s
        Q[:, k] = q / np.sqrt(q @ q)
    return Q

def legvals(z, n):
    # Legendre P_0..P_n in long double by three-term recurrence
    z = np.asarray(z, dtype=LD); out = [np.ones_like(z), z.copy()]
    for k in range(1, n):
        out.append(((2 * k + 1) * z * out[k] - k * out[k - 1]) / (k + 1))
    return out[:n + 1]

def jacvals(z, n, al):
    # Jacobi P_k^{(al,0)}, k=0..n, long double, standard three-term recurrence
    z = np.asarray(z, dtype=LD); al = LD(al); out = [np.ones_like(z)]
    if n >= 1: out.append(((al + 2) * z + al) / 2)
    for k in range(1, n):
        a1 = 2 * (k + 1) * (k + al + 1) * (2 * k + al)
        a2 = (2 * k + al + 1) * (al * al)
        a3 = (2 * k + al) * (2 * k + al + 1) * (2 * k + al + 2)
        a4 = 2 * (k + al) * k * (2 * k + al + 2)
        out.append(((a2 + a3 * z) * out[k] - a4 * out[k - 1]) / a1)
    return out[:n + 1]

def refbasis(Z, n, tri=False):
    if not tri:
        a = legvals(Z[:, 0], n); b = legvals(Z[:, 1], n)
        return np.column_stack([a[t - j] * b[j] for t in range(n + 1) for j in range(t + 1)])
    x, y = Z[:, 0], Z[:, 1]; om = (1 - y) / 2
    a = np.where(om > 0, (2 * (1 + x) / np.where(om > 0, 1 - y, 1)) - 1, LD(-1))
    A = legvals(a, n); cols = []
    for t in range(n + 1):
        for j in range(t + 1):
            p = t - j; B = jacvals(y, j, 2 * p + 1)
            cols.append(A[p] * om ** p * B[j])
    return np.column_stack(cols)

def backsub_ld(R, b):
    R = np.array(R, dtype=LD); b = np.array(b, dtype=LD); N = len(b); x = np.zeros(N, dtype=LD)
    for i in range(N - 1, -1, -1):
        x[i] = (b[i] - R[i, i + 1:] @ x[i + 1:]) / R[i, i]
    return x

def own_cgs2(P, w, n, mode):
    """mode 'dev': order j=0..t, (t,0)=x*(t-1,0), (t,j)=y*(t-1,j-1).
       mode 'mirror_rev': order j=t..0 (j=y-exponent), (t,t)=y*(t-1,t-1), else x*(t-1,j)."""
    x, y = P[:, 0], P[:, 1]
    cols = []; pos = {}
    for t in range(n + 1):
        js = range(t + 1) if mode == 'dev' else range(t, -1, -1)
        for j in js: pos[(t, j)] = len(cols); cols.append((t, j))
    M = len(P); N = len(cols); Q = np.zeros((M, N))
    q = np.sqrt(w).astype(float); Q[:, 0] = q / np.linalg.norm(q)
    for k in range(1, N):
        t, j = cols[k]
        if mode == 'dev':
            v = x * Q[:, pos[(t - 1, 0)]] if j == 0 else y * Q[:, pos[(t - 1, j - 1)]]
        else:
            v = y * Q[:, pos[(t - 1, t - 1)]] if j == t else x * Q[:, pos[(t - 1, j)]]
        for _ in range(2):
            s = Q[:, :k].T @ v; v = v - Q[:, :k] @ s
        Q[:, k] = v / np.linalg.norm(v)
    return Q

def gap_ld(Q, U):
    W = mgs2_ld_fast(Q)
    D = U - W @ (W.T @ U)
    sv = np.linalg.svd(np.array(D, dtype=float), compute_uv=False)
    _, _, vt = np.linalg.svd(np.array(D, dtype=float))
    return float(sv[0]), vt[0]

def main():
    sq, tr = sets(); out = {}
    rng = np.random.default_rng(20261101)
    cases = [('rotpi4', rot(sq, np.pi / 4), 24, np.pi / 4), ('triangle', tr, 20, 0.0)]
    for name, P, n, th in cases:
        w = np.ones(len(P))
        sha = hashlib.sha256(P.tobytes() + w.tobytes()).hexdigest()
        Qyx, Hyx, iyx = arn.vandermonde_arnoldi_CGS(P[:, [1, 0]], n, weight=np.sqrt(w))
        Qxy, Hxy, ixy = arn.vandermonde_arnoldi_CGS(P[:, [0, 1]], n, weight=np.sqrt(w))
        Qdev = own_cgs2(P, w, n, 'dev'); Qmr = own_cgs2(P, w, n, 'mirror_rev')
        # reference frame
        if th:
            c, s = np.cos(LD(th)), np.sin(LD(th))
            PL = np.array(P, dtype=LD); Z = np.column_stack([c * PL[:, 0] + s * PL[:, 1], -s * PL[:, 0] + c * PL[:, 1]])
        else:
            Z = np.array(P, dtype=LD)
        tri = (name == 'triangle'); V = refbasis(Z, n, tri); V = V / np.sqrt((V * V).sum(axis=0))
        svV = np.linalg.svd(np.array(V, dtype=float), compute_uv=False)
        U = mgs2_ld_fast(V)
        orthU = float(np.max(np.abs(np.array(U.T @ U - np.eye(U.shape[1], dtype=LD), dtype=float))))
        g_yx, vmiss = gap_ld(Qyx, U); g_xy, _ = gap_ld(Qxy, U)
        G = Qyx.T @ Qyx - np.eye(Qyx.shape[1])
        off = G - np.diag(np.diag(G))
        # adversarial target from MY reference: f = U vmiss (unit weighted norm)
        f = np.array(U @ vmiss.astype(LD), dtype=float)
        c_yx = np.linalg.lstsq(Qyx, f, rcond=None)[0]
        res_adv = float(np.linalg.norm(Qyx @ c_yx - f))
        # off-sample random interior test points
        T0 = rng.uniform(-1, 1, (400, 2)) if th else None
        if th:
            T = rot(T0, th); ZT = np.column_stack([c * np.array(T, dtype=LD)[:, 0] + s * np.array(T, dtype=LD)[:, 1], -s * np.array(T, dtype=LD)[:, 0] + c * np.array(T, dtype=LD)[:, 1]])
        else:
            T = []
            while len(T) < 400:
                p = rng.uniform(0, 1, 2)
                if p.sum() <= 1: T.append(2 * p - 1)
            T = np.array(T); ZT = np.array(T, dtype=LD)
        nrm = np.sqrt((refbasis(Z, n, tri) ** 2).sum(axis=0)); VT = refbasis(ZT, n, tri) / nrm; VM = refbasis(np.array((P[:128] + P[-128:]) / 2, dtype=LD) if not th else np.column_stack([c * np.array((P[:128] + P[-128:]) / 2, dtype=LD)[:, 0] + s * np.array((P[:128] + P[-128:]) / 2, dtype=LD)[:, 1], -s * np.array((P[:128] + P[-128:]) / 2, dtype=LD)[:, 0] + c * np.array((P[:128] + P[-128:]) / 2, dtype=LD)[:, 1]]), n, tri) / nrm
        # coefficients of f in V-basis: V a = U vmiss  -> a = lstsq in long double via U^T
        R = np.triu(np.array(U.T @ V, dtype=LD))  # V = U R
        a = backsub_ld(R, vmiss)  # f = V a
        ftrue = np.array(VT @ a, dtype=float); fmid = np.array(VM @ a, dtype=float)
        Emid = arn.vandermonde_arnoldi_eval(((P[:128] + P[-128:]) / 2)[:, [1, 0]], Hyx, iyx)
        E = arn.vandermonde_arnoldi_eval(T[:, [1, 0]], Hyx, iyx)
        test_adv = float(np.linalg.norm(E @ c_yx - ftrue) / np.linalg.norm(ftrue)); mid_adv = float(np.linalg.norm(Emid @ c_yx - fmid) / np.linalg.norm(fmid))
        smooth = {}
        for lab, fn in [('cos(3x+y)exp(y/2)', lambda X: np.cos(3 * X[:, 0] + X[:, 1]) * np.exp(X[:, 1] / 2)),
                        ('1/(2+x^2+0.7xy-y)', lambda X: 1 / (2 + X[:, 0] ** 2 + 0.7 * X[:, 0] * X[:, 1] - X[:, 1])),
                        ('exp(x+y)', lambda X: np.exp(X[:, 0] + X[:, 1]))]:
            g = fn(P); gt = fn(T)
            cq = np.linalg.lstsq(Qyx, g, rcond=None)[0]
            pq = E @ cq
            # reference-span LS fit (long double U) and evaluation through V-coefficients
            cu = np.array(U.T @ g.astype(LD), dtype=float)
            au = backsub_ld(R, cu)
            pu = np.array(VT @ au, dtype=float)
            smooth[lab] = {'train_rel_polyrat': float(np.linalg.norm(Qyx @ cq - g) / np.linalg.norm(g)),
                           'train_rel_reference': float(np.linalg.norm(np.array(U, dtype=float) @ cu - g) / np.linalg.norm(g)),
                           'test_rel_polyrat': float(np.linalg.norm(pq - gt) / np.linalg.norm(gt)),
                           'test_rel_reference': float(np.linalg.norm(pu - gt) / np.linalg.norm(gt)),
                           'polyrat_vs_reference_test_pred_rel': float(np.linalg.norm(pq - pu) / np.linalg.norm(gt))}
        out[name] = {'n': n, 'M': len(P), 'input_sha256': sha,
                     'polyrat_yx_vs_own_dev_maxabs': float(np.max(np.abs(Qyx - Qdev))),
                     'polyrat_xy_vs_own_mirror_reversed_maxabs': float(np.max(np.abs(Qxy - Qmr))),
                     'polyrat_index_yx_first_degree3': iyx[6:10].tolist(),
                     'ref_basis': 'product Legendre, long double MGS-free CGS3 (inverse-rotated frame)' if th else 'own long-double Koornwinder/Dubiner (collapsed Legendre x Jacobi(2p+1,0)), long double CGS3',
                     'ref_kappa_double_svd': float(svV[0] / svV[-1]), 'ref_triangular_resid': float(np.max(np.abs(np.array(U @ R - V, dtype=float)))), 'ref_orth_maxabs_ld': orthU,
                     'gap_polyrat_yx': g_yx, 'gap_polyrat_xy': g_xy,
                     'gram_max_all': float(np.max(np.abs(G))), 'gram_max_offdiag': float(np.max(np.abs(off))),
                     'gram_00_entry': float(G[0, 0]),
                     'adv_train_residual_yx': res_adv, 'adv_test_rel_error_yx_random400': test_adv, 'adv_test_rel_error_yx_campaign_midpoints': mid_adv,
                     'smooth': smooth}
        print(name, json.dumps(out[name], indent=1), flush=True)
    pathlib.Path(sys.argv[1]).write_text(json.dumps(out, indent=2) + '\n')

if __name__ == '__main__':
    main()
