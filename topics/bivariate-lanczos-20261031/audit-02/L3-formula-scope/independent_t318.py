"""Independent exact sanity checks of T318; no developer/reviewer imports.

Use fixed monomials, G,X,Y, and F=X G^-1 Y-Y G^-1 X.  If C is the
orthonormal coefficient matrix, [Hx,Hy]=C.T F C.  At a square measure
F=0, so basis derivatives cancel and d[Hx,Hy]=C.T dF C.  All comparisons
below are rational, before the invertible orthonormal congruence.
These finite checks support, but do not replace, the all-n analytic proof.
"""
import sys
import sympy as sp
from sympy.polys.matrices import DomainMatrix

Q = sp.Rational


def rank(A):
    return DomainMatrix.from_Matrix(A).rank()


def exps(d):
    return [(i, k-i) for k in range(d+1) for i in range(k+1)]


def add(p, q, scale=1):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + scale*c
    return {e: c for e, c in r.items() if c}


def mul(p, q):
    r = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            e = (i+k, j+l)
            r[e] = r.get(e, 0) + a*b
    return {e: c for e, c in r.items() if c}


def val(p, z):
    return sum(c*z[0]**i*z[1]**j for (i, j), c in p.items())


def grad(p, z, k):
    return sum(c*e[k]*z[0]**(e[0]-(k == 0))*z[1]**(e[1]-(k == 1))
               for e, c in p.items() if e[k])


def matrices(mom, mons):
    return [sp.Matrix([[mom[a[0]+b[0]+dx, a[1]+b[1]+dy]
                        for b in mons] for a in mons])
            for dx, dy in [(0, 0), (1, 0), (0, 1)]]


def remainders(G, X, Y, mons):
    W = G.inv()
    ans = []
    for shift, B in [((1, 0), X), ((0, 1), Y)]:
        coeff = W*B
        ans.append([add({(e[0]+shift[0], e[1]+shift[1]): 1},
                        {f: coeff[i, a] for i, f in enumerate(mons)}, -1)
                    for a, e in enumerate(mons)])
    return ans


def exact_case(n):
    mons, moments = exps(n), exps(2*n+1)
    # Invertible affine image of a triangular rational lattice; weights have
    # mass N(N+1)/2, so this deliberately tests nonunit-mass conventions.
    nodes = [(Q(i, n)+Q(j, 3*n)+Q(1, 5),
              Q(j, n)-Q(i, 4*n)-Q(1, 7)) for i, j in mons]
    weights = list(range(1, len(nodes)+1))
    V = sp.Matrix([[val({e: 1}, z) for e in mons] for z in nodes])
    assert V.det() != 0
    mom = {e: sum(w*val({e: 1}, z) for w, z in zip(weights, nodes))
           for e in moments}
    G, X, Y = matrices(mom, mons)
    W = G.inv()
    assert X*W*Y-Y*W*X == sp.zeros(len(mons))
    Rx, Ry = remainders(G, X, Y, mons)
    for r in Rx+Ry:
        assert all(val(r, z) == 0 for z in nodes)
    lo = n*(n+1)//2
    pairs = [(a, b) for a in range(lo, len(mons)) for b in range(a+1, len(mons))]
    S = [add(mul(Ry[a], Rx[b]), mul(Rx[a], Ry[b]), -1) for a, b in pairs]
    for s in S:
        assert max(map(sum, s), default=0) <= 2*n+1
        for z in nodes:
            assert val(s, z) == grad(s, z, 0) == grad(s, z, 1) == 0
    # Exact derivative in EVERY moment direction, including mass.  No finite
    # differences, Cholesky, or developer remainder implementation is used.
    derivative_columns = []
    for e in moments:
        E = {f: int(f == e) for f in moments}
        dG, dX, dY = matrices(E, mons)
        dF = dX*W*Y + X*W*dY-X*W*dG*W*Y-dY*W*X-Y*W*dX+Y*W*dG*W*X
        assert dF + dF.T == sp.zeros(len(mons))
        assert dF[:lo, :] == sp.zeros(lo, len(mons))
        column = [dF[a, b] for a, b in pairs]
        assert column == [s.get(e, 0) for s in S]
        derivative_columns.append(column)
    derivative = sp.Matrix(derivative_columns).T
    # Exact mass-direction cancellation.  Normalization L -> L/m changes
    # fixed-basis dF by 1/m, and normalized orthonormal congruence by m.
    assert derivative*sp.Matrix([mom[e] for e in moments]) == sp.zeros(len(pairs), 1)
    E = {e: Q((i % 7)-3, 13) for i, e in enumerate(moments)}
    dG, dX, dY = matrices(E, mons)
    dF = dX*W*Y + X*W*dY-X*W*dG*W*Y-dY*W*X-Y*W*dX+Y*W*dG*W*X
    mass = mom[0, 0]
    normmom = {e: mom[e]/mass for e in moments}
    normE = {e: (E[e]-E[0, 0]*mom[e]/mass)/mass for e in moments}
    Gn, Xn, Yn = matrices(normmom, mons)
    Wn = Gn.inv()
    A, B, C = matrices(normE, mons)
    dFn = B*Wn*Yn + Xn*Wn*C-Xn*Wn*A*Wn*Yn-C*Wn*Xn-Yn*Wn*B+Yn*Wn*A*Wn*Xn
    assert mass*dFn == dF
    # G stays positive definite when only highest-degree moments change.
    # This makes a noncommuting functional, hence not representable by this
    # same square node set; no unsupported global nonmeasure assertion.
    modified = dict(mom)
    for e in moments:
        if sum(e) == 2*n+1:
            modified[e] += Q(e[0]+1, 17)
    G2, X2, Y2 = matrices(modified, mons)
    assert G2 == G
    F2 = X2*W*Y2-Y2*W*X2
    assert F2 != sp.zeros(len(mons))
    rx, ry = remainders(G2, X2, Y2, mons)
    for a, b in pairs:
        s = add(mul(ry[a], rx[b]), mul(rx[a], ry[b]), -1)
        assert max(map(sum, s), default=0) <= 2*n+1
        assert sum(c*modified[e] for e, c in s.items()) == F2[a, b]
    J = sp.Matrix([[val({e: 1}, z) for e in moments] for z in nodes]
                  + [[grad({e: 1}, z, k) for e in moments] for z in nodes for k in range(2)])
    q = []
    for j in range(n+2):
        f = {(j, n+1-j): 1}
        coeff = V.inv()*sp.Matrix([val(f, z) for z in nodes])
        q.append(add(f, {e: coeff[a] for a, e in enumerate(mons)}, -1))
    Frows = [add(mul(q[i], q[j+1]), mul(q[i+1], q[j]), -1)
             for i in range(n+1) for j in range(i+1, n+1)]
    FM = sp.Matrix([[p.get(e, 0) for e in moments] for p in Frows])
    rankD, rankF = rank(derivative), rank(FM)
    assert rankD == rankF
    assert rank(derivative.col_join(FM)) == rankF
    print(f'n={n}: N={len(nodes)}, mass={mass}, derivative {derivative.rows}x{derivative.cols}; '
          f'exact sign/all directions/basis cancellation/normalization/general-L identity PASS; '
          f'rank dF=dim F={rankF}, dim S1={len(moments)-rank(J)}', flush=True)


def hankel_basis(n):
    # Exact finite confirmation of the all-n triangular-basis argument,
    # including diagonal factors from sym(A)=(A+A.T)/2.
    cols = []
    for i in range(n+1):
        for j in range(i+1, n+1):
            C = sp.zeros(n+2)
            C[i, j+1] += Q(1, 2)
            C[j+1, i] += Q(1, 2)
            C[i+1, j] -= Q(1, 2)
            C[j, i+1] -= Q(1, 2)
            assert all(sum(C[a, b] for a in range(n+2) for b in range(n+2)
                           if a+b == m) == 0 for m in range(2*n+3))
            cols.append([C[a, b] for a in range(n+2) for b in range(a, n+2)])
    r = rank(sp.Matrix(cols))
    assert r == n*(n+1)//2
    print(f'n={n}: C(e_i,e_j) exact independent Hankel-orthogonal basis rank={r} PASS', flush=True)


if __name__ == '__main__':
    print('Python', sys.version.split()[0], 'SymPy', sp.__version__, flush=True)
    for n in range(1, 4):
        exact_case(n)
    for n in range(1, 9):
        hankel_basis(n)
    print('ALL EXACT ASSERTIONS PASS', flush=True)
