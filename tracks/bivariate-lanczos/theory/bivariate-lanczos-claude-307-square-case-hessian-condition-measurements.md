# PD-T?bivariate-lanczos-claude-307 — MEASURED: condition (H) on Padua and random square node sets, and LP support-radius rates

ID kind: PD-T.
Aliases: (H) survey; Padua n = 4..7 robust failure (numerical); random square sets; δ_min(ε) LP measurements.
Split from: none (measured companion of PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

MEASURED, floating point (double precision; SDP solver CLARABEL via cvxpy 1.6.0; LP solver HiGHS via scipy 1.18.1), within the scope listed:
1. Padua points (j+k even family): numerical dim S_1 = n(n+1)/2 for n = 1..7. (H) holds for n = 1, 2 (dual margin t_D = 0.0857, 0.0152). For n = 3..7 the primal SDP finds p ∈ S_1 with all node Hessians PD: λ_P = 2.87, 3.29, 12.2, 20.4, 40.7 (box-normalised coefficients in the Chebyshev tensor basis) and t_D < 0 — numerically robust failure of (H) for n = 3..7 (n = 3 is certified exactly in PD-N?…-301).
2. Random square sets (M = N_n uniform in [−1,1]², seeds 1, 2, 3): (H) holds for n = 1, 2 (all seeds); n = 3: holds for seeds 2, 3, fails for seed 1 (λ_P = 7.4e-3); n = 4..6: fails for all seeds (λ_P between 8.2e-7 and 1.5e-2; seed 3 n = 4 (λ_P = 8.2e-7, t_D = −5.9e-7) and seed 2 n = 5 (λ_P = 3.0e-5, t_D = −3.1e-7) are marginal and not resolved at solver accuracy).
3. Positivity radius of the numerical certificates (max-λ_min normalisation): p* ≥ 0 on balls of radius 0.05 (n = 3), 0.01 (n = 4), < 0.01 (n = 5) around all Padua nodes; the certificates are not optimised for radius.
4. LP rates (perturbation E = −ε ev_{z*}, z* = node_0 + r(cos 1, sin 1)): n = 1, r = 0.3: δ_min/√ε = 0.212, 0.193, 0.191, 0.191, 0.191 (ε = 1e-2..1e-6); n = 2, r = 0.03: 0.057, 0.054, 0.054, 0.054, 0.054; n = 3: minimal ℓ1 residual/ε ≈ 0.023–0.035 for all δ ∈ [0.003, 0.2] (ε = 1e-3, 1e-5), never 0. n = 1 with r = 0.03 gives δ_min/ε ≈ 2 at ε ≤ 1e-5 but those runs fail the S_1-residual reliability check (UNRELIABLE: LP tolerance comparable to the S_1-component of E) and are not evidence.

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
Independent rerun: pending.

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
