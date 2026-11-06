# Padua argmax bridge — WORK checkpoint, 2026-11-06

The independently checked exact global range is **2–40**, extended from
2–32. PD-T099 remains **OPEN** for the full all-degree statement. The
remaining bridge is41<=n<N_*, where the inherited eventual onset is
non-effective. No effective argmax n1 or Syvert campaign is claimed.

## What is proved

[Native finite certification](theory/native-finite-range.md) supplies
complete small exact certificates33–40, each accepted by the separately
authored frozen C++/GMP checker, with strict two-corner equality. The
37–40 block ran once per producer/checker case:

| n | Bound/corner leaves | Producer child CPU | Independent checker CPU |
|---|---:|---:|---:|
|37|316/2|298.236|897.769|
|38|320/2|378.753|1049.906|
|39|330/2|456.747|1195.500|
|40|350/2|565.354|1366.973|

All exits are0, partitions complete, and supplied bounds verified. The
unchanged checker also has36 corruption controls from the earlier block.
Original33–36 commands/costs and actual concurrency-qualified wall times
are retained in their receipts; wall time is not relabeled CPU time.

The analytic line now gives an [explicit near-phase model](theory/N1-round6-near-model.md)
with a fixed number of functions, retained cells and harmonic-block
terms, independent of degree. For rho<=1/2 and every n>=10^6,

    |S_n-M_near|<3/14000<1/4096.

The proof includes sinc-compatible finite-h endpoint rows, the single
periodic-jump correction, exact cutoff handling, regularized pole
variation, central entropy/logarithm subtraction and fixed-count
special rows. These are analytic inequalities, not fitted constants.
All component proofs received distinct mathematical reconstruction.
The earlier unchanged-error certificate is still specifically ruled
out for small budgets through10^6; the correction escapes that floor.
Its one-correction allowance is used.

The [two-phase edge defect](theory/N5-two-phase-defect.md) proves
lambda<S_n-1/2048 at all interior complementary vertical-edge centers,
n>=64 and inward rho<=1/2. Thus the new model yields the independently
reviewed [criterion](theory/near-edge-model-criterion.md):

    M_near<=Lambda_c+1/4096
    implies lambda<Lambda_c-107/3584000

for those classes at n>=10^6. The uniform model inequality itself is
unverified. In particular10^6 is a proved model-validity threshold,
not a proved maximum-theorem threshold.

## Practical finite side

The separate MPFR/Arb phase route now has complete independent
verification at known degrees17/24/32. Matched24/32 use the same
proved common local patch and unchanged arithmetic:

| n | Producer visits/leaves | Search CPU | Checker leaves/CPU |
|---|---:|---:|---:|
|24|2036/1020|363.070|1020/202.068|
|32|1980/992|619.327|992/382.569|

Both replays have zero failed or pending predicates. Historical17
uses1288leaves/109.450checkerCPU-s and a different, smaller local
patch. These observations do not prove a scaling law. The earlier
364-failure replay and repaired NaN arithmetic finding remain preserved.
See [overlap record](theory/N3-outward-overlap-r6.md) and exact source,
input, build/runtime, raw-output and exit identities in the short receipts.

A new [maximum-bootstrap reduction](theory/N3-bootstrap-corner.md)
uses the unknown true global maximum in PD-T227 and absorbs it at a
putative off-corner maximizer. Under W<=(3/4)n^4Lambda_c it permits an
inward half-phase patch without a prior global/corner norm ratio. Fresh
MPFR and separate GMP sweeps prove that energy premise for all127
integers2–128. This is a cover reduction, not pointwise local descent
before global closure. A strict complement cover still has to be
implemented/verified in its new mode. No existing acceptance is
retroactively reinterpreted, and the finite energy is not extrapolated
to the analytic n>=10^6 range.

## Gates and remaining work

| Gate | Current disposition |
|---|---|
|B0|PASS; exact native replay and deterministic pilot counts reconciled|
|B1|Finite diagnostic map complete; continuous extrema not certified|
|B2|Finite floating33/64/128 throughput/count scope passes; independent outward17/24/32 validates the method, not higher-degree scaling|
|B3|Near-domain model/error constructed; uniform maximum comparison, far phases and full-square closure OPEN|
|B4|Blocked: no actual effective argmax onset; no Syvert pack|
|B5|Unrestricted transport reformulates the target; specified structured classes fail only in their stated scopes|
|B6|No confirmed noncorner counterexample to PD-T099|

N4/N6 broad routes remain deferred after their specified class
obstructions. N5's true quarter-defect target is OPEN; its selected
phase-blind certificate alone is proved insufficient. More samples
cannot repair that particular limiting obstruction.

Next work is concrete: implement validated evaluation and comparison
of M_near, cover far phases/remaining classes and true-corner coherence,
and test the new bootstrap cover mode after independent implementation
review. The all-n energy premise remains separate. No next model
correction or large compute is inferred from the small near error alone.

## For the paper

The campaign extends exact corner-argmax certification through degree40,
constructs a uniform fixed-count near-phase primitive model, proves a
two-phase actual-lambda defect, and validates an independent outward
phase method at17/24/32. A maximum-bootstrap lemma enlarges the
permitted corner region under an energy condition verified through128.
The full all-degree maximum statement remains unresolved because the
model comparison, far-domain/corner coverage and effective meet-in-the-
middle onset have not been certified.

## Evidence and review

Source code, essential compressed trees and short acceptance records are
committed; full diagnostics/libraries remain local. The evidence index
is [evidence-manifest.json](evidence-manifest.json). Dependency setup
for the Arb checker is pinned in code/phase_checker/setup.py; no
third-party packages/headers are committed. Bulk physical archival is
pending and no Windows delivery is claimed. AC's temporary10MB allowance
and separate-topic cleanup instruction are recorded in LOG.

This is WORK, not merge readiness. Required Claude Opus5.5 xhigh audit
remains pending; Codex supplements do not replace it. Final IDs/shared
registry changes wait for audited preparation. Protocol history and
finding dispositions have canonical records in LOG/linked reviews.
