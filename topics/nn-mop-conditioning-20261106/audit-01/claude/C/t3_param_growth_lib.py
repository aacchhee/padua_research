"""High-precision terminal parity responses for larger N (independent moment solves in z,
central FD in epsilon), compared with the parameter lower bound and identity (11)."""
import sys, json, time
import mpmath as mp
from fractions import Fraction as Fr
from math import comb

def terminal_b(z, w1, w2, n, m):
    M = n+m
    rows, rhs = [], []
    for w, cnt in ((w1, n), (w2, m)):
        for r in range(cnt):
            rows.append([mp.fsum(w[l]*z[l]**(r+j) for l in range(len(z))) for j in range(M)])
            rhs.append(-mp.fsum(w[l]*z[l]**(r+M) for l in range(len(z))))
    c = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    return c[M-1] + mp.fsum(z)

