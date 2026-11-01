"""Exact finite Fraction enclosure from the written analytic theorem73."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import platform
import time


def a(k):
    return F(comb(2*k,k),4**k)*(F(1,2*k+1)+F(1,2*k+2))


def J(k):
    return sum((F(1,2*r+1) for r in range(k+1)),F(0))/(2*k+2)


def atan_bounds(d):
    partial=sum((F((-1)**k,(2*k+1)*d**(2*k+1)) for k in range(64)),F(0))
    next_term=F(1,129*d**129)
    return partial,partial+next_term


def down(value,scale):
    return F(value.numerator*scale//value.denominator,scale)


def up(value,scale):
    return F(-((-value.numerator*scale)//value.denominator),scale)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-sha256',required=True)
    args=parser.parse_args()
    source=Path(__file__)
    digest=lambda:hashlib.sha256(source.read_bytes()).hexdigest()
    before=digest()
    assert before==args.source_sha256
    started=time.monotonic()
    terms=[a(k)*J(k) for k in range(66)]
    assert all(t>0 for t in terms)
    assert all(x>y for x,y in zip(terms,terms[1:]))
    partial=lambda K:sum(((-1)**k*terms[k] for k in range(K+1)),F(0))
    assert partial(1)==F(47,72) and partial(2)==F(1651,2400)
    s64,s65=partial(64),partial(65)
    assert s64-s65==terms[65] and 0<s65<s64
    lo5,hi5=atan_bounds(5)
    lo239,hi239=atan_bounds(239)
    exact_pi_lower=16*lo5-4*hi239
    exact_pi_upper=16*hi5-4*lo239
    pi_lower=down(exact_pi_lower,10**20)
    pi_upper=up(exact_pi_upper,10**20)
    assert 3<pi_lower<=exact_pi_lower<exact_pi_upper<=pi_upper<4
    lower,upper=8*s65/pi_upper**2,8*s64/pi_lower**2
    reported_lower,reported_upper=down(lower,10**12),up(upper,10**12)
    assert 0<reported_lower<=lower<upper<=reported_upper
    assert F(1,45)<reported_lower<reported_upper<2
    after=digest()
    assert after==before
    output={
      'scope':'K=64 finite rational evaluation conditional on analytic theorem73; no quadrature, fit or envelope/global assertion',
      'K':64,'arithmetic':'Python fractions.Fraction; exact integer operations only',
      'python':platform.python_version(),'source_sha256_before':before,'source_sha256_after':after,
      'pi_squared_g_strict_lower':str(8*s65),'pi_squared_g_strict_upper':str(8*s64),
      'pi_squared_g_series_interval_width':str(8*terms[65]),
      'machin_identity':'pi = 16 atan(1/5) - 4 atan(1/239)',
      'arctan_term_counts':[64,65],
      'pi_lower_outward_rational':str(pi_lower),'pi_upper_outward_rational':str(pi_upper),
      'g_lower_outward_rational':str(reported_lower),'g_upper_outward_rational':str(reported_upper),
      'g_reported_interval_width':str(reported_upper-reported_lower),
      'all_finite_exact_checks_passed':True,'elapsed_seconds':round(time.monotonic()-started,6)}
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
