"""Focused audit-02 checks, independent of developer imports.

Usage from repository root:
python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/independent_response_checks.py

The product example checks the missing implication in T116's hypothesis;
it is an exact coefficient perturbation, not an executed floating-point run.
The N101 check reanalyses committed raw data, not the original recurrences.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math


def inverse(a):
    n = len(a)
    b = [list(row) + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if b[i][j])
        b[j], b[k] = b[k], b[j]
        pivot = b[j][j]
        b[j] = [x / pivot for x in b[j]]
        for i in range(n):
            if i != j:
                pivot = b[i][j]
                b[i] = [x - pivot * y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def norm(a):
    return max(sum(abs(x) for x in row) for row in a)


def difference(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


print('T116: exact product probability measure on {+-a}^2, n=1, node (a,a)')
for a, relative in [(F(1, 100), F(1, 100)), (F(1, 2**80), F(1, 2**52))]:
    delta = a * relative
    L = [[F(1), F(0), F(0)], [-a, a, F(0)], [-a, F(0), a]]
    Lh = [[F(1), F(0), F(0)], [-a, a + delta, F(0)], [-a, F(0), a + delta]]
    Li, Lhi = inverse(L), inverse(Lh)
    kappa = norm(Li)
    # p_0=r_0=1, p_1(+-a)=r_1(+-a)=+-1; Lambda_x=Lambda_y=1; b_min=a.
    B = 4 * (1 + 1 / a)**2
    assert norm(difference(Lh, L)) == delta
    assert kappa == 1 + 1 / a
    assert kappa * delta < F(1, 50)
    assert B * delta > 1
    assert norm(Lhi) <= kappa / (1 - kappa * delta)
    assert norm(difference(Lhi, Li)) <= kappa**2 * delta / (1 - kappa * delta)
    assert B / (1 - B * delta) < 0 < norm(Lhi)
    print(json.dumps(dict(a=str(a), beta_relative_error=str(relative),
                         kappa_delta_exact=str(kappa * delta),
                         B_delta_exact=str(B * delta),
                         kappa_delta=float(kappa * delta), B_delta=float(B * delta),
                         inverse_norm=float(norm(Lhi)),
                         Neumann_bounds_valid=True,
                         proposed_B_bound_negative=True), sort_keys=True))

root = Path('topics/bivariate-lanczos-20261031/directions/L1/logs')
data = {}
for fn in ['r01_input3.raw', 'r01_rotation.raw', 'r01_irregular.raw']:
    for line in (root / fn).read_text().splitlines():
        if line.startswith('JSON '):
            r = json.loads(line[5:])
            key = r['run'], r['method'], r['n']
            assert key not in data, key
            data[key] = r

scopes = ['random1681_s0_rot0.3', 'random1681_s7_rot1.0', 'tensorcheb41_rot0.3',
          'Lshape_grid61', 'Lshape_grid61_rot0.3', 'Lshape_rand3000', 'annulus_rand3000']
def frac(x):
    return F(str(x))  # exact decimal values of the committed JSON fields

print('N101(a1): independent exact-decimal reanalysis of stored JSON; no recurrence rerun')
for exponent in [52, 53]:
    unit = F(1, 2**exponent)
    threshold = 1000 * unit
    values, own_values = [], []
    for run in scopes:
        for method in ['bj', 'hl']:
            for n in range(4, 41, 4):
                row = data[run, method, n]
                assert row['N'] < row['M']
                loss = frac(row['loss'])
                for obj in ['res_x', 'res_y', 'res_z', 'res_l', 'res_nk']:
                    source = data[run, 'simax', n] if obj == 'res_nk' else row
                    rho = frac(source[obj])
                    assert rho > 0
                    pred = unit / rho
                    if loss >= threshold or pred >= threshold:
                        values.append((loss / pred, run, method, n, obj))
        for n in range(4, 41, 4):
            row = data[run, 'simax', n]
            loss, rho = frac(row['loss']), frac(row['res_nk'])
            pred = unit / rho
            if loss >= threshold or pred >= threshold:
                own_values.append(loss / pred)
    count = sum(F(1, 3) <= value[0] <= 3 for value in values)
    assert count == 0
    lo, hi = min(values), max(values)
    print(json.dumps(dict(unit=f'2^-{exponent}', triples=len(values), in_factor3_band=count,
                         min_ratio=float(lo[0]), min_identity=lo[1:],
                         max_ratio=float(hi[0]), max_identity=hi[1:],
                         simax_own_min=float(min(own_values)),
                         simax_own_max=float(max(own_values))), sort_keys=True))

rates = []
for run in scopes:
    for method in ['bj', 'hl']:
        for n in [8, 12, 16, 20]:
            rates.append(math.log10(data[run, method, n+4]['loss'] / data[run, method, n]['loss']))
pairs = [('random1681_s0', 'random1681_s0_rot0.3'), ('random1681_s7', 'random1681_s7_rot1.0'),
         ('tensorcheb41', 'tensorcheb41_rot0.3'), ('Lshape_grid61', 'Lshape_grid61_rot0.3')]
deviations, through24 = [], []
for before, after in pairs:
    for method in ['bj', 'hl']:
        for n in range(4, 41, 4):
            x, y = data[before, method, n], data[after, method, n]
            deviation = abs(frac(y['res_z']) / frac(x['res_z']) - 1)
            if x['loss'] < 1e-8 and y['loss'] < 1e-8:
                deviations.append(deviation)
            if n <= 24:
                through24.append(deviation)
print(json.dumps(dict(growth_decades_per4_min=min(rates), growth_decades_per4_max=max(rates),
                     rotation_max_relative_before_loss1e8=float(max(deviations)),
                     rotation_max_relative_through24=float(max(through24))), sort_keys=True))
print('ALL INDEPENDENT CHECKS PASSED')
