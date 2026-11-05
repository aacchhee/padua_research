#!/usr/bin/env python3
"""Rigorous finite Padua witness by certified fixed-point tensor evaluation.

NumPy only proposes an exact dyadic polynomial. All acceptance arithmetic is
FLINT integer/rational or outward-rounded Arb. See certifier-design.md.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import sys
import time
import numpy as np
import flint
from flint import arb, ctx, fmpq, fmpz, fmpz_mat


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rounded_ball(value, scale):
    z = ((value * scale).mid() + arb(fmpq(1, 2))).floor().unique_fmpz()
    if z is None or not abs(value - arb(z) / scale) < arb(1) / scale:
        raise ArithmeticError('fixed-point table enclosure rejected; raise --precision')
    return z


def table(m, degree, bits, family):
    """All exact values enclosed within 2^-bits of returned integer/2^bits."""
    scale = 1 << bits
    entries = []
    for j in range(m + 1):
        # cos_pi(fmpq) avoids a separately rounded pi or trigonometric argument.
        x = arb(fmpq(j, m)).cos_pi()
        prev, value = arb(1), x
        entries.append(fmpz(scale))
        if degree:
            entries.append(rounded_ball(value, scale))
        for k in range(1, degree):
            if family == 'legendre':
                following = ((2*k + 1)*x*value - k*prev)/(k + 1)
            else:
                following = 2*x*value-prev
            entries.append(rounded_ball(following, scale))
            prev, value = value, following
    return fmpz_mat(m + 1, degree + 1, entries)


def exact_round_fraction(num, den, scale):
    # floor(scale*num/den+1/2), exact also for negative moments.
    return (2 * scale * num + den) // (2 * den)


def moment_coefficients(m, bits):
    scale = 1 << bits
    values=[]
    total_abs=fmpq(0)
    rounded_error=fmpq(0)
    for a in range(m+1):
        for b in range(m+1):
            if a+b>m or a%2 or b%2:
                values.append(fmpz(0)); continue
            numerator=4*(1 if a==0 else 2)*(1 if b==0 else 2)
            denominator=(1-a*a)*(1-b*b)
            if a==m and b==0:
                denominator*=2
            if denominator<0: numerator,denominator=-numerator,-denominator
            z=exact_round_fraction(numerator,denominator,scale)
            values.append(fmpz(z))
            exact=fmpq(numerator,denominator)
            total_abs+=abs(exact)
            rounded_error+=abs(exact-fmpq(z,scale))
    return fmpz_mat(m+1,m+1,values), total_abs, rounded_error


def propose(vector_path, m, n, bits):
    v=np.load(vector_path,allow_pickle=False)
    if v.ndim!=1 or v.size!=(n+1)*(n+2)//2 or not np.isfinite(v).all():
        raise ValueError('invalid vector shape/content')
    scale=1<<bits
    c=[0]*((n+1)**2)
    pos=0
    for total in range(n+1):
        for a in range(total,-1,-1):
            b=total-a
            # Proposal only: these integer coefficients define the exact witness.
            c[a*(n+1)+b]=int(round(float(v[pos])*math.sqrt((2*a+1)*(2*b+1))/2*scale))
            pos+=1
    return c


def integral(coefficients,n,bits):
    total=fmpq(0)
    for a in range(n+1):
        row=fmpq(0)
        for b in range(n+1-a):
            c=coefficients[a*(n+1)+b]
            if c: row+=fmpq(c*c,2*b+1)
        total+=row/(2*a+1)
    return total*fmpq(4,1<<(2*bits))


def enclosure_string(value):
    return str(value)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--m',type=int,required=True)
    ap.add_argument('--n',type=int)
    ap.add_argument('--vector',type=Path)
    ap.add_argument('--witness',type=Path)
    ap.add_argument('--bits',type=int,default=56)
    ap.add_argument('--precision',type=int)
    ap.add_argument('--scratch',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    m=args.m;n=m-1 if args.n is None else args.n
    if not 0<=n<m or m<2:raise ValueError('require m>=2 and 0<=n<m')
    if args.bits<16:raise ValueError('insufficient fixed-point precision')
    args.scratch.mkdir(parents=True,exist_ok=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();timings={}
    ctx.prec=args.precision or (2*m+args.bits+160)
    if args.witness:
        payload=json.loads(gzip.decompress(args.witness.read_bytes()))
        if (payload['m'],payload['n'],payload['bits'])!=(m,n,args.bits):raise ValueError('witness convention mismatch')
        coefficients=payload['coefficients']
        witness=args.witness
    else:
        if args.vector is None:raise ValueError('supply --vector or --witness')
        coefficients=propose(args.vector,m,n,args.bits)
        witness=args.scratch/'witness.json.gz'
        payload=dict(m=m,n=n,bits=args.bits,basis='unnormalized Legendre P_a P_b, row-major square',coefficients=coefficients)
        witness.write_bytes(gzip.compress(json.dumps(payload,separators=(',',':')).encode(),mtime=0))
    if len(coefficients)!=(n+1)**2 or any(not isinstance(c,int) for c in coefficients):raise ValueError('invalid coefficients')
    if any(coefficients[a*(n+1)+b] for a in range(n+1) for b in range(n+1) if a+b>n):raise ValueError('total degree violated')
    if not any(coefficients):raise ValueError('zero witness')
    norm=integral(coefficients,n,args.bits)
    if not norm>0:raise ArithmeticError('nonpositive exact norm')
    norm_path=args.scratch/'exact-norm.txt'
    norm_path.write_text(str(norm)+'\n')
    coefficient_l1=fmpq(sum(abs(c) for c in coefficients),1<<args.bits)
    timings['proposal_and_exact_norm']=time.monotonic()-start
    tick=time.monotonic()
    lx=table(m,n,args.bits,'legendre');ly=table(m+1,n,args.bits,'legendre')
    timings['legendre_tables']=time.monotonic()-tick
    print('Legendre tables',m,timings['legendre_tables'],flush=True)
    tick=time.monotonic()
    cmat=fmpz_mat(n+1,n+1,coefficients)
    nodal=(lx*cmat)*ly.transpose()
    del lx,ly,cmat
    timings['integer_polynomial_tensor']=time.monotonic()-tick
    print('polynomial tensor',m,timings['integer_polynomial_tensor'],flush=True)
    tick=time.monotonic()
    tx=table(m,m,args.bits,'chebyshev');ty=table(m+1,m,args.bits,'chebyshev')
    dmat,d_l1,d_error=moment_coefficients(m,args.bits)
    kernel=(tx*dmat)*ty.transpose()
    del tx,ty,dmat
    timings['certified_weight_tensor']=time.monotonic()-tick
    print('weight tensor',m,timings['certified_weight_tensor'],flush=True)
    tick=time.monotonic()
    qnum=fmpz(0);anum=fmpz(0);bnum=fmpz(0);wnum=fmpz(0);rhonum=0
    for j in range(m+1):
        ej=1 if j in (0,m) else 2
        for k in range(j%2,m+2,2):
            ek=1 if k in (0,m+1) else 2
            factor=ej*ek
            p2=nodal[j,k]**2
            kval=kernel[j,k]
            wnum+=factor*kval
            qnum+=factor*kval*p2
            anum+=factor*abs(kval)*p2
            bnum+=factor*p2
            rhonum+=factor
    rho_den=2*m*(m+1)
    if rhonum!=rho_den:raise ArithmeticError('Padua rho mass is not one')
    scale=1<<args.bits
    center=fmpq(qnum,rho_den*scale**9)
    absolute_energy=fmpq(anum,rho_den*scale**9)
    reference_energy=fmpq(bnum,rho_den*scale**6)
    eps=fmpq(1,scale)
    p_error=coefficient_l1*(2*eps+eps**2)
    # |T|<=1; both table errors <=eps, coefficient l1 error d_error.
    k_error=d_l1*(2*eps+eps**2)+d_error*(1+eps)**2
    ctx.prec=max(128,args.bits*2)
    weight_sum=arb(fmpq(wnum,rho_den*scale**3))+arb(0,arb(k_error).abs_upper())
    if not weight_sum.contains(4):raise ArithmeticError('certified weights do not enclose mass four')
    weight_energy=arb(absolute_energy+k_error*reference_energy)
    error=arb(k_error*reference_energy)+2*arb(p_error)*(weight_energy*arb(d_l1)).sqrt()+arb(p_error**2*d_l1)
    qball=arb(center)+arb(0,error.abs_upper())
    quotient=qball/arb(norm)
    sign='negative' if qball<0 else 'positive' if qball>0 else 'undetermined'
    timings['exact_contraction_and_enclosure']=time.monotonic()-tick
    if sign=='undetermined':raise ArithmeticError('enclosure straddles zero')
    report=dict(kind='rigorous fixed-point Padua polynomial energy',m=m,n=n,bits=args.bits,
        table_precision=args.precision or (2*m+args.bits+160),
        arithmetic='FLINT fmpz/fmpq exact; Arb outward balls; NumPy proposal only',
        dependencies=dict(python=sys.version,flint=flint.__version__,numpy=np.__version__,platform=platform.platform()),
        command=sys.argv,code_sha256=sha(__file__),
        definitions_sha256=sha(Path(__file__).resolve().parents[3]/'topics/padua-mz-2d-20261101/definitions.md'),
        witness=dict(path=str(witness),sha256=sha(witness),bytes=witness.stat().st_size,
                     source_vector_sha256=sha(args.vector) if args.vector else None),
        exact_norm=dict(path=str(norm_path),sha256=sha(norm_path),bytes=norm_path.stat().st_size,sign='positive',numerator_bits=int(norm.numerator).bit_length(),
                        denominator_bits=int(norm.denominator).bit_length(),enclosure=str(arb(norm)),
                        rational_value_sha256=hashlib.sha256(str(norm).encode()).hexdigest()),
        weight_sum_enclosure=str(weight_sum),
        energy_enclosure=str(qball),rayleigh_enclosure=str(quotient),sign=sign,
        absolute_energy_enclosure=str(arb(absolute_energy)),reference_energy_enclosure=str(arb(reference_energy)),
        coefficient_l1_enclosure=str(arb(coefficient_l1)),kernel_l1_bound=str(arb(d_l1)),
        polynomial_pointwise_error_bound=str(arb(p_error)),kernel_pointwise_error_bound=str(arb(k_error)),
        energy_error_bound=str(error),relative_width_upper=str(2*error/abs(arb(center))),
        seconds=time.monotonic()-start,phase_seconds=timings,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        status='rigorous producer sign accepted; independent check required')
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('m','sign','energy_enclosure','rayleigh_enclosure','relative_width_upper','seconds')}),flush=True)

if __name__=='__main__':main()
