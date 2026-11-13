#!/usr/bin/env python3
"""Audit the already retained cyclic-block lead on fixed nonunique S supports.

No new candidate selection or quality search. The input is the fresh S audit's
complete exact-rank output; every full-rank nonunique-support member is tested.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import sys
import tempfile
import time

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import ia3_exact as base


def scc(graph):
    counter, index, low, stack, active, parts = 0, {}, {}, [], set(), []

    def visit(v):
        nonlocal counter
        index[v] = low[v] = counter
        counter += 1
        stack.append(v)
        active.add(v)
        for w in graph[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in active:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            part = []
            while True:
                w = stack.pop()
                active.remove(w)
                part.append(w)
                if w == v:
                    break
            parts.append(sorted(part))

    for v in range(len(graph)):
        if v not in index:
            visit(v)
    return parts


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parents[1]
    input_path = root/'evidence/ia3-s-exact.json'
    input_doc = json.loads(input_path.read_text())
    raw_input = Path(input_doc['raw']['path'])
    assert base.sha(raw_input) == input_doc['raw']['sha256']
    source_paths = [Path(__file__).resolve(), Path(base.__file__).resolve()]
    snapshots = {p: p.read_bytes() for p in source_paths}
    scratch = Path(tempfile.mkdtemp(prefix='padua-ia3-blocks-'))
    for p, data in snapshots.items():
        (scratch/p.name).write_bytes(data)
    rows, raw = [], []
    for record in map(json.loads, raw_input.read_text().splitlines()):
        n = record['n']
        N = base.math.comb(n+3, 3)
        if record['support'] != 'alternating-cycle' or record['rank_Q'] != N:
            continue
        z = record['z']
        columns = base.dct_columns(n, z)
        matching = dict(base.match(columns))
        matrix = [[columns[j].get(matching[i], 0) for j in range(N)] for i in range(N)]
        graph = [{j for j, x in enumerate(row) if x and j != i} for i, row in enumerate(matrix)]
        parts = scc(graph)
        A = DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(sp.QQ)
        inv = A.inv()
        assert (A*inv).to_Matrix() == sp.eye(N)
        inverse = inv.to_Matrix()*8
        sums = [sum(abs(inverse[i, j]) for j in range(N)) for i in range(N)]
        result = {'n': n, 'z': z, 'S': str(sum(sums)), 'inverse_inf': str(max(sums)),
                  'block_size_histogram': dict(Counter(map(len, parts))),
                  'max_block_size': max(map(len, parts))}
        rows.append(result)
        raw.append({'result': result, 'scc_mode_indices': parts, 'row_matching': matching,
                    'inverse_row_l1': [str(v) for v in sums]})
    target = scratch/'all-positive-nonunique-blocks.json'
    target.write_bytes(base.serial(raw)+b'\n')
    assert all(p.read_bytes() == data for p, data in snapshots.items())
    receipt = {'pin': base.PIN, 'command': sys.argv,
               'code': [{'path': str(p), 'sha256': base.sha(p), 'snapshot': str(scratch/p.name)} for p in source_paths],
               'input': {'path': str(input_path), 'sha256': base.sha(input_path), 'raw': input_doc['raw']},
               'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
               'rows': rows, 'seconds': time.monotonic()-started,
               'raw': {'path': str(target), 'bytes': target.stat().st_size, 'sha256': base.sha(target),
                       'retention': 'local regenerate-only; no cold-storage delivery'}}
    output = base.serial(receipt)+b'\n'
    assert len(output) < 16384
    path = root/'evidence/ia3-blocks.json'
    path.write_bytes(output)
    print(json.dumps({'receipt': str(path), 'bytes': len(output), 'seconds': receipt['seconds'], 'rows': rows}))


if __name__ == '__main__':
    main()
