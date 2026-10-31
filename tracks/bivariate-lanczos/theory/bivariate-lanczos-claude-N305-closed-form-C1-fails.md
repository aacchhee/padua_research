# PD-N?bivariate-lanczos-claude-305 — MEASURED: the closed-form candidate C1 does not certify (H)-failure for Padua n = 2..12

ID kind: PD-N.
Aliases: C1 = Σ_j (q_j² − q_{j−1}q_{j+1}); IDEA?bivariate-lanczos-claude-310.
Split from: none (created per finding L10 of L3-reconstruction-01).
Split into: none.

## Statement

For the normalised two-term Padua generators (PD-T?…-309(c)) and C1 := Σ_{j=1}^{n}(e_je_jᵀ − ½(e_{j−1}e_{j+1}ᵀ + e_{j+1}e_{j−1}ᵀ)), min over Padua nodes of λ_min(G_iᵀC1G_i) < 0 for every n = 2..12 (the n = 2 entry is automatic: (H) holds at n = 2, PD-T?…-306, so no failure certificate of any kind exists there) (values −1.13, −0.199, −0.077, −2.9e-2, −1.2e-2, −3.8e-3, −1.5e-3, −4.5e-4, −1.5e-4, −4.5e-5, −1.4e-5).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-310 (C1 as a uniform obstruction certificate). Parameter range: Padua n = 2..12, floating point.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| negativity for n = 2..12 | MEASURED | `r02_closed_form_C.py`, log `directions/L3/logs/r02_closed_form_C.log` (margins ≥ 1.4e-5 in absolute value vs O(1) entries) |

Candidate / claim disposition: REJECTED. Rejection reason: failed (within the measured range). The successful replacement is the two-term Turán certificate of PD-T?…-313.

## History

- 2026-10-31T23:55:17+01:00, L3 developer: created per finding L10 of L3-reconstruction-01.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding L13 (n = 2 entry annotated) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «min over Padua nodes of λ_min(G_iᵀC1G_i) < 0 for every n = 2..12».
