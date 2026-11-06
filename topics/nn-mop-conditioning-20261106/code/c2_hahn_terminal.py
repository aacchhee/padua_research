#!/usr/bin/env python3
"""Exact verification of the balanced Hahn positive parity-row formula."""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import platform
import time
from c2_rate_checks import solve,evaluate
from c2_hahn_checks import weights,polynomial,poch


def positive_sum(M):
    A=0
    response=Q(0)
    for k in range(M+1):
        T=sum(comb(k,h)*comb(M+k+3-h,M-k) for h in range(k+1))
        for i in range(M//2):
            choose=comb(M-1,2*i+1)
            A += T*choose*comb(k+i,k)
            response += (T*choose*poch(Q(5,2)+i,k)
                         /poch(Q(1),k)
                         /((2*M+5+2*i)*(Q(M)+Q(7,2)+i)))
    K=Q(M*(M+1)*(2*M+4)*(2*M+5),(3*M+4)*(3*M+5))
    return A,K*response


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m',type=int,default=10)
    args=parser.parse_args()
    if not 2<=args.max_m<=16:
        parser.error('2<=max-m<=16')
    started=time.monotonic()
    cases=[]
    for M in range(2,args.max_m+1):
        n,m=(M+1)//2,M//2
        w=weights(M)
        poly,tests,matrix=polynomial(M,w,n,m)
        rhs=[-sum((w[s][k]*(-1)**k if s==1 else 0)
                  *k**i*evaluate(poly,Q(k)) for k in range(M+1))
             for s,i in tests]
        derivative=solve(matrix,rhs)[-1]
        A,response=positive_sum(M)
        if abs(derivative)!=response:
            raise AssertionError(('positive parity response',M,derivative,response))
        if not Q(A,54)<=response<=3*(M+1)**2*A:
            raise AssertionError(('polynomial comparison',M))
        if any((-1)**(M+k)*evaluate(poly,Q(k))<=0 for k in range(M+1)):
            raise AssertionError(('terminal alternating signs',M))
        cases.append({'M':M,'N':M+1,'nu':[n,m],'A_M':str(A),
                      'integer_b_parity_response_abs':str(response)})
    source=Path(__file__)
    print(json.dumps({'status':'VERIFIED finite exact parity identities; analytic rate proof separate',
                      'python':platform.python_version(),
                      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                      'helper_sha256':{name:hashlib.sha256(source.with_name(name).read_bytes()).hexdigest()
                                       for name in ('c2_rate_checks.py','c2_hahn_checks.py')},
                      'elapsed_seconds':time.monotonic()-started,'cases':cases},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
