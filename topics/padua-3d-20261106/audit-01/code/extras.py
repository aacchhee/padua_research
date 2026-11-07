import itertools, math, sys, collections
sys.path.insert(0, '.')
import claude_t23_check as C
fold = C.fold
# 1. residual symmetry classes of the normalized census (unit*k + axis perms + sign fold)
def canon(z, M):
    best = None
    for u in range(1, M):
        if math.gcd(u, M) != 1: continue
        w = [fold(u*x, M) for x in z]
        for p in itertools.permutations(w):
            if p[0] == 1:
                t = tuple(sorted(p[1:]))
                best = t if best is None or t < best else best
    return best
for n in (2, 3, 4):
    N = math.comb(n+3, 3); M = 2*N-1
    cls = collections.defaultdict(list)
    for b, c in itertools.combinations(range(1, N), 2):
        cls[canon((1, b, c), M)].append((b, c))
    print('n', n, 'pairs', sum(len(v) for v in cls.values()), 'classes', len(cls))
    if n in (2, 4):
        full = {2: [(3,7),(4,6),(5,8),(7,8)], 4: [(11,15),(15,19),(21,29),(25,30)]}[n]
        print('  survivor classes', {f: canon((1,)+f, M) for f in full})
# 1b. node sets literally equal up to axis permutation (exact folded residues)
def nodeset(z, M, N):
    return {tuple(fold(k*x, M) for x in z) for k in range(N)}
for n, a, b in [(4, (1,15,19), (1,21,29)), (4, (1,11,15), (1,25,30)), (2, (1,3,7), (1,4,6)), (2, (1,3,7), (1,5,8))]:
    N = math.comb(n+3, 3); M = 2*N-1
    A = nodeset(a, M, N); B = nodeset(b, M, N)
    ok = any({tuple(p[i] for i in perm) for p in A} == B for perm in itertools.permutations(range(3)))
    print('equal up to axis permutation', n, a, b, ok)
# 2. node counts of non-unit triples mod 39
cnt = collections.Counter()
for z in itertools.product(range(39), repeat=3):
    if any(math.gcd(x, 39) == 1 for x in z): continue
    cnt[len({tuple(fold(k*x, 39) for x in z) for k in range(39)})] += 1
print('non-unit node-count distribution', dict(sorted(cnt.items())))
# 3. d=2 shared-frequency example: n=2, M=11, z=(1,3), monomial basis 1,x,y,x2,xy,y2
cols = []
for (i, j) in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
    cols.append(C.laurent_mono({(i, j, 0): 1}, (1, 3, 0), 11, 2))
print('d2 example rank', C.exact_rank([list(r) for r in zip(*cols)]))
# 4. primitivity of cover vectors
import json
cov = json.load(open(sys.argv[1]))
print('all primitive', all(math.gcd(*[v for _, v in t]) == 1 for _, _, _, t in cov['witnesses']))
print('max |coef|', max(abs(v) for _, _, _, t in cov['witnesses'] for _, v in t))
