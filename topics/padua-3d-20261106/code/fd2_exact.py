"""D2 round 1: exact Padua syzygies and bounded determinantal algebra.

No execution occurs on import. See final-d2/protocol.md for scope/caps.
"""
import argparse
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import random
import resource
import subprocess
import sys
import time

import sympy as s

x, y, z = s.symbols('x y z')
XYZ = (x, y, z)


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


def mons(d, v=3):
    return [a for a in it.product(range(d + 1), repeat=v) if sum(a) <= d]


def expr(a):
    return s.prod(v ** k for v, k in zip(XYZ, a))


def padua(n):
    T = s.chebyshevt
    q = [T(n+1, x)-T(n-1, x)] + [
        T(n+1-k, x)*T(k, y)-T(k-1, x)*T(n+1-k, y)
        for k in range(1, n+2)]
    q = list(map(s.expand, q))
    mm = mons(n+2, 2)
    columns = [s.Poly(t*g, x, y) for g in q for t in (1,x,y)]
    C = s.Matrix([[p.coeff_monomial(a) for p in columns] for a in mm])
    ns = C.nullspace()
    assert len(ns) == n+1
    H = s.Matrix(n+2, n+1, lambda i,j: sum(ns[j][3*i+k]*t
                                           for k,t in enumerate((1,x,y))))
    assert all(s.expand(v)==0 for v in (s.Matrix([q])*H))
    minors = [s.expand((-1)**i * H.minor_submatrix(i, n+1).det())
              for i in []]  # maximal minors use row deletion only below
    minors = [s.expand((-1)**i * H.extract([j for j in range(n+2) if j!=i],
                                          list(range(n+1))).det())
              for i in range(n+2)]
    ratio = s.cancel(minors[0]/q[0])
    assert ratio.is_Rational and ratio != 0
    assert all(s.expand(a-ratio*b)==0 for a,b in zip(minors,q))
    return {'n':n, 'generators':list(map(str,q)), 'matrix':[
        list(map(str,H.row(i))) for i in range(n+2)], 'minor_scale':str(ratio),
        'nullity':len(ns), 'nonzero_entries':sum(v!=0 for v in H),
        'entry_count':len(H), 'syzygies_exact':True, 'minors_exact':True}


def planes(n):
    # Moment-curve normals: every triple is independent and no four meet.
    return [x+t*y+t*t*z-t**3 for t in range(n+3)]


def matrix_and_generators(n, typ, family, field):
    k=n+1 if typ=='en' else n+2
    seed=202611120201+100*n+10*(typ=='sym')+(field=='Q')
    if family=='structured':
        ll=planes(n)
        if typ=='en':
            B=s.Matrix([[t**j for j in range(k)] for t in range(n+3)])
            A=s.diag(*ll)*B
            gs=[s.expand(s.prod(ll[j] for j in keep)*B.extract(keep,range(k)).det())
                for keep in it.combinations(range(n+3),k)]
        else:
            A=s.diag(*ll[:k])+ll[k]*s.ones(k)
            gs=[s.expand(A.extract([r for r in range(k) if r!=i],
                                  [c for c in range(k) if c!=j]).det(method='domain-ge'))
                for i in range(k) for j in range(i,k)]
    else:
        rng=random.Random(seed)
        rows=n+3 if typ=='en' else k
        aa=[]
        for _ in range(4):
            m=s.Matrix(rows,k,lambda i,j:rng.randint(-2,2))
            if typ=='sym': m=s.Matrix(k,k,lambda i,j:m[min(i,j),max(i,j)])
            aa.append(m)
        A=aa[0]+x*aa[1]+y*aa[2]+z*aa[3]
        if typ=='en':
            gs=[s.expand(A.extract(keep,range(k)).det(method='domain-ge'))
                for keep in it.combinations(range(rows),k)]
        else:
            gs=[s.expand(A.extract([r for r in range(k) if r!=i],
                                  [c for c in range(k) if c!=j]).det(method='domain-ge'))
                for i in range(k) for j in range(i,k)]
    return A, gs, seed


def algebra(n, typ, family, field):
    t0=time.monotonic(); c0=time.process_time()
    A, gs, seed=matrix_and_generators(n,typ,family,field)
    coeff=[[[int(s.Poly(v,*XYZ).coeff_monomial(a)) for a in
             ((0,0,0),(1,0,0),(0,1,0),(0,0,1))] for v in A.row(i)]
           for i in range(A.rows)]
    kw={'modulus':1000003} if field=='GF' else {'domain':s.QQ}
    G=s.groebner(gs,*XYZ,order='grevlex',method='f5b',**kw)
    lm=[p.LM(order=G.order).exponents for p in G.polys]
    def standard(a): return not any(all(u>=v for u,v in zip(a,b)) for b in lm)
    basis=[]
    for deg in range(2*n+5):
        layer=[a for a in mons(deg) if sum(a)==deg and standard(a)]
        basis+=layer
        if not layer: break
    else: raise RuntimeError('standard-basis degree guard, finite quotient not established')
    N=math.comb(n+3,3)
    assert len(basis)<=5*N
    positions={a:i for i,a in enumerate(basis)}
    M=s.zeros(len(basis))
    for j,a in enumerate(basis):
        rem=G.reduce(s.expand((x+2*y+3*z)*expr(a)))[1]
        for b,c in s.Poly(rem,*XYZ,**kw).terms(): M[positions[b],j]=c
    u=s.Symbol('u'); f=s.Poly(M.charpoly(u).as_expr(),u,**kw)
    squarefree=s.gcd(f,f.diff()).degree()==0
    return {'n':n,'type':typ,'family':family,'field':field,'seed':seed,
        'matrix_sha256':digest(coeff),'matrix_coefficients':coeff if family=='structured' else None,
        'generators':len(gs),'gb_polynomials':len(G.polys),'gb_sha256':digest([str(p.as_expr()) for p in G.polys]),
        'quotient_dimension':len(basis),'expected_dimension':N,
        'all_degree_le_n_standard':all(standard(a) for a in mons(n)),
        'separating_form':'x+2y+3z','charpoly_squarefree':squarefree,
        'radicality':'certified by squarefree multiplication charpoly' if squarefree else 'inconclusive',
        'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--child',nargs=4)
    ap.add_argument('--output'); args=ap.parse_args()
    if args.child:
        resource.setrlimit(resource.RLIMIT_CPU,(25,26))
        resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
        n,typ,fam,field=args.child
        print(json.dumps(algebra(int(n),typ,fam,field),sort_keys=True)); return
    assert args.output
    begin=time.monotonic()
    receipt={'schema':'fd2-exact-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'python':sys.version,'sympy':s.__version__,'prime':1000003,'padua':[],'cases':[]}
    for n in (2,3,4): receipt['padua'].append(padua(n))
    for n,typ,fam,field in it.product((2,3,4),('en','sym'),('structured','random'),('GF','Q')):
        cmd=[sys.executable,__file__,'--child',str(n),typ,fam,field]
        row={'n':n,'type':typ,'family':fam,'field':field,'command':cmd}
        try:
            p=subprocess.run(cmd,capture_output=True,text=True,timeout=30,
                             env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
            if p.returncode==0: row.update(json.loads(p.stdout)); row['outcome']='completed'
            else: row.update(outcome='failed',returncode=p.returncode,stderr=p.stderr[-1200:])
        except subprocess.TimeoutExpired as e:
            row.update(outcome='wall_timeout',stderr=str(e.stderr)[-300:])
        receipt['cases'].append(row)
        Path(args.output).write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
        print(json.dumps({k:row.get(k) for k in ('n','type','family','field','outcome','quotient_dimension','radicality')}),flush=True)
    receipt['wall_seconds']=time.monotonic()-begin
    Path(args.output).write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')


if __name__=='__main__': main()
