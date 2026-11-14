# PD-T?argmax-bridge-codex-N4-02 — Probability mixtures of full evaluation vectors are rigid

ID kind: PD-T.
Aliases: coordinate-square variance obstruction; positive cardinal-vector rigidity; evaluation mixtures.
Split from: none; elementary lemma used by both N4 and N6.
Split into: none.

## Statement

Let d>=1 and n>=2. Let distinct nodes B_1,...,B_N in R^d be
unisolvent for Pi_n, the full space of polynomials of total degree<=n,
with cardinal polynomials L_1,...,L_N. Fix z in R^d. Let mu be a
probability measure on R^d with finite second moments and integrable
L_i. If

    L_i(z)=integral L_i(y) dmu(y)  for every i,                 (1)

then mu is the point mass delta_z.

In particular:

- A probability mixture of complete cardinal/evaluation vectors equals
  L(z) only when the measure is concentrated at z.
- All L_i(z)>=0 if and only if z is one of the nodes.

## Definitions and assumptions

Unisolvence means evaluation on the nodes is a bijection Pi_n to R^N;
thus every p in Pi_n satisfies p(y)=sum_i p(B_i)L_i(y) identically.
The word complete in the statement requires all N cardinal coordinates.
A finite mixture is included by taking a finitely supported probability
measure. Integrability is automatic for a finite mixture or a measure
on a compact set. No norm inequality is assumed.

## Status by part

Overall status: **PROVED**, elementary written proof.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Rigidity under(1) | PROVED | Reproduce coordinates and their squares |
| Nonnegative cardinal vector iff node | PROVED | Apply rigidity to the nodes' probability distribution |

Candidate disposition: retained generic supporting lemma, with no
historical novelty claim. N6 applications use this ID rather than
allocating a duplicate generic theorem.

## Depends on

Elementary interpolation and the fact that a nonnegative integrable
function of integral zero vanishes almost everywhere. PD-T101 supplies
unisolvence for its Padua specialization, but is not needed for the
generic theorem.

## Proof

For any p in Pi_n, multiply(1) by p(B_i) and sum to get

    p(z)=integral p(y) dmu(y).                                (2)

For each coordinate a=1,...,d, the polynomials y_a and y_a^2 belong to
Pi_n. Equation(2) therefore gives E[y_a]=z_a and E[y_a^2]=z_a^2.
Since mu has mass1,

    integral sum_a (y_a-z_a)^2 dmu(y)=0.

The integrand is nonnegative and vanishes only at y=z. Thus mu is
concentrated at z and equals delta_z.

If L_i(z)>=0 for every i, partition of unity gives sum_i L_i(z)=1.
Apply the proved statement to mu=sum_i L_i(z) delta_(B_i):
its cardinal moments equal L_i(z), by L_i(B_j)=delta_ij. Hence this
measure equals delta_z, forcing z to be one of the nodes. Conversely,
at a node the cardinal vector is a standard basis vector and is
nonnegative. QED.

## Checks and sources

No numerical computation or external source is a premise. This is the
elementary zero-variance argument, not a source theorem imported from
hypergroup literature. `../code/n4_exact_invariants.py` provides exact
Padua small-degree checks; these are supplementary verification of
the specialization, not the proof. Independent review is pending.

## Scope

This rules out positive probability mixtures of **complete evaluation
vectors** supported away from the point being represented. It does not
rule out mixtures of sign projections, scalar Lebesgue values, different
features, or general nonnegative matrices acting on one signed vector.
In particular it does not contradict N4's unrestricted transport
criterion, whose columns are not assumed to be evaluation vectors.

## Open items

No all-degree argmax statement follows. Any proposed positive-mixture
repair must explicitly state which reproduction condition it relaxes.

## History

2026-11-05, Codex N4 round1, parent-assigned gpt-6.1-sol xhigh; runtime
metadata not independently exposed. Rules/input
`98d6c00d8a474cf97602c9cfdea631a837191ac0`. Parent coordinated ownership
with N6 to avoid duplicate generic IDs; N6 owns only its application.
