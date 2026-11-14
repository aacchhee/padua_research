#!/usr/bin/env python3
"""C4C numerical checks (MEASURED; double precision on finite grids) of the
scalar-profile, signed-origin and half-line-residual statements in companion
comparison-unified.tex L1990-4020 (24a98db). Uses scipy.special digamma."""
import numpy as np
from scipy.special import digamma, polygamma

worst = {}


def upd(k, v):
    worst[k] = max(worst.get(k, -np.inf), float(v))


LP = np.log(np.pi)


def Cfun(t):
    return -digamma(t) - digamma(1 - t)


def Phi(t):
    return np.sin(np.pi * t) / np.pi * (Cfun(t) - 2 * LP)


def dPhi(t):
    Cp = -polygamma(1, t) + polygamma(1, 1 - t)
    return np.cos(np.pi * t) * (Cfun(t) - 2 * LP) + np.sin(np.pi * t) / np.pi * Cp


def d2Phi(t):
    Cp = -polygamma(1, t) + polygamma(1, 1 - t)
    Cpp = -polygamma(2, t) - polygamma(2, 1 - t)
    return (-np.pi * np.sin(np.pi * t) * (Cfun(t) - 2 * LP) + 2 * np.cos(np.pi * t) * Cp
            + np.sin(np.pi * t) / np.pi * Cpp)


def f(w):
    return Phi(0.5 + w / (2 * np.pi))


def fp(w):
    return dPhi(0.5 + w / (2 * np.pi)) / (2 * np.pi)


# scalar profile facts used at L2352-2365, L2928, L826
t = np.linspace(1e-6, 1 - 1e-6, 400001)
upd("sup|Phi'| / 12  (text: |Phi'|<=12; table gives 11)", np.max(np.abs(dPhi(t))) / 12)
upd("sup|Phi''| / 35", np.max(np.abs(d2Phi(t))) / 35)
w = np.linspace(-np.pi + 1e-6, np.pi - 1e-6, 400001)
fw = f(w)
upd("sup f  (<=1)", np.max(fw))
upd("-inf f + 1/2 (<0 means f>1/2)", 0.5 - np.min(fw))
print("f(0)=", f(0.0), " so N_s=c_e f+c_d f <= c_e+c_d <= 2 (text says channels <=4, |N_s|<=8)")
fpw = fp(w)
jump = fp(-np.pi + 1e-9) - fp(np.pi - 1e-9)
upd("Var_per f' / 4 (grid + endpoint jump)", (np.sum(np.abs(np.diff(fpw))) + abs(jump)) / 4)


# F_0 on the origin (L2864-3001, 3792-3833)
def F0_parts(z, L):
    b = 2 / np.tan(z / 2) - 4 / z
    d = 1 / (2 * np.sin(z / 2)) - 1 / z
    f0 = f(0.0)
    fz = f(z)
    P0 = 2 * (fz - f0) / z + 2 * fz * d
    Q0 = 2 / np.tan(z / 2) * np.log(np.sin(z)) - 4 * np.log(z) / z
    F0 = (L / np.pi) * b + P0 + Q0 / np.pi
    bp = -1 / np.sin(z / 2) ** 2 + 4 / z ** 2
    dp = -np.cos(z / 2) / (4 * np.sin(z / 2) ** 2) + 1 / z ** 2
    fpz = fp(z)
    P0p = 2 * fpz / z - 2 * (fz - f0) / z ** 2 + 2 * fpz * d + 2 * fz * dp
    Q0p = (-np.log(np.sin(z)) / np.sin(z / 2) ** 2 + 2 / np.tan(z / 2) / np.tan(z)
           - 4 * (1 - np.log(z)) / z ** 2)
    F0p = (L / np.pi) * bp + P0p + Q0p / np.pi
    return F0, F0p, b, d, P0, Q0


for n in (32, 33, 64, 160, 512, 4096):
    m = n + 1
    h = np.pi / m
    L = np.log(n)
    # sup |F0'| on [2h, pi-h]
    z = np.linspace(2 * h, np.pi - h, 400001)
    F0, F0p, b, d, P0, Q0 = F0_parts(z, L)
    M = (4 / 3) * L + (2 / 3) * np.log(m) + 20 / 3
    upd("sup|F0'| on [2h,pi-h] / ((4/3)L+(2/3)log m+20/3)", np.max(np.abs(F0p)) / M)
    V = np.sum(np.abs(np.diff(F0p)))
    upd("Var F0' on [2h,pi-h] / (L/2+(25/2)log m+37/3)  [grid lower bound]", V / (L / 2 + 12.5 * np.log(m) + 37 / 3))
    upd("2M+V bound vs 17L+27: ((19/6)L+(83/6)log m+77/3)/(17L+27)",
        ((19 / 6) * L + (83 / 6) * np.log(m) + 77 / 3) / (17 * L + 27))
    # Var F0' on [h/2, pi-h/2]
    z2 = np.concatenate([np.geomspace(h / 2, 0.5, 200001), np.linspace(0.5, np.pi - 0.5, 200001),
                         np.pi - np.geomspace(0.5, h / 2, 200001)])
    _, F0p2, *_ = F0_parts(z2, L)
    V2 = np.sum(np.abs(np.diff(F0p2)))
    upd("Var F0' on [h/2,pi-h/2] / V_F  [grid lower bound]", V2 / (L / 2 + 12.5 * np.log(2 * m) + 37 / 3))
    # central holes z>=21pi/22: F0 < -1/25
    zc = np.linspace(21 * np.pi / 22, np.pi - 1e-7, 200001)
    F0c, *_ = F0_parts(zc, max(L, 3.0))
    upd("central hole: max F0 + 1/25 (<0 required)", np.max(F0c) + 1 / 25)
    # initial holes z<=5h/2: d<z/16, P0<7z/6, F0 <= 7z/6 + (z/pi) log_+(pi/(2nz))
    zi = np.geomspace(1e-7, 5 * h / 2, 200001)
    F0i, _, bi, di, P0i, Q0i = F0_parts(zi, L)
    upd("initial hole: max d/(z/16)", np.max(di / (zi / 16)))
    upd("initial hole: max P0/(7z/6)", np.max(P0i / (7 * zi / 6)))
    env = 7 * zi / 6 + (zi / np.pi) * np.maximum(np.log(np.pi / (2 * n * zi)), 0)
    upd("initial hole: max F0 - envelope (<=0 required)", np.max(F0i - env))

# |D0 - a D0(0)| <= 5 rho/3 on rho<=1 (L3526)
rng = np.random.default_rng(7)
f0 = f(0.0)
for _ in range(20000):
    x = rng.uniform(0, 1); y = rng.uniform(0, 1 - x); rho = x + y
    ce, cd = np.cos(rho / 2), np.cos((x - y) / 2); a = ce * cd
    U0 = ce * f(x - y) + cd * f(x + y)
    D0 = U0 / np.pi + 4 * a / np.pi ** 2 * LP
    D00 = 2 * f0 / np.pi + 4 / np.pi ** 2 * LP
    upd("|D0-aD0(0)|/(5rho/3)", abs(D0 - a * D00) / (5 * rho / 3))
    upd("|D0-aD0(0)|/(0.4 rho^2)", abs(D0 - a * D00) / (0.4 * rho ** 2))
    # Dbar_phi = 4(ce+cd)/pi + a b0 log pi vs actual D0
    upd("D0/((ce+cd)/pi + a b0 log pi)", D0 / ((ce + cd) / np.pi + a * 4 / np.pi ** 2 * LP))


# half-line matched-cell defect and residual increment (L3159-3259)
def rfun(wv):
    return np.where(wv < np.pi / 2, 1 / np.tan(np.minimum(wv, np.pi / 2 - 1e-300)) - 1 / wv, -1 / wv)


def Rprim(wv):
    return np.where(wv < np.pi / 2, np.log(np.sin(np.minimum(wv, np.pi / 2))) - np.log(wv), -np.log(wv))


def Edef(hh, v, tt):
    K = int(np.ceil((np.pi / 2 - v) / hh)) + 1
    k = np.arange(K)
    samp = rfun(v + hh * (k + tt))
    cell = (Rprim(v + (k + 1) * hh) - Rprim(v + k * hh)) / hh
    dK = (v + K * hh) / hh
    return np.sum(samp - cell) + (digamma(dK + tt) - np.log(dK)) / hh


for n in (32, 64, 160, 512):
    m = n + 1
    hs = np.pi / n
    for _ in range(300):
        x = rng.uniform(0, 1); y = rng.uniform(0, 1 - x); rho = x + y
        if rho < 1e-6:
            continue
        ce, cd = np.cos(rho / 2), np.cos((x - y) / 2); a = ce * cd
        xi = x / np.pi
        for side in (1, -1):
            s = side * y / np.pi
            for j in rng.choice(np.arange(2 if side > 0 else 3, n // 2 + 1), size=6, replace=False):
                v = np.pi * (j + s) / m; v0 = np.pi * j / m
                th = [(1 - s + xi) / 2 + (j + s) / (2 * m), (1 - s - xi) / 2 + (j + s) / (2 * m)]
                th0 = 0.5 + j / (2 * m)
                Ev = [Edef(hs, v, tt) for tt in th]
                E0 = Edef(hs, v0, th0)
                wv = a / np.tan(v / 2) / 2
                wv0 = a / np.tan(v0 / 2) / 2
                Delta = 2 * (wv * sum(Ev) - wv0 * 2 * E0)
                B = a * (16 * rho * m / (3 * np.pi ** 2 * j) + (4 * np.pi ** 2 / 27 + 80 / (9 * np.pi)) * y / j
                         + (10 * np.pi * m / (27 * n)) * y / j ** 2)
                upd("half-line residual increment |Delta|/displayed bound", abs(Delta) / B)
                for tt, Evv in zip(th, Ev):
                    upd("|E-(1/2-t)r(v)|/(5h/24)", abs(Evv - (0.5 - tt) * rfun(np.array([v]))[0]) / (5 * hs / 24))
                    upd("theta in (0,1): max(-theta, theta-1)", max(-tt, tt - 1))
                upd("sum|theta_pm-theta_0|/(rho/pi)", (abs(th[0] - th0) + abs(th[1] - th0)) / (rho / np.pi))
                upd("cot(v/2)/(8/(3v0))", (1 / np.tan(v / 2)) / (8 / (3 * v0)))
                upd("|cot(v/2)-cot(v0/2)|/(8pi^2 y/(9 m v0^2))",
                    abs(1 / np.tan(v / 2) - 1 / np.tan(v0 / 2)) / (8 * np.pi ** 2 * max(y, 1e-300) / (9 * m * v0 ** 2)) if y > 1e-9 else 0)

for k in sorted(worst):
    print(f"{k:80s} {worst[k]: .4e}")
