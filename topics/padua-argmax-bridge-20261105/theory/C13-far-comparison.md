# PD-T?argmax-bridge-C13-far-comparison — Actual far comparison at500000

ID kind: PD-T.
Aliases: full closed far deficit;retained d(n) comparison.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000 and every real phase pair with
1/2<=rho=|alpha|+|beta|<=pi, the corrected primitive satisfies

    S_n(alpha,beta)<Lambda_c(n)-1/2000.                         (3)

The stronger explicit gap(26) is proved below. The entire closed far
diamond, including a=0, vertices, polynomial collisions and both
parities, is covered. The same fixed R64,delta1/100 far model is
used as an intermediate comparison; no model term or correction changes.

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

[C13-far-representation](C13-far-representation.md), equation(24),
and [C13-corner-value-lower](C13-corner-value-lower.md), equation(22).
C08's weighted-coefficient, endpoint-constant, pole-functional and
renormalized-integral theorems supply the unchanged phase-only bounds
for b_full and C_far on the full closed diamond. N1-16 gives k>3/2.
The numbered references(22),(24) below refer to these linked inputs,
not to added local estimates.

## Routine degree-domain lemma

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

## 8. Close the far comparison

C08's weighted coefficient and degree-independent constant bounds hold
on the full closed phase triangle, without an n floor:

    b_full-b_c<=3(1-a)/pi^2,
    C_far<49/25+1/3000+49/50=8821/3000,
    (2k/pi)^2>9/10.

These are the same fixed R64 endpoint and integral functions.
On the far domain, `u=1-a>=191/6144`. Using pi^2<10 and (22),

    Lambda_c-M_far>
       u(4L^2-3L)/10+9/10+d(n)-1/1000-8821/3000.            (25)

The right side increases with L and n on this domain. At L=131/10
and n=n0 it equals283876469737/512001024000. Subtract (24):

    Lambda_c-S>
       382900852945861/466667600000000000>1/2000.             (26)

This proves (3), including a=0, phase vertices and both parities.
The saving over an immediately rounded1/2 corner margin is essential
for this particular scalar allocation; no theorem is refuted by the
failure of that weaker allocation.

QED.

## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

Near phases, other physical-center defects and actual corner
patches are separate. This primitive statement alone does not locate
all global maximizers; the complete assembly has its own record.

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

The phase-only argument for the inline floor is:
write alpha,beta for their absolute phases. On the closed far triangle,
a=cos((alpha+beta)/2)cos((alpha-beta)/2)<=cos(1/4).
Thus u>=1-cos(1/4)>=1/32-1/6144=191/6144 by the alternating
cosine series. This is [C08-far-model-comparison (6)](C08-far-model-comparison.md)'s
phase-only calculation and has no degree floor. Also (2k/pi)^2>9/10
uses k>3/2 from [N1-16](N1-round7-coefficients.md) and pi^2<10;
it is not an additional C08 premise.
