#!/usr/bin/env python3
"""Finite exact checks of retained Hahn upper-search representations."""
import argparse
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json
import platform
import time
from c2_rate_checks import evaluate, solve
from c2_hahn_checks import weights, polynomial, poch


def rising_derivative(a, count):
    return sum((prod((a+j for j in range(count) if j != omitted),
                     start=Q(1)) for omitted in range(count)), start=Q(0))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m', type=int, default=6)
    args=parser.parse_args()
    if not 2 <= args.max_m <= 8:
        parser.error('2<=max-m<=8')
    started=time.monotonic()
    counts={'indices':0, 'polynomial_values':0,
            'weight_coordinates':0, 'common_node_coordinates':0}
    for M in range(2,args.max_m+1):
        w=weights(M)
        alphas=(Q(1),Q(3,2))
        W=[[a*poch(alphas[s]+3,M)/factorial(M) for a in row]
           for s,row in enumerate(w)]
        for t in range(1,M+1):
            for n in range(t+1):
                m=t-n
                poly,tests,matrix=polynomial(M,w,n,m)
                pprime=[j*poly[j] for j in range(1,len(poly))]
                rows=[(s,i,alphas[s]+i) for s,c in enumerate((n,m))
                      for i in range(c)]
                y=Q(-t-1)
                ell=[prod(((y-x2)/(x-x2) for j2,(_,_,x2) in enumerate(rows)
                            if j2 != j), start=Q(1))
                     for j,(_,_,x) in enumerate(rows)]
                C=Q(factorial(t+1),factorial(M-t)) / prod(
                    (t+2+x for _,_,x in rows),start=Q(1))
                def U(l):
                    return prod((l+1+x for _,_,x in rows),start=Q(1))*poch(Q(t+2-l),M-t)
                def dual(s,k, derivative=False):
                    return sum((ell[j]*(rising_derivative(k+alphas[s]+1,i)
                                        if derivative else poch(k+alphas[s]+1,i))
                                / (poch(alphas[s]+1,i)*poch(x+t+2,M-t+1))
                                for j,(channel,i,x) in enumerate(rows) if channel==s),start=Q(0))
                factor=Q((-1)**t*factorial(M-t+1),factorial(t))
                for k in range(M+1):
                    p=evaluate(poly,Q(k))
                    delta=sum(((-1)**(k-l)*comb(k,l)*U(l) for l in range(k+1)),start=Q(0))
                    if p != C*(-1)**(t+k)*delta/(M-k+1):
                        raise AssertionError(('general value',M,n,m,k))
                    counts['polynomial_values']+=1
                    for s in range(2):
                        rhs=[-w[s][k]*k**i*p if channel==s else Q(0)
                             for channel,i in tests]
                        actual=solve(matrix,rhs)[-1]
                        if actual != factor*W[s][k]*p*dual(s,Q(k)):
                            raise AssertionError(('general dual',M,n,m,s,k))
                        counts['weight_coordinates']+=1
                    pp=evaluate(pprime,Q(k))
                    rhs=[-w[s][k]*(k**i*pp+(i*k**(i-1)*p if i else 0))
                         for s,i in tests]
                    actual=solve(matrix,rhs)[-1]
                    proposed=factor*sum((W[s][k]*(pp*dual(s,Q(k))+p*dual(s,Q(k),True))
                                         for s in range(2)),start=Q(0))
                    if actual != proposed:
                        raise AssertionError(('common node dual',M,n,m,k))
                    counts['common_node_coordinates']+=1
                counts['indices']+=1
    if not Q(559,250)**2<5 or not Q(333,100)**2 < (11+5*Q(559,250))/2:
        raise AssertionError('sqrt rational separation')
    if not Q(1863,1000)**4<Q(3125,256) or not Q(26,15)**2>3:
        raise AssertionError('fourth root rational separation')
    source=Path(__file__)
    print(json.dumps({'status':'VERIFIED finite exact search identities; no full upper proved',
                      'M_range':[2,args.max_m], 'counts':counts,
                      'counterexample':{'M':3,'nu':[1,0],'U0':24,'U1':18,'Delta_U0':-6},
                      'rational_base_separation':'beta>12.40758>12.4>12.2>rho_H',
                      'python':platform.python_version(),
                      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                      'helper_sha256':{name:hashlib.sha256(source.with_name(name).read_bytes()).hexdigest()
                                       for name in ('c2_rate_checks.py','c2_hahn_checks.py')},
                      'elapsed_seconds':time.monotonic()-started},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
