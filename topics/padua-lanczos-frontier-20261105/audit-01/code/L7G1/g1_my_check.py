# Auditor's own T24 G1 gate check (Claude L7G1). Rigorous ball arithmetic via FLINT/Arb, exact fmpq products.
import sys, json, pathlib, hashlib
sys.path.insert(0, sys.argv[1]); sys.set_int_max_str_digits(0)
import flint
from flint import fmpq, arb, ctx
ctx.prec = 600
out = pathlib.Path(sys.argv[2]); REC = json.load(open(sys.argv[3]))
DEG = list(range(2, 21)); RULES = ['bj', 'mirror', 'alt', 'pivot']
def N(n): return (n+1)*(n+2)//2
def Fq(s):
    if '/' in s: a, b = s.split('/'); return fmpq(int(a), int(b))
    return fmpq(int(s))
data = {}
for r in RULES:
    p = out/f'full-{r}'/'endpoints.json'
    rows = json.load(open(p))['runs']
    assert [x['degree'] for x in rows] == DEG
    vals = []
    for x in rows:
        n = x['degree']; k = N(n)
        assert x['set'] == 'triangle' and x['rule'] == r and x['sources'] == 'all' and x['source_count'] == k-1 and x['basis_count'] == k and x['point_count'] == 325
        assert Fq(x['normal_trace_exact']) == 325-k
        L, H, R, U = (Fq(x[f]['exact']) for f in ['Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared'])
        assert 0 < L <= U and U == min(H, R)
        assert x['pivot_ties'] == [] and len(x['pivot_choices']) == k-1
        vals.append((L, U))
    data[r] = vals
# exact ratio endpoints
qa, qb, winners = [], [], []
for i, s in enumerate(DEG):
    Lb, Ub = data['bj'][i]
    minU = min(data[c][i][1] for c in RULES[1:]); minL = min(data[c][i][0] for c in RULES[1:])
    qa.append(Lb/minU); qb.append(Ub/minL); assert qa[-1] <= qb[-1]
    winners.append(([c for c in RULES[1:] if data[c][i][1] == minU], [c for c in RULES[1:] if data[c][i][0] == minL]))
def lg(q): return arb(q).log()
A = [lg(q)/2 for q in qa]; B = [lg(q)/2 for q in qb]
# my own slope coefficient derivation: OLS slope weights on 2..10 and 11..20
def slopew(ds):
    m = len(ds); xb = fmpq(sum(ds), m); D = sum((fmpq(d)-xb)**2 for d in ds)
    return {d: (fmpq(d)-xb)/D for d in ds}
e = slopew(range(2, 11)); l = slopew(range(11, 21))
E = [e.get(s, fmpq(0)) for s in DEG]; Lw = [l.get(s, fmpq(0)) for s in DEG]; G = [Lw[i]-E[i]/2 for i in range(19)]
assert all(E[i] == fmpq(s-6, 60) for i, s in enumerate(DEG) if s <= 10) and all(Lw[i] == fmpq(2*s-31, 165) for i, s in enumerate(DEG) if s >= 11)
def corner(c, maximize):  # choose b where c>0 for max, a where c>0 for min
    return [fmpq(1, 2) if x == 0 else (fmpq(1) if ((x > 0) == maximize) else fmpq(0)) for x in c]
def lin(c, tau): return sum((arb(c[i])*((1-arb(tau[i]))*A[i] + arb(tau[i])*B[i]) for i in range(19)), arb(0))
def exact_sign(c, tau, D):
    prod = fmpq(1)
    for i in range(19):
        if c[i] == 0: continue
        m = D*c[i]; assert m.q == 1; m = int(m.p)
        q = qa[i] if tau[i] == 0 else qb[i]
        prod *= q**m
    return (prod > 1) - (prod < 1), len(str(prod.p)), len(str(prod.q))
tmax = corner(G, True); tmin = corner(E, False)
gval = lin(G, tmax); evalmin = lin(E, tmin)
gs = exact_sign(G, tmax, 1320); es = exact_sign(E, tmin, 60)
print('tau(late-half-early max)', [str(t) for t in tmax])
print('max g^T y over box: arb', gval.str(20), 'exact product sign', gs[0], 'digits num/den', gs[1], gs[2])
print('min early slope over box: arb', evalmin.str(20), 'exact product sign', es[0], 'digits', es[1], es[2])
# brute-force check that the corner is the max over all vertices is unnecessary: separable linear function; verify by per-coordinate argument
for i in range(19):
    lo_ = arb(G[i])*A[i]; hi_ = arb(G[i])*B[i]
    if G[i] > 0: assert tmax[i] == 1
    if G[i] < 0: assert tmax[i] == 0
# compare with committed receipt
def rint(iv): return arb(Fq(iv[0])), arb(Fq(iv[1]))
def contains(iv, x):
    lo, hi = Fq(iv[0]), Fq(iv[1]); return bool(x > arb(lo)) and bool(x < arb(hi)) or (bool(x >= arb(lo)) and bool(x <= arb(hi)))
tri = REC['grid_results']['triangle']
print('receipt signed_interval contains my value:', contains(tri['signed_interval'], gval), '| receipt early_minimum_interval contains mine:', contains(tri['early_minimum_interval'], evalmin))
print('receipt witness tau equals mine:', tri['witness_tau'] == [str(t) for t in tmax])
# midpoint diagnostics
mid = [(A[i]+B[i])/2 for i in range(19)]
def ols(xs, ys):
    m = len(xs); xb = sum(xs, arb(0))/m; yb = sum(ys, arb(0))/m
    D = sum(((x-xb)**2 for x in xs), arb(0)); sl = sum(((x-xb)*y for x, y in zip(xs, ys)), arb(0))/D
    return yb - sl*xb, sl
def pred(kind):
    return [arb(d) if kind == 'E' else arb(d+1).log() for d in DEG]
res = {}
for kind in ['E', 'P']:
    x = pred(kind); a, b = ols(x[:13], mid[:13])
    sse = sum(((mid[13+h] - (a + b*x[13+h]))**2 for h in range(6)), arb(0))
    res[kind] = sse
early = sum((arb(E[i])*mid[i] for i in range(19)), arb(0)); late = sum((arb(Lw[i])*mid[i] for i in range(19)), arb(0))
md = tri['midpoint_ratio_descriptive_diagnostics']
print('midpoint E holdout SSE', res['E'].str(12), contains(md['E']['holdout_15_20_SSE'], res['E']))
print('midpoint P holdout SSE', res['P'].str(12), contains(md['P']['holdout_15_20_SSE'], res['P']))
print('midpoint early slope', early.str(12), contains(md['early_slope'], early), ' late slope', late.str(12), contains(md['late_slope'], late))
print('midpoint (tau=1/2) SSE clause value 2SSE_P-SSE_E =', (2*res['P']-res['E']).str(12), '(positive => also an SSE counterchoice)')
print('midpoint late - early/2 =', (late-early/2).str(12))
# rule-curve exponential slopes (all degrees 2..20)
for r in RULES:
    Lc = [lg(v[0])/2 for v in data[r]]; Uc = [lg(v[1])/2 for v in data[r]]; Mc = [(x+y)/2 for x, y in zip(Lc, Uc)]
    xs = [arb(d) for d in DEG]
    print('T24', r, 'E-slopes lower/upper/mid', ols(xs, Lc)[1].str(10), ols(xs, Uc)[1].str(10), ols(xs, Mc)[1].str(10))
print('comparator winners (lower q uses min U over; upper q uses min L over):')
for s, w in zip(DEG, winners): print(' ', s, w)
print('log-ratio intervals a_s,b_s:')
for s, a, b in zip(DEG, A, B): print(' ', s, a.str(8), b.str(8), 'width', (b-a).str(5))
