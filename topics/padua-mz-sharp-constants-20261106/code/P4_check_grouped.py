#!/usr/bin/env python3
"""Alternate exact Rayleigh assembly, grouping the coefficient of each d_j.

Shares the declared interval/scalar code, but not producer form assembly.
An independent agent must actually execute this checker and inspect the
shared scalar routines; this script alone is not an independent rerun.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
from interval_dyadic import BITS,I,model_scalars


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trial',type=Path,required=True)
    parser.add_argument('--producer',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    started,cpu = time.monotonic(),time.process_time()
    trial = json.loads(args.trial.read_text())
    assert trial['J']==512 and trial['encoding']=='exact binary64 hex'
    u = [Fraction(float.fromhex(v)) for v in trial['u']]
    assert len(u)==512 and any(u)
    pi,d,si,si2 = model_scalars(512)
    coeff = [2*v*v for v in u]
    # Coefficient of d_j from each symmetric off-diagonal pair is formed
    # exactly in Fraction, before converting to one interval.
    for j in range(1,513):
        for i in range(1,j):
            factor = Fraction(4*(-1)**(i+j)*u[i-1]*u[j-1],i*i-j*j)
            coeff[j-1] += factor*i*i
            coeff[i-1] -= factor*j*j
    s = sum(((-1)**j*u[j-1] for j in range(1,513)),Fraction())
    num = I.rational(4*s*s)
    den = I.rational(0)
    for j in range(1,513):
        square = u[j-1]**2
        num += I.rational(2*square)*((-1)**j+j*pi*si[j-1])
        den += I.rational(2*square)*j*pi*si2[j-1]+I.rational(coeff[j-1])*d[j-1]
    assert den.lo > 0
    quotient = num/den
    threshold = quotient.lo*10000000 >= 10044369*(1<<BITS)
    producer = json.loads(args.producer.read_text())
    p = producer['quotient']
    overlap = quotient.lo <= int(p['hi_integer']) and int(p['lo_integer']) <= quotient.hi
    assert producer['trial_sha256']==digest(args.trial)
    result = dict(checker='independent grouped form assembly; shared scalar intervals',
                  trial_sha256=digest(args.trial),producer_receipt_sha256=digest(args.producer),
                  checker_sha256=digest(__file__),
                  arithmetic_sha256=digest(Path(__file__).with_name('interval_dyadic.py')),
                  python=sys.version,platform=platform.platform(),command=sys.argv,
                  numerator=num.record(),denominator=den.record(),quotient=quotient.record(),
                  finite_threshold_pass=threshold,producer_enclosure_overlap=overlap,
                  seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('finite_threshold_pass','producer_enclosure_overlap','seconds')}))
    assert threshold and overlap


if __name__=='__main__':
    main()
