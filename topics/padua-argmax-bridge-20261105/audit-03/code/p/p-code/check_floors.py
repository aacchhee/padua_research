"""Referee spot check (MEASURED, float64) of Lemma ul:selected-pairs:
actual eligible projections Q_v(K), Q_h(J) versus the stated floors.
Projections are computed from the paper's own half formula A(u,v)/(cos u-cos v),
derived independently by the referee from G_n=[P_n(cos u)-P_n(cos v)]/(cos u-cos v)-cos nu.
"""
import math, sys, time
import numpy as np
t0 = time.process_time()

def d(z, w):
    return np.abs(z) + np.abs(w) - np.abs(z + w)

def Afun(u, v, al, be):
    a = (math.cos(al) + math.cos(be)) / 2
    return a * (1 + np.cos(v)) - (math.sin(al) / 2) * np.sin(u) + (math.sin(be) / 2) * np.sin(v)

def Gn_direct(n, u, v):
    # check helper: (-1)^r G_n/2 from the Chebyshev sum, used once for validation
    s = 0.0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            nu = (1 if p == 0 else 2) * (1 if q == 0 else 2)
            s += nu * math.cos(p * u) * math.cos(q * v)
    return s - math.cos(n * u)

def Qv_all(n, al, be):
    m = n + 1; N = n * m
    res = []
    r = np.arange(2 * n)
    u = (r * np.pi + al) / n
    cu = np.cos(u)
    for K in range(1, m):
        k = np.arange(1, m)[:, None]
        par = (K + 1 + k) % 2  # r parity required
        mask = (r[None, :] % 2) == par
        vp = ((K + k) * np.pi + be) / m; vm = ((K - k) * np.pi + be) / m
        Vp = Afun(u[None, :], vp, al, be) / (cu[None, :] - np.cos(vp))
        Vm = Afun(u[None, :], vm, al, be) / (cu[None, :] - np.cos(vm))
        res.append(np.sum(np.where(mask, d(Vp, Vm), 0.0)) / N)
    return np.array(res)

def Qh_all(n, al, be):
    m = n + 1; N = n * m
    res = []
    s = np.arange(2 * m)
    v = (s * np.pi + be) / m
    cv = np.cos(v)
    for J in range(1, n):
        K_par = (J + 1) % 2
        j = np.arange(1, n)[:, None]
        mask = ((s[None, :] + j) % 2) == K_par
        up = ((J + j) * np.pi + al) / n; um = ((J - j) * np.pi + al) / n
        Hp = Afun(up, v[None, :], al, be) / (np.cos(up) - cv[None, :])
        Hm = Afun(um, v[None, :], al, be) / (np.cos(um) - cv[None, :])
        res.append(np.sum(np.where(mask, d(Hp, Hm), 0.0)) / N)
    return np.array(res)

def floors(n, r):
    a = 1 - r * r / 4
    U = 347 * a / 1000 - 157 * r / 500; V = 17 * a / 20 - r / 2; W = 779 * a / 750 - 5 * r / 6
    B = 11711 * U / 48400 - 120 * V / (157 * n) - 250 * W / (157 * n) - 100 * V / (3 * n * n)
    if 41 <= n < 64: fin = max(1 / 512, min(1 / 32, B))
    elif 64 <= n < 160: fin = max(1 / 64, min(1 / 20, B))
    elif 160 <= n < 512: fin = max(1 / 32, min(1 / 20, B))
    else: fin = None
    tail = None
    if n >= 64 and r <= 21 / 40:
        pp = 22 / 7
        eta = a * (1 - (4 * pp + r) / n) - r / 2
        Fn = 2 * eta / (pp + r) * n / (n + 1) * (1 / 4 - 1 / n)
        Fs = 35 / 286 * (1 - 6 / n)**2 * (a - r / 2)
        Ar = 97 * a / 100 - r / 2
        Ih = 2303 * a / 5000 - 471 * r / 1250; Rh = 4837 * a / 1875 - 5 * r / 3
        Fh = 539 * Ih / 1936 - (140 * Ar + 400 * Rh) / (157 * n) - 800 * Ar / (3 * n * n)
        tail = min(Fn, Fs, Fh)
    return fin, tail

# validate the half formula once against the Chebyshev sum
n = 7; m = 8; al, be = 0.31, -0.17
errs = []
for rr in range(2 * n):
    for ss in range(2 * m):
        if (rr + ss) % 2 == 1:
            u = (rr * math.pi + al) / n; v = (ss * math.pi + be) / m
            lhs = (-1)**rr * Gn_direct(n, u, v) / 2
            rhs = Afun(u, v, al, be) / (math.cos(u) - math.cos(v))
            errs.append(abs(lhs - rhs))
print('half-formula validation max err (n=7):', max(errs))

rhos = [0.02, 0.2, 0.5]
dirs = [(1, 0), (0, 1), (0.5, 0.5), (0.8, -0.2), (-0.3, 0.7), (-0.9, -0.1)]
rows = []
for n in [41, 42, 63, 64, 100, 159, 160, 320]:
    worst = None
    for rho in rhos:
        for (cx, cy) in dirs:
            s = abs(cx) + abs(cy)
            al = rho * cx / s + 1e-7 * math.sqrt(2); be = rho * cy / s - 1e-7 * math.sqrt(3)
            qv = Qv_all(n, al, be).min(); qh = Qh_all(n, al, be).min()
            q = min(qv, qh)
            fin, tail = floors(n, rho + 2e-7)
            fl = max(x for x in (fin, tail) if x is not None)
            ratio = q / fl
            if worst is None or ratio < worst[0]:
                worst = (ratio, rho, (cx, cy), q, fin, tail)
    rows.append((n, worst))
    print('n=%d worst ratio actual/floor=%.3f at rho=%s dir=%s  actual=%.5f finite=%s tail=%s' % (n, worst[0], worst[1], worst[2], worst[3], worst[4], worst[5]))
    sys.stdout.flush()
print('cpu_s', time.process_time() - t0)
