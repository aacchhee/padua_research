#!/usr/bin/env python3
"""[E] F06: direct float64 evaluation of the projected defects defined in
theory/F06-phase-floor.md eq.(3), at distance-two centres, versus the theorem
floor 1/5-3r/20 with r=|alpha|+|beta| (the strongest admissible r).
MEASURED cross-check at sampled (n,J,K,alpha,beta); not a proof.
G(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(n u), P=T_{n+1}+T_n, evaluated by the
product formula sin(k s)sin(k d)/(sin s sin d), s=(u+v)/2, d=(u-v)/2 (stable at collisions).
"""
import numpy as np
rng = np.random.default_rng(20261108)

def ratio(k, x):
    sx = np.sin(x); out = np.empty_like(x)
    small = np.abs(sx) < 1e-9
    out[~small] = np.sin(k*x[~small])/sx[~small]
    j = np.round(x[small]/np.pi)
    out[small] = k*((-1.0)**(j*(k - 1)))   # L'Hopital limit at x=j*pi
    return out

def G(n, u, v):
    s = (u + v)/2; d = (u - v)/2
    dd = 0.0
    for k in (n + 1, n):
        dd = dd + ratio(k, s)*ratio(k, d)
    return dd - np.cos(n*u)

def dfun(X, Y):
    return np.abs(X) + np.abs(Y) - np.abs(X + Y)

def Qv(n, J, K, al, be):
    m = n + 1; N = n*m; phi = (K*np.pi + be)/m; tot = 0.0
    z = np.arange(2*n)
    for k in range(m + 1):
        f = 0.5 if k in (0, m) else 1.0
        zz = z[(z + k - J) % 2 == 0]
        u = (zz*np.pi + al)/n
        sg = np.where(zz % 2 == 0, 1.0, -1.0)
        Vp = sg*G(n, u, np.full_like(u, phi + k*np.pi/m))/2
        Vm = sg*G(n, u, np.full_like(u, phi - k*np.pi/m))/2
        tot += f*dfun(Vp, Vm).sum()
    return tot/N

def Qh(n, J, K, al, be):
    m = n + 1; N = n*m; th = (J*np.pi + al)/n; tot = 0.0
    z = np.arange(2*m)
    for j in range(n + 1):
        e = 0.5 if j in (0, n) else 1.0
        zz = z[(z + j - K) % 2 == 0]
        v = (zz*np.pi + be)/m
        sg = (-1.0)**(J + j)
        Wp = sg*G(n, np.full_like(v, th + j*np.pi/n), v)/2
        Wm = sg*G(n, np.full_like(v, th - j*np.pi/n), v)/2
        tot += e*dfun(Wp, Wm).sum()
    return tot/N

if __name__ != "__main__":
    raise SystemExit
worst = (9, None)
count = 0
for n in (128, 129, 160, 255, 256):
    m = n + 1
    for trial in range(10):
        r = rng.uniform(0, np.pi/4); w = rng.uniform(-1, 1)
        al = w*r*rng.choice([-1, 1]); be = (r - abs(al))*rng.choice([-1, 1])
        if trial == 0: al, be = 0.0, 0.0
        if trial == 1: al, be = np.pi/4, 0.0
        if trial == 2: al, be = 0.0, -np.pi/4
        r = abs(al) + abs(be); floor = 0.2 - 3*r/20
        for K in (2, m - 2):                     # vertical, both orientations
            Js = [j for j in range(0, n + 1) if (j + K) % 2 == 1]
            for J in rng.choice(Js, 2, replace=False):
                q = Qv(n, int(J), K, al, be); count += 1
                if q - floor < worst[0]: worst = (q - floor, ('Qv', n, int(J), K, al, be, q, floor))
        for J in (2, n - 2):                     # horizontal
            Ks = [k for k in range(0, m + 1) if (J + k) % 2 == 1]
            for K in rng.choice(Ks, 2, replace=False):
                q = Qh(n, J, int(K), al, be); count += 1
                if q - floor < worst[0]: worst = (q - floor, ('Qh', n, J, int(K), al, be, q, floor))
print("evaluations:", count)
print("minimum of Q - (1/5-3r/20) over samples:", worst[0])
print("attained at (proj, n, J, K, alpha, beta, Q, floor):", worst[1])
