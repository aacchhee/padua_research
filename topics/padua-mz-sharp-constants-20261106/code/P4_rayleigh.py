#!/usr/bin/env python3
"""Prepare a float trial, or enclose its exact finite-J Rayleigh quotient.

Preparation's approximate eigenvector is only an input-selection heuristic.
The certificate mode imports no NumPy/SciPy and uses exact dyadic endpoints.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time
from fractions import Fraction
from interval_dyadic import BITS, I, model_scalars

ROOT = Path(__file__).resolve().parents[1]
TARGET = Fraction(10044369,10000000)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_trial(path):
    data = json.loads(Path(path).read_text())
    assert data['J'] == 512 and data['encoding'] == 'exact binary64 hex'
    values = data['u']
    assert len(values) == data['J']
    u = [Fraction(float.fromhex(x)) for x in values]
    assert any(u)
    return u


def prepare(path):
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
        assert os.environ.get(key) == '1', f'set {key}=1 before preparation'
    import numpy as np
    import scipy
    from scipy.linalg import eigh
    from S2_model import gram
    C,D = gram(512)
    vals,vectors = eigh(D,C,subset_by_index=[511,511],driver='gvx')
    data = dict(J=512,encoding='exact binary64 hex',u=[float(v).hex() for v in vectors[:,0]])
    # Compact trial stays below the repository's normal 16 KiB evidence cap.
    Path(path).write_text(json.dumps(data,separators=(',',':'))+'\n')
    assert Path(path).stat().st_size < 16384
    return dict(status='MEASURED trial preparation only',J=512,
                approximate_eigenvalue=float(vals[0]),numpy=np.__version__,
                scipy=scipy.__version__,trial_sha256=digest(path),
                S2_model_sha256=digest(ROOT/'code/S2_model.py'))


def compute(u):
    pi,d,si,si2 = model_scalars(len(u))
    ui = [I.rational(x) for x in u]
    signed_sum = sum(((-1)**j*u[j-1] for j in range(1,len(u)+1)),Fraction())
    numerator = I.rational(4*signed_sum*signed_sum)
    denominator = I.rational(0)
    for j,v in enumerate(ui,1):
        a = j*pi
        numerator += 2*((-1)**j+a*si[j-1])*I.rational(u[j-1]**2)
        denominator += 2*(a*si2[j-1]+d[j-1])*I.rational(u[j-1]**2)
        for i in range(1,j):
            cij = 2*((-1)**(i+j))*(i*i*d[j-1]-j*j*d[i-1])/(i*i-j*j)
            denominator += 2*cij*I.rational(u[i-1]*u[j-1])
    assert denominator.lo > 0
    quotient = numerator/denominator
    passed = quotient.lo*TARGET.denominator >= TARGET.numerator*(1<<BITS)
    return dict(J=len(u),arithmetic='integer dyadic outward intervals',bits=BITS,
                target=str(TARGET),denominator_positive=True,
                numerator=numerator.record(),denominator=denominator.record(),
                quotient=quotient.record(),finite_threshold_pass=passed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trial',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--prepare',action='store_true')
    args = parser.parse_args()
    start,time_cpu = time.monotonic(),time.process_time()
    result = prepare(args.trial) if args.prepare else compute(read_trial(args.trial))
    result.update(command=sys.argv,python=sys.version,platform=platform.platform(),
                  producer_sha256=digest(__file__),
                  arithmetic_sha256=digest(ROOT/'code/interval_dyadic.py'),
                  protocol_sha256=digest(ROOT/'attempts/P4.md'),
                  trial_sha256=digest(args.trial),
                  seconds=time.monotonic()-start,cpu_seconds=time.process_time()-time_cpu,
                  status=result.get('status','finite check; independent rerun/proof review required'))
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','seconds','trial_sha256')}))
    if not args.prepare and not result['finite_threshold_pass']:
        raise SystemExit('fixed threshold not certified')


if __name__ == '__main__':
    main()
