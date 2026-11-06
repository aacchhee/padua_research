# PD-T?padua-3d-codex-T1-02 — original C_k obstruction target

ID kind: PD-T. Aliases: broad torus-coset obstruction; cubature Padua package.
Split from: none. Split into: PD-N?padua-3d-codex-T1-01, the explicitly
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
Candidate disposition: IDEA?padua-3d-codex-T1-02 deferred, not rejected.

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
