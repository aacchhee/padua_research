#!/usr/bin/env python3
"""Preregistered odd-degree even-order rank-only lex selector and quality."""
import itertools as it
import json
import math
import time

import numpy as np

import t8_cyclic as core
from t2_screen import leb, controls


def main():
    assert json.loads((core.TOP/'evidence/t8-controls.json').read_text())['verdict'] == 'PASS'
    start = time.time()
    out = core.metadata('OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_even_family.py')
    out.update({'source_sha256': core.sha(__file__), 'core_sha256': core.sha(core.__file__),
                'known_before_preregistration': 'n3 sole U fullrank M38 z=(1,6,17); no E quality',
                'admissible_degrees': 'odd n>=3', 'selection': 'lex first full rank; rank only',
                'mesh': '21^3 Lobatto', 'rows': [], 'D2_promising': False,
                'fit': 'INCONCLUSIVE: fewer than six n>=4 rows', 'kill': None})
    mesh = np.array(list(it.product(leb.lobatto(21), repeat=3)))
    losses = 0
    core.SCRATCH.mkdir(exist_ok=True)
    for n in [3, 5, 7, 9, 11]:
        degree_start = time.time()
        N = math.comb(n+3, 3)
        M = 2*N-2
        path = core.SCRATCH/f't8-even-selector-n{n}.jsonl'
        selected = None
        visited = 0
        exhausted = False
        with path.open('w') as fp:
            for b, c in it.combinations(range(1, N), 2):
                if (b+c) % 2 != 1:
                    continue
                if time.time()-degree_start > 900:
                    exhausted = True
                    break
                z = (1, b, c)
                L, pts = core.nodes(M, z)
                assert len(pts) == N
                r, v = core.rank_null(core.dictionary(n, M, z))
                visited += 1
                fp.write(json.dumps({'z': z, 'rank': r, 'null': v}, separators=(',', ':'))+'\n')
                if r == N:
                    selected = z
                    break
        row = {'n': n, 'N': N, 'M': M, 'visited_candidates': visited,
               'selected': selected, 'raw_path': str(path),
               'raw_sha256': core.sha(path), 'raw_bytes': path.stat().st_size,
               'selector_complete_to_selected': bool(selected) or not exhausted,
               'search_seconds': round(time.time()-degree_start, 3)}
        if selected is None:
            out['kill'] = 'resource_exhaustion_OPEN' if exhausted else 'no_fullrank_member_at_admissible_degree'
            out['rows'].append(row)
            break
        E = leb.basis(mesh, n)
        row['baselines'] = controls(n, mesh, E)
        physical = np.cos(2*np.pi*np.array(pts)/L)
        row['quality'] = leb.diagnose(physical, n, mesh, E)
        value = row['quality']['sampled_lebesgue']
        if n >= 6 and value is not None and value > row['baselines']['Leja']:
            losses += 1
        else:
            losses = 0
        row['consecutive_admissible_Leja_losses_n_ge6'] = losses
        out['rows'].append(row)
        print(json.dumps(row), flush=True)
        if losses == 2:
            out['kill'] = 'two_consecutive_admissible_Leja_losses_n_ge6'
            break
    if out['kill'] is None:
        out['kill'] = 'bounded_screen_exhausted_n11; no_D2_fit'
    out['seconds'] = round(time.time()-start, 3)
    core.write_receipt('t8-even-family.json', out)


if __name__ == '__main__':
    main()
