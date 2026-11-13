#!/usr/bin/env python3
"""Small exact boundary controls for the interim prior-results audit."""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import sys

import sympy

PIN='5440555cf326afdbd66b75bed195802013901c2d'
TOPIC=Path(__file__).resolve().parents[2]
REPO=TOPIC.parents[1]

def identity(path):
    data=Path(path).read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def member(k,h):
    a,b,c,d,e,f=h
    u,r=divmod(k[0],a)
    v,s=divmod(k[1]-b*u,d)
    return r==0 and s==0 and (k[2]-c*u-e*v)%f==0

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--receipt',required=True,type=Path)
    args=parser.parse_args()
    out={'audit_pin':PIN,'model':'gpt-6-astra xhigh (assigned; runtime metadata unexposed)',
         'command':sys.argv,'code':identity(__file__),
         'versions':{'python':platform.python_version(),'sympy':sympy.__version__},'attaining_admissibility':[]}
    for n,h in [(3,(1,3,3,6,0,10)),(4,(4,0,5,5,5,10)),(5,(5,0,6,6,6,12))]:
        R=2*n
        short=[k for k in itertools.product(range(-R,R+1),repeat=3) if 0<sum(map(abs,k))<R]
        violations=[k for k in short if member(k,h)]
        assert not violations
        boundary=next(k for k in itertools.product(range(-R,R+1),repeat=3)
                      if sum(map(abs,k))==R and member(k,h))
        out['attaining_admissibility'].append({'n':n,'hnf':h,'all_short_vectors_tested':len(short),
                                              'shortest_l1':R,'attaining_vector':boundary})
    out['order19_examples']=[]
    for z in [(1,3,7),(1,4,6),(1,5,8),(1,7,8)]:
        moment=Fraction(sum(sum(a*b for a,b in zip(z,eps))%19==0
                            for eps in itertools.product((-1,1),repeat=3)),8)
        minimum=next(r for r in range(1,10) if any(sum(a*b for a,b in zip(z,k))%19==0
                         for k in itertools.product(range(-r,r+1),repeat=3) if sum(map(abs,k))==r))
        assert minimum==(3 if z==(1,7,8) else 4)
        assert moment==(Fraction(1,4) if z==(1,7,8) else 0)
        out['order19_examples'].append({'z':z,'shortest_dual_l1':minimum,'Haar_T111':str(moment)})
    A=sympy.Matrix([[2,-1,-3],[3,-2,1],[1,3,-2]])
    Ainv=A.inv()
    assert abs(A.det())==38
    candidates=[k for k in itertools.product(range(-5,6),repeat=3) if 0<sum(map(abs,k))<6]
    assert not any(all(v.q==1 for v in Ainv*sympy.Matrix(k)) for k in candidates)
    out['packing_normalization']={'critical_determinant':'38/27','l1_minimum':2,
                                  'integer_short_vectors_tested':len(candidates),'density':'18/19',
                                  'scope':'normalization only, no independent density-optimality proof'}
    f=lambda n:n**3-108*n**2-198*n-108
    assert f(109)==-9809 and f(110)==2312
    # Exact forward difference is increasing and positive from n109.
    assert 3*109**2-213*109-305>0 and 6*109-210>0
    out['packing_threshold']={'f109':f(109),'f110':f(110),'forward_difference_at109':3*109**2-213*109-305}
    out['rleja_coefficient_controls']=[]
    for n in range(0,25):
        direct=sum((a+1)**2*(b+1)**2*(c+1)**2 for a in range(n+1)
                   for b in range(n+1-a) for c in range(n+1-a-b))
        formula=sum(math.comb(3,j)*math.comb(n-j+9,9) for j in range(min(3,n)+1))
        assert direct==formula and formula<=8*math.comb(n+9,9)
        out['rleja_coefficient_controls'].append([n,direct])
    # Freeze all reused executable/data bytes against the assigned audit commit.
    inputs=['code/r08_lattice_enum.cpp','code/r08_lattice_check.py','code/t8_r08_check.py',
            'code/r08_lattice.py','code/t8_r08_halfshift.py','code/t8_r08_tie_correction.py',
            'evidence/t8-r06-witnesses.json','evidence/t8-r08-halfshift-corrected.json']
    out['pinned_inputs']=[]
    for relative in inputs:
        path=TOPIC/relative
        historical=subprocess.check_output(['git','show',f'{PIN}:{path.relative_to(REPO)}'],cwd=REPO)
        assert historical==path.read_bytes(),relative
        out['pinned_inputs'].append(identity(path))
    encoded=json.dumps(out,separators=(',',':'))+'\n'
    assert len(encoded.encode())<16384
    args.receipt.write_text(encoded)
    print(json.dumps(identity(args.receipt)))

if __name__=='__main__':main()
