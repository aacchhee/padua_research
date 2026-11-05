#!/usr/bin/env python3
"""Claude audit: check the PD-T106 kernel weight formula against the defining
moment equations V^T w = (h_a h_b)_{a+b<=m} by a 80-digit mpmath linear solve,
for both parities. Independent of producer/checker code (written from
definitions.md only)."""
import mpmath as mp, sys, json
mp.mp.dps = 80
def h(r): return mp.mpf(0) if r % 2 else mp.mpf(2)/(1-r*r)
def T(r, x): return mp.cos(r*mp.acos(x))
out = []
for m in range(1, int(sys.argv[1])+1):
    xs = [mp.cos(j*mp.pi/m) for j in range(m+1)]
    ys = [mp.cos(k*mp.pi/(m+1)) for k in range(m+2)]
    pts = [(j, k) for j in range(m+1) for k in range(m+2) if (j+k) % 2 == 0]
    modes = [(a, b) for a in range(m+1) for b in range(m+1-a)]
    assert len(pts) == len(modes)
    V = mp.matrix(len(modes), len(pts))
    for i, (a, b) in enumerate(modes):
        for c, (j, k) in enumerate(pts):
            V[i, c] = T(a, xs[j])*T(b, ys[k])
    rhs = mp.matrix([h(a)*h(b) for a, b in modes])
    w = mp.lu_solve(V, rhs)
    # kernel formula
    err = mp.mpf(0)
    for c, (j, k) in enumerate(pts):
        ej = mp.mpf(1)/2 if j in (0, m) else 1
        ek = mp.mpf(1)/2 if k in (0, m+1) else 1
        rho = mp.mpf(2)*ej*ek/(m*(m+1))
        K = 0
        for a, b in modes:
            ca = 1 if a == 0 else 2; cb = 1 if b == 0 else 2
            d = ca*cb*h(a)*h(b)
            if a == m and b == 0: d /= 2
            K += d*T(a, xs[j])*T(b, ys[k])
        err = max(err, abs(rho*K - w[c]))
    out.append((m, float(err), float(sum(w))))
    print(m, mp.nstr(err, 5), mp.nstr(sum(w), 20), flush=True)
