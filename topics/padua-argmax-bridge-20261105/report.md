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

Round7 extracts both logarithmic coefficients of this unchanged model.
Writing r2=alpha^2+beta^2, their gaps below the corner coefficients are
at least47r2/(48pi^2) for log^2 n and r2/(24pi^2) for log n. The
remaining term is uniformly bounded, with no small numerical bound yet.
The logarithmic coefficient has no linear phase cusp; a finite-degree
cusp can remain in the residual. See the [coefficient theorem](theory/N1-round7-coefficients.md)
and the exact [residual comparison obligation](theory/N1-round7-comparison.md).

Round8's [branch helper](theory/N1-round8-jumps.md) writes that residual
increment as a continuous bookkeeping increment plus an error<9/(2n).
It includes every strip seam, special-row approximation, collision mark
and half-angle cutoff; at n>=10^6 it leaves more than1/40000 for
the continuous comparison. The [remaining modulus](theory/N1-round8-modulus.md)
can require fractional/entropy terms as well as the finite-degree cusp.
No constants closing that modulus or C1 are proved. This is an analytic
decomposition of the unchanged model, with no additional correction.


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
before global closure. A strict complement cover requires the explicit
new mode and independent verification recorded below. No existing acceptance is
retroactively reinterpreted, and the finite energy is not extrapolated
to the analytic n>=10^6 range.

The new [analytic energy bound](theory/N3-uniform-energy-r8.md), independently
reviewed, gives for all n>=32

    W_n <= n^4[(21/32)Lambda_c+1,500,000,000(1+log(n+1))].

It proves the unchanged3/4 premise when log n>=128,000,000,000. This
explicit energy onset is far beyond a practical finite bridge and is
not an argmax onset. The intermediate energy range129<=n<ceil(exp(128000000000))
remains OPEN. The finite certifier is deliberately still restricted to
its independently verified2–128 premise.

The [explicit bootstrap certificate mode](theory/N3-bootstrap-cover-r8.md)
now has independent mathematical/source acceptance, including exact
boundary, malformed-partition, premise and strict-defect controls. Its
first known-degree n32 producer completes364leaves in222.813childCPU-s,
versus992leaves/620.093CPU-s in round6. The first independent replay checks all364leaves but rejects20bootstrap
leaves because its projected-defect lower enclosure is zero. All other
344leaves pass. TotalcheckerCPU136.175s, no cap or source/input change.
This is a failed sufficient enclosure, not a counterexample or accepted
new-mode certificate. No retry or new degree is counted; see the
[failed replay](independent-checks-bootstrap-r8-n32.md).

Round9's separately reviewed Arb refinement retains each pair's
nonnegative/opposite-sign defect lower bound before profile aggregation,
and preserves the old natural bounds. The original candidate then
passes364/364leaves,0failed/0pending,exit0 on the changed backend, in
139.405409totalcheckerCPU-s. Sources/input/supervisor and254build/runtime
identities are unchanged after replay. The first failed receipt remains
preserved; no producer rerun or tree change occurred.
[Accepted replay](independent-checks-phase-r9-n32.md).

| Known n32 mode | Leaves | Producer child CPU | Independent checker total CPU | Outcome |
|---|---:|---:|---:|---|
|Round6 pointwise patches|992|620.093|383.663|ACCEPTED|
|Round8 bootstrap, old Arb defect|364|222.813|136.175|20 rejected predicates|
|Same bootstrap candidate, round9 Arb defect|364|222.813 reused run|139.405|ACCEPTED|

The accepted bootstrap case uses about2.8times less combined CPU and
63percent fewer leaves than round6 at this single degree. This is a
known-degree comparison, with no higher-degree complexity assertion.


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
and assess higher-degree cost only under a fresh bounded gate after
the accepted bootstrap calibration. The all-n energy premise remains separate. No next model
correction or large compute is inferred from the small near error alone.

## For the paper

The campaign extends exact corner-argmax certification through degree40,
constructs a uniform fixed-count near-phase primitive model, proves a
two-phase actual-lambda defect, and validates an independent outward
phase method at17/24/32. A maximum-bootstrap lemma enlarges the
permitted corner region under an energy condition verified through128;
its explicit mode now has a full separate known-degree n32 acceptance.
Both near-profile logarithmic coefficients favor the corner, and all
branch artifacts fit a small proved allowance. The continuous residual
comparison remains unresolved.
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
