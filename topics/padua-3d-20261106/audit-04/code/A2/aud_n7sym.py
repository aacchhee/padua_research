import sys, math
sys.path.insert(0, sys.argv[1])
from aud_common import fold_nodes, split_prime, modrank_det, total_modes
n = 7; N = 120; M = 240; L = 480
La, A = fold_nodes((1, 17, 212), (1, 17, 212), L, M)
Lb, B = fold_nodes((1, 17, 28), (1, 17, 28), L, M)
refl = sorted((x, y, L // 2 - w) for x, y, w in A)   # cos(2pi(L/2-w)/L) = -cos(2pi w/L)
print('x3-reflection of (1,17,212) == nodes of (1,17,28):', refl == B, len(A), len(B))
p, w = split_prime(L, 2_000_000_000)
def det(nodes):
    i2 = pow(2, -1, p)
    X = [[(pow(w, v, p) + pow(w, (-v) % L, p)) * i2 % p for v in r] for r in nodes]
    Am = [[math.prod(pow(x, e, p) for x, e in zip(row, al)) % p for al in total_modes(n)] for row in X]
    return modrank_det(Am, p)
ra, da = det(A); rb, db = det(B)
print('p', p, 'ranks', ra, rb, 'det_a', da, 'det_b', db, 'equal up to sign:', da in (db, (-db) % p))
