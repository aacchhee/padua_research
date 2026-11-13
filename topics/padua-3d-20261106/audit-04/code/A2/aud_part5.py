"""Part 5: old nine M=N witnesses. (a) theory table == evidence; (b) producer and checker
(p,omega) validity and exact reproduction of their stored determinants under their own
conventions; (c) own fresh primes > 4e9, second-kind Chebyshev U product basis, own order."""
import sys, math, json, re, time
sys.path.insert(0, sys.argv[1])
from aud_common import fold_nodes, split_prime, modrank_det, prime_factors, total_modes
from sympy import isprime
repo = sys.argv[2]
ev = json.load(open(repo + '/evidence/t8-r06-witnesses.json'))
ck = json.load(open(repo + '/evidence/t8-r08-check-old.json'))
theory = open(repo + '/theory/t8-r08-old-finite-existence.md').read()
rowsT = re.findall(r'^\|(\d+)\|(\d+)\|\(([\d,]+)\)\|\(([\d,]+)\)\|(\d+)\|$', theory, re.M)
tableT = {int(a): (int(b), [int(x) for x in c.split(',')], [int(x) for x in d.split(',')], int(e)) for a, b, c, d, e in rowsT}
rowsP = re.findall(r'^\|(\d+)\|(\d+)\|(\d+),(\d+)\|(\d+),(\d+)\|$', theory, re.M)
tableP = {int(a): (int(b), (int(c), int(d)), (int(e), int(f))) for a, b, c, d, e, f in rowsP}
lex = lambda n: [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)]
def exact_order(w, L, p):
    return pow(w, L, p) == 1 and all(pow(w, L // q, p) != 1 for q in prime_factors(L))
def xs(nodes, L, p, w):
    i2 = pow(2, -1, p)
    return [[(pow(w, v, p) + pow(w, (-v) % L, p)) * i2 % p for v in r] for r in nodes]
def cheb_tab(x, n, p, second=False):
    t = [1, (2 * x if second else x) % p]
    for k in range(2, n + 1): t.append((2 * x * t[-1] - t[-2]) % p)
    return t[:n + 1]
out = {'rows': []}; t0 = time.time(); used = set()
for r, c in zip(ev['rows'], ck['results']['old_witnesses']):
    n, N = r['n'], r['N']
    z, a, D = r['z'], r['phase_nums'], r['phase_den']
    rec = {'n': n, 'N': N}
    rec['theory_eq_evidence'] = tableT[n] == (N, z, a, D) and (c['z'], c['phase_nums'], c['phase_den']) == (z, a, D)
    L, nodes = fold_nodes(z, a, D, N)
    rec['L'] = L; rec['distinct_nodes'] = len(nodes)
    rec['L_matches'] = L == r['certificate']['L'] == c['L'] and tableP[n][0] == L
    # (b) producer: Chebyshev product, lex modes, sorted nodes
    pb = []
    for chk in r['certificate']['checks']:
        p, w = chk['p'], chk['omega']
        ok = isprime(p) and (p - 1) % L == 0 and exact_order(w, L, p)
        X = xs(nodes, L, p, w)
        T = [[cheb_tab(x, n, p) for x in row] for row in X]
        A = [[T[i][0][al[0]] * T[i][1][al[1]] * T[i][2][al[2]] % p for al in lex(n)] for i in range(N)]
        rk, det = modrank_det(A, p)
        pb.append(ok and rk == chk['rank'] == N and det == chk['det'])
    rec['producer_checks_reproduced'] = pb
    cb = []
    for chk, tp in zip(c['checks'], [tableP[n][1], tableP[n][2]]):
        p, w = chk['p'], chk['omega']
        ok = isprime(p) and (p - 1) % L == 0 and exact_order(w, L, p) and p < 1.9e9
        X = xs(nodes, L, p, w)
        A = [[math.prod(pow(x, e, p) for x, e in zip(row, al)) % p for al in lex(n)] for row in X]
        rk, det = modrank_det(A, p)
        cb.append(ok and rk == chk['rank'] == N and det == chk['det'] and (p, det) == tp)
    rec['checker_checks_reproduced_and_theory_table'] = cb
    # (c) own fresh primes, U basis
    own = []; floor = 4_000_000_000 + 7_000_000 * n
    for _ in range(2):
        p, w = split_prime(L, floor); floor = p + 1
        X = xs(nodes, L, p, w)
        U = [[cheb_tab(x, n, p, True) for x in row] for row in X]
        A = [[U[i][0][al[0]] * U[i][1][al[1]] * U[i][2][al[2]] % p for al in total_modes(n)] for i in range(N)]
        rk, det = modrank_det(A, p)
        own.append({'p': p, 'omega': w, 'rank': rk, 'det': det})
    rec['own'] = own
    rec['own_full_rank_both'] = all(o['rank'] == N and o['det'] for o in own)
    out['rows'].append(rec)
    print(json.dumps(rec), flush=True)
out['all_ok'] = all(x['theory_eq_evidence'] and x['distinct_nodes'] == x['N'] and x['L_matches'] and all(x['producer_checks_reproduced'])
                    and all(x['checker_checks_reproduced_and_theory_table']) and x['own_full_rank_both'] for x in out['rows'])
out['seconds'] = round(time.time() - t0, 1)
json.dump(out, open(sys.argv[3], 'w'), indent=1)
print('ALL_OK', out['all_ok'], 'seconds', out['seconds'])
