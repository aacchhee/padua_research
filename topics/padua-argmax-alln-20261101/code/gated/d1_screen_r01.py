#!/usr/bin/env python3
"""D1 round 1 pre-registered float64 screen; MEASURED, never an enclosure.

See gated/d1/r01-screen.md for grids, numerical flags and interpretation.
The full periodic odd mesh avoids the invalid nonzero-alpha folded sum.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import sys
import time

import numpy as np
import scipy

TOPIC = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOPIC / 'code' / 'part3'))
from tests_common import Eval, Primitive, kernel, validate


class PeriodicPrimitive:
    def __init__(self, n):
        self.n, self.m = n, n + 1
        jj, rr = np.nonzero((np.arange(2 * n)[:, None]
                             + np.arange(2 * (n + 1))[None, :]) % 2)
        self.u, self.v = jj * np.pi / n, rr * np.pi / (n + 1)
        assert len(jj) == 2 * n * (n + 1)
        self.cache = {}

    def one(self, alpha, beta):
        key = (float(alpha), float(beta))
        if key not in self.cache:
            self.cache[key] = float(np.abs(kernel(
                self.n, self.u + alpha / self.n,
                self.v + beta / self.m)).sum() / (2 * self.n * self.m))
        return self.cache[key]


def near_grid(h):
    return [(i * h / 2, j * h / 2)
            for i in range(-2, 3) for j in range(-2, 3)
            if abs(i) + abs(j) <= 2]


def nearest_odd(n, t, p):
    m = n + 1
    j0, k0 = round(n * t / np.pi), round(m * p / np.pi)
    candidates = [(j, k) for j in range(max(0, j0 - 2), min(n, j0 + 2) + 1)
                  for k in range(max(0, k0 - 2), min(m, k0 + 2) + 1)
                  if (j + k) % 2]
    return min(candidates,
               key=lambda z: ((z[0] * np.pi / n - t) ** 2
                              + (z[1] * np.pi / m - p) ** 2,
                              z[0], z[1]))


def fourcopy(e, t, p):
    gs = np.array([kernel(e.n, t + a * e.th, p + b * e.ph)
                   for a in (-1, 1) for b in (-1, 1)])
    aa = np.abs(gs).sum(axis=0)
    val = float(np.sum(e.w * np.abs(gs.mean(axis=0))))
    maj = float(np.sum(e.w * aa / 4))
    qv = float(np.sum(e.w * (aa - np.abs(gs[0] + gs[1])
                            - np.abs(gs[2] + gs[3])) / 4))
    qh = float(np.sum(e.w * (aa - np.abs(gs[0] + gs[2])
                            - np.abs(gs[1] + gs[3])) / 4))
    defect = maj - val
    assert defect + 1e-10 >= max(qv, qh)
    assert min(qv, qh) >= -1e-10
    return {'lambda': val, 'majorant': maj, 'defect': defect,
            'Qv': qv, 'Qh': qh, 'corner_gap': e.lc - val}


def validation():
    out = {'existing_matrix_validation': validate(), 'periodic_checks': []}
    for n in (2, 3, 4, 8, 16):
        e, primitive, folded = Eval(n), PeriodicPrimitive(n), Primitive(n)
        for a, b in ((0., 0.), (.17, -.11), (-.23, .07), (.09, .19)):
            t, p = a / n, (np.pi + b) / (n + 1)
            val, maj = e.one(t, p)
            fresh = fourcopy(e, t, p)
            ss = primitive.one(a, b)
            errors = [abs(ss - maj), abs(fresh['majorant'] - maj),
                      abs(fresh['lambda'] - val)]
            if a == b == 0:
                errors.extend([abs(ss - e.lc), abs(ss - folded.lc)])
            assert max(errors) < 1e-9
            out['periodic_checks'].append({'n': n, 'alpha': a, 'beta': b,
                                           'max_abs_error': max(errors)})
    return out


def extrema(rows, key, want_min=False):
    return (min if want_min else max)(rows, key=lambda r: r[key])


def sampled_record(e, primitive, t, p, j, k, extra):
    alpha, beta = e.n * t - j * np.pi, (e.n + 1) * p - k * np.pi
    ans = fourcopy(e, t, p)
    ss = primitive.one(alpha, beta)
    ans.update({'theta': t, 'phi': p, 'J': j, 'K': k,
                'alpha': alpha, 'beta': beta, 'S_periodic': ss,
                'periodic_majorant_error': ss - ans['majorant'], **extra})
    assert abs(ans['periodic_majorant_error']) < 1e-8
    return ans


def strip_samples(e, primitive):
    n, m = e.n, e.n + 1
    rows = []
    for side in ('left', 'right', 'bottom', 'top'):
        vertical = side in ('left', 'right')
        steps = n if vertical else m
        tangent_steps = m if vertical else n
        for width in (1, 2, 4, 8):
            normal = width / n
            if side in ('right', 'top'):
                normal = np.pi - normal
            normal_index = round(steps * normal / np.pi)
            for ordinate in (.25, .5, .75):
                options = [i for i in range(tangent_steps + 1)
                           if (normal_index + i) % 2]
                tangent_index = min(options,
                    key=lambda i: (abs(i / tangent_steps - ordinate), i))
                tangent = tangent_index * np.pi / tangent_steps
                t, p = ((normal, tangent) if vertical else (tangent, normal))
                j, k = ((normal_index, tangent_index) if vertical
                        else (tangent_index, normal_index))
                rows.append(sampled_record(e, primitive, t, p, j, k,
                    {'side': side, 'width_times_n': width,
                     'macro_tangent_over_pi': ordinate}))
    return rows


def degree_screen(n):
    start_wall, start_cpu = time.monotonic(), time.process_time()
    e, primitive = Eval(n), PeriodicPrimitive(n)
    lc = primitive.one(0., 0.)
    assert abs(lc - e.lc) < 1e-8
    logs = math.log(n + 1)
    global_rows = []
    for i in range(-8, 9):
        for j in range(-8, 9):
            if abs(i) + abs(j) > 8:
                continue
            alpha, beta = i * np.pi / 8, j * np.pi / 8
            aa = (math.cos(alpha) + math.cos(beta)) / 2
            ss = primitive.one(alpha, beta)
            global_rows.append({'alpha': alpha, 'beta': beta, 'a': aa,
                'S': ss, 'excess': ss - lc,
                'remainder_over_log': (ss - aa * lc) / logs})
    local_rows = []
    for label, h in (('inverse_log_squared', 1 / logs ** 2), ('inverse_n', 1 / n)):
        for alpha, beta in near_grid(h):
            ss = primitive.one(alpha, beta)
            local_rows.append({'scale': label, 'h': h, 'alpha': alpha,
                              'beta': beta, 'S': ss, 'excess': ss - lc})
    compact = []
    h = 1 / logs ** 2
    for a in (.25, .5, .75):
        for b in (.25, .5, .75):
            j, k = nearest_odd(n, a * np.pi, b * np.pi)
            for alpha, beta in near_grid(h):
                t, p = (j * np.pi + alpha) / n, (k * np.pi + beta) / (n + 1)
                compact.append(sampled_record(e, primitive, t, p, j, k,
                    {'macro_theta_over_pi': a, 'macro_phi_over_pi': b,
                     'zero_phase': alpha == beta == 0.,
                     'grid_alpha': alpha, 'grid_beta': beta}))
    strips = strip_samples(e, primitive)
    compact_minima = {}
    for label, rr in [('all', compact),
                      ('zero', [r for r in compact if r['zero_phase']]),
                      ('small_nonzero', [r for r in compact if not r['zero_phase']])]:
        compact_minima[label] = {key: extrema(rr, key, True)
                                 for key in ('defect', 'Qv', 'Qh', 'corner_gap')}
    summary = {'n': n, 'Lambda_c': lc,
        'global_remainder_max': extrema(global_rows, 'remainder_over_log'),
        'global_excess_max': extrema(global_rows, 'excess'),
        'local_excess_max': {label: extrema([r for r in local_rows
                                           if r['scale'] == label], 'excess')
                            for label in ('inverse_log_squared', 'inverse_n')},
        'compact_minima': compact_minima,
        'strip_minima': {key: extrema(strips, key, True)
                         for key in ('defect', 'Qv', 'Qh', 'corner_gap')},
        'max_periodic_majorant_error': max(abs(r['periodic_majorant_error'])
                                          for r in compact + strips),
        'wall_seconds': time.monotonic() - start_wall,
        'cpu_seconds': time.process_time() - start_cpu}
    return {'summary': summary, 'global_phase_samples': global_rows,
            'near_phase_samples': local_rows, 'compact_samples': compact,
            'moving_strip_samples': strips}


def flags(degrees):
    byn = {r['summary']['n']: r['summary'] for r in degrees}
    if not all(n in byn for n in (64, 128, 256)):
        return {'assessed': False, 'reason': 'bounded budget omitted required degree'}
    rr = [byn[n]['global_remainder_max']['remainder_over_log'] for n in (64, 128, 256)]
    dd = [byn[n]['compact_minima']['all']['defect']['defect'] for n in (64, 128, 256)]
    local = {}
    for scale in ('inverse_log_squared', 'inverse_n'):
        xx = [byn[n]['local_excess_max'][scale]['excess'] for n in (64, 128, 256)]
        local[scale] = {'values_n64_128_256': xx,
                        'kill_flag': xx[-1] > 1e-4 and xx[0] <= xx[1] <= xx[2]}
    return {'assessed': True, 'global_values_n64_128_256': rr,
            'global_kill_flag': rr[-1] > 2 * max(rr[0], 0) and rr[0] < rr[1] < rr[2],
            'local': local, 'compact_defect_values_n64_128_256': dd,
            'compact_defect_kill_flag': dd[-1] < .01 and dd[-1] < dd[0] / 2}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    parser.add_argument('--cpu-budget', type=float, default=180.)
    args = parser.parse_args()
    start_cpu, start_wall = time.process_time(), time.monotonic()
    source_files = [Path(__file__).resolve(), TOPIC / 'code/part3/tests_common.py',
                    TOPIC / 'code/maj.py', TOPIC / 'gated/d1/r01-screen.md']
    out = {'status': 'MEASURED', 'arithmetic': 'NumPy float64; no outward rounding',
           'rules_head': '2dde541f1e5af239cae6e93e4438b9be89d15d87',
           'scientific_input_head': '7d308b10d946b607ae0690454f6c0103690775a4',
           'argv': sys.argv, 'python': sys.version, 'platform': platform.platform(),
           'numpy': np.__version__, 'scipy': scipy.__version__, 'seed': None,
           'source_sha256': {str(p.relative_to(TOPIC)): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in source_files},
           'validation': validation(), 'degrees': []}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for n in (16, 32, 64, 128, 256):
        if out['degrees'] and time.process_time() - start_cpu > args.cpu_budget:
            out['budget_stop_before_n'] = n
            break
        run = degree_screen(n)
        out['degrees'].append(run)
        print(json.dumps(run['summary'], sort_keys=True), flush=True)
        args.output.write_text(json.dumps(out, indent=2) + '\n')
    out['flags'] = flags(out['degrees'])
    out['wall_seconds'] = time.monotonic() - start_wall
    out['cpu_seconds'] = time.process_time() - start_cpu
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'flags': out['flags'], 'wall_seconds': out['wall_seconds'],
                      'cpu_seconds': out['cpu_seconds']}, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
