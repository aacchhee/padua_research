# Post-audit D02 — Rectangular collision-strip averaging

Rules/input084a64f6465956f9c75b5538f83752c30318f151;2026-11-06.
Codex parent-assigned Sol xhigh mathematical worker, serving metadata
unexposed. Root alone controls Git/shared records and distinct review.

## Preregistered scope and resulting claims

The [new idea](../ideas/D02-corner.md) was written before proof or
diagnostic. D01/C07 were frozen. The first target was the rectangular
coordinate strip lemma at n>=1000; the further prospective target was
uniform K_new<=7.8 at n>=10000, followed by actual-corner comparison
using the exact finite corner lower bound. Caps:30 CPU-s diagnostic
and30min first analytic block; no new full-board/kernel/phase run,
producer, new degree certificate or child agent.

Three separate developer analytic results were written:

* [D02 strip](../theory/D02-corner-strip.md), **PROVED**: the complete
  weighted B charge is at most(14/5)[floor(n/2)+1/4]r2/(n+1),
  every n>=1000. This is half D01's charge. All used C07 floors were
  checked on the lower domain; the old small-j floor was explicitly
  identified as failing and is not used.
* [D02 sums](../theory/D02-corner-sums.md), **PROVED**: uniform explicit
  A1,A2,A3,sine/remainder bounds for every n>=10000. They use fixed
  harmonic sums, exact one-offset integrals,32-row rational bounds and
  positive tails. The slope/constant are not fitted to a degree table.
* [D02 comparison](../theory/D02-corner-comparison.md), **PROVED**:
  lambda<=a Lambda_c+[log(n+1)/3+7.8]r2 and
  lambda<=Lambda_c-r2/4 at both actual inward corner patches,
  every n>=10000. The exact n/(n+1) corner prefactor, endpoint1/(n+1),
  one-dimensional error and kappa shift are retained in its lower bound.

These are developer proofs with distinct review still separate, not
self-approved results. No global argmax/localization or new finite
global degree is claimed. D01 retains its primary failure, weaker
alternative failure and n=20000 kill for its old envelope.

## Cheapest proof decision and permitted MEASURED sanity

For E=F-aF0, pure second derivatives obey |E_ii|<=7n/5 on B.
Rectangular averaging gives |Av_four E|<=7n(alpha^2+beta^2)/10,
so the four-copy cost is14n r2/5. There is no rho2<=2r2 step.
This proves the precise separation before the scalar diagnostic.

Only after that lemma was written, a small Python command read the
existing pinned D01 receipt and subtracted half each old strip charge.
These derived numbers remain **MEASURED** sanity values:

| n | K_new measured lower | K_new measured upper |
|---:|---:|---:|
|1000|7.660820283445|7.663535519552|
|1001|7.664116476781|7.666832873295|
|10000|7.556284475846|7.560426010729|
|10001|7.556615395257|7.560756954960|
|20000|7.527991688166|7.532266473759|
|20001|7.528157187317|7.532431980156|
|100000|7.463494478487|7.467900759824|
|100001|7.463527584953|7.467933866691|

This was a scalar receipt transformation, not a new n100000 board
evaluation. It does not prove the uniform target, the n1000 actual
comparison or a sampled onset. The actual proof uses only the analytic
bounds in the linked files.

## Retained intermediate estimates and failure limits

The first uniform estimate retained C05's harmless5/8 row constant for
offsets>=3 and gave K_new<7.796 by the same exact scalar control.
It was retained as a valid coarse estimate. Rechecking that row's
actual b>=11/6 condition at n>=10000 improves5/8 to1/20, yielding
A1<=(7427/4000)L+331/50 and final analytic K_new<7.772. This is a
sharper bound inside the same preregistered allocation, not a changed
gate or rescue run. The positive-one integral correction is essential
to this proof route; omitting it wastes about1.495 in A1. No attempted
mechanism or rejected theorem was hidden by that sharpening.

## Executed exact scalar reproduction

Ordinary rational comparisons in the written proofs were also checked
by Python's standard-library Fraction. The final complete invocation
below actually printed

    all 22 exact rational checks passed
    A1_constant_upper 6.616079161147975
    K_upper 7.771035546065068
    strict_loss_lower 0.3402545044439202
    process_cpu_seconds 0.0012130000000000023

The decimals are explanatory conversions of exact rational values;
the asserted comparisons use Fractions. Earlier six single-process
scalar exploration/subtraction commands each returned successfully
within the tool's approximately0.3s reported elapsed time. No numerical
kernel or subprocess ran. The exact aggregate CPU of those preliminary
scalar commands was not individually metered; their combined elapsed
time plus the final command is below3s, safely inside the30 CPU-s cap.
No independent rerun is attributed to this worker.

Reproduction command, whose full body is committed here:

```bash
python - <<'PY'
from fractions import Fraction as F
from math import factorial
import resource
def cpu():
    return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime
               for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();N=10000;q=F(5,6);M=32;p2=F(9869,1000);checks={}
for a,goals in [(F(17,6),(F(1,16),F(19,1000))),
                (F(11,6),(F(39,200),F(19,200)))]:
    for power,goal in zip((3,4),goals):
        upper=sum(((a+2*j)**-power for j in range(3)),F())
        upper+=(a+4)**(1-power)/(2*(power-1))
        checks[f'tail_{a}_{power}']=upper<goal
def logbounds(x,K):
    u=(x-1)/(x+1)
    lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(K)),F())
    return lo,lo+2*u**(2*K+1)/(F(2*K+1)*(1-u*u))
z=F(1,3)-F(1,2*N);Y=2*q*q/(z*(q+1))
checks['log95_lower']=logbounds(F(95,6),40)[0]>F(1381,500)
checks['logY_upper']=logbounds(Y,8)[1]<F(411,500)
H8=sum((1/(2*j+q) for j in range(8)),F())
Rn=((z**-2-q**-2)/(2*q)+(z**-1-q**-1)/q**2)/2
Rp=((1/q-1/(q+1))/q**2+(q**-2-(q+1)**-2)/(2*q))/2
C0=2*q**-3*H8+q**-3*(-F(1381,500)+F(411,1000))+Rn-Rp
C0+=3*q**-4/(2*N)+F(19,1000)+F(19,200)
C0+=F(1,20)*(F(1,16)+F(39,200))
checks['A1_constant']=C0<F(331,50)
for p,r,pu,vu,goal in [
    (3,1,F(214557,100000),F(214569,100000),F(219,50)),
    (2,2,F(243706,100000),F(249564,100000),F(511,100))]:
    P=sum(((2*j+q)**-p*q**-r for j in range(M+1)),F())
    P+=(2*M+q)**(1-p)/(2*(p-1))*q**-r
    V=sum(((2*j+q)**-p*(q-F(j,N))**-r for j in range(M+1)),F())
    V+=(2*M+q)**(1-p)/(2*(p-1))*3**r
    O=(F(19,1000)+F(1,16)/(2*(p-1)))*(1+F(17,11)**r)
    checks[f'P_{p}{r}']=P<pu;checks[f'V_{p}{r}']=V<vu
    checks[f'A_{p}{r}']=pu+vu+O<goal
pi_lower=16*(F(1,5)-F(1,375)+F(1,15625)-F(1,546875))-F(4,239)
checks['pi_bound']=pi_lower>F(31415,10000) and F(31415,10000)**2>p2
checks['H_bound']=sum((F(10**j,factorial(j)) for j in range(16)),F())>20002
G=1/(F(1,3)-F(1,2*N))+F(51,25*N);tau=F(N+1,N)
Cs=F(50,9)*tau/p2*G+F(108,25)*tau*F(11,N)
Cr=30*tau**2/(p2*N)+F(18,25)*tau*F(11,N*N)
Cr+=F(3456,25)*tau*F(11,N*N)/p2+F(8,N*(N+1))
checks['sine']=Cs<F(339,200);checks['remainder']=Cr<F(31,100000)
f1=16*tau**3/p2**2;f2=4*tau**3/p2
slope=f1*F(7427,4000)-F(1,3)
K=slope*F(46,5)+f1*F(331,50)+f2*F(949,100)
K+=F(339,200)+F(7,5)+F(31,100000)
checks['K']=slope<0 and K<F(1943,250)<F(39,5)
E0=F(144,10001)+F(6,100000000)
strict=F(5501,16000)-F(47,192)*E0-F(1,30000)
checks['strict']=strict>F(1,4)
tau0=F(1001,1000)
checks['strip_polynomial']=(F(151,100)*tau0+F(151,100)*tau0**2
                           +tau0**3/2+F(88,25)<F(71,10))
checks['V_floors']=(F(7,4)<=F(1000,100)
                   and F(7,2)*1000+F(23,8)<=F(1000**2,100))
checks['F_floor']=F(71,80)*1000+F(1,2)<=F(9,10)*1000
assert all(checks.values()),checks
print('all',len(checks),'exact rational checks passed')
print('A1_constant_upper',float(C0),'K_upper',float(K),
      'strict_loss_lower',float(strict))
print('process_cpu_seconds',cpu()-start)
PY
```

## Review and stop boundary

The developer's analytic first block is complete. Root's distinct
review should reconstruct the coordinate normalization, pure derivative
floors, positive-one correction direction, negative-one upper endpoint,
32-row bounds, sine telescoping and the unrounded corner comparison.
The complete Fraction block above is available for an actual independent
scalar rerun; no such rerun is claimed here. The written proof is
explicit enough to inspect its finite rational arithmetic directly.

All three separate theory records remain developer results pending
that independent acceptance. No further diagnostic or producer run is
needed for this bounded block. No old proof, D01 receipt, quantifier,
certificate or one-correction model was edited.
