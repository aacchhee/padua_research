#!/usr/bin/env python3
"""Exact rational group-algebra checks for the A1 reflection identity.

Cos(q*pi) is represented by (z^e+z^-e)/2 with z=exp(i*pi/L).
All operations have Fraction coefficients modulo z^(2L)-1; equality in
this ring implies equality on the relevant root of unity. No float signs
or division by a cosine difference occur. These are verification checks
of the analytic proof, not finite certificates of a maximum.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import lcm
import json


def add(*polys):
    out = defaultdict(Q)
    for p in polys:
        for k, v in p.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q, order):
    out = defaultdict(Q)
    for i, a in p.items():
        for j, b in q.items():
            out[(i+j) % order] += a*b
    return {k: v for k, v in out.items() if v}


def cosine(e, order):
    return add({e % order: Q(1, 2)}, {(-e) % order: Q(1, 2)})


def kernel(n, u, v, order):
    out = {}
    for a in range(n+1):
        for b in range(n+1-a):
            c = (1 if a == 0 else 2)*(1 if b == 0 else 2)
            if (a, b) == (n, 0):
                c = 1
            out = add(out, scale(mul(cosine(a*u, order),
                                    cosine(b*v, order), order), c))
    return out


def direct_cardinal(n, theta, phi, aj, bk, weight, order):
    out = {}
    for a in range(n+1):
        for b in range(n+1-a):
            c = (1 if a == 0 else 2)*(1 if b == 0 else 2)
            if (a, b) == (n, 0):
                c = 1
            p = mul(cosine(a*theta, order), cosine(a*aj, order), order)
            p = mul(p, cosine(b*phi, order), order)
            p = mul(p, cosine(b*bk, order), order)
            out = add(out, scale(p, c*weight))
    return out


def endpoint(i, last):
    return Q(1, 2) if i in (0, last) else Q(1)


def collision_value(n, exponent, order):
    # T'_k(cos u) = k U_(k-1)(cos u), with U a finite exponential sum.
    out = {}
    for k in (n, n+1):
        for j in range(k):
            out = add(out, {((k-1-2*j)*exponent) % order: Q(k)})
    return add(out, scale(cosine(n*exponent, order), -1))


def main():
    rows = []
    for n in range(3, 7):
        m, N = n+1, n*(n+1)
        L = 4*lcm(n, m)
        order = 2*L
        odd_centers = [(J, K) for J in range(n+1) for K in range(m+1)
                       if (J+K) % 2]
        points = set()
        for J, K in odd_centers:
            points.add((J*L//n, K*L//m, J, K))
            da = Q(1, 4) if J < n else Q(-1, 4)
            db = Q(-1, 4) if K else Q(1, 4)
            points.add((int((J+da)*L/n), int((K+db)*L/m), J, K))
        # All corners, edge midpoints, a centre, and diamond-boundary ties.
        for theta, phi in [(0,0),(0,L),(L,0),(L,L),
                           (0,L//2),(L,L//2),(L//2,0),(L//2,L),
                           (L//2,L//2),(0,0)]:
            J, K = min(odd_centers,
                       key=lambda p: abs(n*theta-Q(p[0]*L))
                                     +abs(m*phi-Q(p[1]*L)))
            points.add((theta, phi, J, K))
        cardinal_checks = 0
        for theta, phi, J, K in sorted(points):
            physical_multiset = defaultdict(Q)
            for j in range(n+1):
                for k in range(m+1):
                    if (j+k) % 2:
                        continue
                    aj, bk = j*L//n, k*L//m
                    w = 2*endpoint(j,n)*endpoint(k,m)/N
                    copies = []
                    for sigma in (-1,1):
                        for eta in (-1,1):
                            u, v = (theta+sigma*aj) % order, (phi+eta*bk) % order
                            physical_multiset[(u,v)] += w/4
                            copies.append(kernel(n,u,v,order))
                    reflected = scale(add(*copies), w/4)
                    direct = direct_cardinal(n,theta,phi,aj,bk,w,order)
                    assert direct == reflected, (n,theta,phi,j,k)
                    cardinal_checks += 1
            alpha_e, beta_e = theta-J*L//n, phi-K*L//m
            periodic_multiset = defaultdict(Q)
            for r in range(2*n):
                for s in range(2*m):
                    if (r+s) % 2:
                        periodic_multiset[((r*L//n+alpha_e) % order,
                                           (s*L//m+beta_e) % order)] += Q(1,2*N)
            assert physical_multiset == periodic_multiset, (n,theta,phi,J,K)
        # Collision identities checked before division and also at endpoints.
        for u in (0,L//4,L//2,L):
            assert kernel(n,u,u,order) == collision_value(n,u,order)
            assert kernel(n,u,-u,order) == collision_value(n,u,order)
        assert sum(kernel(n,0,0,order).values()) == 2*N
        # Every exponent is a multiple of L, so z^e=(-1)^(e/L).
        corner = kernel(n,L,L,order)
        assert all(e % L == 0 for e in corner)
        assert sum(c*(-1)**(e//L) for e,c in corner.items()) == (-1)**n*2*n
        # Exact zero G(0,pi), with no numerical sign decision.
        zero = kernel(n,0,L,order)
        value = sum(c * ((1,0,-1,0)[(e//(L//2)) % 4])
                    for e,c in zero.items())
        # Real evaluation here is exact: all exponents are multiples of L/2.
        assert all(e % (L//2) == 0 for e in zero)
        assert value == 0
        rows.append(dict(n=n,physical_points=len(points),
                         exact_cardinal_checks=cardinal_checks,
                         exact_weighted_multiset_checks=len(points),
                         collision_checks=8,zero_checks=1,accepted=True))
    print(json.dumps(dict(arithmetic="Fraction group algebra, no floating signs",
                          scope="identity verification only",rows=rows),indent=2))


if __name__ == "__main__":
    main()
