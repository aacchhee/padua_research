"""Auditor's own floating quality samples (lower samples only) and QR/Leja controls."""
import sys, json, math, time
import numpy as np
import scipy.linalg as sla
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes
from aud_mr import MT, RT, m_nodes, r_nodes

OUT = sys.argv[1]


def basis(P, n):
    mo = np.array(modes(n))
    T = [np.cos(np.arccos(np.clip(P[:, j], -1, 1))[:, None] * np.arange(n + 1)[None, :]) for j in range(3)]
    return T[0][:, mo[:, 0]] * T[1][:, mo[:, 1]] * T[2][:, mo[:, 2]]


def basis_rec(P, n):
    # three-term recurrence version, used for QR selection (closer to polynomial evaluation)
    mo = np.array(modes(n)); T = []
    for j in range(3):
        x = P[:, j]; t = np.ones((len(P), n + 1))
        if n:
            t[:, 1] = x
        for k in range(2, n + 1):
            t[:, k] = 2 * x * t[:, k - 1] - t[:, k - 2]
        T.append(t)
    return T[0][:, mo[:, 0]] * T[1][:, mo[:, 1]] * T[2][:, mo[:, 2]]


def lebesgue(P, n, m):
    V = basis_rec(P, n); N = len(V)
    sv = np.linalg.svd(V, compute_uv=False); cond = sv[0] / sv[-1]
    Vi = np.linalg.inv(V); res = float(np.max(np.abs(V @ Vi - np.eye(N)).sum(axis=1)))
    ax = np.cos(np.pi * np.arange(m) / (m - 1)); best = 0.0
    for i in range(m):
        mesh = np.array([(ax[i], y, z) for y in ax for z in ax])
        lam = np.abs(basis_rec(mesh, n) @ Vi).sum(axis=1)
        best = max(best, float(lam.max()))
    return best, float(cond), res


def angles_to_points(L, X):
    return np.cos(2 * np.pi * np.array(sorted(X), dtype=float) / L)


def pivoted_gs(A, N):
    """Businger-Golub column pivoting by explicit re-orthogonalised Gram-Schmidt."""
    A = A.copy(); K = A.shape[1]; chosen = []; Q = []
    norms = (A * A).sum(axis=0)
    for _ in range(N):
        k = int(np.argmax(norms)); chosen.append(k)
        v = A[:, k].copy()
        for q in Q:
            v -= q * (q @ v)
        for q in Q:
            v -= q * (q @ v)
        v /= np.linalg.norm(v); Q.append(v)
        A -= np.outer(v, v @ A)
        norms = (A * A).sum(axis=0); norms[chosen] = -1
    return chosen


def controls(n):
    N = len(modes(n))
    ax2 = np.cos(np.pi * np.arange(2 * n + 1) / (2 * n))
    can = np.array([(x, y, z) for x in ax2 for y in ax2 for z in ax2])
    A = basis_rec(can, n).T
    mine = pivoted_gs(A, N)
    _, _, piv = sla.qr(A, mode='economic', pivoting=True)
    same = sorted(mine) == sorted(piv[:N].tolist())
    qr = can[sorted(mine)]
    a = np.cos(np.pi * np.arange(n + 1) / n); order = [0]; left = list(range(1, n + 1))
    while left:
        sc = [np.prod([abs(a[i] - a[j]) for j in order]) for i in left]
        k = left[int(np.argmax(sc))]  # argmax returns first maximiser = smallest index among ties
        order.append(k); left.remove(k)
    ax = a[order]; leja = np.array([[ax[i], ax[j], ax[k]] for i, j, k in modes(n)])
    out = {'qr_selection_matches_lapack': same}
    for nm, P in (('QR', qr), ('Leja', leja)):
        out[nm] = [lebesgue(P, n, m)[0] for m in (21, 41)]
    return out


def main():
    res = {}; t0 = time.time()
    which = sys.argv[2].split(',') if len(sys.argv) > 2 else ['ctrl', 'MR', 'SF', 'C']
    if 'ctrl' in which:
        for n in range(3, 9):
            res[f'ctrl{n}'] = controls(n); print('ctrl', n, res[f'ctrl{n}'], round(time.time() - t0), flush=True)
    if 'MR' in which:
        for route, tab, fn in (('M', MT, m_nodes), ('R', RT, r_nodes)):
            for n in range(3, 9):
                L, A, B = fn(n, tab[n]); P = angles_to_points(L, A | B)
                v = [lebesgue(P, n, m) for m in (21, 41)]
                res[f'{route}{n}'] = [x[0] for x in v] + [v[1][1], v[1][2]]
                print(route, n, res[f'{route}{n}'], round(time.time() - t0), flush=True)
    if 'SF' in which:
        from aud_f import nodes as fnodes
        for lab, n, z in (('S3', 3, (1, 4, 11)), ('S5', 5, (1, 17, 30))):
            N = len(modes(n)); L = 4 * N
            X = {tuple(min((2 * k + 1) * g % L, L - (2 * k + 1) * g % L) for g in z) for k in range(2 * N)}
            assert len(X) == N
            v = [lebesgue(angles_to_points(L, X), n, m) for m in (21, 41)]; res[lab] = [x[0] for x in v]
            print(lab, res[lab], flush=True)
        L, X = fnodes(6, 18, 1, 14, 0, 0); v = [lebesgue(angles_to_points(L, X), 5, m) for m in (21, 41)]
        res['F5'] = [x[0] for x in v]; print('F5', res['F5'], flush=True)
    if 'C' in which:
        P28 = ((13,98),(13,142),(16,93),(16,147),(17,28),(17,212),(26,37),(26,203),(28,223),(37,214),(44,113),(44,127),
               (66,85),(66,155),(76,99),(76,141),(85,174),(93,224),(98,227),(99,164),(113,196),(127,196),(141,164),(142,227),
               (147,224),(155,174),(203,214),(212,223))
        ctrl = res.get('ctrl7') or controls(7); rows = []
        for b, c in P28:
            L = 480
            X = {tuple(min((2 * k + 1) * g % L, L - (2 * k + 1) * g % L) for g in (1, b, c)) for k in range(240)}
            assert len(X) == 120
            v = [lebesgue(angles_to_points(L, X), 7, m) for m in (21, 41)]
            q = max(v[0][0] / ctrl['QR'][0], v[1][0] / ctrl['QR'][1])
            lj = min(v[0][0] / ctrl['Leja'][0], v[1][0] / ctrl['Leja'][1])
            rows.append([b, c, v[0][0], v[1][0], q, lj, v[1][1], v[1][2]])
            print('C', rows[-1], round(time.time() - t0), flush=True)
        res['C'] = rows
        res['C_summary'] = {'min_q': min(r[4] for r in rows), 'max_q': max(r[4] for r in rows),
                            'passes': sum(r[4] <= 1 for r in rows), 'min_leja_ratio': min(r[5] for r in rows),
                            'L21_range': [min(r[2] for r in rows), max(r[2] for r in rows)],
                            'L41_range': [min(r[3] for r in rows), max(r[3] for r in rows)],
                            'cond_range': [min(r[6] for r in rows), max(r[6] for r in rows)], 'max_res': max(r[7] for r in rows)}
        print(res['C_summary'])
    json.dump(res, open(OUT, 'w'), indent=1)


if __name__ == '__main__':
    main()
