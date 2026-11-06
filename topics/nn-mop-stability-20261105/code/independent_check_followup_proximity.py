#!/usr/bin/env python3
"""Exact direct-moment sanity for the fixed-N proximity obstruction."""
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
from independent_check_moments import direct, inputs

HERE=Path(__file__).resolve().parent
FILES=[Path(__file__),HERE/'independent_check_moments.py',
       HERE.parent/'theory/conditioning-lower-proximity.md',
       HERE.parent/'theory/conditioning-lower-krawtchouk.md']


def hashes():
    return {str(p.relative_to(HERE.parents[2])):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in FILES}


def main():
    pinned=hashes()
    out=dict(python=platform.python_version(),platform=platform.platform(),
             arithmetic='fractions.Fraction',source_sha256=pinned,cases=[])
    for N,delta in ((4,Q(1,10)),(4,Q(1,20)),(4,Q(1,40)),(6,Q(1,20))):
        M=N-1
        q=Q(2,5)+delta
        x,w=inputs(N,'krawtchouk')
        w[1]=[Q(math.comb(M,k))*q**k*(1-q)**(M-k) for k in range(N)]
        c,J=direct(x,w)
        r=(1-q)/q
        zeta=[(-r)**k/r**M for k in range(N)]
        direction=[wi*zi for wi,zi in zip(w[1],zeta)]
        assert max(map(abs,zeta))==1 and sum(direction)==0
        assert all(direction[k]==q**M*math.comb(M,k)*(-1)**k for k in range(N))
        assert all(sum(direction[k]*x[k]**j for k in range(N))==0 for j in range(M))
        h=[Q(0)]*(2*N)+direction
        scale=max(abs(a['b2']) for a in c.values())
        assert scale==Q(1,5)
        dmin=min(abs(a['b2']-a['b1']) for nu,a in c.items() if sum(nu)<=M-1)
        assert dmin==2*delta/M
        dot=sum(a*b for a,b in zip(J[M-1,1]['b2'],h))
        normalized=abs(dot)/scale
        assert normalized==10*q**M/(M*delta**(M-1))
        assert normalized*dmin==20*q**M/(M*M*delta**(M-2))
        out['cases'].append(dict(N=N,delta=str(delta),q=str(q),dmin=str(dmin),
                                 derivative=str(dot),normalized_witness=str(normalized),
                                 witness_times_dmin=str(normalized*dmin)))
    assert hashes()==pinned
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
