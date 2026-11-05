# Independent phase checker — bounded implementation checkpoint

Rules/input `3dda890275a7599caa707b0fb8c0b6e6f6a80643`.
Developer: Codex, assigned Sol medium (runtime metadata not independently
exposed). Scope: separate arithmetic/checker development, not approval
of the producer and not an audit of its source. Only owned checker files
were written; no Git, shared gates, logs, handoffs or producer edits.

Status: **MEASURED** bounded replay. Full phase certificate and new-degree
claims remain **OPEN**. This supplement is not the required Claude audit.
The baseline and N3 novelty gates identify this as an implementation of
PD-T364, not a new mathematical mechanism.

Implementation: `code/phase_checker/`. FLINT 3.1.3 Arb balls, 160 bits;
denominator-free finite cosine polynomial and analytic derivatives.
No producer operations are imported, copied or linked. Official Debian
packages are fetched by pinned SHA-256 and extracted under local-output;
no third-party header or library is committed. See
[reduction/verification note](theory/phase-checker-reduction.md) for the
nonsmooth lemma, whole-orbit order, endpoint treatment, complete projected
center minimum, exact geometry, and inherited-only corner predicate.

Executed from repository root:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/setup.py
    sh topics/padua-argmax-bridge-20261105/code/phase_checker/build.sh
    python topics/padua-argmax-bridge-20261105/code/phase_checker/controls.py

The setup network action followed the cloud-runtime skill and read the
runtime/network-policy snapshot. All dependencies remain local. Build
requires system C++17/GMP headers and the ordinary system MPFR runtime.

Results are frozen in `evidence/phase-checker-calibration.json`:

- All three producer degree-17 positive sample predicates independently
  pass: far, corner-orbit plus all-center defect, and inherited-local
  corner plus all-center defect. Each candidate has pending regions and
  is correctly **not accepted** as a full certificate.
- Ten corruption controls are rejected: false completion, removed pending
  region, duplicate, ancestor overlap, missing root, pi shrink, inflated
  Lc lower threshold, false outside, false local radius, unknown predicate.
- Degree 17/24/32 independent Lc intervals overlap the inherited accepted
  finite-certificate threshold intervals. This is constant comparison
  only; this checker does not replay their Bernstein leaves or claim a
  complete overlap phase cover.
- Six independent 80-digit triangular-polynomial diagnostics agree in
  value and both phase derivatives, including (0,0), (pi,pi), (0,pi),
  generic phases and degrees through 32. These are numerical diagnostics,
  not replacements for source/mathematical inspection.
- Bounded per-box CPU seconds: n17 .0565, n24 .1249, n32 .3962,
  n33 .4757. Each call includes interval and center boards, projected
  profiles and a redundant zero-phase Lc board. These costs are local
  measurements, not whole-cover or asymptotic forecasts.

Bulk output: `local-output/argmax-bridge-20261105/phase-checker/controls-full.json`
and `n17-incomplete-replay.json`. The committed summary pins inputs and
checker source hashes. Larger artifact archival remains pending AC's
Padua cold-storage workflow; none is necessary for a new proof claim,
because no such claim is made.

The first bounded prototype is practical for leaf diagnostics. Its
finite-polynomial O(n³) kernel and full projected profiles may dominate
large-degree full covers. No blind degree-128 cover is authorized by
these timings; optimize only after the first source/proof inspection.
Potential later improvements are cached constants, skipping profiles
when the far predicate already passes, or a separately implemented Arb
quotient with a rigorous finite-polynomial collision fallback. None has
been implemented or measured here. The new kappa=1/12500 corner proposal
is not assumed or used.

Runs needed: independent mathematical/source review; a full outward
producer cover and whole-leaf independent replay; complete overlap
phase covers at 17/24/32 if demanded before any new degree; any new
corner patch requires its separate exact checks and independent proof.

## Follow-up at c000899 — R1 provenance correction

The preceding checkpoint and `phase-checker-calibration.json` are preserved
as historical bounded mathematics evidence. Review finding **R1** identified
that the original CLI loaded a fixed local shared library without binding it
to source/build identity and reread the candidate when hashing. Those are
real provenance defects; the original receipt cannot supply that stronger
binding retrospectively.

The revised CLI reads candidate bytes once, hashes that same immutable byte
snapshot, and parses it with duplicate-key and nonfinite-number rejection
(including exponent overflow). It rebuilds the kernel in a unique directory
for each check. The source snapshot is preprocessed into a pinned translation
unit, which is compiled with recorded flags and compiler/tool identities.
Headers, compiler runtime dependencies, arithmetic library input closure,
linked dependencies, actual loaded mappings, and the resulting binary are
hashed. Header/tool/dependency changes during the build are rejected; Python
source and binary changes during replay are rejected. No previously existing
`libphase_checker.so` is accepted. Full manifests remain in local receipts;
`evidence/phase-checker-provenance.json` pins the focused regressions.

Executed only the new focused suite:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/provenance_controls.py

It rejects duplicate/nested-duplicate keys, NaN, Infinity and 1e400; checks
snapshot identity after replacing the original file; and launches two
parallel fresh builds with distinct directories. Both independently replay
the original positive n17 far sample and correctly remain unaccepted as
full certificates. The unchanged mathematical campaign was not rerun merely
for metadata. Review disposition is **FIX IMPLEMENTED; independent review
pending**, not self-approved.

The fixed-instance local guard now additionally permits only degrees
33,64,128, phase square 1/128, and the exact rational quadratic-distance
inequality with kappa=1/12500. This relies on the published finite-instance
theorem and corrected independent receipt
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`.
It is not a caller-provided boolean. Every source pin in that receipt must
resolve to its exact bytes. The pre-status-change prose is retrieved from
published commit `c000899f3fb10d6ba0f1725341a045fe11ec943a`; its old pin is
verified rather than ignored. Guard regressions reject n17/32/129 and
phase-square excess. No common all-degree kappa is assumed. A full n17
outward candidate remains awaited and must be checked in its entirety.

## Actual complete n17 replay — not accepted

The outward producer finished 2572 visits / 1288 leaves / zero pending.
Its exact compact plain candidate is
`local-output/argmax-bridge-20261105/N3/outward-full-n17-r3/n17-phase-compact.json`,
SHA-256 `64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`.
Only ignored numeric diagnostic leaf bounds were removed by the producer's
recorded projection. Every root/path/kind and all nonleaf metadata remain.

Executed once, with no leaf cap:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check.py local-output/argmax-bridge-20261105/N3/outward-full-n17-r3/n17-phase-compact.json --output local-output/argmax-bridge-20261105/phase-checker/n17-full-r3-replay.json

The revised provenance-bound checker checked **all 1288 leaves**, taking
60.60368947 CPU seconds. **Acceptance is false**: 924 leaves pass, 364
fail the independent enclosure predicates (184 far and 180 corner-orbit
plus defect). All 28 inherited-local leaves and 32 outside leaves pass.
This is a failure of enclosure strength on broad boxes, not a mathematical
counterexample or an accepted overlap phase certificate. For example root 0,
path 01010 has independent S upper 12.86916394136224 versus Lc lower
8.6179478249936, so strict far comparison cannot be certified by this kernel.

The 570121-byte full replay receipt is local, SHA-256
`021ded297f360245fb30a884efe7a3670321e4a736c22873abaa6079cc0257d7`.
The short committed summary is `evidence/phase-checker-full-n17.json`.
It records fresh build/input identities and all leaf counts. No candidate
or arithmetic source was silently modified to pass. This decisive first
complete overlap test identifies the next obligation: a tighter independent
Arb formula or rigorously validated internal leaf refinement, followed by
complete replay and source review. A degree-128 whole-cover check is not
justified by this failed degree-17 enclosure calibration.
