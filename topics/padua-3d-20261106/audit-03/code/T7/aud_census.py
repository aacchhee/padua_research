#!/usr/bin/env python3
"""Auditor (Claude) independent n=2 brute-force coset census.

Imports no project code.  Groups: own lower-triangular enumeration
(aud_groups.py).  Only the two trivially valid group bounds are used:
2 < m_j <= 20 (m_j<=2: a univariate quadratic vanishes; m_j>20: >10
cosine values).  NO prime reduction, NO order-10 trace kill, NO H-translation
quotient, NO trace / short-relation kill is used to decide anything.
Every half-shift-reduced special index tuple k_j in [0,m_j) and every
free mask is visited (free a_j = f_j/1013, f_j seeded random).
Each 10-node stratum gets a float64 SVD rank at the representative and,
if it has a free coordinate, also at an independent uniform real phase.
Own trace and short-relation predicates and H-orbit ids are computed only
to compare with the producer's bookkeeping.
"""
import itertools as it, json, math, sys, time
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from aud_groups import groups, points

N = 10
MODES = np.array([v for v in it.product(range(3), repeat=3) if sum(v) <= 2])
SCALE = np.sqrt(2.0)**np.count_nonzero(MODES, axis=1)
TRACE = {e: sum((-1)**int(np.dot(e, a)) for a in MODES) for e in it.product((0, 1), repeat=3)}


def vander(x):
    # x: (..., 10, 3) -> orthonormal product Chebyshev matrix (..., 10, 10)
    th = np.arccos(np.clip(x, -1, 1))
    out = np.ones(x.shape[:-1] + (len(MODES),))
    for j in range(3):
        out = out*np.cos(th[..., j:j+1]*MODES[None, :, j])
    return out*SCALE


def ratio(V):
    s = np.linalg.svd(V, compute_uv=False)
    return s[..., -1]/s[..., 0]


def main():
    rng = np.random.default_rng(20261106)
    t0 = time.time()
    stats = Counter(); positives = []; border = []; maxdef = 0.0; minpos = 1.0
    trace_inconsistent = []; short_inconsistent = []
    orbit_target = {}           # producer-comparable bookkeeping (nonprime, m!=10)
    burnside_total = 0
    p19 = defaultdict(set)
    gid = 0
    import os
    for m in range(int(os.environ.get('MMIN', 10)), int(os.environ.get('MMAX', 80))+1):
        isprime = all(m % d for d in range(2, int(m**.5)+1))
        for g in groups(m):
            P = points(g)
            mj = [len(np.unique(P[:, j])) for j in range(3)]
            if min(mj) <= 2 or max(mj) > 20:
                continue
            gid += 1; stats['groups_bruteforced'] += 1
            comparable = (not isprime) and m != N
            two = [h for h in P if h.any() and not ((2*h) % m).any()]
            es = [tuple(int(v) for v in (2*h)//m) for h in two]
            UL = [uv for uv in it.product(range(-2, 3), repeat=3) if any(uv) and sum(v != 0 for v in uv) <= 2
                  and not ((P @ np.array(uv)) % m).any()]
            tau = np.stack([(2*mj[j]*P[:, j]//m) % mj[j] for j in range(3)], axis=1)
            D = 2*m*1013; half = D//2; base = half+1
            free_num = [int(rng.integers(1, 1013)) for _ in range(3)]
            for mask in range(8):
                J = [j for j in range(3) if mask >> j & 1]
                F = [j for j in range(3) if not mask >> j & 1]
                if comparable:
                    if J:
                        img = np.unique(tau[:, J] @ np.array([10**(2*i) for i in range(len(J))]))
                        burnside_total += math.prod(mj[j] for j in J)//len(img)
                    else:
                        burnside_total += 1
                K = np.array(list(it.product(*(range(mj[j]) for j in J))), dtype=np.int64).reshape(-1, len(J)) if J else np.zeros((1, 0), dtype=np.int64)
                S = len(K)
                ph = np.zeros((S, 3), dtype=np.int64)
                for i, j in enumerate(J): ph[:, j] = K[:, i]*(D//(2*mj[j]))
                for j in F: ph[:, j] = free_num[j]*(D//1013)
                q = (P[None, :, :]*(D//m) + ph[:, None, :]) % D
                f = np.minimum(q, D-q)
                codes = np.sort(f[:, :, 0]*base*base + f[:, :, 1]*base + f[:, :, 2], axis=1)
                cnt = 1 + np.count_nonzero(np.diff(codes, axis=1), axis=1)
                stats['strata'] += S
                sel = np.flatnonzero(cnt == N)
                stats['target_count_strata_unquotiented'] += len(sel)
                if not len(sel): continue
                # unique nodes for target rows
                cs = codes[sel]
                keep = np.concatenate([np.ones((len(sel), 1), bool), np.diff(cs, axis=1) != 0], axis=1)
                u = cs[keep].reshape(len(sel), N)
                fn = np.stack([u//(base*base), (u//base) % base, u % base], axis=2)
                axis_low = np.array([[len(np.unique(fn[i, :, j])) <= 2 for j in range(3)] for i in range(len(sel))]).any(axis=1)
                x = np.cos(2*np.pi*fn/D)
                r1 = ratio(vander(x))
                if F:
                    # independent uniform real phase on the free coordinates
                    a = np.zeros((len(sel), 3))
                    for i, j in enumerate(J): a[:, j] = K[sel, i]/(2*mj[j])
                    a[:, F] = rng.random((len(sel), len(F)))
                    t = P[None, :, :]/m + a[:, None, :]
                    xf = np.cos(2*np.pi*t)
                    r2 = np.empty(len(sel))
                    for i in range(len(sel)):
                        dd = np.max(np.abs(xf[i][:, None, :]-xf[i][None, :, :]), axis=2) < 1e-9
                        first = ~np.any(np.tril(dd, -1), axis=1)
                        assert first.sum() == N, ('count not constant on stratum', g, mask)
                        r2[i] = ratio(vander(xf[i][first]))
                    rr = np.maximum(r1, r2)
                else:
                    rr = r1
                for ii, i in enumerate(sel):
                    k = tuple(int(v) for v in K[i])
                    full = rr[ii] > 1e-7
                    if 1e-13 < rr[ii] < 1e-6: border.append((g, mask, k, float(r1[ii]), float(rr[ii])))
                    if full: minpos = min(minpos, rr[ii])
                    else: maxdef = max(maxdef, rr[ii])
                    # own trace predicate
                    tr_bad = False
                    for e in es:
                        fixed = int(np.sum(np.all(fn[ii][:, [j for j in range(3) if e[j]]]*4 == D, axis=1)))
                        if fixed != TRACE[e]: tr_bad = True; break
                    # own compatible short relation predicate (support<=2, |u|<=2)
                    sr = False
                    for uvec in UL:
                        if any(uvec[j] for j in F): continue
                        num = sum(uvec[j]*k[J.index(j)]*(2*m//mj[j]) for j in J if uvec[j])  # 2u.a * (2m)
                        if num % (2*m) == 0: sr = True; break
                    if full and (tr_bad or sr or axis_low[ii]):
                        (trace_inconsistent if tr_bad else short_inconsistent).append((g, mask, k, float(rr[ii])))
                    if full:
                        positives.append({'g': g, 'm': m, 'mask': mask, 'k': k, 'ratio': float(rr[ii])})
                    if m == 19:
                        p19[g].add((mask, bool(full)))
                    if comparable and not axis_low[ii]:
                        # orbit id under H translations (special coords only)
                        if J:
                            T = (np.array(k)[None, :] + tau[:, J]) % np.array([mj[j] for j in J])
                            oid = int((T @ np.array([10**(2*i) for i in range(len(J))])).min())
                        else:
                            oid = -1
                        key = (g, mask, oid)
                        dec = 'trace' if tr_bad else ('short' if sr else ('full' if full else 'other-deficient'))
                        prev = orbit_target.get(key)
                        assert prev is None or prev == dec, ('decision not constant on orbit', key, prev, dec)
                        orbit_target[key] = dec
        print(json.dumps({'order_done': m, 'secs': round(time.time()-t0, 1), 'strata': stats['strata']}), flush=True)
    oc = Counter(orbit_target.values())
    out = {'stats': dict(stats), 'burnside_quotient_strata_nonprime_m_ne_10': burnside_total,
           'orbit_target_strata': len(orbit_target), 'orbit_decisions': dict(oc),
           'positives_unquotiented': len(positives),
           'positive_groups': sorted({(p['m'],) + tuple(p['g']) for p in positives}),
           'positive_masks': dict(Counter(p['mask'] for p in positives)),
           'max_deficient_ratio': maxdef, 'min_full_ratio': minpos, 'borderline': border[:50],
           'n_borderline': len(border), 'trace_inconsistent': trace_inconsistent[:20],
           'short_or_axis_inconsistent': short_inconsistent[:20],
           'p19_groups_with_target_strata': len(p19),
           'p19_groups_mixed_rank_over_phases': sum(1 for v in p19.values() if len({f for _, f in v}) > 1),
           'seconds': time.time()-t0}
    json.dump({'summary': out, 'positives': positives}, open(sys.argv[1], 'w'), indent=1, default=list)
    print(json.dumps(out, default=list)[:4000])


if __name__ == '__main__':
    main()
