#!/usr/bin/env python3
"""Audit-04 J01 supplement.

Part A (exact intervals, own evaluator j01_own.py): corner-256 constants of
paper ul:corner-lemma at n=256: T>107/10, ebar<1/5, KD<1/5, CEbar<3/2,
C4<9/500, kWy<93/100, M(256)<26, deltaA-rU*M>2729/21000, deltaD-2rU*M>49/1000,
delta-M*pi^4/6144>49/2000, (16/pi^2)(49/2000)>1/30.  Also the paper's
intermediate claims C/Theta<3/50 at 512 and <1/10 at 192.
Part B (MEASURED, mpmath floats, not a proof): first closing integer n of
each gate, and a log-spaced real-n monotonicity sanity scan on [160,1e9].
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
import j01_own as J
import mpmath as mp

chk = {}
c = J.consts(256)
L = c["L"]
q_h, rU = F(7, 48), F(2, 125)
h = J.PI / 4
jstar = J.J0
M = (4 * L.sq() + F(79, 5) * L) / J.PI.sq() + F(9, 4) + c["CE"] + 2 * c["KD"]
dA = q_h * (c["T"] - c["ebar"] + jstar) - F(1, 4) - c["C4"] - h * c["ky"]
dD = 2 * q_h * (c["T"] + jstar) - F(4, 15) - c["CE"] - F(3, 2) * c["KD"] - c["ebar"]
chk["(1-cos(pi/4))/2>7/48"] = (1 - J.INV_SQRT2.hi) / 2 > q_h
chk["L(256) in (277/50,111/20)"] = L.lo > F(277, 50) and L.hi < F(111, 20)
chk["T(256)>107/10"] = c["T"].lo > F(107, 10)
chk["ebar(256)<1/5"] = c["ebar"].hi < F(1, 5)
chk["KD(256)<1/5"] = c["KD"].hi < F(1, 5)
chk["CEbar(256)<3/2"] = c["CE"].hi < F(3, 2)
chk["C4(256)<9/500"] = c["C4"].hi < F(9, 500)
chk["kWy(256)<93/100"] = c["ky"].hi < F(93, 100)
chk["M(256)<26"] = M.hi < 26
chk["rU>pi^4/6144"] = rU > (J.PI.sq().sq() / 6144).hi
chk["dA-rU*M>2729/21000"] = (dA - rU * M).lo > F(2729, 21000)
chk["dD-2rU*M>49/1000"] = (dD - 2 * rU * M).lo > F(49, 1000)
d = J.Iv(min((dA).lo, (dD / 2).lo), min(dA.hi, (dD / 2).hi))
chk["delta-M*pi^4/6144>49/2000"] = (d - M * J.PI.sq().sq() / 6144).lo > F(49, 2000)
chk["(16/pi^2)(49/2000)>1/30"] = (16 / J.PI.sq() * F(49, 2000)).lo > F(1, 30)
# central-pair constants used by the corner lemma
I4 = F(319, 360)
kap = 4 * I4 / J.PI.sq()
chk["4I4/pi^2<9/25"] = kap.hi < F(9, 25)
chk["Ec(h,h)<(9/25)/sqrt2<4/15"] = (F(9, 25) * J.INV_SQRT2).hi < F(4, 15)
print("n=256: T", c["T"], "ebar", c["ebar"], "KD", c["KD"], "CE", c["CE"], "C4", c["C4"],
      "kWy", c["ky"], "M", M)
print("dA-rU M", dA - rU * M, " dD-2rU M", dD - 2 * rU * M)
# Paper's intermediate ratio claims
g1 = J.gate(512, J.sin_q(F(1, 2)), J.cos_q(F(1, 2)))
g2 = J.gate(192, J.INV_SQRT2, J.INV_SQRT2)
chk["C/Theta(512)<3/50"] = g1["ratio"].hi < F(3, 50)
chk["C/Theta(192)<1/10"] = g2["ratio"].hi < F(1, 10)
chk["tan(1/2)>1/2"] = (J.sin_q(F(1, 2)) / J.cos_q(F(1, 2))).lo > F(1, 2)
# CEbar and ebar at the far base 192 for the report
print("n=192: CE", g2["CE"], "ebar", g2["ebar"], "KD", g2["KD"], "Theta", g2["Theta"])
print("n=512: CE", g1["CE"], "ebar", g1["ebar"], "KD", g1["KD"], "Theta", g1["Theta"])
for k, v in chk.items():
    print("CHECK", k, v)
okA = all(chk.values())
print("PART_A_PASS", okA)

# ---------------- Part B: MEASURED scans (floats) ----------------
mp.mp.dps = 30
pi = mp.pi


def cf(n):
    n = mp.mpf(n)
    m = n + 1
    L = mp.log(n)
    H = 1 + L
    b = 4 / pi**2
    r0 = mp.log(mp.mpf(5) / 2) + mp.mpf(1) / 18
    T = (4 * L**2 - 3 * L) / pi**2
    D = ((52 / pi**2) * H + 7) / n + 10 / n**2 + 20 * H / (pi * n**2)
    Mesh = (b * (2 * L + 2 * r0) / n + (4 + b * (L + 1 / n)) / (4 * n**2 - 1)
            + b / (2 * n - 1)**2 + (5 + b * (mp.log(n + 0.5) + 2)) / (4 * (n - 0.5)**2))
    eb = D + Mesh + 1 / n
    KD = ((6 + 16 / (3 * pi)) * H + 2 / pi) / n
    MA = 1 / pi + 4 / pi**2
    gn = 1 + mp.log(2 + 8 * m / (3 * pi))
    Gg = (7 * MA * L + mp.mpf(111) / 2 + (63 + mp.log(2) + 4 * mp.log(pi) + 7 * mp.log(m)
                                          + 16 * mp.log(2 * m) + 1.5 * gn) / pi) / m
    W = (3 * mp.log(m) + mp.log(2) + 2 * mp.log(pi) + 2) / (pi * m)
    CE = D + Gg + (64 + 16 * L) / n + 318 / n**2 + Mesh + W
    A4 = 4 / n + 40 * H / (pi * n**2)
    C4 = A4 + 20 / n**2
    db = (17 * L + 27) / n**2
    kx = (9.5 * H + mp.mpf(23) / 3 * L + 77.5) / n + 152 / n**2
    ky = kx + db
    U = T - eb + A4 + 0.092
    d1, d2 = 11 * U / 48 - mp.mpf(5) / 12, 11 * U / 48
    l1, l2 = kx + mp.mpf(5) / 48, ky
    S0 = d1 + d2
    e = d1 * d2 / S0
    f = (d2 * l1 + d1 * l2) / S0
    g = (l1 - l2)**2 / (4 * S0)
    peak = C4 + l1**2 / (4 * d1) + l2**2 / (4 * d2)
    half = C4 + g + f / 2 - e / 4
    vert = l1 / (2 * d1) + l2 / (2 * d2)
    Th = T + 0.092
    C = 0.442 + 2 * KD

    def G(r1):
        hh = r1 / 2
        return Th * (1 - mp.cos(hh)) - C * mp.sin(hh) - 0.442**2 * mp.cos(hh) / (2 * Th) - CE - eb

    return dict(peak=peak, half=half, vert=vert, G1=G(1), G2=G(pi / 2), d1=d1, U=U,
                ratio=C / Th, CE=CE, eb=eb, KD=KD, l1=l1, l2=l2, C4=C4)


LO, HI = 160, 2400
table = {n: cf(n) for n in range(LO, HI)}


def first(pred):
    bad = [n for n in range(LO, HI) if not pred(table[n])]
    return (max(bad) + 1) if bad else LO


thr = {}
thr["max P_n<41/1000"] = first(lambda v: v["peak"] < 0.041)
thr["P_n(1/2)<-1/7"] = first(lambda v: v["half"] < -1 / 7)
thr["vertex<1/2"] = first(lambda v: v["vert"] < 0.5)
thr["G(n,1)>1/2"] = first(lambda v: v["G1"] > 0.5)
thr["G(n,pi/2)>3/100"] = first(lambda v: v["G2"] > 0.03)
thr["tan(1/2)>=C/Theta"] = first(lambda v: v["ratio"] < mp.tan(0.5))
for k, v in thr.items():
    print("MEASURED smallest integer n in [160,2400) after which it holds through 2399:", k, v)
# real-n monotonicity sanity (log grid)
import math
grid = [160 * (10 ** (k / 400)) for k in range(0, 2800)]
vals = [cf(n) for n in grid]
mono = {}
for key, sign in (("peak", -1), ("half", -1), ("vert", -1), ("G1", 1), ("G2", 1), ("d1", 1),
                  ("U", 1), ("ratio", -1), ("CE", -1), ("eb", -1), ("KD", -1), ("l1", -1),
                  ("l2", -1), ("C4", -1)):
    seq = [v[key] for v in vals]
    ok = all(sign * (seq[i + 1] - seq[i]) > 0 for i in range(len(seq) - 1))
    mono[key] = ok
print("MEASURED log-grid real-n monotonicity on [160, %.3g]:" % grid[-1], mono)
print("grid points", len(grid))
sys.exit(0 if okA else 1)
