#!/usr/bin/env python3
"""Three preregistered translated rules; Q(zeta_24) exact rank kills."""
import itertools as it
import json
import math
from pathlib import Path
import time

import numpy as np
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix

import t8_cyclic as core
from t2_screen import leb, controls

PHASE = (6, 4, 3)  # angles = 2*pi*PHASE/24


def generator(name, n):
    return {'PK': (1, n + 1, (n + 1)**2),
            'PT': (1, n + 1, (n + 1) * (n + 2) // 2),
            'PO': (1, 2*n + 1, 2*n*n + 2*n + 1)}[name]


def terms(n, M, z):
    result = []
    for a in core.modes(n):
        result.append([(sum(e*b*c for e, b, c in zip(s, a, z)) % M,
                        sum(e*b*c for e, b, c in zip(s, a, PHASE)) % 24)
                       for s in it.product((-1, 1), repeat=3)])
    return result


def phased_rank(n, M, z):
    ts = terms(n, M, z)
    N = len(ts)
    L = math.lcm(M, 24)
    p = L + 1
    while not sp.isprime(p):
        p += L
    rho = pow(int(sp.primitive_root(p)), (p - 1)//24, p)
    assert pow(rho, 24, p) == 1
    assert all(pow(rho, 24//q, p) != 1 for q in (2, 3))
    B = [[0]*N for _ in range(M)]
    for j, col in enumerate(ts):
        for r, h in col:
            B[r][j] = (B[r][j] + pow(rho, h, p)) % p
    mr = core.mod_rank(B, p)
    out = {'splitting_prime': p, 'zeta24_image': rho, 'modular_rank': mr}
    if mr == N:
        out['rank'] = N
        return out
    K = QQ.algebraic_field(sp.exp(sp.I*sp.pi/12))
    powers = [K.unit**h for h in range(24)]
    B = [[K.zero]*N for _ in range(M)]
    for j, col in enumerate(ts):
        for r, h in col:
            B[r][j] += powers[h]
    R, piv = DomainMatrix(B, (M, N), K).rref()
    out['rank'] = len(piv)
    if len(piv) == N:
        out['bad_prime_only'] = True
        return out
    R = R.to_list()
    free = next(j for j in range(N) if j not in piv)
    v = [K.zero]*N
    v[free] = K.one
    for i, j in enumerate(piv):
        v[j] = -R[i][free]
    assert any(v) and all(sum((x*y for x, y in zip(row, v)), K.zero) == K.zero for row in B)
    out['cyclotomic_null'] = [[list(a), [str(c) for c in q.to_list()]]
                              for a, q in zip(core.modes(n), v) if q]
    out['null_verified_Q_zeta24'] = True
    return out


def main():
    assert json.loads((core.TOP/'evidence/t8-controls.json').read_text())['verdict'] == 'PASS'
    start = time.time()
    out = core.metadata('OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_phases.py')
    out.update({'source_sha256': core.sha(__file__),
                'core_sha256': core.sha(core.__file__), 'phase_numerators_over24': PHASE,
                'field_polynomial': 't^8-t^4+1', 'families': []})
    mesh = np.array(list(it.product(leb.lobatto(21), repeat=3)))
    cache = {}
    for name in ['PK', 'PT', 'PO']:
        rows = []
        losses = 0
        kill = None
        for n in range(2, 13):
            N = math.comb(n+3, 3)
            M = N
            z = tuple(v % M for v in generator(name, n))
            L, pts = core.nodes(M, z, PHASE)
            row = {'n': n, 'N': N, 'M': M, 'z': z, 'nodes': len(pts)}
            if len(pts) != N:
                kill = 'exact_cardinality_mismatch'
                rows.append(row)
                break
            rc = phased_rank(n, M, z)
            row['certificate'] = rc
            if rc['rank'] != N:
                kill = 'certified_cyclotomic_deficiency'
                rows.append(row)
                break
            if n not in cache:
                E = leb.basis(mesh, n)
                cache[n] = (E, controls(n, mesh, E))
            E, base = cache[n]
            physical = np.cos(2*np.pi*np.array(pts)/L)
            row['baselines'] = base
            row['quality'] = leb.diagnose(physical, n, mesh, E)
            value = row['quality']['sampled_lebesgue']
            if n >= 6 and value is not None and value > base['Leja']:
                losses += 1
            else:
                losses = 0
            rows.append(row)
            if losses == 2:
                kill = 'two_consecutive_Leja_losses'
                break
        out['families'].append({'name': name, 'rows': rows, 'kill': kill,
                                'D2_promising': False, 'fit': 'INCONCLUSIVE'})
        print(json.dumps({'family': name, 'n_last': rows[-1]['n'], 'kill': kill}), flush=True)
    out['seconds'] = round(time.time()-start, 3)
    core.write_receipt('t8-phases.json', out)


if __name__ == '__main__':
    main()
