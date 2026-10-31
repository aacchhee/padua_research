# PD-T?bivariate-lanczos-claude-107 — Two regimes of loss of orthogonality, and the per-node propagator as a predictor (measured)

ID kind: PD-T.
Aliases: regime split (product-aligned vs non-product supports); node-propagator predictor P(n); shadow recurrence; amplification-not-source finding; controlled fraction of the block Paige identity.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] For the BJ window recurrence (and, where stated, HL), u := 2^-52, on the node sets listed in Scope:

(a) **Product-aligned regime.** On uniform random squares (M = 1681, 6724), tensor Chebyshev 41², Padua n = 48/80 with cubature weights, Padua 48 with uniform weights, x↔y swaps and the square rotated by π/2, the injecting-operator defect and the commutator residual stay at 1e-15–1e-14 until loss starts, and loss is Ritz-type: on random squares loss ≈ u/ρ_Z ≈ u/ρ_{H_x} ≈ u/ρ_{H_y} (ratio 0.4–2.5, bj).
(b) **Non-product regime.** On supports that are not products in the recurrence's coordinates (square rotated by 0.05, 0.3, 1.0, π/4; tensor grid and L-shape grid rotated by 0.3; random L-shape; annulus; disk; triangle; sheared squares; rotated product set) loss grows exponentially from degree ≈ 8–12 (BJ and HL alike), independent of Ritz convergence, and scales with u. The rate increases with the departure from product structure: rotation by 0.05 rad gives 2e-13 at n = 24, by 0.3 gives 5e-6, by π/4 gives 4e-3; the triangle reaches 1 at n = 20 (M = 1681).
(c) **Node-propagator predictor.** Driving the computed recurrence at all nodes simultaneously with iid forcing of size u/√M per node and step (PD-T?…-104 part 1; one extra pass of the recurrence without inner products), the response P(n) = max_{k ≤ N_n} ‖γ_k‖ tracks the measured loss within a factor 1–5 in both regimes (random square, square rotated 0.3 and π/4, disk, tensor, Padua cubature, random1681_s0; degrees 4–40), whereas u/ρ_Z misses the non-product regime by 10³–10⁸. Exception: on the triangle P(n) underestimates by 50× at n = 12 and by 10³ at n = 16.
(d) **Amplification, not source growth.** With F-products alone or J-products alone computed in double (the rest in long double), the rotated square shows the same exponential growth as the all-double run (`r02_mixed_precision.log`); in the exact ω-recurrence (PD-T?…-106) the F-sources stay at 1e-17 and the J commutator sources stay 2–3 orders below the loss while the propagation term carries the growth (`r02_identities.log`).
(e) **Within-degree coupling.** The ratio max|coefficient of q_{(t,r)} in F q_{(t−1,j−1)}|/min β (r < j) is ≤ 7e-15 on tensor 41², 2e-3–0.17 on the random square, and 0.3–2.5 on the rotated squares and the triangle, where ‖(A′_t)⁻¹‖ grows roughly linearly in t (2 → 21 at t = 16), against ≈ 2 = 1/β on product supports (`r02_block_solve_growth.log`).
(f) **Block-Paige identity controls little.** For F-Ritz vectors, the joint min-residual vector and Z-Ritz vectors, the component of the new block along y in the identity's direction B s is 0–47% of ‖Q̂_+ᵀy‖ (typically ≤ 10% for F-Ritz vectors; PD-T?…-103 corollary).

**Corrections (2026-10-31T23:05Z, response to reconstruction 01; the wording above is kept as originally written):**
- **(a)/(b) are statements about the listed set types, not a classifier by support** (recon-01 major finding). Product supports with non-product weights (square with exp(8xy): loss 1.9e-8 at n = 24, 1.6·10⁵ × u/ρ_Z) and sampled product densities (Gaussian cloud: 2.4·10³ × u/ρ_Z) lose far above the Ritz level. See PD-N?…-106. The regime depends on the measure, not on the support shape.
- **(b) "exponentially"**: over n ≤ 24 the log-loss is convex in n (recon-01: the per-degree factor rises from ≈ 3–4 at n ≈ 10 to ≈ 8–12 at n ≈ 22). In the developer's c01 runs the decades per 4 degrees increase too, e.g. 2.3 → 2.5 → 2.8 for rotation 0.3 between n = 12 and 24. "Grows exponentially" is to be read as "grows at least exponentially, at an increasing rate, over the measured range". The onset is n ≈ 18 for the 0.05 rotation (PC-2).
- **(b) depends on the selection rule**: all statements are for the dev (BJ input-code) parent rule; other one-relation rules change the loss by 10³–10⁸ (PD-N?…-105).
- **(c)** captures the vector channel only. It misses strongly non-uniform weights (clustered checkerboards; PC-3, PD-N?…-103 (b)) and the triangle.
- **(e)**: non-diagonal within-degree coupling does not imply growth: recon-01 found weights exp(xy), exp(4xy) on the square stable; the developer's rerun gives 2.7× and 32× u/ρ_Z at n = 24.

## Definitions

ρ_O: minimal Ritz residual of section O on the computed span (R01). Defects and C_res: PD-T?…-102, -104. P(n): see (c), code `l1_node_propagator.py`.

## Assumptions

Uniform weights except Padua cubature and the exp(x)exp(y), exp(2xy) weight probes; IEEE double (NumPy 2.5.3, OpenBLAS 0.3.34); long double = x87 80-bit.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r01_{input3,padua,swap}.raw`, `r01_verdict.txt`, `r01_defect_probe.log` |
| (b) | MEASURED | `logs/r01_{rotation,irregular}.raw`, `r01_defect_probe.log`, `r01_precision_scaling.log` |
| (c) | MEASURED | `logs/r02_node_propagator.log` |
| (d) | MEASURED | `logs/r02_mixed_precision.log`, `logs/r02_identities.log` |
| (e) | MEASURED | `logs/r02_block_solve_growth.log` |
| (f) | MEASURED | `logs/r02_identities.log` |

## Depends on

PD-T?…-103, -104, -106 (identities whose terms are measured).

## Checks

Commands in `topics/bivariate-lanczos-20261031/directions/L1/R01.md` §6 and `R02.md` §5. Independent rerun: none yet.

## Sources

None (own measurements). Zaccaron 2014 Table 2.1 (as reported in two inconsistent accounts, LIT?…-029) shows loss 1.2e-13, 9.8e-9, 6.1e-3 at degrees 10, 20, 30 — an exponential profile from low degree resembling (b); its node set is not identified in the repository (UNVERIFIED; not used as evidence).

## Proof or evidence

Measured; see logs. Representative: square (M = 1681, seed 11) n = 24: loss 8e-14, P = 7e-14, u/ρ_Z = 6e-14; rotated 0.3: loss 5e-6, P = 2e-5, u/ρ_Z = 6e-14; disk: loss 1e-8, P = 1e-8, u/ρ_Z = 8e-15.

## Scope

The listed sets, M ≤ 6724, degrees ≤ 48, dev parent rule. "Product-aligned" is an empirical label for the listed set types, not a classifier (PD-N?…-106): exact products (tensor grids, Padua cubature below degree n_P) are covered by PD-T?…-105; random squares are near-product (coupling ≤ 0.17). The predictor (c) is a linearised simulation with the run's own coefficients; it is a diagnostic, not a bound.

## Open items

(i) Prove a relation between max|Q̂ᵀQ̂ − I| and the propagator response (PD-T?…-104 open item). (ii) Explain the triangle discrepancy (node-dependent local-error sizes vs the uniform forcing model is a candidate explanation). (iii) M-independence of the growth rate (Runs needed on AC's servers).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R02).
- 2026-10-31T23:05Z (response to reconstruction 01): corrections block added after (f).
  - Support classifier withdrawn (major finding → PD-N?…-106).
  - "Exponential" qualified as convex (minor finding, matters for R04/R05 targets).
  - Selection dependence noted (B1 → PD-N?…-105).
  - PC-2 and PC-3 folded in.
  - The original statements (a)–(f) are unchanged above.
