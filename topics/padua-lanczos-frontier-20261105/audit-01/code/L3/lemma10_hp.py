import numpy as np, mpmath as mp
mp.mp.dps = 50
rng = np.random.default_rng(5)
worst = (0, None)
for trial in range(20000):
    n = rng.integers(2, 9); m = rng.integers(1, n + 1)
    Q, _ = np.linalg.qr(rng.standard_normal((n, m)))
    E = rng.standard_normal((n, m)) * 10.0 ** rng.uniform(-6, 0.5)
    Qt, _ = np.linalg.qr(Q + E)
    Qt = Qt * np.sign(np.sum(Qt * Q, axis=0) + 1e-300)
    lhs = np.linalg.norm(Qt @ Qt.T - Q @ Q.T, 2)
    mid = np.linalg.norm(Qt - Q, 2); rhs = np.linalg.norm(Qt - Q, 'fro')
    for name, val in [('lhs/mid', lhs / mid), ('mid/fro', mid / rhs)]:
        if val > worst[0]:
            worst = (val, (name, n, m, Q.copy(), Qt.copy()))
    r0 = rng.standard_normal(n); r = r0 + rng.standard_normal(n) * 10.0 ** rng.uniform(-6, 1)
val, (name, n, m, Q, Qt) = worst
print('float64 worst', val, name, n, m)
# recompute in high precision: re-orthonormalize Q and Qt exactly (mp QR) to remove float non-orthonormality
def mp_orth(A):
    A = mp.matrix(A.tolist())
    cols = []
    for j in range(A.cols):
        v = A[:, j]
        for _ in range(2):
            for c in cols:
                v = v - (c.T * v)[0] * c
        v = v / mp.norm(v)
        cols.append(v)
    M = mp.matrix(A.rows, A.cols)
    for j, c in enumerate(cols):
        for i in range(A.rows): M[i, j] = c[i]
    return M
Qm, Qtm = mp_orth(Q), mp_orth(Qt)
D = Qtm * Qtm.T - Qm * Qm.T
lhs = max(mp.svd_r(D, compute_uv=False)); mid = max(mp.svd_r(Qtm - Qm, compute_uv=False))
fro = mp.norm(Qtm - Qm)  # mp.norm of matrix: Frobenius (p=2 on entries)
fro = mp.sqrt(sum((Qtm[i, j] - Qm[i, j]) ** 2 for i in range(n) for j in range(m)))
print('high-precision lhs/mid', mp.nstr(lhs / mid, 20), 'mid/fro', mp.nstr(mid / fro, 20), 'mid', mp.nstr(mid, 5))
