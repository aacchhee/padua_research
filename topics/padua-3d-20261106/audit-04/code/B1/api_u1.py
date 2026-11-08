#!/usr/bin/env python3
"""Auditor audit04-B1 API probes of the public parity_nodes/parity_fit/basis API.

Imports the producer module from the isolated extracted copy (argv[1] = code dir)
and checks it against an own cosine-basis oracle.
"""
import itertools as it, json, math, sys
import numpy as np
sys.path.insert(0, sys.argv[1])
import u1_usable as u

def exps(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]
def own_basis(x, n):
    th = np.arccos(np.clip(x, -1, 1)); E = np.array(exps(n)); out = np.ones((len(x), len(E)))
    for j in range(3):
        out *= np.cos(np.outer(th[:, j], np.arange(n+1)))[:, E[:, j]]
    return out*2.0**((E > 0).sum(1)/2)

rng = np.random.default_rng(20261108)
rep = {'cases': [], 'rejections': 0, 'unexpected_accepts': [], 'other': {}}
q = rng.uniform(-1, 1, (50, 3))
for n in (1, 2, 4, 5, 9, 16):
    for equal in (False, True):
        x, w, rec = u.parity_nodes(n, equal)
        M, N = len(x), math.comb(n+3, 3)
        # recipe metadata consistency with own rule
        m = rec['orders']; ids = np.array(rec['indices'])
        ok_meta = (m == ([n+1]*3 if equal else [n, n+1, n+1]) and len(ids) == M and
                   np.allclose(x, np.cos(np.pi*ids/np.array(m)), rtol=0, atol=0) and
                   np.array_equal(rec['multiplicities'], np.where((ids == 0) | (ids == np.array(m)), 1, 2).prod(1)) and
                   abs(w.sum()-1) < 1e-15 and w.min() > 0)
        Bq = u.basis(q, n); Bo = own_basis(q, n)
        cmax = rng.standard_normal((N, 4))
        Y = own_basis(x, n) @ cmax
        err = {}
        for lab, val, shape, exp in (('vector', Y[:, 0], (N,), cmax[:, 0]),
                                     ('list', Y[:, 0].tolist(), (N,), cmax[:, 0]),
                                     ('Mx1', Y[:, :1], (N, 1), cmax[:, :1]),
                                     ('Mx4', Y, (N, 4), cmax),
                                     ('complex', Y[:, 1]*(2-1j), (N,), cmax[:, 1]*(2-1j)),
                                     ('fortran', np.asfortranarray(Y), (N, 4), cmax)):
            c = u.parity_fit(n, val, equal)
            assert c.shape == shape, (lab, c.shape)
            err[lab] = float(np.max(np.abs(c-exp)))
        # multiple RHS equals columnwise single RHS
        cm = u.parity_fit(n, Y, equal)
        col = max(float(np.max(np.abs(cm[:, k]-u.parity_fit(n, Y[:, k], equal)))) for k in range(4))
        for lab, bad in (('scalar', 1.0), ('0d', np.array(3.0)), ('len1', [1.0]), ('short', np.ones(M-1)),
                         ('long', np.ones(M+1)), ('rowvec', np.ones((1, M))), ('transposed', np.ones((3, M))),
                         ('short2', np.ones((M-1, 2))), ('rank3', np.ones((M, 2, 1))), ('rank4', np.ones((M, 1, 1, 1)))):
            if M == 1 and lab == 'len1':
                continue
            try:
                u.parity_fit(n, bad, equal)
            except ValueError:
                rep['rejections'] += 1
            else:
                rep['unexpected_accepts'].append((n, equal, lab))
        rep['cases'].append({'n': n, 'equal': equal, 'M': M, 'N': N, 'meta_ok': bool(ok_meta),
                             'basis_vs_own': float(np.max(np.abs(Bq-Bo))), 'coef_err': err, 'multi_vs_single': col})
# invalid degree observations (NOTE scope)
for bad_n in (0, -1, 1.5, True):
    try:
        out = u.parity_nodes(bad_n)
        rep['other'][str(bad_n)] = f'accepted: M={len(out[0])}'
    except Exception as e:
        rep['other'][str(bad_n)] = type(e).__name__
json.dump(rep, open(sys.argv[2], 'w'), indent=1)
print(json.dumps({'rejections': rep['rejections'], 'unexpected_accepts': rep['unexpected_accepts'],
                  'max_coef_err': max(max(c['coef_err'].values()) for c in rep['cases']),
                  'max_basis_diff': max(c['basis_vs_own'] for c in rep['cases']),
                  'meta_ok': all(c['meta_ok'] for c in rep['cases']),
                  'max_multi_vs_single': max(c['multi_vs_single'] for c in rep['cases']), 'invalid_degree': rep['other']}))
