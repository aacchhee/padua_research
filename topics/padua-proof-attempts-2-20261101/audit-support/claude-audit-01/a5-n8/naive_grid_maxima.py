#!/usr/bin/env python3
"""Diagnostic (not proof): number of NAIVE discrete local maxima of lambda_n on
uniform x-y grids of the closed square (a grid point counts if no in-square
8-neighbour is strictly larger), for several grid sizes.  Shows how a plain
grid census depends on resolution when maxima come in crease-separated twins.
claude-audit-01; imports only census_padua_maxima.py from this directory."""
import json, sys
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from census_padua_maxima import cardinal_cheb


def lam_grid(C, xs):
    n = C.shape[1] - 1
    A = np.arange(n + 1)
    T = np.cos(np.outer(A, np.arccos(np.clip(xs, -1, 1))))
    lam = np.zeros((len(xs), len(xs)))
    for i in range(C.shape[0]):
        lam += np.abs(T.T @ C[i] @ T)
    return lam


def naive_count(lam):
    P = np.pad(lam, 1, mode='constant', constant_values=-np.inf)
    M1, M2 = lam.shape
    ok = np.ones_like(lam, dtype=bool)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di or dj:
                ok &= ~(P[1 + di:1 + di + M1, 1 + dj:1 + dj + M2] > lam)
    pts = np.argwhere(ok)
    inner = sum(1 for a, b in pts if 0 < a < M1 - 1 and 0 < b < M2 - 1)
    return int(len(pts)), int(inner)


out = {}
for n in (3, 4, 5, 6, 7, 8):
    _, C = cardinal_cheb(n)
    row = {}
    for G in (51, 101, 201, 401, 801, 1601, 3201):
        xs = np.linspace(-1, 1, G)
        tot, inner = naive_count(lam_grid(C, xs))
        row[G] = {'total': tot, 'inner': inner}
    out[n] = row
    print(n, json.dumps(row), flush=True)
json.dump(out, open(sys.argv[1], 'w'), indent=1)
