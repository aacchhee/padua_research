# PD-N?padua-3d-20261106-codex-T9-r06-04 — strictly positive unshifted cosine cubature cannot be minimal for n>=110

ID kind: PD-N.
Aliases: T9-R06-P; strict-positive packing obstruction; successor of conditional T9-01.
Split from: PD-T?padua-3d-20261106-codex-T9-r06-01, t9-r06-packing-source.md theorem’s negative cardinality consequence; this record gives an already named claim its own durable home.
Split into: none. Provisional ID retained; no final allocation or shared crosswalk edit.

## Statement

For every integer n>=110, no cubature supported on the full unshifted cosine image X=cos H of a finite torus subgroup H, with strictly positive weights at every node and exact on Pi_(2n-1) for product Chebyshev probability measure, has at most N=binom(n+3,3) nodes. More precisely every such rule has |X|>=19n^3/108>N.

## Definitions

H is a finite subgroup of (R/(2pi Z))^3, L its annihilator in Z^3, a a phase in radians, X=cos(a+H) coordinatewise, and mu is normalized product Chebyshev measure. Pi_n means total degree<=n. For this statement a=0, det(L)=|H|, and each cosine fibre has at most8 torus points.

## Assumptions

Finite subgroup, zero phase, full support with strictly positive weights, exact total degree2n-1, n>=110. The imported octahedron lattice-packing density18/19 uses the l1 unit ball normalization.

## Status by part

Overall status: **PROVED with explicit LITERATURE dependency**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Nonnegative-witness short-dual implication and folding inequality | PROVED | Local lemma and fibre size8 |
| Maximal lattice packing density18/19 | LITERATURE | Betke–Henk statement/normalization read; its full proof and Minkowski original not inherited |
| n>=110 exclusion | PROVED with explicit LITERATURE dependency | Local consequence of that imported theorem |

Candidate / claim disposition: **REJECTED: refuted** for minimal positive full-support unshifted subgroup cubature at every n>=110. Rejection reason: refuted within these hypotheses; translated or zero-mass rules are outside scope.

## Negative-result scope

Attempted mechanism: obtain exactly N total-degree nodes from a positive unshifted subgroup rule exact through2n-1. Parameter range: every n>=110 under the stated full-support/positivity hypotheses. The old CONDITIONAL PD-N?padua-3d-20261106-codex-T9-01 is superseded for this scope, not silently relabelled in its historical body.

## Depends on

PD-T?padua-3d-20261106-codex-T9-r06-02, positive identity-mass witness; PD-T?padua-3d-20261106-codex-T9-r06-01, packing reduction. Canonical source LIT?padua-3d-20261106-codex-T9-r06-01 (Betke–Henk), with T10-03 retained as its reading-event alias. [Source mapping](../novelty-gate-supplement-round08.md).

## Checks

No new numerical or optimizer run by this response worker. The local proof was read and reconstructed from the old combined body. [Audit03/T9](../audit-03/T9.md) independently accepted these scoped statements; [independent-checks-round06](../independent-checks-round06.md) records supplementary checks. The exact-algebra controls are [t9-r06-exact.json](../evidence/t9-r06-exact.json), with source/command identities in the old receipt manifest. Reading a historical output is not a new independent execution.

## Sources

[Round08 gate/source supplement](../novelty-gate-supplement-round08.md) records the actual predecessor bodies, source aliases and limits. External source dependencies appear explicitly below; no cited proof is inherited by citation.

## Proof or evidence

The local witness lemma forces every nonzero dual vector to have l1 norm>=2n. Therefore the translates of the radius-n l1 ball have disjoint interiors. The imported maximal lattice density18/19 gives

    (4n^3/3)/det(L)<=18/19,
    |H|=det(L)>=38n^3/27,
    |X|>=|H|/8>=19n^3/108.

Multiplying the difference19n^3/108-binom(n+3,3) by108 gives

    f(n)=n^3-108n^2-198n-108.

Here f(109)=-9809,f(110)=2312 and f(n+1)-f(n)=3n^2-213n-305>0 for n>=109. Thus the difference is positive for every n>=110. Betke–Henk's displayed packing lattice is a critical lattice of the difference body2O, and the comparison packing lattice is n Bcrit, not(n/2)Bcrit; this uses the companion corrections from audit03-fixes.

## Scope and D3

D3: in dimension2 the unit l1 ball has area2 and the lattice-packing bound is density<=1. The analogous inequalities give det(L)>=2n^2 and |cos H|>=n^2/2. This is strictly below the Padua cardinality(n+1)(n+2)/2, so that argument does not exclude Padua. The sharper three-dimensional18/19 constant and n>=110 threshold are essential here.

## Open items

The finite complement n<=109 is not classified by this theorem; handoff08's separately assigned unrestricted probes own its new evidence. Arbitrary phases and removal of the identity through zero masses are not covered. E4's exact source-dependent label is pending AC’s convention decision; it must never be shortened to bare PROVED.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Response08 completes audit03 novelty m2/m3 by splitting already named statements from combined bodies. Statements/statuses are retained; E4's source-label criterion belongs to root and AC. Old pinned bodies are unchanged by this worker.
