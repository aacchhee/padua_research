"""Independent exact forward evaluation of the proposed T209 order.

No developer/reviewer imports. Use maximal windows (ALL predecessors), which
dominate every W/L subset under union-only support propagation. Thus the finite
checks test arbitrary preceding-column windows without random sampling.
The all-n conclusion is from the report's reconstruction, not enumeration.
"""
from itertools import product
import json


def indices(n):
    ix = [(s, j) for s in range(n + 1) for j in range(s + 1)]
    return ix, {v: k for k, v in enumerate(ix)}


def condition(ops, n):
    return all(ops[s+1, j + (ops[s,j] == 'Y')] == ops[s,j]
               for s in range(1, n) for j in range(s+1))


def staircase(ops, n):
    boundary = []
    for s in range(1, n+1):
        row = [ops[s,j] for j in range(s+1)]
        a = row.count('X') - 1
        if row != ['X']*(a+1) + ['Y']*(s-a):
            return False
        boundary.append(a)
    return boundary[0] == 0 and all(b-a in (0,1) for a,b in zip(boundary,boundary[1:]))


def forward(ops, n):
    ix, pos = indices(n)
    supports = {}
    deps = 0
    def obtain(A, m):
        nonlocal deps
        deps += 1
        assert (A,m) in supports, ('unavailable dependency', A, ix[m])
        return supports[A,m]
    for s in range(n):
        # All formed columns at this degree are data, and can include every
        # predecessor of their child plus the child itself.
        unformed = {'X': [], 'Y': []}
        for j in range(s+1):
            m = pos[s,j]
            for A in 'XY':
                c = pos[s+1,j+(A == 'Y')]
                if ops[ix[c]] == A:
                    supports[A,m] = (1 << (c+1)) - 1
                else:
                    unformed[A].append(m)
        for A in 'YX':
            for m in unformed[A]:
                _, j = ix[m]
                B = ops[s,j]
                assert B != A
                p = pos[s-1, j-(B == 'Y')]
                src = obtain(A,p)
                ans = 0
                while src:
                    bit = src & -src
                    ans |= obtain(B, bit.bit_length()-1)
                    src -= bit
                for l in range(m):
                    ans |= obtain(A,l)
                supports[A,m] = ans
        for j in range(s+1):
            for A in 'XY':
                # All permitted indices form a prefix in graded order.
                upper = pos[s+1,j+(A == 'Y')]
                assert supports[A,pos[s,j]] < (1 << (upper+1))
    assert len(supports) == 2*pos[n,0]
    return deps


for n in range(1,7):
    interior = [(s,j) for s in range(2,n+1) for j in range(1,s)]
    fixed = {(s,0):'X' for s in range(1,n+1)} | {(s,s):'Y' for s in range(1,n+1)}
    count = hits = deps = 0
    for choices in product('XY',repeat=len(interior)):
        ops = fixed | dict(zip(interior,choices))
        c = condition(ops,n)
        assert c == staircase(ops,n)
        count += 1
        if c:
            hits += 1
            deps += forward(ops,n)
    assert hits == 2**(n-1)
    print(json.dumps(dict(mode='all_selections_maximal_windows', n=n, selections=count,
                         satisfying_C=hits, dependencies_verified=deps)), flush=True)

for n in range(7,15):
    count = deps = 0
    for steps in product((0,1),repeat=n-1):
        b = 0
        ops = {(1,0):'X',(1,1):'Y'}
        for s, step in enumerate(steps,2):
            b += step
            ops.update({(s,j):('X' if j <= b else 'Y') for j in range(s+1)})
        assert condition(ops,n)
        deps += forward(ops,n)
        count += 1
    print(json.dumps(dict(mode='all_staircases_maximal_windows',n=n,selections=count,
                         dependencies_verified=deps)), flush=True)
