#!/usr/bin/env python3
"""Audit03: re-verify every producer-named (p, omega) in the T8 r06 receipts.

Own primality test and order check; own monomial-basis evaluation and
elimination; determinant mod p via own fraction-free-free Gauss (row ops),
converted to the producer's product-Chebyshev basis by det C = prod 2^(a_j-1).
"""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import t8_exact_audit as ex

def det_mod_p(A, p):
    A = A.copy() % p; n = A.shape[0]; det = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i, c]), None)
        if piv is None: return 0
        if piv != c: A[[c, piv]] = A[[piv, c]]; det = -det
        det = det * int(A[c, c]) % p
        inv = pow(int(A[c, c]), p - 2, p)
        A[c] = A[c] * inv % p
        col = A[c+1:, c].copy()
        nz = np.nonzero(col)[0]
        if len(nz): A[c+1+nz] = (A[c+1+nz] - col[nz, None] * A[c][None, :] % p) % p
    return det % p

def mono_matrix(n, L, nodes, p, w):
    inv2 = (p + 1) // 2; E = ex.exponents(n)
    X = np.array([[(pow(w, v, p) + pow(w, (L - v) % L, p)) * inv2 % p for v in t] for t in nodes], dtype=np.int64)
    pw = [np.ones((len(nodes), n + 1), dtype=np.int64) for _ in range(3)]
    for j in range(3):
        for e in range(1, n + 1): pw[j][:, e] = pw[j][:, e-1] * X[:, j] % p
    return np.stack([pw[0][:, a] * pw[1][:, b] % p * pw[2][:, c] % p for a, b, c in E], axis=1)

def lc_prod(n, p):
    r = 1
    for al in ex.exponents(n):
        for a in al:
            if a > 1: r = r * pow(2, a - 1, p) % p
    return r

def rows_of(ev):
    out = []
    for name in ['controls', 'witnesses', 'phi2', 'phi3', 'strata', 'union2', 'union3', 'union4', 'near-orders']:
        d = json.loads((ev / f't8-r06-{name}.json').read_text())
        for row in d['rows']:
            items = [dict(row, **s) for s in row['survivors']] if 'survivors' in row else [row]
            for it in items:
                if 'certificate' not in it or not it['certificate'].get('checks'): continue
                if 'phase_nums' in it: ph, den = it['phase_nums'], it['phase_den']
                elif 'mask' in it: ph, den = it['mask'], it['phase_den']
                elif 'phase_over120' in it: ph, den = it['phase_over120'], 120
                else:  # audit M20 control
                    ph, den = [30, 75, 69], 120
                ph = ph if isinstance(ph[0], list) else [ph]
                n = it.get('n', 2 if it.get('control', '').startswith('PD-N') else 3)
                M = it.get('M', 10 if n == 2 else 20)
                z = it.get('z', [1, 2, 7])
                out.append((name, n, M, z, ph, den, it['certificate']))
    return out

def main():
    ev = Path(sys.argv[1]); res = []; bad = 0
    for name, n, M, z, ph, den, cert in rows_of(ev):
        L, nodes = ex.nodes_exact(M, z, ph, den)
        assert L == cert['L'] and len(nodes) == cert['nodes'], (name, n)
        qs = ex.prime_factors(L)
        for chk in cert['checks']:
            p, w = chk['p'], chk['omega']
            ok_p = ex.is_prime(p) and (p - 1) % L == 0
            ok_w = pow(w, L, p) == 1 and all(pow(w, L // q, p) != 1 for q in qs)
            V = mono_matrix(n, L, nodes, p, w)
            rk = ex.rank_mod_p(V, p)
            dm = None
            if V.shape[0] == V.shape[1]:
                dm = det_mod_p(V, p) * lc_prod(n, p) % p
                dm = dm if dm else None
            agree = ok_p and ok_w and rk == chk['rank'] and (chk['det'] is None and (dm is None or rk < len(nodes)) or chk['det'] == dm)
            bad += not agree
            res.append({'route': name, 'n': n, 'M': M, 'z': z, 'p': p, 'prime_ok': ok_p, 'order_L_ok': ok_w,
                        'rank_own': rk, 'rank_claimed': chk['rank'], 'det_cheb_own': dm, 'det_claimed': chk['det'], 'agree': agree})
    Path(sys.argv[2]).write_text(json.dumps({'checks': len(res), 'disagreements': bad, 'rows': res}))
    print(json.dumps({'checks': len(res), 'disagreements': bad}))
    for r in res:
        if not r['agree']: print('DISAGREE', r)

if __name__ == '__main__': main()
