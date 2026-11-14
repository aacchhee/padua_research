"""MEASURED: next-order structure of the corner remainder
   R_n = Lambda_c(n) - [ (4/pi^2)(log N + d)^2 + kappa - 1/N ],  N = n+1/2,
using the exact positive formula (paper cu:positive), binary64 + math.fsum per row.
kappa: PD-T271 30-digit decimal (MEASURED use only)."""
import numpy as np, math, sys, json, time
from mpmath import mp, mpf, euler, log, pi as mpi
mp.dps = 30
kappa = mpf('0.9197101183884925350995182257905')
d = euler + log(8/mpi)
def corner(n):
    m = n + 1
    th = np.arange(n + 1) * np.pi / n
    ph = np.arange(n + 1) * np.pi / m          # k = 0..n (k=m terms vanish)
    eps = np.ones(n + 1); eps[0] = eps[n] = 0.5
    eta = np.ones(n + 1); eta[0] = 0.5
    cth = np.cos(th); cph = np.cos(ph)
    rows = []
    for j in range(n + 1):
        k = np.arange((j + 1) % 2, n + 1, 2)     # j+k odd
        f = (1 + cph[k]) / np.abs(cth[j] - cph[k])
        rows.append(eps[j] * math.fsum((eta[k] * f).tolist()))
    return 4 * math.fsum(rows) / (n * m) + 1 / m
out = []
ns = [int(x) for x in sys.argv[1:]] or [100, 101, 200, 201, 400, 401, 800, 801, 1600, 1601, 2400, 2401]
t0 = time.process_time()
for n in ns:
    N = mpf(n) + mpf(1) / 2
    main = 4 / mpi**2 * (log(N) + d)**2 + kappa - 1 / N
    R = mpf(corner(n)) - main
    out.append((n, float(R), float(R * N**2), float(R * N**2 / log(N))))
    print(n, "R=%.4e  R*N^2=%.6f  R*N^2/logN=%.6f" % out[-1][1:])
print("CPU", time.process_time() - t0)
json.dump(out, open('corner_next_out.json', 'w'))
