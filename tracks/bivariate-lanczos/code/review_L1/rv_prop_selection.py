"""Exact-coefficient propagator norm for different one-relation selections (dev / mirror / alt / adapt):
u * median_i and u * max_i ||L*(z_i)^{-1}||_2 at n = 8, 12, 16, 20 (exact coefficients from a long-double full-CGS2
run with the same selection), and the BJ (block window, CGS, double) loss with that selection.
Usage: python3 -I -u rv_prop_selection.py > logs_L1/prop_selection.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rv_core as C
from rv_prop import exact_coeffs, build_L, U

print(f'# rv_prop_selection.py numpy {np.__version__}')
degs = (8, 12, 16, 20)
for name in ('square_rotpi4', 'square_rot0.3', 'triangle', 'disk'):
    P, w = C.node_set(name); x, y = P[:, 0], P[:, 1]
    for ch in ('dev', 'mirror', 'alt', 'adapt'):
        rows, idx = exact_coeffs(x, y, w, 20, choice=ch)
        N = C.N_of(20)
        nr = np.zeros((len(x), len(degs)))
        for i in range(len(x)):
            Inv = np.linalg.inv(build_L(rows, N, (x[i], y[i])))
            for c, n in enumerate(degs):
                Nn = C.N_of(n); nr[i, c] = np.linalg.norm(Inv[:Nn, :Nn], 2)
        Q, _ = C.window_rec(x, y, w, 20, ch, 'block', 'cgs'); L = C.loss_profile(Q, 20)
        print(f'   {name:14s} {ch:6s} loss: ' + ' '.join(f'{L[n]:.1e}' for n in degs)
              + ' | u*med: ' + ' '.join(f'{U*np.median(nr[:, c]):.1e}' for c in range(len(degs)))
              + ' | u*max: ' + ' '.join(f'{U*np.max(nr[:, c]):.1e}' for c in range(len(degs))))
        sys.stdout.flush()
