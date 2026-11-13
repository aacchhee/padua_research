# PD-T?padua-3d-20261106-codex-T1-02 — original C_k obstruction target

ID kind: PD-T. Aliases: broad torus-coset obstruction; cubature Padua package.
Split from: none. Split into: PD-N?padua-3d-20261106-codex-T1-01, the explicitly
restricted reflection-stable single-coset obstruction. The original target
below is retained unchanged in scope and stays OPEN.

## Statement

For each fixed k, let C_k consist of cosine images in [-1,1]^3 of unions
of at most k finite torus-subgroup cosets, without reflection-invariance
assumptions. Prove that for all sufficiently large n no X in C_k with
|X|=binom(n+3,3) is Pi_n-unisolvent while also having one of the handoff's
additional properties: (i) discrete orthogonality of a specified total-degree
basis, (ii) positive product-Chebyshev cubature of degree >=2n-1,
or (iii) the full Padua cubature/kernel package.

## Definitions and assumptions

The particular basis, normalization and interpretation of (i)/(iii) still
require formal specification. Positive cubature means positive real node
weights reproducing all polynomials of the given total degree under the
normalized product Chebyshev measure. No common subgroup is required for
different cosets in this broad definition; this choice only enlarges C_k.

## Status by part

Overall status: **OPEN**. A proved supporting/restricted result does not
make this target PARTIAL: its unrestricted quantifiers have not been
decomposed into an exhaustive proved/open case partition.
Candidate disposition: IDEA?padua-3d-20261106-codex-T1-02 deferred, not rejected.

## Depends on

The restricted result is separately PROVED for k=1 and a single whole
coset invariant under every coordinate reflection. No logical extension
to this statement is claimed.

## Checks and evidence

Finite exact diagnostics in t1-reflection-enum.json concern only the
classified restricted class. No broad C_k enumeration, cubature solver,
or all-coset-phase proof was executed. The LSX asymptotic bound is a
conjectural source statement, not a verified premise or a proof here.

## Sources

literature-T1.md records source access and coverage. Closest entries:
IDEA-029/120/181. No publication novelty claim.

## Scope and remaining gap

Reflection saturation of a coset is a union of reflected cosets and need
not be a single subgroup coset. Consequently it cannot be fed into the
binary classification without proof. Taking a cosine image erases angles
but does not grant this missing hypothesis. Arbitrary phases can also
cancel character moments, and arbitrary positive weights need not be the
Haar-pushforward weights. Unshifted Haar subgroups may admit a separate
lattice-packing obstruction; that known-mechanism lead is deferred until
its fulltext/theorem hypotheses and a valid reduction are recorded.

## Open items

Formalize (i)/(iii), analyze noninvariant subgroup cosets and multiple
cosets, and separate Haar weights from arbitrary positive cubature.

## History

2026-11-06, Codex gpt-6.1-sol xhigh (assigned; runtime metadata unexposed).
Original target preserved, with restricted result split explicitly.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.


## Original wording and class boundary — 2026-11-06 — m2

Verbatim original handoff-01 T1 target (bullets retained):

> Formalize the class C_k: node sets that are cosine images of cosets of finite subgroups of the torus 𝕋³, with reflection folding, or unions of at most k such cosets.
> Prove that for |X| = binom(n+3, 3), unisolvence on Π_n combined with any of the following is impossible for all large n:
> - (i) discrete orthogonality of a total-degree basis;
> - (ii) positive cubature of degree ≥ 2n−1;
> - (iii) the full Padua package (P2 + P3 of BRIEF §2).

The displayed Statement above clarified two phrases: “specified” basis in
(i), and product-Chebyshev measure in (ii). The earlier History claim of
unchanged wording was inaccurate; this addendum preserves the original and
records those clarifications. Under an existential interpretation of (i),
any unisolvent finite set with any positive weights gives a positive-definite
discrete inner product on Π_n; Gram–Schmidt supplies an orthogonal basis.
Thus mere existence of some such basis imposes no extra condition. A fixed
basis/normalization must be specified before the intended obstruction is
well-posed; that obligation remains OPEN. The cubature measure was fixed to
the topic's normalized product arcsine target, not a universal measure claim.

Audit-01 T1 NOTE-1 independently verified H={(i,j,i+j)/4:i,j∈Z/4}, a=0:
its 16 torus elements fold to ten points in {−1,0,1}³ with |det V(Π₂)|=256.
H is invariant under none of R1,R2,R3. This is audit evidence, not a newly
executed developer census here. It demonstrates why reflection invariance
cannot be silently dropped from the narrower theorem. No all-n conclusion
or disproof of the additional cubature package follows.

The Haar-packing lead is separately retained with a concrete resume condition
in IDEA?padua-3d-20261106-codex-T1-Haar, ../candidates-deferred-response-01.md.


## Dated audit-02 dependency synchronization — 2026-11-06

The unrestricted target remains OPEN. [T7's symbolic reduction](t7-finite-reduction.md)
covers arbitrary finite single cosets and continuous phase strata;
[its cubic survivor](t7-rank-two-survivor.md) is a computer-assisted PROVED
finite example. [T9-HAAR](t9-haar-packing-reduction.md) proves the
unshifted Haar/dual reduction, with [a conditional count obstruction](t9-packing-conditional.md)
under its stated density premise. These results do not settle unrestricted
minimal-node interpolation or its quality.
