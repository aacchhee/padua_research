#!/usr/bin/env python3
"""Exact forward differentiation verifies frozen normal derivative.

Differentiate every projection coefficient and norm, unlike e1_exact's
frozen-coefficient polynomial propagator. A separately formed final projector
then compares both normal derivatives as rational vectors.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
from e1_exact import Q, Mat, build, dot, multiply, points


def normal(v, b, d):
    for u, du in zip(b,d):
        v=v-dot(v,u)/du*u
    return v


def verify(name,rule,degree=3):
    xy=points(name)
    with contextlib.redirect_stdout(io.StringIO()):
        coords,b,d,rec,metadata=build(xy,degree,rule)
    M,N=len(xy),len(b)
    checks=0
    for source in range(1,N):
        node=(source*37)%M
        f=Mat([[int(i==node) for i in range(M)]])
        db=[Mat(1,M)]
        dd=[Q(0)]
        frozen=[Mat(1,M)]
        for k in range(1,N):
            axis,parent,alpha,_=rec[k]
            u=multiply(b[parent],coords[axis])
            du=multiply(db[parent],coords[axis])
            h=multiply(frozen[parent],coords[axis])
            if k==source:
                du=du+f
                h=h+f
            derivative=du
            for l in range(k):
                da=(dot(db[l],u)+dot(b[l],du)-alpha[l]*dd[l])/d[l]
                derivative=derivative-da*b[l]-alpha[l]*db[l]
                if alpha[l]:
                    h=h-alpha[l]*frozen[l]
            db.append(derivative)
            dd.append(2*dot(b[k],derivative))
            frozen.append(h)
            if k>=source:
                if normal(derivative-h,b,d) != Mat(1,M):
                    raise AssertionError((name,rule,source,k))
                checks+=1
    # Check actual basis, not just its construction.
    for i in range(N):
        for j in range(N):
            assert dot(b[i],b[j])==(d[i] if i==j else 0)
    return {"set":name,"rule":rule,"degree":degree,"sources":N-1,"normal_vector_equalities":checks,"basis_pairwise_equalities":N*N,"arithmetic":"exact rational","result":"PASS"}


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    rows=[verify(s,r) for s in ['triangle','rotated'] for r in ['bj','mirror','alt','pivot']]
    result={"status":"MEASURED verification; developer execution, not independent rerun","checks":rows,"code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
