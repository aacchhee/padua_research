#!/usr/bin/env python3
"""Supplementary independent finite checks; analytic claims remain hand proofs.

No producer imports. Direct subgroup closure precedes classification checks.
Use --source-root at the pinned worktree and separately rerun producer scripts
into --t1-replay/--t6-replay before summarizing them here.
"""
import argparse
import cmath
from fractions import Fraction as F
from hashlib import sha256
from itertools import product, permutations
import json
from math import comb, lcm, pi, prod
from pathlib import Path
import platform

PIN = 'ab2f33674cea44fa1cc10c69ed2031b43e488ffc'
TOPIC = Path('topics/padua-3d-20261106')

def subgroups(moduli):
    points = list(product(*(range(m) for m in moduli)))
    def add(x,y):
        return tuple((a+b)%m for a,b,m in zip(x,y,moduli))
    cycles = {}
    for g in points:
        c = {tuple(0 for _ in moduli)}
        h = g
        while h not in c:
            c.add(h)
            h = add(h,g)
        cycles[g] = c
    zero = frozenset({tuple(0 for _ in moduli)})
    found, todo = {zero}, [zero]
    while todo:
        h = todo.pop()
        for g in points:
            if g in h:
                continue
            ext = frozenset(add(x,y) for x in h for y in cycles[g])
            if ext not in found:
                found.add(ext)
                todo.append(ext)
    return points, found

def direct_groups():
    rows=[]
    for ms in [(1,3,4),(2,2,2),(2,3,4),(3,3,3),(4,4,4)]:
        points, groups = subgroups(ms)
        stable=0
        shift_tests=0
        stable_shifts=0
        for h in groups:
            if any(len({x[j] for x in h}) != ms[j] for j in range(3)):
                continue
            if not all(tuple(-v%ms[j] if j==i else v for j,v in enumerate(x)) in h
                       for x in h for i in range(3)):
                continue
            stable += 1
            period=lcm(*ms)
            annihilator={v for v in points if all(sum(vj*xj*(period//mj)
                for vj,xj,mj in zip(v,x,ms))%period==0 for x in h)}
            assert all(all((2*vj)%mj==0 for vj,mj in zip(v,ms))
                       for v in annihilator)
            code={tuple(int(vj!=0) for vj in v) for v in annihilator}
            assert all(sum(b)!=1 for b in code)
            assert all(tuple(x^y for x,y in zip(b,c)) in code for b in code for c in code)
            predicted={x for x in points if all(sum(bj*xj for bj,xj in zip(b,x))%2==0 for b in code)}
            assert predicted==set(h)
            active=[any(b[j] for b in code) for j in range(3)]
            # a_j=r_j/(2*m_j); enumerate all r representatives, including shifts
            # forbidden by active parity. Formula and direct set reflection agree.
            for r in product(*(range(2*m) for m in ms)):
                coset={tuple((rj+2*xj)%(2*mj) for rj,xj,mj in zip(r,x,ms)) for x in h}
                actual=all(tuple(-v%(2*ms[j]) if j==i else v for j,v in enumerate(x)) in coset
                           for x in coset for i in range(3))
                expected=all(not active[j] or r[j]%2==0 for j in range(3))
                assert actual==expected
                shift_tests+=1
                stable_shifts+=actual
        rows.append(dict(moduli=ms,all_subgroups=len(groups),full_projection_reflection_subgroups=stable,
                         shift_representatives_checked=shift_tests,stable_shift_representatives=stable_shifts))
    return rows

def count_and_boundary():
    minima=[]
    for n in range(2,31):
        best=None
        for qs in product(range(n,n+3),repeat=3):
            if sum(q<=n for q in qs)>=2:
                continue
            for p in product((0,1),repeat=3):
                count=sum(prod(sum(i%2==((pj+s)%2) for i in range(q+1))
                               for q,pj in zip(qs,p)) for s in (0,1))
                best=count if best is None else min(best,count)
        formula=F((n+1)*(n+2)**2,4) if n%2==0 else F((n+1)**2*(n+3),4)
        assert best==formula and best>comb(n+3,3)
        minima.append([n,best,comb(n+3,3)])
    points=[(1,1,0),(1,-1,0),(-1,0,1),(-1,0,-1)]
    a=[(1,)+p for p in points]
    determinant=0
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        determinant+=(-1)**inversions*prod(a[i][p[i]] for i in range(4))
    assert abs(determinant)==8
    return dict(two_relation_minima_n2_to_30=minima,n1_exact_affine_determinant=determinant)

def fourier():
    rows=[]
    for d in range(3,7):
        for n in range(d-1,13):
            m=n//(d-1)
            total=F(0)
            count=0
            for a in product(range(1,m+1),repeat=d):
                if a[0]!=min(a):
                    continue
                k=(n-sum(a[1:])+(d-3)*a[0],)+tuple(x-a[0] for x in a[1:])
                assert min(k)>=0 and sum(k)==n-2*a[0]
                r=(n-sum(k),)+tuple(n-sum(k)+2*x for x in k[1:])
                assert r==tuple(2*x for x in a)
                total+=F(1,prod(a))
                count+=1
            h=sum((F(1,j) for j in range(1,m+1)),F(0))
            assert d*total>=h**d
            rows.append([d,n,count])
    # Independent midpoint integration checks the Fourier sign convention only.
    mesh=8192
    errors=[]
    for q in (-3,-2,-1,1,2,3):
        approx=sum((pi-2*pi*(j+.5)/mesh)*cmath.exp(-1j*q*2*pi*(j+.5)/mesh)
                   for j in range(mesh))/mesh
        error=abs(approx-(-1j/q))
        assert error<1e-6
        errors.append(error)
    return dict(exact_general_dimension_subset_rows=rows,sawtooth_midpoint_mesh=mesh,
                sawtooth_coefficients=[-3,-2,-1,1,2,3],sawtooth_max_error=max(errors),
                integration_status='MEASURED sign sanity, no quadrature enclosure')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--t1-replay',type=Path,required=True)
    p.add_argument('--t6-replay',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    t1=json.loads(args.t1_replay.read_text())
    t6=json.loads(args.t6_replay.read_text())
    assert t1['verdict']=='PASS'
    files=['code/t1_reflection_enum.py','code/t6_sanity.py']
    receipt=dict(schema='padua3d-supplementary-math-v1',source_commit=PIN,
        assigned_model='gpt-6-astra high; actual runtime metadata not exposed',
        status='finite diagnostics plus separately recorded analytic reconstruction; not Claude audit',
        source_worktree=str(args.source_root),python_version=platform.python_version(),
        numpy_version=t6['numpy_version'],random_seed=None,
        checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        producer_code_sha256={f:sha256((args.source_root/TOPIC/f).read_bytes()).hexdigest() for f in files},
        commands=[f'python {TOPIC}/code/t1_reflection_enum.py --cap3 12 --cap2 10 --nmax 6 --padua-max 10 --output {args.t1_replay}',
                  f'python {TOPIC}/code/t6_sanity.py --output {args.t6_replay}',
                  f'python /workspace/padua_research/{TOPIC}/code/independent_math.py --source-root {args.source_root} --t1-replay {args.t1_replay} --t6-replay {args.t6_replay} --output {args.output}'],
        replay_output_sha256={str(f):sha256(f.read_bytes()).hexdigest() for f in [args.t1_replay,args.t6_replay]},
        producer_replays=dict(t1_dimensions=[{k:r[k] for k in ['dimension','projection_order_cap','cosets','ordered_cases_sha256','degree_rows']} for r in t1['dimensions']],
            padua_degrees=[r['degree'] for r in t1['padua']],t6_support_n=[r['n'] for r in t6['exact_checks']['support_checks']],
            t6_general=t6['exact_checks']['general_dimension_subset'],t6_measured_fft=t6['measured_fft']),
        own_direct_group_checks=direct_groups(),own_minima_boundary=count_and_boundary(),own_fourier=fourier(),
        limits='Finite subgroup/shift samples and floating sign check are diagnostics. All-order theorem acceptance rests on written analytic reconstruction. No novelty claim; no Claude audit approval.')
    args.output.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',bytes=args.output.stat().st_size,groups=receipt['own_direct_group_checks'])))

if __name__=='__main__':
    main()
