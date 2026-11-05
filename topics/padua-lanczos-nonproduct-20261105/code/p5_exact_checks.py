#!/usr/bin/env python3
"""Supplementary exact Padua checks; no all-degree computer-proof claim.

The finite dual calculation differentiates every full projection coefficient
in a monic gauge. It then compares its normal part with the frozen recurrence.
Small nodes use exact real radical fields, never floating cosines.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import sympy as S
from sympy.polys.domains import QQ


def run_order(m, dual):
    radicals = {2: (), 3: (S.sqrt(2),), 4: (S.sqrt(2), S.sqrt(5)),
                5: (S.sqrt(3), S.sqrt(5))}[m]
    K = QQ.algebraic_field(*radicals) if radicals else QQ
    zero, one = K.zero, K.one
    rat = lambda a, b=1: K.convert(S.Rational(a, b))
    nodes = [(j, k, K.from_sympy(S.cos(S.pi*j/m)),
              K.from_sympy(S.cos(S.pi*k/(m+1))),
              rat(2, m*(m+1)) * rat(1 if j in (0, m) else 2, 2)
              * rat(1 if k in (0, m+1) else 2, 2))
             for j in range(m+1) for k in range(m+2) if (j+k) % 2 == 0]
    M = len(nodes)
    xs, ys, weights = ([z[t] for z in nodes] for t in (2, 3, 4))
    assert M == (m+1)*(m+2)//2 and sum(weights, zero) == one

    def dot(v, w):
        return sum((a*b*c for a, b, c in zip(weights, v, w)), zero)

    def mul(v, w):
        return [a*b for a, b in zip(v, w)]

    def axpy(v, scalar, w):
        if scalar == zero:
            return v[:]
        return [a+scalar*b for a, b in zip(v, w)]

    def cheb(z, top):
        vals = [one]
        if top:
            vals.append(z)
        for a in range(2, top+1):
            vals.append(2*z*vals[-1]-vals[-2])
        return vals

    tx = [cheb(x, 2*m) for x in xs]
    ty = [cheb(y, 2*m) for y in ys]
    moment_checks = 0
    for a in range(2*m):
        for b in range(2*m-a):
            value = sum((w*txi[a]*tyi[b]
                         for w, txi, tyi in zip(weights, tx, ty)), zero)
            assert value == (one if a == b == 0 else zero)
            moment_checks += 1
    assert sum((w*t[2*m] for w, t in zip(weights, tx)), zero) == one

    s = m-1
    indices = [(d-b, b) for d in range(s+1) for b in range(d+1)]
    loc = {ab: h for h, ab in enumerate(indices)}
    N = len(indices)

    def monic(vals, a):
        return one if a == 0 else vals[a]*rat(1, 2**(a-1))

    B = [[monic(txi, a)*monic(tyi, b) for txi, tyi in zip(tx, ty)]
         for a, b in indices]
    D = [rat(1, 2**(2*a-1)) if a else one for a, _ in indices]
    for h, (_, b) in enumerate(indices):
        D[h] *= rat(1, 2**(2*b-1)) if b else one
    gram_checks = 0
    for h in range(N):
        for l in range(h+1):
            assert dot(B[h], B[l]) == (D[h] if l == h else zero)
            gram_checks += 1

    def normal(v):
        result = v[:]
        for b, d in zip(B, D):
            result = axpy(result, -dot(b, v)/d, b)
        return result

    e = [rat((-1)**z[0]) for z in nodes]
    assert dot(e, e) == one
    assert normal(e) == e
    dual_directions = 0
    rule_rows = []
    for rule in ('BJ', 'mirror'):
        parents, operators, alphas = [None], [None], [[]]
        creator_checks = 0
        for h, (a, b) in enumerate(indices[1:], 1):
            use_x = (b == 0) if rule == 'BJ' else (a > 0)
            p = loc[a-1, b] if use_x else loc[a, b-1]
            op = xs if use_x else ys
            z = mul(op, B[p])
            alpha = [dot(B[l], z)/D[l] for l in range(h)]
            result = z[:]
            for l in range(h):
                result = axpy(result, -alpha[l], B[l])
            assert result == B[h]
            parents.append(p)
            operators.append(op)
            alphas.append(alpha)
            creator_checks += 1

        def frozen(sources):
            result = [[zero]*M]
            for h in range(1, N):
                v = axpy(mul(operators[h], result[parents[h]]), one, sources[h])
                for l in range(h):
                    v = axpy(v, -alphas[h][l], result[l])
                result.append(v)
            return result

        # Source e at x1 has budget squared 2. The normalized readout after
        # dividing by its budget has squares 1,0,1,... on pure-x outputs.
        sources = [[zero]*M for _ in range(N)]
        sources[loc[1, 0]] = e[:]
        V = frozen(sources)
        source_scale_squared = dot(mul(xs, B[0]), mul(xs, B[0]))
        assert source_scale_squared == rat(1, 2)
        pure_x_squares = []
        for a in range(1, s+1):
            h = loc[a, 0]
            readout = dot(e, V[h])
            squared = readout**2*source_scale_squared/D[h]
            assert squared == (one if a % 2 else zero)
            pure_x_squares.append(int(squared == one))

        if dual:
            for h_source in range(1, N):
                for node_source in range(M):
                    sources = [[zero]*M for _ in range(N)]
                    sources[h_source][node_source] = one
                    V = frozen(sources)
                    deriv = [[zero]*M]
                    for h in range(1, N):
                        p, op = parents[h], operators[h]
                        z = mul(op, B[p])
                        dz = axpy(mul(op, deriv[p]), one, sources[h])
                        result = dz[:]
                        for l in range(h):
                            da = ((dot(deriv[l], z)+dot(B[l], dz))/D[l]
                                  - alphas[h][l]*2*dot(B[l], deriv[l])/D[l])
                            result = axpy(result, -da, B[l])
                            result = axpy(result, -alphas[h][l], deriv[l])
                        deriv.append(result)
                    for d, v in zip(deriv, V):
                        assert all(x == zero for x in normal(axpy(d, -one, v)))
                    dual_directions += 1

        rule_rows.append({'rule': rule, 'exact_creators': creator_checks,
                          'normal_x_readout_squares': pure_x_squares,
                          'lower_capacity_squared': (s+1)//2})

    return {'m': m, 'stage': s, 'nodes': M, 'columns': N,
            'normal_dimension': M-N, 'field': str(K),
            'exact_cubature_moments': moment_checks,
            'sharp_T_2m_failure': True, 'exact_gram_entries': gram_checks,
            'rules': rule_rows, 'dual_source_coordinate_directions': dual_directions}


def symbolic_checks():
    x = S.symbols('x')
    count = 0
    p = [S.Integer(1)] + [S.sqrt(2)*S.chebyshevt(a, x) for a in range(1, 9)]
    beta = [S.Integer(0), 1/S.sqrt(2)] + [S.Rational(1, 2)]*8
    for a in range(1, 9):
        low = beta[a-1]*p[a-2] if a >= 2 else 0
        assert S.expand(x*p[a-1]-low-beta[a]*p[a]) == 0
        count += 1
    for c in range(1, 9):
        values = {c-1: S.Integer(0)}
        for a in range(c, 9):
            value = S.sqrt(2)*S.chebyshevu(a-1, x) if c == 1 else 2*S.chebyshevu(a-c, x)
            if a == c:
                assert S.simplify(value-1/beta[c]) == 0
            else:
                low = beta[a-1]*values[a-2]
                assert S.expand(beta[a]*value-x*values[a-1]+low) == 0
            values[a] = value
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    rows = [run_order(m, dual=(m <= 3)) for m in (2, 3, 4, 5)]
    result = {'status': 'PASS supplementary exact finite checks',
              'scope': 'analytic theorem corroboration, not a finite proof reduction',
              'sympy_version': S.__version__,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'symbolic_univariate_identities_through_degree_8': symbolic_checks(),
              'orders': rows, 'elapsed_seconds': time.monotonic()-started}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
