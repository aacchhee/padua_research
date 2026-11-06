# PD-T?argmax-bridge-C13-corner-comparison — Actual-corner comparison at500000

ID kind: PD-T.
Aliases: half-diamond actual descent;r2-over-six loss.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000 and inward A,B>=0,A+B<=1/2, put
r2=A^2+B^2,a=(cos A+cos B)/2. At either parity-correct actual
nonnode corner,

    lambda_n<=a Lambda_c+[log(n+1)/3+16]r2,                   (20)
    lambda_n<=Lambda_c-r2/6.                                  (5)

At(-1,-1) the physical point is(-cos(A/n),-cos(B/(n+1))).
For even n the second patch is its x reflection; for odd n it is
its y reflection. The origin is included, with equality there. Every
positive inward phase is strictly below the corner value. All corrected
polynomial, endpoint and initially zero-cardinal conventions are those
of C02/C07. This is a direct actual-function result without energy or
a global-norm equality assumption.

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

[C13-corner-value-lower](C13-corner-value-lower.md), including its
routine baseline(19). C02's exact four-copy cardinal normalization;
C05's quarter-angle identities and regular series; and C07's enlarged
collision strip, exact Fourier moments and finite-polynomial bounds.
The degree-sensitive constants are rechecked below, with the original
phase split, thresholds and parity convention retained.

## Routine degree-domain lemma

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

## 5. Recheck the actual-corner patch

The corner-value theorem's routine baseline(19) gives
Lambda_c>=A_n^2-epsilon(n), with
epsilon(n)=(L+2)^2/n+(L+2)/(2n^2)<1/1000. Its stronger retained
deformation is not needed for this comparison.

The C07 actual-corner derivative argument also retains its constants
below1e6. Here are every numerical floor checks used in that argument:

* tau=m/n<=1001/1000, tau^3<101/100;
* `1/3-1/n>=(999/1000)/3` in the regular negative-one strip;
* its j<=100 comparisons follow from
  `(1-120/n)^(-2)<101/100` at n>=n0;
* the C05 harmless normalized f terms, bounded by its displayed
  rational expression, are <1/100 at n0 even with H2=1+log(2m)<16;
  the sine P-part is at most108tau*16/(25n)<1/100;
* `3n/2+7/4<=(151/100)n` and
  `3n^2/2+7n/2+23/8<=(151/100)n^2` bound the finite V derivatives;
* its polynomial F Hessian `(71/80)n+1/2<=(9/10)n` and final
  enlarged-strip count `14/5+28/(5n)<3` hold on this domain.

The decreasing logarithmic ratios in the harmless terms are checked
at n0; all other inequalities improve with n. The exact Fourier
moments, quarter-angle identity, baseline F0<=n, reflected-copy
normalization, regular discrete series and collision-strip geometry
are unchanged algebraic statements. Thus their same complete budget
is newly established for n>=n0:

    lambda_n<=a Lambda_c+[log m/3+16](A^2+B^2).                (20)

No sign of a perturbed cardinal is assumed. Initially zero cardinals,
the finite endpoint and every moved strip index stay in the orbit sum.

Using1-a>=47(A^2+B^2)/192, (19), pi^2<10 and log m<=L+1,
the strict coefficient left by (20) is at least

    p(L)=(47/192)[(2/5)(L+3/2)^2-1/1000]-(L+1)/3-16.

This polynomial increases for L>=131/10, and

    p(131/10)=10987/64000>1/6.

This proves (5), at both parity-correct actual corners. In particular
arbitrarily small positive phases remain strictly below Lambda_c.


## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

This result applies only to the two actual inward corner patches.
Near noncorner and far phase comparisons remain separately owned
results; no global localization is assumed in this proof.

2026-11-06, author response to F1/F2. This file splits its stated scope
from the original combined PD-T?argmax-bridge-C13-onset record, freeze
`6cc04de4d3cc8303c3660043bf15b92e50c527ffd21e10747cdc49de3ec3f070` (483 lines,22065bytes).
The exact local snapshot, source mapping and current file identities
are recorded in the attempt. Original proof paragraphs and equation
numbers are retained where possible, so those numbers refer to the
original reviewed sequence. No final ID or shared crosswalk is assigned
by this worker. Rules read4b728b04216a5490910780bc609a82b853058426;
parent-assigned auxiliary Sol xhigh role, serving metadata unexposed.
