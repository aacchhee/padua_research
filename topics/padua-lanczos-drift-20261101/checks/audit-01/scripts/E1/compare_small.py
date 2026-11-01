"""Compare producer functions (e1_exact.bounds, e1_cgs2.run) with the auditor's
first-principles implementation on the same small generic point sets.
The producer is imported ONLY here, for comparison."""
import sys, json, io, contextlib
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/padua_research/tracks/bivariate-lanczos/code/drift')
sys.set_int_max_str_digits(0)
import first_principles as fp
import e1_exact, e1_cgs2
from flint import fmpq

rows = []
for (M, n, seed) in [(14, 3, 1), (20, 4, 2)]:
    pts = fp.make_points(M, seed)
    xyq = [(fmpq(a.numerator, a.denominator), fmpq(b.numerator, b.denominator)) for a, b in pts]
    for rule in ['bj', 'mirror', 'alt', 'pivot']:
        mons, B, D = fp.basis_mono_gs(pts, n)
        ch, par, ties, xs, ys = fp.rule_choices(pts, n, rule, mons, B)
        alpha, sig2 = fp.recurrence(pts, B, D, ch, par, xs, ys)
        N = len(B)
        g = fp.g_responses(pts, ch, par, alpha, xs, ys, N)
        Rii = [1 - sum((B[k][i] ** 2 / D[k] for k in range(N)), F(0)) for i in range(M)]
        v = {(h, i): sig2[h] * sum((g[(k, h)][i] ** 2 / D[k] for k in range(h, N)), F(0)) for h in range(1, N) for i in range(M)}
        L2 = max(Rii[i] * v[(h, i)] for (h, i) in v)
        H2 = sum(Rii[i] * v[(h, i)] for (h, i) in v)
        U2 = max(sum(v[(h, i)] for h in range(1, N)) for i in range(M))
        # record03/05 full-graph upper, own implementation from the record's formulas
        rho = {}
        for h in range(1, N):
            A = xs if ch[h] == 0 else ys
            for i in range(M):
                s = abs(A[i] * B[par[h]][i]) + 3 * abs(B[h][i]); part = F(0)
                for l in range(h):
                    term = alpha[h][l] * B[l][i]; s += abs(term); part += term
                    if l >= 1: s += abs(part)
                rho[(h, i)] = s
        Uinf2 = sum((sum((abs(g[(k, h)][i]) * rho[(h, i)] for h in range(1, k + 1)), F(0)) ** 2 / D[k]
                     for k in range(1, N) for i in range(M)), F(0))
        with contextlib.redirect_stdout(io.StringIO()):
            pb = e1_exact.bounds(xyq, n, rule, 'all')
            e1_cgs2.points = lambda name, _x=xyq: _x
            pc = e1_cgs2.run('custom', n, rule)
        rows.append({'M': M, 'n': n, 'rule': rule,
                     'Knode_equal': F(pb['Knode_squared']['exact']) == L2,
                     'KHS_equal': F(pb['KHS_squared']['exact']) == H2,
                     'Urow_equal': F(pb['Urow_squared']['exact']) == U2,
                     'choices_equal': ''.join(pb['pivot_choices']) == ''.join('XY'[c] for c in ch[1:]),
                     'Uinf_fullgraph_equal': F(pc['upper_squared']['exact']) == Uinf2})
print(json.dumps(rows, indent=0))
print('ALL EQUAL:', all(all(v for k, v in r.items() if k.endswith('equal')) for r in rows))
