#!/usr/bin/env python3
"""Exact check: the Betke-Henk/Minkowski lattice L = B Z^3, B = (1/3)[[2,-1,-3],[3,-2,1],[1,3,-2]]
(columns are the basis vectors), has det 38/27 and no nonzero vector with |x|_1 < 2.

Reduction: if x = B c with |x|_1 < 2 then |x|_inf < 2, and c = B^{-1} x gives
|c_i| <= ||row_i(B^{-1})||_1 * |x|_inf < 2 * max_i ||row_i(B^{-1})||_1 =: C.
So it suffices to enumerate integer c with |c_i| <= floor(C) (exact Fractions).
"""
import hashlib, itertools, json, sys
from fractions import Fraction as F
from pathlib import Path

B = [[F(2, 3), F(-1, 3), F(-1, 1)], [F(1, 1), F(-2, 3), F(1, 3)], [F(1, 3), F(1, 1), F(-2, 3)]]

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def inv3(m):
    d = det3(m)
    cof = [[(m[(i+1)%3][(j+1)%3]*m[(i+2)%3][(j+2)%3] - m[(i+1)%3][(j+2)%3]*m[(i+2)%3][(j+1)%3]) for j in range(3)] for i in range(3)]
    return [[cof[j][i]/d for j in range(3)] for i in range(3)]

d = det3(B)
Bi = inv3(B)
C = 2*max(sum(abs(v) for v in row) for row in Bi)
R = int(C)  # floor, C positive
best = None
count_min = 0
for c in itertools.product(range(-R, R+1), repeat=3):
    if c == (0, 0, 0):
        continue
    x = [sum(B[i][j]*c[j] for j in range(3)) for i in range(3)]
    l1 = sum(abs(t) for t in x)
    if best is None or l1 < best:
        best, count_min = l1, 0
    if l1 == best:
        count_min += 1
out = dict(schema='cap-critical-lattice-v1', code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           command=' '.join(sys.argv), basis_columns=[[str(B[i][j]) for i in range(3)] for j in range(3)],
           det=str(d), abs_det=str(abs(d)), enumeration_radius=R, coefficient_bound=str(C),
           min_nonzero_l1=str(best), number_of_minimal_vectors=count_min,
           verdict='PASS' if (abs(d) == F(38, 27) and best == 2) else 'FAIL',
           density_of_O_packing=str(F(4, 3)/abs(d)), delsarte_cap_over_volume=str(abs(d)/F(4, 3)))
print(json.dumps(out, indent=1))
if len(sys.argv) > 1:
    Path(sys.argv[1]).write_text(json.dumps(out, indent=1)+'\n')
