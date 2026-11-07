#!/usr/bin/env python3
"""Repository-only independent exact cosine rank; no raw-linkage access."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time
import numpy as np
import check_certificate as own


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--payload', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    start, utc = time.process_time(), datetime.now(timezone.utc).isoformat()
    r = json.loads(a.payload.read_bytes())
    n, ids, orders = r['n'], r['ids'], r['orders']
    assert r['schema'] == 'pdpr-canonical-parity-v1'
    assert r['exact_geometry'] == 'x_j=cos(pi*i_j/m_j), indices=canonical_parity_grid[ids]'
    assert r['id_order'] == 'itertools.product(range(m_j+1)); i3 fastest; retain equal index parities'
    assert type(n) is int and n >= 1 and orders == [n, n+1, n+1]
    assert all(type(x) is int for x in orders+ids)
    grid = []
    for ordinal in range(math.prod(m+1 for m in orders)):
        i, rest = divmod(ordinal, (orders[1]+1)*(orders[2]+1))
        j, k = divmod(rest, orders[2]+1)
        if (i-j) % 2 == 0 and (j-k) % 2 == 0:
            grid.append((i, j, k))
    assert len(grid) == math.prod(m//2+1 for m in orders)+math.prod((m+1)//2 for m in orders)
    assert ids == sorted(set(ids)) and ids and 0 <= ids[0] <= ids[-1] < len(grid)
    M, N = len(ids), math.comb(n+3, 3)
    assert type(r['M']) is int and type(r['N']) is int and (M, N) == (r['M'], r['N']) and M >= N
    geometry = [grid[i] for i in ids]
    assert len(set(geometry)) == M
    L = math.lcm(*(2*m for m in orders))
    factors = own.prime_divisors(L)
    exponents = [(i, j, k) for i in range(n+1) for j in range(n+1-i) for k in range(n+1-i-j)]
    assert len(set(exponents)) == len(exponents) == N
    attempts = []
    for coefficient in range(1, 257):
        p = coefficient*L+1
        if p == r['certificate']['p'] or not own.is_prime(p):
            continue
        assert p < 2**30 and (p-1)**2+(p-1) < np.iinfo(np.int64).max
        rho = next(t for t in range(2, p) if pow(t, L, p) == 1 and all(pow(t, L//q, p) != 1 for q in factors))
        x = []
        for triplet in geometry:
            point = []
            for axis in range(3):
                exponent, rem = divmod(L*triplet[axis], 2*orders[axis])
                assert rem == 0
                point.append((pow(rho, exponent, p)+pow(rho, -exponent, p))*pow(2, -1, p) % p)
            x.append(point)
        x = np.array(x, dtype=np.int64)
        powers = [np.array([[pow(int(t), j, p) for j in range(n+1)] for t in x[:, axis]], dtype=np.int64) for axis in range(3)]
        V = np.column_stack([((powers[0][:, i]*powers[1][:, j]) % p)*powers[2][:, k] % p for i, j, k in exponents])
        rank, chosen, _ = own.eliminate(V, p, ids)
        attempts.append({'p': p, 'rho': rho, 'rank': rank})
        if rank == N:
            square = V[[ids.index(i) for i in chosen]]
            rank, _, determinant = own.eliminate(square, p, chosen)
            assert rank == N and 0 < determinant < p
            break
    else:
        raise AssertionError('bounded prime attempts inconclusive: '+str(attempts))
    out = {'verdict': 'PASS', 'command': sys.argv, 'started_utc': utc,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-start,
        'python': platform.python_version(), 'numpy': np.__version__, 'payload': own.identity(a.payload),
        'checker': own.identity(__file__), 'independent_arithmetic_helper': own.identity(own.__file__),
        'n': n, 'M': M, 'N': N, 'full_grid_count': len(grid), 'L': L, 'rank': rank,
        'p': p, 'rho': rho, 'rho_power_L': pow(rho, L, p),
        'order_tests': [[q, pow(rho, L//q, p)] for q in factors],
        'prime_proof': 'Complete integer trial division2..isqrt(p)', 'different_from_producer_prime': True,
        'basis': 'Complete monomials, lexical(i,j,k), i+j+k<=n',
        'minor_row_ids': chosen, 'determinant_mod_p': determinant, 'attempts': attempts,
        'arithmetic_bound': (p-1)**2+(p-1),
        'arithmetic': 'Exact int64 staged modular products/normalized-row elimination without dot accumulation; Python integer powers/determinant.',
        'dependency_scope': 'Only committed payload plus this independent checker/helper and Python/NumPy. No producer import, receipt, Git or raw path is read.',
        'conclusion': 'Ideal exact-cosine full column rank N, a Pi_n-determining set; positive-weight LS uniquely defined. M>N is not square interpolation.',
        'linkage_scope': 'No measurement linkage is rechecked here. The separate full certificate review receipt records prior raw linkage; exact algebra replay requires none of those temporary files.',
        'limits': 'No rounded-node rank, condition, norm, error/noise or universal-degree certificate; formal Claude audit pending.',
        'research_rounds': 0}
    encoded = json.dumps(out, indent=2)+'\n'
    assert len(encoded.encode()) < 16384
    a.output.write_text(encoded)
    print(json.dumps({k: out[k] for k in ('verdict', 'n', 'M', 'N', 'p', 'rho', 'determinant_mod_p', 'actual_cpu')}))


if __name__ == '__main__':
    main()
