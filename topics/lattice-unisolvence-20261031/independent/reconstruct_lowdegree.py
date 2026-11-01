#!/usr/bin/env python3
"""Independent subbox extremal count and normalized n2 factor identity."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
TOPIC=ROOT/'topics/lattice-unisolvence-20261031'


def has_subbox_certificate(record):
    lx,ly,lz=record['lengths'];n=record['n']
    for mx in range(1,1<<lx):
        for my in range(1,1<<ly):
            per_z=[0]*lz
            for x,y,z in record['points']:
                if (mx>>x)&1 and (my>>y)&1:
                    per_z[z]+=1
            best=sorted(per_z,reverse=True)
            for sizez in range(1,lz+1):
                dim=sum(a+b+c<=n for a,b,c in product(range(mx.bit_count()),range(my.bit_count()),range(sizez)))
                # For these x/y sets and z-cardinality, top layer counts attain
                # the maximum selected-point count over every possible z set.
                if sum(best[:sizez])>dim:
                    return True
    return False


def main():
    lp=TOPIC/'directions/C3/lowdegree.json';rp=TOPIC/'directions/C3/ranks.json'
    low=json.loads(lp.read_text());reps={r['id']:r for r in json.loads(rp.read_text())['representatives']}
    for row in low['boxes']:
        assert has_subbox_certificate(reps[row['id']])==(row['certificate'] is not None)
    item=low['n2_factor']
    u,v,w,r,s,t=sp.symbols('u v w r s t')
    axes=[[0,1,u],[0,1,v,w],[0,1,r,s,t]]
    # Use the theorem's explicitly displayed column order.
    exps=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,0,2),(0,1,1),(0,2,0),(1,0,1),(1,1,0),(2,0,0)]
    matrix=sp.Matrix([[sp.prod(axes[j][index[j]]**exp[j] for j in range(3)) for exp in exps] for index in item['points']])
    actual=sp.expand(matrix.det(method='domain-ge'))
    predicted=-u**3*(u-1)*v**2*w*(w-1)*(v-w-1)*s**3*(t-1)*(s-t-1)
    assert sp.expand(actual-predicted)==0
    mapped=sp.sympify(item['determinant']).subs(dict(zip(sp.symbols('x2 y2 y3 z2 z3 z4'),[u,v,w,r,s,t])))
    assert sp.expand(mapped-actual)==0
    out={'all_checks_passed':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (lp,rp)},
         'subbox_decisions_checked':len(low['boxes']),'subbox_certificates_found':0,
         'n2_symbolic_factor_checked':True,'sympy':sp.__version__,
         'method':'Independent maximizing-z-layer reduction for every x/y subset, and direct normalized polynomial determinant identity.'}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
