# PD-T?bivariate-lanczos-claude-307 — MEASURED: condition (H) on Padua and random square node sets, and LP support-radius rates

ID kind: PD-T.
Aliases: (H) survey; Padua n = 4..7 robust failure (numerical); random square sets; δ_min(ε) LP measurements.
Split from: none (measured companion of PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

MEASURED, floating point (double precision; SDP solver CLARABEL via cvxpy 1.6.0; LP solver HiGHS via scipy 1.18.1), within the scope listed:
1. Padua points (j+k even family): numerical dim S_1 = n(n+1)/2 for n = 1..7. (H) holds for n = 1, 2 (dual margin t_D = 0.0857, 0.0152). For n = 3..7 the primal SDP finds p ∈ S_1 with all node Hessians PD: λ_P = 2.87, 3.29, 12.2, 20.4, 40.7 (box-normalised coefficients in the Chebyshev tensor basis) and t_D < 0 — numerically robust failure of (H) for n = 3..7 (n = 3 is certified exactly in PD-N?…-301).
2. Random square sets (M = N_n uniform in [−1,1]², seeds 1, 2, 3): (H) holds for n = 1, 2 (all seeds); n = 3: holds for seeds 2, 3, fails for seed 1 (λ_P = 7.4e-3); n = 4..6: robust failure in 7 of the 9 cases (λ_P between 8.2e-7 and 1.5e-2; seed 3 n = 4 (λ_P = 8.2e-7, t_D = −5.9e-7) and seed 2 n = 5 (λ_P = 3.0e-5, t_D = −3.1e-7) are marginal and not resolved at solver accuracy).
3. Positivity radius of the numerical certificates (max-λ_min normalisation): p* ≥ 0 on balls of radius 0.05 (n = 3), 0.01 (n = 4), < 0.01 (n = 5) around all Padua nodes; the certificates are not optimised for radius.
4. LP rates (perturbation E = −ε ev_{z*}, z* = node_0 + r(cos 1, sin 1)): n = 1, r = 0.3: δ_min/√ε = 0.212, 0.193, 0.191, 0.191, 0.191 (ε = 1e-2..1e-6); n = 2, r = 0.03: 0.057, 0.054, 0.054, 0.054, 0.054; n = 3: minimal ℓ1 residual/ε ≈ 0.023–0.035 over the tested nested grids for δ ∈ [0.003, 0.2] (ε = 1e-3, 1e-5). A grid residual is an UPPER bound on the true minimal residual over K_δ, so it is evidence of non-representability only within the certified positivity radius of p* (developer bound 3.89e-4; reviewer interval certificate 0.04, L3-reconstruction-01); for larger δ the nonzero grid residual is not evidence. n = 1 with r = 0.03 gives δ_min/ε ≈ 2 at ε ≤ 1e-5 but those runs fail the S_1-residual reliability check (UNRELIABLE: LP tolerance comparable to the S_1-component of E) and are not evidence.

5. (Added R02.) Quadratic-generator form (PD-T?…-309): for Padua n = 1..7 and a random square set (seed 1, n = 1..6), the map C ↦ p_C on {C ⊥ Hankel} has rank n(n+1)/2 and its image coincides with the numerically computed S_1 (all principal-angle cosines 1 to ≤ 1e-15); the SDP max λ s.t. G_iᵀCG_i ⪰ λI, ‖c‖_∞ ≤ 1 gives λ ≤ 2e-11 for Padua n = 1, 2 and λ = 0.126, 0.0553, 0.0603, 0.0159, 0.0109 for n = 3..7 (same verdicts as item 1). Logs `r02_structure_padua.log`, `r02_structure_random_seed1.log`.

6. (Added R03.) Ordered Harris–Simanek checkerboards S_0 = {(X_i, Y_j) : i + j even}, |X| = n+1, |Y| = n+2 (square case; benchmark of plan.md, source codex/charter-unisolvence-20261031@eb7bdcd PD-T001/PD-T003, NOT accepted; (H) is weight-independent so the weights are not used): Chebyshev–Lobatto X, Y (= Padua): (H) for n ≤ 2, robust failure n = 3..6 (identical numbers to item 1); equispaced X, Y: (H) holds for n = 1..5 with margins t_D = 8.6e-2, 2.0e-2, 1.8e-3, 1.3e-4, 4.8e-6, n = 6 unresolved in this floating survey (t_D = 4.6e-8, λ_P ≈ −1.6e-13) [superseded: (H) is exactly certified for n = 6, 7 (PD-T?…-310, PROVED) and n = 8 (reviewer computation)]; graded X, Y (−1 + 2t², t equispaced): (H) for n ≤ 4, n = 5, 6 unresolved (|t_D|, |λ_P| ≤ 1e-10); sorted uniform X, Y (two draws, default_rng(7)): draw 1 (H) n ≤ 4, robust failure n = 5 and marginal n = 6 (λ_P = 2.1e-6, at the 1e-6 threshold); draw 2 (H) n = 1, 2, 4, robust failure n = 3, 5, 6. So within square checkerboards the outcome depends on the node distribution, not on the count: the Chebyshev–Lobatto (Padua) case fails earliest among the deterministic families tested. Log `hs_checkerboard_condition.log` (`python3 hs_checkerboard_condition.py 6 7`).

## Definitions / Assumptions

As in PD-T?…-303. Floating point; numerical nullspaces with relative SVD threshold 1e-11; LP grids are inner approximations of K_δ.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| items 1–4 | MEASURED | logs below; no general claim |

## Depends on

PD-T?…-303 (interpretation only).

## Checks

All commands run from `tracks/bivariate-lanczos/code/L3/` (code hashes in `directions/L3/logs/code_sha256.txt`), Python 3.13.18, numpy 2.5.3, scipy 1.18.1, cvxpy 1.6.0, 2 cores; outputs in `topics/bivariate-lanczos-20261031/directions/L3/logs/`:
- `python3 hess_condition.py padua 7 0` → `hess_condition_padua.log`
- `python3 hess_condition.py random 6 s` (s = 1, 2, 3; numpy default_rng(s)) → `hess_condition_random_seed{s}.log`
- `python3 inspect_certificate.py n` (n = 3, 4, 5) → `inspect_certificate_n{n}.log`
- `python3 lp_rate.py 1 bisect 0.3` → `lp_rate_n1_r0.3.log`; `python3 lp_rate.py 1 bisect 0.03` → `lp_rate_n1_r0.03.log`; `python3 lp_rate.py 2 bisect 0.03` → `lp_rate_n2_r0.03.log`; `python3 lp_rate.py 3 resid 0.03` → `lp_resid_n3.log`; `python3 lp_rate.py 2 resid 0.03` → `lp_resid_n2.log`; `python3 lp_rate.py 3 scan 0.03 8 24` → `lp_rate_n3_scan.log` (non-nested grid and a solver time-limit reported as infeasible: superseded by the resid runs, kept as a record).
Independent reruns (prior, cited): L3-reconstruction-01 reproduced items 1, 2 (seed 1), 4 and the equispaced/graded parts of item 6 (n ≤ 5) in a Legendre basis with a different primal normalisation and different LP grids (`tracks/bivariate-lanczos/code/review_L3/indep_measured.py`, logs `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_H.log`, `indep_lp.log`), and proved S_1 = {p_C} exactly for Padua n ≤ 3 (`indep_generator_cert.py`). Codex audit-01 (L3-framework) read these records but did not rerun the LP/SDP survey (cvxpy unavailable there). Items 2 (seeds 2, 3), 3 and 5 and the sorted-uniform part of item 6 have no independent rerun. The Padua n = 4..7 part of item 1 is superseded mathematically by PD-T?…-313/PD-N?…-303 (PROVED for all n ≥ 4).

## Sources

None.

## Proof or evidence

Measurements only.

## Scope

Padua n ≤ 7; three random seeds per n ≤ 6; LP rates for one perturbation direction per n.

## Open items

Exact certificates for n ≥ 4; a structural explanation of the transition between n = 2 and n = 3 (Padua) and of the frequent failure for random square sets at n ≥ 4; worst-direction rates instead of one direction.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
- 2026-10-31T23:54:00+01:00, L3 developer: finding L5 of L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396) (marginal cases no longer counted as failures; grid residual stated as an upper bound). Independent checks: the reconstruction reproduced items 1, 2 (seed 1), 4 and 6 in a Legendre basis and proved S_1 = {p_C} exactly for Padua n ≤ 3 (upgrade of item 5 for n ≤ 3).
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «n = 4..6: fails for all seeds (λ_P between 8.2e-7 and 1.5e-2;»; «n = 3: minimal ℓ1 residual/ε ≈ 0.023–0.035 for all δ ∈ [0.003, 0.2] (ε = 1e-3, 1e-5), never 0.»; «draw 1 (H) n ≤ 4, robust failure n = 5, 6;».
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding L9 (R04 pending correction applied) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «n = 6 unresolved (t_D = 4.6e-8, λ_P ≈ −1.6e-13);».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): stale 'Independent rerun: pending' replaced by the actual rerun record (L3-framework note on stale T307 wording; LC-L1 spirit) of Codex audit-01 (audit-01/L3-framework.md; candidate 5ccfac2). Measurements unchanged; status MEASURED. Original wording of the replaced passages: «Independent rerun: pending.».
