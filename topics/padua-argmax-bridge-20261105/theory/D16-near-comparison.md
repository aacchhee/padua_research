# PD-T?argmax-bridge-codex-D16-near — Near noncorner exclusion from degree10000

ID kind: PD-T. Aliases: quadratic absorption of phase-dependent absolute
errors; separate-origin near comparison. Split from: D16 onset.
Split into: the analytic allowance has its own D16 record.

## Statement and status

For every integer n>=10000, m=n+1, and physical odd center
0<=J<=n,0<=K<=m,J+K odd, which is not an actual nonnode corner,
suppose theta=(J*pi+alpha)/n,phi=(K*pi+beta)/m belong to[0,pi] and
rho=|alpha|+|beta|<=1/2. With exactly PD-T101/PD-T364's corrected
Padua cardinals, exceptional highest x mode, endpoint weights and
finite-polynomial collision values,

    lambda_n(cos theta,cos phi)<Lambda_c(n)-11/1000,    (1)
    Lambda_c(n)=S_n(0,0)=lambda_n(-1,-1).

Status: **PROVED**, developer analytic assembly under the directed
Decimal numerical contract in SPEC, with independent review PENDING.
No independent acceptance or root range adoption is asserted.

## Dependencies and definitions

C08-far-weighted-coefficient gives b_full-b_c<=3(1-a)/pi^2 on the
closed phase diamond. D10-relative-constant gives, on rho<=1/2,

    C_infty(psi)-C_infty(0)<=15rho^(3/2)/32+(113/72)r2
                              +(4/9)r2*log(1/rho),
    r2=alpha^2+beta^2,

with continuous origin value. D16-phase-allowance proves the NEW
absolute bounds C+K*rho and E0 on n>=32, at their actual phases.
C02-defect-dense-band gives the physical projected floor >1/16 on
the full physical rho<=1/2 guard for n>=4096. The true completed
model and full defect identity are exactly D02 and PD-T364.

All analytic arithmetic is exact over the reals; logs are natural.
Work at absolute phases only for S_n and M_infty, retaining the
physical defect at its original signed center. No mesh interchange.
Set L=log n,a=(cos|alpha|+cos|beta|)/2,u=1-a and

    T=(4L^2-3L)/pi^2, A=77/96,
    B=[(47/192)T-113/72]/2,
    J0=27A^4/(256B^3).

The name J0 denotes a scalar maximum, not the physical center J.

## Proof

The coefficient bound gives

    M_infty(psi,L)-M_infty(0,L)
         <=-u*T+C_infty(psi)-C_infty(0).              (2)

For |alpha|,|beta|<=1/2 the alternating cosine bound implies
u>=r2/4-(alpha^4+beta^4)/48>=47r2/192. Also
sup_(0<rho<=1) sqrt(rho)*log(1/rho)=2/e<3/4, because e>8/3.
Thus (4/9)r2*log(1/rho)<=rho^(3/2)/3. Combining with (2) gives

    M_infty(psi,L)-M_infty(0,L)
          <=A*rho^(3/2)-2B*r2
          <=A*rho^(3/2)-B*rho^2,                    (3)

whenever B>0, since r2>=rho^2/2. The origin follows continuously.
This derives the phase inequality at the new degree range; D11's
finite comparison theorem is not used below its own degree floor.

The D16 allowance at psi and at the actual origin, and S_n(0)=Lambda_c,
now give

    S_n(psi)-Lambda_c
       <=A*rho^(3/2)-B*rho^2+K*rho+C+E0.            (4)

For B>0,K>=0 and x>=0, split the negative quadratic in half. Writing
y=sqrt(x), the first maximum is attained at y=3A/(2B); completing
the square gives the second:

    A*x^(3/2)-(B/2)*x^2<=27A^4/(32B^3)=8J0,
    K*x-(B/2)*x^2<=K^2/(2B).

Therefore the entire closed near triangle satisfies

    S_n(psi)-Lambda_c<=C+E0+8J0+K^2/(2B).            (5)

This is a sum of two absolute error allowances, preserving their
phase coefficients until absorption. It is not a finite relative
error theorem, and needs no cancellation with the origin.

### Endpoint and all-n transfer

The sole preregistered N10000 directed receipt has, outward,

    T(10000)>31.58084612999139>22,
    B(10000)>3.08064175722984>0,
    C(10000)<0.021215057412574,
    E0(10000)<0.017200555360308,
    8J0(10000)<0.011944505115745,
    K(10000)^2/(2B(10000))<0.000272256957413,
    1/16-C-E0-8J0-K^2/(2B)>0.011867625153962>11/1000. (6)

The receipt retains all50-digit endpoints. Here
T'(n)=(8log n-3)/(pi^2*n)>0 on n>=10000, so B increases and
stays positive. J0 decreases. C,K,E0 decrease by the separate
analytic allowance proof on all real n>=32; hence K^2/(2B) decreases.
The complete right side of (5) decreases on the unbounded range,
so the strict budget (6) holds for every integer n>=10000.

At a physical noncorner odd center, at least one coordinate is
interior: 0<J<n or0<K<m. C02 applies with the full signed guard and
gives Delta>=max(Q_h,Q_v)>1/16. Subtracting this single floor from
(5) proves (1). The projections are not added. The endpoint centers
are precisely the two actual nonnode corners and are excluded here.

## Evidence, scope and history

Sole author command, trusted arithmetic, frozen code and receipt hashes,
CPU and exact chronology are in ../attempts/D16-phase-budget.md.
No phase/kernel/board/root/quadrature/degree scan or source retuning.
D10's accepted true constant and C08 coefficient retain their original
phase-only scopes; the full D13 finite relative target remains OPEN.
This is a sufficient new onset, with no minimality or priority claim.
Distinct mathematical/source/arithmetic review is required before adoption.
2026-11-06, parent-requested Codex Sol xhigh, rules/input
8040e0b2c9869a7871ad1825e9b9c746186db084; serving metadata unexposed.


### Supplementary review closure — 2026-11-06

Distinct mathematical reconstruction ACCEPTED this unchanged developer
scope; [independent-checks-D16-budget.md](../independent-checks-D16-budget.md),
report SHA25662d9c92d6f6a48734dcff56da2df8048e8fad6ddc8ff79ad3bae057e3672aa6c.
The preceding pending supplementary-review wording is historical. Exact
review scope, process notes and computational provenance remain in that
report. Final Claude audit is separate; executable instance/source release
is not implied by acceptance of a sufficient mathematical contract.
