#!/usr/bin/env python3
"""Exact scalar C4 certificate; justification: conditioning-normality-certificate.md.

Computes only coefficient layers through N-2, then checks every d there.
No floating arithmetic is used in the certificate computation. The receipt
is finite exact evidence; independent replay is a separate obligation.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
import conditioning as cond


def case(N,family):
    if not isinstance(N,int) or N<2:
        raise ValueError('N must be an integer at least 2')
    start = time.monotonic()
    x,w = cond.base.inputs(N,family)
    if len(x)!=N or len(set(x))!=N or len(w)!=2 or any(len(row)!=N for row in w) or not all(v>0 for row in w for v in row):
        raise ValueError('certificate requires distinct nodes and two positive weight vectors')
    # Replace the generic graph's scalar constructor in this process only.
    # marginal/layers call Dual solely to construct zero/one, so Fraction
    # propagates throughout and no AD operation or mpmath conversion occurs.
    cond.Dual = Fraction
    c = cond.layers(N-1,*(cond.marginal(x,row) for row in w))
    diffs = [r['b2']-r['b1'] for r in c.values()]
    if not all(isinstance(v,Fraction) for r in c.values() for v in r.values()):
        raise TypeError('certificate graph left exact Fraction arithmetic')
    passed = all(v!=0 for v in diffs)
    ident = json.dumps(dict(nodes=list(map(str,x)),weights=[list(map(str,r)) for r in w]),sort_keys=True)
    payload = json.dumps([[*nu,*[str(c[nu][f]) for f in cond.FIELDS]] for nu in sorted(c)],separators=(',',':'))
    return dict(N=N,family=family,passed=passed,interior_sites=len(diffs),
                max_degree=N-2,min_abs_d=str(min(map(abs,diffs))),
                input_sha256=hashlib.sha256(ident.encode()).hexdigest(),
                exact_coefficient_payload_sha256=hashlib.sha256(payload.encode()).hexdigest(),
                elapsed_seconds=time.monotonic()-start)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes',nargs='+',type=int,default=list(range(4,65)))
    ap.add_argument('--family',choices=['krawtchouk','hahn'],default='hahn')
    args = ap.parse_args()
    result = dict(arithmetic='fractions.Fraction',
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  graph_code_sha256=hashlib.sha256(Path(cond.__file__).read_bytes()).hexdigest(),cases=[])
    for N in args.sizes:
        row = case(N,args.family)
        result['cases'].append(row)
        print(json.dumps(row),file=sys.stderr,flush=True)
    result['all_passed'] = all(r['passed'] for r in result['cases'])
    print(json.dumps(result,indent=2,sort_keys=True))
    if not result['all_passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
