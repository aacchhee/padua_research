# padua-lanczos-nonproduct-20261105 — span drift on genuinely non-product families

This file is written only by the topic orchestrator. Branch
`codex/padua-lanczos-nonproduct-20261105`; [draft PR #30](https://github.com/aacchhee/padua_research/pull/30).

## Status (2026-11-05): WORK

PR #24's all-degree drift separation (PD-T324) and closure growth (PD-T328/329) hold on SH_n, an affine image of a product measure. This topic seeks the same on families that are genuinely non-product. Directions are in [handoff 01](../topics/padua-lanczos-nonproduct-20261105/handoffs/01-work.md):

- **P1:** the triangle, with explicit Proriol–Koornwinder and Hahn/Krawtchouk OPs.
- **P2:** the disk, testing whether rotation invariance removes the effect.
- **P3:** non-affine perturbations of SH_n and their stability radius.
- **P4:** a structural criterion.
- **P5:** Padua.
- **P6:** exact scans.

Results currently have provisional IDs; the substantive independent Claude
audit follows development. No shared registry or final allocation changed.

- **Verification:** N0 PASS: six SH cases, 88 symbolic identities and44 exact
  triangle/rotated-grid prefix rows match the predecessor evidence in an
  actual fresh replay. [Record](../topics/padua-lanczos-nonproduct-20261105/n0-replay.md).
- **PROVED, admissions:** triangle lattices and positive rational reweightings,
  continuous radial disks and the324-point rational D36x9 grid, and an
  n-dependent positive rank-two reweighting of SH are genuinely non-product.
  Exact injectivity/oversampling scopes are in the [triangle](../topics/padua-lanczos-nonproduct-20261105/theory/p1-triangle-admission.md),
  [disk](../topics/padua-lanczos-nonproduct-20261105/theory/p2-01-family-admission.md)
  and [SH weight](../topics/padua-lanczos-nonproduct-20261105/theory/p3-01-high-mode-weight-admission.md) records.
- **PROVED, model:** the positive-weight finite normal quotient, exact
  atomless capacity as a maximum of the pointwise response spectral norm,
  and moment-preserving capacity-transfer theorems are written. Finite
  cubature moment matching does not identify arbitrary-source capacities.
  [Weighted model](../topics/padua-lanczos-nonproduct-20261105/theory/p4-weighted-normal-quotient.md),
  [atomless model](../topics/padua-lanczos-nonproduct-20261105/theory/p4-continuous-capacity.md),
  [transfer](../topics/padua-lanczos-nonproduct-20261105/theory/p4-moment-capacity-transfer.md).
- **MEASURED:**36 exact pilot rows on three finite measures, four rules and
  degrees2–4 agree between two arithmetic implementations. This is one
  worker's execution, with distinct-agent checking separate.
  [Finite record](../topics/padua-lanczos-nonproduct-20261105/theory/p6-finite-scans.md).
- **MEASURED:** fresh reweighted-triangle H24_222 scan has60 matched exact
  rows through16. Its N2 interval screen and the inherited T24 reanalysis
  are both INCONCLUSIVE; disk8 is matched and disk16 remains in progress.
  [Screens](../topics/padua-lanczos-nonproduct-20261105/theory/p6-n2-screen.md).

- **PROVED, all-degree separation:** an explicit n-dependent rank-two
  positive reweighting of SH is not affine-product and retains the original
  exponential BJ lower and polynomial full-source mirror upper for every
  n>=2 and0<|eta|<1. Fixed eta is allowed; eta_0(n)=1/2 is a uniform sufficient
  certificate. The weight frequency changes with n, so this is not a fixed
  smooth-density/node-geometry theorem.
  [Moment/witness proof](../topics/padua-lanczos-nonproduct-20261105/theory/p3-02-exact-moments-creators.md),
  [capacity/radius proof](../topics/padua-lanczos-nonproduct-20261105/theory/p3-03-uniform-capacity-radius.md).
- **PROVED, Padua contrast:** for every m>s>=1, positive Chebyshev Padua
  measures are genuinely non-product and both BJ and mirror obey
  sqrt(ceil(s/2))<=kappa<=2sqrt(2)(s+1)(N_s-1). BJ/best therefore has a
  polynomial upper for every finite collection of fixed admissible rules.
  [Admission](../topics/padua-lanczos-nonproduct-20261105/theory/p5-01-padua-admission.md),
  [capacity](../topics/padua-lanczos-nonproduct-20261105/theory/p5-02-padua-polynomial-capacity.md).

The continuous triangle/disk rate questions remain OPEN after the N3
recursion attempts redirected to P4. Scope and chronology limitations are
retained in the theory records and topic log. Distinct supplementary checks
are underway; the required Claude audit has not yet occurred.

## Next step

`Codex (gpt-6-astra high): Continue codex/padua-lanczos-nonproduct-20261105.`
