# PD-T?argmax-bridge-C13-near-comparison — Actual near noncorner comparison at500000

ID kind: PD-T.
Aliases: fixed near-model phase increment;all-center near exclusion.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000 and every real phase pair with
rho=|alpha|+|beta|<=1/2, the corrected odd-board primitive obeys

    S_n(alpha,beta)<Lambda_c(n)+383/12500
                               <Lambda_c(n)+1/32.             (2)

For every physical odd noncorner center, with
0<=J<=n,0<=K<=n+1,J+K odd and at least one interior coordinate,
and every physical representation
theta=(J*pi+alpha)/n,phi=(K*pi+beta)/(n+1) in[0,pi]^2,

    lambda_n(cos theta,cos phi)<Lambda_c(n)-1/32.               (4)

All phases, axes and the closed rho=1/2 boundary are included. S_n and
the full physical defect are normalized exactly as PD-T364. The fixed
near model is N1-15, with R128,delta1/1000,J4096,H8 and its original
finite cutoffs and corrections. Actual corner centers are excluded
from (4), rather than supplied a positive constant defect.

## Status and record boundary

Overall status: **PROVED**, by the written analytic proof. The distinct
[original mathematical reconstruction](../independent-checks-C13-onset.md)
supports the frozen mathematics at n>=500000. Its F1/F2 record repairs
are being submitted for a focused check; that check is **pending**.
This author does not independently approve the repaired batch. Formal
Claude audit remains separate.

All old n>=10^6 theorem statements keep their original quantifiers.
The proof below rechecks the lower-domain component estimates, rather
than applying those old statements below their degree floors. No model,
constant, threshold, correction, scientific computation or assumption
has changed in this split. Exact real arithmetic; natural logarithms.
The exceptional x mode and all finite-polynomial collision, endpoint
and initially zero-cardinal conventions remain unchanged.

## Depends on

[C13-near-representation](C13-near-representation.md), equation(1),
including its lower-domain geometry. C05's endpoint/full finite-h proof,
whose lower-domain steps are rechecked below; C04's phase-only fixed T
bound; N1-16/17's exact coefficients and residual identity; and C02's
[strong all-class defect](C02-defect-dense-band.md), >1/16 on this
domain already for n>=4096. The physical equality lambda=S-Delta uses
the full defect, with Delta>=max(Q_v,Q_h), exactly as PD-T364.

## Routine degree-domain lemma

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

## Representation premise

Use (1) and its origin consequence from
[C13-near-representation](C13-near-representation.md). References below
to(12) mean that file's same explicit eta0<1/1000 bound. All retained
cell geometry used below is proved there at the present degree floor.

## 3. Actual near-model phase increment below one million

We next recheck the C05 finite-h proof. Its endpoint quotient identities
are exact for n>=1024. On the auxiliary phase diamond the small sinc
arguments satisfy

    |(u+/-v)/2|<403/n<=403/500000<1/1000.

This uses |j|<=r-1, r<=128 and pi<22/7, rather than the coarser
4r/n bound to establish that argument range. The shifted linear
denominators still exceed(12/5)k: their unshifted lower is
(pi-1/2)k>(5/2)k and their displacement is <512/n<1/10.

The endpoint sinc-product bounds in C05(9) therefore hold with the
same constants. For explicit checks, r^2/n^2<10^-7; the quotient
Hessian coefficient is bounded by

    1/[2*.99]+1/[4*.99^2]
             +[(16/3)/.99^2+(32/9)/.99^3]*10^-7<1.

The reciprocal-displacement identity and all odd reciprocal sums are
unchanged. The complete endpoint Hessian and remaining beta slope obey

    |E_end,ij|<43988/n+8437761/n^2<45000/n,
    |partial_beta E_end(0,0)|<34/n+22656/n^2<35/n.

Thus C05's endpoint increment is newly established on this domain:

    |E_end(phase)-E_end(0)|<=45000r2/n+40beta/n,
    r2=alpha^2+beta^2.                                      (13)

For the other components, C05's strip/outer singular cancellation is
an exact algebraic identity, including all fixed h_J,g_J constants.
The seam lies below delta+h/2<251/250000. The N1-10 Taylor calculation
on this slightly enlarged interval still gives
`|E_s(z)|<=(7/4)z+(1/9)z|log z|<3/1000` (the same derivation
uses only z<101/100000 and offsets in[1/4,3/4]). Hence its two seam
errors and finite-epsilon terms retain the bounds3/(1000m) and14/n.

The two paired lower q/U terms retain their losses4/n and L/(3n).
The remaining common lower term is bounded by15000L/n^2. Instead
of the old n>900000 rounding, use15000/n<=3/100. The entire lower
boundary allocation is therefore at most

    [18+3/1000+(1/3+3/100)L]/n<5(L+1)/n,                    (14)

already for L>=3. The central missing intervals and collision holes
have the same total measure<=4h and lie above5/2; their proof costs
<10(L+1)/n. The actual special rows plus full H8 discrepancy cost
<50(L+1)/n. The fixed jump expression costs<10(L+1)/n, by its
original exact finite cutoffs and one-summand constants. These proofs
use only m/n<=2, L>3, h<4/n and the cell geometry established above.

Thus the exact C05 decomposition is preserved, with absolute rest
error<75(L+1)/n at each phase. Subtracting at the origin, together
with (13), proves for the actual residual increment F_n

    |F_n-[T(phase)-T(0)]|
       <=45000r2/n+40beta/n+200(L+1)/n.                      (15)

No auxiliary Q_n conversion or extra artifact allowance is used.
Every H8 row, collision hole and retained cutoff is charged once.

## 4. Relax the limiting allowance, keeping the fixed T

C04's phase-only bound, whose T is exactly the same fixed function,
is independent of n:

    T-T(0)<=c alpha^(3/2)+(1225/144)alpha^2
       +(4/9)alpha^2log(1/alpha)+(395/48)beta^2
       +(1/9)beta^2log(1/beta)+10^-9 beta, c=15/32.           (16)

Its use here does not extend C04's n>=1e6 comparison statement.
We recompare (16) with the exact coefficient loss. N1-16's phase-only
coefficient algebra gives, for every L>=131/10,

    G_n>=[47L^2/480+L/240]r2=A(L)r2.

At the lower endpoint,

    A(131/10)-1225/144-32/9>19/4,
    A(131/10)-395/48>8.

If alpha>=exp(-8), the alpha allowance after its coefficient loss is
at most `c alpha^(3/2)-(19/4)alpha^2`, whose elementary maximum is

    27c^4/[256(19/4)^3]<1/20000.

For0<alpha<exp(-8), discard the remaining negative quadratic term
and use C04's same bound `c exp(-12)+(32/9)exp(-16)<10^-5`.
For beta, the entropy maximum with coefficient8 is
`exp(-144)/(18e)<10^-9`, and its fixed slope costs at most10^-9/2.
Axes use continuous zero values. Consequently

    T-T(0)-G_n<1/10000                                  (17)

on the whole closed near triangle.

The exact N1-17 identity, (12), (15) and (17) now imply

    S-Lambda_c<2/1000+1/10000+11270/n+200(L+1)/n
       <=2/1000+1/10000+11270/500000+3000/500000
        =383/12500<1/32.                                  (18)

This proves (2). The accepted C02 dense-band floor is >1/16 for
all physical noncorner odd centers at n>=4096, with every signed
phase and parity. Since lambda=S-Delta and Delta>=max(Q_v,Q_h),
equation (18) gives (4). No defect is asserted at an actual corner.


## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

This theorem excludes all near noncorner centers. Actual corner
patches and the entire far diamond remain separate comparisons. The
original tight C1 tolerance and degree41..499999 are not proved here.

2026-11-06, author response to F1/F2. This file splits its stated scope
from the original combined PD-T?argmax-bridge-C13-onset record, freeze
`6cc04de4d3cc8303c3660043bf15b92e50c527ffd21e10747cdc49de3ec3f070` (483 lines,22065bytes).
The exact local snapshot, source mapping and current file identities
are recorded in the attempt. Original proof paragraphs and equation
numbers are retained where possible, so those numbers refer to the
original reviewed sequence. No final ID or shared crosswalk is assigned
by this worker. Rules read4b728b04216a5490910780bc609a82b853058426;
parent-assigned auxiliary Sol xhigh role, serving metadata unexposed.


## D01 dated record addendum — 2026-11-06 (audit-01 F1/F2)

This addendum preserves every preceding byte and the frozen proof body.
The historical pending focused-review wording above is superseded by
[the accepted focused F1/F2 review](../independent-checks-C13-onset.md#focused-f1f2-repair-review--2026-11-06),
which pins the pre-addendum bytes. That supplementary review is ACCEPTED;
the formal Claude audit remains a separate obligation. The interim
[audit-01](../audit-01.md) supports the stated scope with its explicit
upstream residual limits. No theorem, proof status, constant, parameter,
threshold or quantifier changes here.

For the routine domain bookkeeping, include c=0 and finite sums and
products of positive decreasing factors. More explicitly, for a polynomial
P(L) with nonnegative coefficients of degree at most two, P(log n)/n^j
is decreasing here (unless identically zero): L P'(L)<=2P(L) and
jL>2. Factors (1+1/n)^q, q>=0, also decrease. Thus this covers
(L+2)^2/n, (L+2)/(2n^2), m^2/n^3=(1+1/n)^2/n and the
m H2/n^j terms actually used (j>=2), writing
H2=1+log(2m); its logarithmic derivative is at most 1/H2, while
m/n^j has logarithmic derivative at most 1-j. The pure inverse powers
and (2/63)(1+1/n) decrease as well. L(delta+h/2)/(6m) is a sum of
positive multiples of L/m and L/m^2, both decreasing at n>=n0.
For the stated near G(x), differentiation gives
G'(x)=x[7/4+log(1/x)/9]>0 on its small positive argument range;
x=delta+h decreases, so G(delta+h) decreases. Fixed tails stay fixed.
These are the already-used termwise monotonicity facts reconstructed in
audit-01, rather than an extension of any upstream theorem domain.

The lower logarithm citation in (6) is unchanged. The upper citation is
[N1-16, scalar k check](N1-round7-coefficients.md): its positive
exponential series through degree 10 proves log 10<2303/1000.
Consequently log n0=6 log 10-log 2<6(2303/1000)<14, since log 2>0.
The earlier attribution of this upper bound to lower log 10 and upper
log 2 bounds is superseded by this citation. L<14 is used only at n0.

Equation (16) is exactly [C04-near-limit-comparison (3)](C04-near-limit-comparison.md),
a bound on the fixed phase function. The 11270 in (15)/(18) is
45000(1/4)+40(1/2), from [C05-finiteh-model-comparison (1)](C05-finiteh-model-comparison.md)
and r2<=1/4, beta<=1/2. Its old n>900000 rounding is C05-model
(11); the lower-domain treatment is recorded in near-representation.
