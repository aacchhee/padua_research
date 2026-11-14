"""Independent (non-Arb) evaluator of the Padua primitive S_n and actual lambda_n,
written from the paper's displayed formulas only (preliminaries.tex
eq:angular-kernel, localization-unified.tex ul:primitive, ul:cardinal-reflection).

G_n(u,v) = D_n(u,v) - cos(n u),   D_n = sum_{|p|+|q|<=n} e^{i(pu+qv)}
         = R_{n+1}(S) R_{n+1}(T) + R_n(S) R_n(T),   S=(u+v)/2, T=(v-u)/2,
R_k(x) = sin(kx)/sin(x)  (k (-1)^{j(k-1)} at x=j*pi).

Every angle is pi * (integer)/(integer); arguments are reduced EXACTLY with
Python/numpy integers before one sin evaluation, so every factor has small
relative error (no cancellation in sin S, sin T near collisions).

This prototype is FLOATING (binary64, MEASURED). Rigorous version: replace
sinpi by an own Taylor polynomial with nextafter widening (see i-ideas.md).
"""
import numpy as np
from fractions import Fraction as F
from math import lcm


def sinpi_red(num, den):
    """sin(pi*num/den) for int64 arrays num, scalar den>0, exact reduction."""
    r = np.mod(num, 2 * den)            # in [0, 2den)
    sign = np.where(r >= den, -1.0, 1.0)
    r = np.where(r >= den, r - den, r)  # in [0, den): sin(pi*(x+1)) = -sin(pi x)
    r = np.where(2 * r > den, den - r, r)  # sin(pi(1-x)) = sin(pi x), x in [0,1/2]
    return sign * np.sin(np.pi * (r / den))


def Rk(k, num, den):
    """sin(k x)/sin(x), x = pi*num/den, vectorised, exact removable values."""
    s = sinpi_red(num, den)
    t = sinpi_red(k * num, den)
    zero = np.mod(num, den) == 0
    j = num // den
    lim = k * np.where(np.mod(j * (k - 1), 2) == 0, 1.0, -1.0)
    out = np.empty_like(s)
    nz = ~zero
    out[nz] = t[nz] / s[nz]
    out[zero] = lim[zero]
    return out


def H_board(n, a, b):
    """H_rs for (r,s) in Gamma^-; phases alpha=pi*a, beta=pi*b with rational a,b."""
    a, b = F(a), F(b)
    m = n + 1
    Q = lcm(a.denominator, b.denominator)
    aQ, bQ = a.numerator * (Q // a.denominator), b.numerator * (Q // b.denominator)
    r = np.arange(2 * n, dtype=np.int64)[:, None]
    s = np.arange(2 * m, dtype=np.int64)[None, :]
    mask = ((r + s) % 2 == 1)
    rr = np.broadcast_to(r, mask.shape)[mask]
    ss = np.broadcast_to(s, mask.shape)[mask]
    # u = pi (r+a)/n = pi (rQ+aQ) m /(nmQ);  v = pi (s+b)/m = pi (sQ+bQ) n /(nmQ)
    U = (rr * Q + aQ) * m
    V = (ss * Q + bQ) * n
    den = 2 * n * m * Q                  # S = pi (U+V)/den, T = pi (V-U)/den
    Snum, Tnum = U + V, V - U
    D = Rk(n + 1, Snum, den) * Rk(n + 1, Tnum, den) + Rk(n, Snum, den) * Rk(n, Tnum, den)
    # cos(n u) = cos(r pi + alpha) = (-1)^r cos(pi a)
    cna = np.where(rr % 2 == 0, 1.0, -1.0) * np.cos(np.pi * float(a))
    return D - cna


def S_n(n, a, b):
    return np.abs(H_board(n, a, b)).sum() / (2 * n * (n + 1))


def lambda_phys(n, xi, zeta):
    """Actual Lebesgue function at z=(-cos(pi xi), -cos(pi zeta)) = (cos(pi(1-xi)), cos(pi(1-zeta))).
    lambda = sum_{j+k even} w_jk/4 |sum_{sig,eta} G_n(theta+sig a_j, phi+eta b_k)|."""
    xi, zeta = F(xi), F(zeta)
    m = n + 1
    th, ph = 1 - xi, 1 - zeta           # theta = pi*th, phi = pi*ph
    Q = lcm(th.denominator, ph.denominator)
    tQ, pQ = th.numerator * (Q // th.denominator), ph.numerator * (Q // ph.denominator)
    j = np.arange(n + 1, dtype=np.int64)[:, None]
    k = np.arange(m + 1, dtype=np.int64)[None, :]
    mask = ((j + k) % 2 == 0)
    jj = np.broadcast_to(j, mask.shape)[mask]
    kk = np.broadcast_to(k, mask.shape)[mask]
    e = np.where((jj == 0) | (jj == n), 0.5, 1.0)
    f = np.where((kk == 0) | (kk == m), 0.5, 1.0)
    w = 2 * e * f / (n * m)
    den = 2 * n * m * Q
    tot = np.zeros(jj.shape)
    for sg in (1, -1):
        for et in (1, -1):
            # u = pi (th + sg j/n) = pi (tQ n m + sg j Q m)/(n m Q) ; v = pi (pQ n m + et k Q n)/(nmQ)
            U = (tQ * n * m + sg * jj * Q * m)
            V = (pQ * n * m + et * kk * Q * n)
            Snum, Tnum = U + V, V - U
            D = Rk(n + 1, Snum, den) * Rk(n + 1, Tnum, den) + Rk(n, Snum, den) * Rk(n, Tnum, den)
            # cos(n u) = cos(pi (n th + sg j)) = (-1)^j cos(pi n th)
            cnu = np.where(jj % 2 == 0, 1.0, -1.0) * sinpi_red(np.array([2 * tQ * n + Q]), 2 * Q)[0]  # cos(pi n th)=sin(pi(n th+1/2))
            tot += D - cnu
    return float((w / 4 * np.abs(tot)).sum())


if __name__ == "__main__":
    import sys
    print(S_n(4, 0, 0), lambda_phys(4, 0, 0))
