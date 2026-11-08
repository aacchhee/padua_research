"""Replay n2..7 extract-QR selection hashes (developer helpers) and an
independent monomial rank over F_p at auditor-chosen primes p = 1 mod q."""
import sys, json, math, hashlib
sys.path.insert(0, sys.argv[1])  # code dir of the isolated run copy
import numpy as np, scipy.linalg as la, sympy
import t10_lattices as t
raw = json.load(open(sys.argv[2])); old = json.load(open(sys.argv[3]))
def rank_mod_p(M, p):
    M = [row[:] for row in M]; r = 0; cols = len(M[0])
    for c in range(cols):
        piv = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                fac = M[i][c]; M[i] = [(x - fac * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r
out = []
for n in range(2, 8):
    N = math.comb(n + 3, 3)
    best = min((r for r in raw['rows'] if r['n'] == n and r['rank'] == N), key=lambda r: (r['fold'], r['det'], r['family']))
    q, keys, weights, points = t.folded(np.array(best['B']))
    ids = la.qr(t.basis(points, n).T, pivoting=True, mode='economic', check_finite=False)[2][:N]
    sel = [keys[int(i)] for i in ids]
    h = hashlib.sha256(json.dumps({'denominator': q, 'selected_folded_keys': sel}, separators=(',', ':')).encode()).hexdigest()
    prior = next(r for r in old['rows'] if r[0] == n)
    # auditor prime: smallest prime p = 1 mod q above 10**6 (different from 73..5881 used before)
    k = 10**6 // q + 1
    while not sympy.isprime(k * q + 1): k += 1
    p = k * q + 1
    g = sympy.primitive_root(p); w = pow(g, (p - 1) // q, p); i2 = pow(2, p - 2, p)
    xs = [[(pow(w, kk, p) + pow(w, (q - kk) % q, p)) * i2 % p for kk in key] for key in sel]
    alphas = [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)]
    M = [[pow(x[0], a, p) * pow(x[1], b, p) * pow(x[2], c, p) % p for (a, b, c) in alphas] for x in xs]
    out.append({'n': n, 'q': q, 'hash_matches_subset_rank': h == prior[-1], 'p': p, 'rank': rank_mod_p(M, p), 'N': N, 'distinct_nodes': len(set(map(tuple, sel)))})
print(json.dumps(out))
