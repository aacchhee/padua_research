# PD-T?bivariate-lanczos-claude-204 — Measured section accuracy on semi-orthogonal runs: the F-section is accurate exactly when the local level is small; one-pass windows lose local orthogonality on rot0.3, triangle and annulus; a two-pass window restores it everywhere and removes most of the plain-run loss there

Final ID: **PD-T049** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: L2-Q1(b) measurements (F-part); IDEA?…-206 P1/P2; local channel vs propagated channel; "two-pass window".
Split from: none.
Split into: PD-N?…-206 (one-pass counterexamples of (a)).

## Statement

[FP, MEASURED] BJ block window, u = 2^-53, 12 benchmarks, run types: plain one-pass CGS ("none"), CGS2 against all previous columns ("fullcgs2"), oracle partial reorthogonalization at √u ("oracle"), and the same with a two-pass window ("w2_none", "w2_oracle"). Semi-orthogonal (SO) degree: L(n) ≤ √u.

(a) **F-section (frozen kill rule for the F-part).** e_F > u^{3/4} at SO degrees occurs only on one-pass runs of rot0.3 (n = 18–24), triangle (n = 8, 10) and annulus (n = 16–30); in each case the local level μ (max in-window |Ω|) is ≥ 1.2e-11 there and e_F ≈ 0.1–0.6·μ (e.g. rot0.3 oracle n = 24: μ = 2.2e-9, e_F = 6.9e-10; triangle n = 10: μ = 6.6e-10, e_F = 1.4e-10). On every SO degree of every fullcgs2, w2_none and w2_oracle run, e_F ≤ 2.2e-15 (≤ 7.7e-15 on tensor 41²). This is the pattern Theorem A of PD-T?…-201 predicts (error term 2μ₁τ₁); the frozen kill rule therefore kills "semi-orthogonality alone ⇒ accurate F-section" for one-pass windows (scope: these three sets) and does not fire for two-pass windows or full reorthogonalization.
(b) **IDEA?…-206 (pre-registered 00:16).** P1: with the two-pass window, μ ≤ 3.2e-16 at all SO degrees on all benchmarks (criterion 10³u: survives). P2: two-pass window + oracle partial, e_F ≤ 2.2e-15 at all SO degrees (criterion u^{3/4}: survives). P3 (expected to fail): e_H > u^{3/4} at SO degrees on 7 benchmarks — fails as expected (PD-N?…-201).
(c) **Local vs propagated loss.** On the triangle the plain one-pass loss is local: L(n) = μ(n) at every degree (1.0e-11 at n = 8 … 1 at n = 20). Rotπ/4 and the disk keep μ ≤ 3e-14 while L grows to 4e-3 and 1e-8, and the L-shape has μ = 1.3e-10 at L = 0.12 (n = 30): their loss is propagated (out of window); the annulus is intermediate (μ/L ≈ 10⁻⁴–10⁻¹). The two-pass window alone reduces the plain loss at the last degree from 1.0 to 7.4e-5 (triangle, n = 20), 5.8e-6 → 8.6e-7 (rot0.3, n = 24), 4.2e-3 → 2.5e-4 (rotπ/4, n = 24), 4.9e-3 → 1.7e-4 (annulus, n = 28); it leaves the J-defect unchanged (triangle 1.6e-3 → 1.7e-3 at n = 20).
(d) **Cost of the oracle partial runs** (dot products, BJ count): window passes Σ|W_k| = 12 676 (one pass, M = 1681, n = 24); oracle partial reorthogonalization adds 17 077–30 906 reorthogonalization dot products on rot0.3/rotπ/4 (35–80 triggered columns of 324) against 105 300 for fullcgs2; on product-type sets nothing is triggered. (Oracle measurement costs, 39 974, are not part of a practical scheme; R02 replaces them by the ω-estimate.)
(e) **Normalisation factor χ of Corollary A′ (added after audit-01, L2-F2; no kill rule).** χ(n) := max over columns k of degree ≤ n of ‖B_kq̂_{p(k)}‖₂/β_k (computed product norm over computed normalisation, double), in the two-pass-window runs without reorthogonalization (w2_none) and in the PRO-2D-J runs of PD-T?…-207, all 12 benchmarks, all degrees: max χ = 5.28 (triangle), 3.63 (cubic checkerboard), 3.08 (annulus), 2.80 (rot0.3), 2.32 (rotπ/4), 2.08 (L-shape), 1.91 (disk), 1.67 (square), 1.57 (equispaced checkerboard), 1.73 ≈ √3 (tensor 41², Padua 48, Chebyshev–Lobatto checkerboard); the same maximum in both run types. No near-breakdown occurs in these runs, so the χ factor of PD-T?…-201 Corollary A′ is at most 6.3 there. In the same runs the Frobenius loss at the last degree of PRO-2D-J is 3.7e-8 (rotπ/4), 3.3e-8 (triangle), 1.7e-7 (L-shape), 6.9e-8 (annulus) > √u although entrywise L ≤ 10√u: Corollary A′'s hypothesis η = ‖Ω‖_F ≤ √u is not met literally on these four sets (PD-T?…-201 Remark (ii): entrywise semi-orthogonality gives only η ≤ N√u). Measured, not a bound.

## Definitions

e_F, e_τ, e_H, μ, L as in candidates.md (IDEA?…-203) and PD-T?…-201; W = Q̂R⁻¹ with R = chol(Q̂ᵀQ̂) in double.

## Assumptions

Double precision, NumPy 2.5.3 / SciPy 1.18.1; section errors evaluated in double (evaluation floor ≤ 1.9e-14 on product controls, PD-N?…-201 Checks).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r01_sections.raw`, `r01_sections_w2.raw`, `r01_verdicts.txt` |
| (b) | MEASURED | `logs/r01_sections_w2.raw`, `r01_verdicts.txt` (IDEA-206 block) |
| (c) | MEASURED | same |
| (d) | MEASURED (counts) | `stats` lines in the raw logs |
| (e) | MEASURED | `logs/audit01_chi.raw.gz` from `cd tracks/bivariate-lanczos/code/L2 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I l2_audit01_chi.py > …/L2/logs/audit01_chi.raw` (run 2026-11-01T08:25:47–08:25:58+01:00, exit 0; Python 3.13.18, NumPy 2.5.3; gzipped afterwards; .gz sha256 0e0b0049e9bc3cb7084ba1d078220bc6b430c367f48b302e8cd12f1948d993b1, uncompressed sha256 7a8f8c15cfddf89d73db6b803419c31f8d170303e8eaa69d2cfc5014aa4f9e62) |

## Depends on

PD-T?…-201 (what is predicted), -202 (J-part).

## Checks

Commands in PD-N?…-201; part (e): command in the status table. Independent rerun: none of the all-12 section suite. Codex audit-01 reran Theorem-A stress cases and the PRO/selection section measurements on selected sets (`topics/bivariate-lanczos-20261031/audit-01/L2/theorem-A-rerun.log`, `proJ-rerun.log`, `selection-rerun.log`), supporting the scoped mechanism; it did not rerun the full suite.

## Sources

None.

## Proof or evidence

Measured; see logs.

## Scope

As PD-N?…-201. The oracle partial scheme reorthogonalizes only against out-of-window vectors (then a further window pass); with a one-pass window it does not repair local loss, which is why the triangle oracle run is not semi-orthogonal beyond n = 10.

## Open items

Two-pass window for the HL ORTH variant (conditional second MGS pass); whether μ stays at rounding level for larger M and n (Runs needed, R02).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01).
- 2026-11-01T01:29:55+01:00: Split into updated (original: "Split into: none."), reconstruction 01 F3 (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, finding **L2-F2**, supplementary evidence; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`) New measured part (e): size of the normalisation factor χ that PD-T?…-201 Corollary A′ now carries explicitly, and the Frobenius loss in the PRO-2D-J runs; new script `l2_audit01_chi.py`, log `logs/audit01_chi.raw.gz`. Checks line extended; original: "Commands in PD-N?…-201. Independent rerun: none." Parts (a)–(d) unchanged; status MEASURED unchanged.
