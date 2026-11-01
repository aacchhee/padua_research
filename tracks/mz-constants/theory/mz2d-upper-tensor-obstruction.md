# PD-N?mz2d-codex-11 — doubled tensor weights do not majorize Padua

ID kind: PD-N.
Aliases: pointwise tensor-CC majorant failure; checkerboard weight ratio.
Split from: IDEA?mz2d-codex-11.
Split into: none. The upper target remains in
[PD-T?mz2d-codex-10](mz2d-upper-open.md).

## Statement

For the signed interpolatory `dx dy` Padua rule at `m=2`, the retained
node `(0,−1)` has weight `4/9`, whereas its weight in the full-grid
tensor control `CC_2 tensor CC_3` is `4/27`. Consequently

\[
 w^P(0,-1)=3w^{\rm tensor}(0,-1)
 >2w^{\rm tensor}(0,-1).                                  \tag{1}
\]

The proposed universal pointwise majorant
`wPad(j,k)<=2 wCC_m(j) wCC_(m+1)(k)` is therefore false.

## Definitions

Padua nodes, weights and the tensor control are exactly those in
[definitions.md](../../../topics/padua-mz-2d-20261101/definitions.md).
Both quadratures use unnormalized Lebesgue measure of mass four.
The tensor grid includes all nodes, while Padua retains even `j+k`.

## Assumptions

Only `m=2` is needed for the counterexample. The proposed majorant is
pointwise on retained nodes, not a Loewner inequality restricted to
values of low-degree polynomials.

## Status by part

Overall status: **PROVED** in development; independent audit pending.
Candidate disposition: **REJECTED: refuted**, for the precise universal
pointwise factor-two majorant. No spectral theorem is rejected.

## Negative-result scope

Attempted mechanism: IDEA?mz2d-codex-11, direct comparison of signed
Padua samples against twice the positive tensor-CC samples by individual
nodal weights.
Parameter range: an exact counterexample at `m=2`. No universal
all-degree weight-ratio asymptotic is asserted.

## Depends on

Interpolatory exactness and the elementary degree-two cardinal
polynomial below. The CC endpoint/central weights can be derived
directly by moment equations; PD-T013 is an alternative local reference.

## Checks

A floating diagnostic using `padua_weights` and `cc_weights` from
`tracks/mz-constants/code/mz2d_spectra.py` first found ratio three at
this node. The proof is analytic and independent of the diagnostic.
Run provenance and its explicitly measured scope are recorded in
[D2.md](../../../topics/padua-mz-2d-20261101/directions/D2.md).
No exact checker or independent rerun is claimed or needed for the
written elementary proof.

## Sources

IDEA-056/072, the marginal-compression predecessor, and PD-T013 were
read. This elementary pointwise comparison carries no historical
novelty claim and uses no external source theorem.

## Proof or evidence

The six retained `m=2` nodes are

\[
 (1,1),(1,-1/2),(0,1/2),(0,-1),(-1,1),(-1,-1/2).
\]

The polynomial

\[
 L(x,y)=(2y^2-y-x^2)/3
\]

has total degree two, is one at `(0,−1)`, and is zero at the other five
listed nodes. Hence exactness gives

\[
 w^P(0,-1)=Q_2L=\int_{[-1,1]^2}L
 =\frac{2(4/3)-0-(4/3)}3=4/9.
\]

The CC rule with x denominator two has the three nodes `1,0,−1` and
weights `1/3,4/3,1/3`: symmetry, constant exactness and x-squared
exactness give these values directly. The rule with y denominator three
has endpoint weights `1/9`. Indeed its symmetric weight pattern is
`a,b,b,a` at `1,1/2,−1/2,−1`; exactness for one and y-squared gives
`a+b=1` and `2a+b/2=2/3`, hence `a=1/9`.
Thus the tensor weight at the stated node is `(4/3)(1/9)=4/27`, proving
(1).

## Scope

This kills the proposed pointwise upper comparison, even before any
tensor polynomial norm estimate is attempted. It does not refute a
comparison on a restricted polynomial value space. In fact at `m=2`
the desired Padua upper inequality holds trivially on `Pi_1`, because
all squared products have total degree two and are exact. The failure
of the weight comparison is therefore particularly separate from the
spectral target.

## Open items

Independent audit. A successor based on tensor controls must use the
actual polynomial space or a different majorant and prove its final
constant; factor-two nodal domination cannot be its input.

## History

2026-11-01, Codex, requested gpt-6.1-sol xhigh, rules
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`, unchanged after campaign
merge of `806cc7b4509fd93bae652f9545d32d95529f8281`.
Candidate and kill test were recorded before the diagnostic. A small
floating failure was replaced by this full analytic counterexample.
