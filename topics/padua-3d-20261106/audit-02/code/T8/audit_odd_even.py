#!/usr/bin/env python3
"""Auditor checks of O (n=5,6) and E (n=3,5,7,9) using own code.
Producer raw JSONL is read only as a source of CERTIFICATES (null vectors),
each re-verified by audit_census.verify_null; coverage/order/node sets/full-rank
certificates are computed independently."""
import sys, json, math, itertools as it, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from audit_census import modes, node_set, node_key, verify_null, actual_node_rank, primes_1_mod

RAW = Path(sys.argv[1]); what = sys.argv[2:]
out = {}
if 'odd' in what:
    for n in (5, 6):
        t0 = time.time(); N = math.comb(n + 3, 3); M = 2 * N - 1
        pairs = list(it.combinations(range(1, N), 2))
        keys = {}
        for b, c in pairs:
            pts = node_set(M, (1, b, c)); assert len(pts) == N
            keys.setdefault(node_key(M, pts), (1, b, c))
        raw = [json.loads(l) for l in (RAW / f't8-odd-n{n}.jsonl').read_text().splitlines()]
        rawkeys = {node_key(M, node_set(M, tuple(r['z']))): r for r in raw}
        assert set(rawkeys) == set(keys) and len(raw) == len(rawkeys)
        full = []; nulls = 0
        p = primes_1_mod(M, 1, start=10**6)[0]
        for key, r in rawkeys.items():
            z = tuple(r['z'])
            if r['null'] is None:
                assert actual_node_rank(n, M, node_set(M, z), p) == N
                full.append(z)
            else:
                assert len(r['null']) == N and verify_null(n, M, z, r['null']); nulls += 1
        out[f'odd_n{n}'] = dict(M=M, pairs=len(pairs), distinct_node_sets=len(keys),
                                fullrank_certified=sorted(full), deficiency_certified=nulls,
                                prime=p, seconds=round(time.time() - t0, 1))
        print(out[f'odd_n{n}'], flush=True)
if 'even' in what:
    from numpy.polynomial import legendre as Lg
    def leg_basis(P, n):
        T = [Lg.legvander(P[:, j], n) for j in range(3)]
        return np.column_stack([T[0][:, a] * T[1][:, b] * T[2][:, c] for a, b, c in modes(n)])
    axis = np.cos(np.pi * np.arange(21) / 20)
    mesh = np.array(list(it.product(axis, repeat=3)))
    def lebesgue(P, n):
        V = leg_basis(P, n); W = leg_basis(mesh, n)
        Lc = np.linalg.solve(V.T, W.T)
        return float(np.abs(Lc).sum(axis=0).max()), float(np.linalg.cond(V))
    def leja_axis(m):  # own discrete Leja on Lobatto(m) points, start at x=1, tie -> lower index
        v = np.cos(np.pi * np.arange(m) / (m - 1)) if m > 1 else np.ones(1)
        order = [0]; rem = list(range(1, m))
        while rem:
            best = max(rem, key=lambda i: (np.prod([abs(v[i] - v[j]) for j in order]), -i))
            order.append(best); rem.remove(best)
        return v[order]
    for n in (3, 5, 7, 9):
        t0 = time.time(); N = math.comb(n + 3, 3); M = 2 * N - 2
        prefix = [(1, b, c) for b, c in it.combinations(range(1, N), 2) if (b + c) % 2]
        raw = [json.loads(l) for l in (RAW / f't8-even-selector-n{n}.jsonl').read_text().splitlines()]
        assert [tuple(r['z']) for r in raw] == prefix[:len(raw)]
        for r in raw[:-1]:
            z = tuple(r['z']); assert len(node_set(M, z)) == N
            assert r['null'] is not None and len(r['null']) == N and verify_null(n, M, z, r['null'])
        sel = tuple(raw[-1]['z']); pts = node_set(M, sel); assert len(pts) == N
        ps = primes_1_mod(M, 2, start=10**6)
        ranks = [actual_node_rank(n, M, pts, p) for p in ps]
        assert ranks[0] == N
        P = np.cos(2 * np.pi * np.array(pts) / M)
        lam, cond = lebesgue(P, n)
        ax = leja_axis(n + 1)
        LP = np.array([[ax[a], ax[b], ax[c]] for a, b, c in modes(n)])
        lam_leja, _ = lebesgue(LP, n)
        out[f'E_n{n}'] = dict(M=M, selected=sel, prefix_len=len(raw), earlier_nulls_verified=len(raw) - 1,
                              actual_node_ranks=ranks, primes=ps, lebesgue_legendre=lam,
                              cond_legendre=cond, own_leja_lebesgue=lam_leja,
                              seconds=round(time.time() - t0, 1))
        print(out[f'E_n{n}'], flush=True)
print(json.dumps(out, default=str))
