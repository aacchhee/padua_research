"""MEASURED, cancellation-free: f(u,v)=(1+cos v)/|cos u-cos v| with
cos u - cos v = -2 sin((u+v)/2) sin((u-v)/2) and 1+cos v = 2 cos^2(v/2);
all half-angles are pi*integer/(2nm) reduced exactly."""
import numpy as np, math, sys, json, time
from mpmath import mp, mpf, euler, log, pi as mpi
from indep_S import sinpi_red
mp.dps = 30
kappa = mpf('0.9197101183884925350995182257905')
d = euler + log(8/mpi)
def corner(n):
    m = n + 1; den = 2 * n * m
    rows = []
    for j in range(n + 1):
        k = np.arange((j + 1) % 2, n + 1, 2, dtype=np.int64)
        U = j * m; V = k * n                     # u = pi U/(nm), v = pi V/(nm)
        sp = np.abs(sinpi_red(U + V, den)); sm = np.abs(sinpi_red(U - V, den))
        c2 = sinpi_red(V + n * m, den) ** 2      # cos(v/2)=sin(pi(V+nm)/(2nm))
        f = 2 * c2 / (2 * sp * sm)
        eta = np.where(k == 0, 0.5, 1.0)
        e = 0.5 if j in (0, n) else 1.0
        rows.append(e * math.fsum((eta * f).tolist()))
    return 4 * math.fsum(rows) / (n * m) + 1 / m
ns = [int(x) for x in sys.argv[1:]] or [100, 101, 200, 201, 400, 401, 800, 801, 1600, 1601, 3200, 3201, 6400, 6401]
out = []; t0 = time.process_time()
for n in ns:
    N = mpf(n) + mpf(1) / 2
    R = mpf(corner(n)) - (4 / mpi**2 * (log(N) + d)**2 + kappa - 1 / N)
    out.append((n, float(R * N**2)))
    print(n, "R*N^2=%.7f" % out[-1][1])
print("CPU", time.process_time() - t0)
json.dump(out, open('corner_next2_out.json', 'w'))
