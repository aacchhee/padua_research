# padua-lanczos-nonproduct-20261105 — span drift on genuinely non-product families

This file is written only by the topic orchestrator. Branch
`codex/padua-lanczos-nonproduct-20261105`; [draft PR #30](https://github.com/aacchhee/padua_research/pull/30).

## Status (2026-11-06): AUDIT (focused A3 diff after response01)

PR #24's all-degree drift separation (PD-T324) and closure growth (PD-T328/329) hold on SH_n, an affine image of a product measure. This topic seeks the same on families that are genuinely non-product. Directions are in [handoff 01](../topics/padua-lanczos-nonproduct-20261105/handoffs/01-work.md):

- **P1:** the triangle, with explicit Proriol–Koornwinder and Hahn/Krawtchouk OPs.
- **P2:** the disk, testing whether rotation invariance removes the effect.
- **P3:** non-affine perturbations of SH_n and their stability radius.
- **P4:** a structural criterion.
- **P5:** Padua.
- **P6:** exact scans.

Results currently have provisional IDs. The Claude substantive [audit 01](../topics/padua-lanczos-nonproduct-20261105/audit-01.md)
accepts every proof in scope and found no BLOCKING issue. It returned three MAJOR wording and record
findings, among them that the P3 family is moment-equivalent to SH_n through degree 2n+1. No shared registry or final allocation changed.

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
- **PROVED, covariance obstruction:** fixed covariance and distinct physical
  principal-axis angles do not bound absolute degree-two aggregate capacity
  on the specified thin-annulus family. This does not refute an all-degree
  BJ/best ratio criterion.
  [Scoped PD-N](../topics/padua-lanczos-nonproduct-20261105/theory/p4-covariance-capacity-obstruction.md).
- **MEASURED, P1/P2 probes:** exact low-degree triangle and radial-disk
  moments/bases/creators through8; the P1 final-source central-binomial chain
  is checked under BJ only. Restricted chains and sampled spectra do not
  close an all-source capacity recursion or prove a rate.
  [Triangle probe](../topics/padua-lanczos-nonproduct-20261105/theory/p1-continuous-creator-probe.md),
  [disk probe](../topics/padua-lanczos-nonproduct-20261105/theory/p2-03-finite-recurrence-probe.md).
- **MEASURED:**36 exact pilot rows on three finite measures, four rules and
  degrees2–4 agree between two arithmetic implementations. This is one
  worker's execution, with distinct-agent checking separate.
  [Finite record](../topics/padua-lanczos-nonproduct-20261105/theory/p6-finite-scans.md).
- **MEASURED:** H24_222 and D36x9 each have60 matched exact rows through16.
  Their N2 screens and the inherited T24 reanalysis are INCONCLUSIVE; D65 has degree8 pilots and an incomplete
  degree12 cost probe.
  [Screens](../topics/padua-lanczos-nonproduct-20261105/theory/p6-n2-screen.md).

- **PROVED, all-degree separation on non-affine-product measures
  moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight
  mode:** an explicit positive rank-two reweighting retains the original
  exponential BJ lower and polynomial full-source mirror upper for every
  n>=2 and 0<|eta|<1. Gram matrices, monic basis, creators, pivots, source
  scales and frozen response are eta-independent; only the ambient normal
  projector changes. Fixed eta is allowed; every eta_0<1 is sufficient,
  including eta_0=1/2. The ratio lower first exceeds1 at n=18. AC accepts
  this weaker variant; the n-independent perturbation is OPEN/deferred to a
  follow-up topic and is not a precondition for this PR.
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
accept the P3/P4/P5 proofs and terminal-block corollary, and reproduce the
completed Hahn16/disk8 finite evidence and separately launched disk16
alternating/pivot replay without unresolved findings. Compact endpoint tables
and N2 screens have distinct independent validation. The
completed Claude substantive audit accepted every proof in scope. The
[response](../topics/padua-lanczos-nonproduct-20261105/response-01.md) addresses its findings and AC's Q1–Q3 decisions; the material BJ chain qualifier receives focused diff
re-audit before preparation. Final scan-review coverage is in the dated records.

## Next step

`Claude (Opus 5.5 high): Continue codex/padua-lanczos-nonproduct-20261105.`
