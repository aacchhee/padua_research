# PD-T?bivariate-lanczos-claude-117 — Measured on two Harris–Simanek checkerboards (m = 30, dev rule, degrees ≤ 20): off-pattern gains reach 10¹⁴ while on-pattern gains stay ≤ 5·10³, and the first-order off-pattern coefficient channel reproduces the clustered-checkerboard loss

ID kind: PD-T.
Aliases: gain census; coefficient-channel measurement; first-order off-pattern prediction; former PD-T?…-114 part 5; "the clustered-checkerboard loss is this first-order channel" (former title clause of PD-T?…-114).
Split from: PD-T?bivariate-lanczos-claude-114, part 5 ([FP, MEASURED]), its closing reading ("So on the clustered checkerboard …"), and the title clause "the clustered-checkerboard loss is this first-order channel". Split 2026-11-01T08:33:59+01:00, Codex audit-01, L1-later finding LL-M2. Two items stay in PD-T?…-114 as a verification record under Checks: part 5's first bullet (the formula check) and the univariate orthonormality numbers. The original wording of part 5 is preserved in PD-T?…-114's History.
Split into: none.

## Statement

[FP, MEASURED] Setting:
- Harris–Simanek checkerboards with m = 30 (PD-T?…-111, -112): cubic-clustered (s|s|²) and equispaced.
- BJ (dev) ordering, block window, degrees ≤ 20.
- c* = the product-type coefficients; on-pattern / off-pattern as defined in PD-T?…-114 (structurally permitted positions / structural zeros of c*).
- The gain of a window entry (k, l) is max |A + Aᵀ| over degrees ≤ n, with A from the univariate formulas of PD-T?…-114 part 3. Their numerical implementation is verified in PD-T?…-114, Checks.

(a) **Gain census.**
   - Cubic-clustered: on-pattern gains ≤ 5.0e3 (n = 16 and 20). Off-pattern gains up to 9.9e11 (n = 16) and 1.3e14 (n = 20); 296 resp. 709 of 7031 off-pattern entries are above 1e6 (medians 1.9, 6.4).
   - Equispaced: on-pattern ≤ 5.6, off-pattern ≤ 4.2e2 (n = 16) and 1.4e3 (n = 20).
(b) **First-order prediction.** The first-order defect −Σ δh_{k,l}(A + Aᵀ), with δh = the BJ run's off-pattern values, gives:
   - clustered: D = 1.8e-11 (n = 16) and 7.8e-9 (n = 20), against the BJ loss 2e-11, 8e-9 and the nonlinear long-double D(c* + BJ off-pattern) 2e-11, 8e-9;
   - equispaced: 4.2e-15, 1.5e-14 against 4e-15, 1e-14;
   - for the three absolute u-noise draws of IDEA?…-117: 2.3–4.8e-4 (n = 16) and 2.7–5.8e-2 (n = 20), against the measured median 4e-4, 3e-2.
(c) **Reading (MEASURED, within this scope).**
   - On the clustered checkerboard the loss up to degree 20 is reproduced to the printed digit by the first-order coefficient channel restricted to the structural zeros of c*.
   - The large gains are off-pattern only.
   - The BJ run's off-pattern errors (max 2.1e-13 in absolute value) produce 10⁶–10⁷ times less defect than generic absolute u-noise on the same entries.
   - "Reproduced" means first-order agreement in this finite scope. It is not a causal proof, and no second-order error bound is given.

## Definitions

D(c, n) = max |Ξ(c)_nᵀ Ξ(c)_n − I| over the columns of degree ≤ n (PD-T?…-114). Off-pattern values of the BJ run are the computed inner products q̂_lᵀ(a q̂_{p(k)}).

## Assumptions

IEEE double precision for the BJ run (NumPy 2.5.3); long double (x86 80-bit) for Ξ, c*, the formula evaluation and the direct check; weights |1/ω′| normalised.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) gain census | MEASURED | `logs/r06_gain_identity.log`; producer rerun by Codex audit-01 (below) |
| (b) first-order predictions | MEASURED | `logs/r06_gain_identity.log`, `logs/r06_coefficient_channel.log` |
| (c) reading | MEASURED (interpretation of (a)–(b) within their scope) | no second-order bound; dev rule only |

## Depends on

PD-T?…-114 parts 1–4 (the gain formulas; PROVED), PD-T?…-111 (product-type coefficients of the checkerboards), PD-T?…-112 (a) (the loss being explained).

## Checks

- Developer run: `python3 -I tracks/bivariate-lanczos/code/L1/l1_r06_gain_identity.py > topics/bivariate-lanczos-20261031/directions/L1/logs/r06_gain_identity.log` (35 s, Python 3.13.18, NumPy 2.5.3). The IDEA?…-117 runs are in `logs/r06_coefficient_channel.log`.
- Rerun by Codex audit-01 (L1-later): the same producer, run with Python 3.12.14 and NumPy 2.3.5; log `topics/bivariate-lanczos-20261031/audit-01/L1-later/gain_producer_rerun.log`, sha256 `583ca75e1338abcb7d8d193b71d865fd861f5f774a5be666d7e3af495f37169e`.
  - It reproduced 91 entries per family.
  - Cubic: off-pattern gains 9.9e11 / 1.3e14 at n = 16 / 20, on-pattern maximum 5.0e3.
  - Equispaced: off-pattern 4.2e2 / 1.4e3, on-pattern 5.6.
  - The first-order BJ predictions 1.8e-11 / 7.8e-9 were reproduced too.
  - This is a rerun of the developer's producer, not an independent implementation. Reconstruction 02 reproduced the on/off split independently but not the magnitudes.

## Sources

None.

## Proof or evidence

Measured; see the logs above.

## Scope

Two checkerboards (m = 30), the dev ordering, the block window, degrees ≤ 20. Not covered:
- second-order terms (the n = 24 values of IDEA?…-117 are beyond first order for the u-noise draws, D ≈ 6);
- other parent rules: alt gives 3.1e-13 on the cubic set at n = 24 (PD-N?…-105, reconstruction-02 extension), and their off-pattern channel is not analysed;
- the HL ordering (not run);
- the reason the BJ off-pattern errors are more benign than generic u-noise (PD-T?…-115).

## Open items

Which structure of the BJ off-pattern errors keeps them away from the high-gain directions (R07, PD-T?…-115).

## History

- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later LL-M2; branch head 5f52331): created by splitting part 5 and its reading out of PD-T?…-114, whose parts 1–4 stay PROVED there.
  - Items (a)–(c) are part 5's second and third bullets and its closing reading, with only the labels and the setting line changed.
  - The title clause "the clustered-checkerboard loss is this first-order channel" becomes the measured, scoped title above.
  - The last bullet of (c), the Scope's "other parent rules" item (from PD-T?…-114's History, reconstruction-02 M1) and the audit-01 rerun in Checks are new.
  - Original wording: PD-T?…-114, History entry of 2026-11-01T08:33:59+01:00.
