"""S1 audit: compare lambda_min on Pi_N (full interpolation space) and Pi_{N-1} (dense, small N)."""
import sys, json
import numpy as np
from numpy.polynomial import legendre as Lg
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from cc_tools import cc_weights
out=[]
for N in [100, 101, 400, 401, 1600, 1601, 3200]:
    x = np.cos(np.arange(N + 1) * np.pi / N); w = cc_weights(N)
    V = Lg.legvander(x, N) * np.sqrt((2 * np.arange(N + 1) + 1) / 2)
    G = V.T @ (w[:, None] * V)
    full = np.linalg.eigvalsh(G)[0]; con = np.linalg.eigvalsh(G[:N, :N])[0]
    L = np.log(N)
    out.append(dict(N=N, full=float(full), constrained=float(con), L2full=float(L*L*full), L2con=float(L*L*con)))
    print(out[-1], flush=True)
json.dump(out, open(sys.argv[1], 'w'), indent=1)
