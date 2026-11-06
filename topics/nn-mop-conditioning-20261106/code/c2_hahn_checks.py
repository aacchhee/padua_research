#!/usr/bin/env python3
"""Exact finite checks of C2 Hahn identities; written all-N proofs separate."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial, prod
from pathlib import Path
import platform
import time

from c2_rate_checks import solve, evaluate


def poch(a, r):
    return prod((a+j for j in range(r)), start=Q(1))


def weights(M):
    return [[poch(alpha+1,k)/factorial(k)*Q(M-k+1)
             / (poch(alpha+3,M)/factorial(M)) for k in range(M+1)]
            for alpha in (Q(1),Q(3,2))]


def polynomial(M, w, n, m):
    degree = n+m
    if degree == 0:
        return [Q(1)], [], []
    tests = [(0,i) for i in range(n)]+[(1,i) for i in range(m)]
    moments = [[sum(row[k]*k**j for k in range(M+1))
                for j in range(2*degree+1)] for row in w]
    matrix = [[moments[s][i+j] for j in range(degree)] for s,i in tests]
    rhs = [-moments[s][i+degree] for s,i in tests]
    return solve(matrix,rhs)+[Q(1)], tests, matrix


def tau_formula(M,n,m):
    t=n+m
    if t == M+1:
        return -Q(M*(M+1),2)
    R=Q(1)
    for count,alpha in ((n,Q(1)),(m,Q(3,2))):
        R *= (t+alpha+1)/(t+count+alpha+1)
    return -Q(t*(t-1),2)+(M-t+1)*(1-(t+1)*R)


def cross_expectation(M,r):
    return ((-1)**r * Q(factorial(M),factorial(M-r))*factorial(r+1)
            /poch(Q(r+3),r)*poch(Q(-1,2),r)/poch(Q(9,2),r))


def determinant(matrix):
    size=len(matrix)
    rows=[list(row) for row in matrix]
    value=Q(1)
    for col in range(size):
        pivot=next(row for row in range(col,size) if rows[row][col])
        if pivot != col:
            rows[col],rows[pivot]=rows[pivot],rows[col]
            value=-value
        factor=rows[col][col]
        value *= factor
        for row in range(col+1,size):
            ratio=rows[row][col]/factor
            for j in range(col+1,size):
                rows[row][j] -= ratio*rows[col][j]
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n',type=int,default=10)
    args=parser.parse_args()
    if not 2 <= args.max_n <= 14:
        parser.error('finite verification limit: 2 <= max-n <= 14')
    started=time.monotonic()
    cases=[]
    normality_count=expectation_count=derivative_count=kernel_count=0
    for N in range(2,args.max_n+1):
        M=N-1
        w=weights(M)
        polys={}
        taus={}
        for t in range(M+2):
            for n in range(t+1):
                m=t-n
                poly,_,_=polynomial(M,w,n,m)
                actual=poly[-2] if t else Q(0)
                expected=tau_formula(M,n,m)
                if actual != expected:
                    raise AssertionError(('tau',N,n,m,actual,expected))
                polys[n,m]=poly
                taus[n,m]=actual
                if t:
                    normality_count += 1
                if t <= M:
                    row_x=[Q(1)+i for i in range(n)]+[Q(3,2)+i for i in range(m)]
                    kernel=[[1/((x+j+1)*(x+j+2)) for j in range(t)] for x in row_x]
                    actual_det=determinant(kernel)
                    formula=(prod((factorial(j) for j in range(1,t+1)),start=1)
                             *prod((row_x[h]-row_x[i] for i in range(t) for h in range(i+1,t)),start=Q(1))
                             /prod((poch(x+1,t+1) for x in row_x),start=Q(1)))
                    if actual_det != formula:
                        raise AssertionError(('kernel constant',N,n,m))
                    kernel_count += 1
        bscales=[]
        for j in (0,1):
            values=[]
            for t in range(M+1):
                for n in range(t+1):
                    m=t-n
                    up=(n+(j==0),m+(j==1))
                    values.append(abs(2*(taus[n,m]-taus[up])/M-1))
            bscales.append(max(values))
        if not all(0<scale<=2*M+3 for scale in bscales):
            raise AssertionError('field-scale bound')
        b01=2*(taus[0,1]-taus[1,1])/M-1
        if b01 != Q(36-91*M,495*M):
            raise AssertionError(('explicit nonzero b1',N,b01))
        for r in range(M+1):
            actual=sum(w[1][k]*evaluate(polys[r,0],Q(k)) for k in range(M+1))
            expected=cross_expectation(M,r)
            if actual != expected:
                raise AssertionError(('cross expectation',N,r,actual,expected))
            expectation_count += 1
        C=Q(1,2**M*comb(M+4,4))
        dw=[C*(-1)**k*comb(M,k) for k in range(M+1)]
        if sum(dw) or any(abs(a)>b for a,b in zip(dw,w[1])):
            raise AssertionError('admissibility or mass')
        poly,tests,matrix=polynomial(M,w,M-1,1)
        rhs=[-sum((dw[k] if s==1 else 0)*k**i*evaluate(poly,Q(k))
                  for k in range(M+1)) for s,i in tests]
        actual_derivative=solve(matrix,rhs)[-1]
        expected_magnitude=C*factorial(M)/abs(cross_expectation(M,M-1))
        if abs(actual_derivative) != expected_magnitude:
            raise AssertionError(('terminal derivative',N))
        derivative_count += 1
        lower=Q(2**(M+1),M*(2*M+3)*comb(M+4,4)*(M+1)*(2*M+1))
        attained=2*abs(actual_derivative)/(M*bscales[1])
        if attained < lower:
            raise AssertionError(('explicit lower',N))
        identity=json.dumps([[str(x) for x in row] for row in w],sort_keys=True)
        cases.append({'N':N,'b1_scale':str(bscales[0]),'b2_scale':str(bscales[1]),
                      'terminal_integer_b_derivative_abs':str(abs(actual_derivative)),
                      'attained_relative_response':str(attained),'proved_lower':str(lower),
                      'weights_sha256':hashlib.sha256(identity.encode()).hexdigest()})
    source=Path(__file__)
    helper=source.with_name('c2_rate_checks.py')
    print(json.dumps({'status':'VERIFIED exact finite identities; written all-N proofs separate',
                      'python':platform.python_version(),
                      'rules_local_sha':'76ba4214b100c86a44941f5e9a662ce9ce48efb8',
                      'topic_input_sha':'b4a04981d42c7cd872957facf5e3995e4096ca67',
                      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                      'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),
                      'normality_systems':normality_count,'kernel_determinants':kernel_count,
                      'cross_expectations':expectation_count,'terminal_derivatives':derivative_count,
                      'elapsed_seconds':time.monotonic()-started,'cases':cases},
                     indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
