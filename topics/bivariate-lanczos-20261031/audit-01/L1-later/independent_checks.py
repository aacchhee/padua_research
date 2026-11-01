"""Independent Codex checks: no imports from developer/reconstruction modules.

Exact checkerboard moments and a float64 recurrence/QR/Ritz test on the
documented seed-11 square.  The latter is a measurement, not a proof.
"""
from fractions import Fraction as F
import math
import sys
import json
from pathlib import Path
import numpy as np


def checkerboard_moments():
    # Deliberately nonuniform ordered rational nodes, unlike published examples.
    X = list(map(F, [-3, -1, 0, 2, 6]))
    Y = list(map(F, [-4, -2, 1, 3, 5, 9]))
    m = len(X) - 1

    def bary_abs(nodes):
        return [1 / abs(math.prod(x - t for t in nodes if t != x)) for x in nodes]

    wx, wy = bary_abs(X), bary_abs(Y)
    for parity in (0, 1):
        mismatches = []
        for total in range(2 * m + 1):
            for a in range(total + 1):
                b = total - a
                full = sum(wx[i] * wy[j] * x**a * y**b
                           for i, x in enumerate(X) for j, y in enumerate(Y)) / 2
                check = sum(wx[i] * wy[j] * x**a * y**b
                            for i, x in enumerate(X) for j, y in enumerate(Y)
                            if (i + j) % 2 == parity)
                if check != full:
                    mismatches.append((a, b))
        assert not mismatches
        sharp = sum(wx[i] * wy[j] * x**m * y**(m+1) *
                    (F((i+j) % 2 == parity) - F(1, 2))
                    for i, x in enumerate(X) for j, y in enumerate(Y))
        assert sharp != 0
        print('exact_checkerboard', parity, 'moments_checked', 45,
              'mismatches', len(mismatches), 'degree9_x4y5_difference', str(sharp))


def recurrence(points, weights, nmax=24, rule='dev', full=False):
    labels = [(t, j) for t in range(nmax+1) for j in range(t+1)]
    number = {ij: k for k, ij in enumerate(labels)}
    Q = np.zeros((len(points), len(labels)))
    Q[:, 0] = np.sqrt(weights / sum(weights))
    for k, (t, j) in enumerate(labels[1:], 1):
        if rule == 'alt':
            axis = 0 if j < t/2 else 1
        elif rule == 'mirror':
            axis = 1 if j == t else 0
        else:
            axis = 0 if j == 0 else 1
        par = (t-1, j) if axis == 0 else (t-1, j-1)
        vec = points[:, axis] * Q[:, number[par]]
        start = 0 if full else max(t-2, 0) * max(t-1, 1) // 2
        block = Q[:, start:k]
        vec -= block @ (block.T @ vec)
        Q[:, k] = vec / np.linalg.norm(vec)
    return Q


def metrics(Q, points):
    loss = float(abs(Q.T @ Q - np.eye(Q.shape[1])).max())
    U = np.linalg.qr(Q, mode='reduced')[0]
    results = {}
    for label, diagonal in [('x', points[:, 0]), ('y', points[:, 1]),
                             ('z', points[:, 0] + 1j * points[:, 1])]:
        AU = diagonal[:, None] * U
        section = U.T @ AU
        if label == 'z':
            lam, vec = np.linalg.eig(section)
        else:
            lam, vec = np.linalg.eigh((section + section.T)/2)
        residuals = np.linalg.norm(AU @ vec - (U @ vec) * lam, axis=0)
        rho = float(min(residuals))
        results[label] = {'rho': rho, 'loss_over_eps_prediction': loss*rho/(2.0**-52),
                          'loss_over_u_prediction': loss*rho/(2.0**-53)}
    return loss, results


def numerical_scope():
    points = np.random.default_rng(11).uniform(-1, 1, (1681, 2))
    for angle in (0.05, math.pi/4):
        R = np.array([[math.cos(angle), -math.sin(angle)],
                      [math.sin(angle), math.cos(angle)]])
        P = points @ R.T
        Q = recurrence(P, np.ones(len(P)))
        print('rotation', angle, 'n24', metrics(Q, P), flush=True)
        if angle > 0.1:
            for rule, full in [('alt', False), ('dev', True)]:
                Q = recurrence(P, np.ones(len(P)), rule=rule, full=full)
                print('selection_control', rule, 'full', full,
                      'loss', float(abs(Q.T @ Q - np.eye(Q.shape[1])).max()), flush=True)
    weights = np.exp(8 * points[:, 0] * points[:, 1])
    Q = recurrence(points, weights)
    print('exp8xy_n24', metrics(Q, points), flush=True)


def frozen_rule_reanalysis():
    root = Path(__file__).resolve().parents[4]
    logs = root / 'topics/bivariate-lanczos-20261031/directions/L1/logs'
    rows = []
    for suffix in ['input3', 'rotation', 'swap', 'padua', 'irregular']:
        for line in (logs / ('r01_' + suffix + '.raw')).read_text().splitlines():
            if line.startswith('JSON '):
                r = json.loads(line[5:])
                if r['method'] != 'simax' and r['N'] < r['M'] and not (
                        r['run'] == 'tensorcheb41' and r['n'] >= 40):
                    rows.append(r)
    cases = sorted(set((r['run'], r['method']) for r in rows))
    for u in [2.0**-52, 2.0**-53]:
        predictions = {}
        for case in cases:
            data = [r for r in rows if (r['run'], r['method']) == case]
            for key in ['res_x', 'res_y', 'res_z']:
                informative = [r for r in data if max(r['loss'], u/max(r[key], 1e-300)) >= 1000*u]
                predictions[case, key] = bool(informative) and all(
                    1/3 <= r['loss'] * r[key] / u <= 3 for r in informative)
        zp = [case for case in cases if predictions[case, 'res_z']]
        k1 = bool(zp) and all(predictions[c, 'res_x'] or predictions[c, 'res_y'] for c in zp)
        print('stored_data_reanalysis', 'u', u, 'K1', k1, 'Z_predicts', zp)


if __name__ == '__main__':
    print('python', sys.version.split()[0], 'numpy', np.__version__,
          'float64_eps', np.finfo(float).eps, 'longdouble_eps', np.finfo(np.longdouble).eps)
    if len(sys.argv) > 1 and sys.argv[1] == 'rule':
        frozen_rule_reanalysis()
    else:
        checkerboard_moments()
        numerical_scope()
