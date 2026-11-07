import json, copy, sys, itertools
sys.path.insert(0, '.')
import claude_t23_check as C
cover = json.load(open(sys.argv[1]))
caught = 0; trials = 0
for idx in [0, 18, 40, 100, 170]:
    for mode in ('coef', 'drop', 'swapaxis'):
        bad = copy.deepcopy(cover)
        b, c, r, terms = bad['witnesses'][idx]
        if mode == 'coef': terms[0][1] += 1
        elif mode == 'drop':
            if len(terms) < 2: continue
            terms.pop()
        else:
            terms[:] = [[[a[0], a[2], a[1]], v] for a, v in terms]
            if all(a[1] == a[2] for a, _ in terms): continue
        trials += 1
        try:
            C.part_AB(bad)
        except AssertionError:
            caught += 1
# field method alone detects a non-annihilator
F = C.Field(39)
nz = [k for k in range(20) if not C.F_is_zero(C.eval_node_field(F, {(1,0,0):1,(0,0,0):-1}, (k,2*k,3*k), 3))] if hasattr(C,'F_is_zero') else [k for k in range(20) if C.eval_node_field(F, {(1,0,0):1,(0,0,0):-1}, (k,2*k,3*k), 3) != []]
print('mutations', trials, 'caught', caught, 'x-1 nonzero at nodes', len(nz), 'of 20 (expect 19)')
# coverage mutation: drop one witness
bad = copy.deepcopy(cover); bad['witnesses'].pop(); bad['count'] = 170
try:
    C.part_AB(bad); print('coverage mutation NOT caught')
except AssertionError:
    print('coverage mutation caught')
# zero-index multiplicities: folded D columns sum to 8 for z=(1,2,5), M=39
D = {}
for a in C.mono_basis(3):
    s = [0]*20
    for eps in itertools.product((-1,1), repeat=3):
        s[C.fold(sum(e*x*z for e,x,z in zip(eps,a,(1,2,5))),39)] += 1
    assert sum(s) == 8
print('folded column sums all 8')
