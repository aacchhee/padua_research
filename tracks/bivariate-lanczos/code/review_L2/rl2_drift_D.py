"""L2 reconstruction 01, item 3 part D: L-shape (rng(1)) and annulus (rng(2)), M = 3000, n = 30: BJ + CGS2-all
(double), reference-free theta_LB and drift against a box-frame Legendre reference (long double QR), with kappa.
Own code.  MEASURED.  Usage: python3 -I rl2_drift_D.py > logs_L2/drift_D.log"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R

LD = R.LD


def lshape(M, seed):
    rng = np.random.default_rng(seed); out = []
    while len(out) < M:
        p = rng.uniform(-1, 1, 2)
        if not (p[0] > 0 and p[1] > 0):
            out.append(p)
    return np.array(out)


def annulus(M, seed, r0=0.5):
    rng = np.random.default_rng(seed); out = []
    while len(out) < M:
        p = rng.uniform(-1, 1, 2)
        if r0 <= np.hypot(*p) <= 1:
            out.append(p)
    return np.array(out)


for name, P in (('lshape', lshape(3000, 1)), ('annulus', annulus(3000, 2))):
    t0 = time.time()
    x, y = P[:, 0].copy(), P[:, 1].copy(); w = np.ones(len(x)); n = 30
    Q = R.recur(x, y, w, n, rule='bj', orth='cgs2all')
    Wd = np.linalg.qr(Q)[0]
    dX, dY = R.defects(Wd, x, y, n)
    ns = [16, 20, 24, 28, 30]
    lb = {s: float(dX[:s].max() / (2 * np.abs(x).max())) for s in ns}
    V = R.vander_product(np.asarray(x, dtype=LD), np.asarray(y, dtype=LD), w, n, 'legendre')
    kap = {s: R.kappa(np.asarray(V[:, :R.Nof(s)], dtype=np.float64)) for s in ns}
    Uo = R.hqr(V)[0]
    ang = R.sin_angles_nested(Wd.astype(LD), Uo, ns)
    print(f"  {name}: M=3000 loss={np.abs(Q.T @ Q - np.eye(Q.shape[1])).max():.1e}; " +
          " ".join(f"n={s}: thetaLB={lb[s]:.1e} sin(Leg box, LD)={ang[s]:.1e} kappa={kap[s]:.1e} (u*kappa={R.U * kap[s]:.0e})"
                   for s in ns) + f" ({time.time() - t0:.0f}s)", flush=True)
