# PD-N?argmax-bridge-codex-N6-02 — Positive full-vector lifts from fixed traces cannot move off their support

ID kind: PD-N.
Aliases: arbitrary-time trace-mixture obstruction; full-cardinal convex lift.
Split from: none. Scoped application of the generic N4 variance theorem;
that theorem retains its sole ID `PD-T?argmax-bridge-codex-N4-02`.
Split into: none.

## Statement

Let n>=2 and let L(z) be the complete vector of PD-T101's degree-n
Padua cardinals. For any fixed finite phase set S, put

    Gamma_s(t)=(cos((n+1)t+s),cos(nt+s)),
    U_S=union_(s in S) {Gamma_s(t): t in R/2pi Z}.

For each z in the square outside U_S, no probability measure mu
supported on U_S satisfies

    L(z)=integral L(y) dmu(y).                              (1)

The same impossibility holds if mu in(1) is replaced by a real signed
measure of mass1 and total variation<=1, if a common scalar envelope
E>=0 multiplies the right side of(1), or if the same invertible linear
regrouping R is applied to both vectors in(1).

In particular, with S={0,pi},

    U_S={(x,y) in [-1,1]^2: T_n(x)^2=T_(n+1)(y)^2}.         (2)

For every n>=2, z_n=(cos(pi/(2n)),1) lies outside this support, so this
fixed two-trace lifting mechanism fails at every such n. At n2 the
already frozen point z=(-1,-sqrt(2)/2) also lies outside U_S, even
when arbitrary comparison times along both traces are permitted.

## Definitions and assumptions

Use total-degree interpolation on PD-T101's even checkerboard and its
corrected (n,0) coefficient1. Measures are Borel measures on the compact
square; all required polynomial integrals therefore exist. A signed
measure is finite and real, and total variation is its usual Jordan
total mass. A common regrouping means the same invertible matrix is
applied at z and every integrated y. No norm bound, sign pattern,
extremizer or one-dimensional source theorem is assumed.

## Status by part

Overall status: **PROVED**, analytic application of the locally proved
N4 theorem. Independent review and Claude audit are pending.

| Part | Status | Evidence |
|---|---|---|
| No probability full-vector lift outside U_S | PROVED | Direct application of N4-02; no duplicate generic theorem |
| Trace support(2) and exact off-support points | Routine lemmas of this negative result | T101's Chebyshev identities and the round1 torus inverse |
| Signed-contraction, scalar-envelope and invertible-grouping forms | Equivalent formulations / routine algebra | Jordan masses, partition of unity and matrix inverse |

Candidate disposition: **REJECTED: failed**, for
`IDEA?argmax-bridge-codex-N6-02`'s universal full-vector lifting mechanism.
The specifically stated off-support existence assertion is refuted.
N6-03 and04 are **equivalent** IDEA dispositions, consolidated with02;
they receive no separate PD-N. Broad319/341 and the global scalar
trace-supremum comparison remain OPEN, not rejected.

## Negative-result scope

Attempted mechanism: express every full cardinal vector by a positive
probability mixture of vectors at points on fixed traces, then apply
the triangle inequality. Comparison times may vary arbitrarily, and
the measure may have continuous support. Parameter range: every n>=2
at points outside the prescribed support. The exact counterfamily
z_n in the Statement concerns S={0,pi}. The theorem does not assert
that no positive operator on cardinal indices exists, or that scalar
Lebesgue-value comparisons or noninvertible nonlinear features fail.

## Depends on

- [PD-T?argmax-bridge-codex-N4-02](N4-variance-rigidity.md), whose proof
  reproduces coordinates and their squares and forces mu=delta_z.
- PD-T101 for Padua unisolvence and cardinal partition of unity.
- [Round1 family verification](N6-parallel-family-verification.md)
  for the unimodular inverse, used only for the support equality.

## Proof or evidence

Apply N4-02 to(1). Compactness supplies its integrability hypotheses.
It forces mu=delta_z. Since U_S is compact, a measure supported on
U_S cannot equal delta_z when z is outside U_S. This proves the
negative statement without rebuilding the generic variance theorem.

For the two traces, write m=n+1 and choose physical angles
theta,phi in[0,pi]. A family preimage has phase

    s=m eta phi-n epsilon theta mod2pi,

for epsilon,eta in{+1,-1}. Thus it lies on phase0 or pi exactly when
one of m phi-n theta,m phi+n theta belongs to pi Z. This is equivalent
to |cos(m phi)|=|cos(n theta)|: cos A=+-cos B exactly when
A=B or A=-B modulo pi. Since T_n(x)=cos(n theta), this proves(2),
including endpoints. No uniqueness or noncollision is assumed here.

At z_n, T_n(cos(pi/(2n)))=0 and T_m(1)=1, so(2) excludes z_n.
At n2,z=(-1,-r/2),r=sqrt(2),

    T_2(-1)=1,
    T_3(-r/2)=4(-r/2)^3-3(-r/2)=r/2.

Their squares1 and1/2 differ, so this point lies off both entire traces.
This conclusion is stronger in support than round1's same-t test, but
it concerns full-vector probability lifts rather than scalar norms.

For a real signed measure nu of mass1, let p and q be the positive
and negative Jordan masses. Then p-q=1 and p+q=TV(nu)<=1, so q=0
and p=1. Hence this supposedly signed contraction class is exactly
the positive probability class. A TV>1 lift is outside the result;
its unweighted triangle bound incurs that larger norm factor and
provides no contraction automatically.

If a scalar E multiplies a probability mixture in(1), sum the
cardinal coordinates. Partition of unity gives1=E, eliminating the
envelope. If both sides of(1) are multiplied by an invertible R,
apply R inverse to recover(1). These are algebraic consolidations,
not independently failed mechanisms or new negative-result IDs.

For example, retain a pair as E_pair=(L_i+L_j)/2 and
O_pair=(L_i-L_j)/2. Its exact contribution is
|L_i|+|L_j|=2max(|E_pair|,|O_pair|), so complete pairwise regrouping
preserves the original norm and all sign changes. Retaining both
features is invertible, and a probability mixture of those complete
features is still(1). The distinct problem of controlling only scalar
block maxima has no complete polynomial-reproduction hypothesis and
is outside this result.

## Checks and sources

No numerical or symbolic execution is a premise. The n2 off-support
calculation is displayed completely. Round1 code and receipt were not
rerun or changed. No external fulltext or source result was used.
N4's independent review remains credited to that record, not counted
as a new independent N6 check.

## Scope and open items

This supplies a narrow mechanism gate, not a counterexample to PD-T099
and not a rejection of the covering family. In particular it does not
refute

    sup_square lambda_n <= max(max_t lambda_n(Gamma_0(t)),
                              max_t lambda_n(Gamma_pi(t))). (G)

An inequality like(G) can hold without a positive full-vector lift.
At n2, inherited PD-T209 and the nonnode corners' trace membership
give both suprema3, even though round1's same-t comparison fails.
Thus the distinction is substantive and has an accepted finite example.

## History

2026-11-05, Codex N6 round2, assigned gpt-6.1-sol xhigh; rules/input
`714f3cad18859c07cd13f31561f2a185f9591a7f`. Round1 published at
`0bca52bc1b8edf2e91d3749b710d2df285dc3e6b` and left unchanged.
The parent coordinated the generic theorem's ownership with N4.
The application and equivalence gates were written in the round2
candidate file before this proof was recorded; their expected outcome
was already informed by the existing N4 theorem.
