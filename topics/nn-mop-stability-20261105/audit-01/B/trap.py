#!/usr/bin/env python3
"""Auditor B: challenge the path-plus-anchor diagnostic (D2-02).

T1 (missing anchor, GENUINE compatible arrays, exact): for w2' = w2 + c*w1 the
    alternating first-e1 path H (beta,gamma,delta) is EXACTLY identical, but
    d_0 and many NN entries differ.  So the d_0 anchor is genuinely needed.
T2 (anchor sufficiency): path_recovery.recover on the w2' array recovers w2'
    (not w2), i.e. the anchor resolves the ambiguity (H is identical).
T3 (unused data): perturb EVERY off-path entry, plus the unused second b at
    the last two path sites (terminal b1=b2 identity and the never-read b2 at
    nu_(N-2)); the recover() output is bit-identical while the fieldwise E
    of the perturbed array is O(1).
"""
import copy, importlib.util, json, sys
from fractions import Fraction as Fr
import mpmath as mp
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from exact_jacobian import nn_and_sl, D, base

spec = importlib.util.spec_from_file_location('pr', '/home/user/padua_research/topics/nn-mop-stability-20261105/code/path_recovery.py')
pr = importlib.util.module_from_spec(spec); spec.loader.exec_module(pr)


def exact_arrays(x, w, N):
    nn, sl = nn_and_sl([D(t) for t in x], [[D(t) for t in r] for r in w], N)
    return {nu: {f: v.v for f, v in r.items()} for nu, r in nn.items()}, {k: {f: v.v for f, v in r.items()} for k, r in sl.items()}


def used_entries(N):
    used = {(0, 0): {'b1', 'b2'}}
    for k in range(N):
        nu = ((k+1)//2, k//2)
        used.setdefault(nu, set()).update({'b1' if k % 2 == 0 else 'b2', 'a1', 'a2'})
        if k >= 2:
            used.setdefault(((k-1)//2, (k-2)//2), set()).update({'b1', 'b2'})
    return used


def mpd(c):
    return {nu: {f: mp.mpf(v.numerator)/v.denominator for f, v in r.items()} for nu, r in c.items()}


def E(got, ref):
    m = mp.mpf(0)
    for f in ('a1', 'a2', 'b1', 'b2'):
        s = max(abs(r[f]) for r in ref.values())
        m = max(m, max(abs(got[nu][f]-r[f]) for nu, r in ref.items())/s)
    return m


out = []
mp.mp.dps = 100
for fam in ('krawtchouk', 'hahn'):
    for N in (4, 6, 8):
        x, w = base.inputs(N, fam)
        c = Fr(1, 3)
        w2p = [a+c*b for a, b in zip(w[1], w[0])]
        nn1, sl1 = exact_arrays(x, w, N)
        nn2, sl2 = exact_arrays(x, [w[0], w2p], N)
        sl_identical = all(sl1[k][f] == sl2[k][f] for k in sl1 for f in sl1[k])
        diff = sorted([(nu, f) for nu in nn1 for f in nn1[nu] if nn1[nu][f] != nn2[nu][f]])
        d0_1 = nn1[0, 0]['b2']-nn1[0, 0]['b1']; d0_2 = nn2[0, 0]['b2']-nn2[0, 0]['b1']
        xx = [mp.mpf(t.numerator)/t.denominator for t in x]
        ww = [[mp.mpf(t.numerator)/t.denominator for t in r] for r in w]
        ww2 = [ww[0], [mp.mpf(t.numerator)/t.denominator for t in w2p]]
        A1, A2 = mpd(nn1), mpd(nn2)
        r_21 = pr.recover(A2, N, xx, ww, 100)       # array 2 judged against input 1
        r_22 = pr.recover(A2, N, xx, ww2, 100)      # array 2 judged against input 2
        # T3
        used = used_entries(N)
        P = copy.deepcopy(A1)
        changed = 0
        for nu, r in P.items():
            for f in r:
                if f not in used.get(nu, set()):
                    r[f] = r[f]+(mp.mpf(1)/2 if f[0] == 'b' else r[f]+1)
                    changed += 1
        r_true = pr.recover(A1, N, xx, ww, 100)
        r_pert = pr.recover(P, N, xx, ww, 100)
        unused_on_path = sorted([(nu, f) for nu in used for f in ('a1', 'a2', 'b1', 'b2') if f not in used[nu]])
        row = dict(family=fam, N=N, c='1/3',
                   T1_sl_exactly_identical=sl_identical, T1_d0=[str(d0_1), str(d0_2)],
                   T1_num_NN_entries_differ=len(diff), T1_total_entries=4*len(nn1),
                   T1_E_between_genuine_arrays=float(E(A2, A1)),
                   T2_recover_A2_vs_input1=r_21, T2_recover_A2_vs_input2_mixed=r_22['mixed_input_diagnostic'],
                   T3_entries_changed=changed, T3_unused_entries_at_path_sites=[[list(a), b] for a, b in unused_on_path],
                   T3_recover_identical=(r_true == r_pert), T3_E_perturbed=float(E(P, A1)),
                   T3_recover_true_mixed=r_true['mixed_input_diagnostic'])
        out.append(row)
        print(fam, N, 'SL identical', sl_identical, 'diff entries', len(diff), '/', 4*len(nn1),
              'E', float(E(A2, A1)), '| rec A2 vs in1', r_21['mixed_input_diagnostic'], 'vs in2', r_22['mixed_input_diagnostic'],
'| T3 changed', changed,
              'identical', r_true == r_pert, 'E', float(E(P, A1)), 'unused-on-path', unused_on_path, file=sys.stderr)
print(json.dumps(out, indent=1, default=str))
