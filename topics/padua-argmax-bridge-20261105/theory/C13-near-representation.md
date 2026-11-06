# PD-T?argmax-bridge-C13-near-representation — Near representation error below one million

ID kind: PD-T.
Aliases: unchanged-model near error;C13 representation at500000.
Split from: the original combined PD-T?argmax-bridge-C13-onset proof.
Split into: none; this file owns only the stated substantive comparison.

## Statement and definitions

For every integer n>=500000, put m=n+1,L=log n and
rho=|alpha|+|beta|. On the full closed signed domain rho<=1/2,

    |S_n(alpha,beta)-M_near(|alpha|,|beta|,log n)|<1/1000.      (1)

S_n is exactly PD-T364's corrected odd-board primitive. M_near is
exactly [N1-15](N1-round6-near-model.md), with R128,delta1/1000,J4096,
the original truncated h/g and jump constants, H8, actual row/collision
sets and finite cutoffs. The origin is included and S_n(0,0)=Lambda_c.
No model term or parameter is replaced.

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

N1-06/09/10/11/12/13/14/15 and the corrected finite kernel: the
exact retained rows/cells, coefficient normalization, shifted-series
identities, endpoint/jump errors, phase-only regular/central variation
and H8 tails. Every changed degree condition is checked below. The
original C13 source reading and fresh NN-MOP registry gate remain in
[the idea record](../ideas/C13-onset.md).

## 1. Actual degree constraints

Put n0=500000. The elementary bounds log10>23/10 and log2<7/10,
proved in N1-16/C08 by positive log/exponential series, give

    log n0=6log10-log2>131/10, log n0<14.                     (6)

Every function `(c log n+d)/n^j` used below, with c,d>0 and j>=1,
decreases on n>=n0: its derivative has the sign of
`c-j(c log n+d)<0`. Bounds by a value at n0 therefore use L<14 only
at n0; no assertion L<14 at every larger n is made.

Here are the principal constraints from the underlying proofs.

| Component | Actual sufficient condition / changed bookkeeping |
|---|---|
| Near exact finite endpoint rows | n>=8R=1024; all are inside z<delta once m>128000pi |
| Both retained near strips have K_s>=R | X=delta*m/pi>=R+1=129 suffices for both t_s in[0,1]; n>=405429 is a simple sufficient integer condition using pi<22/7 |
| Near shifted-series tails | K_s>=R is enough for the exact finite-sum identities; J4096 need not be below K_s |
| Near outer cells | their lower endpoint exceeds delta-pi/(2m); on the present domain it exceeds ell0=249/250000 |
| Near tail rounding b>317 | replaced by b>158 and its explicit larger tail allowance below |
| C05 rounding15000/n<1/60 | fails below900000; retain15000/n<=3/100 instead, which still fits its final rest budget |
| Fixed h/g4096 and H8 | the same tails remain; their coefficients are charged below, without changing a truncation |
| Far H4 domain | n>=ceil(12800pi), hence the sufficient integer floor40229, plus n>=8R=512 |
| C07 regular/finite-strip constants | the explicit inequalities checked in C13-corner-comparison.md require only much smaller floors than n0 |

The near strip scale is therefore roughly pi*R/delta, not an intrinsic
one-million restriction. The published N1-06 condition X>=2R is a
sufficient convenience. Its centered-cell identities require K>=R;
the near proof below uses those identities directly under X>=129,
and does not reuse the broader published domain conclusion.

At n>=n0, m/n<=1001/1000, h=pi/m<4/n, X>159 and
`delta-h/2>249/250000`. The first/last128 near rows have
z<=128pi/m<delta. The additional central/collision rows remain near
pi and disjoint from those endpoint rows. Both parity conventions and
actual cutoffs are unchanged.

## 2. A re-extracted near representation error

All quantities here are uniform on the closed signed half diamond.
Write tau0=1001/1000 and ell0=249/250000. N1-09's exact correction
and its error E5 are valid for n>=1024. Its ordinary-row and single-pole
errors, with P=sin alpha+sin beta<=1/2, are bounded by

    r_n<1/n^2,
    E5<=tau0^2/(4*127^2)+tau0/(508n)+(L+1)/(2n)+4/n,
    D_n<=[10+(20/3)(L+1)]/n^2.                               (7)

For r_n use its displayed formula, pi<4 and H_n<=n. For the second
term of E5 use pi<4 and m/n<=tau0. These are bounds for the actual
corrected rows, not N1-07's old asymptotic endpoint-row errors.

For the existing N1-10 strip approximation, b_s>=X-1/2>158.
The function `(6+(log x)/2)/x^2` decreases for x>=158, and log158<6.
Its two shifted harmonic/log tails therefore cost at most
`9/(4*158^2)`. The original exact J4096 truncation costs <10^-6,
because its coefficient Z_n is bounded by5 independently of L.
The discrete endpoint residual also still costs <10^-6: in N1-10's
notation delta+h<126/125000, and

    (2/pi)G(delta+h)
       <(101/108)(126/125000)^2<10^-6.

Here `G(x)=x^2[7/4+(log(1/x)+1/2)/9]/2`; log(1/x)<9 on the
required last cells, and the negative G(Rh) can be dropped. The regular
A-strip and logarithm quadratures satisfy, respectively,

    L*(delta+h/2)/(6m)<10^-8,
    q/[4pi*m*(R-1/2)]<=1/(3060n)<10^-9.

These follow from (6), h<4/n and monotonicity. Thus the full unchanged
strip error is below

    e_strip=9/(4*158^2)+2*10^-6+10^-8+10^-9.                  (8)

The exact N1-11 jump proof uses only n>=1024, m/n<=2 and its actual
half-cell cutoffs. Its unchanged error is bounded by

    e_jump=3/n^2+1/(27*128^3)+1/(16n*128^2).                  (9)

No endpoint branch or extra jump constant is inserted.

For N1-15's outer replacement, keep its actual ordinary cell unions.
The singular term has error at most `(L+8)/(n^2 ell0^2)`;
the regular BV terms have error at most `[(6/5)L+23]/(2n)`.
On endpoint I cells the same formula remains valid up to8/5, and
log(2/ell0)<8. The integral of the second-derivative majorant is
at most `147/ell0^2+4/ell0`. The central residual variation and
central log costs are at most5/(2n) and1/(12n). Consequently

    e_outer <=(L+8)/(n^2 ell0^2)+[(6/5)L+23]/(2n)
                 +[147/ell0^2+4/ell0]/(8n^2)+5/(2n)+1/(12n).
                                                                    (10)

The cell-index argument is unchanged: central rows are already special,
there are at most two extra collision holes, all ordinary cells have
distance at least h/2 from pi, and their lower endpoints exceed ell0.
The variation bounds in N1-13/14 are phase-only. Their integrable central
logarithms and endpoint formulas therefore apply to these actual cells;
there is no assumption that an old n>=1e6 quadrature tolerance survives.

The at most four H8 special rows cost at most

    e_special=32/(225n),                                    (11)

by the same per-tail bound1/450, twelve-block count and original
coefficients. Exact collisions stay polynomial and duplicate rows are
merged as before. No number of floor transitions multiplies this error.

Add (7)--(11). Every variable term decreases on n>=n0 and all fixed
tails are retained. Evaluating the resulting rational upper at n0 with
L replaced by14 gives

    eta0=12989329736187619160983471
                  /38345245772322816000000000000<1/1000.    (12)

This proves (1), including the origin. It also bounds the origin model
normalization error by1/1000 since S(0,0)=Lambda_c. The fixed model is
exactly N1-15's one-correction model; none of its terms was removed.


## Checks, scope and split history

The one original exact Fraction control and its 0.000206207process CPU
seconds are recorded in [the attempt](../attempts/C13-onset.md). No new
mathematical computation was run for this repair. No phase/kernel/degree
scan, numerical quadrature, fitted estimate, energy premise or executable
certifier claim is introduced.

This is a representation theorem only. Its actual near maximum
comparison is [C13-near-comparison](C13-near-comparison.md); far phases,
actual-corner descent and global equality have separate records.

2026-11-06, author response to F1/F2. This file splits its stated scope
from the original combined PD-T?argmax-bridge-C13-onset record, freeze
`6cc04de4d3cc8303c3660043bf15b92e50c527ffd21e10747cdc49de3ec3f070` (483 lines,22065bytes).
The exact local snapshot, source mapping and current file identities
are recorded in the attempt. Original proof paragraphs and equation
numbers are retained where possible, so those numbers refer to the
original reviewed sequence. No final ID or shared crosswalk is assigned
by this worker. Rules read4b728b04216a5490910780bc609a82b853058426;
parent-assigned auxiliary Sol xhigh role, serving metadata unexposed.
