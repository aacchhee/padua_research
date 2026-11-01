# padua-lanczos-drift-20261101: finite-precision span drift in bivariate Lanczos (PR #15)

This is the topic's results file; only the topic orchestrator writes it. Branch `codex/padua-lanczos-drift-20261101`, draft PR #15. It was migrated into the repository on 2026-11-01 under the repository-only results rule of draft PR #16. The source was the orchestrator's local working track of the same name, revised here.

All IDs are provisional (`PD-T?drift-codex-NN`, `PD-N?drift-codex-NN`, `IDEA?drift-codex-NN`). The permanent reservations are PD-T136–155, PD-N062–071, IDEA-246–285 and LIT-445–459. Theory records are in `tracks/bivariate-lanczos/theory/drift-codex-*.md`, code in `tracks/bivariate-lanczos/code/drift/`, and the topic files in `topics/padua-lanczos-drift-20261101/`.

## Status (2026-11-01): WORK → AUDIT

- **Development.** Codex developed the campaign (scientific source `b09e1db`).
- **Audit-01.** The Claude audit (Opus 5.5 xhigh) of `36c93794` returned CHANGES REQUIRED: 0 high, 10 medium and 32 low findings, with no PROVED or MEASURED claim refuted. See [audit-01](../topics/padua-lanczos-drift-20261101/audit-01.md).
- **Response-01.** By AC's redirection, Claude is the developer of the fixes. Because Claude is also the auditor of record, a Codex re-audit is required before PR preparation. See [response-01](../topics/padua-lanczos-drift-20261101/response-01.md).
- **Integration.** PR #14 merged first (main `e0d9e3d`). It was merged into this branch without rebasing, and the ledger and crosswalk text of both topics is kept.

## Meaningful results, at their stated scope

| Record | Status | Result |
|---|---|---|
| [PD-T?drift-codex-30](../tracks/bivariate-lanczos/theory/drift-codex-e5-30-padua-positivity-radius-upper-bound.md) | PROVED, analytic (audit: confirmed) | For the named Padua certificate P_n, ρ_n = O(n⁻⁵), with limsup n⁵ρ_n ≤ 20√2π⁴/9. The witness is ζ_n = (cos(π/n + a/n⁴), cos(π/(n+1) + a/n⁴)), a = 20π³/9. This settles PD-T075(U1) only. A response-01 remark (re-audit pending) sharpens the constant to 2√2π⁴(10−2√2)/9 ≈ 219.5. PD-T075(U2) and PD-T056(G) remain OPEN. |
| [PD-T?drift-codex-31](../tracks/bivariate-lanczos/theory/drift-codex-e5-31-explicit-square-root-spread-family.md) | PROVED (audit: confirmed) | An explicit square n = 1 four-atom split gives spread ≤ √(6ε) and a √ε lower bound for residual γε, γ < 1/3. This is reading (E) only. |
| [PD-T?drift-codex-01](../tracks/bivariate-lanczos/theory/drift-codex-e1-01-span-derivative.md), [-02](../tracks/bivariate-lanczos/theory/drift-codex-e1-02-rational-span-bounds.md) | PROVED (audit: confirmed) | The normal-quotient first-order span derivative for aggregate injections, plus rational node, HS and row bounds (spectral output). |
| [PD-T?drift-codex-03](../tracks/bivariate-lanczos/theory/drift-codex-e1-03-scalar-operation-bridge.md) | PROVED, formal model (audit: confirmed) | The first-order normal map of a declared scalar CGS2 graph. Dot, coefficient and norm errors lie in the polynomial kernel. It makes no IEEE claim. |
| [PD-T?drift-codex-04](../tracks/bivariate-lanczos/theory/drift-codex-e1-04-finite-aggregate-separation.md) | PROVED, computer-assisted (audit: confirmed with corrections) | A degree-12 aggregate separation: T24 κ ratio > 1126 (BJ against pivot), rational rotated Q24 > 11.72 (BJ against alt, Urow certificate). The original KHS-only test is INCONCLUSIVE (squared ratio 62.16 < 100). There is an exact rotQ24 pivot tie at (2,1); T24 has none. |
| [PD-T?drift-codex-05](../tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md) | MEASURED | The full scalar-CGS2 factor-10 comparison is INCONCLUSIVE. The post-hoc squared ratios are > 7 (rotQ24) and > 800 (T24). |
| [PD-T?drift-codex-10](../tracks/bivariate-lanczos/theory/drift-codex-e3-10-polynomial-span-certificate.md), [-11](../tracks/bivariate-lanczos/theory/drift-codex-e3-11-selection-criterion.md) | PROVED (11: fixed degree) | An a posteriori computed-polynomial span certificate, and a filtered fixed-degree selection criterion. Uniform polynomial safety is OPEN. |
| [PD-N?drift-codex-15](../tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md) | PROVED, scoped negative | A fixed-degree projection-only closure obstruction on ten nodes. Response-01 rescopes it (re-audit pending). The original PD-T055 is OPEN. |
| PD-N?drift-codex-14 | Quantifier refutation | In response-01 it is handled as an IDEA disposition rather than a PD-N (re-audit pending). |
| [PD-N?drift-codex-32](../tracks/bivariate-lanczos/theory/drift-codex-e5-32-failed-negative-witness-paths.md) | PROVED, scoped negative | Three failed negative-witness paths. Case 3 rejects only the eventual-witness mechanism; fixed-A paths do contain finite-n negative points. |
| [PD-T?drift-codex-50](../tracks/bivariate-lanczos/theory/drift-codex-e6-50-public-va-drift-measured.md) | MEASURED | Pinned polyrat 0.2.2 shows span gaps of 0.004105 (rotated square, n = 24) and 0.010164 (triangle, n = 20) at near-machine orthogonality. Upstream `[y,x]` is the dev order and `[x,y]` the reversed mirror. Smooth fits stay accurate. Adversarial-direction off-sample errors depend on the test distribution: about 15 times larger on uniform points than on the original midpoint set. |

Still OPEN:
- an all-degree exponential/matching drift theorem (E2);
- general staircase safety;
- the original universal obstruction PD-T055;
- a uniform optimal Padua radius PD-T075(U2);
- reading (G) of PD-T056.

## Evidence

- **Audit and response.** Audit reruns, the reviewer reports and the scripts are in [checks/audit-01/](../topics/padua-lanczos-drift-20261101/checks/audit-01/). The response checkers write to `topics/padua-lanczos-drift-20261101/evidence/response-01-*.json`.
- **Cold storage.** The audit-01 raw outputs are in AC's Padua cold storage (`padua-lanczos-drift-20261101/audit-01/`, zip sha256 `29c17721…`, readback verified). Codex's own development ZIP is not yet delivered (audit P-F1).

## Next step

A Codex re-audit (`gpt-6-astra` xhigh) of response-01 and the PR14 integration. Then PR preparation: final IDs from the reserved ranges, registry application, and this topic's section of the root `RESULTS.md` once PR #16 has merged. Only AC merges.
