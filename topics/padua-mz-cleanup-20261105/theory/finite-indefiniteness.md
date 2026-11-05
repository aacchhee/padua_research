# PD-T376 — explicit finite signed Padua indefiniteness

ID kind: PD-T. Aliases: dyadic negative energy witness; finite loss of
positive definiteness. Split from: C1 constructive finite certification.
Split into: none. Frozen definitions are those of the original 2D topic.

## Statement

For the signed interpolatory Lebesgue Padua rule on the even checkerboard,
the quadratic form p -> Q_m(p²) on Pi_(m-1) is indefinite at each m in {1101,1240,1600}.
For each row there is an explicitly specified dyadic polynomial p
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

The exact witness is sum C_ab P_a(x)P_b(y)/2^56 over a+b<=m-1,
where P_a(1)=1. Coefficients are integers in compact JSON carried in gzip containers.
The m1600 artifact is identified by SHA-256
`16d89f2c8600364aac3962c4164f0e0875c4fa866fc61269fd6f849e8f1fdad6`.
For m1240 the witness identity is
`1a9faac5677ac4dde63749a6acac38d95ee88a5082445e6ba6b59cc297d35e4e`;
for m1101 it is
`22913a3271c0cd826ff062a1f880c3539ef937b0141820dab381b53181662813`.
The gzip hashes above identify the original staged containers. Container
bytes are environment-specific: different Python/zlib builds may compress
the same JSON differently. Portable payload identities below hash the
exact decompressed UTF-8 JSON bytes without reserialization. The compact
producer encoding was also checked byte-for-byte.

| m | Decompressed JSON SHA-256 | Bytes |
|---|---|---:|
| 1101 | `71bcbc676272a19765c2e859c9116856ae7b5e2680eee332d042f4a3cf62e19e` | 9956905 |
| 1240 | `899c680efe9fdd6ea013ce28e906bb273fbcc10633ee949df0fc47403abd9b3d` | 12801774 |
| 1600 | `6bcf531c197b828cd67e1e3518a5404c6aa9bffeb456a9d26ee1b7ee96b1ec0f` | 20861351 |

[Payload identity sidecar](../evidence/witness-payload-identities.json)
also records m60/m400. No accepted witness or certificate was replaced.

All three use the same checked conventions and coefficient denominator.
The m1600 proposal comes from the copied minimum solver's m1600 vector
`a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`.
Neither proposal accuracy nor an eigenvalue solver result is a premise.
All integrals use unnormalized dxdy, of mass four.

## Status by part

Overall: **PROVED (computer-assisted development)**, subject to the
arithmetic dependencies and artifact limitations below. Claude
[audit-01](../audit-01.md) accepted the finite reduction and stated scopes;
[response-01](../response-01.md) records the provenance/wording response.
Supplementary independent executions are complete.

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
Thus its accepted artifact defines a nonzero member of Pi_(m-1) at each listed degree. It
computes the exact positive rational

    N = sum 4 C_ab²/[2^112 (2a+1)(2b+1)].

The exact rational is manifested separately, with a small enclosing
interval near 1 in the receipt. Every exact node-table entry is enclosed
by Arb; each fixed-point center must pass an explicit error predicate.
All tensor contractions and coefficient-rounding errors are exact integer
or rational arithmetic. The signed weight kernel includes the exceptional
halved T_m coefficient. The proof of the global energy-error bound and
the strict sign predicate is in [certifier-design](../certifier-design.md).

That bound yields a strictly negative producer enclosure at each listed
degree, as the three corresponding receipts record. A separate checker loads the same exact dyadic polynomial,
builds new certified tables and evaluates the contractions with a proved
floating arithmetic error bound. For the checker, reconstruct the outward
energy interval from `q_center +/- q_absolute_error` and divide by the
positive exact continuous norm (or its outward enclosure). That quotient
interval lies strictly inside the corresponding rational bracket in the
Statement. Its default printed `q_enclosure` loses display digits and,
at m1240/1600, does not by itself imply the tighter rational bracket.
Each path nevertheless accepts
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
The same producer/checker reduction is executed separately at 1101
and 1240, as the evidence receipts record; each interval is contained in
its displayed rational bracket. The m60 validation and m400 feasibility gate precede this acceptance.
Commands and source hashes are recorded in each receipt.

## Sources, limitations and next step

No external theorem, literature novelty or priority claim is added.
The specific witness and exact rational norm files are large outputs, held
in session scratch pending Padua cold-storage delivery. Committed code,
small receipts, identities and the reduction remain in Git. Independent
regeneration of a proposal and a new accepted certificate is possible from
the recorded commands; identical witness bytes across numerical-library
versions are not guaranteed. The staged original bytes retain their own
identities. Claude audit-01 independently regenerated different accepted
witnesses and checked the stated reduction/brackets; it did not retrieve
the developer's large package. Delivery to AC's computer is not claimed.
m1240 is the smallest even degree certified negative in this campaign.
This is a statement about completed coverage, not a theorem that every
earlier even degree is positive. The odd witness at 1101 is a distinct
finite parity check, not an odd-degree first crossing.

## History

2026-11-05: finite m1600 negative float observation promoted to a
computer-assisted finite result only after producer and independent
strict negative enclosures. No old registry status is edited in WORK.
