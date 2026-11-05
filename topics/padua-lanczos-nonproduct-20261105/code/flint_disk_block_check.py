#!/usr/bin/env python3
"""Exact FLINT matrix-inverse endpoint checker; consumes an untrusted basis export.

No producer/scalar-checker arithmetic module is imported. All exported basis,
creator, Gram, scale and pivot identities are verified before response inversion.
Raw basis and JSONL endpoint arrays belong in /tmp, not Git.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

DEPS = Path('/tmp/padua-lanczos-nonproduct-20261105/deps')
sys.path.insert(0, str(DEPS))
sys.set_int_max_str_digits(1000000)
import flint
from flint import fmpq as Q, fmpq_mat as Mat
flint.ctx.threads = 1
FIELDS = ('Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared')


def require(test, message):
    if not test:
        raise ValueError(message)


def identity(path):
    path = Path(path)
    data = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def scientific(row):
    return {k: v for k, v in row.items()
            if k not in {'elapsed_seconds', 'exact_gram_pairs_checked'}}


def parse_input(path):
    tokens = Path(path).read_text().split()
    require(bool(tokens), 'empty input')
    m = int(tokens[0])
    require(0 < m <= 10000 and len(tokens) == 1 + 3*m, 'input dimensions')
    points = [[Q(v) for v in tokens[1+3*i:4+3*i]] for i in range(m)]
    require(all(p[2] > 0 for p in points), 'positive weights')
    require(sum(p[2] for p in points) == 1, 'normalized weights')
    require(len({(str(p[0]), str(p[1])) for p in points}) == m, 'distinct nodes')
    return points


def verify_basis(doc, points):
    degree, rule = doc['max_degree'], doc['rule']
    require(isinstance(degree, int) and 2 <= degree <= 20, 'degree range')
    require(rule in ('bj', 'mirror', 'alt', 'pivot'), 'rule')
    m, n = len(points), (degree+1)*(degree+2)//2
    require(m > n and doc['point_count'] == m and doc['basis_count'] == n,
            'point/basis counts and M>N')
    require([[Q(v) for v in p] for p in doc['points']] == points,
            'exported points differ from independently read input')
    meta = [[t, j] for t in range(degree+1) for j in range(t+1)]
    ends = [(t+1)*(t+2)//2 for t in range(degree+1)]
    require(doc['meta'] == meta and doc['ends'] == ends, 'grading metadata')
    b = [[Q(v) for v in col] for col in doc['B']]
    d = [Q(v) for v in doc['d']]
    require(len(b) == n and all(len(col) == m for col in b), 'basis dimensions')
    require(len(d) == n and all(v > 0 for v in d), 'positive pivot dimensions')
    require(b[0] == [Q(1)]*m and d[0] == 1, 'exact constant start')
    require(len(doc['steps']) == n and doc['steps'][0] is None, 'steps dimensions')
    B = Mat(b)
    weighted_transpose = Mat([[points[i][2]*b[k][i] for k in range(n)] for i in range(m)])
    gram = B * weighted_transpose
    require(gram == Mat([[d[k] if k == l else 0 for l in range(n)] for k in range(n)]),
            'full weighted Gram identity')
    index = {tuple(tj): k for k, tj in enumerate(meta)}
    candidates, selected = [], []
    for k in range(1, n):
        t, j = meta[k]
        step = doc['steps'][k]
        axis = step['axis']
        require(type(axis) is int and axis in (0, 1), 'axis')
        admissible = [a for a in (0, 1) if not (a == 0 and j == t) and not (a == 1 and j == 0)]
        require(axis in admissible, 'admissible selected parent axis')
        parent = index[t-1, j-axis]
        require(type(step['parent']) is int and step['parent'] == parent, 'selected parent')
        alpha = [Q(v) for v in step['alpha']]
        require(len(alpha) == k, 'alpha dimensions')
        sigma = Q(step['sigma_squared'])
        require(sigma > 0, 'positive source scale')
        selected.append((axis, parent, alpha, sigma))
        if rule != 'pivot':
            wanted = (0 if j == 0 else 1) if rule == 'bj' else ((0 if j != t else 1) if rule == 'mirror' else (0 if 2*j < t else 1))
            require(axis == wanted, 'fixed rule selected wrong axis')
        for a in admissible if rule == 'pivot' else [axis]:
            p = index[t-1, j-a]
            z = [points[i][a]*b[p][i] for i in range(m)]
            scale = sum(points[i][2]*z[i]*z[i] for i in range(m))
            require(scale > 0, 'candidate scale')
            candidates.append((k, a, p, z, scale))
    # Matrix multiplication derives every candidate's exact projection anew.
    C = Mat([c[3] for c in candidates])
    inner = C * weighted_transpose
    coefficients = [[inner[r, l]/d[l] if l < c[0] else Q(0)
                     for l in range(n)] for r, c in enumerate(candidates)]
    residuals = C - Mat(coefficients)*B
    expected = Mat([b[c[0]] for c in candidates])
    require(residuals == expected, 'candidate creator/projection residue identity')
    by_column = {}
    for r, (k, axis, parent, z, scale) in enumerate(candidates):
        by_column.setdefault(k, []).append((axis, parent, scale))
        chosen_axis, chosen_parent, alpha, sigma = selected[k-1]
        if axis == chosen_axis:
            require(parent == chosen_parent and scale == sigma, 'selected source scale')
            require(coefficients[r][:k] == alpha, 'selected projection coefficients')
    ties, choices = [], []
    for k in range(1, n):
        axis, parent, alpha, sigma = selected[k-1]
        if rule == 'pivot':
            cs = by_column[k]
            # All independently checked candidate residuals equal B[k]; their
            # norms therefore are verified d[k]. Compare full exact scores.
            best = max(cs, key=lambda c: (d[k]/c[2], -c[0]))
            require(axis == best[0], 'adaptive pivot score or X tie rule')
            if len(cs) == 2 and d[k]/cs[0][2] == d[k]/cs[1][2]:
                ties.append(meta[k])
        choices.append('XY'[axis])
    require(doc['choices'] == choices and doc['ties'] == ties, 'choices/ties metadata')
    return b, d, selected, ends, choices, ties, {
        'full_weighted_gram_entries': n*n,
        'candidate_creator_vectors_checked': len(candidates),
        'candidate_creator_scalar_entries_checked': len(candidates)*m,
        'all_exported_points_match_input': True,
        'positive_pivots_scales': True, 'choices_ties': True}


def block_unit_inverse(rows):
    # [[L,0],[C,R]]^-1 = [[L^-1,0],[-R^-1 C L^-1,R^-1]].
    # No node/source or representation change: only the exact inverse algorithm.
    n = len(rows)
    if n == 1:
        require(rows[0][0] == 1, 'block inverse unit diagonal')
        return Mat([[1]])
    cut = n//2
    left = block_unit_inverse([row[:cut] for row in rows[:cut]])
    right = block_unit_inverse([row[cut:] for row in rows[cut:]])
    cross = -(right * Mat([row[:cut] for row in rows[cut:]]) * left)
    a, c, r = left.tolist(), cross.tolist(), right.tolist()
    return Mat([row + [Q(0)]*(n-cut) for row in a] +
               [c[j] + r[j] for j in range(n-cut)])


def endpoint_rows(doc, points, verified, started, inverse_check=True):
    b, d, steps, ends, choices, ties, checks = verified
    degree, m, n = doc['max_degree'], len(points), len(b)
    inversed = [1/v for v in d]
    lo, hs, row, traces = [[Q(0) for s in range(degree+1)] for _ in range(4)]
    end_degree = {ends[s]-1: s for s in range(2, degree+1)}
    # Constant source is included in A/G for the inverse identity but omitted
    # from the source budget exactly as specified (h=1,...,N_s-1).
    alpha = [[Q(0)]*n]
    for k, (axis, parent, coeffs, sigma) in enumerate(steps, 1):
        alpha.append(coeffs + [Q(0)]*(n-k))
    identity_matrix = Mat([[int(k == l) for l in range(n)] for k in range(n)])
    phase_inverse = phase_validation = phase_energy = 0.0
    for i, point in enumerate(points):
        normal, value = {}, Q(1)
        for k in range(n):
            value -= point[2]*b[k][i]*b[k][i]*inversed[k]
            if k in end_degree:
                s = end_degree[k]
                require(0 <= value <= 1, 'normal projector diagonal')
                normal[s] = value
                traces[s] += value
        a = [r[:] for r in alpha]
        for k in range(n):
            a[k][k] = Q(1)
        for k, (axis, parent, coeffs, sigma) in enumerate(steps, 1):
            a[k][parent] -= point[axis]
        A = Mat(a)
        phase_start = time.perf_counter()
        G = block_unit_inverse(a)
        phase_inverse += time.perf_counter()-phase_start
        phase_start = time.perf_counter()
        if inverse_check:
            require(A*G == identity_matrix, 'node inverse identity')
        phase_validation += time.perf_counter()-phase_start
        phase_start = time.perf_counter()
        totals, maxima = [Q(0)]*(degree+1), [Q(0)]*(degree+1)
        for h in range(1, n):
            energy = Q(0)
            sigma = steps[h-1][3]
            for k in range(h, n):
                v = G[k, h]
                energy += v*v*inversed[k]
                if k in end_degree:
                    s = end_degree[k]
                    contribution = sigma*energy
                    totals[s] += contribution
                    maxima[s] = max(maxima[s], contribution)
        for s in range(2, degree+1):
            lo[s] = max(lo[s], normal[s]*maxima[s])
            hs[s] += normal[s]*totals[s]
            row[s] = max(row[s], totals[s])
        phase_energy += time.perf_counter()-phase_start
        if (i+1) % 32 == 0 or i+1 == m:
            print(f'node {i+1}/{m}', file=sys.stderr, flush=True)
    result = []
    for s in range(2, degree+1):
        ns = ends[s]
        require(traces[s] == m-ns, 'normal trace')
        upper = min(hs[s], row[s])
        require(0 < lo[s] <= upper, 'endpoint order')
        result.append({'set': doc['family'], 'rule': doc['rule'], 'degree': s,
            'sources': 'all', 'source_count': ns-1, 'point_count': m, 'basis_count': ns,
            **{f: {'exact': str(v)} for f, v in zip(FIELDS, (lo[s], hs[s], row[s], upper))},
            'pivot_choices': choices[:ns-1], 'pivot_ties': [p for p in ties if p[0] <= s],
            'normal_trace_exact': str(traces[s]),
            'exact_gram_pairs_checked': n*(n-1)//2,
            'elapsed_seconds': time.monotonic()-started})
    checks.update(node_inverse_count=m, node_inverse_product_checks=m if inverse_check else 0,
                  every_source_prefix=True, normal_diagonal_trace=True,
                  phase_inverse_seconds=phase_inverse,
                  phase_inverse_validation_seconds=phase_validation,
                  phase_energy_accumulation_seconds=phase_energy)
    return result


def run(args):
    start = time.monotonic()
    require(flint.__version__ == '0.9.0', 'requires pinned python-flint0.9.0')
    paths = [args.input, args.basis, Path(__file__), args.export_source, args.export_binary]
    identities = [identity(p) for p in paths]
    references = [(path, identity(path)) for path in args.reference]
    doc = json.loads(args.basis.read_text())
    points = parse_input(args.input)
    verified = verify_basis(doc, points)
    basis_seconds = time.monotonic()-start
    print(f'verified_basis_seconds {basis_seconds:.6f}', file=sys.stderr, flush=True)
    result = endpoint_rows(doc, points, verified, start)
    comparisons = []
    for path, ident in references:
        expected = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        require(bool(expected) and [r['degree'] for r in expected] == list(range(2, expected[-1]['degree']+1)) and expected[-1]['degree'] >= doc['max_degree'], 'reference degree coverage')
        reference_max_degree = expected[-1]['degree']
        expected = [r for r in expected if r['degree'] <= doc['max_degree']]
        require([scientific(r) for r in result] == [scientific(r) for r in expected],
                'reference scientific fields mismatch: '+str(path))
        comparisons.append({'reference': ident, 'status': 'PASS all scientific fields',
                            'rows': len(result), 'reference_max_degree': reference_max_degree,
                            'comparison_prefix': [2, doc['max_degree']], 'omitted_fields': ['elapsed_seconds', 'exact_gram_pairs_checked']})
    for p, ident in zip(paths, identities):
        require(identity(p) == ident, 'input/code/export changed during check')
    for p, ident in references:
        require(identity(p) == ident, 'reference changed during check')
    args.output.write_text(''.join(json.dumps(r, separators=(',', ':'))+'\n' for r in result))
    receipt = {'status': 'PASS exact FLINT block-inverse finite check',
        'independent_agent_review': 'not established by this developer execution',
        'family': doc['family'], 'rule': doc['rule'], 'max_degree': doc['max_degree'],
        'input': identities[0], 'basis_export': identities[1], 'checker': identities[2],
        'exporter_source': identities[3], 'exporter_binary': identities[4],
        'output': identity(args.output), 'checks': verified[-1], 'comparisons': comparisons,
        'command': [sys.executable, '-B', *sys.argv],
        'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
        'threads': flint.ctx.threads, 'python': platform.python_version(),
        'source_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'platform': platform.platform(), 'basis_validation_seconds': basis_seconds,
        'elapsed_seconds': time.monotonic()-start,
        'model': 'all-source weighted Euclidean aggregate input; spectral normal output; no extra node weight in v',
        'method': 'Full rational Gram/creator verification, per-node recursive unit-triangular block inverse, A*G=I, every original source/node/prefix'}
    args.receipt.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'status': receipt['status'], 'seconds': receipt['elapsed_seconds'],
                      'receipt': str(args.receipt)}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'basis', 'output', 'receipt', 'export-source', 'export-binary'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--reference', type=Path, action='append', default=[])
    args = parser.parse_args()
    try:
        run(args)
    except Exception as exc:
        failure = {'status': 'FAILED exact FLINT check', 'error': str(exc),
                   'command': [sys.executable, '-B', *sys.argv], 'checker': identity(__file__)}
        args.receipt.write_text(json.dumps(failure, indent=2)+'\n')
        raise


if __name__ == '__main__':
    main()
