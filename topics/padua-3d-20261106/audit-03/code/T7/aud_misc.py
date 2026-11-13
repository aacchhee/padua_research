#!/usr/bin/env python3
"""Auditor (Claude): torsion trace table, T7-06 Lambda on own meshes, node sets."""
import itertools as it, json, math, sys
import numpy as np
from numpy.polynomial import chebyshev as C

def trace_table():
    rows = {}
    for n in range(1, 11):
        modes = [a for a in it.product(range(n+1), repeat=3) if sum(a) <= n]
        N = len(modes)
        rows[n] = [N] + [sum((-1)**sum(a[:k]) for a in modes) for k in (1, 2, 3)]
    return rows

def basis(x, n):
    modes = [a for a in it.product(range(n+1), repeat=3) if sum(a) <= n]
    th = np.arccos(np.clip(x, -1, 1))
    return np.stack([np.prod([np.cos(a[j]*th[:, j]) * (np.sqrt(2) if a[j] else 1) for j in range(3)], axis=0) for a in modes], axis=1)

def lam(X, n, mesh):
    V = basis(X, n); Vi = np.linalg.inv(V)
    best = 0.
    for k in range(0, len(mesh), 4096):
        best = max(best, np.abs(basis(mesh[k:k+4096], n) @ Vi).sum(axis=1).max())
    return best, np.linalg.cond(V)

def t706():
    g = np.array([7, 7, 4])/10; h = np.array([5, 0, 5])/10; a = np.array([1, 2, 4])/101
    T = np.array([(k*g + l*h + a) % 1 for k in range(10) for l in range(2)])
    X = np.cos(2*np.pi*T)
    assert len(np.unique(np.round(X, 12), axis=0)) == 20
    out = {}
    for q, kind in ((21, 'lobatto'), (41, 'lobatto'), (61, 'lobatto'), (40, 'uniform-x')):
        if kind == 'lobatto': g1 = np.cos(np.linspace(0, np.pi, q))
        else: g1 = np.linspace(-1, 1, q)
        mesh = np.array(list(it.product(g1, repeat=3)))
        out[f'{kind}{q}'] = lam(X, 3, mesh)[0]
    rng = np.random.default_rng(1); mesh = rng.uniform(-1, 1, (200000, 3))
    out['random2e5'] = lam(X, 3, mesh)[0]
    out['cond2'] = lam(X, 3, mesh[:10])[1]
    return out

if __name__ == '__main__':
    print(json.dumps({'trace_table_n:[N,k1,k2,k3]': trace_table(), 'T7-06': t706()}, indent=1))
