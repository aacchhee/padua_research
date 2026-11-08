"""Auditor's exact check of the cubic z=(1,4,11) triangular DCT claims."""
import sys, json, math
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from alib import modes, frac_inverse
from aud_s import alias_matrix

n = 3; N = 20; z = (1, 4, 11)
C = alias_matrix(n, z)
A = [[F(x, 8) for x in row] for row in C]
mo = modes(n)
name = {(0,0,0):'1',(1,0,0):'x',(0,1,0):'y',(0,0,1):'z',(2,0,0):'T2x',(0,2,0):'T2y',(0,0,2):'T2z',
        (3,0,0):'T3x',(0,3,0):'T3y',(0,0,3):'T3z',(1,1,0):'xy',(1,0,1):'xz',(0,1,1):'yz',(2,1,0):'T2x.y',
        (1,2,0):'x.T2y',(2,0,1):'T2x.z',(0,2,1):'T2y.z',(1,0,2):'x.T2z',(0,1,2):'y.T2z',(1,1,1):'xyz'}
col = {name[m]: j for j, m in enumerate(mo)}
h = F(1, 2); q = F(1, 4)
# record's displayed identities: mode -> {freq: coeff}
table = {'1': {0: 1}, 'x': {1: 1}, 'y': {4: 1}, 'z': {11: 1}, 'T2x': {2: 1}, 'T2y': {8: 1}, 'T2z': {18: -1},
         'T3x': {3: 1}, 'T3y': {12: 1}, 'T3z': {7: -1},
         'xy': {3: h, 5: h}, 'xz': {10: h, 12: h}, 'yz': {7: h, 15: h}, 'T2x.y': {2: h, 6: h}, 'x.T2y': {7: h, 9: h},
         'T2x.z': {9: h, 13: h}, 'T2y.z': {3: h, 19: h}, 'x.T2z': {17: -h, 19: -h}, 'y.T2z': {18: h, 14: -h},
         'xyz': {6: q, 8: q, 14: q, 16: q}}
pivot = {'1': 0, 'x': 1, 'y': 4, 'z': 11, 'T2x': 2, 'T2y': 8, 'T2z': 18, 'T3x': 3, 'T3y': 12, 'T3z': 7,
         'xy': 5, 'xz': 10, 'yz': 15, 'T2x.y': 6, 'x.T2y': 9, 'T2x.z': 13, 'T2y.z': 19, 'x.T2z': 17, 'y.T2z': 14, 'xyz': 16}
order = list(table)  # displayed order
out = {}
# 1. each displayed identity equals the exact computed column
mism = []
for m, exp in table.items():
    j = col[m]; colv = {r: A[r][j] for r in range(N) if A[r][j]}
    if colv != {k: F(v) for k, v in exp.items()}:
        mism.append((m, colv, exp))
out['identity_mismatches'] = len(mism)
# also a pure-floating check of the identities at the 20 actual angles
th = [(2 * k + 1) * math.pi / 40 for k in range(N)]
err = 0
for m, exp in table.items():
    a = [k for k, v in name.items() if v == m][0]
    for t in th:
        lhs = math.prod(math.cos(e * g * t) for e, g in zip(a, z))
        rhs = sum(float(v) * math.cos(r * t) for r, v in exp.items())
        err = max(err, abs(lhs - rhs))
out['identity_float_err'] = err
# 2. pivot structure: each column's nonpivot freqs are earlier pivots; pivots distinct and cover 0..19
seen = set(); tri_ok = True; diag = []
for m in order:
    fr = set(table[m]); p = pivot[m]
    if p in seen or not (fr - {p}) <= seen:
        tri_ok = False
    seen.add(p); diag.append(abs(F(table[m][p])))
out['triangular_order_ok'] = tri_ok and seen == set(range(N))
out['diag_hist'] = {str(k): diag.count(k) for k in set(diag)}
det = math.prod(diag); out['abs_det_A'] = str(det)
# 3. exact inverse and row sums in inherited mode order
inv = frac_inverse(A)
I = [[sum(A[i][k] * inv[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
out['inverse_ok'] = all(I[i][j] == (1 if i == j else 0) for i in range(N) for j in range(N))
rows = [sum(abs(x) for x in inv[i]) for i in range(N)]
out['row_l1'] = [str(x) for x in rows]
out['S'] = str(sum(rows)); out['inf'] = str(max(rows))
out['col0'] = [str(inv[i][0]) for i in range(N)]
w = [1] + [2] * (N - 1)
out['bound'] = str(sum(abs(inv[i][r]) * w[r] for i in range(N) for r in range(N)))
# 4. DCT orthogonality exact-ish: B^T B diag; and sum_k |Binv[r,k]| <= w_r
B = np.cos(np.outer((2 * np.arange(N) + 1) * np.pi / (2 * N), np.arange(N)))
G = B.T @ B
out['BtB_offdiag_max'] = float(np.max(np.abs(G - np.diag(np.diag(G)))))
out['BtB_diag'] = [round(float(x), 12) for x in np.diag(G)[:3]]
Binv = np.linalg.inv(B)
out['Binv_formula_err'] = float(np.max(np.abs(Binv - (np.array(w)[:, None] * B.T / N))))
out['Binv_rowabs_max_over_w'] = float(np.max(np.abs(Binv).sum(axis=1) / np.array(w)))
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
