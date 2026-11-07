#!/usr/bin/env python3
"""Exact rational completion of the published U3-F coherent-coset scope."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path
import platform
import sys
import tempfile
import time

import sympy as sp
from sympy.polys.matrices import DomainMatrix
import u3_constructions as base

def dictionary(n,a,b,r,s,e1,e2):
    N=len(base.modes(n)); rows={}; refs={}
    for col,alpha in enumerate(base.modes(n)):
        for eps in base.SIGNS:
            x,y,z=[u*v for u,v in zip(alpha,eps)]
            f1=x+r*z; f2=x+y+s*z; cl=(f1%a,f2%b)
            if cl not in rows: rows[cl]=[0]*N; refs[cl]=(f1,f2)
            u,v=refs[cl]
            assert (f1-u)%a==0 and (f2-v)%b==0
            exponent=e1*((f1-u)//a)+e2*((f2-v)//b)
            rows[cl][col]+=(-1 if exponent%2 else 1)
    normalized=set()
    for row in rows.values():
        if not any(row): continue
        first=next(x for x in row if x)
        # Only nonzero scalar row operations; primitive normalization is exact.
        g=sp.igcd(*row)
        if first<0: g=-g
        normalized.add(tuple(int(x//g) for x in row))
    return tuple(sorted(normalized))

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--receipt',default=str(base.TOP/'evidence/u3-f-exact.json'))
    p.add_argument('--scratch'); args=p.parse_args()
    frozen={str(Path(__file__).name):base.sha(__file__),str(Path(base.__file__).name):base.sha(base.__file__)}
    scratch=Path(args.scratch or tempfile.mkdtemp(prefix='padua-u3-F-exact-')); scratch.mkdir(parents=True,exist_ok=True)
    raw=scratch/'exact-rows.jsonl'; assert not raw.exists(); started=time.monotonic(); rows=[]; cache={}
    with raw.open('w') as out:
        for n in range(3,9):
            start=time.monotonic(); N=len(base.modes(n)); hist=Counter(); ranks=Counter(); positive=[]; exact=0; fresh=0
            for M in (2*N,2*N-4):
                for a in range(2,base.math.isqrt(M)+1):
                    if M%a: continue
                    b=M//a
                    if b%a: continue
                    for r in range(a):
                        for s in range(b):
                            h1=[Q(1,a),Q(0),Q(r,a)]; h2=[Q(1,b),Q(1,b),Q(s,b)]
                            for phase,(e1,e2) in enumerate(((0,0),(1,0),(0,1),(1,1))):
                                cs=[base.component([(e1*x+e2*y)/2 for x,y in zip(h1,h2)],[h1,h2])]
                                L,X,sizes=base.nodes(cs); key=[M,a,b,r,s,phase]
                                row={'n':n,'key':key,'count':len(X)}; why='wrong-count'
                                if len(X)==N:
                                    axes=[len({x[j] for x in X}) for j in range(3)]; row['axis_counts']=axes
                                    why='short-axis' if min(axes)<=n else None; traces=[]
                                    for k,l in ((a//2,0),(0,b//2),(a//2,b//2)):
                                        if (k and a%2) or (l and b%2): continue
                                        h=[k*x+l*y for x,y in zip(h1,h2)]
                                        if all(x.denominator==1 for x in h): continue
                                        e=[int(2*x)%2 for x in h]
                                        f=sum(all(not e[j] or 4*x[j]==L for j in range(3)) for x in X)
                                        traces.append([e,f,base.trace(n,e)])
                                    row['traces']=traces
                                    if any(f!=d for _,f,d in traces): why='trace-mismatch'
                                    if why is None:
                                        A=dictionary(n,a,b,r,s,e1,e2); exact+=1
                                        if A not in cache:
                                            cache[A]=int(DomainMatrix.from_Matrix(sp.Matrix(A)).convert_to(sp.QQ).rank()); fresh+=1
                                        rank=cache[A]; ranks[rank]+=1; row['exact_rank']=rank
                                        why='exact-full-rank' if rank==N else 'exact-deficient'
                                        if rank==N: positive.append({'key':key,'rank':rank,'components':cs})
                                hist[why]+=1; row['outcome']=why; base.write(out,row)
            result={'n':n,'histogram':dict(hist),'exact_tests':exact,'new_exact_dictionaries':fresh,
                    'exact_rank_histogram':dict(ranks),'positives':positive,'seconds':time.monotonic()-start,
                    '120second_warning_reached':time.monotonic()-start>120,'coverage':'complete prescribed finite universe'}
            rows.append(result); print(json.dumps(result),flush=True)
    assert frozen=={str(Path(__file__).name):base.sha(__file__),str(Path(base.__file__).name):base.sha(base.__file__)}
    result={'schema':'u3-folded-exact-v1','input_sha':base.INPUT,'command':sys.argv,'source_sha256':frozen,
            'versions':{'python':platform.python_version(),'sympy':sp.__version__},'degrees':rows,
            'raw':{'path':str(raw),'bytes':raw.stat().st_size,'sha256':base.sha(raw),'retention':'local regenerate-only, no archival delivery'},
            'elapsed_seconds':time.monotonic()-started}
    data=json.dumps(result,separators=(',',':'))+'\n'; assert len(data.encode())<16384
    Path(args.receipt).write_text(data)
    print(json.dumps({'receipt':args.receipt,'bytes':len(data.encode()),'source_sha256':frozen}),flush=True)

if __name__=='__main__': main()
