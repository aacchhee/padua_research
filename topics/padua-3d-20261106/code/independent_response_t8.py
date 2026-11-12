#!/usr/bin/env python3
"""Supplementary exact checks, independent of developer helper imports.

Reflection counts use literal one-dimensional folded grids and binary syndromes.
Symmetries use multiplication of generator residues, rather than node-set hashes.
No prose is hash-pinned. Raw independent reruns belong in /tmp.
"""
import argparse
from collections import Counter
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import importlib.util
import shutil
import sys

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def reflection_census(n):
    target = math.comb(n + 3, 3)
    cap = 2 * target
    # All admissible codes, reconstructed directly from the d=3 classification.
    codes = [(0,), (0, 3), (0, 5), (0, 6), (0, 7), (0, 3, 5, 6)]
    rows = []
    for code in codes:
        active = [any(b & (1 << j) for b in code) for j in range(3)]
        axes = []
        for a in active:
            types = Counter()
            for m in range(1, cap + 1):
                if a and m % 2:
                    continue
                for phase in ([0] if a else [0, 1]):
                    folded = {min((2*k+phase) % (2*m), (-2*k-phase) % (2*m))
                              for k in range(m)}
                    if a:
                        e = sum((v // 2) % 2 == 0 for v in folded)
                        o = len(folded) - e
                    else:
                        e, o = len(folded), 0
                    types[(e, o, len(folded), m//2)] += 1
            axes.append(list(types.items()))
        words = [p for p in range(8) if all(active[j] or not(p & (1<<j))
                                            for j in range(3))]
        syndromes = {}
        for p in words:
            key = tuple((p & b).bit_count() % 2 for b in code)
            syndromes.setdefault(key, []).append(p)
        third = np.array([k for k, _ in axes[2]], dtype=np.int64)
        mult = np.array([v for _, v in axes[2]], dtype=np.int64)
        total = short = alias = live = 0
        for patterns in syndromes.values():
            for (x, mx), (y, my) in it.product(axes[0], axes[1]):
                count = sum(x[p & 1] * y[(p >> 1) & 1] * third[:, (p >> 2) & 1]
                            for p in patterns)
                hits = count == target
                low = (min(x[2], y[2]) <= n) | (third[:, 2] <= n)
                pair = ((int(x[3] <= n) + int(y[3] <= n) + (third[:, 3] <= n)) >= 2
                        if len(code) == 4 else np.zeros(len(third), dtype=bool))
                weight = mult * mx * my
                total += int(weight[hits].sum())
                short += int(weight[hits & low].sum())
                alias += int(weight[hits & ~low & pair].sum())
                live += int(weight[hits & ~low & ~pair].sum())
        rows.append(dict(binary_code=list(code), target_count_cosets=total,
                         short_projection=short, pair_alias_after_short=alias,
                         surviving_necessary_screens=live))
    return dict(degree=n, cap=cap, classes=rows,
                target_count_cosets=sum(r['target_count_cosets'] for r in rows))


def generator_orbit(z, m):
    """Exact equivalence for a primitive cyclic orbit with a unit coordinate.

    Its k=1 image must be the image of some k' of the other orbit. For two
    generators with unit coordinate, that parameter is a unit. Coordinate
    sign choices and permutations therefore give the complete equivalence.
    """
    return min(tuple(sorted(min(a*u % m, -a*u % m) for a in z))
               for u in range(1, m) if math.gcd(u, m) == 1)


def symmetry():
    out = []
    for n in (2, 3, 4):
        target = math.comb(n+3, 3)
        m = 2*target-1
        groups = Counter(generator_orbit((1, b, c), m)
                         for b, c in it.combinations(range(1, target), 2))
        out.append(dict(degree=n, normalized_pairs=sum(groups.values()), classes=len(groups)))
    for m, group in [(19, [(1,3,7), (1,4,6), (1,5,8)]),
                     (69, [(1,15,19), (1,21,29)]),
                     (69, [(1,11,15), (1,25,30)])]:
        assert len({generator_orbit(z, m) for z in group}) == 1
    return out


def padua():
    out = []
    for n in range(1, 13):
        m = 2*n*(n+1)
        z = (n+1, n)
        folded = {tuple(min(k*a % m, -k*a % m) for a in z) for k in range(m)}
        parity = {(i*(n+1), j*n) for i in range(n+1) for j in range(n+2)
                  if (i+j) % 2 == 0}
        assert folded == parity
        assert len(folded) == math.comb(n+2, 2)
        assert [len({x[j] for x in folded}) for j in range(2)] == [n+1, n+2]
        short = [(a,b) for a in range(-2*n, 2*n+1) for b in range(-2*n, 2*n+1)
                 if 0 < abs(a)+abs(b) <= 2*n and (a*z[0]+b*z[1]) % m == 0]
        assert short == [(-2*n, 0), (2*n, 0)]
        out.append(dict(degree=n, modulus=m, nodes=len(folded), short_dual_vectors=short))
    return out


def field_rank(A, p):
    A = np.asarray(A, dtype=np.int64).copy() % p
    r = 0
    for j in range(A.shape[1]):
        choices = np.flatnonzero(A[r:, j])
        if not len(choices):
            continue
        i = r + int(choices[0])
        A[[i, r]] = A[[r, i]]
        A[r] = A[r] * pow(int(A[r, j]), -1, p) % p
        for i in range(r+1, len(A)):
            if A[i, j]:
                A[i] = (A[i] - A[i, j] * A[r]) % p
        r += 1
        if r == len(A):
            break
    return r


def actual_node_rank(n, M, z, phase=(0,0,0)):
    L = math.lcm(M,24) if any(phase) else M
    p = L+1
    while not sp.isprime(p):
        p += L
    rho = pow(int(sp.primitive_root(p)), (p-1)//L, p)
    assert pow(rho,L,p)==1
    assert all(pow(rho,L//q,p)!=1 for q in sp.factorint(L))
    exps = list(a for a in it.product(range(n+1),repeat=3) if sum(a)<=n)
    points = {tuple(min((k*a*(L//M)+h*(L//24))%L,
                       (-k*a*(L//M)-h*(L//24))%L)
                    for a,h in zip(z,phase)) for k in range(M)}
    vals = [tuple((pow(rho,h,p)+pow(rho,-h % L,p))*pow(2,-1,p)%p for h in pt)
            for pt in points]
    A = [[math.prod(pow(x,a,p) for x,a in zip(pt,alpha))%p for alpha in exps]
         for pt in vals]
    return len(points), field_rank(A,p), p


def verify_unshifted_null(n,M,z,v):
    exps = [a for a in it.product(range(n+1),repeat=3) if sum(a)<=n]
    assert len(v)==len(exps) and any(v)
    # Fourier coefficients of 8*p(cos(theta)); full, not folded, residues.
    coeff = [0]*M
    for a,c in zip(exps,v):
        for signs in it.product((-1,1),repeat=3):
            coeff[sum(x*y*s for x,y,s in zip(a,z,signs))%M] += c
    return not any(coeff)


def phase_node_certificates(receipt):
    w = sp.Symbol('w')
    modulus = sp.Poly(sp.cyclotomic_poly(120,w),w,domain=sp.QQ)
    def rem(v):
        return sp.rem(sp.Poly(v,w,domain=sp.QQ),modulus)
    rows = []
    for family in receipt['families']:
        row = family['rows'][0]
        assert row['n']==2 and row['M']==10
        terms = row['certificate']['cyclotomic_null']
        def evaluate(k,mutate=False):
            coordinates=[]
            for a,h in zip(row['z'],(6,4,3)):
                t=(12*k*a+5*h)%120
                coordinates.append(rem((w**t+w**((-t)%120))/2))
            total = rem(int(mutate))
            for alpha,cs in terms:
                cp=sum(sp.Rational(c)*w**(5*(len(cs)-1-i)) for i,c in enumerate(cs))
                term=rem(cp)
                for a,x in zip(alpha,coordinates):
                    tx=[rem(1),x,rem(2*x.as_expr()**2-1)][a]
                    term=rem(term.as_expr()*tx.as_expr())
                total=rem(total.as_expr()+term.as_expr())
            return total.is_zero
        assert all(evaluate(k) for k in range(10))
        assert not evaluate(0,True)
        count,rank,p=actual_node_rank(2,10,row['z'],(6,4,3))
        assert count==10 and rank==row['certificate']['rank']
        rows.append(dict(family=family['name'],nodes=count,rank_lower=rank,
                         prime=p,exact_node_witness_checks=10,mutation_rejected=True))
    return rows


def t8_checks(scratch):
    # Run unchanged producer code with output destinations rebound in memory.
    scratch.mkdir(parents=True,exist_ok=True)
    (scratch/'evidence').mkdir(exist_ok=True)
    for rel in ['preregistration-T8.md','evidence/t2-n3-null-cover.json']:
        shutil.copy2(ROOT/rel,scratch/rel)
    sys.path.insert(0,str(ROOT/'code'))
    spec=importlib.util.spec_from_file_location('t8_cyclic',ROOT/'code/t8_cyclic.py')
    core=importlib.util.module_from_spec(spec)
    sys.modules['t8_cyclic']=core
    spec.loader.exec_module(core)
    core.TOP=scratch
    core.SCRATCH=scratch/'raw'
    core.controls()
    for n in (2,3):
        core.census(n)
    for n in (5,6):
        core.odd(n)
    import t8_phases
    t8_phases.main()
    replays=[]
    for path in sorted((scratch/'evidence').glob('t8*.json')):
        actual=json.loads(path.read_text())
        expected=json.loads((ROOT/'evidence'/path.name).read_text())
        # Prose may receive dated additions; do not pin its historical digest.
        omit={'seconds','raw_path','versions','preregistration_sha256'}
        assert {k:v for k,v in actual.items() if k not in omit} == {
            k:v for k,v in expected.items() if k not in omit}, path.name
        replays.append(dict(receipt=path.name,sha256=sha(path),
                            raw_sha256=actual.get('raw_sha256'),scientific_fields_equal=True))
    independent=[]
    for name,n in [('unshifted-n2',2),('unshifted-n3',3),('odd-n5',5),('odd-n6',6)]:
        counts=Counter()
        ranks=Counter()
        for line in (scratch/'raw'/f't8-{name}.jsonl').read_text().splitlines():
            row=json.loads(line)
            if 'rank' not in row:
                continue
            M,z=row['M'],row['z']
            count,r,p=actual_node_rank(n,M,z)
            assert count==math.comb(n+3,3) and r==row['rank'], row
            counts['actual_node_modular_rank_checks']+=1
            ranks[r]+=1
            if row['null'] is not None:
                assert verify_unshifted_null(n,M,z,row['null'])
                counts['exact_null_checks']+=1
            else:
                counts['certified_fullrank']+=1
        independent.append(dict(screen=name,**counts))
    return dict(producer_replays=replays,actual_node_checks=independent,
                phase_checks=phase_node_certificates(json.loads((ROOT/'evidence/t8-phases.json').read_text())),
                scope='complete U n2,n3 and O n5,n6 reruns; every retained null checked exactly; '
                      'all ranks corroborated by actual-node modular lower bounds; P three rules at n2')


def even_checks(scratch):
    import t8_even_family
    t8_even_family.main()
    actual=json.loads((scratch/'evidence/t8-even-family.json').read_text())
    expected=json.loads((ROOT/'evidence/t8-even-family.json').read_text())
    def clean(v):
        if isinstance(v,dict):
            return {k:clean(x) for k,x in v.items() if k not in
                    {'seconds','search_seconds','raw_path','versions','preregistration_sha256'}}
        if isinstance(v,list):
            return [clean(x) for x in v]
        return v
    assert clean(actual)==clean(expected)
    rows=[]
    for r in actual['rows']:
        n,N,M=r['n'],r['N'],r['M']
        prefix=it.islice(((1,b,c) for b,c in it.combinations(range(1,N),2)
                         if (b+c)%2),r['visited_candidates'])
        raw=[json.loads(x) for x in Path(r['raw_path']).read_text().splitlines()]
        assert [tuple(x['z']) for x in raw]==list(prefix)
        for x in raw[:-1]:
            assert x['rank']<N and verify_unshifted_null(n,M,x['z'],x['null'])
        assert raw[-1]['z']==r['selected'] and raw[-1]['rank']==N
        count,rank,p=actual_node_rank(n,M,r['selected'])
        assert count==rank==N
        # Separate floating cardinal evaluator, fixed Chebyshev basis and mesh.
        points=sorted({tuple(min(k*a%M,-k*a%M) for a in r['selected']) for k in range(M)})
        physical=np.cos(2*np.pi*np.asarray(points)/M)
        exps=[a for a in it.product(range(n+1),repeat=3) if sum(a)<=n]
        def basis(points):
            tables=[np.polynomial.chebyshev.chebvander(points[:,j],n) for j in range(3)]
            return np.column_stack([tables[0][:,a]*tables[1][:,b]*tables[2][:,c] for a,b,c in exps])
        V=basis(physical)
        axis=np.cos(np.pi*np.arange(21)/20)
        mesh=np.asarray(list(it.product(axis,repeat=3)))
        value=float(np.max(np.sum(np.abs(np.linalg.solve(V.T,basis(mesh).T)),axis=0)))
        assert math.isclose(value,r['quality']['sampled_lebesgue'],rel_tol=1e-10)
        rows.append(dict(degree=n,selected=r['selected'],prime=p,rank=rank,
                         prefix_nulls=len(raw)-1,sampled_lebesgue=value))
    assert actual['kill']=='two_consecutive_admissible_Leja_losses_n_ge6'
    return dict(producer_scientific_fields_equal=True,rows=rows,kill=actual['kill'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--t8', action='store_true')
    ap.add_argument('--even', action='store_true',help='also replay final T8 E continuation')
    ap.add_argument('--scratch',type=Path,default=Path('/tmp/response-t8-independent'))
    args = ap.parse_args()
    reflections = [reflection_census(n) for n in range(2, 7)]
    expected = json.loads((ROOT / 'evidence/t1-full-enum.json').read_text())['rows']
    for actual, prior in zip(reflections, expected):
        assert actual['classes'] == prior['classes'], (actual, prior)
    sym = symmetry()
    assert [r['classes'] for r in sym] == [18,100,301]
    result = dict(schema='padua-3d-independent-response-t8-v1', verdict='PASS',
                  rules_sha='120a19ee71baa8e7834b3b183798df2cf489c432',
                  arithmetic='Python integers and exact numpy int64, maximum count <= 85^3',
                  python=platform.python_version(), numpy=np.__version__,
                  inputs={p: sha(ROOT/p) for p in [
                      'code/t1_full_enum.py', 'code/t2_symmetry_check.py',
                      'evidence/t1-full-enum.json', 'evidence/t2-symmetry-check.json']},
                  checker_sha256=sha(__file__), reflection=reflections,
                  symmetry=sym, padua=padua(),
                  scope='M4/m3 independent reconstruction; T8 review pending')
    if args.t8:
        result['t8']=t8_checks(args.scratch)
        result['scope']='M4/m3 and finite T8 U/O/P computations; supplementary, not Claude audit'
        for p in ['code/t8_cyclic.py','code/t8_phases.py',
                  'evidence/t8-unshifted-n2.json','evidence/t8-unshifted-n3.json',
                  'evidence/t8-odd-n5.json','evidence/t8-odd-n6.json','evidence/t8-phases.json']:
            result['inputs'][p]=sha(ROOT/p)
        if args.even:
            result['even']=even_checks(args.scratch)
            for p in ['code/t8_even_family.py','evidence/t8-even-family.json']:
                result['inputs'][p]=sha(ROOT/p)
    args.output.write_text(json.dumps(result, sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'verdict':'PASS', 'reflection_counts':[r['target_count_cosets'] for r in reflections],
                      'symmetry_classes':[r['classes'] for r in sym], 'padua_degrees':[1,12]}))


if __name__ == '__main__':
    main()
