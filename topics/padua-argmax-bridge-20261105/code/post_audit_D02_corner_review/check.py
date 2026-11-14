"""Independent exact scalar reconstruction of D02; no board/kernel run.

All acceptance comparisons use Fraction. Decimal output is presentation only.
This supplements the analytic review; it does not assert sampled uniformity.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import resource

TOPIC = Path(__file__).resolve().parents[2]
N, q = 10000, Q(5, 6)
checks = {}
values = {}

def less(name, lhs, rhs):
    checks[name] = bool(lhs < rhs)
    assert checks[name], (name, lhs, rhs)

def log_interval(x, terms):
    u = (x-1)/(x+1)
    lo = 2*sum((u**k/k for k in range(1, 2*terms, 2)), Q())
    return lo, lo+2*u**(2*terms+1)/((2*terms+1)*(1-u*u))

# Strip pure-phase bounds, including the corrected first-coordinate mode.
t0 = Q(1001,1000)
less('secant', Q(25,17), Q(3,2))
less('secant_prime', Q(3,2)*Q(6,5)/2, 1)
less('secant_second', Q(3,2)*(Q(6,5)**2+Q(3,2)**2)/4, Q(3,2))
less('V_first_floor', Q(7,4)/1000, Q(1,100))
less('V_second_floor', Q(7,2)/1000+Q(23,8)/1000**2, Q(1,100))
strip_poly = Q(151,100)*(t0+t0*t0)+t0**3/2+Q(88,25)
less('D_second_budget', strip_poly, Q(71,10))
less('corrected_F_floor', Q(71,80)+Q(1,2000), Q(9,10))
less('baseline_small_T', Q(22,7)/(4*1001), Q(1,1000))
less('baseline_sine_loss', Q(1,1000)**2/6, Q(1,100))
less('baseline_F0_factor', Q(25,99)*Q(22,7), 1)
less('regular_phase_error', 3*t0, Q(31415,10000))
less('regular_upper_T', Q(11,7)+Q(1,4000), Q(8,5))
less('regular_T_over_Z', 1+6*t0/(5*Q(31415,10000)), Q(7,5))
x = Q(8,5)
less('sine_chord', Q(3,5), 1-x*x/6+x**4/120-x**6/5040)

# Four offset-series constants, each from three exact terms and a tail integral.
for tag, start, exponent, target in (
    ('Q3',Q(17,6),3,Q(1,16)),('Q4',Q(17,6),4,Q(19,1000)),
    ('R3',Q(11,6),3,Q(39,200)),('R4',Q(11,6),4,Q(19,200))):
    val = sum((1/(start+2*j)**exponent for j in range(3)), Q())
    val += 1/(2*(exponent-1)*(start+4)**(exponent-1))
    less(tag, val, target)
    values[tag] = float(val)
less('offset_harmonic_row', Q(1,10001)+Q(12,11), Q(11,10))

# The two one-offset corrections have opposite signs. Combine their logs
# only after subtracting the positive-offset improvement.
z = Q(1,3)-Q(1,2*N)
Y = 2*q*q/(z*(q+1))
assert Y == Q(500000,219967)
less('log_95_lower', Q(1381,500), log_interval(Q(95,6),40)[0])
less('log_Y_upper', log_interval(Y,8)[1], Q(411,500))
harmonic8 = sum((1/(2*j+q) for j in range(8)), Q())
negative_rational = (z**-2-q**-2)/(4*q)+(z**-1-q**-1)/(2*q*q)
positive_rational = (q**-1-(q+1)**-1)/(2*q*q)+(q**-2-(q+1)**-2)/(4*q)
a1_const = 2*q**-3*harmonic8+q**-3*(-Q(1381,500)+Q(411,1000))
a1_const += negative_rational-positive_rational+3*q**-4/(2*N)
a1_const += Q(19,1000)+Q(19,200)+(Q(1,16)+Q(39,200))/20
less('A1_constant', a1_const, Q(331,50))
assert q**-3+(Q(1,16)+Q(39,200))/2 == Q(7427,4000)

# 0,...,32 contains 33 exact rows; the tail starts at32.
for p,r,pbound,vbound,total_bound in (
    (3,1,Q(214557,100000),Q(214569,100000),Q(219,50)),
    (2,2,Q(243706,100000),Q(249564,100000),Q(511,100))):
    tail = (64+q)**(1-p)/(2*(p-1))
    positive = sum(((2*j+q)**-p for j in range(33)),Q())*q**-r+tail*q**-r
    negative = sum(((2*j+q)**-p*(q-Q(j,N))**-r for j in range(33)),Q())+tail*3**r
    other = (Q(19,1000)+Q(1,32*(p-1)))*(1+Q(17,11)**r)
    less(f'P{p}{r}', positive,pbound)
    less(f'V{p}{r}', negative,vbound)
    less(f'A{p}{r}_rounded_budget', pbound+vbound+other,total_bound)
    values[f'A{p}{r}_unrounded_budget'] = float(positive+negative+other)

# Check the exact telescoping formula for arbitrary symbolic truncation
# through algebra: partial sums at equal positive/negative cutoff leave
# 1/q-1/(q+2M+1). The analytic limit is1/q, as reviewed in prose.
for M in (0,1,5):
    telescoped = sum((1/(q+2*j)-1/(q+2*j+1) for j in range(M+1)),Q())
    telescoped += sum((1/(q+2*j-1)-1/(q+2*j) for j in range(1,M+1)),Q())
    assert telescoped == 1/q-1/(q+2*M+1)

pi_lower = 16*sum((Q((-1)**j,(2*j+1)*5**(2*j+1)) for j in range(4)),Q())-Q(4,239)
less('pi_lower', Q(31415,10000),pi_lower)
pi2 = Q(9869,1000)
less('pi_square',pi2,Q(31415,10000)**2)
less('exp10',20002,sum((Q(10)**k/factorial(k) for k in range(16)),Q()))
tau = Q(N+1,N)
g = 1/z+Q(51,25*N)
sine = 50*tau*g/(9*pi2)+108*tau*11/(25*N)
rem = 30*(N+1)**2/(pi2*N**3)+Q(18*(N+1)*11,25*N**3)
rem += Q(3456*(N+1)*11,25*N**3)/pi2+Q(8,N*(N+1))
less('sine_budget',sine,Q(339,200))
less('remainder_budget',rem,Q(31,100000))
f1,f2 = 16*tau**3/pi2**2,4*tau**3/pi2
slope = Q(7427,4000)*f1-Q(1,3)
less('negative_log_slope',slope,0)
K = slope*Q(46,5)+f1*Q(331,50)+f2*Q(949,100)+Q(339,200)+Q(7,5)+Q(31,100000)
less('uniform_K',K,Q(1943,250))
less('target_K',Q(1943,250),Q(39,5))

# Exact logarithm/kappa support and the final strictly positive margin.
log10_lower = 3*log_interval(Q(2),4)[0]+log_interval(Q(5,4),1)[0]
less('log10_lower',Q(23,10),log10_lower)
less('log10_upper',10,sum((Q(2303,1000)**k/factorial(k) for k in range(11)),Q()))
gamma_lower = sum((Q(1,k) for k in range(1,11)),Q())-Q(2303,1000)-Q(1,20)
less('gamma_lower',Q(23,40),gamma_lower)
less('log8pi_lower',Q(37,40),log_interval(Q(28,11),2)[0])
ell = Q(46,5)
p = Q(47,480)*(ell+Q(3,2))**2-ell/3-Q(39,5)
assert p == Q(5501,16000)
less('p_increasing',0,Q(47,240)*(ell+Q(3,2))-Q(1,3))
less('E_first_decreasing',2*tau-(ell+2),0)
less('E_second_decreasing',1-2*(ell+2),0)
E0 = Q(144,10001)+Q(6,100000000)
margin = p-Q(47,192)*E0-Q(1,30000)
less('strict_loss',Q(1,4),margin)

values.update(A1_constant=float(a1_const),sine=float(sine),remainder=float(rem),
              K_upper=float(K),strict_loss_lower=float(margin))
def ident(p):
    data = p.read_bytes()
    return dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
receipt = dict(status='PASS',requested_model='gpt-6-astra high',serving_metadata='unexposed',
    rules_head='084a64f6465956f9c75b5538f83752c30318f151',
    scope='Exact scalar comparisons supporting an independent analytic review; no board/phase/kernel runs',
    checker=ident(Path(__file__).resolve()),
    reviewed_prose=[ident(TOPIC/'theory'/f'D02-corner-{x}.md') for x in ('strip','sums','comparison')],
    checks=checks,checks_count=len(checks),values_presentation_only=values,
    exact_final_values=dict(K=str(K),strict_loss=str(margin)),
    cpu_seconds_through_checks=sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime
                                  for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN)))
target = TOPIC/'evidence/d02-review-corner.json'
target.write_text(json.dumps(receipt,indent=2)+'\n')
assert target.stat().st_size<16384
print(json.dumps(dict(checks=len(checks),status='PASS',values=values,
                     cpu_seconds_through_checks=receipt['cpu_seconds_through_checks'],receipt=ident(target))))
