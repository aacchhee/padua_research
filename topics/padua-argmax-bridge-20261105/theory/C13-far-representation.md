# PD-T?argmax-bridge-C13-far-representation — Unrounded full-phase representation error at500000

ID kind: PD-T.
Aliases: fixed far-model error;component budget before9-over25 rounding.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000, put m=n+1,L=log n and use
exactly C06's [fixed far model](C06-far-compact-error.md), with
R64,delta1/100, exact infinite h/g constants, finite sinc endpoint
profiles and the original joint integral. On every real signed phase
pair |alpha|+|beta|<=pi,

    |S_n(alpha,beta)-M_far(alpha,beta;log n)|<E_far(n),

where E_far is the explicit component sum(23) below. Uniformly,

    E_far(n)<290652925961/525000000000.                       (24)

This includes axes, vertices,a=0, every polynomial collision and both
parities. The old9/25 tolerance is not claimed at500000; no model
term or fixed parameter changes. Exact corrected-kernel normalization
is that of PD-T364 and C06.

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

N1-06/07/08's corrected full-phase endpoint mesh/finite-row/collision
proofs; N1-02/04/05's ordinary-row approximation and endpoint residual;
and C06's compact-error proof, including its complete phase-only
variation, central-log and missing-cell estimates. Their unrounded
component formulas are used below after checking their actual lower
degree conditions. The model's finite polynomial and full closed-domain
conventions are unchanged.

## Routine degree-domain lemma

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

## 7. Unrounded far representation error

The C06 compact-error proof uses the same full-phase model at R64,
delta1/100. Its endpoint component inputs N1-06/07/08 apply already
for n>=ceil(12800pi), well below n0. Its interior variation bounds
are phase-only, and the expanded cells require only
`delta-h/2>delta/2`, also satisfied. First/last64 rows remain inside
the endpoint strips; central and collision rows retain their exact
finite-polynomial treatment. Thus its complete error decomposition,
with a single shared ordinary-row error charge, is valid here.

Define these positive bounds at any n>=n0:

    e_rows=(763L+86237)/n+7082790000/n^2,
    e_mesh=[(449/2)L+1762]/n
                         +[(101124/8)(L+13)+1/2]/n^2,
    e_collision=(62+8L)/(3n)+6/n^2,
    e_interior=(3002L+32803)/n,
    E=4(L+1)/n+(2/63)(1+1/n),
    D=[10+(20/3)(L+1)]/n^2,
    E_far=e_rows+e_mesh+e_collision+e_interior+E+D+7/50.       (23)

The first line is N1-07's exact R64 row bound with H_n<=L+1.
For e_mesh use N1-06's explicit C_X formula, H_R^*<5,
`1/(X-1/2)<318/m`, and `log(X+1/2)<L+1`.
The first reciprocal inequality needs only m>5050pi.
Replacing m by n upwards gives precisely the second line.
N1-08's collision formula, pi>3 and log(4m/R)<L+1 give the
third line, including both small polynomial collision allowances.

The fourth line is C06's unrounded ordinary-interior budget:300L+6000
for BV cells,1500L+20000 for missing cells/boundaries,1200L+6800 for
actual special rows and2L+3 for the integrable central log. Collision
shares of D are disjoint and charged just once. The last three lines
are its ordinary-row cancellation, single-pole approximation and the
same phase-uniform endpoint residual Q<7/50.

It follows that `|S-M_far|<E_far`. Each variable term in (23)
decreases. At n0 with L replaced by14, their exact rational sum is

    E_far<290652925961/525000000000.                          (24)

This replaces the old rounded9/25 error; that old tolerance is not
claimed at n0. No full-phase collision or endpoint term is dropped.


## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

This is a representation error, not a maximum comparison. The
separate [far comparison](C13-far-comparison.md) combines it with the
retained corner lower and existing phase-only model bounds.

2026-11-06, author response to F1/F2. This file splits its stated scope
from the original combined PD-T?argmax-bridge-C13-onset record, freeze
`6cc04de4d3cc8303c3660043bf15b92e50c527ffd21e10747cdc49de3ec3f070` (483 lines,22065bytes).
The exact local snapshot, source mapping and current file identities
are recorded in the attempt. Original proof paragraphs and equation
numbers are retained where possible, so those numbers refer to the
original reviewed sequence. No final ID or shared crosswalk is assigned
by this worker. Rules read4b728b04216a5490910780bc609a82b853058426;
parent-assigned auxiliary Sol xhigh role, serving metadata unexposed.
