#!/usr/bin/env python3
"""Floating sanity checks (NOT proof): normalization of the readout and
position of the exact bounds relative to numerical spectra."""
import sys, json, pickle
from fractions import Fraction as F
import numpy as np
sys.set_int_max_str_digits(0)
bj = pickle.load(open(sys.argv[1], 'rb')); alt = pickle.load(open(sys.argv[2], 'rb'))
cert = json.load(open(sys.argv[3]))
def fl(n, d): return float(F(n, d))
out = {}
d = np.array([fl(*x) for x in bj['d']])
Bm = np.array([[fl(x, den) for x in num] for num, den in bj['b']]).T   # 625x91
Vm = np.array([[fl(x, den) for x in num] for num, den in bj['V']]).T
Bo = Bm / np.sqrt(d); W = Vm / np.sqrt(d)
out['orthonormality_err'] = float(np.abs(Bo.T @ Bo - np.eye(91)).max())
Phi = W - Bo @ (Bo.T @ W)                       # R V D^{-1/2}
sig = np.linalg.svd(Phi, compute_uv=False)
out['bj_sigma_max_sq'] = float(sig[0] ** 2)
t = np.array(cert['lower_monic_coefficients'], dtype=float)
a = np.sqrt(d) * t; a /= np.linalg.norm(a)      # unit output direction
out['Phi_a_norm_sq'] = float(np.linalg.norm(Phi @ a) ** 2)
out['L'] = cert['lower_integer_floor_L']
out['L_le_sigma_max_sq'] = out['L'] <= out['bj_sigma_max_sq'] * (1 + 1e-9)
# wrong normalisation (sum t_k^2 instead of sum d_k t_k^2) for contrast
y = Vm @ t; ry = y - Bm @ ((Bm.T @ y) / d)
out['wrong_norm_quotient'] = float(ry @ ry / (t @ t))
out['col90_sq'] = float(np.linalg.norm(Phi[:, 90]) ** 2)
# alt envelope spectrum
da = np.array([fl(*x) for x in alt['d']])[1:]
S = np.array([[fl(x, den) for x in num] for num, den in alt['S']])  # 90x625
A = S / np.sqrt(da)[:, None]
out['alt_envelope_lambda_max_float'] = float(np.linalg.svd(A, compute_uv=False)[0] ** 2)
out['alt_trace_float'] = float((A * A).sum())
out['B'] = cert['upper_integer_B']
print(json.dumps(out, indent=1))
