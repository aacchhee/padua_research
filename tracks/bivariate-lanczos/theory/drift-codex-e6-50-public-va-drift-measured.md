# PD-T?drift-codex-50 — Actual public polyrat V+A span and fitting measurements

ID kind: PD-T (provisional).
Aliases: E6-50; public V+A drift benchmark; actual upstream CGS2; upstream coordinate-order mapping; adversarial versus smooth polynomial fitting.
Split from: none; implementation confirmation and fit comparison extending the finite evidence of PD-N013 and PD-T051.
Split into: none. No final global identifier allocated.

## Statement

**MEASURED, finite execution scope.** In the recorded Python/NumPy/SciPy environment, actual unmodified `vandermonde_arnoldi_CGS` from polyrat 0.2.2, upstream commit `6903d7af9995c9d88e661fb229626696e00fdfba`, was executed on every member of the unchanged twelve-case `L2.BENCH` suite at its original maximal degree and on the frozen once-rounded rational T24/Q24 grids at degrees 12 and 16. Two upstream coordinate orientations and own L2 full-CGS2 dev, mirror, alt and adapt were evaluated on each case.

1. On all sixteen case instances, upstream input `[y,x]` produces columns entrywise equal to own L2 dev in this execution. Inspection and an exhaustive parent check through degree 47 map upstream `[y,x]` to campaign dev, including within-degree order. Upstream `[x,y]` maps to mirror with the campaign within-degree order reversed. Source inspection is an implementation fact, not an inherited published stability theorem.
2. On frozen rotpi4 at degree 24 and triangle at degree 20, upstream `[y,x]` has computed reference span gap respectively `0.004105469352253462` and `0.010163571396223751`, while maximum Gram error is at most `6.89e-15`. Reference normalized evaluation-matrix condition numbers are respectively approximately `3.78e3` and `1.01e2`. Rot0.3 and both rational grids also have resolved drift relative to their reported reference diagnostic scales. The complete values and own-selection comparisons are linked below.
3. A unit weighted-norm target selected post hoc from the reference polynomial span in the largest missing upstream `[y,x]` direction has relative training residual equal, to the displayed numerical precision, to those gaps. Actual upstream recurrence evaluation on the recorded 128 deterministic midpoint test points yields relative errors approximately `1.014e-3` and `1.569e-3` for the same two cases. By contrast, the independently fixed analytic target `exp(x+y)` has relative training and test errors at most `2.2e-15` on rot0.3, rotpi4 and triangle in these runs.

All statements are numerical observations for these pinned inputs and this execution environment. The adversarial target is represented numerically in a well-conditioned reference span, not by an exact symbolic polynomial certificate. No universal failure of polynomial fitting, all selections, or all reorthogonalization methods is asserted.

## Definitions

For positive sample weights w, the reference evaluation matrix contains `sqrt(w)` times all total-degree-at-most-n product-Chebyshev or Dubiner basis evaluations, column normalized before Householder QR. Inverse-rotated coordinates are used for the rotated-square Chebyshev references; triangle uses Dubiner. U denotes its QR orthonormal factor. W denotes the Householder orthonormal factor of the upstream computed basis Q. The measured gap is `||(I-WWᵀ)U||₂`, and orthogonality is `max|QᵀQ-I|`.

The common adversarial target for each case is `f=Uv`, where v is a leading right singular vector of `(I-P_upstream_yx)U`. Its weighted training norm is one; the saved v is applied to every compared method on that case. Training residual is `||(I-WWᵀ)f||₂/||f||₂`. Actual recurrence predictions use upstream `vandermonde_arnoldi_eval` and `np.linalg.lstsq` coefficients; target test values use the reference QR triangular solve. Test relative error divides the Euclidean error norm by the Euclidean norm of target values.

T24 is the rational grid `(i/12-1,j/12-1)` for integers i,j≥0 with i+j≤24, M = 325. Q24 rotates the 25×25 rational square grid by cosine 3/5 and sine 4/5, M = 625. Each coordinate is formed exactly using Fraction, then rounded once to binary64. The experiment therefore concerns that rounded measure. Test points are `(P[:128]+P[-128:])/2`.

## Assumptions

- Frozen existing seed, positive weights, points and maximal degree for every old L2 benchmark; n12 and n16 for the two additional grids.
- Binary64 upstream and own numerical routines in the manifested environment; `OPENBLAS_NUM_THREADS=1`.
- Actual upstream code is imported unchanged through the documented namespace-package adapter. This bypasses unrelated unavailable rational-solver package imports, and is not a full polyrat installation test.
- Reference conditioning and numerical rank are evaluated explicitly. `u*kappa` is a diagnostic error scale, not a rigorous forward-error enclosure. Raw outputs with a failed reference screen do not certify a distance to the exact polynomial span.
- Midpoint tests on triangle and rotated square stay in the respective convex domain. Tests on nonconvex L-shape and annulus can leave the sampling domain; their errors do not receive the same in-domain interpretation.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Actual upstream/own equality in sixteen cases | MEASURED | `upstream_yx_vs_dev_entry_max=0` in all case records; platform dependent |
| Order/selection mapping | Source inspection and executed check | Actual upstream `index.py`, `_update_rule`; parent assertions through n47 |
| Resolved span and adversarial fit discrepancies on stable references | MEASURED | Saved target coefficients, condition/rank diagnostics, actual upstream construction/evaluation |
| Smooth-target contrast | MEASURED | Fixed `exp(x+y)` companion run; no general smooth-function conclusion |

Candidate / claim disposition: Retained as finite implementation and fitting evidence; no novelty claim. Algorithmic equivalence is an IDEA disposition in `ideas-e6.md`, not a new negative theorem. The broad inference that observed drift makes every fit problem inaccurate was rejected by the smooth-target comparison.

## Depends on

PD-N013 and PD-T051 provide the earlier benchmark definitions and measured comparison context; they are not proof premises for these newly executed numerical observations. PD-N015 supplies the prior finite-scope warning against uniform safety claims for the tested selections. PD-T053 is relevant only if interpreting retained terminal closure defects as a bound on the maximum of adjacent-degree angles; it is not used to certify the direct reference gaps here.

## Checks

Producer code:

- [e6_benchmark.py](../code/drift/e6_benchmark.py).
- [e6_smooth.py](../code/drift/e6_smooth.py).

Rules/base SHA: `806cc7b4509fd93bae652f9545d32d95529f8281`. [Provenance manifest](../../../topics/padua-lanczos-drift-20261101/evidence/e6-provenance.json) records final producer/dependency hashes, output hashes/bytes, Python/NumPy/SciPy versions and actual commands. Commands from repository root include:

`OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --output topics/padua-lanczos-drift-20261101/evidence/e6-benchmarks.json`

`OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --sets T24 Q24 --output topics/padua-lanczos-drift-20261101/evidence/e6-frozen-grids12.json`

`OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --sets T24 Q24 --grid-degree 16 --output topics/padua-lanczos-drift-20261101/evidence/e6-frozen-grids.json`

`OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_smooth.py --output topics/padua-lanczos-drift-20261101/evidence/e6-smooth.json`

The root orchestrator reported an independently executed rotpi4/triangle rerun with matching results on 2026-11-01; its precise command/output and independent-check record are maintained by the root, not invented or self-certified here. Remaining independent coverage is narrower than the full twelve-set plus grid suite.

## Sources

Exact upstream URLs, commit/file hashes, source selection/order evidence, adapter and access attempts are in [external-code.md](../../../topics/padua-lanczos-drift-20261101/external-code.md). This record makes no newly inherited theorem claim from Hokanson, Brubeck–Nakatsukasa–Trefethen, or Zhu–Nakatsukasa. Existing literary comparisons are in L2-prior-art and literature records; paper/code attribution is kept separate from local numerical evidence.

BNT authors' public `chebfun/examples/linalg/VandermondeArnoldi.m` was retrieved and inspected. It is univariate; no multivariate parent rule exists there to benchmark. No MATLAB/Octave runtime is installed, so this example was not executed. No heavy runtime installation is required to establish the scope of the present multivariate polyrat record. Identifiable ZN author code was not located in the bounded search and was not run. Code-page proxy403 failures are not described as paper-fulltext access failures.

## Proof or evidence

The [direction record](../../../topics/padua-lanczos-drift-20261101/directions/E6.md) contains the numerical tables and full interpretation. Essential small outputs are [full suite](../../../topics/padua-lanczos-drift-20261101/evidence/e6-benchmarks.json), [n12 grids](../../../topics/padua-lanczos-drift-20261101/evidence/e6-frozen-grids12.json), [n16 grids](../../../topics/padua-lanczos-drift-20261101/evidence/e6-frozen-grids.json), and [smooth target](../../../topics/padua-lanczos-drift-20261101/evidence/e6-smooth.json). Together with the manifest these occupy about 278 KB; no third-party code or fulltext is vendored.

L-shape, annulus and cubic-checkerboard reference numerical ranks are respectively 493/496, 495/496 and 89/465 at the recorded tolerance. Disk and equispaced checkerboard references also fail the condition screen. Their raw gaps are noncertifying. Square's apparent gap is comparable to uκ, so no resolved square drift is asserted. Product controls tensor41, Padua48 and Chebyshev checkerboard have upstream gaps below 1.1e-14.

## Scope

This result confirms earlier own-code drift in an actual retrieved upstream implementation and distinguishes worst reference-polynomial approximation loss from accurate fitting of one fixed smooth function. It does not identify polyrat with ZN's unavailable implementation. Column order and coordinate orientation remain part of every implementation comparison. The cubic-checkerboard smooth test's enormous off-sample error is a separate severe-conditioning observation; its failed reference rank prevents attributing it to a trusted exact-span gap.

## Open items

- Independently rerun both n12 grids and any further consequential cases; full-suite independent execution is not implied by the reported two-case check.
- If desired, execute the actual univariate BNT example in an existing supported MATLAB/Chebfun environment; this is background coverage, not a missing multivariate BNT experiment.
- Obtain a verifiable ZN author-code URL, pin and inspect its source/order and execute it. Until then its actual-code comparison remains unperformed.
- Obtain AC's long-term cold-storage destination for external source archives. Current small evidence is retained; source URLs plus hashes permit retrieval subject to service availability.

## History

2026-11-01: Codex E6 developer, requested gpt-6.1-sol medium (exact runtime model/effort not independently exposed), measured actual upstream implementation and own comparisons at recorded base SHA. Root later requested a THEORY-template durable home; this file records the already measured scope without upgrading status or duplicating large tables. All Git and final-ID allocation remain with the orchestrator.
