# PD-T?argmax-bridge-codex-H04 — Sharp quadrature for F03's smooth residual

ID kind: PD-T, provisional support lemma; no global allocation.
Aliases: H04; centered smooth partial rows; two-pole residual quadrature.
Split from: support obligation in F03 (8), not a conjunct of PD-T098.
Split into: none.

## Statement

For every integer n>=2 put m=n+1 and, for 1<=r<=n,

    t_r=r/m,  a_r=(1-t_r)/2,  w_r=cot(pi*t_r/2),
    B(x)=cot(pi*x)-1/(pi*x)+1/[pi*(1-x)],
    V_n=sum_(r=1)^n w_r sum_(l=0)^(r-1) B((l+a_r)/n).

The removable values are B(0)=1/pi and B(1)=-1/pi. Define

    I(t)=integral_0^t B(x) dx,
    C_B=4 integral_0^1 cot(pi*t/2) I(t) dt,
    beta_B=-4/pi^2
           +2 integral_0^1 t*cot(pi*t/2)*(B(t)+1/pi) dt.       (1)

All these integrands have the continuous endpoint values proved below.
Then, on the full integer sequence, with no parity restriction,

    |4 V_n/[n(n+1)] - C_B - beta_B/n| <= 17/n^2.             (2)

The coefficient in (1) is strictly negative:

    -4/pi^2 < beta_B < 0.                                   (3)

Thus the actual row centering does not eliminate the 1/n term. Formula
(2) is stronger than an O(log n/n^2) remainder for this contribution.

## Definitions and assumptions

All arithmetic and integrals are exact real analysis; logarithms are
natural. V_n is exactly the residual in [F03-identities-support](F03-identities-support.md) (8), with the same partial
rows and m=n+1. Its occurrence in the corner is exactly 4V_n/(nm).
No signed full-row substitution or conjectured coefficient is used.

For compatibility with other lanes, PD-T270's normalization is

    A_n=(2/pi)(log n+gamma+log(8/pi)).

A_n does not enter this proof; no replacement of n by n+1 or by n+1/2
inside that quantity is made here. The harmonic part of F03 (7), the
constant identification with kappa, and full-corner normalization are
separate obligations. This lemma assumes only the explicit V_n above.

## Status by part

Overall status: **PROVED**, written analytic development; distinct
mathematical review has not yet occurred.

| Mathematical part | Status | Evidence |
|---|---|---|
| All-n estimate (2), both parities and all row endpoints | PROVED | Exact cell union, uniform derivative bounds and quadrature below |
| Coefficient formula (1) and strict sign (3) | PROVED | Endpoint removal and elementary cotangent inequalities below |

The full PD-T098 sharp corner target and F03 origin-sign target retain
their own status; this supporting lemma does not complete either one.

## Depends on

[F03-identities-support](F03-identities-support.md) fixes the exact object
and its occurrence in the corner, using PD-T159 and PD-T226; the present
estimate for that object is self-contained. The elementary cotangent
partial fraction and its pole-cancelled identity are also proved locally
in PD-T269 section 4; the needed derivation and bounds are given below.
PD-T270/271 are normalization/background only, not unproved inputs.

## Proof

### 1. Pole removal and concrete derivative bounds

The elementary partial fraction, with the positive/negative k terms
paired, is

    cot(pi*x)=(1/pi)[1/x
                    +sum_(k>=1){1/(x-k)+1/(x+k)}].          (4)

For completeness, the local derivation used in PD-T269 works for each
noninteger real x: the cosine-series coefficients of cos(x*s) on
0<=s<=pi are a_0=2sin(pi*x)/(pi*x) and
a_k=2(-1)^k*x*sin(pi*x)/[pi*(x^2-k^2)]. They are absolutely summable;
evaluating the cosine series at s=pi and dividing by sin(pi*x) gives
(4). Uniform convergence on compact sets avoiding integer poles, and
absolute convergence of the differentiated series, justify the uses
below. At x=0 and x=1 the cancellation can equivalently be checked by
the Taylor series of sine and cosine.

Remove the poles k=0 and k=1 exactly. On [-1/4,5/4],

    B(x)=(1/pi)[1/(x+1)
                    +sum_(k>=2){1/(x-k)+1/(x+k)}].          (5)

This is analytic there. For j=1,2, its derivative series has the bound

    |B^(j)(x)| <= (j!/pi)*2*(4/3)^(j+1)
                                      *sum_(h>=1) h^(-j-1).

Indeed the remaining negative poles are -h and positive poles h+1,
h>=1, and both distances are at least h-1/4>=(3/4)h. The elementary
integral comparisons sum h^-2<=2 and sum h^-3<=3/2, and pi>3, give

    |B'(x)|<=3,  |B''(x)|<=5.                               (6)

Using B(0)=1/pi and the first bound over this interval also gives

    |B(x)| <= 1/3+3*(5/4) < 5.                              (7)

The exact identity B(1-x)=-B(x) gives I(1)=0. Direct integration,
with the constant fixed at t=0, also gives for 0<t<1

    I(t)=(1/pi)log[sin(pi*t)/(pi*t*(1-t))].                 (8)

The integral definition supplies its endpoint values without a log
singularity: I(0)=I(1)=0.

Put W(t)=t*cot(pi*t/2) with W(0)=2/pi. The inequality tan z>=z
on [0,pi/2) gives 0<=W<=2/pi<1. Substituting x=t/2 into (4),

    W(t)=2/pi-(4t^2/pi)sum_(k>=1)1/(4k^2-t^2).

Differentiate this absolutely and uniformly convergent series on [0,1].
Since 4k^2-t^2>=3k^2,

    |W'| <= (32/(9*pi))sum k^-2 < 3,
    |W''| <= (8/pi)[(16/27)sum k^-2+(4/9)sum k^-4] < 5.     (9)

The last comparison uses sum k^-2<=2, sum k^-4<=4/3 and pi>3.

### 2. The exact row cells and their uniform remainder

Fix a row, writing t=r/m and a=(1-t)/2. Its r samples (l+a)/n,
0<=l<r, are the midpoints of the r cells

    [(l+a-1/2)/n, (l+a+1/2)/n].

Their union is EXACTLY

    [-t/(2n), t+t/(2n)],                                 (10)

because r=mt. Their center is t/2. For n>=2 this union lies in
[-1/4,5/4]; indeed its upper endpoint is at most
(n+1/2)/(n+1)<1. Thus neither the r=n row nor the lower extension
causes an unestimated endpoint pole.

For a C^2 function on a cell of length h, Taylor's formula integrated
about its midpoint gives midpoint error at most h^3 sup|f''|/24.
Apply this with h=1/n, sum the r cells, and multiply the integral
comparison by n. The resulting error in the sum of B-values is at most

    r*5/(24n^2) <= 5t/(16n),                              (11)

where m/n<=3/2. Put d=t/(2n). The two extensions in (10) satisfy

    |n integral_(-d)^0 B - (t/2)B(0)| <= 3t^2/(8n),
    |n integral_t^(t+d) B - (t/2)B(t)| <= 3t^2/(8n),        (12)

by (6). Combining (11),(12) and t<=1 yields the signed approximation

    sum_(l=0)^(r-1) B((l+a)/n)
       =n I(t)+(t/2)[B(t)+B(0)]+e_(n,r),
    |e_(n,r)| <= 17t/(16n).                               (13)

Every row endpoint is included. No condition on n or r being even or
odd entered the exact geometry or these estimates.

### 3. Outer endpoint removal and exact n,m normalization

Define on [0,1]

    J(t)=integral_0^1 B(st) ds,
    F(t)=W(t)J(t)=cot(pi*t/2)I(t),
    G(t)=W(t)[B(t)+1/pi].                                 (14)

The integral expression for J removes the apparent pole at t=0.
From (6),(7), |J|<=5, |J'|<=3/2 and |J''|<=5/3. Therefore (9) gives

    ||F''||_infty <= 5*5+2*3*(3/2)+5/3 < 36,
    ||G''||_infty <= 5*(5+1/3)+2*3*3+5 < 50.              (15)

The endpoint values are exactly

    F(0)=2/pi^2, F(1)=0,
    G(0)=4/pi^2, G(1)=0.                                 (16)

For completeness the composite trapezoid estimate needed here is

    |(1/m)[(f(0)+f(1))/2+sum_(r=1)^(m-1)f(r/m)]
                 -integral_0^1 f| <= ||f''||_infty/(12m^2). (17)

On a single cell the error is one half the integral of
(x-left)(right-x)f''(x); its absolute value is at most
||f''|| h^3/12. Summing proves (17), without importing an
Euler--Maclaurin expansion or an unbounded formal series.

Multiply (13) by w_r and the exact 4/(nm). Since t*w_r=W(t)<=1,

    4V_n/(nm)=(4/m)sum_(r=1)^(m-1) F(r/m)
              +(2/(nm))sum_(r=1)^(m-1) G(r/m)+E_n,
    |E_n| <= 17/(4nm).                                   (18)

Apply (17) to F and G. Equations (15),(16) give

    (4/m)sum F=4 integral F-4/(pi^2*m)+R_F,
       |R_F|<=12/m^2,
    (2/(nm))sum G=(2/n)integral G-4/(pi^2*n*m)+R_G,
       |R_G|<=25/(3n*m^2).                               (19)

The endpoint terms in (19) combine EXACTLY, rather than being silently
replaced at a coarser scale:

    -4/(pi^2*m)-4/(pi^2*n*m)=-4/(pi^2*n).                 (20)

Thus (18)--(20) give (1),(2) with remainder bounded first by

    12/m^2+25/(3n*m^2)+17/(4nm).

To see it is less than 17/n^2, put y=n/m<1. Multiplying by n^2
rewrites this bound as

    (11/3)y^2+(151/12)y < 65/4 < 17.                       (21)

This is a concrete degree-uniform estimate for every n>=2, stronger
than the requested logarithmic remainder. All m=n+1 factors survived
until the exact cancellation (20).

### 4. The first coefficient does not vanish

Differentiating (5) shows B'(t)<0 on [0,1], because every term of its
first derivative is negative. Hence 0<B(t)+1/pi<2/pi in the interior.
Isolating k=1 in (4) gives, for 0<t<1,

    B(t)=1/[pi*(1+t)]
                   -(2t/pi)sum_(k>=2)1/(k^2-t^2).

The sum is strictly greater than sum_(k>=2)k^-2>=1/2, the latter
by integration from 2 to infinity. Consequently

    B(t)+1/pi < (2-t^2)/[pi*(1+t)].                       (22)

The elementary telescoping sum sum_(k>=1)(4k^2-1)^-1=1/2 and (4)
give the pole-cancelled identity, also PD-T269 (10),

    W(t)/(1-t^2)=2/pi+(4t^2/pi)
          *sum_(k>=1)1/[(4k^2-1)(4k^2-t^2)].

Bound the last factor (4k^2-t^2)^-1 by (4-t^2)^-1 to obtain

    W(t) <= (2/pi)*(1-t^2)/(1-t^2/4).                     (23)

Combining (22),(23),

    0<G(t)<(2/pi^2)*(1-t)*(2-t^2)/(1-t^2/4)
           <(4/pi^2)*(1-t),  0<t<1.

Integrating gives 0<integral G<2/pi^2. Formula (1) now proves (3).
This strict sign is an exact paper inequality, not a numerical fit.

## Checks and sources

PAPERONLY: no scientific job, code, import, numerical evaluation, scalar
check, degree selection, native/compiler execution, PDF or external
theorem assumption. Read/search/metadata commands and owned prose writes
are the only tool actions. No Git or shared registry/log mutation.
The proof was communicated to H01/H02/H03 and the root during work;
distinct mathematical review remains separate from this development.

## Scope and open items

This estimates exactly one contribution of F03 (7). It is a genuine
quantitative replacement of F03's nonvanishing coarse |B| bound, not a
finite exact one-index evaluator for V_n. The constants in (1) are
ordinary one-dimensional integrals with smooth endpoint removal; they
are not the original nested residual under another name.

The harmonic aggregate, total 1/n coefficient, kappa identification and
conversion to N=n+1/2 require their own proofs. No origin sign, global
argmax statement or completion of PD-T098 is claimed by H04.

## History

2026-11-07; rules/input ad257038cdff1d66f6e9c03d7ed43405c76cf6b0.
Root released H04 as a bounded PAPERONLY support round after the completed
Campaign-H gate. Owned idea/attempt registered candidate, separation and
kill test BEFORE derivation. Parent-assigned Codex mathematical developer,
inherited serving metadata not independently exposed. The initial
zero-first-coefficient subguess was tested and disproved by (3); the
registered expansion target is proved. No extra H round was launched.

## Dated status addendum — 2026-11-08 (Claude audit-03 MINOR fix H-C01)

"Distinct mathematical review has not yet occurred" in the status line above
is historical. This supporting result was accepted without conditions by
[independent-checks-H-support.md](../independent-checks-H-support.md) and as
part of the integrated proof by [independent-checks-H-main.md](../independent-checks-H-main.md);
the Claude reconstruction is [audit-03](../audit-03.md). The parent theorem is
[H-sharp-corner-expansion](H-sharp-corner-expansion.md). Separately, audit-03
finding H-C03 records that the two coefficients of the |W''| majorant are
swapped in the display near line 129 (correct form
(8/pi)[(16/27) sum k^-2 + (4/9) sum k^-4], still at most 4.74 < 5); that
mathematical correction is returned to the developer and is not applied here.


## Dated majorant alignment — 2026-11-08 (H-C03)

The canonical W'' majorant in (9) above follows the audit's requested
coefficient ordering, replacing `(4/9)sum k^-2+(16/27)sum k^-4` by
`(16/27)sum k^-2+(4/9)sum k^-4`. Indeed, for f_k(t)=t^2/(4k^2-t^2),

    f_k''(t)=8k^2(4k^2+3t^2)/(4k^2-t^2)^3
            =8k^2/(4k^2-t^2)^2
                         +32k^2*t^2/(4k^2-t^2)^3.

On 0<=t<=1, the denominator is >=3k^2, so
`f_k''<=8/(9k^2)+32/(27k^4)`. Multiplication by 4/pi gives
`(8/pi)[(4/9)sum k^-2+(16/27)sum k^-4]`, which is the historical
bound; this direct estimate is itself valid. The alternative swapped-form
bound requested by H-C03 follows instead by bounding the numerator as
`4k^2+3t^2<=4k^2+3` in the first displayed expression and using
`4k^2-t^2>=3k^2`, giving
`f_k''<=32/(27k^2)+8/(9k^4)`. Multiplication by 4/pi yields the
new canonical form. With the displayed series bounds and pi>3 it
is less than `(8/3)[32/27+16/27]=128/27<5`.
The bounds |W''|<5, (15), (19) and 17/n^2 are unchanged.

This is a mathematical change requiring a distinct mathematical review;
it is not an auditor in-place MINOR fix. The historical line remains pinned
at input commit `b45e29fa1fe3dbfa2517ff8043e5d9c440870530` and in audit-03;
no old audit report or source pin was rewritten. This addendum records the
actual derivation, including that the old ordering also admits a valid bound.


## Dated dependency correction — 2026-11-08 (F-01, H-C02)

The canonical exact origin reduction is now the separate **PROVED**
[F03-identities-support](F03-identities-support.md), split from historical
F03 sections 1–3. Its PD-T159 endpoint normalization and PD-T226 signed
periodic/polynomial endpoint rows are explicit premises of the reduction.
References above have been repointed accordingly. The original F03 sign and
useful-lower targets remain **OPEN** and are not assumptions of this result;
the proposed exact O(n) evaluator is also not assumed. H05's abstract series
estimate itself does not require the corner identification.

This corrects the source/status mapping, not the exact formulas or H theorem.
The original prose and reviewed source pins remain available at input commit
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`; no historical audit has been edited.
The [distinct review](../independent-checks-onset512-response.md#f03-source-split-and-h04-majorants--accepted-focused-response)
accepts the split and dependency map; H04's two valid majorants are also
independently reconstructed there.

## Dated note — 2026-11-08 (Claude audit-04 MINOR fix J2-06)

The audit-03 addendum above said the |W''| majorant coefficients are "swapped"
(finding H-C03). The later source correction and its distinct review show that
both coefficient orderings are valid termwise bounds and the revised ordering is
only weaker (about 3.71 against 3.49 when the zeta series are summed exactly);
the crude constants 128/27 and 1088/243 are both below 5, so 36, 50 and 17/n^2
are unchanged. The H-C03 characterization as a defect is therefore withdrawn;
response-03's DISPUTED disposition was correct. See [audit-04](../audit-04.md).
