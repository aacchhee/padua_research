# PD-T?argmax-bridge-C13-corner-value-lower — Finite corner-value lower at500000

ID kind: PD-T.
Aliases: retained finite deformation;explicit same-mesh baseline.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000, put m=n+1,L=log n,
k=gamma+log(8/pi), A_n=(2/pi)(L+k), and use exactly PD-T159's
actual corner value Lambda_c(n) and same-mesh one-dimensional L_n.
Then, with d(n)=((16/25)n-28000)/(n+1),

    Lambda_c(n)>A_n^2+d(n)-1/1000.                           (22)

The proof retains the exact baseline B_n=n L_n^2/(n+1)+1/(n+1)
and Lambda_c=B_n+Delta_corner. In particular d(n)>0 on this domain,
so the weaker Lambda_c>=A_n^2-1/1000 bound is a routine consequence.
Delta_corner is the signed same-mesh deformation, not PD-T364's
physical four-copy triangle defect. No global argmax is assumed.

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

PD-T159's exact finite corner/same-mesh identities; C07's finite
nonnegative unordered-pair proof; PD-T270's all-degree L_n error;
N1-16's scalar k>3/2; and PD-T269's explicitly quantified central
approximation and positive cotangent expansion. The retained strip
argument has n>=40 as its actual domain; all n>=500000 uses below
are rechecked from those estimates. No old n>=1e6 bound is extended
as an unverified premise.

## Routine degree-domain lemma

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

## Routine baseline before the retained deformation

C07's finite same-mesh deformation proof is valid for every n>=2.
With k=gamma+log(8/pi)>3/2 and A_n=(2/pi)(L+k), define the exact
same-mesh baseline and its signed finite deformation by

    B_n=n L_n^2/(n+1)+1/(n+1),
    Lambda_c=B_n+Delta_corner(n).

PD-T159/C07 give this identity. PD-T270's bound on L_n and the
same-mesh square calculation give, on n>=n0,

    B_n>=A_n^2-epsilon(n),
    epsilon(n)=(L+2)^2/n+(L+2)/(2n^2)<1/1000.                (19)

Both error functions decrease; their upper at n0 with L<14 is
256/500000+8/500000^2<1/1000.

## 6. Retain the actual finite positive corner margin

C08's retained adjacent-pair proof has the actual domain condition
n>=40 in its PD-T269 approximation. Its finite positive pairing is
valid for every n>=2, and its exact retained-strip calculation gives

    Delta_corner(n)>d(n), d(n)=((16/25)n-28000)/(n+1).        (21)

This is the signed same-mesh deformation, not the physical triangle
defect in (3)--(4). It is obtained by retaining unordered adjacent
pairs, paying4600/n per pair and2400/n for its full strip mesh error,
then using `4 integral h>16/25`. Discarded unordered pairs are
nonnegative. No finite data or new margin fit is used.

Add (21) to the baseline inequality B_n>=A_n^2-epsilon(n)
from(19), using Lambda_c=B_n+Delta_corner(n) and epsilon(n)<1/1000.
This gives

    Lambda_c>A_n^2+d(n)-1/1000.                              (22)

The function d(n) increases; its derivative has numerator28000+16/25.
It is therefore useful to retain it, rather than round it to1/2.
The n0 value is292000/500001. The original C08 margin theorem is
unchanged; (21)--(22) are this proof's explicit lower-domain extraction.


## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

This is a corner-value lower bound. It does not locate global
maximizers. The weaker baseline used by the actual-corner comparison
is routine inside this stronger theorem; no eighth supporting record
or independent additional deformation is introduced. F2 is addressed
by writing B_n and Lambda_c=B_n+Delta_corner before adding(21).

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

The baseline (19) uses [PD-T270](../../padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md)'s bound
|L_n-A_n|<=1/(4n^2), together with L_n>=A_n-1/(4n^2)>0
and A_n<=L+2, as reconstructed in audit-01/corner-review.md.
The nonnegativity Delta_corner>=0 is the finite unordered-pair
argument of [C07-positive-deformation](C07-corner-positive-deformation.md),
valid for n>=2. It is what permits passing from B_n's baseline to
Lambda_c>=A_n^2-epsilon in the corner comparison; no deformation is
added twice. The retained d(n) argument and its floor remain unchanged.
