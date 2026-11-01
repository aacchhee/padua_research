"""Clustered checkerboard (m = 30, e = 0): HL (exact window, MGS2) and block-window CGS2 losses, and joint/single Ritz
predictions u/rho (u = 2^-53) on the exact span; PD-T?...-112 (a) remaining claims. Own code only.
Usage: python3 -I -u rv2_checkerboard_ritz.py > logs_L1b/checkerboard_ritz.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L1'))
import numpy as np
import rv_core as C
from rv2_checkerboard import checkerboard
U = 2.0 ** -53
P, w, _, _ = checkerboard('cubic', 30)
x, y, w = P[:, 0].astype(float), P[:, 1].astype(float), w.astype(float)
nmax = 24; degs = (12, 16, 20, 24)
for lab, kw in (('BJ block CGS', dict(choice='dev', win='block', orth='cgs')), ('HL exact MGS2', dict(choice='dev', win='exact', orth='mgs2')),
                ('block CGS2', dict(choice='dev', win='block', orth='cgs2'))):
    Q, _ = C.window_rec(x, y, w, nmax, **kw); L = C.loss_profile(Q, nmax)
    print(f'{lab:14s} loss n=12,16,20,24: ' + ' '.join(f'{L[n]:.1e}' for n in degs))
Qf, _ = C.window_rec(x, y, w, nmax, 'dev', 'full', 'cgs2')
for n in degs:
    Un = Qf[:, :C.N_of(n)]
    r = (C.min_ritz(Un, x), C.min_ritz(Un, y), C.min_ritz(Un, x + 1j * y, hermitian=False))
    print(f'n={n}: u/rho_X={U/r[0]:.1e} u/rho_Y={U/r[1]:.1e} u/rho_Z={U/r[2]:.1e}')
