"""Auditor-independent exact mixed-input induced condition for the Krawtchouk
p1=2/5,p2=1/2 family in z=2k/M-1 (node scale 1, relative weights), via dual numbers."""
import sys
from fractions import Fraction as Fr
from math import comb
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kraw_exact as K

def nn_dual(M, dirn):
    # dirn: (kind, index) ; kind 'x','w1','w2'
    z = [Fr(2*k, M) - 1 for k in range(M+1)]
    def w(p, s):
        return [K.D(Fr(comb(M,k))*p**k*(1-p)**(M-k), (Fr(comb(M,k))*p**k*(1-p)**(M-k)) if dirn==(s,k) else 0) for k in range(M+1)]
    w1, w2 = w(Fr(2,5),'w1'), w(Fr(1,2),'w2')
    nodes = [K.D(z[k], 1 if dirn==('x',k) else 0) for k in range(M+1)]
    return nodes, w1, w2

class DN(K.D):
    pass

def pw(d, e):
    r = K.D(1)
    for _ in range(e): r = r*d
    return r

def mop(nodes, w1, w2, n, m):
    t = n+m
    if t == 0: return [K.D(1)]
    rows, rhs = [], []
    for ws, cnt in ((w1,n),(w2,m)):
        for i in range(cnt):
            mom = [sum((ws[l]*pw(nodes[l], i+j) for l in range(len(nodes))), K.D(0)) for j in range(t+1)]
            rows.append(mom[:t]); rhs.append(-mom[t])
    return K.solve(rows, rhs) + [K.D(1)]

K.mop = mop
M = int(sys.argv[1]); N = M+1
cols = [(s,k) for s in ('x','w1','w2') for k in range(M+1)]
J = {}
base = None
for c in cols:
    nodes, w1, w2 = nn_dual(M, c)
    co = K.nn_coeffs(nodes, w1, w2, M)
    for nu, r in co.items():
        for key, v in (('a1', r[('a',1,1)]), ('a2', r[('a',2,1)]), ('b1', r[('b',1)]), ('b2', r[('b',2)])):
            J.setdefault((nu,key), {})[c] = v.b
            if base is None or True:
                J[(nu,key)]['val'] = v.a
A = {f: max(abs(J[(nu,g)]['val']) for (nu,g) in J if g==f) for f in ('a1','a2','b1','b2')}
kap = max(sum(abs(J[row][c]) for c in cols)/A[row[1]] for row in J)
print(N, kap, float(kap))
