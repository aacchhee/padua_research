"""C01-6: re-run the R07 noise models (IDEA?...-118 H_term, -119, -120) with noise scale u = 2^-53 (plan unit
roundoff) instead of the scripts' EPS = 2^-52; same sets, seeds and decision rules.  MEASURED only.
Usage: python3 -I l1_c01_u53_rerun.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_r07_offpattern_anatomy as A
import l1_r07_termwise_predictor as T
import l1_r07_closed_loop as CL

U53 = 2.0 ** -53
A.EPS = U53; T.EPS = U53; CL.EPS = U53


def sets(names):
    out = []
    for name, m, f in names:
        if f is None:
            X, Y = np.cos(np.pi * np.arange(m + 1) / m), np.cos(np.pi * np.arange(m + 2) / (m + 1))
        else:
            X, Y = f(np.linspace(-1, 1, m + 1)), f(np.linspace(-1, 1, m + 2))
        out.append((name, X, Y))
    return out


cub30 = ('cubic s|s|^2, m=30', 30, lambda s: s * np.abs(s) ** 2)
eq30 = ('equispaced, m=30', 30, lambda s: s)
quad = ('quadratic s|s|, m=30', 30, lambda s: s * np.abs(s))
quar = ('quartic s|s|^3, m=30', 30, lambda s: s * np.abs(s) ** 3)
cub36 = ('cubic s|s|^2, m=36', 36, lambda s: s * np.abs(s) ** 2)
cl30 = ('Chebyshev-Lobatto, m=30', 30, None)
order = {'survives': 0, 'inconclusive': 1, 'killed': 2}

print(f"# l1_c01_u53_rerun.py numpy={np.__version__} noise scale u = 2^-53")
print("## IDEA-118 (H_term row is the criterion; other rows unchanged by the noise scale)")
for name, X, Y in sets([cub30]):
    A.run(name, X, Y)
print("## IDEA-119")
v = []
for name, X, Y in sets([quad, quar, cub36, cl30]):
    loss, est = T.run(name, X, Y)
    if loss[20] >= 1e-13:
        r = [est[n] / loss[n] for n in (16, 20)]
        vv = 'killed' if any(x < 0.01 or x > 100 for x in r) else ('survives' if all(0.1 <= x <= 10 for x in r) else 'inconclusive')
    else:
        vv = 'survives' if est[20] < 1e-12 else ('killed' if est[20] >= 1e-11 else 'inconclusive')
    v.append(vv); print(f"   verdict on {name}: {vv}", flush=True)
print(f"# IDEA-119 overall: {max(v, key=order.get)}")
print("## IDEA-120")
v = []
for name, X, Y in sets([cub30, eq30, quad, quar, cub36, cl30]):
    loss, cl = CL.run(name, X, Y)
    if loss[20] >= 1e-13:
        r = [cl[n] / loss[n] for n in (16, 20)]
        vv = 'killed' if any(x < 0.02 or x > 50 for x in r) else ('survives' if all(0.2 <= x <= 5 for x in r) else 'inconclusive')
    else:
        vv = 'survives' if cl[20] < 1e-12 else ('killed' if cl[20] >= 1e-11 else 'inconclusive')
    v.append(vv); print(f"   verdict on {name}: {vv}", flush=True)
print(f"# IDEA-120 overall: {max(v, key=order.get)}")
