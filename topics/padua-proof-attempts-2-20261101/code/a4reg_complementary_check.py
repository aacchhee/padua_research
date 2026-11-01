"""Finite exact regression of theory71; no numerical absolute-value signs."""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import time
import sympy as sp
from sympy.external.gmpy import GROUND_TYPES
from sympy.polys.matrices import DomainMatrix

IMPORTED_SHA = '13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(n, old):
    m, N = n + 1, n * (n + 1)
    order = 2 * N
    z = sp.Symbol('z')
    field = sp.QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(order, z), z), 'zeta')
    root = field([1, 0])
    powers = [root ** i for i in range(order)]
    half = field.convert(sp.Rational(1, 2))
    cosines = [half * (powers[i] + powers[-i % order]) for i in range(order)]
    def cos(i):
        return cosines[i % order]
    def endpoint_weight(i, maximum):
        return sp.Rational(1, 2) if i in (0, maximum) else sp.Integer(1)
    def key(value):
        return tuple(str(coefficient) for coefficient in value.to_list())
    def evaluate(coefficients, value):
        result = field.zero
        for coefficient in reversed(coefficients):
            result = result * value + field.convert(coefficient)
        return result
    cheb = old.chebyshev_coefficients(n + 1)
    p, derivative, divided = old.divided_difference(n, cheb)
    def Q(a, b):
        return sum((field.convert(c) * a ** i * b ** j
                    for (i, j), c in divided.items()), field.zero)
    nodes = [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]
    modes = [(a, d-a) for d in range(n + 1) for a in range(d, -1, -1)]
    matrix = DomainMatrix([[cos(a*j*m)*cos(b*k*n) for a,b in modes]
                          for j,k in nodes], (len(nodes),len(nodes)),field)
    inverse = matrix.inv().to_list()
    assert (matrix * DomainMatrix(inverse, matrix.shape, field)).to_dense() == DomainMatrix.eye(len(nodes),field).to_dense()
    point_count = regular_count = singular_count = multiset_entries = 0
    for epsilon in (-1, 1):
        r = n if epsilon == -1 else 0
        for q in range(1, m):
            if (r + q) % 2 != 1:
                continue
            point_count += 1
            raw = defaultdict(lambda: sp.S.Zero)
            odd = defaultdict(lambda: sp.S.Zero)
            exceptional = []
            for index,(j,k) in enumerate(nodes):
                jp = j if epsilon == 1 else n-j
                A = cos(jp*m)
                zs = [cos((q+k)*n), cos((q-k)*n)]
                tau = field.convert((-1)**jp)
                weight = 2*endpoint_weight(j,n)*endpoint_weight(k,m)/N
                E = []
                coincidences = []
                for shifted in zs:
                    coincident = shifted == A
                    coincidences.append(coincident)
                    if coincident:
                        assert A == -field.one
                        E.append(field.zero)
                    else:
                        E.append((field.one+shifted)/(A-shifted))
                true_kernel = half*(Q(A,zs[0])+Q(A,zs[1]))-tau
                cardinal = sum((inverse[mode][index] * field.convert(epsilon**a) * cos(b*q*n)
                                for mode,(a,b) in enumerate(modes)),field.zero)
                assert cardinal == field.convert(weight)*true_kernel
                formal = tau*(E[0]+E[1])
                if any(coincidences):
                    exceptional.append((jp,k))
                    assert coincidences == [True,False]
                    assert jp == n and k == m-q and weight == sp.Rational(1,N)
                    assert E == [field.zero,-field.one]
                    assert true_kernel == tau*field.convert(n-1)
                    assert formal == -tau
                    assert true_kernel**2 == field.convert((n-1)**2)
                    assert formal**2 == field.one
                    assert Q(-field.one,-field.one) == evaluate(derivative,-field.one)
                    singular_count += 1
                else:
                    assert true_kernel == formal
                    for shifted,e in zip(zs,E):
                        assert Q(A,shifted)-tau == field.convert(2)*tau*e
                    regular_count += 1
                for e in E:
                    raw[key(e)] += weight
            assert exceptional == [(n,m-q)]
            for jp in range(n+1):
                for ell in range(m+1):
                    if (jp+ell)%2 != 1:
                        continue
                    A, B = cos(jp*m),cos(ell*n)
                    if A == B:
                        assert A == -field.one
                        e = field.zero
                    else:
                        e = (field.one+B)/(A-B)
                    odd[key(e)] += 4*endpoint_weight(jp,n)*endpoint_weight(ell,m)/N
            assert dict(raw) == dict(odd)
            assert sum(raw.values()) == sum(odd.values()) == 2
            multiset_entries += len(raw)
            assert sp.Rational(1,m)-sp.Rational(n-2,N) == sp.Rational(2,N)
    return {'n':n,'nodes':len(nodes),'complementary_points':point_count,
            'regular_cardinal_identities':regular_count,'unique_endpoint_checks':singular_count,
            'weighted_raw_E_multiset_distinct_entries':multiset_entries,
            'weighted_raw_E_multisets_exact':True,'endpoint_actual_n_minus_1_formal_1':True,
            'rational_plus_2_over_N_normalization_exact':True,'all_equalities_exact':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-sha256',required=True)
    args=parser.parse_args()
    source=Path(__file__)
    imported=source.with_name('a4reg_exact_check.py')
    before=digest(source)
    assert before==args.source_sha256
    assert digest(imported)==IMPORTED_SHA
    spec=importlib.util.spec_from_file_location('frozen_a4reg',imported)
    old=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    started=time.monotonic()
    results=[check(n,old) for n in range(1,7)]
    assert digest(source)==before and digest(imported)==IMPORTED_SHA
    import flint
    print(json.dumps({'scope':'finite n=1,...,6 complementary vertical-edge points; no absolute-value gap sum or asymptotic/global assertion',
      'python':platform.python_version(),'sympy':sp.__version__,'ground_types':GROUND_TYPES,
      'python_flint':flint.__version__,'FLINT':flint.__FLINT_VERSION__,
      'source_sha256_before':before,'source_sha256_after':digest(source),
      'imported_source_sha256_before':IMPORTED_SHA,'imported_source_sha256_after':digest(imported),
      'elapsed_seconds':round(time.monotonic()-started,6),'results':results},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
