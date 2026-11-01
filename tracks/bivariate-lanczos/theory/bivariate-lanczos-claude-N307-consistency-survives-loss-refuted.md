# PD-N?bivariate-lanczos-claude-307 — MEASURED: "the completed computed pair stays consistent until loss 1e-3 on product-aligned supports" is false

ID kind: PD-N.
Aliases: R06 hypothesis A (kill criterion K13); IDEA?bivariate-lanczos-claude-314.
Split from: none (created per finding L8 of L3-reconstruction-02).
Split into: none.

## Statement

For BJ (block window, CGS) on the uniform random square, M = 1681 (L1 `nodes_random(1681, 0)`), the asymmetry of the completed pair (Ĥ_F, Ĥ_J) (PD-T?…-314) exceeds 1e3·u·‖Ĥ‖ at n = 28 (2.1e3·u) while the loss is 3.3e-13 ≤ 1e-3, and reaches 1.7e7·u at n = 40 (loss 2.7e-9). The excess sits in the implicit J-completion (asym_J ≈ fwd_J); the raw F data stay nearly symmetric (asym_F ≤ 3.6e-13 ≈ 2e-3·fwd_F), which is a Greenbaum-like counter-indication (finding M2): the refuted statement concerns the completed pair, not the raw data.

## Negative-result scope (PD-N only)

Attempted mechanism: R06 hypothesis A ("consistency survives loss on product-aligned supports"). Parameter range: one random square, BJ/CGS, n ≤ 40, double precision.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| K13 violation at n = 28..40 | MEASURED | `directions/L3/logs/r06_consistency_random.log`; fresh rerun by Codex audit-01 L3-framework (`topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_random_n40.log`: asymmetry/u 2.09e3 at n = 28, 1.69e7 at n = 40) |

Candidate / claim disposition: REJECTED. Rejection reason: refuted (completed-pair version, within scope).

## History

- 2026-11-01T00:48:09+01:00, L3 developer: created per finding L8 of L3-reconstruction-02.
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): current evidence cited (status-pointer maintenance) from Codex audit-01 (audit-01/L3-framework.md; candidate 5ccfac2); the audit's reading — a finite measured failure, not a proof that no nonlinear positive measure or Greenbaum model exists — matches the stated scope. Status unchanged. Original wording of the replaced passages: «| K13 violation at n = 28..40 | MEASURED | `directions/L3/logs/r06_consistency_random.log` |».
