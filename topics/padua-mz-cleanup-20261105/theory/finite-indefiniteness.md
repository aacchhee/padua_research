# PD-T?mz-cleanup-codex-01 — explicit finite signed Padua indefiniteness

ID kind: PD-T. Aliases: dyadic negative energy witness; finite loss of
positive definiteness. Split from: C1 constructive finite certification.
Split into: none. Frozen definitions are those of the original 2D topic.

## Statement

For the signed interpolatory Lebesgue Padua rule on the even checkerboard,
the quadratic form p -> Q_m(p²) on Pi_(m-1) is indefinite at each m in {1101,1240,1600}.
For each row there is an explicitly reproducible dyadic polynomial p
with continuous squared norm N>0 and the indicated strict Rayleigh bounds:

| m | lower bound | upper bound |
|---|---|---|
| 1101 | -35067/10^6 | -35066/10^6 |
| 1240 | -273/10^7 | -270/10^7 |
| 1600 | -23415/10^6 | -23414/10^6 |

This is an enclosure of a particular Rayleigh quotient, not an extremal
eigenvalue bracket. It supplies lambda_-(m,m-1)<0 at each listed degree; the positive
constant polynomial supplies a positive direction. It does not establish
a first negative degree or positivity at smaller degrees.

## Definitions and assumptions

The exact witness is sum C_ab P_a(x)P_b(y)/2^56 over a+b<=1599,
where P_a(1)=1 (replace1599 by m-1 for the other degrees). Coefficients are integers in the deterministic gzip JSON
artifact identified by SHA-256
`16d89f2c8600364aac3962c4164f0e0875c4fa866fc61269fd6f849e8f1fdad6`.
For m1240 the witness identity is
`1a9faac5677ac4dde63749a6acac38d95ee88a5082445e6ba6b59cc297d35e4e`;
for m1101 it is
`22913a3271c0cd826ff062a1f880c3539ef937b0141820dab381b53181662813`.
All three use the same checked conventions and coefficient denominator.
The m1600 proposal comes from the copied minimum solver's m1600 vector
`a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`.
Neither proposal accuracy nor an eigenvalue solver result is a premise.
All integrals use unnormalized dxdy, of mass four.

## Status by part

Overall: **PROVED (computer-assisted development)**, subject to the
arithmetic dependencies and artifact limitations below. Required Claude
audit remains pending; a supplementary independent run is complete.

The finite reduction, exact norm positivity, and strict negative energy
enclosures are the parts of this claim. No general spectral growth claim
or measured crossing is included here.

## Depends on

PD-T101/106's accepted signed cardinal/weight formula in the frozen
conventions; Legendre orthogonality and |P_a|<=1 on [-1,1]. FLINT exact
integers/rationals and Arb outward ball arithmetic are trusted for the
producer. The independent alternate arithmetic has its explicitly
documented standard IEEE dot-product model as an additional assumption.

## Proof and finite reduction

The producer rejects noninteger, zero, and out-of-triangle coefficients.
Thus its accepted artifact defines a nonzero member of Pi_1599. It
computes the exact positive rational

    N = sum 4 C_ab²/[2^112 (2a+1)(2b+1)].

The exact rational is manifested separately, with a small enclosing
interval near 1 in the receipt. Every exact node-table entry is enclosed
by Arb; each fixed-point center must pass an explicit error predicate.
All tensor contractions and coefficient-rounding errors are exact integer
or rational arithmetic. The signed weight kernel includes the exceptional
halved T_m coefficient. The proof of the global energy-error bound and
the strict sign predicate is in [certifier-design](../certifier-design.md).

That bound yields the producer's strictly negative enclosure near
-0.0234144. A separate checker loads the same exact dyadic polynomial,
builds new certified tables and evaluates the contractions with a proved
floating arithmetic error bound. Its negative interval lies inside the
conservative rational bracket in the Statement. Each therefore accepts
the sign independently of the eigensolver proposal.

Consequently Q_m(p²)<0 while N>0 at each listed degree. Exactness gives
Q_m(1²)=4>0.
These are respectively negative and positive directions of the same real
symmetric quadratic form on Pi_(m-1), proving indefiniteness at each listed degree. The minimum
of its continuous-normalized Rayleigh quotient is at most this negative
quotient, proving the claimed negative minimum. ∎

## Checks and evidence

Rules/input ad503cb0603fc017444b0aa732240981eefa4d24. Codex,
gpt-6.1-sol xhigh. The producer and independent checker ran in separate
agents and use distinct tensor arithmetic. See
[independent receipt](../independent-checks-witness.md), the small
evidence receipts, and [cold-storage manifest](../cold-storage.json).
The same producer/checker reduction is executed separately at1101
and1240, as the evidence receipts record; each interval is contained in
its displayed rational bracket. The m60 validation and m400 feasibility gate precede this acceptance.
Commands and source hashes are recorded in each receipt.

## Sources, limitations and next step

No external theorem, literature novelty or priority claim is added.
The witness and exact rational norm are regenerable large outputs, held
in session scratch pending Padua cold-storage delivery. Committed code,
small receipts, identities and the reduction remain in Git. Independent
reconstruction from the recorded command is possible; delivery to AC's
computer is not claimed. Required Claude audit must check the reduction,
error bounds, source/receipt hashes and independent arithmetic assumptions.
m1240 is the smallest even degree certified negative in this campaign.
This is a statement about completed coverage, not a theorem that every
earlier even degree is positive. The odd witness at1101 is a distinct
finite parity check, not an odd-degree first crossing.

## History

2026-11-05: finite m1600 negative float observation promoted to a
computer-assisted finite result only after producer and independent
strict negative enclosures. No old registry status is edited in WORK.
