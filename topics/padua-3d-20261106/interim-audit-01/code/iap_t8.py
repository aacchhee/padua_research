#!/usr/bin/env python3
"""Interim exact T8 replay with an independently assembled monomial DCT census.

Modular certificates deliberately reuse the inspected historical checker
with fresh prime floors. They are actual fresh executions, not a claim of
an independently authored modular elimination implementation.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import time

PIN='5440555cf326afdbd66b75bed195802013901c2d'
TOPIC=Path(__file__).resolve().parents[2]

def identity(path):
    data=Path(path).read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def monomial_dictionary(n,z):
    N=math.comb(n+3,3); M=2*N
    columns=[]
    for a in range(n+1):
        for b in range(n+1-a):
            for c in range(n+1-a-b):
                alpha=(a,b,c)
                col=Counter()
                for beta in itertools.product(*(range(x+1) for x in alpha)):
                    m=sum((x-2*y)*v for x,y,v in zip(alpha,beta,z))%(2*M)
                    if m>M: m=2*M-m
                    weight=math.prod(math.comb(x,y) for x,y in zip(alpha,beta))
                    if m>N: m,weight=M-m,-weight
                    if m!=N: col[m]+=weight
                columns.append({i:Fraction(v) for i,v in col.items() if v})
    return columns

def sparse_rank(columns):
    piv={}
    for original in columns:
        col=dict(original)
        while col:
            key=min(col); value=col[key]
            if key not in piv:
                piv[key]={i:v/value for i,v in col.items()}
                break
            for i,v in piv[key].items():
                after=col.get(i,0)-value*v
                if after: col[i]=after
                else: col.pop(i,None)
    return len(piv)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scratch',required=True,type=Path)
    parser.add_argument('--receipt',required=True,type=Path)
    args=parser.parse_args()
    args.scratch.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    path=TOPIC/'code/t8_r08_check.py'
    spec=importlib.util.spec_from_file_location('frozen_t8',path)
    checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
    import sympy
    result={'audit_pin':PIN,'model':'gpt-6-astra xhigh (assigned; runtime metadata unexposed)',
            'command':sys.argv,'self':identity(__file__),'reused_modular_checker':identity(path),
            'versions':{'python':platform.python_version(),'numpy':checker.np.__version__,
                        'scipy':checker.scipy.__version__,'sympy':sympy.__version__},
            'structure':checker.structural()}
    census=[]; hist=Counter();survivors=[]
    for b,c in itertools.combinations(range(1,40),2):
        z=(1,b,c)
        r=sparse_rank(monomial_dictionary(3,z))
        original_rank=checker.integer_rank(checker.cosine_coefficients(3,z))
        assert r==original_rank
        L,fold=checker.nodes(40,z,z,80)
        assert L==80 and len(fold)==20
        hist[r]+=1;census.append([list(z),r])
        if r==20:
            det=abs(checker.integer_determinant(checker.cosine_coefficients(3,z)))
            assert det==2**49
            cert=checker.certificate(3,40,z,z,80,prime_floor=1800000000)
            assert all(x['rank']==20 and x['det'] for x in cert['checks'])
            survivors.append({'z':z,'abs_chebyshev_DCT_det':det,
                              'fresh_primes':[x['p'] for x in cert['checks']],
                              'fresh_modular_dets':[x['det'] for x in cert['checks']]})
    expected=[(1,4,11),(1,4,29),(1,6,15),(1,6,25),(1,11,36),(1,15,34),(1,25,34),(1,29,36)]
    assert [row['z'] for row in survivors]==expected
    raw=args.scratch/'cubic-monomial-census.json';assert not raw.exists()
    raw.write_text(json.dumps(census,separators=(',',':'))+'\n')
    result['cubic']={'parameters':len(census),'rank_histogram':dict(sorted(hist.items())),
                     'raw':identity(raw),'survivors':survivors}
    old_path=TOPIC/'evidence/t8-r06-witnesses.json'
    result['old_input']=identity(old_path);result['old_witnesses']=[]
    for r in json.loads(old_path.read_text())['rows']:
        cert=checker.certificate(r['n'],r['M'],r['z'],r['phase_nums'],r['phase_den'],prime_floor=1800000000)
        N=math.comb(r['n']+3,3)
        assert cert['nodes']==N and all(x['rank']==N and x['det'] for x in cert['checks'])
        result['old_witnesses'].append(cert)
        print(json.dumps({'old_n':r['n'],'N':N,'primes':[x['p'] for x in cert['checks']]}),flush=True)
    current_path=TOPIC/'evidence/t8-r08-halfshift-corrected.json'
    result['halfshift_input']=identity(current_path);result['halfshift_selected']=[]
    for r in json.loads(current_path.read_text())['rows']:
        if not r.get('selected'):continue
        z=r['selected']['z']
        cert=checker.certificate(r['n'],r['M'],z,z,2*r['M'],prime_floor=1800000000)
        N=math.comb(r['n']+3,3)
        assert cert['nodes']==N and all(x['rank']==N and x['det'] for x in cert['checks'])
        assert sparse_rank(monomial_dictionary(r['n'],z))==N
        result['halfshift_selected'].append(cert)
    # Exact phase counterexample controls: cyclotomic remainder, no floating cosines.
    t=sympy.Symbol('t');gauss=[]
    for q in range(2,9):
        L=4*q;phi=sympy.Poly(sympy.cyclotomic_poly(L,t),t)
        residues=[(1+4*j)%L for j in range(q)]
        assert len({min(r,L-r) for r in residues})==q
        for m in range(1,2*q):
            expression=sum(t**((m*r)%L)+t**((-m*r)%L) for r in residues)
            assert sympy.rem(sympy.Poly(expression,t),phi).is_zero
        for r in residues:
            assert sympy.rem(sympy.Poly(t**((q*r)%L)+t**((-q*r)%L),t),phi).is_zero
        gauss.append({'q':q,'tensor_nodes':q**3,'Pi_q_dimension':math.comb(q+3,3),
                      'zero_nonconstant_Chebyshev_1d_moments':2*q-1,'Tq_annihilates':True})
    result['phase_gauss_controls']=gauss
    # The fixed-dual tetrahedron norm and cardinal values at rational deformations.
    signs=[eps for eps in itertools.product((-1,1),repeat=3) if math.prod(eps)==1]
    tetra=[]
    for t in [Fraction(1),Fraction(1,2),Fraction(1,3),Fraction(1,10)]:
        nodes=[(t*e[0],Fraction(e[1]),Fraction(e[2])) for e in signs]
        def cardinal(e,p):return (1+e[0]*p[0]/t+e[1]*p[1]+e[2]*p[2])/4
        assert all(cardinal(e,p)==(i==j) for i,e in enumerate(signs) for j,p in enumerate(nodes))
        norm=max(sum(abs(cardinal(e,p)) for e in signs) for p in itertools.product((-1,1),repeat=3))
        assert norm==max(1/t,(1/t+3)/2)
        tetra.append({'t':str(t),'vertex_maximum':str(norm)})
    result['fixed_dual_tetrahedron_controls']=tetra
    result['elapsed_seconds']=time.monotonic()-start
    assert result['self']==identity(__file__)
    encoded=json.dumps(result,separators=(',',':'))+'\n'
    assert len(encoded.encode())<16384,len(encoded.encode())
    args.receipt.write_text(encoded)
    print(json.dumps({'receipt':identity(args.receipt),'elapsed_seconds':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
