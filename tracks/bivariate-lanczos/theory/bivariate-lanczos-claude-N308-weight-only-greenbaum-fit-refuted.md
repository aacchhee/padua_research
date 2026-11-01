# PD-N?bivariate-lanczos-claude-308 — MEASURED: a first-order consistent (weight-only) fit does not remove ≥ 90% of the forward error on the rotated square

ID kind: PD-N.
Aliases: R06 hypothesis C (kill criterion K15, written after K13/K14 and before its own test); IDEA?bivariate-lanczos-claude-316.
Split from: none (created per finding L8 of L3-reconstruction-02).
Split into: none.

## Statement

On the rotated random square (θ = 0.3, M = 1681, BJ/CGS), the best first-order fit of the computed partial coefficient data by exact sections of any consistent section pair near Φ(μ) (equivalently, in the overdetermined case, of node-reweighted measures) leaves ρ = ‖Jη* − e‖/‖e‖ ≥ 0.45 for n = 12..20 with the minimiser in the linear regime, when e is computed against an accurate (80-bit long-double CGS2) reference; ρ = 0.65–0.74 at n = 18, 19, 20 with loss ≥ 1e-9 (L3-reconstruction-02, `consistency_recheck.py`, a different rounding realisation). Hence hypothesis C (ρ ≤ 0.1 at every n ≥ 18 with loss ≥ 1e-9) is false within this scope. The developer's own kill (n = 19, ρ = 0.57) used a double-precision reference whose minimiser left the linear regime (finding M1) and is superseded by the reviewer's linear-regime kill.

## Negative-result scope (PD-N only)

Attempted mechanism: R06 hypothesis C (weight-only Greenbaum-type backward fit). Parameter range: rotated square, n ≤ 20 (linear regime), BJ/CGS; first-order (linearised) fits only.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| ρ ≥ 0.45 (n = 12..20), linear regime | MEASURED | reviewer logs `reviews/logs_L3b/consistency_recheck_rot03*.log`; developer log `directions/L3/logs/r06_weight_fit_rot03.log` (double reference); fresh rerun n = 18–20 (ρ = .652, .709, .740) and rank-sensitivity instrumentation by Codex audit-01 L3-framework (`topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_rot03_n18_20.log`, `lstsq_sensitivity.log`) |

Candidate / claim disposition: REJECTED. Rejection reason: refuted (within scope).

## History

- 2026-11-01T00:48:09+01:00, L3 developer: created per finding L8 of L3-reconstruction-02.
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): current evidence cited (status-pointer maintenance) from Codex audit-01 (audit-01/L3-framework.md; candidate 5ccfac2); first-order (linearised) fits only, as stated — no claim about nonlinear positive-measure fits. Status unchanged. Original wording of the replaced passages: «| ρ ≥ 0.45 (n = 12..20), linear regime | MEASURED | reviewer logs `reviews/logs_L3b/consistency_recheck_rot03*.log`; developer log `directions/L3/logs/r06_weight_fit_rot03.log` (double reference) |».
