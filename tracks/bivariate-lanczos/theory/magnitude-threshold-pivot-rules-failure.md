# PD-N?bivariate-lanczos-claude-507 — Magnitude-threshold pivot rules (alternative pivot only if kappa times larger; pair-norm comparison) do not restore the robustness of the fixed 'scheme' rule in point-by-point Givens updating

ID kind: PD-N.
Aliases: pivk-kappa rule; VB-C 2010 p. 395 pivot suggestion ('if two pivots differ in some orders of magnitude, ... choosing the larger one'); IDEA?bivariate-lanczos-claude-504 (b1), (b2); pairnorm.
Split from: PD-N?bivariate-lanczos-claude-506 (finding L9 of reconstruction 01: this mechanism failure is a separate evidenced failure).
Split into: none.

## Statement

[FP, MEASURED; scope = Parameter range below.] Let Algorithm 1 use, for each doubly-parented monomial, the primary ('scheme') pivot unless (pivk-kappa) the alternative pivot has modulus larger than kappa times the primary one, or (pairnorm-kappa) the norm of the alternative rotated pair exceeds kappa times that of the primary pair. Then, on Padua first-family sets with n = 20 and 30, cubature and U(0.1,1) weights, orders given, sortx, rand1-3, gepp (24 streams, `logs/r03_rules.jsonl`):

(K1) On the four orders rand1-3 and gepp (all prefixes numerically unisolvent in the sense of PD-T?bivariate-lanczos-claude-503: floating-point σ_min estimates, not certificates) pivk10, pivk100 and pairnorm100 reproduce the 'scheme' error to the printed digits (ratio 1.00 on all 16 streams; the alternative pivot is never taken), and pairnorm1 coincides with 'largest' (ratios to scheme 1.5-42, i.e. no better than 'largest').

(K2) On the structured orders (given, sortx; almost all prefixes singular) at n = 30 the rules that do take the alternative pivot are far worse than 'scheme' (cubature weights, scheme 2.3e-14 on both): pivk10 8.6e-9 (given), 2.7e-11 (sortx); pivk100 5.9e-12, 1.8e-11; pairnorm1 4.0e-12, 4.2e-13; U(0.1,1) weights (scheme 2.4e-14, 2.6e-14): pivk10 4.3e-3, 2.4e-9; pivk100 4.3e-3, 2.3e-9; pairnorm1 1.6e-13, 3.6e-13. At n = 20 on these orders pivk10, pivk100 and pairnorm100 equal 'scheme'; pairnorm1 is 1.2-2.7 times larger.

(K3) pairnorm100 is never meaningfully better than 'scheme' (ratio 1.00 on the numerically unisolvent orders; 0.99-2.4 over all 24 streams) and is up to 2.4 times worse (n = 30, U weights, given: 5.9e-14 vs 2.4e-14); it is equivalent to 'scheme' (an IDEA disposition, not a PD-N matter).

Hence no rule in this family improves on 'scheme' on any tested stream and the rules with kappa <= 100 that act at all are worse than 'scheme' by up to 11 orders of magnitude (pivk100, n = 30, U weights, given: 4.3e-3 versus 2.4e-14). In particular the reading of the VB-C p. 395 suggestion as 'choose the larger pivot when they differ by orders of magnitude' (kappa = 100) does not enhance stability in this range.

## Definitions

pivk{10,100}, pairnorm{1,100}: `givens_core.c` `givens_run2` rules 4 and 3 (kappa = 10, 100, 1, 100); 'scheme': rule 0; error: relative Frobenius error of (H_x, H_y) against the long-double reference, as in PD-T?bivariate-lanczos-claude-502.

## Assumptions

IEEE double, real nodes, the tables of parents of Algorithm 1, no skip threshold.

## Status by part

Overall status: MEASURED (the negative statement). Candidate / claim disposition: REJECTED: failed (pivk10, pivk100, pairnorm1: they do not achieve the stability aim; pairnorm100: equivalent to 'scheme', IDEA disposition 'equivalent').

| Mathematical part | Status | Evidence |
|---|---|---|
| K1-K3 | MEASURED | `logs/r03_rules.jsonl`, `r03_rules.log`, `r03_defer3.jsonl` (same rule columns) |

## Negative-result scope

Attempted mechanism: IDEA?bivariate-lanczos-claude-504 (b1), (b2). Parameter range: Algorithm 1, IEEE double, Padua n = 20, 30 only (n = 50 not run for these rules), kappa in {1, 10, 100}, the 24 streams above. A different kappa, a relative rather than absolute comparison, or n >= 40 is not covered.

## Depends on

PD-N?bivariate-lanczos-claude-506 ('largest' = kappa 1 member); input `f6_givens_vs_hl_deficit.py` via the bit-identical C port.

## Checks

`python3 -I exp_r03.py` in `tracks/bivariate-lanczos/code/L5/` (see R03.md section 5). Independent rerun: none. The independent reconstruction did not test these variants.

## Sources

VB-C 2010 p. 395 (the reconstruction verified that it states the kappa >> 1 rule).

## Proof or evidence

Measured; see Checks.

## Scope

Exactly the range above. Does not cover other pivot-selection principles (rank-revealing in a relative sense with a data-derived scale, pivoting on the column norm, randomised choice).

## Open items

n = 40, 50; kappa between 1 and 10 and between 100 and 1e8; why the first alternative taken at a near-singular prefix already destroys the zero pattern (mechanism OPEN, as in 506).

## History

2026-10-31T23:00Z, Claude Sonnet 5.5 (high), created in response to L5 reconstruction 01 finding L9 (and L7), by splitting N4 out of PD-N?bivariate-lanczos-claude-506.

2026-11-01T08:22:31+01:00, Claude Sonnet 5.5 (high), response to Codex audit-01 (L5) finding **M2** (terminology only): "(K1) On the four orders rand1-3 and gepp (all prefixes unisolvent)" and "(ratio 1.00 on the unisolvent orders ...)" now say "numerically unisolvent" (floating-point σ_min estimates of PD-T?bivariate-lanczos-claude-503, not exact or interval certificates). No number, scope, status (MEASURED) or disposition changed; audit-01 accepts this record as an eligible scoped negative statement.
