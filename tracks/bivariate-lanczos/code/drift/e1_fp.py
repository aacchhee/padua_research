#!/usr/bin/env python3
"""Compare single-pass binary64 sensitivity calculation with exact evidence.

This numerical comparison is not a bound or independent exact rerun. Pivot
choices are frozen to the exact run; differentiation of pivot decisions is
outside the experiment.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import numpy as np


def compute(exact):
    if exact['set']=='triangle':
        xy=np.array([(float(Fraction(i,12)-1),float(Fraction(j,12)-1)) for i in range(25) for j in range(25-i)])
    else:
        rational=[(Fraction(i,12)-1,Fraction(j,12)-1) for i in range(25) for j in range(25)]
        xy=np.array([(float((3*x-4*y)/5),float((4*x+3*y)/5)) for x,y in rational])
    M=len(xy);n=exact['degree'];N=(n+1)*(n+2)//2
    B=np.zeros((N,M));B[0]=1;d=np.zeros(N);d[0]=M
    rec=[None];index={(0,0):0};k=1
    for t in range(1,n+1):
        for j in range(t+1):
            axis='XY'.index(exact['pivot_choices'][k-1])
            parent=index[t-1,j-axis]
            u=xy[:,axis]*B[parent]
            alpha=(B[:k]@u)/d[:k]
            B[k]=u-alpha@B[:k]
            d[k]=B[k]@B[k]
            rec.append((axis,parent,alpha,u@u))
            index[t,j]=k;k+=1
    Rdiag=1-np.sum(B*B/d[:,None],axis=0)
    lower=0.;hs=0.;rows=np.zeros(M)
    for source in range(1,N):
        g=np.zeros((N,M));g[source]=1
        for k in range(source+1,N):
            axis,parent,alpha,_=rec[k]
            g[k]=xy[:,axis]*g[parent]-alpha@g[:k]
        energy=np.sum(g[source:]**2/d[source:,None],axis=0)
        raw=rec[source][3]*energy;terms=Rdiag*raw
        lower=max(lower,float(np.max(terms)));hs+=np.sum(terms);rows+=raw
    upper=min(hs,np.max(rows))
    normalized=B/np.sqrt(d[:,None])
    return {'set':exact['set'],'degree':n,'rule':exact['rule'],'Knode_squared_binary64':lower,'upper_squared_binary64':upper,'Knode_squared_exact_float':exact['Knode_squared']['float'],'upper_squared_exact_float':exact['upper_squared']['float'],'lower_relative_error':abs(lower/exact['Knode_squared']['float']-1),'upper_relative_error':abs(upper/exact['upper_squared']['float']-1),'basis_orthogonality_frobenius':float(np.linalg.norm(normalized@normalized.T-np.eye(N))),'normal_diagonal_min':float(np.min(Rdiag))}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--exact-dir',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    rows=[]
    for source in sorted(Path(a.exact_dir).glob('*-all.json')):
        e=json.loads(source.read_text())
        if e['degree'] in [2,8,12]:
            rows.append(compute(e))
    Path(a.output).write_text(json.dumps({'status':'MEASURED binary64 comparison; exact choices frozen','numpy_version':np.__version__,'runs':rows},indent=2)+'\n')
    print(json.dumps({'runs':len(rows),'max_relative_error':max(max(r['lower_relative_error'],r['upper_relative_error']) for r in rows)}))
