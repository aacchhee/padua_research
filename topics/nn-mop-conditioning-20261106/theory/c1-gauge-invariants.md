# PD-T502 — diagonal gauges retain diagonal sensitivity

ID kind: PD-T. Aliases: invariant b fields; frozen gauge; smooth gauge
section; fieldwise gauge infimum; terminal step-line lower bound.
Split from: none. Split into: none.

## Statement

Fix a normal positive common-support input q with N distinct real nodes,
and the PD-T432 input box. Let the diagonal gauge act on the type-II
polynomials by R_nu=s_nu P_nu, with s_nu>0 and s_(0,0)=1. Either freeze
every s_nu as q varies, or choose each s_nu(q) positive and C1 locally.
Include all coefficients in both rescaled NN recurrences and scale each
coefficient field by its own base sup magnitude (absolute scale one for
an identically zero base field). Write kappa_s for the local induced norm.
Then, for either gauge class,

    kappa_s >= max(kappa_b1, kappa_b2),

where kappa_bj is the induced condition of the original b_j field with its
original field sup scale. For the alternating first-e1 step-line, with all
four coefficient fields retained, kappa_s>=kappa_beta, with beta scaled by
its own field sup. These are exact inequalities for every gauge.

Let K_fix be the infimum over positive fixed gauges, and K_dep the
infimum over all such local C1 sections. Pointwise at q,

    kappa_b <= K_dep <= K_fix <= kappa_monic.                 (1)

For the exact Krawtchouk inputs of PD-T437, every N>=2, with the node
scale one and componentwise-relative weights, (1) implies the all-gauge
NN lower bound

    K_dep >= 5/[2(N-1)^2] *
      [(5+2sqrt(6))^(N-2)+(5-2sqrt(6))^(N-2)].              (2)

For the same inputs and the alternating step-line, let K_dep^SL denote
its distinct gauge infimum. For every N>=3,

    K_dep^SL >= (4sqrt(6))^(N-1)/[4(N-1)(N-2)].                (3)

Both statements also hold for node scales |x_l| or 2/(N-1), logarithmic
weight input, and fixed-mass tangent boxes: the witness changes weights
only and preserves mass. Equations (2)–(3) prove exponential lower growth
for these fieldwise gauges. They make no claim for an output norm with a
single scale combining all matrix entries.

## Definitions

Write the monic NN relations as

    xP_nu=P_(nu+e_j)+b_(nu,j)P_nu
                         +sum_i a_(nu,i)P_(nu-e_i).

Absent terms are omitted. A terminal successor is the common support
polynomial; its otherwise arbitrary scale can be included. The rescaled
coefficients are

    u_(nu,j)=s_nu/s_(nu+e_j),
    B_(nu,j)=b_(nu,j),
    A_(nu,i)=a_(nu,i) s_nu/s_(nu-e_i).                       (4)

The six fields are u1,u2,B1,B2,A1,A2, with only structurally present
entries. In the monic gauge the u fields are identically one with zero
derivative, so including them changes no PD-T432 condition.

On the step-line, R_k=s_k Q_k gives

    xR_k=u_k R_(k+1)+beta_k R_k+G_k R_(k-1)+D_k R_(k-2),
    u_k=s_k/s_(k+1), G_k=gamma_k s_k/s_(k-1),
    D_k=delta_k s_k/s_(k-2).                               (5)

A positive fixed gauge means a constant list s chosen at the base point,
then kept fixed throughout differentiation. A data-dependent gauge means
a local section q↦s(q), so its derivative is part of the output map.
The two infima are different definitions; merely selecting orthonormal
scales at the base point does not differentiate the orthonormal map.

For example a transformed coefficient a'=a exp(ell_nu-ell_mu) obeys

    da'=exp(ell_nu-ell_mu)[da+a(dell_nu-dell_mu)].             (6)

The second term vanishes only for frozen gauges. Constant signs may be
allowed as well: field sup norms and all conclusions above are unchanged.

## Assumptions

The finite normal domain and exact first-order derivative are those of
PD-T432. Gauge functions are C1, positive, and nonzero locally. Output
scales are always frozen at the base point when defining the derivative
norm. Arbitrary independent redefinition of those scales is outside this
gauge group. Relative field conditioning is not fully componentwise
output conditioning, which is infinite on sensitive zero entries.

## Status by part

Overall status: PROVED, by the written proof. No numerical premise.
Candidate disposition: retained variant of PD-T432/437; historical novelty
unclaimed. Historical pre-response scope: exact finite-N gauge minimizers
and general-family sharp rates remained OPEN. The separate `c1-gauge-sharp-rate.md` now combines this
lower bound with C2's sharp upper to prove the Krawtchouk NN gauge rate.

## Depends on

PD-T432 for the local map and row support norm. PD-T437 for the exact
terminal parity response, explicit binomial coefficients/scales, and its
summed lower bound. No external source theorem is used.

## Proof

Substitute R_nu=s_nu P_nu into the original recurrence and divide each
term by its own scale to obtain (4). This is an identity for every input
where the recurrence exists. Therefore B_j(q)=b_j(q) identically,
including for a data-dependent gauge; both its derivative and its sup
scale equal the monic ones. Taking the maximum over output fields proves
the lower bound. The same substitution proves (5) and the beta lower.
Every fixed gauge is a C1 section, while the identity section is allowed,
which proves (1).

PD-T437's parity perturbation w2_l(epsilon)=w2_l(1+epsilon(-1)^l)
has unit relative norm, fixes nodes/w1, and preserves the second mass.
Its terminal derivative is on b2 itself. The exact scale ||b2||=1/5 and
the summed terminal response in PD-T437 therefore prove (2) verbatim,
now for every fixed or C1 gauge.

For (3), set M=N-1, n=ceil(M/2), m=floor(M/2), r=m-1, c=24/25.
This is the terminal index of the prescribed alternating path; m>=1.
At total degree M, b1=b2, so its beta derivative is the same terminal
derivative. The explicit Krawtchouk formulas in PD-T437 imply

    b1_(n,m)=(-M+2n+m)/(5M), b2_(n,m)=n/(5M)

on the whole triangle. Thus |beta_k|<=1/5 and beta_0=-1/5, giving
||beta||=1/5. The same witness response divided by this scale is

    (5^M/M) Q_(n,r),
    Q_(n,r)=[v^r](1+c v/(1-v))^n.

For r=0, Q=1. For r>=1 the positive expansion gives

    Q=sum_(j>=1) binom(n,j)c^j binom(r-1,j-1)
      >=c^r binom(n+r-1,r)=c^r binom(M-2,r).

Here r is a central index of M-2 for both parities of M; hence the
binomial is at least 2^(M-2)/(M-1). Also r<=(M-1)/2. The same bound is
valid for M=2,3, where r=0. Therefore the witness ratio is at least

    5^M c^((M-1)/2) 2^(M-2)/[M(M-1)]
      >=(4sqrt(6))^M/[4M(M-1)],

as claimed. Node-input modifications do not alter a weight-only witness,
log weights have derivative w_l times the log perturbation, and the
parity mass is exactly zero. This proves every stated input variant.

## What is and is not invariant

A constant rescaling of a complete field cancels from its field-relative
condition, but a nonuniform site rescaling need not cancel from maxima.
Thus all fixed gauges need not have the same condition. They share the
diagonal lower bound.

The example s_nu=t^|nu| gives u=1/t and A_i=t a_i. Sending t to zero
shrinks all backward coefficients but enlarges the forward coefficients.
Each backward field's relative derivative is unchanged, so omitting the
forward coefficients does not remove the diagonal lower bound or justify
claiming polynomial fieldwise conditioning.

More strongly, choose s_(0,0)=1 and s_nu=t^(|nu|-1) for |nu|>=1.
All A entries of degree>=2 shrink by t, while degree-one A entries are
unchanged; all u derivatives vanish for a fixed gauge. Consequently the
infimum can discard highly sensitive offdiagonal rows in a field-sup
metric and need not be attained in general. The dated addendum below
records the subsequently proved b-dominant benchmark attainment. This is
a feature of the declared metric; the invariant B fields still prevent a small Krawtchouk condition.

An input-dependent section can normalize one nonzero coefficient to a
constant via (6), making its derivative zero. This is not equivalent to
freezing that gauge. Closed-walk products of matrix entries are invariant
under diagonal similarity, because the scale ratios telescope; NN
two-edge forward/backward products recover the corresponding a field.
Invariants can constrain a representation even when an individual entry
has been normalized. No universal rate is inferred merely from this
observation.

If one independently enlarges only the error-normalization denominator,
without rescaling the represented output and derivative, the reported
condition can be made arbitrarily small. That is a change of metric, not
the defined gauge optimization. A single matrix norm denominator is also a
different problem: arbitrary similarities change its size, so the above
fieldwise lower bound must not be applied to it without norm comparison.

## Checks, sources, scope and open items

The written result is independent of numerical runs. `code/c1_metrics.py`
checks terminal derivatives through a primal/adjoint moment solve against
the frozen AD graph at small N; C1 measurements have their own record.
No LIT-347 normalization equivalence is claimed here; M2 belongs to C4.
The finite Hahn measurements originally rely on the separate predecessor
finite normality theorem and remain MEASURED. Later C2 all-N Hahn
normality and diagonal lower results are inherited through this invariant
in `c1-hahn-gauge-lower.md`; its lower base2 is not sharp. The finalized
Krawtchouk sharp-upper dependency gives the separate gauge-rate squeeze
in `c1-gauge-sharp-rate.md`. These later consequences do not change the
standalone gauge algebra or infer an asymptotic theorem from finite fits.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, source/rules
`b4a04981d42c7cd872957facf5e3995e4096ca67`. New explicit gauge definitions
and quantified consequence of the retained terminal witness.

2026-11-06 audit-02 addendum: [response-gauge-infimum.md](response-gauge-infimum.md) proves finite positive attainment of the exact b-field lower for both b-dominant benchmarks, for all N>=2 in all six stated input models. The generic non-dominant optimizer problem remains OPEN.

## Final ID aliases (2026-11-06)

- `PD-T?nn-mop-cond-codex-C1-01` → `PD-T502`.
