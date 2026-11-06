# PD-T?nn-mop-cond-response-gauge — finite positive gauges attain the b-field lower

Preferred qualified provisional alias: `PD-T?nn-mop-cond-codex-response-gauge-01`; the heading ID is retained as a historical alias pending final allocation.
ID kind: PD-T. Aliases: degree-one anchored taper; finite gauge-infimum
attainment; b-dominance optimizer; fixed/smooth gauge equality.
Split from: none. Split into: none.

## Statement

Fix N>=2 distinct common real nodes and strictly positive weights for two
measures. Assume every mixed moment system through total degree N is
normal. Retain all six rescaled NN fields u1,u2,B1,B2,A1,A2 with their
separate base field-sup scales, as in C1-01. The input unit set may be any
fixed bounded symmetric tangent set; write ||Df||_* for the support norm
of a scalar derivative on that set. All coefficient maps and derivatives
below are evaluated at the same base input q.

Let v_i=a_(e_i,i)>0 be the two first marginal variances, and put

    d_i=||D a_(e_i,i)||_*,   r_i=d_i/v_i,
    L_i=max_(|nu|>=2,nu_i>0) |a_(nu,i)|,
    H_i=max_(|nu|>=2,nu_i>0) ||D a_(nu,i)||_*,
    K=max(kappa_b1,kappa_b2).

An empty maximum L_i or H_i is zero. For every t>0 choose the fixed
positive gauge

    s_(0,0)=1,  s_nu=t^(|nu|-1) for |nu|>=1.               (1)

This includes the terminal successor scales at degree N. Its exact
six-field condition is

    kappa(t)=max{K,
      max_(i=1,2) max(d_i,t H_i)/max(v_i,t L_i)}.          (2)

In particular, if

    0<K<infinity,  r_1<=K, r_2<=K,                        (3)

then the two all-gauge infima satisfy

    K_dep=K_fix=K,                                        (4)

and are attained by a positive fixed gauge (1). More explicitly, every
finite positive t satisfying

    t L_i<=v_i,  t H_i<=K v_i   (i=1,2)                   (5)

attains (4). Such t always exist; a constructive choice is

    t=min(1, v_i/L_i for L_i>0,
              K v_i/H_i for H_i>0).                      (6)

Here K_fix is the infimum over fixed positive gauges and K_dep over
local positive C1 sections, with every rescaled coefficient retained.
The fixed optimizer is itself a C1 section, so it attains both classes.

### Exact benchmark specialization

For each of the exact Krawtchouk and Hahn pairs specified below, every
integer N>=2 satisfies (3). Consequently (4) is valid and attained for
every such N in all these input models:

- node scale one, componentwise-node scales |x_l|, or spacing scale
  2/(N-1), always with componentwise-relative weights;
- any of those node models with separately fixed-mass weight tangents;
- natural logarithmic weight coordinates with the identical tangent set.

This is equality with the exact b-field condition of the selected input
model, not a formula for its numeric value. The field metric and gauge
class are essential; no single-matrix, componentwise-output or algorithm
error theorem is asserted.

## Definitions and assumptions

Use monic NN relations through coefficient degree M=N-1,

    xP_nu=P_(nu+e_j)+b_(nu,j)P_nu
                              +sum_i a_(nu,i)P_(nu-e_i).

Terms with nu_i=0 are absent. The rescaled coefficients for R_nu=s_nu P_nu
are u_(nu,j)=s_nu/s_(nu+e_j), B_(nu,j)=b_(nu,j),
A_(nu,i)=a_(nu,i)s_nu/s_(nu-e_i). Output denominators are frozen at q
when differentiating. A field identically zero at q uses absolute scale
one; the a fields here are nonzero because v_i>0. A zero b field uses
that same convention consistently in K and in the rescaled metric.

The general theorem assumes (3); it does not assert that b dominance
holds for every positive normal input or every tangent set. Positivity
of a scalar marginal variance follows from distinct nodes, positive
weights and N>=2; mixed normality is a separate assumption.

For benchmarks x_k=2k/M-1, k=0,...,M. Krawtchouk weights are

    w_(i,k)=binom(M,k)p_i^k(1-p_i)^(M-k),
    (p_1,p_2)=(2/5,1/2).

Hahn weights are

    w_(i,k)=(alpha_i+1)_k/k! * (2)_(M-k)/(M-k)! / Z_i,
    Z_i=(alpha_i+3)_M/M!,  (alpha_1,alpha_2)=(1,3/2).

Both masses are one. These are the PD-T290 inputs after per-measure mass
normalization (C2-02), which leaves kappa, K and r unchanged. Normality
is furnished by PD-T437 and C2-02 respectively. The chosen node
scales and tangent constraints are frozen at q.

## Status by part

Overall status: PROVED. The general finite optimization theorem (2)–(6)
has a written analytic proof. Its benchmark applications have analytic
tails, a proved finite reduction, committed exact code/essential receipt,
and an actually executed separate rerun plus a different primal-moment
implementation. The completed supplementary check is
[response-independent.md](../response-independent.md); completed review
and process records are in [audit-02](../audit-02.md) and [LOG](../LOG.md).

| Mathematical part | Status | Evidence |
|---|---|---|
| General formula and attainment under (3) | PROVED | Written finite-dimensional proof below; no computation |
| All-N Krawtchouk specialization | PROVED | Written M>=1 argument for non-spacing models, M>=2 for spacing; exact M=1 spacing case and distinct exact rerun |
| All-N Hahn specialization | PROVED | Written M>=14 tail, exact M=1..13 reduction and distinct exact rerun |

These are one finite-optimization theorem and its benchmark applications,
with routine variance/tail estimates below. No general all-input optimizer
characterization is asserted.
Candidate disposition: retained quantitative variant of C1-01/03 and
audit01 NOTE1. Historical novelty unclaimed. Full candidate/history:
[response-gauge-candidate](../response-gauge-candidate.md).

## Depends on

PD-T286/432 for the finite NN domain, analytic coefficient derivative and
field-support norm; C1-01 (`c1-gauge-invariants.md`) for gauge algebra and
K<=K_dep<=K_fix; PD-T437 for Krawtchouk normality and the mass-zero parity
lower K>=5^M/M; C2-02 (`c2-hahn-normality.md`) for Hahn normality and exact
b scales; C2-04 (`c2-hahn-terminal-rate.md`) for its positive A_M lower,
including the fixed-mass loss of at most two. The finite checker imports
no repository arithmetic code or third-party mathematical package.

## Proof

### 1. The finite-t identity and positive optimizer

A backward edge at |nu|=1 connects s_nu=1 to s_0=1. Every backward edge
at |nu|>=2 has ratio t. Thus the unique degree-one entry of field A_i is
v_i, with derivative support d_i. All its higher entries and their
frozen-gauge derivative supports are multiplied by t. Its base field sup
is exactly max(v_i,t L_i), and its maximal derivative support is exactly
max(d_i,t H_i). Every u entry is a nonzero constant in q, so has derivative
zero, even when its value is 1/t. The B fields and their denominators
are unchanged. The induced max-over-fields norm is therefore exactly (2).

All maxima involve finitely many analytic coefficient derivatives, so
L_i,H_i are finite. Under (3), (6) is strictly positive and satisfies (5).
The denominator of each A_i field then equals v_i and every derivative
row divided by v_i is at most K. Hence kappa(t)=K exactly. Every gauge,
including every input-dependent C1 section, has condition at least K
because B_j(q)=b_j(q) identically. Fixed gauges are C1 sections, proving
(4) and attainment in both classes.

For completeness (2) also shows

    lim_(t down to 0) kappa(t)=max(K,r_1,r_2).             (7)

Equation (7) alone is not an all-gauge characterization when (3) fails.
The positive inequalities (5), rather than the inadmissible t=0 limit,
prove the stated finite attainment.

### 2. A first-variance bound for the mixed input

For any positive probability weights pi_l on real nodes, set
mu=sum pi_l x_l and v=sum pi_l(x_l-mu)^2>0. Differentiating normalized
weights in relative coordinates dot w_l=w_l z_l gives

    dot v=2 sum_l pi_l(x_l-mu) dot x_l
           +sum_l pi_l((x_l-mu)^2-v) z_l.                (8)

For |dot x_l|<=1, |z_l|<=1, the exact unconstrained support is the sum
of the absolute coefficients in (8). Cauchy–Schwarz and the triangle
inequality imply

    r(v)<=2/sqrt(v)+2.                                  (9)

Indeed the two numerator sums are at most 2sqrt(v) and 2v. Restricting
node scales or imposing mass constraints only reduces that variance
row's support. Natural log weights give exactly the same first-order
relative-weight coordinates.

### 3. Krawtchouk dominance outside the one-node-spacing exception

The binomial generating identity gives Var(k)=Mp(1-p), hence
v=4p(1-p)/M. For the two parameters, v>=24/(25M), so (9) gives

    r_i<=5 sqrt(M/6)+2 <(5/2)sqrt(M)+2 <=(9/2)M.

For every integer M>=1, 5^M>=5M^2: the M=1 case is equality and the
inductive multiplier 5 is greater than ((M+1)/M)^2<=4. PD-T437's weight-only,
mass-zero parity direction therefore gives, for every stated node/mass
model,

    K>=5^M/M>=5M>(9/2)M>=r_i.                           (10)

The variance estimate covers mixed node scale one, componentwise scale
|x_l|<=1 and every fixed-mass restriction. For M>=2 the spacing scale
2/M<=1 also lies in that domain. Only M=1 spacing requires the exact
finite check in section 5. Log-weight models are tangent-identical.

### 4. Hahn variance and analytic tail

Write a=alpha+1 and b=2. The elementary convolution of rising factorials
used in C2-02 gives

    E k=M a/(a+b),
    E[k(k-1)]=M(M-1)a(a+1)/[(a+b)(a+b+1)].

For the second formula, replace k by k-2 in the weight sum after
factoring k(k-1)(a)_k/k!=(a)_2(a+2)_(k-2)/(k-2)!;
the first is the analogous one-step shift. Normalization cancels to the
displayed ratios. Combining these identities gives

    v=4ab(M+a+b)/[M(a+b)^2(a+b+1)].

For a=b=2 this is (M+4)/(5M)>=1/5. For a=5/2,b=2 it is

    v=(160/891)(1+9/(2M))>=160/891>4/25.

Consequently every mixed r_i<7 by (9), and the same holds for all smaller
node/mass boxes. The spacing box is smaller once M>=2.

C2-04 defines the positive integer

    A_M=sum_(k=0)^M T_(M,k)
          sum_(i=0)^(floor(M/2)-1) binom(M-1,2i+1)binom(k+i,k),
    T_(M,k)=sum_(h=0)^k binom(k,h)binom(M+k+3-h,M-k).

At k=M, T_(M,M)=2^M; the i=0 term is M-1. Hence, for M>=2,

    A_M>=2^M(M-1).

C2-04's terminal parity direction is weight-only, with admissible
fixed-mass correction costing at most two; thus in all six stated boxes

    K>=f_M/2,  f_M=2^M(M-1)/[27M(2M+3)].                (11)

For M>=2,

    f_(M+1)/f_M
      =2M^2(2M+3)/[(M+1)(M-1)(2M+5)]>1,

because numerator minus denominator is 2M^3+M^2+2M+5>0.
Moreover f_14/2=106496/11718>7. Equations (9) and (11) prove (3)
for every M>=14. Without fixed masses f_13>7 already suffices, but the
common finite reduction below deliberately covers M<=13 for all boxes.

### 5. Exact finite reduction and checker

The only remaining obligations are Hahn M=1,...,13 (N2..14) and
Krawtchouk M=1 (N2) for the spacing model. The checker verifies a stronger
single-terminal-row inequality in all six node/mass models for all those
sizes. Krawtchouk N4/N6 are supplementary sanity cases, not tail premises.

Here is the finite row calculation, all in the normalized x coordinate.
At the balanced terminal index nu=(ceil(M/2),floor(M/2)), let

    P(x)=x^M+sum_(r=0)^(M-1)c_r x^r,
    C_((s,j),r)=sum_l w_(s,l) x_l^(j+r),
    C c=-(sum_l w_(s,l)x_l^(j+M))_(s,j),
    C^T lambda=e_(M-1),  L_s(x)=sum_(j<nu_s)lambda_(s,j)x^j.

Both systems are nonsingular by the inherited normality. Implicit
moment differentiation gives dot tau=-sum_(s,j)lambda_(s,j)
dot L_measure,s(x^j P). The successor is the support polynomial,
whose subleading derivative is -sum_l dot x_l. The terminal b2 row
therefore has node and ordinary-weight coefficients

    g_x,l=1-sum_s w_(s,l)(L_s P)'(x_l),
    g_w,s,l=-L_s(x_l)P(x_l).                             (12)

The unconstrained weight support is sum_l w_(s,l)|g_w,s,l|.
For separately fixed masses it is

    min_lambda sum_l w_(s,l)|g_w,s,l-lambda|,             (13)

attained at a weighted median (C1-02 supplies the proof). Add the node
support sum_l s_l|g_x,l|. The exact variance support uses (8) and the
same support calculation. For b2's base field scale the checker uses
PD-T437's 1/5 for Krawtchouk and C2-02's exact rational tau-difference
formula over every coefficient site for Hahn. Thus the finite inequality

    terminal_b2_support / ||b2||_sup >= max(r_1,r_2)      (14)

implies K>=max(r_1,r_2). Positivity K>0 follows directly from each
strict positive comparison in the receipt (or from the translation
response in the mixed model). These are exact rational comparisons,
not a sample of an unbounded parameter range: sections 3–4 reduced all
remaining sizes to this finite list.

`code/response_gauge_infimum.py` implements (8),(12),(13),(14) in Python
`fractions.Fraction`, with exact Gauss–Jordan primal/adjoint solves.
Exact guards verify weight normalization/positivity, both mass-null
identities, translation covariance sum_l g_x,l=1, and the normalized
Hahn polynomial subleading coefficient against the closed formula.
For each N, the receipt stores the smallest exact dominance ratio across
the six models and a SHA256 of all six rational comparisons. Every
smallest ratio exceeds one. No floating-point comparison is used.

## Checks and essential evidence

Developer actually ran from repository root, Python3.12.14:

```sh
python topics/nn-mop-conditioning-20261106/code/response_gauge_infimum.py > /tmp/response-gauge-infimum.json
```

It exited zero: 96 exact comparisons passed (Hahn N2..14: 78;
Krawtchouk N2/4/6: 18). Only Krawtchouk N2 and Hahn N2..14 are essential
finite obligations. The compact committed receipt is
[`response-gauge-infimum.json`](../response-gauge-infimum.json), containing
the code SHA256, exact per-N minimum ratios and comparison digests.
No randomness, external inputs, numerical package or cold-storage artifact
is needed. Trusted dependencies: Python integer/Fraction arithmetic,
this checker implementation and the named analytic dependencies.

A distinct worker actually executed the checker into
`/tmp/response-gauge-independent-replay.json` and independently implemented
all 96 comparisons in `code/response_independent.py`, using direct primal
differential solves, whole-triangle moment-derived b2 scales, and a
different fixed-mass support minimization. Every exact comparison digest
agrees. The [independent record](../response-independent.md) reconstructs
the finite-t proof, variance bounds, tail/onset and finite reduction; its
[receipt](../response-independent.json) pins codes, commands, own outputs
and exact per-case minimum ratios. Reading the developer receipt alone
was not counted as a rerun. No computational certification obligation
remains within this finite reduction. Completed review and process
records are in [audit-02](../audit-02.md) and [LOG](../LOG.md).

## Sources, scope and limitations

The [gate](../novelty-gate-response-gauge.md) identifies
Fischer-type sensitivity (IDEA087/088, LIT112/113/365) and norm-balancing
algorithm scaling (LIT348/502) as background, at the literature index's
stated coverage. No new primary source theorem or historical-priority
claim is made. The audit supplied the taper and observation being proved.

This theorem resolves the exact finite-N gauge-infimum *value as K* and
existence of a finite positive optimizer for the specified benchmarks.
It does not compute the exact maximizing b row for every N, select the
most numerically useful gauge, or give an algorithm error guarantee.
Formula (6) can require extremely small t; exact mathematical attainment
says nothing about representability or rounding quality. The existing
LIT-508 record reports exact power-of-2 scaling (p. 628) for its forward
matrix problem, within its stated primary-page coverage; this supplies
no such guarantee for (6). LIT-507/508 and their reading limits are in
the [gate addendum](../novelty-gate-response-gauge.md). The NN six-field
theorem does not close PD-T432's alternate step-line diagonal-scaling
question. Generic inputs
without (3), and metrics combining all fields into one denominator,
remain outside the equality assertion. A smooth section might improve
non-b rows by its derivative; (4) follows solely because the b lower is
already attained by a fixed section.

## History

2026-11-06, Codex bounded mathematical worker; coordinator requested
`gpt-6.1-sol` high. Runtime model/effort metadata is not separately exposed.
Source/rules `3d5b29d7aa8c1274793139d7040695035e1bda22`. New result under
handoff03 audit01 NOTE1; gate timing is qualified in [LOG](../LOG.md).
The predecessor's statement that exact finite-N optimizers remain open is preserved as
history, not silently rewritten. The new theorem closes the stated
benchmark cases and the general b-dominant case only. Completed independent
executions and proof reconstruction are recorded in [response-independent.md](../response-independent.md).
