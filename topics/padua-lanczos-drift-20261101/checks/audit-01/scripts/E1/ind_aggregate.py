"""Auditor-independent aggregate bounds (PD-T?drift-codex-02 quantities).

Does NOT import producer code. Differences from producer e1_exact.py:
 - basis from canonical monomial Gram LDL^T (ind_basis.py), not parent-GS;
 - alpha_kl = b_l^T (a_k b_p)/d_l from that basis, and the identity
   a_k b_p - sum_l alpha_kl b_l == b_k is checked exactly for every k, node;
 - responses g_.h(z_i) obtained per node as columns of Lambda_i^{-1}, where
   Lambda_i is the unit lower-triangular frozen-recurrence matrix at node i
   (producer recurses per source over all nodes).
mode=exact: exact rationals. mode=arb: rigorous ball enclosures (prec bits);
exact inputs (alpha, sigma^2, d, R_ii, coordinates) are converted to balls.
All sources h=1..N-1.
"""
import sys, time, json
from flint import fmpq, fmpq_mat, arb, arb_mat, ctx
from ind_basis import nodes, exact_basis

sys.set_int_max_str_digits(0)


def setup(name, n, rule):
    pts = nodes(name)
    mons, V, B, D = exact_basis(pts, n)
    M, N = len(pts), len(mons)
    idx = {m: k for k, m in enumerate(mons)}
    cols = [[B[i, k] for i in range(M)] for k in range(N)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    choice = [None]; parent = [None]; tie_cols = []; pivot_margin = []
    for k in range(1, N):
        t, j = mons[k]
        cand = []
        if j < t:
            cand.append(("X", idx[(t - 1, j)]))
        if j > 0:
            cand.append(("Y", idx[(t - 1, j - 1)]))
        if len(cand) == 1:
            ax, p = cand[0]
        elif rule == "bj":
            ax, p = cand[0] if j == 0 else cand[1]
        elif rule == "alt":
            ax, p = cand[0] if 2 * j < t else cand[1]
        elif rule == "mirror":
            ax, p = cand[0] if j != t else cand[1]
        elif rule in ("pivot", "pivotY"):
            sX = sum((xs[i] * cols[cand[0][1]][i]) ** 2 for i in range(M))
            sY = sum((ys[i] * cols[cand[1][1]][i]) ** 2 for i in range(M))
            if sX == sY:
                tie_cols.append(mons[k])
            pivot_margin.append(float(abs(sX - sY) / (sX + sY)))
            ax, p = cand[0] if (sX < sY or (sX == sY and rule == "pivot")) else cand[1]
        else:
            raise ValueError(rule)
        choice.append(ax); parent.append(p)
    alpha = [None]; sigma2 = [None]
    for k in range(1, N):
        a = xs if choice[k] == "X" else ys
        z = [a[i] * cols[parent[k]][i] for i in range(M)]
        al = [sum((cols[l][i] * z[i] for i in range(M)), fmpq(0)) / D[l] for l in range(k)]
        for i in range(M):
            r = z[i]
            for l in range(k):
                if al[l]:
                    r -= al[l] * cols[l][i]
            assert r == cols[k][i], ("monic residual mismatch", k, i)
        alpha.append(al)
        sigma2.append(sum((v * v for v in z), fmpq(0)))
    Rii = [1 - sum((cols[k][i] ** 2 / D[k] for k in range(N)), fmpq(0)) for i in range(M)]
    assert min(Rii) >= 0
    return dict(pts=pts, mons=mons, M=M, N=N, cols=cols, D=D, xs=xs, ys=ys, choice=choice,
                parent=parent, alpha=alpha, sigma2=sigma2, Rii=Rii, tie_cols=tie_cols,
                min_pivot_rel_margin=(min(pivot_margin) if pivot_margin else None))


def per_node(S, i, mode):
    N = S["N"]
    num = (lambda q: q) if mode == "exact" else (lambda q: arb(q))
    zero = num(fmpq(0))
    Lam = [[zero] * N for _ in range(N)]
    for k in range(N):
        Lam[k][k] = num(fmpq(1))
    for k in range(1, N):
        al = S["alpha"][k]
        for l in range(k):
            if al[l]:
                Lam[k][l] = num(al[l])
        a = S["xs"][i] if S["choice"][k] == "X" else S["ys"][i]
        Lam[k][S["parent"][k]] = num(al[S["parent"][k]] - a)
    flat = [Lam[r][c] for r in range(N) for c in range(N)]
    G = (fmpq_mat(N, N, flat) if mode == "exact" else arb_mat(N, N, flat)).inv()
    v = [None]
    for h in range(1, N):
        e = zero
        for k in range(h, N):
            gk = G[k, h]
            e += gk * gk / num(S["D"][k])
        v.append(num(S["sigma2"][h]) * e)
    return v


def run(name, n, rule, mode="exact", node_list=None, prec=512):
    ctx.prec = prec
    t0 = time.time()
    S = setup(name, n, rule)
    t1 = time.time()
    M, N = S["M"], S["N"]
    num = (lambda q: q) if mode == "exact" else (lambda q: arb(q))
    ell_max = None; wit = None; khs = num(fmpq(0)); rows = []
    for i in (range(M) if node_list is None else node_list):
        v = per_node(S, i, mode)
        Ri = num(S["Rii"][i])
        rs = num(fmpq(0))
        for h in range(1, N):
            rs += v[h]
            ell = Ri * v[h]
            khs += ell
            if mode == "exact":
                if ell_max is None or ell > ell_max:
                    ell_max, wit = ell, (h, i)
            else:
                # track the ball with the largest upper end (and its lower end)
                if ell_max is None or ell.upper() > ell_max.upper():
                    ell_max, wit = ell, (h, i)
        rows.append((i, rs))
    if mode == "exact":
        urow_i, urow = max(rows, key=lambda r: r[1])
        # for exact mode knode lower=upper
        res = dict(Knode2=ell_max, KHS2=khs, Urow2=urow, Urow_node=urow_i)
    else:
        # rigorous enclosure of a max of balls: [max lower, max upper]
        urow_i, urow_ball = max(rows, key=lambda r: r[1].upper())
        urow_lo = max(r[1].lower() for r in rows)
        res = dict(Knode2_ball=ell_max, KHS2=khs, Urow2_ball=urow_ball, Urow2_lower=urow_lo, Urow_node=urow_i)
    res.update(set=name, degree=n, rule=rule, mode=mode, prec=prec, M=M, N=N,
               nodes_evaluated=(M if node_list is None else len(list(node_list))),
               choices="".join(S["choice"][1:]), pivot_tie_columns=S["tie_cols"],
               min_pivot_rel_margin=S["min_pivot_rel_margin"], witness=wit,
               secs_setup=round(t1 - t0, 2), secs_total=round(time.time() - t0, 2))
    return res


def ser(v):
    if isinstance(v, fmpq):
        return str(v)
    if isinstance(v, arb):
        def ex(a):
            m, e = a.man_exp(); m, e = int(m), int(e)
            return str(fmpq(m * 2 ** e) if e >= 0 else fmpq(m, 2 ** (-e)))
        return {"lower": ex(v.lower()), "upper": ex(v.upper()), "mid": v.mid().str(30), "rad": v.rad().str(5)}
    return v


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("set"); p.add_argument("degree", type=int); p.add_argument("rule")
    p.add_argument("--mode", default="exact"); p.add_argument("--nodes", default=None)
    p.add_argument("--prec", type=int, default=512); p.add_argument("--out", default=None)
    a = p.parse_args()
    nl = None if a.nodes is None else [int(s) for s in a.nodes.split(",")]
    r = run(a.set, a.degree, a.rule, a.mode, nl, a.prec)
    js = {k: ser(v) for k, v in r.items()}
    if a.out:
        open(a.out, "w").write(json.dumps(js, indent=1) + "\n")
    summ = {k: v for k, v in js.items() if k not in ("Knode2", "KHS2", "Urow2")}
    for k in ("Knode2", "KHS2", "Urow2"):
        if k in r:
            summ[k + "_float"] = float(r[k])
    print(json.dumps(summ, default=str))
