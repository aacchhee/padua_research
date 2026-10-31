# PD-T?bivariate-lanczos-claude-204 — Measured section accuracy on semi-orthogonal runs: the F-section is accurate exactly when the local level is small; one-pass windows lose local orthogonality on rot0.3, triangle and annulus; a two-pass window restores it everywhere and removes most of the plain-run loss there

ID kind: PD-T.
Aliases: L2-Q1(b) measurements (F-part); IDEA?…-206 P1/P2; local channel vs propagated channel; "two-pass window".
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ block window, u = 2^-53, 12 benchmarks, run types: plain one-pass CGS ("none"), CGS2 against all previous columns ("fullcgs2"), oracle partial reorthogonalization at √u ("oracle"), and the same with a two-pass window ("w2_none", "w2_oracle"). Semi-orthogonal (SO) degree: L(n) ≤ √u.

(a) **F-section (frozen kill rule for the F-part).** e_F > u^{3/4} at SO degrees occurs only on one-pass runs of rot0.3 (n = 18–24), triangle (n = 8, 10) and annulus (n = 16–30); in each case the local level μ (max in-window |Ω|) is ≥ 1.2e-11 there and e_F ≈ 0.1–0.6·μ (e.g. rot0.3 oracle n = 24: μ = 2.2e-9, e_F = 6.9e-10; triangle n = 10: μ = 6.6e-10, e_F = 1.4e-10). On every SO degree of every fullcgs2, w2_none and w2_oracle run, e_F ≤ 2.2e-15 (≤ 7.7e-15 on tensor 41²). This is the pattern Theorem A of PD-T?…-201 predicts (error term 2μ₁τ₁); the frozen kill rule therefore kills "semi-orthogonality alone ⇒ accurate F-section" for one-pass windows (scope: these three sets) and does not fire for two-pass windows or full reorthogonalization.
(b) **IDEA?…-206 (pre-registered 00:16).** P1: with the two-pass window, μ ≤ 3.2e-16 at all SO degrees on all benchmarks (criterion 10³u: survives). P2: two-pass window + oracle partial, e_F ≤ 2.2e-15 at all SO degrees (criterion u^{3/4}: survives). P3 (expected to fail): e_H > u^{3/4} at SO degrees on 7 benchmarks — fails as expected (PD-N?…-201).
(c) **Local vs propagated loss.** On the triangle the plain one-pass loss is local: L(n) = μ(n) at every degree (1.0e-11 at n = 8 … 1 at n = 20). Rotπ/4 and the disk keep μ ≤ 3e-14 while L grows to 4e-3 and 1e-8, and the L-shape has μ = 1.3e-10 at L = 0.12 (n = 30): their loss is propagated (out of window); the annulus is intermediate (μ/L ≈ 10⁻⁴–10⁻¹). The two-pass window alone reduces the plain loss at the last degree from 1.0 to 7.4e-5 (triangle, n = 20), 5.8e-6 → 8.6e-7 (rot0.3, n = 24), 4.2e-3 → 2.5e-4 (rotπ/4, n = 24), 4.9e-3 → 1.7e-4 (annulus, n = 28); it leaves the J-defect unchanged (triangle 1.6e-3 → 1.7e-3 at n = 20).
(d) **Cost of the oracle partial runs** (dot products, BJ count): window passes Σ|W_k| = 12 676 (one pass, M = 1681, n = 24); oracle partial reorthogonalization adds 17 077–30 906 reorthogonalization dot products on rot0.3/rotπ/4 (35–80 triggered columns of 324) against 105 300 for fullcgs2; on product-type sets nothing is triggered. (Oracle measurement costs, 39 974, are not part of a practical scheme; R02 replaces them by the ω-estimate.)

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

## Depends on

PD-T?…-201 (what is predicted), -202 (J-part).

## Checks

Commands in PD-N?…-201. Independent rerun: none.

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
