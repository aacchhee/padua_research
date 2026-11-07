# PD-T?argmax-bridge-codex-D23-01 — low-order full-row cotangent error budget

ID kind: PD-T. Aliases: D23 cheap arithmetic; J2/K8/L4/WD16;
low-order C11 specialization; full normalized S tail accounting.
Split from: none; a specialization of C02/C06/C08, with their original
claims unchanged. Split into: none.

Rules/input: `c1e5bef6ae645dd4e42c82c8fe2c709b76b8a2f4`.
2026-11-06, Codex mathematical developer, requested Sol xhigh; actual
serving model/effort metadata are not independently exposed.

## Statement

Use the exact C02 point-row decomposition of the true full normalized
primitive

    S_n(alpha,beta) = [n(n+1)]^-1 sum_(r,k) |F_rk|,

on alpha,beta>=0, alpha+beta<=pi. Retain the four rows
`0,2m-1,m-1,m`, m=n+1, and every guarded direct point by their finite
polynomial values. In each other row use at most twelve disjoint blocks
per cotangent channel, with at most n samples per channel. Set

    a=(cos alpha+cos beta)/2 in [0,1],
    B_n(a)=2+(4a/pi)H_n,
    M_J=389120/(19683*pi^5)*(2J+3)^4*4^-J,
    eta_(K,L)=|B_(2L)|/[(2L) K^(2L)],
    T_W=16/(9*pi^2)*4^(-W-1)*[(2W+3)*4/3+8/9].       (1)

Here the Bernoulli number in eta is unrelated to the row factor B_n.
For integers J>=1, K>=1, L>=1, W>=1, replace the smooth residual by
C02's polynomial of degree 2J+1, each harmonic sum by its K-prefix/L-order
formula, and each endpoint derivative w' by its centered residual series
through W. The resulting exact-real number A satisfies

    |S_n-A| <= E_n(J,K,L,W,a),
    E_n = B_n(a) [7*pi^4*M_J/(2880*n^4)
                   +48*eta_(K,L)/pi +2*pi*T_W/n^2].    (2)

All analytic tails, including both derivative endpoints in every block,
are included. For the ONE proposed source candidate

    J=2, K=8, L=4, W=16,

    E_n < 2/10^7          (160<=n<=2147483647),         (3)
    E_2048 < 11/(2*10^8),                             (4)

uniformly over the closed phase triangle. Formula (2) remains valid for
every n>=2; (3) does not assert the same small bound below160 or at
unbounded n. It is a bound for the full normalized S, not a single row,
four-special-row surrogate, limiting model, or actual four-copy lambda.

## Definitions, assumptions and status

Overall status: **PROVED analytic developer corollary**, distinct review
pending. It depends only on the accepted exact row/block domain and
remainder proofs, reconstructed below. Implementation acceptance and
measured speed remain separate and unexecuted.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| General full-row tail formula (2) | PROVED | C02 plus the C06 derivative series, including its block count |
| Fixed-order specializations (3)–(4) | PROVED | Explicit rational majorants below |

The exact phase row identity, correctly guarded sign partition, excluded
collision values, four retained rows, at most twelve blocks per channel,
and the coefficient bound (5) are hypotheses already proved in C02/N2.
No empirical sign decisions, interval overlap, unproved small remainder,
or cancellation between positive error budgets is assumed. Finite
integer ceilings apply only to the specialization/implementation, not to
the exact-real row identities.

## Depends on

- `C02-row-cotangent.md`, equations (1)–(4), (6)–(11), (15)–(16), and
  `independent-checks-C02-row.md`: all J>=1; all K,L>=1; all ordinary rows.
- `N5-partial-cotangent.md`: corrected midpoint error7qh^4/5760 times
  the residual fourth-derivative bound, on the full extended cell domain.
- `attempts/C06-rows-code.md` and `independent-checks-C06-rows.md`:
  the centered residual derivative series and both endpoint tails.
- `C08-row-box-contract.md`, (16)–(17): the same full-row derivative
  charge, already written for WD96; this record substitutes a general W.
- `independent-checks-C10-rows.md` and `independent-checks-C11-rows.md`:
  outward moment recurrence and the unchanged successful-call contracts.

No published source theorem, asymptotic model, benchmark, or numerical
experiment is a premise. Gate/classification: `../ideas/D23-cheap-backend.md`.

## Proof

### 1. Orders and domain really are parameterized

For every block, x_i=pi(y+i)/n lies strictly in(0,pi). Its extended cells
are in[-pi/4,5pi/4], hence z=x/pi-1/2 has |z|<=3/4. The two poles at0
and pi have already been removed before expanding the residual.

C02's fourth derivative tail begins at j=J+1. Its coefficient majorant
is valid for j>=1, and J>=1 puts every fourth derivative tail term at
j>=2. Thus J2 and J4 both satisfy the original hypotheses. The proof
uses the combined residual series of radius3/2 in z, not the uncancelled
tangent series of radius1/2. The cells/domain and the exact polynomial
moment identity do not depend on J. There is no special n floor here.

For q>K, the Euler–Maclaurin argument starts at x=y+K>K. The periodic
Bernoulli remainder is bounded using the LAST INCLUDED order2L, not an
unproved next-term rule. Every positive K and L>=1 is permitted. Thus
K8/L4 is valid, including arbitrarily small y>0. The potentially tiny
denominators are still in the explicit prefix. For q<=K this part is
exact. Changing K does not weaken the strict pole guard.

The derivative residual series uses

    |b_j| <= (4/pi)*(3/2)^(-2j-2),  j>=1.

For W>=1, differentiating its tail j>=W+1 gives, on |z|<=3/4,

    |w'(x)-sum_(j=0)^W b_j*(2j+1)*z^(2j)/pi|
      <=16/(9*pi^2)*sum_(j>=W+1) (2j+1)*4^-j
      = T_W.                                           (1a)

The geometric sum proves the formula in(1); no requirement W>=96
occurs. In the existing implementation the coefficient vector extends
through WD, so the additional implementation condition is WD>=J.
The candidate2<=16 satisfies it. Coefficients for both uses retain their
full Arb640 preparation balls; no midpoint coefficient is substituted.

### 2. Full ordinary-row accumulation

Write h=pi/n and use C02's actual coefficients C_r,D_r, which satisfy

    sum_ordinary (|C_r|+|D_r|) <= m B_n(a).              (5)

The error of one partial block is at most

    7*q*h^4*M_J/5760 +2*eta/h +h*T_W/12.               (6)

The last term follows because each of the two endpoint derivative balls
has radius T_W and the derivative difference is multiplied by h/24.
It cannot be discarded when WD is decreased. For each channel the
disjoint sample counts sum to at most n, and at most twelve blocks give

    7*n*h^4*M_J/5760 +24*eta/h +h*T_W.                 (7)

The exact signed-row decomposition multiplies its two channel sums by
`-2*C_r` and `-2*D_r`. Multiply(7) by2(|C_r|+|D_r|), sum(5), then divide
by nm. This gives exactly(2). In particular the smooth term does NOT
receive a twelve-block factor, whereas BOTH harmonic tails and BOTH
derivative endpoint tails do. Retained/direct polynomial values have
zero analytic row approximation error; their actual numerical radii
are retained separately, as required below. No four-special-row H8
bound has been reused for the ordinary rows.

### 3. Explicit budget for the single candidate

Since B8=-1/30, the harmonic tail is exactly

    eta_(8,4)=1/(240*8^8)=1/4026531840.                (8)

The derivative tail is bounded, using pi>3, by

    T_16 < 6848/(729*2^34) < 6/10^10.                 (9)

The smooth coefficient simplifies before it is bounded:

    7*pi^4*M_2/2880
      =7*389120*2401/(2880*19683*16*pi) < 3.           (10)

Use H_n<=1+log n and pi>3. Let

    D(x)=2+(4/3)(1+log x),  x>=1.

Then B_n(a)<=D(n), and D(x)/x^4 is strictly decreasing because its
derivative is x^-5[4/3-4D(x)]<0. Also log2<7/10: the first four
positive terms of exp(7/10) sum to12013/6000>2. Consequently, n<2^31
gives H_n<23 and B_n(a)<98/3; n=160<2^8 gives D(160)<54/5.

For every160<=n<=2147483647 the three terms in(2) are therefore bounded
separately by

    E_smooth < 3*(54/5)/160^4 < 5/10^8,
    E_harmonic < (98/3)*16/4026531840 < 13/10^8,
    E_derivative < (98/3)*8*(6/10^10)/160^2 < 1/10^11.

Their sum is less than2/10^7, proving(3). All displayed comparisons are
integer/rational comparisons after the elementary pi/log bounds.

At n2048=2^11, D(2048)<68/5. The same separate bounds give

    E_smooth < 3*(68/5)/2048^4 < 3/10^12,
    E_harmonic < (68/5)*16/4026531840 < 541/10^10,
    E_derivative < (68/5)*8*(6/10^10)/2048^2 < 2/10^14.

Their sum is less than11/(2*10^8), proving(4). No measured input value
or phase cancellation enters this specialization.

### 4. Arithmetic inclusion and the actual upper-error contract

Formula(3) is an ANALYTIC truncation budget, not the full output radius.
The existing C10 moments compute at the exact input midpoint with
MP=640 Arb operations, round the WHOLE resulting ball to P=160, then
add exactly once

    d*q*2^(1-d)*rad(y)/n.                              (11)

Indeed z_i=(y+i)/n-1/2 has |z_i|<1/2 throughout the guarded input ball,
so the mean-value derivative bound in(11) holds for each moment. The
centered-cell recurrence is a finite triangular identity for every d;
J2 simply restricts it to d<=5. Induction over the recurrence using Arb
inclusion retains every640-bit rounding radius, including cancellation
in the endpoint powers and prior moments. Outward160 rounding retains
those radii. There is no new fixed precision theorem, suppressed
conditioning radius, or assumption that smaller d numerically gives a
narrower interval. The same inclusion argument applies to the unchanged
CP=640 coefficient construction, to all160-bit operations, W via entire
sinc, harmonic reciprocals/logs, and the retained/direct finite primitive.

After adding the three valid tails inside the partial balls and carrying
all complete coefficient/partial/direct balls through all rows and the
normalization, the returned ball I=[c-R,c+R] contains S_n. Thus its true
upper endpoint U=c+R obeys

    0<=U-S_n<=2R.                                     (12)

For the later fixed point pilot, REQUIRE the full radius R<=1/100000.
Then the actual normalized upper overhead is <=1/50000=2e-5, comfortably
below the motivating1e-3 slack. This criterion includes roundoff,
coefficient uncertainty, input conversion, retained rows and every tail.
The tails are already in R and MUST NOT be added to it a second time.
If a diagnostic uses binary64 projections, require the corresponding
outward endpoint gap separately; a nearest-rounded radius estimate alone
is not the formal radius check.

For arbitrary-precision rational phase inputs pole proximity can be
arbitrarily small. No input-independent absolute bound on all floating
conditioning radii follows merely from P160/CP640/MP640. The exact
returned-ball condition is consequently essential; a wide successful
ball remains valid but fails this pilot's tightness gate. No precision,
order, input, source or case rescue is allowed after such failure.

## Cost scope, checks and sources

The source-level moment triangular loops have D(D+1)/2 iterations,
D=2J+1:561 atJ16 versus15 atJ2. The actual even-k correction counts
are272 versus6. The w' Horner loop drops96 to16, the harmonic explicit
prefix cap32 to8 and Bernoulli corrections16 to4. These are exact
operation-count reductions, not a runtime speedup prediction. The four
retained rows still cost4n finite polynomial evaluations, and ordinary
row/sign/direct work remains O(n). Coefficient preparation still uses
the same exact rational recurrence and CP640, now through WD16.

Only read/search/hash/file-writing tools were used in this paper gate.
No native numerical call, compiler, board, finite scan, benchmark,
producer or checker run occurred. The supporting proofs and accepted
review reports were read; no independent acceptance of D23 is claimed.

## Scope and open items

This developer proof passes the paper validity/normalized-tail gate for
one proposed fixed candidate. It does not authorize scientific execution.
Next: distinct mathematical review, an isolated exact-constant source
copy, a frozen finite SPEC and distinct source review before root release.
The proposed known-n2048 generic point is a cost/accuracy diagnostic;
no cover, new degree, actual lambda benchmark, or throughput law follows.
Future cover use must preserve its own complete certificate/replay gates.

## History

2026-11-06: D23 prospective task supplied J2/4, WD16/24, K8/LH4 as
possibilities. This record selects only J2/WD16/K8/LH4 after reconstructing
the accepted parameter hypotheses and charging all three tails. The
standard parameter specialization makes no novelty or priority claim.
All C11 sources, shared files, native fallbacks and Git state untouched.


## Root analytic/source review closure — 2026-11-06

Report [D23](../independent-checks-D23-backend.md), SHA256 `874ba7d9322f2c2cc1df3a90e75e4e755fd0495296c523edc4e0d6d3deb14b48`, accepts this parameterized analytic bound and the unchanged first frozen backend/pilot contract. Root adopts the analytic implication. No measured cost, successful pilot or finite cover follows from this closure. Exact primary release/accounting and independent replay remain separate; reviewed prefix is preserved.


## Independent implementation-result closure — 2026-11-06

[D23 result review](../independent-checks-D23-result.md), SHA256 `fefe368e1a9dfe40b8698c6daced0cec5ce764aa8a921677745f775cb4c4b06a`, accepts the fixed fresh old/new2048 pilot and source/evidence inspection of the original controls. It independently rebuilt both libraries and executed exactly two cold-table calls; the24 primary calls were not all rerun. D28 additionally freshly validates41 new-backend points at6912. Root adopts this implementation scope and the finite measured speed comparisons, not an all-degree runtime law. Exact mathematical error/radius hypotheses above are unchanged; final Claude audit remains separate.
