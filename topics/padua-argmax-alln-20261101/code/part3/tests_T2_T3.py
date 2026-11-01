"""Execute plan v2 section 6 T2/T3. Float64 MEASURED only.

Dated 2026-11-01 operational choices: the 9x9 interior macroscopic lattice
is (i*pi/10,j*pi/10), 1<=i,j<=9.  Each search box is centered on its
nearest anti-node, with fixed phase grid {-1/2,-1/4,0,1/4,1/2}^2,
then bounded local refinement.  Macro rounding and parity are retained.
T3 uses ANGLE offsets from (0,pi), rather than Cartesian x,y offsets;
even reflection represents the requested |xi|<=3 by [0,3]^2.
"""
import argparse, json, time
import numpy as np
from tests_common import Eval, validate


def interior():
    rows = []
    for n in (32, 64, 128):
        e = Eval(n)
        for a in range(1, 10):
            for b in range(1, 10):
                j, k = round(n * a / 10), round((n + 1) * b / 10)
                if (j + k) % 2 == 0:
                    opts = [(j + d, k + f) for d, f in ((-1, 0), (1, 0), (0, -1), (0, 1))]
                    j, k = min(opts, key=lambda z: (z[0] / n - a / 10) ** 2 + (z[1] / (n + 1) - b / 10) ** 2)
                vmax, phase = e.cellmax(j, k)
                rows.append({'n': n, 'a': a, 'b': b, 'j': j, 'k': k,
                             'gap': e.lc - vmax, 'phase': phase.tolist(),
                             'antinode_gap': e.lc - e.one(j * np.pi / n, k * np.pi / (n + 1))[0]})
        print('T2 n', n, 'done', flush=True)
    changes = []
    for a in range(1, 10):
        for b in range(1, 10):
            rr = [r for r in rows if r['a'] == a and r['b'] == b]
            changes.append({'a': a, 'b': b, 'change_64_128': abs(rr[2]['gap'] - rr[1]['gap'])})
    return {'rows': rows, 'changes': changes,
            'max_change_64_128': max(changes, key=lambda r: r['change_64_128']),
            'criterion_exceedances': [r for r in changes if r['change_64_128'] > .05]}


def corner():
    # 13x13 includes fixed phases 0,.25,...,3; save all raw gaps.
    q = np.linspace(0, 3, 13)
    rows = []
    for n in (16, 64, 256):
        e = Eval(n)
        for x in q:
            for y in q:
                val, maj = e.one(x * np.pi / n, np.pi - y * np.pi / n)
                rows.append({'n': n, 'xi': float(x), 'eta': float(y),
                             'lambda_minus_corner': val - e.lc, 'majorant_minus_corner': maj - e.lc})
        print('T3 n', n, 'done', flush=True)
    return {'rows': rows}


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('test', choices=['T2', 'T3']); p.add_argument('output')
    args = p.parse_args(); start = time.monotonic()
    out = {'status': 'MEASURED', 'arithmetic': 'float64', 'validation': validate(), 'test': args.test}
    out.update(interior() if args.test == 'T2' else corner())
    out['seconds'] = time.monotonic() - start
    with open(args.output, 'w') as f: json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k not in ('rows', 'changes')}, indent=2))
