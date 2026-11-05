"""L6 auditor (Claude) independent replay of the l6-02 n1 contract.

Written from the contract text (theory/l6-02-actual-n1-implementation-contract.md),
not from l6_n1_producer.py / l6_n1_independent.py. Host binary64 Python floats
perform the computation; every primitive is re-verified against an exact
Fraction round-to-nearest-even implemented here by a different algorithm
(exponent/quantum scaling, not binary search over encodings).
Then compares with the committed packed trace and exact-analysis evidence.
Usage: python3 -I -B my_replay.py <trace.json> <analysis.json> <receipt.json>
"""
import json, math, struct, sys
from fractions import Fraction as F

def bits_of(x): return struct.unpack('>Q', struct.pack('>d', x))[0]
def w(x): return f'{bits_of(x):016x}'
def exact(x): return F(*x.as_integer_ratio())

def rn_fraction(x):
    """Exact RN-even of a nonzero rational to binary64 (finite, no overflow)."""
    assert x != 0
    neg = x < 0; a = abs(x)
    # floor(log2 a)
    E = a.numerator.bit_length() - a.denominator.bit_length()
    if F(2) ** E > a: E -= 1
    assert F(2) ** E <= a < F(2) ** (E + 1)
    qexp = max(E, -1022) - 52          # quantum exponent (subnormals: -1074)
    quantum = F(2) ** qexp
    q = a / quantum
    n = q.numerator // q.denominator; rem = q - n
    if rem > F(1, 2) or (rem == F(1, 2) and n % 2 == 1): n += 1
    val = n * quantum
    assert val < F(2) ** 1024
    f = float(val)                      # exact: val is representable
    assert exact(f) == val
    return -f if neg else f

def rn_sqrt(x):
    """RN of sqrt(x) for a nonnegative double x, certified via floor/ceil isqrt."""
    a = exact(x)
    if a == 0: return x                 # sqrt(+-0) = +-0
    K = 400
    num = (a.numerator << (2 * K)) // a.denominator
    lo = F(math.isqrt(num), 1 << K)
    hi = lo + F(1, 1 << K)
    assert lo * lo <= a <= hi * hi
    r1, r2 = rn_fraction(lo), rn_fraction(hi)
    assert r1 == r2, 'sqrt rounding not decided at K bits'
    return r1

def zero_result(op, x, y=None):
    sx = bits_of(x) >> 63
    if op == 'sqrt': return -0.0 if sx else 0.0
    sy = bits_of(y) >> 63
    if op in ('mul', 'div'): return -0.0 if sx ^ sy else 0.0
    if op == 'add': return -0.0 if (sx and sy) else 0.0
    if op == 'sub': return -0.0 if (sx and not sy) else 0.0

TRACE = []
STATES = []
def P(op, x, y=None):
    if op == 'add': host = x + y; ex = exact(x) + exact(y)
    elif op == 'sub': host = x - y; ex = exact(x) - exact(y)
    elif op == 'mul': host = x * y; ex = exact(x) * exact(y)
    elif op == 'div': host = x / y; ex = exact(x) / exact(y)
    elif op == 'sqrt': host = math.sqrt(x); ex = exact(x)
    else: raise ValueError(op)
    if op == 'sqrt': ref = rn_sqrt(x)
    elif ex == 0: ref = zero_result(op, x, y)
    else: ref = rn_fraction(ex)
    assert bits_of(host) == bits_of(ref), (op, w(x), host, ref)
    TRACE.append((op, [w(x)] if y is None else [w(x), w(y)], w(host), ex))
    return host

def S(label, v):
    enc = lambda z: [enc(t) for t in z] if isinstance(z, list) else w(z)
    STATES.append({'label': label, 'words': enc(v)})

# --- contract primitives (text of l6-02, section "Scalar primitives") ---
def DOT(v, u):
    s = 0.0
    for r in range(3):
        p = P('mul', v[r], u[r]); s = P('add', s, p)
    return s
def NORM(v): return P('sqrt', DOT(v, v))
def PROD(A, q): return [P('mul', A[r], q[r]) for r in range(3)]
def CGS2(v, qs, label):
    S(label + '.input', v); bs = []
    for ip in range(2):
        b = [DOT(qi, v) for qi in qs]
        new = []
        for r in range(3):
            s = 0.0
            for i, qi in enumerate(qs):
                p = P('mul', qi[r], b[i]); s = P('add', s, p)
            new.append(P('sub', v[r], s))
        S(label + '.b' + str(ip + 1), b); S(label + '.w' + str(ip + 1), new)
        bs.append(b); v = new
    h = [P('add', bs[0][i], bs[1][i]) for i in range(len(qs))]
    S(label + '.h', h)
    return v, h

Xd = [0.0, 1.0, 0.0]; Yd = [0.0, 0.0, 1.0]
S('Xdiag', Xd); S('Ydiag', Yd)
s3 = P('sqrt', 3.0); a = P('div', 1.0, s3); q0 = [a, a, a]
S('startup.s', s3); S('q0', q0)
v = PROD(Yd, q0); S('Yq0', v)
v, g = CGS2(v, [q0], 'q1.cgs'); beta1 = NORM(v); assert beta1 > 0
q1 = [P('div', z, beta1) for z in v]; S('q1.beta', beta1); S('q1.q', q1)
v = PROD(Xd, q0); S('Xq0', v)
v, h = CGS2(v, [q0, q1], 'q2.cgs'); beta2 = NORM(v); assert beta2 > 0
q2 = [P('div', z, beta2) for z in v]; S('q2.beta', beta2); S('q2.q', q2)
qs = [q0, q1, q2]
HXcols = [[h[0], h[1], beta2]]; term = {}
for j in (1, 2):
    v = PROD(Xd, qs[j]); S('Xq' + str(j), v)
    t, c = CGS2(v, qs, 'Xcol' + str(j)); HXcols.append(c); term['X' + str(j)] = t
v = PROD(Yd, q1); S('Yq1', v)
t, j1 = CGS2(v, qs, 'Ycol1'); term['Y1'] = t
j0 = [g[0], beta1, 0.0]
T = lambda m: [list(r) for r in zip(*m)]
Qf = T(qs); Hxf = T(HXcols)
S('Q', Qf); S('Hx', Hxf); S('j0', j0); S('j1', j1)

out = {'n_primitives': len(TRACE), 'n_states': len(STATES)}

# --- compare with committed trace ---
trace = json.load(open(sys.argv[1])); analysis = json.load(open(sys.argv[2])); rec = json.load(open(sys.argv[3]))
prims = trace['primitives']
assert len(prims) == len(TRACE)
for i, (p, m) in enumerate(zip(prims, TRACE)):
    assert p['seq'] == i and p['op'] == m[0] and p['args'] == m[1] and p['out'] == m[2], i
    assert F(p['exact']) == m[3], i
assert trace['states'] == STATES
out['trace_match'] = True
rw = rec['raw_words']
assert rw['Q'] == [[w(x) for x in r] for r in Qf] and rw['Hx'] == [[w(x) for x in r] for r in Hxf]
assert rw['j0'] == [w(x) for x in j0] and rw['j1'] == [w(x) for x in j1]
assert rw['terminals'] == {k: [w(x) for x in val] for k, val in term.items()}
out['receipt_raw_words_match'] = True
ops = {}
for m in TRACE: ops[m[0]] = ops.get(m[0], 0) + 1
out['op_counts'] = ops

# --- exact analysis ---
Q = [[exact(x) for x in r] for r in Qf]; Hx = [[exact(x) for x in r] for r in Hxf]
y0 = [exact(x) for x in j0]; y1 = [exact(x) for x in j1]
h0, h1, b2 = Hx[0][0], Hx[1][0], Hx[2][0]
def mm(A, B): return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
Hxy0 = [sum(Hx[i][k] * y0[k] for k in range(3)) for i in range(3)]
y2 = [(Hxy0[i] - h0 * y0[i] - h1 * y1[i]) / b2 for i in range(3)]
Hy = T([y0, y1, y2])
I3 = [[F(int(i == j)) for j in range(3)] for i in range(3)]
X = [[F(int(i == j == 1)) for j in range(3)] for i in range(3)]
Y = [[F(int(i == j == 2)) for j in range(3)] for i in range(3)]
Fx = sub(mm(X, Q), mm(Q, Hx)); Fy = sub(mm(Y, Q), mm(Q, Hy)); G = sub(mm(T(Q), Q), I3)
def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
detQ = det3(Q)
s = lambda A: [[str(x) for x in r] for r in A]
for key, val in [('Q', s(Q)), ('raw_Hx', s(Hx)), ('completed_Hy', s(Hy)), ('Fx', s(Fx)), ('Fy', s(Fy)), ('Gram_loss', s(G))]:
    assert analysis[key] == val, key
assert analysis['detQ'] == str(detQ) and analysis['C1_j2'] == [str(x) for x in y2]
assert analysis['omitted_Y_column'] == [str(Fy[i][2]) for i in range(3)]
out['analysis_match'] = True
out['detQ_nonzero'] = detQ != 0

# certified spectral quantities via exact characteristic polynomial + sympy real-root isolation
import sympy as sp
lam = sp.symbols('lam')
def eig_intervals(Sym):
    Ms = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in Sym])
    assert Ms == Ms.T
    poly = sp.Poly(Ms.charpoly(lam).as_expr(), lam)
    iv = poly.intervals(eps=sp.Rational(1, 2 ** 200))
    roots = []
    for (lo, hi), mult in iv:
        roots += [(F(int(sp.numer(lo)), int(sp.denom(lo))), F(int(sp.numer(hi)), int(sp.denom(hi))))] * mult
    assert len(roots) == 3
    return sorted(roots)
u = F(1, 2 ** 53)
gev = eig_intervals(G)                       # eigenvalues of Gram loss
gnorm_hi = max(max(abs(lo), abs(hi)) for lo, hi in gev)
qtq = eig_intervals(mm(T(Q), Q))
Qn2 = qtq[-1]; sig2 = qtq[0]                 # ||Q||^2, sigma_min^2 intervals
fx2 = eig_intervals(mm(T(Fx), Fx))[-1]; fy2 = eig_intervals(mm(T(Fy), Fy))[-1]
out['gram_norm_upper_over_u'] = float(gnorm_hi / u)
out['Gram_le_half'] = gnorm_hi <= F(1, 2)
out['Gram_le_4u'] = gnorm_hi <= 4 * u
# ||Fx|| <= c u ||Q||  <=>  fx2 <= c^2 u^2 Qn2 ; certify with interval endpoints
def le(c, f2):
    return f2[1] <= c * c * u * u * Qn2[0]
out['Fx_le_64u_Q'] = le(64, fx2); out['Fy_le_64u_Q'] = le(64, fy2)
out['Fx_le_1u_Q'] = le(1, fx2); out['Fy_le_2u_Q'] = le(2, fy2)
out['Fx_norm_over_uQ_approx'] = math.sqrt(float(fx2[1] / Qn2[0])) / float(u)
out['Fy_norm_over_uQ_approx'] = math.sqrt(float(fy2[1] / Qn2[0])) / float(u)
om = sum(Fy[i][2] ** 2 for i in range(3))
out['omitted_Y_col_norm_over_u_approx'] = math.sqrt(float(om)) / float(u)
out['kappa_Q_sq_upper'] = float(Qn2[1] / sig2[0])
colnorms = lambda A: [math.sqrt(float(sum(A[i][j] ** 2 for i in range(3)))) / float(u) for j in range(3)]
out['Fx_col_norms_over_u'] = colnorms(Fx); out['Fy_col_norms_over_u'] = colnorms(Fy)
# symmetry / commutator
asym = []
for name, H in (('Hx', Hx), ('Hy', Hy)):
    for i in range(3):
        for j in range(i + 1, 3):
            d = H[i][j] - H[j][i]
            if d: asym.append((name, i, j, str(d)))
out['asymmetry'] = asym
C = sub(mm(Hx, Hy), mm(Hy, Hx))
out['comm_col0_zero'] = all(C[i][0] == 0 for i in range(3))
out['comm_row0'] = [str(C[0][j]) for j in range(3)]
out['Hx01_minus_Hx10'] = str(Hx[0][1] - Hx[1][0])
out['Hx01_minus_Hx10_is_2^-55'] = (Hx[0][1] - Hx[1][0]) == F(1, 2 ** 55)
out['Hx02_minus_Hx20_is_-2^-54'] = (Hx[0][2] - Hx[2][0]) == -F(1, 2 ** 54)
out['Hx_words'] = {'01': w(Hxf[0][1]), '10': w(Hxf[1][0]), '02': w(Hxf[0][2]), '20': w(Hxf[2][0])}
out['subnormal_or_nonfinite'] = any(((int(m[2], 16) >> 52) & 2047) in (0, 2047) and int(m[2], 16) & ((1 << 63) - 1) for m in TRACE)
print(json.dumps(out, indent=1, default=str))
