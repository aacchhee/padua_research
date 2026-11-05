#!/usr/bin/env python3
"""Exact rational moment reconstruction; finite recurrence probe, not a rate fit."""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
import hashlib
import json
from pathlib import Path


def frac(x):
    return str(x.numerator) if x.denominator == 1 else str(x)


class Disk:
    def __init__(self, mu):
        self.mu = mu

    @lru_cache(None)
    def moment(self, r, j):
        if r % 2 or j % 2:
            return F(0)
        a, b = r // 2, j // 2
        numerator = F(factorial(2*a)*factorial(2*b),
                      4**(a+b)*factorial(a)*factorial(b))
        for k in range(a+b):
            numerator /= self.mu + 2 + k
        return numerator

    def inner(self, p, q):
        return sum((v*w*self.moment(r+a, j+b)
                    for (r, j), v in p.items()
                    for (a, b), w in q.items()), F(0))


def product(p, axis):
    return {(r+(axis == 0), j+(axis == 1)): v
            for (r, j), v in p.items()}


def subtract(p, q, c):
    result = p.copy()
    for key, value in q.items():
        result[key] = result.get(key, F(0)) - c*value
        if not result[key]:
            del result[key]
    return result


def directions():
    result = {(F(1), F(0)), (F(-1), F(0)),
              (F(0), F(1)), (F(0), F(-1))}
    for a, b, c in [(3,4,5), (5,12,13), (8,15,17), (7,24,25)]:
        for u, v in [(F(a,c), F(b,c)), (F(b,c), F(a,c))]:
            for sx in [-1, 1]:
                for sy in [-1, 1]:
                    result.add((sx*u, sy*v))
    return sorted(result)


def run(max_degree, mu):
    disk = Disk(mu)
    indices = [(n-j,j) for n in range(max_degree+1) for j in range(n+1)]
    polynomials, norms = [], []
    for rj in indices:
        p = {rj: F(1)}
        for q, norm in zip(polynomials, norms):
            p = subtract(p, q, disk.inner(p,q)/norm)
        d = disk.inner(p,p)
        assert d > 0 and p[rj] == 1
        polynomials.append(p)
        norms.append(d)
    assert all(disk.inner(p,q) == 0
               for k,p in enumerate(polynomials) for q in polynomials[:k])
    lookup = {rj:k for k,rj in enumerate(indices)}
    creator_rows = {}
    for rule in ['bj', 'mirror', 'alt']:
        rows = []
        for k,(r,j) in enumerate(indices[1:], 1):
            use_x = j == 0 or (r > 0 and
                      (rule == 'mirror' or (rule == 'alt' and j < (r+j)/2)))
            axis = 0 if use_x else 1
            parent = lookup[(r-use_x, j-(not use_x))]
            raw = product(polynomials[parent], axis)
            coefficients = [(l,disk.inner(raw,polynomials[l])/norms[l])
                            for l in range(k)]
            coefficients = [(l,a) for l,a in coefficients if a]
            reconstructed = raw
            for l,a in coefficients:
                reconstructed = subtract(reconstructed,polynomials[l],a)
            assert reconstructed == polynomials[k]
            same = [(l,a) for l,a in coefficients
                    if sum(indices[l]) == r+j]
            rows.append({'index': [r,j], 'parent': list(indices[parent]),
                         'axis': 'x' if use_x else 'y',
                         'sigma_monic_squared': frac(disk.inner(raw,raw)),
                         'beta_normalized_squared': frac(norms[k]/norms[parent]),
                         'coefficients': [[*indices[l], frac(a)]
                                          for l,a in coefficients],
                         'same_degree_transfer_squared':
                           [[*indices[l], frac(a*a*norms[l]/norms[k])]
                            for l,a in same]})
        creator_rows[rule] = rows
    degree_summary = []
    for n in range(2,max_degree+1):
        group = [lookup[(n-j,j)] for j in range(n+1)]
        rule_summaries = {}
        for rule, rows in creator_rows.items():
            response = {}
            first = group[0]
            response[first] = F(1)
            for k in group[1:]:
                response[k] = -sum((F(a)*response.get(lookup[(r,j)], F(0))
                                     for r,j,a in rows[k-1]['coefficients']), F(0))
            sigma = F(rows[first-1]['sigma_monic_squared'])
            gain = sigma*sum((response[k]**2/norms[k] for k in group),F(0))
            coupling = max((F(c[2]) for k in group
                            for c in rows[k-1]['same_degree_transfer_squared']),
                           default=F(0))
            rule_summaries[rule] = {'first_final_source_gain_squared': frac(gain),
                                   'largest_same_degree_transfer_squared': frac(coupling),
                                   'same_degree_edges': sum(len(rows[k-1][
                                       'same_degree_transfer_squared']) for k in group)}
        degree_summary.append({'degree':n, 'rules':rule_summaries})
    dirs = directions()
    grid = {(F(k,9)*u, F(k,9)*v) for k in range(1,10) for u,v in dirs}
    assert len(dirs) == 36 and len(grid) == 324
    assert all(u*u+v*v == 1 for u,v in dirs)
    assert all((y,x) in grid and (-x,y) in grid for x,y in grid)
    assert {x*x+y*y for x,y in grid} == {F(k*k,81) for k in range(1,10)}
    grid_text = '\n'.join(f'{frac(x)} {frac(y)}' for x,y in sorted(grid))+'\n'
    return {'status': 'MEASURED exact finite reconstruction', 'mu':frac(mu),
            'maximum_degree':max_degree, 'columns':len(indices),
            'checks': {'orthogonality':True, 'creator_identity':True,
                       'grid_points':len(grid), 'directions':len(dirs),
                       'grid_d4':True, 'grid_sha256':hashlib.sha256(grid_text.encode()).hexdigest()},
            'basis_degree_2': [{'index':list(indices[k]), 'norm_squared':frac(norms[k]),
                                'polynomial':[[*ij,frac(v)] for ij,v in sorted(polynomials[k].items())]}
                               for k in range(min(6,len(indices)))],
            'degree_summary':degree_summary, 'creator_rows':creator_rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degree', type=int, default=8)
    parser.add_argument('--mu', default='0')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    assert 2 <= args.degree <= 12
    mu = F(args.mu)
    assert mu > -1
    report = run(args.degree,mu)
    raw = json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(raw)
    compact = {key:value for key,value in report.items() if key != 'creator_rows'}
    compact['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    compact['report_sha256'] = hashlib.sha256(raw.encode()).hexdigest()
    compact['report_bytes'] = len(raw.encode())
    print(json.dumps(compact,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
