#!/usr/bin/env python3
"""Independent exact scalar/finite controls; no row backend or native calls."""
from fractions import Fraction as F
from math import comb, factorial, floor, ceil
from pathlib import Path
import hashlib
import json
import platform
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (50, 55))
started = time.process_time()
checks = 0

def check(ok):
    global checks
    assert ok
    checks += 1

# Newton differences of (s+1)^4, not a hard-coded generating function.
row = [F((i+1)**4) for i in range(5)]
differences = []
while row:
    differences.append(row[0])
    row = [b-a for a,b in zip(row,row[1:])]
r = F(1,4)
fourth_sum = sum(d*r**j/(1-r)**(j+1) for j,d in enumerate(differences))
check(fourth_sum == F(1520,81))
tail_constant = F(1024,243)*fourth_sum/4
check(tail_constant == F(389120,19683))
M96 = tail_constant * F(195**4,3**5*4**96)
check(M96 < F(1,2**165))

# Akiyama--Tanigawa construction, whose B1 convention is +1/2;
# all even coefficients equal the t/(exp(t)-1) convention used in the proof.
work, bernoulli = [], []
for degree in range(65):
    work.append(F(1,degree+1))
    for j in range(degree,0,-1):
        work[j-1] = j*(work[j-1]-work[j])
    bernoulli.append(work[0])
check(bernoulli[64] == F(-106783830147866529886385444979142647942017,510))
eta = abs(bernoulli[64])/F(64*64**64)
coarse_eta = F(4*factorial(63),6**64*64**64)
check(eta <= coarse_eta < F(1,2**256))
smooth_factor = F(7*4**4,2880)*F(7,24)
harmonic_factor = 16*(2+F(4,3)*65)
check(smooth_factor < F(1,5))
check(harmonic_factor < 2**11)
check(M96*smooth_factor+coarse_eta*harmonic_factor < F(1,2**166))

# Unit-cell quartic residual and normalized fourth derivative.
quartic_functional = F(1,80)-F(1,24)
check(quartic_functional/24 == -F(7,5760))

# Construct an exact discrete antiderivative by triangular coefficient
# elimination. The q-independent polynomial identity is checked in full.
power_degrees = [0,1,2,3,31,193]
for degree in power_degrees:
    residual = [F(0)]*(degree+1)
    residual[degree] = F(1)
    coefficients = [F(0)]*(degree+2)
    for j in range(degree,-1,-1):
        coefficient = residual[j]/(j+1)
        coefficients[j+1] = coefficient
        for ell in range(j+1):
            residual[ell] -= coefficient*comb(j+1,ell)
    check(all(x == 0 for x in residual))
    def evaluate(t):
        value = F(0)
        for c in reversed(coefficients):
            value = value*t+c
        return value
    for t in (F(-7,3),F(0),F(11,2),F(10**20)):
        check(evaluate(t+1)-evaluate(t) == t**degree)

# Exact log enclosure via the positive atanh series, for small finite
# reference sums. This diagnostic enumeration is not an evaluation backend.
em_cases = []
for prefix, order, q, y in [(2,1,17,F(1,10)),(64,32,65,F(1,10)),
                           (64,32,100,F(1,10)),(64,32,100,F(5))]:
    x, z = y+prefix, y+q
    t = (z-x)/(z+x)
    terms = 512
    loglo = 2*sum(t**(2*j+1)/F(2*j+1) for j in range(terms))
    logtail = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    explicit = sum(1/(y+i) for i in range(prefix))
    correction = F(1,2)*(1/x-1/z)+sum(
        bernoulli[2*j]/(2*j)*(x**(-2*j)-z**(-2*j)) for j in range(1,order+1))
    target = sum(1/(y+i) for i in range(q))
    upper_error = max(abs(target-explicit-correction-loglo),
                      abs(target-explicit-correction-loglo-logtail))
    local_bound = abs(bernoulli[2*order])/F(2*order)*(x**(-2*order)-z**(-2*order))
    check(upper_error < local_bound)
    em_cases.append(dict(K=prefix,L=order,q=q,y=str(y),exact_remainder_bound_pass=True))

# Exact normalized open-arc floor/ceil indexing, including grid coincidences
# and the seam. Only finite controls: the proof covers arbitrary degrees.
arc_cases = 0
for n in (2,3,7,16,31):
    for shift in (F(0),F(1,2),F(3,4)):
        for left,right in [(F(0),F(1)),(F(1,4),F(3,4)),
                           (shift/n,(shift+1)/n),(F(0),shift/n),
                           (F(2,7),F(5,7))]:
            lo = max(0,floor(n*left-shift)+1)
            hi = min(n-1,ceil(n*right-shift)-1)
            selected = list(range(lo,hi+1)) if lo <= hi else []
            direct = [k for k in range(n) if left < (k+shift)/n < right]
            check(selected == direct)
            arc_cases += 1

source = Path(__file__).resolve()
result = dict(schema='C02-row-independent-exact-controls-v1',status='PASS',
              assertions=checks,cpu_seconds=time.process_time()-started,
              python=platform.python_version(),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              bernoulli_B64=str(bernoulli[64]),geometric_sum=str(fourth_sum),
              polynomial_degrees=power_degrees,em_cases=em_cases,open_arc_cases=arc_cases,
              command='python topics/padua-argmax-bridge-20261105/code/cheap_c02_row_review/control.py',
              scope='Supplementary exact controls; no production row evaluation, whole-box enclosure, cover, or degree certification.')
print(json.dumps(result,indent=2))
