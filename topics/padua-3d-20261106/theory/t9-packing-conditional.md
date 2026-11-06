# PD-N?padua-3d-codex-T9-01 — conditional unshifted Haar count obstruction

ID kind: PD-N. Aliases: T9-PACK;18/19 threshold110.
Split from: none; split into: none. Depends on: T9-HAAR.

## Statement / assumptions / status

**Assume** every lattice packing of the three-dimensional unit l1 ball
has density at most18/19. For n≥110, no unshifted finite-subgroup Haar
cosine rule with at most binom(n+3,3) distinct nodes is exact on Π_{2n−1}³.

Overall status: CONDITIONAL. The density theorem is an UNVERIFIED source
premise, not a result proved or primary-read by this worker. Candidate
disposition: conditional class obstruction retained. No universal nonexistence.

## Negative-result scope

Attempted mechanism: finite subgroup H⊂T³, *unshifted*, equal torus
Haar masses followed by cosine folding, product-arcsine cubature precision
2n−1. Arbitrary phases, non-Haar masses and interpolation without this
cubature requirement are excluded from the conclusion's scope.

## Depends on / proof

T9-HAAR gives |X|≥19n³/108. This exceeds N=(n³+6n²+11n+6)/6 iff
f(n)=n³−108n²−198n−108>0. f(109)=−9809 and f(110)=2312;
For1≤n≤108, n²(n−108)−198n−108<0, and
f'(x)=3x²−216x−198>0 for x≥109. Consequently110 is the first
integer threshold for this inequality. This is an analytic count bound,
not an exhaustive lattice census. No conclusion is obtained at n≤109.

## Checks / sources / open items

Exact threshold checks: code/t9_checks.py, evidence/t9-checks.json.
T1 packing lead, DOI10.1016/S0885-064X(03)00005-0, and literature-T9.md
retain missing primary statement and normalization. Independent proof of
δ≤18/19, or inspection of a correct source theorem with that bound,
would discharge this specific dependency. Any other explicit δ<1 would
give an eventual obstruction via T9-HAAR, with its own threshold, but need
not justify110. Even then all phase/weight extensions remain OPEN.

## History

2026-11-06 Codex: maintain CONDITIONAL status rather than importing18/19
from a secondary lead. Threshold arithmetic is separate from source status.
