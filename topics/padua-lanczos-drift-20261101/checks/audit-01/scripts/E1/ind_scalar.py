"""Auditor-independent record05 check (no producer import).

Full declared scalar-CGS2 graph (record03 formulas):
  rho_hi = |(A_h b_p)_i| + sum_l |alpha_hl b_l(i)| + sum_{l>=1} |sum_{r<=l} alpha_hr b_r(i)| + 3|b_h(i)|
  U_inf^2 = sum_{i,k} [sum_h |g_kh(z_i)| rho_hi]^2 / d_k                (comparator upper)
  S_ti = sum_{h<=t} |g_th(z_i)| rho_hi ; greedy signs ; G_t^2 = (|s*S|^2 - sum_l (b_l^T s*S)^2/d_l)/d_t
Responses g via per-node inverse of the frozen-recurrence matrix (ind_aggregate.per-node style).
mode exact (T24) or arb (rotated; rigorous balls, sign decisions certified unambiguous).
"""
import sys, json, time
from flint import fmpq, fmpq_mat, arb, arb_mat, ctx
from ind_aggregate import setup, ser

sys.set_int_max_str_digits(0)
EV = '/home/claude/padua_research/topics/padua-lanczos-drift-20261101/evidence'


def node_G(S, i, mode):
    N = S['N']
    num = (lambda q: q) if mode == 'exact' else (lambda q: arb(q))
    Lam = [[num(fmpq(0))] * N for _ in range(N)]
    for k in range(N):
        Lam[k][k] = num(fmpq(1))
    for k in range(1, N):
        al = S['alpha'][k]
        for l in range(k):
            if al[l]:
                Lam[k][l] = num(al[l])
        a = S['xs'][i] if S['choice'][k] == 'X' else S['ys'][i]
        Lam[k][S['parent'][k]] = num(al[S['parent'][k]] - a)
    flat = [Lam[r][c] for r in range(N) for c in range(N)]
    return (fmpq_mat(N, N, flat) if mode == 'exact' else arb_mat(N, N, flat)).inv()


def rho_all(S):
    N, M = S['N'], S['M']; cols = S['cols']
    rho = [[fmpq(0)] * M for _ in range(N)]
    for h in range(1, N):
        A = S['xs'] if S['choice'][h] == 'X' else S['ys']
        al = S['alpha'][h]; p = S['parent'][h]
        for i in range(M):
            s = abs(A[i] * cols[p][i]) + 3 * abs(cols[h][i]); part = fmpq(0)
            for l in range(h):
                term = al[l] * cols[l][i]; s += abs(term); part += term
                if l >= 1:
                    s += abs(part)
            rho[h][i] = s
    return rho


def upper(name, rule, mode, prec=512):
    ctx.prec = prec
    S = setup(name, 12, rule); rho = rho_all(S)
    N, M = S['N'], S['M']
    num = (lambda q: q) if mode == 'exact' else (lambda q: arb(q))
    tot = num(fmpq(0))
    for i in range(M):
        G = node_G(S, i, mode)
        for k in range(1, N):
            s = num(fmpq(0))
            for h in range(1, k + 1):
                gk = G[k, h]
                if mode == 'exact':
                    if gk: s += abs(gk) * rho[h][i]
                else:
                    s += abs(gk) * num(rho[h][i])
            tot += s * s / num(S['D'][k])
    return tot, S['choice']


def bj_lower(name, target, committed_signs, mode, prec=512):
    ctx.prec = prec
    S = setup(name, 12, 'bj'); rho = rho_all(S)
    N, M = S['N'], S['M']; cols = S['cols']; D = S['D']
    num = (lambda q: q) if mode == 'exact' else (lambda q: arb(q))
    St = []
    for i in range(M):
        G = node_G(S, i, mode)
        s = num(fmpq(0))
        for h in range(1, target + 1):
            s += abs(G[target, h]) * num(rho[h][i])
        St.append(s)
    def gain(signs):
        v = [St[i] * signs[i] for i in range(M)]
        nv = sum((x * x for x in v), num(fmpq(0)))
        proj = num(fmpq(0))
        for l in range(N):
            c = sum((num(cols[l][i]) * v[i] for i in range(M)), num(fmpq(0)))
            proj += c * c / num(D[l])
        return (nv - proj) / num(D[target])
    # own greedy signs (node order 0..M-1, tie -> +1), certified in arb mode
    c = [num(fmpq(0))] * N; signs = []; ambiguous = 0
    for i in range(M):
        score = -sum((num(cols[l][i]) * c[l] / num(D[l]) for l in range(N)), num(fmpq(0)))
        if mode == 'exact':
            sg = 1 if score >= 0 else -1
        else:
            if score.lower() > 0 or (score.mid() == 0 and score.rad() == 0): sg = 1
            elif score.upper() < 0: sg = -1
            else: ambiguous += 1; sg = 1
        signs.append(sg)
        for l in range(N):
            c[l] += num(cols[l][i]) * St[i] * sg
    expected = sum((num(S['Rii'][i]) * St[i] * St[i] for i in range(M)), num(fmpq(0))) / num(D[target])
    return gain(committed_signs), gain(signs), signs, ambiguous, expected


if __name__ == '__main__':
    name, mode = sys.argv[1], sys.argv[2]
    comp = 'pivot' if name == 'triangle' else 'alt'
    t0 = time.time()
    U, ch = upper(name, comp, mode)
    cert = next(w for w in json.load(open(f'{EV}/e1-multinode-certificates.json'))['witnesses'] if w['set'] == name)
    Lc, Lg, signs, amb, expct = bj_lower(name, cert['target_column'], cert['node_signs'], mode)
    out = {'set': name, 'mode': mode, 'comparator': comp, 'Uinf2': ser(U), 'L_committed_signs': ser(Lc),
           'L_own_greedy': ser(Lg), 'own_greedy_signs_equal_committed': signs == cert['node_signs'],
           'ambiguous_sign_decisions': amb, 'expected_random_sign': ser(expct), 'target': cert['target_column'],
           'secs': round(time.time() - t0, 1)}
    open(f'ind-scalar-{name}.json', 'w').write(json.dumps(out, indent=1) + '\n')
    print(json.dumps({k: (v if not isinstance(v, (dict, str)) or k in ('set', 'mode', 'comparator') else (v if isinstance(v, str) and len(v) < 60 else '...')) for k, v in out.items()}))
