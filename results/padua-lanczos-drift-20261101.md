# padua-lanczos-drift-20261101: finite-precision span drift in bivariate Lanczos (PR #15)

This is the topic's results file; only the topic orchestrator writes it. Branch `codex/padua-lanczos-drift-20261101`, draft PR #15. It was migrated into the repository on 2026-11-01 under the repository-only results rule of PR #16 (now merged at `28aaa208`). The source was the orchestrator's local working track of the same name, revised here.

All IDs are provisional (`PD-T?drift-codex-NN`, `PD-N?drift-codex-NN`, `IDEA?drift-codex-NN`). The permanent reservations are PD-T136–155, PD-N062–071, IDEA-246–285 and LIT-445–459. Theory records are in `tracks/bivariate-lanczos/theory/drift-codex-*.md`, code in `tracks/bivariate-lanczos/code/drift/`, and the topic files in `topics/padua-lanczos-drift-20261101/`.

## Status (2026-11-01): AUDIT — response-02 done, Codex re-audit pending

- **Development.** Codex developed the campaign (scientific source `b09e1db`).
- **Audit-01.** The Claude audit (Opus 5.5 xhigh) of `36c93794` returned CHANGES REQUIRED: 0 high, 10 medium and 32 low findings, with no PROVED or MEASURED claim refuted. See [audit-01](../topics/padua-lanczos-drift-20261101/audit-01.md).
- **Response-01.** By AC's redirection, Claude is the developer of the fixes. Because Claude is also the auditor of record, a Codex re-audit is required before PR preparation. See [response-01](../topics/padua-lanczos-drift-20261101/response-01.md).
- **Integration.** PR #14 merged first (main `e0d9e3d`); PR #16 is now merged at `28aaa208` and integrated without rewriting history. Both topics’ ledger/crosswalk content is preserved.
- **Audit-02.** Codex Astra xhigh re-audited Claude response-01: CHANGES REQUIRED, 2 medium and 8 low findings. Numerical checks reproduce. Correct the record-15 ancillary limit and address record-05 finite-result classification, plus the listed low corrections. [Audit record](../topics/padua-lanczos-drift-20261101/audit-02.md).
- **Response-02.** Claude answered all 10 audit-02 findings ([response-02](../topics/padua-lanczos-drift-20261101/response-02.md)): record 15 limit factor corrected; record 05's finite inequalities split into the new PROVED record 06; record 30 labels and eventual-only scope; E6 wording and the numpy pin; a degree-4 trajectory replay; repository-only results wording. Codex re-audit pending (handoff 08).

## Meaningful results, at their stated scope

| Record | Status | Result |
|---|---|---|
| [PD-T?drift-codex-30](../tracks/bivariate-lanczos/theory/drift-codex-e5-30-padua-positivity-radius-upper-bound.md) | PROVED, analytic (audit: confirmed) | For the named Padua certificate P_n, ρ_n = O(n⁻⁵), with limsup n⁵ρ_n ≤ 20√2π⁴/9. The witness is ζ_n = (cos(π/n + a/n⁴), cos(π/(n+1) + a/n⁴)), a = 20π³/9. This settles PD-T075(U1) only. A response-01 remark (mathematics confirmed by audit-02; endpoint-label and eventual-only a≤0 scope corrections A02-L3/L4 applied in response-02, re-audit pending) sharpens the constant to 2√2π⁴(10−2√2)/9 ≈ 219.5. PD-T075(U2) and PD-T056(G) remain OPEN. |
| [PD-T?drift-codex-31](../tracks/bivariate-lanczos/theory/drift-codex-e5-31-explicit-square-root-spread-family.md) | PROVED (audit: confirmed) | An explicit square n = 1 four-atom split gives spread ≤ √(6ε) and a √ε lower bound for residual γε, γ < 1/3. This is reading (E) only. |
| [PD-T?drift-codex-01](../tracks/bivariate-lanczos/theory/drift-codex-e1-01-span-derivative.md), [-02](../tracks/bivariate-lanczos/theory/drift-codex-e1-02-rational-span-bounds.md) | PROVED (audit: confirmed) | The normal-quotient first-order span derivative for aggregate injections, plus rational node, HS and row bounds (spectral output). |
| [PD-T?drift-codex-03](../tracks/bivariate-lanczos/theory/drift-codex-e1-03-scalar-operation-bridge.md) | PROVED, formal model (audit: confirmed) | The first-order normal map of a declared scalar CGS2 graph. Dot, coefficient and norm errors lie in the polynomial kernel. It makes no IEEE claim. Full-trajectory replay: degree 3 independent (audits), degree 4 developer (response-02). |
| [PD-T?drift-codex-04](../tracks/bivariate-lanczos/theory/drift-codex-e1-04-finite-aggregate-separation.md) | PROVED, computer-assisted (audit: confirmed with corrections) | A degree-12 aggregate separation: T24 κ ratio > 1126 (BJ against pivot), rational rotated Q24 > 11.72 (BJ against alt, Urow certificate). The original KHS-only test is INCONCLUSIVE (squared ratio 62.16 < 100). There is an exact rotQ24 pivot tie at (2,1); T24 has none. |
| [PD-T?drift-codex-06](../tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md) | PROVED, finite computer-assisted, formal scalar model (split from -05 in response-02, A02-M2; re-audit pending) | At degree 12 in record 03's formal scalar-CGS2 model (l-infinity relative operation errors), the full-graph comparator uppers and explicit BJ node-sign witnesses give K_inf,BJ > 800 K_inf,pivot on T24 (squared certificate ratio 657331.08) and K_inf,BJ > 7 K_inf,alt on rotQ24 (62.09). The thresholds were chosen post hoc. The rotQ24 certificate ratio is below 100, so it does not decide factor ten there. No IEEE or all-degree claim. |
| [PD-T?drift-codex-05](../tracks/bivariate-lanczos/theory/drift-codex-e1-05-finite-scalar-cgs2-capacities.md) | MEASURED experiment; factor-ten target PARTIAL | The exploratory scalar experiment and its both-grid factor-ten test are INCONCLUSIVE: the test passes on T24 and not on rotQ24. The factor-ten target is PARTIAL: T24 conjunct PROVED in -06, rotQ24 conjunct OPEN. |
| [PD-T?drift-codex-10](../tracks/bivariate-lanczos/theory/drift-codex-e3-10-polynomial-span-certificate.md), [-11](../tracks/bivariate-lanczos/theory/drift-codex-e3-11-selection-criterion.md) | PROVED (11: fixed degree) | An a posteriori computed-polynomial span certificate, and a filtered fixed-degree selection criterion. Uniform polynomial safety is OPEN. |
| [PD-N?drift-codex-15](../tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md) | PROVED (core confirmed by audit-02; ancillary limit corrected in response-02, re-audit pending) | The generalized fixed-degree projection-only closure lemma and its ten-node instance are confirmed. The relative-source limit is lim δ_(A_m)/u = (κ_(A_m)/b)‖v_m‖ ≥ ‖v_m‖, not ‖v_m‖ (A02-M1). On T_3/BJ with the source in v_20 the squared limit is 88/15 against ‖v_20‖² = 22/5. Exact regression: [response-02-e4-creator-limit.json](../topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json). The original PD-T055 is OPEN. |
| IDEA?drift-codex-14 (withdrawn PD-N vehicle) | IDEA disposition accepted | The zero-error quantifier refutation is retained as an IDEA, not a PD-N. Delete its withdrawn theory-file tombstone at preparation. |
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
- **Cold storage.** The audit-01 raw outputs are in AC's Padua cold storage (`padua-lanczos-drift-20261101/audit-01/`, zip sha256 `29c17721…`, readback verified). Codex’s original development ZIP and run artifacts are now verified locally by audit-02; Windows delivery remains pending. No large raw capacity file is needed for compact-evidence regeneration.

## Next step

Independent Codex re-audit of response-02 (handoff 08). PR16 is merged: results tracking is repository-only. After acceptance, PR preparation assigns final IDs from reserved ranges, applies approved registry proposals, and adds only this topic’s root `RESULTS.md` section. Only AC merges.
