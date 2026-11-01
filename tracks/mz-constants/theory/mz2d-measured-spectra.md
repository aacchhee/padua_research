# PD-T?mz2d-codex-03 — Finite two-dimensional Padua spectral measurements

ID kind: PD-T.
Aliases: D0 signed-Padua extension; rectangular tensor-CC spectral control.
Split from: none; this extends the finite scope of PD-T026 without changing it.
Split into: none. The exact finite enclosure record is separate.

## Statement

In the float64 computations at construction degrees
`m in {10,20,30,40,60,80,100}`, with `n=m-1`, the extreme signed-Padua
Gram eigenvalues and the matching rectangular tensor-CC control were
measured as tabulated below. Both full extreme coefficient vectors are
retained for every case. The m=10,20,30,40 Padua values agree with separate
direct moment-solve/nodal-Gram computations within 7.3e-14. This statement
is restricted to the actual finite computations, not all m.

## Definitions

Use the frozen [campaign definitions](../../../topics/padua-mz-2d-20261101/definitions.md):
even-checkerboard Padua nodes, signed interpolatory Lebesgue weights of
mass four, and orthonormal Legendre products on total degree at most n.
The control is `C_m tensor C_(m+1)` on the same rectangular coordinate
grids and the same total-degree space. Coefficients are ordered by total
degree ascending, x degree descending within each degree. The two extrema
are ordinary real symmetric-form eigenvalues, regardless of weight signs.

## Assumptions

Finite float64 NumPy 2.3.5/SciPy 1.17.0 arithmetic; Python 3.12.14;
single-thread BLAS environment; RNG seed 20261101. Kernel weights use the
discrete Chebyshev orthogonality construction verified in D1. Direct
crosschecks solve the unnormalized Chebyshev moment equations separately.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| Padua extrema and full vectors at seven m | MEASURED | d0-spectra.json; floating residuals only |
| Matching rectangular tensor controls and vectors | MEASURED | same artifact and finite scope |
| Direct formulation crosschecks at four old m | MEASURED | same developer executed a second formulation |
| Two negative Padua weights at each tested even m | MEASURED | grid entries and signed/absolute masses retained |

Candidate / claim disposition: none. No new mechanism or novelty claim is
made by this numerical record. The universal target PD-T028 remains OPEN.

## Depends on

Frozen definitions and D1's discrete Chebyshev kernel identity. Prior
PD-T026 supplies the old comparison table only; no asymptotic or positivity
result is assumed. Exact rational enclosures are a separate record and are
not required to interpret these floating observations.

## Checks

Producer: [mz2d_spectra.py](../code/mz2d_spectra.py).
Essential evidence:
[d0-spectra.json](../../../topics/padua-mz-2d-20261101/evidence/d0-spectra.json).
Command, full source commit, code and definition hashes, environment,
versions, seed, byte size, output hash and retention:
[d0-manifest.json](../../../topics/padua-mz-2d-20261101/evidence/d0-manifest.json).
Preparation and failed-run history:
[D0.md](../../../topics/padua-mz-2d-20261101/directions/D0.md).
The final output is 837344 bytes. No independent-agent rerun is claimed.

## Sources

The supplied prior Padua implementation and PD-T026 identify the finite
reproduction target. No external literature assertion is used as proof.

## Proof or evidence

| m | Padua minimum | Padua maximum | tensor CC minimum | tensor CC maximum |
|---:|---:|---:|---:|---:|
| 10 | .356191382630 | 1.634856614784 | .399433637548 | 1.005590885139 |
| 20 | .272233004958 | 1.723313731670 | .318138735560 | 1.004649255151 |
| 30 | .236705530370 | 1.757929855946 | .281916208023 | 1.004520681202 |
| 40 | .214817029467 | 1.778088623884 | .259849024875 | 1.004471120722 |
| 60 | .188593480489 | 1.802011149918 | .232861354600 | 1.004463819591 |
| 80 | .172730495887 | 1.816497914219 | .216153284009 | 1.004439734729 |
| 100 | .161748411019 | 1.826582423850 | .204382855645 | 1.004445390099 |

Maximum stored eigenpair residual norm is 1.30e-12, computed in floating
arithmetic. Direct moment-solve weights differ from kernel weights by at
most 1.96e-15; deterministic full-operator vector checks have relative
discrepancy at most 2.16e-12. These are diagnostics without rigorous
rounding control. Each listed Padua case has exactly two measured negative
weights at `(j,k)=(0,0),(m,0)`, corresponding to `(x,y)=(+/-1,1)`.

Padua uses matrix-free tensor contractions throughout. Large tensor
controls use four coordinate-parity dense blocks, maximum dimension 1275
at m100, after ARPACK upper-spectrum stagnation; full-vector nodal residuals
were checked. No 5050-by-5050 dense eigensolve was performed.

## Scope

No rigorous enclosure, universal positivity, upper threshold, monotonicity,
asymptotic order or eta convergence follows from this measurement record.
Floating residuals do not certify that a computed eigenpair is a global
extremum. The exact finite enclosure development is maintained separately.

## Open items

Independent actual rerun and audit. External archival at AC's designated
destination. All listed D0 runs are complete; no larger run is an implicit
proof obligation. PD-T028 and its universal two-dimensional questions
remain OPEN unless settled by separate proof records.

## History

2026-11-01: Codex, requested gpt-6.1-sol medium technical effort, rules/base
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`. Definitions and D1 kill criterion
were written and read before these numerical runs. Actual final run source
commit and uncommitted runner content identity are in the manifest.
