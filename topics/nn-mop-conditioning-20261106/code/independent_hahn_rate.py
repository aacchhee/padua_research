#!/usr/bin/env python3
"""Focused independent C2-04 checks; no developer implementation imports."""
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json
import platform
import mpmath as mp

TOPIC = Path(__file__).resolve().parents[1]


def solve(matrix, rhs):
    rows = [list(a)+[b] for a,b in zip(matrix,rhs)]
    for j in range(len(rows)):
        pivot = next(i for i in range(j,len(rows)) if rows[i][j])
        rows[j],rows[pivot] = rows[pivot],rows[j]
        divisor = rows[j][j]
        rows[j] = [a/divisor for a in rows[j]]
        for i in range(len(rows)):
            if i != j:
                ratio = rows[i][j]
                rows[i] = [a-ratio*b for a,b in zip(rows[i],rows[j])]
    return [row[-1] for row in rows]


def poch(a,n):
    return prod((a+j for j in range(n)),start=Q(1))


def evaluate(c,x):
    return sum(a*x**j for j,a in enumerate(c))


def multiply(a,b,degree):
    return [sum(a[i]*b[j-i] for i in range(j+1)) for j in range(degree+1)]


def positive_arrays(M):
    T=[sum(comb(k,h)*comb(M+k+3-h,M-k) for h in range(k+1)) for k in range(M+1)]
    A=sum(T[k]*comb(M-1,2*i+1)*comb(k+i,k) for k in range(M+1) for i in range(M//2))
    response=sum(T[k]*comb(M-1,2*i+1)*poch(Q(5,2)+i,k)/factorial(k)
                 /((2*M+5+2*i)*(M+Q(7,2)+i)) for k in range(M+1) for i in range(M//2))
    K=Q(M*(M+1)*(2*M+4)*(2*M+5),(3*M+4)*(3*M+5))
    return T,A,K*response


def main():
    exact=[]
    dual_coordinates=0
    for M in range(2,12):
        n,m=(M+1)//2,M//2
        weights=[[poch(alpha+1,k)/factorial(k)*(M-k+1) for k in range(M+1)] for alpha in (Q(1),Q(3,2))]
        indices=[(s,j) for s,size in enumerate((n,m)) for j in range(size)]
        moments=[[sum(w[k]*Q(k)**j for k in range(M+1)) for j in range(2*M+1)] for w in weights]
        matrix=[[moments[s][j+r] for r in range(M)] for s,j in indices]
        polynomial=solve(matrix,[-moments[s][j+M] for s,j in indices])+[Q(1)]
        values=[evaluate(polynomial,Q(k)) for k in range(M+1)]
        # Compute every relative second-weight coordinate, not just parity.
        gradient=[]
        for k in range(M+1):
            rhs=[-weights[1][k]*Q(k)**j*values[k] if s==1 else Q(0) for s,j in indices]
            gradient.append(solve(matrix,rhs)[-1])
        derivative=sum((-1)**k*g for k,g in enumerate(gradient))
        x=[Q(1)+Q(j,2) for j in range(M)]
        y=-M-1
        lagrange=[prod(((y-x[l])/(x[j]-x[l]) for l in range(M) if l!=j),start=Q(1)) for j in range(M)]
        C=Q(factorial(M+1))/prod((M+2+u for u in x),start=Q(1))
        T,A,response=positive_arrays(M)
        for k in range(M+1):
            expected_value=C*(-1)**(M+k)*Q(factorial(M),2**M)*T[k]/(M-k+1)
            assert values[k]==expected_value
            dual=sum(lagrange[2*i+1]*poch(Q(k)+Q(5,2),i)/poch(Q(5,2),i)/(M+Q(7,2)+i) for i in range(m))
            expected_gradient=Q((-1)**M,factorial(M))*weights[1][k]*values[k]*dual
            assert gradient[k]==expected_gradient
            dual_coordinates+=1
        assert abs(derivative)==response
        assert abs(derivative)==sum(abs(g) for g in gradient)
        assert sum(gradient)==0
        assert Q(A,54)<=response<=3*(M+1)**2*A
        mean=sum(w*(-1)**k for k,w in enumerate(weights[1]))/sum(weights[1])
        direction=[Q((-1)**k-mean,1)/(1+abs(mean)) for k in range(M+1)]
        assert sum(a*w for a,w in zip(direction,weights[1]))==0 and max(map(abs,direction))<=1
        constrained=sum(a*g for a,g in zip(direction,gradient))
        assert abs(constrained)==response/(1+abs(mean))>=response/2
        exact.append(dict(M=M,A=str(A),D=str(response)))

    # Formal-series construction independent of the terminal moment solves.
    degree=20
    X=[Q(0)]+[Q(j+1) for j in range(1,degree+1)]
    power=[Q(1)]+[Q(0)]*degree
    Y=[Q(0)]*(degree+1)
    for j in range(degree+1):
        factor=Q(comb(2*j,j),4**j)
        Y=[a+factor*b for a,b in zip(Y,power)]
        power=multiply(power,X,degree)
    H=Y[:];H[0]+=1
    f=multiply([Q(comb(j+3,3),2) for j in range(degree+1)],Y,degree)
    Hpower=[Q(1)]+[Q(0)]*degree
    coefficient_checks=0
    for M in range(1,degree+1):
        if M>=2:
            T,A,response=positive_arrays(M)
            b=multiply(f,Hpower,degree)[M]
            assert b-Q((-1)**(M-1)*(3*M+2),2)==A
            coefficient_checks+=1
        Hpower=multiply(Hpower,H,degree)

    mp.mp.dps=110
    rho=(7+3*mp.sqrt(3)+mp.sqrt((7+3*mp.sqrt(3))**2-4))/2
    r=3/(rho+1);delta=1-4*r+2*r*r
    Hvalue=1+(1-r)/mp.sqrt(delta)
    assert 0<r<1-1/mp.sqrt(2)
    assert abs(r*delta**(-mp.mpf('1.5'))/Hvalue-1)<mp.mpf('1e-100')
    assert abs(rho**4-14*rho**3+24*rho**2-14*rho+1)<mp.mpf('1e-100')
    assert abs(Hvalue/r-rho)<mp.mpf('1e-100')
    sources=[Path(__file__),TOPIC/'theory/c2-hahn-terminal-rate.md',TOPIC/'theory/c2-hahn-normality.md']
    result=dict(status='PASS finite exact identities; analytic proof review separate',
                source_commit='b4a04981d42c7cd872957facf5e3995e4096ca67',
                role='supplementary independent checker; not final readiness auditor',
                python=platform.python_version(),mpmath=mp.__version__,
                defining_moment_cases=len(exact),relative_weight_coordinates=dual_coordinates,
                fixed_mass_cases=len(exact),coefficient_identities=coefficient_checks,
                coefficient_M_range=[2,degree],rho=mp.nstr(rho,60),saddle=mp.nstr(r,60),
                exact_cases=exact,
                sha256={str(p.relative_to(TOPIC)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources})
    print(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
