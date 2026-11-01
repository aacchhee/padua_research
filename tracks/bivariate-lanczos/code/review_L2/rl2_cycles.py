"""L2 reconstruction 01: well-definedness of the PD-T?...-205 section recursion over one-relation selections
(support-only, block window).  Classifies selections by the condition (C): every unformed A-product belongs to a
column created by the other operator.  Exhaustive for n <= 5, random for n = 6..9.  Exact combinatorics.
Usage: python3 -I rl2_cycles.py > logs_L2/cycles.log"""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl2_lib as R


def cand(t, j):
    c = []
    if j <= t - 1:
        c.append(('X', j))
    if j >= 1:
        c.append(('Y', j - 1))
    return c


def analyse(sel, n):
    N, Nc = R.Nof(n), R.Nof(n - 1)
    idx = [(t, j) for t in range(n + 1) for j in range(t + 1)]
    pos = {k: i for i, k in enumerate(idx)}
    creator, formed = {}, {'X': {}, 'Y': {}}
    for k in range(1, N):
        t, j = idx[k]; op, pj = sel[(t, j)]; p = pos[(t - 1, pj)]
        creator[k] = (op, p)
        if p < Nc:
            formed[op][p] = k
    condC = all((m in formed[A]) or creator[m][0] != A for A in 'XY' for m in range(1, Nc))
    H, state = {}, {}

    def win(k):
        t, j = idx[k]
        return set(range(R.start_of(max(t - 2, 0)), k))

    def get(A, m):
        key = (A, m)
        if state.get(key) == 'done':
            return H[key]
        if state.get(key) == 'busy':
            raise RecursionError
        state[key] = 'busy'
        if m in formed[A]:
            k = formed[A][m]; s = win(k) | {k}
        else:
            B, p = creator[m]; s = set()
            for l in sorted(get(A, p)):
                s |= get(B, l)
            for l in sorted(win(m)):
                s |= get(A, l)
        H[key] = s; state[key] = 'done'
        return s
    try:
        for A in 'XY':
            for m in range(Nc):
                get(A, m)
        ok = True
    except RecursionError:
        ok = False
    return condC, ok


def main():
    print("# rl2_cycles.py: (C) = every unformed A-product of m has creator(m) != A", flush=True)
    for n in (2, 3, 4, 5):
        cols = [(t, j) for t in range(1, n + 1) for j in range(t + 1)]
        tab = {(c, o): 0 for c in (True, False) for o in (True, False)}
        for combo in itertools.product(*[cand(t, j) for (t, j) in cols]):
            c, o = analyse(dict(zip(cols, combo)), n)
            tab[(c, o)] += 1
        print(f"  n={n} exhaustive ({sum(tab.values())} selections): (C) and well defined {tab[(True, True)]}; "
              f"(C) and cycle {tab[(True, False)]}; not (C) and well defined {tab[(False, True)]}; "
              f"not (C) and cycle {tab[(False, False)]}", flush=True)
    for n in (6, 7, 8, 9):
        rr = random.Random(n)
        tab = {(c, o): 0 for c in (True, False) for o in (True, False)}
        cols = [(t, j) for t in range(1, n + 1) for j in range(t + 1)]
        # random selections conditioned on (C): build degree by degree
        for trial in range(3000):
            sel = {}
            for (t, j) in cols:
                sel[(t, j)] = rr.choice(cand(t, j))
            c, o = analyse(sel, n)
            tab[(c, o)] += 1
        print(f"  n={n} random (3000): (C)&ok {tab[(True, True)]}, (C)&cycle {tab[(True, False)]}, "
              f"not(C)&ok {tab[(False, True)]}, not(C)&cycle {tab[(False, False)]}", flush=True)
    # named rules
    rules = {'bj': lambda t, j: ('X', j) if j == 0 else ('Y', j - 1),
             'mirror': lambda t, j: ('Y', t - 1) if j == t else ('X', j),
             'alt': lambda t, j: ('X', j) if 2 * j < t else ('Y', j - 1)}
    for nm, f in rules.items():
        for n in (6, 12, 20):
            sel = {(t, j): f(t, j) for t in range(1, n + 1) for j in range(t + 1)}
            print(f"  rule {nm} n={n}: (C) = {analyse(sel, n)[0]}, well defined = {analyse(sel, n)[1]}", flush=True)


if __name__ == '__main__':
    main()
