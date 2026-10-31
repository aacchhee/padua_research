# PD-N?bivariate-lanczos-claude-105 — The non-product growth is not caused by "one relation per column" as such, and the window truncation is a cause on some sets (refutes the PD-T?…-109 Consequence)

ID kind: PD-N.
Aliases: selection-rule dependence; parent-rule dependence; truncation vs single-pass CGS; recon-01 B1.
Split from: PD-T?bivariate-lanczos-claude-109 ("Consequence" sentence).
Split into: none.

## Statement

[FP, MEASURED] Seed-11 node sets of R02/R03 (M = 1681, uniform weights: square, square rotated by 0.3 and π/4, disk, triangle). Graded basis with column (t, j) ↔ x^{t−j}y^j; one CGS pass, no reorthogonalisation, double precision. Loss at degree n is max|Q̂_nᵀQ̂_n − I|.

(a) **Selection dependence at fixed truncation.** Block window (degrees t−2..t). The parent rules are:
   - dev: the input code's rule, BJ;
   - mirror: HL BIT;
   - alt: X-product for j < t/2, Y-product otherwise;
   - adapt: per column, the admissible product with the larger β/‖Aq_p‖.

   Loss by rule:

   | set | n | dev | mirror | alt | adapt |
   |---|---|---|---|---|---|
   | rotation 0.3 | 24 | 5.8e-6 | 2.1e-8 | 1.1e-9 | 2.9e-12 |
   | rotation π/4 | 24 | 4.2e-3 | 3.4e-1 | 1.5e-8 | 9.4e-7 |
   | disk | 24 | 9.8e-9 | 1.1e-10 | 8.4e-12 | 3.6e-11 |
   | triangle | 20 | 1.0 | 5.4e-5 | 1.2e-7 | 1.6e-9 |
   | triangle | 24 | 1.0 | 0.99 | 1.4e-5 | 1.6e-7 |

   The square stays ≤ 1.5e-13 for every rule. Selections that all use one relation per column therefore differ by factors 10³–10⁸ at the same truncation.
(b) **Truncation.** Dev rule with one CGS pass against all previous columns (no window):
   - rotation π/4: 1.9e-14 at n = 24;
   - disk: 6.9e-15 at n = 24 (the growth disappears without truncation);
   - triangle: 1.0 at n = 20;
   - rotation 0.3: 1.6e-6 at n = 24 (single-pass Gram–Schmidt on the selected products loses orthogonality without any truncation).

Consequence: the PD-T?…-109 statement "the growth … is caused by the triangular one-relation-per-column selection of the Jacobi pencil (PD-T?…-108), not by the truncation of the window" is refuted within this scope, on two counts:
- (a) the selection rule, not one-relation-ness, sets the magnitude;
- (b) removing the truncation removes the growth on two of the four non-product sets.

What remains measured:
- for a fixed selection, the growth is a property of the exact recurrence (PD-T?…-109 (a), P* = P);
- no tested one-relation selection reaches the product level on rotation π/4 or on the triangle (best 1.5e-8 and 1.6e-7 at n = 24, against ≤ 1.5e-13 on the square).

## Negative-result scope (PD-N only)

- Attempted mechanism: "one-relation-per-column selection (as a class) is the cause, the truncation is not".
- Parameter range: the five seed-11 sets, n ≤ 24, four parent rules, block and full windows, one CGS pass.
- Not covered: other parent rules; other windows except depth 10 and CGS2 (the reconstruction ran these: modest effects); larger M.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `topics/bivariate-lanczos-20261031/directions/L1/logs/c01_recon_runs.log` (developer rerun with own code, own seeds); independently `reviews/logs_L1/sweep_alt.log` A and `prop_selection.log` (reconstruction 01, other seeds; the selection dependence is also present in the exact-coefficient propagator, e.g. triangle u·max_i‖L*(z_i)⁻¹‖ at n = 20: 1.2 dev, 3.4e-8 adapt) |
| (b) | MEASURED | the same log; independently `reviews/logs_L1/sweep_loss.log` (fullcgs_f64) |

Candidate / claim disposition:
- PD-T?…-109 "Consequence" (second half): REJECTED: refuted.
- IDEA?…-111 recorded inference "the row selection, not the truncation, causes the instability": REJECTED: refuted.
- R03 F8 ("the window truncation itself is unstable off product supports" listed as a failed route): withdrawn. Truncation is not *sufficient* (two relations with the same truncation are stable on rotated squares and the disk), but it is a cause on rotation π/4 and the disk.

Rejection reason: refuted (MEASURED, stated scope).

## Depends on

PD-T?…-101 (graded basis independent of the parent rule), -108 (selections as triangular left inverses), -109.

## Checks

The developer's re-implementation of the dev rule agrees with the library BJ recurrence within a factor ≤ 14 at every printed degree (triangle n = 16: 4.9e-4 vs 6.8e-3). This is a different norm rounding amplified by the growth; the same log has the libBJ rows.

## Sources

- Barrio–Peña–Sauer 2010, Remark 9 and §5 (the choice of variable per polynomial affects rounding; point-dependent heuristics), read in fulltext pp. 409–410, 413, 418–419. This qualitatively anticipates (a) in the evaluation setting; no growth rates are reported there.
- Reconstruction 01 (reviews/L1-reconstruction-01.md, finding B1) found (a) and (b) first; this file records the developer's confirmation.

## Proof or evidence

Measured: `python3 -I tracks/bivariate-lanczos/code/L1/l1_c01_recon_checks.py runs > topics/bivariate-lanczos-20261031/directions/L1/logs/c01_recon_runs.log` (7 s). The criterion (candidates.md C01-2, C01-3) was written before the run.

## Scope

Finite: one M, one seed per shape, n ≤ 24. "adapt" and "alt" are heuristics; no optimality is claimed.

## Open items

- A selection principle: which triangular selection minimises max_z‖L*(z)⁻¹‖ for a given measure (L2 hand-off).
- The single-pass CGS mechanism on the triangle and on rotation 0.3 (a κ²-type loss of the selected products?).

## History

- 2026-10-31T23:05Z: created (Claude Opus 5.5, xhigh; L1 response to reconstruction 01, finding B1).
