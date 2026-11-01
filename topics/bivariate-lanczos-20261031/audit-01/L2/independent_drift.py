"""Codex L2 audit: independent BJ/CGS2 and stable polynomial references.

Imports no developer/reconstruction modules. All conclusions are MEASURED.
Run from repository root with OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I PATH.
"""
import json
import platform
import numpy as np
import scipy
from scipy.special import eval_jacobi


def count(n):
    return (n + 1) * (n + 2) // 2


def nodes():
    rng = np.random.default_rng(11)
    sq = rng.uniform(-1, 1, (1681, 2))
    disk = []
    while len(disk) < 1681:
        v = rng.uniform(-1, 1, 2)
        if v @ v <= 1:
            disk.append(v)
    tri = []
    while len(tri) < 1681:
        v = rng.uniform(0, 1, 2)
        if v.sum() <= 1:
            tri.append(2 * v - 1)
    return sq, np.asarray(tri)


def bj(P, n, dtype):
    P = P.astype(dtype)
    q = np.zeros((len(P), count(n)), dtype=dtype)
    q[:, 0] = 1 / np.sqrt(dtype(len(P)))
    for d in range(1, n + 1):
        for j in range(d + 1):
            k = count(d - 1) + j
            parent = count(d - 2) + max(j - 1, 0)
            v = P[:, int(j > 0)] * q[:, parent]
            # Explicit full CGS2: no recurrence window or coefficient reuse.
            for _ in range(2):
                h = q[:, :k].T @ v
                v = v - q[:, :k] @ h
            q[:, k] = v / np.sqrt(v @ v)
    return q


def products(P, n, kind):
    xs = np.polynomial.legendre.legvander(P[:, 0], n) if kind == 'legendre' else np.polynomial.chebyshev.chebvander(P[:, 0], n)
    ys = np.polynomial.legendre.legvander(P[:, 1], n) if kind == 'legendre' else np.polynomial.chebyshev.chebvander(P[:, 1], n)
    v = np.column_stack([xs[:, d-j] * ys[:, j] for d in range(n+1) for j in range(d+1)])
    return v / np.linalg.norm(v, axis=0)


def dubiner(P, n):
    u, v = (P[:, 0] + 1) / 2, (P[:, 1] + 1) / 2
    a = 2 * u / (1-v) - 1
    b = 2 * v - 1
    out = np.column_stack([eval_jacobi(i, 0, 0, a) * (1-v)**i * eval_jacobi(d-i, 2*i+1, 0, b)
                           for d in range(n+1) for i in range(d, -1, -1)])
    return out / np.linalg.norm(out, axis=0)


def largest_sine(U, W):
    return float(np.linalg.svd(W - U @ (U.T @ W), compute_uv=False)[0])


def main():
    print(json.dumps(dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                          unit_roundoff=float(np.finfo(float).epsneg), longdouble_unit_roundoff=float(np.finfo(np.longdouble).epsneg))), flush=True)
    sq, tri = nodes()
    angle = np.pi / 4
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    rot = sq @ rotation.T
    # The inverse uses the rounded nodes, not a separately stored exact sample.
    unrot = (rot.astype(np.longdouble) @ np.linalg.inv(rotation).T.astype(np.longdouble)).astype(float)
    for label, P, n, refs in [('rotpi4', rot, 24, [products(unrot, 24, 'legendre'), products(unrot, 24, 'chebyshev')]),
                             ('triangle', tri, 20, [dubiner(tri, 20)])]:
        U = [np.linalg.qr(v)[0] for v in refs]
        print(json.dumps(dict(bench=label, reference_condition=[float(np.linalg.cond(v)) for v in refs],
                              reference_disagreement=largest_sine(U[0], U[-1]))), flush=True)
        for dtype in [np.float64, np.longdouble]:
            Q = bj(P, n, dtype)
            gram_error = float(np.max(np.abs(Q.T @ Q - np.eye(Q.shape[1], dtype=dtype))))
            W = np.linalg.qr(Q.astype(float))[0]
            rows = []
            running_bound = 0.0
            for d in range(n + 1):
                if d < n:
                    block = W[:, count(d-1):count(d)]
                    future = W[:, :count(d+1)]
                    for a in range(2):
                        product = P[:, a, None] * block
                        defect = np.linalg.norm(product - future @ (future.T @ product), axis=0).max()
                        running_bound = max(running_bound, float(defect/(2*np.max(np.abs(P[:, a])))))
                if d in [8, 12, 16, 18, 20, 22, 24] and d <= n:
                    rows.append(dict(degree=d, drift=[largest_sine(u[:, :count(d)], W[:, :count(d)]) for u in U]))
            print(json.dumps(dict(bench=label, arithmetic=np.dtype(dtype).name, gram_max=gram_error,
                                  max_stage_drift_lower_bound=running_bound, rows=rows)), flush=True)


if __name__ == '__main__':
    main()
