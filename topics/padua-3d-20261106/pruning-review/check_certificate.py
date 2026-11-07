#!/usr/bin/env python3
"""Independent canonical decoder and different-prime monomial minor proof."""
import argparse
from datetime import datetime, timezone
import hashlib
import copy
import importlib.util
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
import numpy as np


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def pinned(record):
    assert identity(record['path']) == record, record['path']


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))


def prime_divisors(n):
    return [d for d in range(2, n+1) if n % d == 0 and is_prime(d)]


def eliminate(matrix, modulus, ids):
    """Largest-residue row pivot; normalize first; no floating arithmetic."""
    a, labels, chosen, determinant, swaps = matrix.copy(), list(ids), [], 1, 0
    for j in range(a.shape[1]):
        k = j+int(np.argmax(a[j:, j]))
        if a[k, j] == 0:
            return j, chosen, 0
        if j != k:
            a[[j, k]] = a[[k, j]]
            labels[j], labels[k] = labels[k], labels[j]
            swaps += 1
        chosen.append(labels[j])
        value = int(a[j, j])
        determinant = determinant*value % modulus
        a[j, j:] = a[j, j:]*pow(value, -1, modulus) % modulus
        multiplier = a[j+1:, j].copy()
        a[j+1:, j:] = (a[j+1:, j:] - multiplier[:, None]*a[j, j:][None, :]) % modulus
    return a.shape[1], chosen, determinant*(-1 if swaps % 2 else 1) % modulus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--payload', type=Path, required=True)
    parser.add_argument('--producer-check', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    began, utc = time.process_time(), datetime.now(timezone.utc).isoformat()
    payload = json.loads(args.payload.read_bytes())
    producer = json.loads(args.producer_check.read_bytes())
    assert identity(args.payload) == producer['payload']
    n, orders, ids = payload['n'], payload['orders'], payload['ids']
    assert payload['schema'] == 'pdpr-canonical-parity-v1'
    assert type(n) is int and n >= 1 and orders == [n, n+1, n+1]
    assert all(type(i) is int for i in orders+ids)
    # Enumerate by a single mixed-radix ordinal, not producer product/filter.
    complete = []
    for ordinal in range(math.prod(m+1 for m in orders)):
        first, remainder = divmod(ordinal, (orders[1]+1)*(orders[2]+1))
        second, third = divmod(remainder, orders[2]+1)
        if (first-second) % 2 == 0 and (second-third) % 2 == 0:
            complete.append((first, second, third))
    assert len(complete) == math.prod(m//2+1 for m in orders)+math.prod((m+1)//2 for m in orders)
    assert ids == sorted(set(ids)) and 0 <= ids[0] <= ids[-1] < len(complete)
    N, M = math.comb(n+3, 3), len(ids)
    assert payload['N'] == N and payload['M'] == M and M >= N
    coordinates = np.array([complete[i] for i in ids], dtype=np.int64)
    assert len(set(map(tuple, coordinates))) == M
    physical = np.cos(np.pi*coordinates/np.array(orders))
    byte_hash = hashlib.sha256(np.asarray(physical, dtype='<f8').tobytes()).hexdigest()
    assert byte_hash == payload['binary64_link']['sha256']
    provenance = payload['provenance']
    for key in ('receipt', 'raw_details', 'raw_inventory', 'checkpoint', 'path', 'recipe', 'assessment_map'):
        pinned(provenance[key])
    with np.load(provenance['checkpoint']['path']) as stored:
        assert np.array_equal(stored['ids'], ids) and stored['nodes'].tobytes() == physical.tobytes()
    with np.load(provenance['path']['path']) as path:
        assert np.array_equal(path[f'm{M}'], ids)
    with np.load(provenance['assessment_map']['path']) as assessed:
        assert assessed['nodes'].tobytes() == physical.tobytes()
    details = json.loads(Path(provenance['raw_details']['path']).read_bytes())
    selected = next(p for p in details['paths'] if p['n'] == n and p['rule'] == 'A')
    assert selected['primary_M'] == M == math.ceil(1.20*N)
    L = math.lcm(*(2*m for m in orders))
    assert L == payload['certificate']['L']
    prime_factors = prime_divisors(L)
    tested = []
    for multiplier in range(1, 257):
        p = L*multiplier+1
        if p == payload['certificate']['p'] or not is_prime(p):
            continue
        rho = next(r for r in range(2, p) if pow(r, L, p) == 1 and all(pow(r, L//q, p) != 1 for q in prime_factors))
        assert p < 2**30 and (p-1)**2+(p-1) < np.iinfo(np.int64).max
        x = np.empty((M, 3), dtype=np.int64)
        for j in range(M):
            for axis in range(3):
                exponent, rem = divmod(L*int(coordinates[j, axis]), 2*orders[axis])
                assert rem == 0
                x[j, axis] = (pow(rho, exponent, p)+pow(rho, -exponent, p))*pow(2, -1, p) % p
        # Lexicographic complete monomials, distinct from graded Chebyshev order.
        exponents = [(a, b, c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
        assert len(exponents) == len(set(exponents)) == N
        powers = [np.array([[pow(int(t), k, p) for k in range(n+1)] for t in x[:, axis]], dtype=np.int64) for axis in range(3)]
        matrix = np.column_stack([((powers[0][:, a]*powers[1][:, b]) % p)*powers[2][:, c] % p for a, b, c in exponents])
        rank, minor_ids, _ = eliminate(matrix, p, ids)
        tested.append({'p': p, 'rho': rho, 'rank': rank})
        if rank == N:
            rows = [ids.index(i) for i in minor_ids]
            rank2, _, determinant = eliminate(matrix[rows], p, minor_ids)
            assert rank2 == N and 0 < determinant < p
            break
    else:
        raise AssertionError('bounded independent prime attempts inconclusive: '+str(tested))
    # A disposable repository-shaped copy has no raw data directories.
    mutations = []
    with tempfile.TemporaryDirectory(prefix='padua-review-certificate-portable-') as temp:
        topic = Path(temp)/'topics/padua-3d-20261106'
        (topic/'code').mkdir(parents=True)
        (topic/'evidence').mkdir()
        code = topic/'code/pdpr_certify.py'
        code.write_bytes(Path(producer['checker']['path']).read_bytes())
        assert identity(code)['sha256'] == producer['checker']['sha256']
        delivered = topic/'evidence'/args.payload.name
        delivered.write_bytes(args.payload.read_bytes())
        (topic/'evidence'/Path(provenance['receipt']['path']).name).write_bytes(Path(provenance['receipt']['path']).read_bytes())
        result = subprocess.run([sys.executable, str(code), 'verify', '--payload', str(delivered)],
                                capture_output=True, text=True, check=True)
        assert json.loads(result.stdout)['result']['exact_full_column_rank']
        spec = importlib.util.spec_from_file_location('portable_certificate', code)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert module.load(delivered).tobytes() == physical.tobytes()
        for label in ('duplicate_ID', 'boolean_ID', 'out_of_range_ID', 'bad_count', 'wrong_schema', 'wrong_root', 'composite_prime', 'wrong_determinant'):
            altered = copy.deepcopy(payload)
            if label == 'duplicate_ID': altered['ids'][1] = altered['ids'][0]
            elif label == 'boolean_ID': altered['ids'][0] = False
            elif label == 'out_of_range_ID': altered['ids'][-1] = len(complete)
            elif label == 'bad_count': altered['M'] += 1
            elif label == 'wrong_schema': altered['schema'] = 'unsupported'
            elif label == 'wrong_root': altered['certificate']['rho'] = 1
            elif label == 'composite_prime': altered['certificate']['p'] = 2*L+1
            else: altered['certificate']['det_mod_p'] = 0
            try:
                module.verify(altered)
            except (ValueError, AssertionError):
                mutations.append(label)
            else:
                raise AssertionError('invalid payload accepted: '+label)
    report = {'verdict': 'PASS', 'scope': 'Independent exact full-column-rank certificate for the ideal cosine geometry; measured rounded quality remains separate.',
        'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1',
        'command': ['python', str(Path(__file__)), '--payload', str(args.payload), '--producer-check', str(args.producer_check), '--output', str(args.output)],
        'started_utc': utc, 'ended_utc': datetime.now(timezone.utc).isoformat(), 'actual_cpu': time.process_time()-began,
        'python': platform.python_version(), 'numpy': np.__version__, 'checker': identity(__file__),
        'payload': identity(args.payload), 'producer_check': identity(args.producer_check), 'producer_checker': producer['checker'],
        'n': n, 'orders': orders, 'full_grid_count': len(complete), 'M': M, 'N': N, 'L': L,
        'prime_factors_L': prime_factors, 'prime': p, 'root': rho, 'root_power_L': pow(rho, L, p),
        'order_residues': [[q, pow(rho, L//q, p)] for q in prime_factors],
        'prime_proof': 'Complete integer trial division by every integer2..isqrt(p); Python integer arithmetic.',
        'producer_prime_distinct': p != payload['certificate']['p'],
        'basis': 'Complete monomials in lexical(a,b,c), a=0..n,b=0..n-a,c=0..n-a-b.',
        'rank': rank, 'minor_row_ids': minor_ids, 'minor_det_mod_prime': determinant, 'attempts': tested,
        'arithmetic': {'dtype': 'signed int64 residues', 'single_product_maximum': (p-1)**2,
                       'elimination_difference_absolute_bound': (p-1)**2+(p-1),
                       'rule': 'Pairwise products reduced before third factor; no int64 dot accumulation; Python determinant/power arithmetic.'},
        'geometry_link': {'decoded_ids_match_checkpoint_path': True, 'binary64_bytes_match_checkpoint_and_assessment': True,
                         'binary64_sha256': byte_hash, 'recipe': 'np.cos(np.pi*independently_decoded_indices/np.array(orders))'},
        'inputs': [provenance[k] for k in ('receipt', 'raw_details', 'raw_inventory', 'checkpoint', 'path', 'recipe', 'assessment_map')],
        'portable_no_raw_copy': {'files': ['code/pdpr_certify.py', 'evidence/'+args.payload.name,
            'evidence/'+Path(provenance['receipt']['path']).name], 'actual_cli_verify': 'PASS', 'actual_load_matches': True,
            'mutations_rejected': mutations},
        'conclusion': 'The specified ideal cosine set is Pi_n-determining; positive-weight least squares has a unique coefficient minimizer. M>N, so this is not an N-site interpolant.',
        'limits': 'No exact rank assertion about the separately interpreted binary64 dyadic matrix; no certified norm, conditioning, covariance/error bound, or all-degree theorem. Formal Claude audit remains pending.',
        'research_rounds': 0}
    encoded = json.dumps(report, indent=2)+'\n'
    assert len(encoded.encode()) < 16384, len(encoded)
    args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
