#!/usr/bin/env python3
"""Upper bound for a declared dense-matvec scalar-CGS2 rounding graph.

The graph and quotient-kernel reduction are theorem03 in
theory/drift-codex-e1-03-scalar-operation-bridge.md. This formal standard
relative-error l-infinity capacity is not actual IEEE error realizability.
"""
import argparse
import hashlib
import json
import platform
import time
from pathlib import Path
import flint
from e1_exact import Q, Mat, build, multiply, points, scalar


def run(name,n,rule):
    start=time.monotonic();xy=points(name)
    coords,b,d,rec,_=build(xy,n,rule);M,N=len(xy),len(b)
    absolute=[[Q(0)]*M for _ in range(N)]
    for source in range(1,N):
        axis,parent,alpha,_=rec[source]
        u=multiply(b[parent],coords[axis])
        rho=[]
        for i in range(M):
            products=Q(0);sums=Q(0);partial=Q(0)
            for l,c in enumerate(alpha):
                term=c*b[l][0,i]
                products+=abs(term);partial+=term
                if l>=1:
                    sums+=abs(partial)
            rho.append(abs(u[0,i])+products+sums+3*abs(b[source][0,i]))
        g=[None]*N;g[source]=Mat([[1]*M])
        for i in range(M):
            absolute[source][i]+=rho[i]
        for k in range(source+1,N):
            a,p,coefficients,_=rec[k]
            v=multiply(g[p],coords[a]) if p>=source else Mat(1,M)
            for l in range(source,k):
                if coefficients[l]:
                    v=v-coefficients[l]*g[l]
            g[k]=v
            for i in range(M):
                absolute[k][i]+=abs(v[0,i])*rho[i]
        print(json.dumps({'event':'graph_source','source':source,'elapsed':time.monotonic()-start}),flush=True)
    upper=sum((sum((value*value for value in absolute[k]),Q(0))/d[k] for k in range(1,N)),Q(0))
    theory=Path(__file__).resolve().parents[2]/'theory/drift-codex-e1-03-scalar-operation-bridge.md'
    return {'status':'MEASURED exact upper for declared formal scalar-CGS2 graph','set':name,'degree':n,'rule':rule,'source_count':N-1,'upper_squared':scalar(upper),'input_norm':'all formal relative scalar errors have l-infinity norm<=1','output_norm':'spectral norm of final orthonormal-basis normal derivative','rho':'|A bp|+sum_l |alpha_l b_l|+sum_{l>=1}|sum_{h<=l}alpha_h b_h|+3|bk|','graph':'coordinate multiplication; first dense matvec products and left-to-right sum; first subtraction; second dense matvec (zero baseline products/sums); second subtraction; normalization division. Scalar dot/norm errors have zero final-normal contribution by theorem03.','limitations':'Permissive standard model; second subtract-zero rounding included for safe upper. No actual IEEE worst-case attainment claim. Result depends on analytic quotient-kernel reduction and this declared operation order.','elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'aggregate_code_sha256':hashlib.sha256(Path(__file__).with_name('e1_exact.py').read_bytes()).hexdigest(),'theory_sha256':hashlib.sha256(theory.read_bytes()).hexdigest() if theory.exists() else 'path unavailable','python':platform.python_version(),'python_flint':flint.__version__}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--set',choices=['triangle','rotated'],required=True);p.add_argument('--degree',type=int,required=True);p.add_argument('--rule',choices=['bj','mirror','alt','pivot'],required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=run(a.set,a.degree,a.rule);result['command']=' '.join(__import__('sys').argv)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'event':'complete','elapsed':result['elapsed_seconds']}))
