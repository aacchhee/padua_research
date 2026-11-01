"""Response to Codex audit-01, finding L2-F4 / claim-coverage note on PD-T?bivariate-lanczos-claude-205:
finite, exact (support-only, combinatorial) checks of the two lemmas written in PD-T?bivariate-lanczos-claude-209:

 (S) a one-relation selection satisfies condition (C) iff it is a 'staircase': at every degree t >= 1 the columns
     (t, j) with j <= s_t are created by X and those with j > s_t by Y, with s_1 = 0 and s_{t+1} - s_t in {0, 1};
     hence there are exactly 2^(n-1) (C)-selections of degree n;
 (W) for every (C)-selection the implicit-section definitions of PD-T?...-205 are acyclic, for ANY windows and
     reorthogonalisation sets W_c, L_c contained in {columns before c} (hypothesis (P)); moreover the degree-(s+1)
     part of supp H_A e_(s,j) is contained in {(s+1, j') : j' <= j + [A = Y]} (support lemma).

Independent implementation (support-only dependency graph; does not import developer or reviewer code except the
optional cross-check against reconstruction 01's rl2_cycles.analyse for n <= 5, block windows).
Usage (from this directory):
    python3 -I l2_audit01_staircase.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw
MEASURED / exhaustive finite check of combinatorial statements; the proofs are in the theory file."""
import sys, os, itertools, random, time, platform

sys.setrecursionlimit(100000)


def Nof(n):
    return (n + 1) * (n + 2) // 2


def cand(t, j):
    c = []
    if j <= t - 1:
        c.append(('X', j))
    if j >= 1:
        c.append(('Y', j - 1))
    return c


class Sel:
    """selection sel[(t, j)] = (op, parent j); windows/L sets given as functions of the column index"""

    def __init__(self, sel, n, window='block', rng=None):
        self.n = n
        self.idx = [(t, j) for t in range(n + 1) for j in range(t + 1)]
        self.pos = {k: i for i, k in enumerate(self.idx)}
        self.N, self.Nc = Nof(n), Nof(n - 1)
        self.creator, self.formed = {}, {'X': {}, 'Y': {}}
        for k in range(1, self.N):
            t, j = self.idx[k]
            op, pj = sel[(t, j)]
            p = self.pos[(t - 1, pj)]
            self.creator[k] = (op, p)
            if p < self.Nc:
                assert p not in self.formed[op]
                self.formed[op][p] = k
        self.W = {}
        for k in range(1, self.N):
            t, j = self.idx[k]
            if window == 'block':
                lo = Nof(t - 3) if t >= 3 else 0          # degrees t-2..t before k
                self.W[k] = set(range(lo, k))
            else:                                          # arbitrary subset of {0..k-1} (window + L set)
                self.W[k] = {l for l in range(k) if rng.random() < 0.5}

    def condC(self):
        return all((m in self.formed[A]) or self.creator[m][0] != A for A in 'XY' for m in range(1, self.Nc))

    def sections(self):
        """returns (ok, supports); ok False if the definitions are cyclic"""
        H, state = {}, {}

        def get(A, m):
            key = (A, m)
            if state.get(key) == 'done':
                return H[key]
            if state.get(key) == 'busy':
                raise RecursionError
            state[key] = 'busy'
            if m in self.formed[A]:
                k = self.formed[A][m]
                s = self.W[k] | {k}
            else:
                B, p = self.creator[m]
                s = set()
                for l in sorted(get(A, p)):
                    s |= get(B, l)
                for l in sorted(self.W[m]):
                    s |= get(A, l)
            H[key] = s
            state[key] = 'done'
            return s
        try:
            for A in 'XY':
                for m in range(self.Nc):
                    get(A, m)
        except RecursionError:
            return False, None
        return True, H

    def support_lemma(self, H):
        """degree-(s+1) part of supp H_A e_(s,j) within {j' <= j + [A=Y]} and supp within degree <= s+1"""
        for (A, m), s in H.items():
            t, j = self.idx[m]
            for l in s:
                tl, jl = self.idx[l]
                if tl > t + 1:
                    return False
                if tl == t + 1 and jl > j + (1 if A == 'Y' else 0):
                    return False
        return True


def is_staircase(sel, n):
    s_prev = None
    for t in range(1, n + 1):
        ops = [sel[(t, j)][0] for j in range(t + 1)]
        nx = sum(1 for o in ops if o == 'X')
        if ops != ['X'] * nx + ['Y'] * (t + 1 - nx):
            return False
        s_t = nx - 1
        if t == 1:
            if s_t != 0:
                return False
        elif s_t - s_prev not in (0, 1):
            return False
        s_prev = s_t
    return True


def staircases(n):
    for bits in itertools.product((0, 1), repeat=n - 1):
        s = [0]
        for b in bits:
            s.append(s[-1] + b)
        sel = {}
        for t in range(1, n + 1):
            st = s[t - 1]
            for j in range(t + 1):
                sel[(t, j)] = ('X', j) if j <= st else ('Y', j - 1)
        yield sel


def main():
    print(f"# l2_audit01_staircase.py python={platform.python_version()}", flush=True)
    t0 = time.time()
    # (1) exhaustive over all selections, n <= 6, block windows
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_L2'))
        import rl2_cycles
        have_ref = True
    except Exception as e:  # pragma: no cover
        have_ref = False
        print(f"  (reconstruction-01 cross-check unavailable: {e})")
    for n in range(2, 7):
        cols = [(t, j) for t in range(1, n + 1) for j in range(t + 1)]
        tot = nC = nstair = mism = cyc = lemma_bad = ref_mism = 0
        for combo in itertools.product(*[cand(t, j) for (t, j) in cols]):
            sel = dict(zip(cols, combo))
            S = Sel(sel, n)
            c = S.condC()
            st = is_staircase(sel, n)
            tot += 1; nC += c; nstair += st; mism += (c != st)
            if c:
                ok, H = S.sections()
                cyc += (not ok)
                if ok and not S.support_lemma(H):
                    lemma_bad += 1
            if have_ref and n <= 5:
                okr = S.sections()[0]
                cr, ok_ref = rl2_cycles.analyse(sel, n)
                ref_mism += (cr != c) or (ok_ref != okr)
        print(f"  n={n} exhaustive, block window: {tot} selections; (C) {nC}; staircase {nstair} (2^(n-1) = {2 ** (n - 1)}); "
              f"(C) != staircase: {mism}; (C) with cyclic definitions: {cyc}; support-lemma violations: {lemma_bad}"
              + (f"; disagreements with rl2_cycles.analyse: {ref_mism}" if have_ref and n <= 5 else ""), flush=True)
    # (2) all staircases, larger n, block windows
    for n in range(7, 14):
        cnt = cyc = bad = notC = 0
        for sel in staircases(n):
            S = Sel(sel, n)
            cnt += 1
            notC += (not S.condC())
            ok, H = S.sections()
            cyc += (not ok)
            if ok and not S.support_lemma(H):
                bad += 1
        print(f"  n={n} all {cnt} staircases, block window: not (C) {notC}; cyclic {cyc}; support-lemma violations {bad}",
              flush=True)
    # (3) all staircases with random arbitrary windows/L-sets inside {l < c} (hypothesis (P)), 3 draws each
    rng = random.Random(20261101)
    for n in range(2, 11):
        cnt = cyc = bad = 0
        for sel in staircases(n):
            for _ in range(3):
                S = Sel(sel, n, window='random', rng=rng)
                cnt += 1
                ok, H = S.sections()
                cyc += (not ok)
                if ok and not S.support_lemma(H):
                    bad += 1
        print(f"  n={n} staircases x 3 random windows/L-sets in {{l < c}}: {cnt} cases; cyclic {cyc}; "
              f"support-lemma violations {bad}", flush=True)
    # (4) named rules are staircases
    rules = {'bj': lambda t, j: ('X', j) if j == 0 else ('Y', j - 1),
             'mirror': lambda t, j: ('Y', t - 1) if j == t else ('X', j),
             'alt': lambda t, j: ('X', j) if 2 * j < t else ('Y', j - 1)}
    for nm, f in rules.items():
        for n in (6, 12, 20):
            sel = {(t, j): f(t, j) for t in range(1, n + 1) for j in range(t + 1)}
            S = Sel(sel, n)
            print(f"  rule {nm} n={n}: staircase {is_staircase(sel, n)}, (C) {S.condC()}, acyclic {S.sections()[0]}",
                  flush=True)
    print(f"# done in {time.time() - t0:.1f}s", flush=True)


if __name__ == '__main__':
    main()
