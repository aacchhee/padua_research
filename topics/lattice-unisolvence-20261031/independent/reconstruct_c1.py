#!/usr/bin/env python3
"""Independent C1 count, matrix ranks and formal quadratic identity."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import sys
import sympy as sp
from reconstruct_rank import independent_rank

ROOT=Path(__file__).resolve().parents[3]
TOPIC=ROOT/'topics/lattice-unisolvence-20261031'


def points(n,phase=0):
    return [(i,j) for i,j in product(range(n+1),range(n+2)) if (i+j-phase)%4<2]


def main():
    source=TOPIC/'directions/C1/results.json'
    data=json.loads(source.read_text())
    extension_path=TOPIC/'directions/C1/extension.json'
    extension=json.loads(extension_path.read_text())
    correction=((1,0,-1,0),(0,1,0,-1),(0,0,0,0),(0,0,0,0))
    for n in range(129):
        for phase in range(4):
            assert len(points(n,phase))-comb(n+2,2)==correction[n%4][phase]
        phase=0 if n%2 else 1
        pp=set(points(n,phase))
        assert len(pp)==comb(n+2,2)
        assert pp.isdisjoint({(n-i,n+1-j) for i,j in pp})
    for row in data['counts']:
        assert len(points(row['n']))==row['count']
        assert row['target']==comb(row['n']+2,2)
    for row in data['ranks']:
        n,p=row['n'],row['p']
        exp=[(a,b) for a,b in product(range(n+1),repeat=2) if a+b<=n]
        matrix=[[pow(row['x'][i],a,p)*pow(row['y'][j],b,p)%p for a,b in exp] for i,j in points(n)]
        assert independent_rank(matrix,p)==row['rank']==row['target']
    shifted_tests=0
    for group in data.get('shifted',[]):
        n,phase=group['n'],group['phase']
        selected=points(n,phase)
        assert len(selected)==group['count']==group['target']==comb(n+2,2)
        mapped={(i,4*(j//4)+(j+phase)%4) for i,j in points(n)}
        assert mapped==set(selected)
        exp=[(a,b) for a,b in product(range(n+1),repeat=2) if a+b<=n]
        for row in group['generic_samples']:
            p=row['p']
            matrix=[[pow(row['x'][i],a,p)*pow(row['y'][j],b,p)%p for a,b in exp] for i,j in selected]
            assert independent_rank(matrix,p)==row['rank']==group['target']
            shifted_tests+=1
    for row in extension['ranks']:
        n,p,phase=row['n'],row['p'],row['phase']
        exp=[(a,b) for a,b in product(range(n+1),repeat=2) if a+b<=n]
        matrix=[[pow(row['x'][i],a,p)*pow(row['y'][j],b,p)%p for a,b in exp] for i,j in points(n,phase)]
        assert independent_rank(matrix,p)==row['rank']==row['target']
    x=sp.symbols('x0:3');u=sp.symbols('u0:3');v=sp.symbols('v0:3')
    matrix=sp.Matrix([[1,x[r],x[r]**2,y,x[r]*y,y**2] for r in range(3) for y in (u[r],v[r])])
    actual=sp.expand(matrix.det(method='domain-ge'))
    delta=sp.prod(x[j]-x[i] for j in range(3) for i in range(j))
    residual=sp.Matrix([[1,x[r],u[r]+v[r]] for r in range(3)]).det()
    predicted=-delta*sp.prod(v[r]-u[r] for r in range(3))*residual
    assert sp.expand(actual-predicted)==0
    crossed=[]
    for row in data['n2_crossed_examples']:
        matrix=sp.Matrix([[1,row['x'][i],row['x'][i]**2,row['y'][j],row['x'][i]*row['y'][j],row['y'][j]**2] for i,j in points(2)])
        determinant=int(matrix.det(method='domain-ge'))
        assert determinant==int(row['determinant'])==int(row['formula'])
        crossed.append(determinant)
    assert crossed==[0,16,-180,0]
    for n in range(2,99,4):
        for phase in (0,2):
            pp=set(points(n,phase))
            assert {(n-i,n+1-j) for i,j in pp}==pp
            assert all((n-i,n+1-j)!=(i,j) for i,j in pp)
            assert len(pp)==comb(n+2,2)
            assert sum(2*d+1 for d in range(n//2+1))-len(pp)//2==(n+2)//4
        assert {(n-i,n+1-j) for i,j in points(n,1)}==set(points(n,3))
    out={'all_checks_passed':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (source,extension_path)},'count_n_range':[0,128],
         'count_phases_checked':[0,1,2,3],
         'matrix_ranks_checked':len(data['ranks'])+shifted_tests+len(extension['ranks']),
         'shifted_matrix_ranks_checked':shifted_tests,'extension_matrix_ranks_checked':len(extension['ranks']),
         'quadratic_formal_identity_checked':True,
         'crossed_determinants':crossed,'antipodal_index_checks_n':'2,6,...,98',
         'method':'Fresh total-degree matrices, exact polynomial determinant, direct counts and central-inversion set equality.',
         'sympy':sp.__version__}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
