#!/usr/bin/env python3
"""Supplementary (MEASURED-level, not proof) degree-12 end-to-end replay of the
PD-T138 declared scalar CGS2 implementation on rotQ24/BJ, perturbed by
w -> w(1+eps*delta) at EVERY scalar operation, with
  * the frozen L4 witness signs delta = s_i sign(g_90,h(z_i) m_hio) on the
    vector-operation channels of PD-T138's amplitude table, and
  * arbitrary fixed pseudo-random |delta|<=1 on all dot/norm/sqrt channels and
    on the second-pass matvec channels (claimed first-order normal-invisible).
Checks R*Qtilde/eps against Phi = R V D^{-1/2} built from the auditor's own exact
V, and the readout quotient ||Phi a||^2 for the committed 91-integer vector.
Arithmetic: Python decimal (libmpdec), independent of FLINT.
"""
import sys, json, time, random
from decimal import Decimal as Dm, getcontext
from fractions import Fraction as F
sys.path.insert(0, sys.argv[1]); import indep as I
sys.set_int_max_str_digits(0)
getcontext().prec = 70
EPS = Dm('1e-28')
t0 = time.time()
cert = json.load(open(sys.argv[2])); low = json.load(open(sys.argv[3]))
lrow = next(r for r in low['witnesses'] if r['set'] == 'rotated' and r['rule'] == 'bj')
s = lrow['node_signs']; M = 625
coords = I.nodes(); b, d, rec, mono = I.basis('bj', coords)
# adjoint row y_h = g_{90,h}
y = [None] * 91; y[90] = I.V([1] * M, 1)
for h in range(89, 0, -1):
    terms = []; acc = None
    for k in range(h + 1, 91):
        ax, p, alpha = rec[k]
        if alpha[h]: terms.append((-alpha[h], y[k]))
        if p == h:
            pk = y[k].pmul(coords[ax]); acc = pk if acc is None else acc + pk
    lc = I.lincomb(terms); y[h] = lc if acc is None else acc + lc
sg = lambda x: (x > 0) - (x < 0)
def D(fr): return Dm(fr.numerator) / Dm(fr.denominator)
def Dv(v): return [Dm(x) / Dm(v.d) for x in v.n]
X = [Dv(c) for c in coords]
# exact amplitude signs for the witness channels
W = {}
for k in range(1, 91):
    ax, p, alpha = rec[k]
    gk = [s[i] * sg(y[k].n[i]) for i in range(M)]
    u = b[p].pmul(coords[ax])
    mult = [gk[i] * sg(u.n[i]) for i in range(M)]
    bk = [gk[i] * sg(b[k].n[i]) for i in range(M)]
    prod = []; add = []; partial = None
    for l, a in enumerate(alpha):
        term = b[l].scale(-a)
        partial = term if partial is None else partial + term
        prod.append([gk[i] * sg(term.n[i]) for i in range(M)])
        add.append([gk[i] * sg(partial.n[i]) for i in range(M)] if l >= 1 else None)
    W[k] = (mult, prod, add, bk)
print(json.dumps({'event': 'signs_ready', 'sec': time.time() - t0}), flush=True)
rng = random.Random(20261105)
POOL = [Dm(repr(rng.uniform(-1, 1))) for _ in range(10007)]
ctr = [0]
def pz():
    ctr[0] += 1; return POOL[ctr[0] % 10007]
one = Dm(1)
def R(w): return w * (one + EPS * pz())          # random kernel-channel rounding
def Rw(w, dl): return w * (one + EPS * dl) if dl else w   # witness channel
def Dot(qa, qb):
    acc = R(qa[0] * qb[0])
    for i in range(1, M): acc = R(acc + R(qa[i] * qb[i]))
    return acc
qt = [[one / Dm(25)] * M]                        # exact q_0 = 1/sqrt(625)
for k in range(1, 91):
    ax, p, alpha = rec[k]; mult, prod, add, bk = W[k]
    a = [Rw(X[ax][i] * qt[p][i], mult[i]) for i in range(M)]
    c = [Dot(qt[l], a) for l in range(k)]
    r = []
    for i in range(M):
        acc = Rw(qt[0][i] * c[0], prod[0][i])
        for l in range(1, k):
            acc = Rw(acc + Rw(qt[l][i] * c[l], prod[l][i]), add[l][i])
        r.append(Rw(a[i] - acc, bk[i]))
    e = [Dot(qt[l], r) for l in range(k)]
    z = []
    for i in range(M):
        acc = R(qt[0][i] * e[0])
        for l in range(1, k): acc = R(acc + R(qt[l][i] * e[l]))
        z.append(Rw(r[i] - acc, bk[i]))
    ss = R(z[0] * z[0])
    for i in range(1, M): ss = R(ss + R(z[i] * z[i]))
    beta = R(ss.sqrt())
    qt.append([Rw(z[i] / beta, bk[i]) for i in range(M)])
    if k % 10 == 0: print(json.dumps({'event': 'column', 'k': k, 'sec': time.time() - t0}), flush=True)
# normal projection with exact basis (in Decimal)
bD = [Dv(v) for v in b]; dD = [D(x) for x in d]
def proj(w):
    out = list(w)
    for bl, dl in zip(bD, dD):
        cf = sum((x * y_ for x, y_ in zip(bl, w)), Dm(0)) / dl
        out = [o - cf * x for o, x in zip(out, bl)]
    return out
bj = __import__('pickle').load(open(sys.argv[4], 'rb'))
Vex = [I.V(n, dd, reduce=False) for n, dd in bj['V']]
num_err = Dm(0); den_norm = Dm(0); colrel = []
P = []; Phi = []
for k in range(91):
    pk = [x / EPS for x in proj(qt[k])]
    fk = [x / D(dk).sqrt() for x, dk in zip(proj(Dv(Vex[k])), [d[k]] * M)]
    P.append(pk); Phi.append(fk)
    e2 = sum(((u - v) ** 2 for u, v in zip(pk, fk)), Dm(0)); n2 = sum((v * v for v in fk), Dm(0))
    num_err += e2; den_norm += n2
    if n2 > 0: colrel.append(float((e2 / n2).sqrt()))
t = cert['lower_monic_coefficients']
tD = sum((D(dk) * tk * tk for dk, tk in zip(d, t)), Dm(0))
aD = [D(dk).sqrt() * tk / tD.sqrt() for dk, tk in zip(d, t)]
Pa = [sum((aD[k] * P[k][i] for k in range(91) if t[k]), Dm(0)) for i in range(M)]
out = {'eps': str(EPS), 'prec': getcontext().prec, 'kernel_channel_draws': ctr[0],
       'frob_rel_err_RQtilde_over_eps_vs_Phi': float((num_err / den_norm).sqrt()),
       'max_col_rel_err': max(colrel), 'col90_sq_replay': float(sum((x * x for x in P[90]), Dm(0))),
       'readout_sq_replay': float(sum((x * x for x in Pa), Dm(0))),
       'L': cert['lower_integer_floor_L'], 'seconds': time.time() - t0}
print(json.dumps(out), flush=True)
json.dump(out, open(sys.argv[5], 'w'), indent=1)
