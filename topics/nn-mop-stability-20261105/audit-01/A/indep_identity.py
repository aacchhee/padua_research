#!/usr/bin/env python3
"""Exact test of the determinant identity behind the D1-04 converse:
   det M_(eta+e1+e2) * det M_eta = +- d_eta * det M_(eta+e1) * det M_(eta+e2),
with d_eta = t_(eta+e1) - t_(eta+e2) from defining-moment solves (PD-T286).
Also a planted-failure test: choose w2 so that one mixed det vanishes while all
lower degrees are normal, and confirm the computed d at eta is 0 there.
No developer code imported."""
import random, json, sys
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from indep_hahn import frac_solve, hahn_inputs


def data(x, w, N):
    mu = [[sum(ws[l]*x[l]**r for l in range(len(x))) for r in range(2*N+1)] for ws in w]
    det, P = {(0, 0): F(1)}, {(0, 0): [F(1)]}
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            rows = [(0, i) for i in range(n)]+[(1, i) for i in range(m)]
            d, c = frac_solve([[mu[s][i+j] for j in range(k)] for s, i in rows], [-mu[s][i+k] for s, i in rows])
            det[n, m] = d
            P[n, m] = None if c is None else c+[F(1)]
    return det, P


def t(P, nu):
    return P[nu][-2] if sum(nu) else F(0)


def check(x, w, N, label):
    det, P = data(x, w, N)
    signs, tested = set(), 0
    for (n, m), dv in det.items():
        if n and m:
            eta = (n-1, m-1)
            if any(P[q] is None for q in (eta, (n, m-1), (n-1, m))) or det[eta] == 0:
                continue
            d = t(P, (n, m-1))-t(P, (n-1, m))
            lhs = dv*det[eta]
            rhs = d*det[n, m-1]*det[n-1, m]
            assert abs(lhs) == abs(rhs), (label, n, m)
            signs.add((n, m, 1 if lhs == rhs else -1) if lhs != 0 else (n, m, 0))
            tested += 1
    return dict(label=label, N=N, tested=tested, sign_pattern=sorted(signs))


random.seed(20261106)
out = []
for N in (4, 5, 6, 7):
    x = sorted(random.sample(range(-50, 51), N))
    x = [F(v, 50) for v in x]
    w = [[F(random.randint(1, 30), random.randint(1, 30)) for _ in range(N)] for _ in range(2)]
    out.append(check(x, w, N, 'random'))
for N in (4, 8, 12):
    x, w = hahn_inputs(N)
    out.append(check(x, w, N, 'hahn'))
# planted failure: N=4 nodes, w1 fixed, w2 = w1 * (1 + u*l^2 ... ) choose u so that det M_(1,2)=0?
# simpler exact construction: det M_(1,1)=0 iff equal means; choose w2 with mean equal mean of w1
x = [F(v) for v in (0, 1, 2, 3)]
w1 = [F(1), F(2), F(3), F(4)]
w2 = [F(4), F(1), F(1), F(4)]          # mean 1.5? compute and adjust
m1 = sum(a*b for a, b in zip(w1, x))/sum(w1)
# adjust w2 so its mean equals m1: w2 = (a, 1, 1, c) solve with c free
a = F(4)
# mean2 = (0*a + 1 + 2 + 3c)/(a+2+c) = m1 -> 3 + 3c = m1(a+2+c)
c = (m1*(a+2)-3)/(3-m1)
w2 = [a, F(1), F(1), c]
assert all(v > 0 for v in w2)
det, P = data(x, [w1, w2], 4)
d00 = t(P, (1, 0))-t(P, (0, 1))
out.append(dict(label='planted M_(1,1) singular', det11=str(det[1, 1]), d00=str(d00)))
print(json.dumps(out, indent=1))
