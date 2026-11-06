# PD-N?argmax-bridge-codex-N5-01 — Obstruction to the phase-blind full-band quarter certificate

ID kind: PD-N.
Aliases: N5 round5 budget; N5-05 certificate obstruction; full vertical
sign-band envelope; quarter-unit budget escape.
Split from: none; scoped failure of IDEA?argmax-bridge-codex-N5-05's
single analytic certificate, leaving its original target OPEN.
Split into: none.

## Precise result and scope

**PROVED analytic developer obstruction**, subject to distinct review.
The single full-band lower certificate preregistered in
../ideas/N5-round5-budget.md cannot establish its proposed uniform
quarter floor. This is an obstruction to that certificate, not a
counterexample to the full projected-defect target (C5).

Put a0=15/16, c=11/15 and define ell and F_n below. Along the admissible
subsequence

    n=4t+1>=65, m=n+1, J=0, q=m/2, alpha=beta=0,       (1)

F_n has a limit and

    lim F_n < B=487302379/1968469140 < 1/4.            (2)

Consequently F_n<1/4 for all sufficiently large n in (1). The exact
threshold is neither needed nor supplied. Every finite Q_v diagnostic
in this round exceeds 1/4. The original all-degree/all-phase claim
Q_v>=1/4 remains **OPEN**. Neither (2) nor a small lower certificate
implies a small Q_v or actual defect S-lambda.

## Definitions and dependencies

Use the N5-04 domain: n>=64, m=n+1, N=nm, J in {0,n},
1<=q<=m-1, J+q odd, rho=|alpha|+|beta|<=1/2, and inward physical
theta=(J*pi+alpha)/n in [0,pi]. Put phi=(q*pi+beta)/m,
u_r=(r*pi+alpha)/n, b_k=k*pi/m, and f_k=1 except f_0=f_m=1/2.
The canonical full projection, including finite polynomial collision
values, is

    Gamma={(r,s):0<=r<2n,0<=s<2m,r+s odd},
    P_n=T_(n+1)+T_n,
    G_rs=D_n(cos u_r,cos v_s)-cos(n*u_r),
    v_s=(s*pi+beta)/m,
    D_n(x,y)=[P_n(x)-P_n(y)]/(x-y), polynomially at x=y,
    d(x,y)=|x|+|y|-|x+y|,
    Q_v=(1/(4N))*sum_Gamma d(G_rs,G_(r,2q-s)),         (3)

where the reflected second index is modulo 2m and beta is unchanged.
The equivalent folded form from T222/T366 and N5-04 is

    H_+=[(-1)^r D_n(cos u_r,cos(phi+b_k))-cos alpha]/2,
    H_-=[(-1)^r D_n(cos u_r,cos(phi-b_k))-cos alpha]/2,
    Q_v=(1/N)*sum_(k=0)^m f_k
             sum_(0<=r<2n,r+k=J mod2) d(H_+,H_-).      (4)

The exceptional term is cos(alpha), not 1. At regular denominators,
with x=cos u and y=cos v,

    H(u,v)=A(u,v)/(x-y),
    A=a*(1+y)-(sin alpha/2)*sin u+(sin beta/2)*sin v,
    a=(cos alpha+cos beta)/2>=a0,
    (|sin alpha|+|sin beta|)/2<=1/4.                  (5)

These identities and bounds are proved in N5-04, equations (3)-(5).
The actual deficit satisfies Delta=S-lambda>=Q_v. Its equality with
Q_v is not assumed.

For y_+=cos(phi+b), y_-=cos(phi-b) and 0<b<pi, the interior phi
ensures y_+<y_-. Define the preregistered phase-blind envelope

    ell(u,b)=2*a0*min((c+y_+)/(x-y_+),
                       (c+y_-)/(y_--x))              (6)

when y_+<x<y_- and c+y_+>0. Set ell=0 otherwise, including all
collisions and b=0,pi. Define

    F_n=(1/N)*sum_(k=0)^m f_k
                 sum_(0<=r<2n,r+k=J mod2) ell(u_r,b_k). (7)

Indeed (5) gives A>=a0*(1+y)-1/4=a0*(c+y), since 1-1/(4a0)=c.
On (6)'s support both numerators are positive, the denominators
have opposite signs, and d(H_+,H_-)=2*min(|H_+|,|H_-|)>=ell.
Off that support d>=0. Thus F_n<=Q_v on the entire target domain.
This proof does not replace the finite polynomial values of (3).

This is a quantitative continuation of T222/T366/N5-04's mechanism,
with a deliberately stronger proposed floor, not a new mechanism.
T366's rho<=1/10 floor and N5-04's 1/2048 floor do not settle the
quarter target. PD-T266's limiting vertical minimum concerns a
different limiting function and supplies no finite n64 rate here.
IDEA318/330/459 do not provide the missing quarter inequality.

## Status by part and negative-result scope

Overall status: **PROVED**, for the negative mathematical statement (2).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The specified F_n certificate fails a uniform quarter floor | PROVED | (1)-(2), parity lattice and exact integral upper bound below |
| F_n<=Q_v | PROVED routine supporting inequality | (5)-(7); not a part of the quarter target |
| Original (C5), Q_v>=1/4 on the unchanged N5-04 domain | OPEN external target | Retained verbatim in the idea record; neither implied nor refuted here |
| Finite direct full-Q diagnostics | MEASURED checks | 72 cases and numerical controls in the receipt |

Attempted mechanism: the exact full sum (7) of the phase-blind separate
worst-numerator envelope (6), preregistered under
IDEA?argmax-bridge-codex-N5-05 before evaluating the certificate.
Parameter range of the failure: the central admissible subsequence
(1), already within the proposed n>=64 domain; no phase or n scan is
used to infer a universal failure of Q_v.
Mechanism disposition: **REJECTED: failed**, because F_n cannot have
the proposed uniform quarter floor. The original C5 theorem is not
rejected; its candidate is deferred after the single authorized attempt.

## Depends on and sources

Load-bearing local dependency: N5-04's exact (3)-(5) identities and
uniform a>=15/16, perturbation<=1/4 on its unchanged domain, proved
in ../theory/N5-two-phase-defect.md. T222/T366 are predecessors for
the projection. No measured value or external literature statement is
a proof premise. The elementary entropy, atanh and arctangent formulas
used below are justified directly; no fresh external source is cited.

## Proof of the scoped obstruction

### 1. Exact central envelope and its integral

In (1), q=2t+1 is odd, phi=pi/2, and r+k is even. For
s=sin b, we have y_+=-s and y_-=s. If 0<s<c and |x|<s,

    ell=2*a0*min((c-s)/(x+s),(c+s)/(s-x));            (8)

otherwise ell=0. The two fractions meet at x_*=-s^2/c and
their minimum is at most c/s. Integrating first the increasing
right fraction on (-s,x_*) and then the decreasing left fraction
on (x_*,s) gives

    integral_(-s)^s ell dx = 2*a0*f(s),
    f(s)=(c+s)*log(2c/(c+s))
                   +(c-s)*log(2c/(c-s)).             (9)

The endpoint convention is f(c)=0. The nonnegative f is the sum
of these two exact nonnegative integrals divided by 2a0.

### 2. The parity lattice has this improper-integral limit

For any fixed eta>0, restrict eta<=b<=pi-eta. The envelope is
bounded there. Its discontinuities lie on finitely many smooth arcs
x=+/-sin b and sin b=c (with the endpoint conventions). Thus it
is Riemann integrable on that compact rectangle. The even-even and
odd-odd r,k grids each have spacings 2pi/n and 2pi/m. Their separate
normalized limits have density 1/(4pi^2), so together their density
is 1/(2pi^2) on 0<=u<2pi, 0<=b<=pi.

The omitted endpoint tails are uniformly controlled. For
0<b<=eta<=pi/2, (8) is supported on two u intervals, each of
length 2b. A parity grid of spacing 2pi/n has at most
2nb/pi+2 points in their union. Since sin b>=2b/pi,

    ell<=2*a0*c/sin b<=a0*c*pi/b.

For K=floor(m*eta/pi), summing k=1,...,K and dividing by N bounds
one tail by

    2*a0*c*K/m+(2*a0*c/n)*H_K
      <=2*a0*c*eta/pi+(2*a0*c/n)*(1+log m).          (10)

When K=0 the tail is empty. The identical bound applies at pi;
the endpoint rows themselves vanish. This tends to zero by first
letting n tend to infinity along (1), then eta tend to zero. The
corresponding integral tails satisfy the same bound without the
harmonic error. Compact Riemann convergence and (10) prove

    F_n -> F_inf=(1/(2pi^2))*integral_0^pi integral_0^(2pi)
                            ell(u,b) du db
                =(1/pi^2)*integral_0^pi integral_0^pi
                            ell(u,b) du db.          (11)

No unproved convergence rate or interchange of unbounded tails is
used. In particular the parity-dependent lattice is retained.

### 3. An explicit integral upper bound below a quarter

In the integral over 0<u<pi substitute x=cos u. On |x|<s<c,

    1/sqrt(1-x^2)<=1/sqrt(1-s^2).

Using (9), b <-> pi-b symmetry, and then s=sin b on
0<b<arcsin c in (11), we obtain

    F_inf <= (4*a0/pi^2)*I,
    I=integral_0^c f(s)/(1-s^2) ds.                 (12)

For 0<=z<=1 the entropy series, continuous at z=1, is

    (1+z)log(1+z)+(1-z)log(1-z)
       =sum_(j>=1) z^(2j)/[j*(2j-1)]
       >=z^2+z^4/6.

Applying it to z=s/c in (9) yields

    f(s)<=2c*log2-s^2/c-s^4/(6c^3).

With T=atanh c, integrate this elementary rational envelope:

    I <= [2c*log2-1/c-1/(6c^3)]*T
                       +1+1/(6c^2)+1/18.           (13)

For completeness the rational bounds used next are elementary.
Writing z=1/3, the positive atanh series gives

    log2=2*atanh z
       <2*(z+z^3/3+z^5/5)+2*z^7/[7*(1-z^2)]
       =23581/34020 <347/500.

Likewise T>sum_(j=0)^4 c^(2j+1)/(2j+1)>93/100. Finally,
Machin's identity pi=16*atan(1/5)-4*atan(1/239) and the
alternating arctangent bounds give

    pi>16*(1/5-1/(3*5^3))-4/239 >157/50.

Machin's identity follows by the tangent addition formula with its
angles in the first quadrant. The coefficient with log2 replaced
by its upper bound is negative:

    C=2c*(347/500)-1/c-1/(6c^3)=-1917599/2495625<0.

Since T>93/100, (12)-(13) imply

    F_inf < [4*a0/(157/50)^2]
                 *[C*(93/100)+1+1/(6c^2)+1/18]
           =487302379/1968469140 <1/4.              (14)

The bracket is positive, as its displayed rational value confirms;
therefore replacing pi by its positive lower bound preserves the
upper estimate. Equations (11) and (14) prove (2).

## Measurements, remaining obligation and stop

The complete (3) was computed directly by the new
../code/n5_large_budget.py, without using S-lambda as a proxy. The
72 preregistered cases n64/65, both J, nearest parity-valid endpoint
and middle q, and the six axis/mixed phases all pass. The minimum
is 0.5230485747479166311 at n65,J65,q32,alpha0,beta=-1/2.
These are floating MEASURED values, with separate binary64 and
80-digit scalar polynomial-recurrence diagnostics; they are not
outward bounds. The small receipt ../evidence/n5-large-budget.json
pins source, environment, scope and off-Git raw output. Its exact
rational checks reproduce (14)'s arithmetic, not the analytic proof.

One scratch 50-digit quadrature of (12)'s comparison integral gave
0.23781962720376754123. This is only a measured diagnostic, is not
the actual F_inf, and is not a premise of (14).

The remaining obligation is still precisely (C5): the full (3) must
be bounded below by 1/4 uniformly on the unchanged domain. The
separate worst numerator losses in (5)-(6) cannot provide that bound
even after exact full-band summation. Any later solution would need
an additional argument beyond this frozen certificate; no such
successor is attempted here. No negation of an actual-lambda quarter
margin, effective full-square onset, primitive maximum, or PD-T099
result is asserted. This authorized round stops with a scoped proved
obstruction and the original target open.

## Checks and history

Executed from the repository root, input/rules
fc8c2885f47b08cecc7f65328db0e740cbc205ea:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n5_large_budget.py --output local-output/argmax-bridge-20261105/N5/large-budget-cases.json --receipt topics/padua-argmax-bridge-20261105/evidence/n5-large-budget.json
```

First direct run: 72 cases, 0.476517077 CPU seconds. After adding only
the exact rational arithmetic check for (14), the bounded replay of
the same 72 cases used 0.448897379 CPU seconds; identical raw bytes.
Python3.12.14, numpy2.3.5, mpmath1.3.0, longdouble64 significand
bits, scalar control at80 decimal digits, no seed. Source and bulk
identities are pinned in the receipt. First source/receipt/raw bytes
are retained locally; provenance and aggregate limits are recorded
once in attempts/N5.md. Independent replay and mathematical review
are separate, not claimed here. No unexecuted experiment is needed
for the analytic (2); the open C5 would require a further argument.

2026-11-06: parent authorized one bounded round5 after published
N5-04 and its distinct review. Codex developer, model/effort inherited
from the parent allocation; serving metadata unexposed. The prospective
gate, exact C5, correction and finite test came first; the sole envelope
was added to the idea record before its analytic evaluation. The
subsequent negative statement concerns that envelope alone. All
round4 files and reports remain unchanged. No new round is authorized.
