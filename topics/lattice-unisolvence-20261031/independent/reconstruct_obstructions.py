#!/usr/bin/env python3
"""Fresh projected-set checks and modular rectangle determinants."""
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "topics/lattice-unisolvence-20261031"


def determinant_mod(rows,p):
    basis, pivot_order, determinant = {}, [], 1
    for original in rows:
        row = list(original)
        for col in range(len(row)):
            if row[col] % p == 0:
                continue
            if col in basis:
                scale = row[col] % p
                row = [(a-scale*b)%p for a,b in zip(row,basis[col])]
            else:
                pivot = row[col] % p
                determinant = determinant*pivot % p
                basis[col] = [v*pow(pivot,p-2,p)%p for v in row]
                pivot_order.append(col)
                break
    if len(basis) != len(rows):
        return 0
    inversions = sum(a>b for i,a in enumerate(pivot_order) for b in pivot_order[i+1:])
    return determinant*(-1 if inversions%2 else 1)%p


def evaluate(record,axes,p):
    n=record['n']
    exps=[exp for exp in product(range(n+1),repeat=3) if sum(exp)<=n]
    return [[pow(axes[0][i],a,p)*pow(axes[1][j],b,p)*pow(axes[2][k],c,p)%p for a,b,c in exps] for i,j,k in record['points']]


def main():
    rp=TOPIC/'directions/C3/ranks.json'
    op=TOPIC/'directions/C3/obstructions.json'
    data=json.loads(op.read_text())
    reps={r['id']:r for r in json.loads(rp.read_text())['representatives']}
    projection_count=0
    for row in data['projection_certificates']:
        r=reps[row['id']]
        found=False
        for axis,L in enumerate(r['lengths']):
            for mask in range(1<<L):
                q=mask.bit_count()
                if q>r['n']:
                    continue
                points={tuple(v for j,v in enumerate(index) if j!=axis) for index in r['points'] if not (mask>>index[axis])&1}
                if len(points)<comb(r['n']-q+2,2):
                    found=True
        cert=row['certificate']
        assert found==(cert is not None),row['id']
        if cert is not None:
            axis=cert['removed_axis'];removed=cert['removed_layers']
            assert len(removed)==len(set(removed))<=r['n']
            actual={tuple(v for j,v in enumerate(index) if j!=axis) for index in r['points'] if index[axis] not in removed}
            assert sorted(actual)==[tuple(v) for v in cert['projection']]
            assert len(actual)==cert['projection_size']<comb(r['n']-len(removed)+2,2)==cert['bivariate_dimension']
            projection_count+=1
    tested,nonseparable=0,0
    for row in data['rectangle_tests']:
        r=reps[row['id']];values=[]
        for test in row['tests']:
            u,v=test['pair'];dets=[];p=test['p']
            for i,j in ((0,0),(0,1),(1,0),(1,1)):
                axes=[list(a) for a in test['axes_a']]
                axes[u]=test['axes_b'][u] if i else test['axes_a'][u]
                axes[v]=test['axes_b'][v] if j else test['axes_a'][v]
                dets.append(determinant_mod(evaluate(r,axes,p),p))
            rectangular=(dets[0]*dets[3]-dets[1]*dets[2])%p
            assert rectangular==test['rectangle'],(r['id'],test['pair'])
            # A lexicographic column permutation changes all four determinants
            # by the same sign; their squared product comparison is invariant.
            old=test['determinants_AA_AB_BA_BB']
            assert dets==old or dets==[(-x)%p for x in old]
            values.append(rectangular);tested+=1
        assert any(values)==row['nonseparable_witness']
        nonseparable+=any(values)
    out={
        'all_checks_passed':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (rp,op)},
        'projection_decisions_checked':len(data['projection_certificates']),
        'projection_certificates_found':projection_count,'rectangle_tests_checked':tested,
        'nonseparable_representatives':nonseparable,
        'method':'Independent all-subset projection counts and row-space-basis determinant computation with lexicographic monomials.'}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
