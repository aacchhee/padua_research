"""Sanity check (seconds): inertia-based count of joint eigenvalues of a commuting
symmetric pair (H_x, H_y) in a box, using M = (H_x-a)(a'-H_x)(H_y-b)(b'-H_y).
Random real nodes, graded Chebyshev-Vandermonde QR. Also report commutator size
and the bandwidth of M. Not a result; a feasibility probe for gen2-draft-3."""
import numpy as np
from numpy.polynomial import chebyshev as C

rng = np.random.default_rng(1)
n = 8
N = (n + 1) * (n + 2) // 2
M_pts = N  # square case (unisolvent generic set)
x = rng.uniform(-1, 1, M_pts); y = rng.uniform(-1, 1, M_pts)
w = rng.uniform(0.5, 1.5, M_pts)
# graded-lex Chebyshev basis
cols = []
for k in range(n + 1):
    for i in range(k, -1, -1):
        j = k - i
        cols.append(C.chebval(x, np.eye(i + 1)[i]) * C.chebval(y, np.eye(j + 1)[j]))
V = np.sqrt(w)[:, None] * np.array(cols).T
Q, R = np.linalg.qr(V)
Hx = Q.T @ (x[:, None] * Q); Hy = Q.T @ (y[:, None] * Q)
comm = np.linalg.norm(Hx @ Hy - Hy @ Hx)
print(f"N={N}, ||[Hx,Hy]||={comm:.2e}, bandwidth check: max|Hx| outside band ~")
# bandwidth: graded blocks
deg = np.array([k for k in range(n + 1) for _ in range(k + 1)])
off = np.abs(deg[:, None] - deg[None, :]) > 1
print(f"max |Hx| off block-tridiagonal = {np.abs(Hx[off]).max():.2e}")

def count_box(a, a2, b, b2):
    Mx = (Hx - a * np.eye(N)) @ (a2 * np.eye(N) - Hx)
    My = (Hy - b * np.eye(N)) @ (b2 * np.eye(N) - Hy)
    Mm = Mx @ My
    S = 0.5 * (Mm + Mm.T)
    ev = np.linalg.eigvalsh(S)
    return int((ev > 0).sum()), float(np.linalg.norm(Mm - Mm.T)), float(np.abs(ev).min())

for (a, a2, b, b2) in [(-1, 0, -1, 0), (-0.5, 0.5, -0.5, 0.5), (0, 1, -1, 1), (-0.3, 0.3, 0.2, 0.9)]:
    true = int(((x > a) & (x < a2) & (y > b) & (y < b2)).sum())
    cnt, asym, minabs = count_box(a, a2, b, b2)
    print(f"box x in({a},{a2}) y in({b},{b2}): true={true} inertia={cnt} asym={asym:.1e} min|ev|={minabs:.1e}")

print("--- corrected joint count: n_box = (n_prod - N + n_x + n_y)/2 ---")
def inertia(Mat):
    S = 0.5*(Mat+Mat.T); return int((np.linalg.eigvalsh(S) > 0).sum())
for (a, a2, b, b2) in [(-1, 0, -1, 0), (-0.5, 0.5, -0.5, 0.5), (0, 1, -1, 1), (-0.3, 0.3, 0.2, 0.9)]:
    true = int(((x > a) & (x < a2) & (y > b) & (y < b2)).sum())
    I = np.eye(N)
    Mx = (Hx - a*I) @ (a2*I - Hx); My = (Hy - b*I) @ (b2*I - Hy)
    nx, ny, np_ = inertia(Mx), inertia(My), inertia(Mx @ My)
    print(f"box: true={true}  joint-inertia count={(np_ - N + nx + ny)//2}  (nx={nx}, ny={ny}, nprod={np_})")
