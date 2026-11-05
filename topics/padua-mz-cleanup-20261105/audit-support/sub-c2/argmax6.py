import numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/subC2')
from majorant import weights
for m in (101, 201, 401, 601, 801, 1201):
    W, S, mask = weights(m)
    R = (m - 1) // 2
    j = np.arange(m + 1)[:, None]; k = np.arange(m + 2)[None, :]
    b6 = np.pi ** 4 * j * k + 2.5 * np.pi ** 2 * (j + k) + 25 / 4 + 400 * (1 + np.log(R))
    r6 = np.where(mask, m * m * np.abs(S) / b6, 0)
    jj, kk = np.unravel_index(np.argmax(r6), r6.shape)
    # also pieces at that node
    print(f"m={m}: max ratio {r6[jj,kk]:.4f} at (j,k)=({jj},{kk}); m^2 S = {m*m*S[jj,kk]:.3f}; RHS = {b6[jj,kk]:.3f}")
