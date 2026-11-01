"""L2 reconstruction 01: does the pivot-adaptive selection ('adapt': per column the candidate with larger
beta/||A q_p|| after the first orthogonalisation pass) satisfy condition (C) of rl2_cycles.py, i.e. is the
PD-T?...-205 recursion defined for it?  Own implementation of the rule as described in PD-T?...-206.
Usage: python3 -I rl2_adapt_C.py > logs_L2/adapt_C.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rl2_lib as R
from rl2_cycles import cand, analyse


def adapt_selection(x, y, w, nmax, mode):
    N = R.Nof(nmax); M = len(x)
    Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    sel = {}
    for t in range(1, nmax + 1):
        for j in range(t + 1):
            k = R.start_of(t) + j
            W = np.arange(R.start_of(max(t - 2, 0)), k)
            best = None
            for (op, pj) in cand(t, j):
                p = R.start_of(t - 1) + pj
                a = (x if op == 'X' else y) * Q[:, p]
                if mode == 'cgs2all':
                    Qk = Q[:, :k]; r = a - Qk @ (Qk.T @ a); r = r - Qk @ (Qk.T @ r)
                else:
                    r = a - Q[:, W] @ (Q[:, W].T @ a)
                sc = np.linalg.norm(r) / np.linalg.norm(a)
                if best is None or sc > best[0]:
                    best = (sc, op, pj, r)
            _, op, pj, r = best
            if mode != 'cgs2all':
                r = r - Q[:, W] @ (Q[:, W].T @ r)
            Q[:, k] = r / np.linalg.norm(r)
            sel[(t, j)] = (op, pj)
    return sel


def main():
    sq, dk, tr = R.rng11_sets()
    sets = [('rotpi4', R.rotate(sq, np.pi / 4), 24), ('rot0.3', R.rotate(sq, 0.3), 24), ('triangle', tr, 20),
            ('disk', dk, 24), ('square', sq, 24)]
    for name, P, n in sets:
        x, y = P[:, 0].copy(), P[:, 1].copy()
        for mode in ('cgs2all', 'cgs2win'):
            sel = adapt_selection(x, y, np.ones(len(x)), n, mode)
            viol = []
            for nn in range(2, n + 1):
                sub = {k: v for k, v in sel.items() if k[0] <= nn}
                c, ok = analyse(sub, nn)
                if not c or not ok:
                    viol.append(nn)
            print(f"  {name:8s} adapt/{mode}: first degree n at which (C) fails / recursion undefined: "
                  f"{viol[0] if viol else 'none (<= %d)' % n}", flush=True)


if __name__ == '__main__':
    main()
