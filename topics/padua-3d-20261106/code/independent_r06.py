#!/usr/bin/env python3
"""Independent actual-node checks; imports no project mathematics.

Finite-field rank is only a characteristic-zero rank lower bound.
Floating Lebesgue values are mesh samples, not certified suprema.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import tempfile

import numpy as np
import sympy as sp


def indices(n, d=3):
    return [a for a in itertools.product(range(n + 1), repeat=d) if sum(a) <= n]


def fold(rows, denominator):
    return sorted({tuple(min(int(t) % denominator, -int(t) % denominator)
                         for t in row) for row in rows})


def modular_rank(matrix, prime):
    a = [[int(x) % prime for x in row] for row in matrix]
    r = 0
    for j in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        inv = pow(a[r][j], -1, prime)
        a[r] = [(v * inv) % prime for v in a[r]]
        for i in range(r + 1, len(a)):
            t = a[i][j]
            if t:
                a[i] = [(x - t * y) % prime for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def actual_certificate(rows, denominator, n, prime=None):
    if prime is None:
        k = 1
        while not sp.isprime(k * denominator + 1) or k * denominator + 1 == 2:
            k += 1
        prime = k * denominator + 1
    if not sp.isprime(prime) or (prime - 1) % denominator:
        raise ValueError('not a splitting prime')
    root = pow(int(sp.primitive_root(prime)), (prime - 1) // denominator, prime)
    if pow(root, denominator, prime) != 1 or any(
            pow(root, denominator // q, prime) == 1 for q in sp.factorint(denominator)):
        raise ValueError('root has wrong order')
    nodes = fold(rows, denominator)
    inv2 = pow(2, -1, prime)
    coords = [[(pow(root, t, prime) + pow(root, -t, prime)) * inv2 % prime
               for t in row] for row in nodes]
    # Monomials, independent of the producer's character/Chebyshev dictionary.
    matrix = [[math.prod(pow(x, a, prime) for x, a in zip(row, alpha)) % prime
               for alpha in indices(n, len(row))] for row in coords]
    return {'denominator': denominator, 'prime': prime, 'root': root,
            'nodes': len(nodes), 'degree': n, 'rank_lower': modular_rank(matrix, prime),
            'matrix_sha256': hashlib.sha256(json.dumps(matrix).encode()).hexdigest()}


def mesh_value(rows, denominator, n, side=21):
    nodes = np.cos(2 * np.pi * np.array(fold(rows, denominator)) / denominator)
    alpha = indices(n)
    def vandermonde(x):
        tables = [np.polynomial.chebyshev.chebvander(x[:, j], n) for j in range(3)]
        return np.column_stack([tables[0][:, a] * tables[1][:, b] * tables[2][:, c]
                                for a, b, c in alpha])
    v = vandermonde(nodes)
    inv = np.linalg.inv(v)
    mesh = np.array(list(itertools.product(np.cos(np.linspace(0, np.pi, side)), repeat=3)))
    best = max(float(np.abs(vandermonde(x) @ inv).sum(axis=1).max())
               for x in np.array_split(mesh, max(1, len(mesh) // 400)))
    return {'mesh_side': side, 'sampled_lambda': best,
            'inverse_residual': float(np.max(np.abs(v @ inv - np.eye(len(v)))))}


def controls():
    t7 = [[101 * ((7*k + 5*l) % 10) + 10,
           101 * ((7*k) % 10) + 20,
           101 * ((4*k + 5*l) % 10) + 40]
          for k in range(10) for l in range(2)]
    t8 = [[6*k*z + phase for z, phase in zip((1, 2, 7), (30, 75, 69))]
          for k in range(20)]
    traces = []
    for n in range(1, 25):
        values = [sum((-1)**sum(a[:r]) for a in indices(n)) for r in (1, 2, 3)]
        N = math.comb(n+3, 3)
        traces.append({'n': n, 'N': N, 'trace': values,
                       'parity_allowed': N % 2 == 1 or 0 in values})
    padua = []
    for n in range(1, 13):
        M = 2*n*(n+1)
        nodes = fold([[k*(n+1), k*n] for k in range(M)], M)
        expected = math.comb(n+2, 2)
        if len(nodes) != expected:
            raise RuntimeError('Padua count failure')
        fixed = sum(tuple(min((t+z*M//2)%M, -(t+z*M//2)%M)
                          for t,z in zip(row,(n+1,n))) == row for row in nodes)
        if fixed != n//2+1:
            raise RuntimeError('Padua trace failure')
        padua.append([n, len(nodes), fixed])
    return {'t7': actual_certificate(t7, 1010, 3, 8081),
            't7_quality': mesh_value(t7, 1010, 3),
            't8': actual_certificate(t8, 120, 3, 241),
            't8_quality': mesh_value(t8, 120, 3),
            'trace': traces, 'padua_count_trace': padua}


def t10_global():
    """Independent full HNF search, testing membership by v adj(B) mod det."""
    results = []
    for n,bound in [(1,2),(2,12),(3,38)]:
        K = np.array([v for v in itertools.product(range(1-2*n,2*n),repeat=3)
                      if 0 < sum(map(abs,v)) < 2*n],dtype=np.int64)
        tested = 0
        for q in range(1,bound+1):
            winners = []
            for a in sp.divisors(q):
                for b in sp.divisors(q//a):
                    c=q//a//b
                    for r,s,t in itertools.product(range(b),range(c),range(c)):
                        tested += 1
                        adj = np.array([[b*c,-r*c,r*t-b*s],[0,a*c,-a*t],[0,0,a*b]])
                        if not np.any(np.all((K@adj)%q==0,axis=1)):
                            winners.append([a,b,c,r,s,t])
            if winners:
                results.append({'n':n,'minimum_det':q,'hnfs_tested':tested,
                                'minimizers':len(winners)})
                break
    return results


def t7_primes():
    # Projective lines in F_p^3, independent of producer HNF enumeration.
    from collections import Counter
    distribution = Counter()
    for b,c in itertools.product(range(1,19),repeat=2):
        columns = []
        for alpha in indices(2):
            freq = Counter(sum(e*z for e,z in zip(signs,(1,b,c))) % 19
                           for signs in itertools.product(*[[-a,a] if a else [0]
                                                            for a in alpha]))
            columns.append([freq[j] for j in range(19)])
        rank = sp.Matrix(columns).T.rank()
        distribution[rank] += 1
    return {'all_prime_orders':list(sp.primerange(10,81)),
            'total_groups':sum(int(p*p+p+1) for p in sp.primerange(10,81)),
            'p19_groups':381,'p19_coordinate_kernel':57,
            'p19_nonzero_projection_rank_distribution':dict(distribution)}


def t8_counts(receipt):
    checked=[]
    for case in json.loads(receipt.read_text())['rows']:
        M,N=case['M'],case['N']; D=2*M*257; total=passing=0
        for b,c in itertools.combinations(range(1,M),2):
            z=(1,b,c)
            for h in (0,1):
                for J in [(1,),(2,),(1,2)]:
                    nums=[h*j*257 if i not in J else 2*M for i,j in enumerate(z)]
                    actual=fold([[k*j*(D//M)+a for j,a in zip(z,nums)] for k in range(M)],D)
                    total+=1;passing+=len(actual)==N
        if (total,passing)!=(case['count_strata_tested'],case['count_permitted']):
            raise RuntimeError('Direct fold count differs from gcd count')
        checked.append({'M':M,'N':N,'strata':total,'permitted':passing})
    return checked


def t9_algebra():
    sums = []
    for n in range(25):
        direct = sum(math.prod((a+1)**2 for a in alpha) for alpha in indices(n))
        closed = sum(math.comb(3,j)*math.comb(n-j+9,9) for j in range(min(3,n)+1))
        if direct != closed:
            raise RuntimeError('R-Leja coefficient formula')
        sums.append([n,direct])
    tetra = []
    signs = [e for e in itertools.product((-1,1),repeat=3) if math.prod(e)==1]
    for b in [sp.Rational(1),sp.Rational(3,2),sp.Rational(2),sp.Rational(3),sp.Rational(5)]:
        value=max(sum(abs(1+e[0]*v[0]*b+e[1]*v[1]+e[2]*v[2])/4 for e in signs)
                  for v in itertools.product((-1,1),repeat=3))
        if value != max(b,(b+3)/2):
            raise RuntimeError('Tetrahedron formula')
        tetra.append([str(b),str(value)])
    B=sp.Matrix([[2,-1,-3],[3,-2,1],[1,3,-2]])/3
    f=lambda n:n**3-108*n*n-198*n-108
    return {'rleja_sum_0_to_24':sums,'tetrahedron_b_lambda':tetra,
            'critical_det':str(abs(B.det())),'packing_comparison_f109_f110':[f(109),f(110)]}


def t10_actual(raw):
    from collections import Counter
    cases = json.loads(raw.read_text())['rows']
    selected = [r for r in cases if (r['n'],r['family']) in
                [(3,'K-table'),(6,'parity-aniso'),(7,'parity-aniso'),(12,'K-table')]]
    out=[]
    for case in selected:
        n=case['n']; B=sp.Matrix(case['B']); q=int(B.det()); inverse=B.inv()
        numerators=[]
        for j in itertools.product(*[range(int(B[i,i])) for i in range(3)]):
            point=q*inverse*sp.Matrix(j)
            numerators.append([int(v)%q for v in point])
        cert=actual_certificate(numerators,q,n)
        if cert['rank_lower']!=case['rank'] or cert['nodes']!=case['fold']:
            raise RuntimeError('Independent actual-node T10 rank/count mismatch')
        cert['family']=case['family']
        if n in (6,7):
            counts=Counter(tuple(min(t,q-t) for t in row) for row in numerators)
            nodes=sorted(counts);weights=np.array([counts[v]/q for v in nodes])
            alpha=indices(n)
            def basis(x):
                tables=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
                return np.column_stack([np.prod([tables[j][:,a[j]] for j in range(3)],axis=0) for a in alpha])
            V=basis(np.cos(2*np.pi*np.array(nodes)/q))
            scaling=np.array([2**sum(i>0 for i in a) for a in alpha])
            rawC=scaling[:,None]*V.T*weights
            gram=V.T@(weights[:,None]*V)
            lsC=np.linalg.solve(gram,V.T*weights)
            norms=[0.,0.];axis=np.cos(np.linspace(0,np.pi,41))
            for x in axis:
                evaluation=basis(np.array([(x,y,z) for y,z in itertools.product(axis,repeat=2)]))
                for i,C in enumerate((rawC,lsC)):
                    norms[i]=max(norms[i],float(np.abs(evaluation@C).sum(axis=1).max()))
            cert['raw_LS_norm41']=norms
            cert['raw_LS_reproduction_residual']=[float(np.linalg.norm(C@V-np.eye(len(alpha)),np.inf)) for C in (rawC,lsC)]
        out.append(cert)
    return {'input_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'selected':out}


def t7_census():
    """Independent reconstruction of the complete n2 finite reduction.

    Uses projected phase lattices, and directly folded actual nodes.
    Positive ranks decide existence/generic rank, not every phase's rank.
    """
    from collections import Counter
    from sympy.matrices.normalforms import hermite_normal_form
    counts=Counter();survivors=[];unresolved=[]
    degree=indices(2)
    for m in range(10,81):
        for a in sp.divisors(m):
            for b in sp.divisors(m//a):
                c=m//a//b
                for r,s,t in itertools.product(range(b),range(c),range(c)):
                    counts['groups_seen']+=1
                    adj=np.array([[b*c,-r*c,r*t-b*s],[0,a*c,-a*t],[0,0,a*b]],dtype=np.int64)
                    orders=[m//math.gcd(m,*map(int,row)) for row in adj]
                    if min(orders)<=2:
                        counts['groups_killed_low_projection']+=1;continue
                    if max(orders)>20:
                        counts['groups_killed_high_projection']+=1;continue
                    if sp.isprime(m):
                        counts['groups_covered_prime_block']+=1;continue
                    if m==10:
                        counts['groups_killed_no_fold_trace']+=1;continue
                    integers=np.array(list(itertools.product(range(a),range(b),range(c))))
                    points=(integers@adj.T)%m
                    hnf=[int(v) for v in (a,b,c,r,s,t)]
                    for mask in range(8):
                        active=[j for j in range(3) if mask>>j&1]
                        if active:
                            gen=sp.diag(*[orders[j] for j in active]).row_join(sp.Matrix(
                                [[2*orders[j]*int(adj[j,k])//m for k in range(3)] for j in active]))
                            Q=hermite_normal_form(gen)
                            representatives=itertools.product(*[range(int(Q[j,j])) for j in range(len(active))])
                        else: representatives=[()]
                        for rep in representatives:
                            phase=[-1]*3
                            for j,k in zip(active,rep):phase[j]=k
                            counts['quotient_strata_seen']+=1
                            D=math.lcm(m,1009,*[2*v for v in orders])
                            nums=[(1+3*j)*(D//1009) if phase[j]<0 else phase[j]*(D//(2*orders[j])) for j in range(3)]
                            rows=(points*(D//m)+nums)%D
                            nodes=fold(rows,D)
                            if any(len({node[j] for node in nodes})<=2 for j in range(3)):
                                counts['strata_killed_projection']+=1;continue
                            if len(nodes)!=10:
                                counts['strata_wrong_count']+=1;continue
                            counts['target_count_strata']+=1
                            trace_failure=False
                            for h in points:
                                if not any(h) or any((2*h)%m):continue
                                e=2*h//m
                                nodal=sum(all(node[j]*4==D for j in range(3) if e[j]) for node in nodes)
                                polynomial=sum((-1)**sum(int(e[j])*alpha[j] for j in range(3)) for alpha in degree)
                                if nodal!=polynomial:trace_failure=True;break
                            if trace_failure:
                                counts['strata_killed_fixed_trace']+=1;continue
                            relation=False
                            for u in itertools.product(range(-2,3),repeat=3):
                                if not any(u) or sum(v!=0 for v in u)>2:continue
                                if any(v and phase[j]<0 for j,v in enumerate(u)):continue
                                if any((np.array(u)@adj)%m):continue
                                compat=sum(sp.Rational(v*phase[j],orders[j]) for j,v in enumerate(u) if v)
                                if compat.q==1:relation=True;break
                            if relation:
                                counts['strata_killed_short_relation']+=1;continue
                            cert=actual_certificate(rows,D,2)
                            entry={'hnf':hnf,'phase_stratum':phase,'certificate':cert}
                            if cert['rank_lower']==10:
                                counts['strata_full_rank_witness']+=1;survivors.append(entry)
                            else:
                                counts['strata_unresolved']+=1;unresolved.append(entry)
        print(json.dumps({'census_order_complete':m,'groups_seen':counts['groups_seen']}),flush=True)
    return {'counts':dict(counts),'survivors':survivors,'unresolved':unresolved,
            'prime_block_separate':'independent-r06-t7-primes.json',
            'rank_semantics':'maximum/generic stratum rank; exceptional phase loci not classified'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--t8', type=Path)
    parser.add_argument('--t7-raw', type=Path)
    parser.add_argument('--t10-global', action='store_true')
    parser.add_argument('--t7-primes', action='store_true')
    parser.add_argument('--t9-algebra', action='store_true')
    parser.add_argument('--t10-actual', type=Path)
    parser.add_argument('--t8-counts', type=Path)
    parser.add_argument('--t7-census', action='store_true')
    args = parser.parse_args()
    out = args.output or Path(tempfile.mkdtemp(prefix='padua-independent-r06-'))/'controls.json'
    result = {'rules_input': '7afa6a54a4db4652267e38cd48658ba435d20481',
              'command': sys.argv, 'python': platform.python_version(),
              'numpy': np.__version__, 'sympy': sp.__version__,
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'controls': controls() if not any([args.t8,args.t7_raw,args.t10_global,args.t7_primes,args.t9_algebra,args.t10_actual,args.t8_counts,args.t7_census]) else {}}
    if args.t7_census:
        result['t7_census'] = t7_census()
    if args.t8_counts:
        result['t8_counts'] = t8_counts(args.t8_counts)
    if args.t10_actual:
        result['t10_actual'] = t10_actual(args.t10_actual)
    if args.t7_primes:
        result['t7_primes'] = t7_primes()
    if args.t9_algebra:
        result['t9_algebra'] = t9_algebra()
    if args.t10_global:
        result['t10_global'] = t10_global()
    if args.t8:
        source = json.loads(args.t8.read_text())
        checked = []
        cases = []
        for parent in source['rows']:
            cases.extend([{**parent, **child} for child in parent['survivors']]
                         if 'survivors' in parent else [parent])
        for case in cases:
            if 'phase_nums' not in case and 'mask' not in case:
                continue
            den, M, n = case['phase_den'], case['M'], case['n']
            D = math.lcm(den, M)
            phases = case.get('phase_nums', case.get('mask'))
            if isinstance(phases[0], int):
                phases = [phases]
            rows = [[k*z*(D//M)+a*(D//den) for z,a in zip(case['z'], phase)]
                    for phase in phases for k in range(M)]
            cert = actual_certificate(rows, D, n)
            expected = max(c['rank'] for c in case['certificate']['checks'])
            if cert['rank_lower'] != expected:
                raise RuntimeError('T8 independent rank disagrees; inspect prime effects')
            cert['generator'] = case['z']
            if 'quality' in case:
                cert['quality'] = mesh_value(rows, D, n)
                delta = abs(cert['quality']['sampled_lambda']-case['quality']['sampled_lebesgue'])
                cert['sample_difference'] = delta
                if delta > 1e-7 * case['quality']['sampled_lebesgue']:
                    raise RuntimeError('T8 quality disagreement')
            checked.append(cert)
        result['t8'] = {'input_sha256': hashlib.sha256(args.t8.read_bytes()).hexdigest(),
                        'checked': checked}
    if args.t7_raw:
        data = [json.loads(line) for line in args.t7_raw.read_text().splitlines()]
        ranks = {}
        full = 0
        best = float('inf')
        for case in data:
            a,b,c,r,s,t = case['hnf']
            B = sp.Matrix([[a,r,s],[0,b,t],[0,0,c]])
            inv = B.inv()
            D = math.lcm(a*b*c, case['phase_denominator'])
            rows = []
            for k in itertools.product(range(a),range(b),range(c)):
                pt = inv * sp.Matrix(k)
                rows.append([int(D*pt[j])+case['phase'][j]*(D//case['phase_denominator'])
                             for j in range(3)])
            cert = actual_certificate(rows,D,3,case['prime'])
            rank = cert['rank_lower']
            if cert['nodes'] != case['count'] or rank != case['rank']:
                raise RuntimeError('T7 direct reconstruction disagrees')
            ranks[rank] = ranks.get(rank,0)+1
            if rank == 20:
                full += 1
                best = min(best, mesh_value(rows,D,3)['sampled_lambda'])
        result['t7_sample'] = {'raw_sha256': hashlib.sha256(args.t7_raw.read_bytes()).hexdigest(),
                               'rows':len(data),'rank_lower_distribution':ranks,
                               'full_rank_count':full,'best_sampled_lambda':best}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(out), 'bytes': out.stat().st_size,
                      'sections': list(result)}))


if __name__ == '__main__':
    main()
