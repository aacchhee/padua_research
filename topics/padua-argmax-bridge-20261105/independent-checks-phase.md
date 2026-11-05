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
