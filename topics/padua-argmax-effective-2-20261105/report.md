# Effective Padua argmax, phase 2 — development report

Branch `codex/padua-argmax-effective-2-20261105`, [draft PR25](https://github.com/aacchhee/padua_research/pull/25).
Rules read at integration `ed21cc0bf205549936fccde90244a291bc6de324`,
input topic head `50cc7effde11fc9cc875cf2b8275a76458c75152`,
fetched/merged main `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`.
Mathematics used AC-requested Astra ultra; code/replays used Sol medium;
a distinct Astra high agent supplied the mathematical supplement.
Parent serving metadata is unexposed. Required Claude audit remains PENDING.

## Main result: H3 has an explicit physical n^-2 radius

For every n>=2, both parity-correct nonnode corners have strict descent for
inward increments 0<H=h_x+h_y<=10^-11/n²:

    lambda_n(c+h)<=Lambda_c(n)−n² Lambda_c(n) H/16 < Lambda_c(n).

The [radius proof](theory/corner-n2-local-radius.md), provisional T07, uses
separate [energy T05](theory/corner-weighted-energy.md),
[global norm T06](theory/corner-global-norm-ratio.md), existing PD-T251 slopes
and PD-T227's aggregate inequality. W_n<=10^10 n^4 Lambda_c and
Lambda_n<=27500 Lambda_c are explicit. The scalar inequality permits
individual cardinal sign changes, so PD-N085 is respected. The small constant
is not a claim that the practical H1 corner zone or runtime gate is solved.
The old n^-6 radius can be larger at moderate degrees and remains available.

These are written analytic PROVED statements, with supplementary independent
reconstruction complete and required Claude audit pending. They add no global
finite degree or effective all-degree threshold.

## H1 and noncorner defect

[Exact phase structure T01](theory/phase-structure.md) verifies lambda=S−Delta
with full reflection defect, endpoint multiplicities, polynomial collisions,
physical class domains and a sufficient three-region certificate reduction.
Projected Qv/Qh provide lower bounds on Delta, not equality with it.

[Defect T04](theory/defect-radius-extension.md) proves Delta>=1/8192 for every
n>=48, every admissible noncorner odd center and rho<=1/10. It enlarges the
inherited 1/64 radius with separately checked finite-line constants. The bound
still needs to beat a uniform upper bound for the primitive excess on the
relevant region. It is not a new global argmax certificate.

The [bounded interval-box pilot](box-pilot.md) visited2000 boxes at each of
n17/32/64/128 with unresolved frontiers880/902/774/802. At n256 it reached
the60-CPU-second budget after802 boxes with308 unresolved. No floating cover
completed. The diagnostic margin is not an outward error bound. A fast O(n²) point kernel and O(n³) projected-profile computation
alone do not establish a box-count growth law or exact certificate throughput.
A separate phase-box checker and corruption controls remain to be built.

## H2 boundary profile and the scoped failed trial

[Boundary T03](theory/profile-boundary-cotangent.md) gives an exact shifted
cotangent sum on all four closed phase-diamond edges, including removable
endpoints, and an explicit profile with absolute error at most
7/(12[n(n+1)]²). At the midpoints S_n=L_{n(n+1)} exactly, with its inherited
explicit one-dimensional remainder.

[N01](theory/profile-leading-only-obstruction.md) consequently rejects only
profiles a(alpha,beta)*b_n: a vanishes at a midpoint whereas S_n grows like
(4/pi)log n. This is an analytic obstruction to that specified trial, not
refutation of the original unspecified H2 proposal. The full-diamond profile,
its uniform remainder and a proved explicit N1 remain OPEN. No full-diamond
A3 fit was performed. Boundary accuracy cannot be used as an interior bridge.

## Gates, completed runs and independent checks

[All gate verdicts](gates.md), [structural/A0 detail](gates-structural.md),
[H1 attempt](attempts/H1.md), [H2 attempt](attempts/H2.md),
[H3 attempt](attempts/H3.md) retain original criteria and failed/deferred routes.
A0 confirms the coarse log-degree scale near300000 under hypothetical measured
C values; the sharpened geometric alternative is preserved without claiming a
proved global C. A4 cannot yet compare an H1 range with a full-diamond N1.

Fresh native producer/checker replays at n17/n24 independently accept both
regenerated and committed certificates, matching every mathematical field and
frontier. [Replay record](independent-replay.md). This is reproduction, not a
new degree or a fresh corruption-control suite.

Exact Fraction checks at n3–6 test3544 cardinal identities,172 weighted
multisets and collision/zero/endpoint cases. Compiled point probes evaluate
5240 physical samples across eight degrees. The all-class projection probe
visits1,198,029 admissible center-phase samples at n48/96/192. Positive sampled
margins and roundoff-sized corner excesses provide neither continuum bounds
nor a confirmed counterexample. Receipts and exact reproducible commands are
in [phase-probe.md](phase-probe.md) and [projection-probe.md](projection-probe.md).

The [independent Astra supplement](independent-math-checks.md) reconstructs
T01–T07/N01, including the new full-orbit formula, and executes a separately
authored70-digit polynomial checker at n2–8. It records final reviewed hashes
and no unresolved mathematical finding. It explicitly does not complete the
full-registry novelty/protocol audit or replace the required Claude audit.

## Exact remaining gap

PD-T099 remains **OPEN**. The certified global range is still exactly2–32;
phase2 certifies no n>32. The inherited eventual N_* remains non-effective.
The unknown bridge remains33<=n<N_*, with no explicit full-diamond N1 supplied
here. Local H3 and boundary H2 are supporting results, not cases of the global
statement; they do not turn PD-T099 into PARTIAL.

Next mathematical work: practical verified H1 cover/predicates and independent
checker; a compatible full-diamond H2 expansion with explicit remainders; then
A4 bridge arithmetic and continuous A5 coverage. R3 is retained/deferred with
its existing finite comparisons; no new E-C mechanism or R3 run was attempted.

## For the paper

Subject to the required audit, the Padua Lebesgue-function paper can add an
explicit all-degree physical n^-2 strict corner-descent neighborhood, aggregate
energy/global-norm bounds, a wider uniform noncorner defect neighborhood, and
an exact phase-boundary cotangent profile with a uniform vanishing error. It
must retain the global corner-argmax assertion as OPEN beyond the finite
certified range and the inherited non-effective eventual theorem. No priority,
submission or new literature-transfer claim is made.

## Protocol and storage limits

Scientific registrations remain provisional; permanent reservation is in
[ALLOCATIONS.md](ALLOCATIONS.md). [Literal shared-record proposals](proposed-record-changes.md)
are not applied to merged state. Complete prospective-gate timing qualifications
for the energy child and IDEA358 wrapper are explicitly retained in H3/H2 gate
records for Claude's disposition. No retrospective full compliance is claimed.

Code and small essential receipts are committed. Bulk replay/probe outputs stay
under local-output/argmax-effective-2-20261105 pending physical delivery to AC's
Padua cold storage; no Windows transfer or durable retention is claimed. All
scientific proofs above are analytic and do not depend on unique local raw
bytes. Generated measurements remain reproducible at their pinned source
identities, while rerunning does not reproduce old timing bytes.
