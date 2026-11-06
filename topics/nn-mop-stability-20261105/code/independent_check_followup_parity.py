#!/usr/bin/env python3
"""Exact defining-moment parity derivative check, independent of C4/AD."""
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
from independent_check_moments import direct, inputs

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FILES = [Path(__file__), HERE/'independent_check_moments.py',
         HERE.parent/'theory/conditioning-lower-krawtchouk.md']


def hashes():
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in FILES}


def coefficient(n,r):
    # Positive binomial expansion, not the developer's interpolation graph.
    if r == 0:
        return Q(1)
    return sum((Q(math.comb(n,j)*math.comb(r-1,j-1))*Q(24,25)**j
                for j in range(1,min(n,r)+1)),Q(0))


def main():
    pinned = hashes()
    result = dict(python=platform.python_version(),platform=platform.platform(),
                  arithmetic='fractions.Fraction',source_sha256=pinned,cases=[],summation=[])
    previous,current=2,10
    for L in range(31):
        B=2 if L==0 else current
        total=sum((coefficient(n,L-n) for n in range(L+1)),Q(0))
        assert 2*5**L*total == B
        result['summation'].append(dict(L=L,total=str(total),algebraic_power_sum=B))
        if L>=1:
            previous,current=current,10*current-previous
    for N in (2,3,4,6,8):
        M = N-1
        x,w = inputs(N,'krawtchouk')
        c,J = direct(x,w)
        h = [Q(0)]*(2*N)+[a*(-1)**k for k,a in enumerate(w[1])]
        assert sum(h[2*N:]) == 0
        scale = max(abs(v['b2']) for v in c.values())
        assert scale == Q(1,5)
        assert all(v['b2']==Q(n,5*M) for (n,m),v in c.items())
        terminal = []
        for m in range(1,M+1):
            n = M-m
            dot = sum(a*b for a,b in zip(J[n,m]['b2'],h))
            assert dot == sum(a*b for a,b in zip(J[n,m]['b1'],h))
            predicted = Q(5**M,M)*coefficient(n,m-1)
            assert abs(dot)/scale == predicted
            terminal.append(dict(n=n,m=m,derivative=str(dot),normalized=str(predicted)))
        # The weaker axis predecessor provides the same lower bound directly.
        axis = abs(sum(a*b for a,b in zip(J[M-1,0]['b2'],h)))/scale
        assert axis == Q(5**M,M)
        r = (M-1)//2
        strong = Q(5**M,M)*coefficient(M-1-r,r)
        total=sum((coefficient(n,M-1-n) for n in range(M)),Q(0))
        average_bound=Q(5**M,M*M)*total
        assert max(Q(row['normalized']) for row in terminal)>=average_bound
        if M >= 2:
            # Square the claimed bound to compare in rational arithmetic.
            assert strong**2 >= Q(96**M,16*M*M*(M-1)*(M-1))
        result['cases'].append(dict(N=N,zero_mass=True,b2_scale=str(scale),
                                    weaker_axis=str(axis),terminal=terminal,
                                    balanced_witness=str(strong),summed_lower_bound=str(average_bound)))
    assert hashes() == pinned
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
