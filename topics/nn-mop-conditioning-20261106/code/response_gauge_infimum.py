#!/usr/bin/env python3
"""Exact finite dominance check; analytic tails are in response-gauge-infimum.md.

No imported repository arithmetic. Coordinates are normalized x=2k/M-1;
weights are relative, nodes have one of the three stated absolute scales.
A single terminal b2 row bounds the whole b condition. For fixed masses,
the exact weighted-median support is computed separately for each measure.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path
import platform


def solve(matrix, rhs):
    a = [list(row) + [v] for row, v in zip(matrix, rhs)]
    for j in range(len(a)):
        pivot = next(i for i in range(j, len(a)) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [v / scale for v in a[j]]
        for i in range(len(a)):
            if i != j and a[i][j]:
                scale = a[i][j]
                a[i] = [v - scale * u for v, u in zip(a[i], a[j])]
    return [row[-1] for row in a]


def evaluate(c, x):
    value = Q(0)
    for a in reversed(c):
        value = value * x + a
    return value


def derivative(c):
    return [i * c[i] for i in range(1, len(c))]


def poch(a, n):
    return prod((a + i for i in range(n)), start=Q(1))


def weights(family, M):
    if family == 'krawtchouk':
        return [[Q(comb(M, k)) * p**k * (1-p)**(M-k)
                 for k in range(M+1)] for p in (Q(2, 5), Q(1, 2))]
    return [[poch(alpha+1, k) / factorial(k) * (M-k+1)
             / (poch(alpha+3, M) / factorial(M))
             for k in range(M+1)] for alpha in (Q(1), Q(3, 2))]


def tau_integer(M, n, m):
    t = n + m
    if t == M + 1:
        return -Q(M*(M+1), 2)
    r = ((t+Q(2)) / (t+n+Q(2))
         * (t+Q(5, 2)) / (t+m+Q(5, 2)))
    return -Q(t*(t-1), 2) + (M-t+1) * (1-(t+1)*r)


def b2_scale(family, M):
    if family == 'krawtchouk':
        return Q(1, 5)
    return max(abs(2*(tau_integer(M,n,t-n)
                      - tau_integer(M,n,t-n+1))/M-1)
               for t in range(M+1) for n in range(t+1))


def weight_support(g, w, fixed_mass):
    if not fixed_mass:
        return sum(weight*abs(value) for value, weight in zip(g, w))
    ordered = sorted(zip(g, w))
    total = sum(w)
    partial = Q(0)
    for median, weight in ordered:
        partial += weight
        if 2 * partial >= total:
            return sum(weight*abs(value-median)
                       for value, weight in zip(g, w))
    raise AssertionError('missing weighted median')


def terminal_row(x, w):
    M = len(x)-1
    n, m = (M+1)//2, M//2
    tests = [(0,j) for j in range(n)] + [(1,j) for j in range(m)]
    mu = [[sum(weight*node**r for node,weight in zip(x,row))
           for r in range(2*M+1)] for row in w]
    matrix = [[mu[s][j+r] for r in range(M)] for s,j in tests]
    c = solve(matrix, [-mu[s][j+M] for s,j in tests]) + [Q(1)]
    adjoint = solve([list(col) for col in zip(*matrix)],
                    [Q(int(j == M-1)) for j in range(M)])
    # L_s(x)=sum_{test rows from s} lambda_(s,j) x^j.
    dual = [[Q(0)]*M for _ in range(2)]
    for coefficient, (s,j) in zip(adjoint, tests):
        dual[s][j] = coefficient
    gx = []
    gw = [[], []]
    for l, node in enumerate(x):
        p, dp = evaluate(c,node), evaluate(derivative(c),node)
        total = Q(0)
        for s in range(2):
            L = evaluate(dual[s],node)
            dL = evaluate(derivative(dual[s]),node)
            total += w[s][l] * (dL*p + L*dp)
            gw[s].append(-L*p)
        gx.append(1-total)  # tau_support=-sum x_l
    # Translation covariance and both mass-null directions are exact guards.
    assert sum(gx) == 1
    assert all(sum(a*b for a,b in zip(row,weight)) == 0
               for row,weight in zip(gw,w))
    return gx, gw, c


def variance_row(x, w):
    mu = sum(a*b for a,b in zip(x,w))
    v = sum(weight*(node-mu)**2 for node,weight in zip(x,w))
    return v, [2*weight*(node-mu) for node,weight in zip(x,w)], [
        (node-mu)**2-v for node in x]


def case(family,N):
    M=N-1
    x=[Q(2*k,M)-1 for k in range(N)]
    w=weights(family,M)
    assert all(sum(row)==1 and min(row)>0 for row in w)
    gx,gw,c=terminal_row(x,w)
    assert c[-2] == (Q(2,M)*tau_integer(M,(M+1)//2,M//2)+M
                     if family=='hahn' else c[-2])
    sb=b2_scale(family,M)
    variants=[]
    exact_payload=[]
    for model in ('mixed','componentwise','spacing'):
        sx=([Q(1)]*N if model=='mixed' else
            [abs(z) for z in x] if model=='componentwise' else [Q(2,M)]*N)
        for mass in (False,True):
            b_support=sum(abs(a)*b for a,b in zip(gx,sx)) + sum(
                weight_support(g,w_s,mass) for g,w_s in zip(gw,w))
            b_lower=b_support/sb
            r=[]
            for w_s in w:
                v,vx,vw=variance_row(x,w_s)
                r.append((sum(abs(a)*b for a,b in zip(vx,sx))
                          +weight_support(vw,w_s,mass))/v)
            assert b_lower >= max(r), (family,N,model,mass,b_lower,r)
            variants.append({'model':model,'fixed_mass':mass,'pass':True})
            exact_payload.append([model,mass,str(b_lower),*[str(a) for a in r]])
    # Normalized Hahn polynomial's subleading coefficient check above
    # is independent of its derivative evaluation.
    canonical=json.dumps(exact_payload,separators=(',',':')).encode()
    return {'family':family,'N':N,'variants':len(variants),'all_pass':True,
            'exact_comparisons_sha256':hashlib.sha256(canonical).hexdigest(),
            'smallest_dominance_ratio':str(min(Q(row[2])/max(Q(row[3]),Q(row[4]))
                                               for row in exact_payload))}


def main():
    # Hahn M=1..13 is the entire finite obligation, because the analytic
    # fixed-mass tail starts M=14; the unrestricted tail starts M=13.
    rows=[case('hahn',N) for N in range(2,15)]
    # Krawtchouk is analytic for M>=2; M=1 spacing needs its exact row.
    rows += [case('krawtchouk',N) for N in (2,4,6)]
    output={'schema':1,'purpose':'finite dominance obligation; not a floating fit',
            'rules_source':'3d5b29d7aa8c1274793139d7040695035e1bda22',
            'python':platform.python_version(),'arithmetic':'fractions.Fraction',
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks':len(rows)*6,'all_pass':True,'rows':rows,
            'independent_rerun':'separate execution required; not self-certified'}
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
