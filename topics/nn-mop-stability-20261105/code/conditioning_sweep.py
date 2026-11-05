#!/usr/bin/env python3
"""Preregistered G3 proportionality screen; no asymptotic rate inference."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys
import conditioning as cond


def inputs(N,family,gap):
    x,w = cond.base.inputs(N,family)
    M = N-1
    if family == 'krawtchouk':
        p = Q(2,5)+gap
        w[1] = [Q(math.comb(M,k))*p**k*(1-p)**(M-k) for k in range(N)]
    else:
        beta = 1+gap
        def poch(a,n):
            return math.prod((a+j for j in range(n)),start=Q(1))
        w[1] = [poch(beta+1,k)/math.factorial(k)*poch(Q(2),M-k)/math.factorial(M-k) for k in range(N)]
    return x,w


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--N',type=int,default=8)
    ap.add_argument('--family',choices=['krawtchouk','hahn'],required=True)
    ap.add_argument('--gaps',nargs='+',default=['1/10','1/20','1/50','1/100','1/200'])
    ap.add_argument('--dps',type=int,default=180)
    args = ap.parse_args()
    result = dict(status='MEASURED',prediction='kappa proportional to 1/min interior abs d',
                  N=args.N,family=args.family,dps=args.dps,
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  derivative_code_sha256=hashlib.sha256(Path(cond.__file__).read_bytes()).hexdigest(),cases=[])
    for gs in args.gaps:
        gap = Q(gs)
        if gap<=0 or (args.family=='krawtchouk' and gap>=Q(3,5)):
            ap.error('positive gap, and p2<1, required')
        x,w = inputs(args.N,args.family,gap)
        row = cond.conditioning_case(args.N,args.family,args.dps,x,w)
        row['parameter_gap'] = str(gap)
        result['cases'].append(row)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
