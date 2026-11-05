#!/usr/bin/env python3
"""Independent AD check of the proved terminal parity sensitivity formula.

This is MEASURED support; the lower-bound theorem has a written proof.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
import mpmath as mp
import conditioning as cond


def check(N):
    xq,wq = cond.base.inputs(N,'krawtchouk')
    x,w = cond.seed_inputs(xq,wq)
    c = cond.layers(N,*(cond.marginal(x,row) for row in w))
    M = N-1
    errors = []
    for n in range(M):
        m,r = M-n,M-n-1
        coefficient = (Q(1) if r==0 else
                       sum(Q(math.comb(n,j)*math.comb(r-1,j-1))*Q(24,25)**j
                           for j in range(1,min(n,r)+1)))
        exact = Q(5**M,M)*coefficient
        row = c[n,m]['b2']
        got = 5*abs(sum(row.g[2*N+j]*cond.base.convert(wq[1][j],mp.mpf)*(-1)**j for j in range(N)))
        expected = cond.base.convert(exact,mp.mpf)
        errors.append(abs(got-expected)/max(1,abs(expected),abs(got)))
    return dict(N=N,sites=M,max_scaled_discrepancy=str(max(errors)),
                b2_field_scale_discrepancy=str(abs(max(abs(row['b2'].v) for row in c.values())-mp.mpf(1)/5)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes',nargs='+',type=int,default=[3,4,6,8,12])
    ap.add_argument('--dps',type=int,default=120)
    args = ap.parse_args()
    with mp.workdps(args.dps):
        result = dict(status='MEASURED',python=platform.python_version(),mpmath=mp.__version__,dps=args.dps,
                      code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      derivative_code_sha256=hashlib.sha256(Path(cond.__file__).read_bytes()).hexdigest(),
                      cases=[check(N) for N in args.sizes])
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
