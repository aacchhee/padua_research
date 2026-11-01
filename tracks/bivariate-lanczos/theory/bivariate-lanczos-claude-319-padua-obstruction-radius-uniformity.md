# PD-T?bivariate-lanczos-claude-319 — PARTIAL ((U1) PROVED in PD-T144; (U2) OPEN): dependence on n of the Padua obstruction radius (does the positivity radius of P_n tend to 0? is there an obstruction radius uniform in n?)

Final ID: **PD-T075** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: δ_0(n) asymptotics; uniform obstruction radius; "no radius uniform in n" (withdrawn wording); positivity radius ρ_n of P_n; maximal obstruction radius δ_obs(n).
Split from: PD-T?bivariate-lanczos-claude-313 (Open items) and PD-N?bivariate-lanczos-claude-303 (Statement), pre-audit wording: 313 «So δ_0(n) → 0 with n (roughly n⁻³ in the sampled column): the obstruction holds for each n, with no radius uniform in n.»; N303 «The radius δ_0(n) shrinks with n (rigorous reviewer bounds 5.63e-4 … 6.55e-8 for n = 4..12, PD-T?…-313 Open items), so the obstruction is per degree, not uniform in n.»
Split into: PD-T144 (original subquestion (U1), PROVED: ρ_n = O(n^-5), limsup n^5 ρ_n ≤ 20√2π⁴/9). (U2) is not split and remains OPEN in this file.

## Statement

For the Padua points 𝒫_n = {(cos jπ/n, cos kπ/(n+1)) : j + k even} and K_δ(n) := ∪_{z ∈ 𝒫_n} B̄(z, δ), define
- ρ_n := sup{δ ≥ 0 : P_n ≥ 0 on K_δ(n)} (n ≥ 4), the positivity radius of the certificate P_n of PD-T?…-313;
- δ_obs(n) := sup{δ ≥ 0 : some nonzero p ∈ Π_{2n+1} with p ≥ 0 on K_δ(n) vanishes at every node of 𝒫_n} (n ≥ 1), the maximal obstruction radius; by PD-T?…-302(b1) and 303 it equals sup{δ : r(δ) = 0} for any positive weights, i.e. the largest radius up to which, for every small ε, some ε-perturbation given as data is not exactly representable on K_δ (reading (E)).
Open questions: (U1) does ρ_n → 0 as n → ∞? (U2) is inf_{n ≥ 3} δ_obs(n) > 0 (an obstruction radius uniform in n)?

## Definitions

As in PD-T?…-302, 303, 313. A "chosen radius δ_0(n)" in PD-T?…-303(e), 313, PD-N?…-301/303 is any δ_0(n) ∈ (0, δ_obs(n)] for which the stated obstruction holds; it is an existential choice, not an optimal radius.

## Assumptions

[EXACT]; Padua unisolvence for Π_n where sections are needed (as in PD-N?…-303); (U1) does not need it.

## Status by part

Overall status: PARTIAL: original subquestion (U1) is PROVED in split result PD-T144; original subquestion (U2) remains OPEN. This is a decomposition of the original target, not aggregation with a supporting lemma.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (U1) ρ_n → 0 | PROVED | PD-T144: explicit eventual negative witness gives rho_n=O(n^-5) and limsup n^5 rho_n <=20sqrt(2)pi^4/9; analytic proof independently reconstructed |
| (U2) inf_n δ_obs(n) > 0 | OPEN | no evidence either way: certified bounds concern one certificate P_n and are lower bounds |

Minor routine facts (labelled individually, excluded from the status): 0 < ρ_n ≤ δ_obs(n) for n ≥ 4 (P_n is one admissible p; ρ_n > 0 by PD-T?…-303(e) and 313) — PROVED (routine); δ_obs(3) > 0 (PD-N?…-301) — PROVED; a chosen radius may always be taken nonincreasing in n (replace δ_0(n) by min_{3 ≤ k ≤ n} δ_0(k)) — PROVED (routine), and says nothing about ρ_n or δ_obs(n).

## Depends on

PD-T?…-302(b1), 303(e), 313, PD-N?…-301, 303.

## Checks

Evidence only (not claims of this file):
- Certified lower bounds b_n ≤ ρ_n (interval/rational arithmetic, reviewer code `tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py`, L3-reconstruction-02, log `topics/bivariate-lanczos-20261031/reviews/logs_L3b/padua_delta0.log`; fresh rerun by Codex audit-01 L3-certificates `python3 -I -B tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py 4 12`, log `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_delta0.log`, identical bounds): b_n = 5.6302e-4, 1.0225e-4, 2.3627e-5, 6.6062e-6, 2.1471e-6, 7.8710e-7, 3.1825e-7, 1.3955e-7, 6.5495e-8 for n = 4..12, binding node (j, k) = (1, 1) in every case. The reduction behind these bounds was not re-derived by the developer; they are cited as reviewer computations. Decreasing lower bounds cannot bound ρ_n or δ_obs(n) from above.
- MEASURED (floating sampling in the same reviewer runs, 720 directions, geometric radii): the first sampled radius around the binding node with min P_n < 0 on the circle is 3.372e-2, 1.433e-2, 6.631e-3, 3.490e-3, 2.088e-3, 1.099e-3, 7.475e-4, 7.162e-4, 3.460e-4 (n = 4..12). If certified, these would be upper bounds on ρ_n only. Descriptive least-squares log–log slope over n = 4..12 (developer, from the printed values): −4.1 for the sampled column (the earlier text said "roughly n⁻³", which this fit does not support), −8.3 for the certified lower bounds; nine values, no model selection, no asymptotic claim.

## Sources

None.

## Proof or evidence

(U1) is proved in split result PD-T144 by zeta_n=(cos(pi/n+a/n^4),cos(pi/(n+1)+a/n^4)), a=20pi^3/9: n^14 P_n(zeta_n) tends to -6400pi^12/729 and n^5 times its distance to the (1,1) node tends to 20sqrt(2)pi^4/9. No matching lower rate or explicit finite negativity threshold is claimed. (U2) stays OPEN. In particular rho_n<=delta_obs(n), so this upper bound for rho_n does not upper-bound delta_obs(n) or disprove a uniform obstruction radius. The earlier certified lower bounds and sampled measurements remain historical evidence, not the proof of decay.

## Scope

Padua family only; the question concerns the dependence on n of the radius, not the existence of the per-degree obstruction (PROVED: PD-N?…-301 for n = 3, PD-N?…-303 for n ≥ 4 under unisolvence).

## Open items

(1) Certify the sampled negative values exactly (rational point ζ_n, exact sign of P_n(ζ_n), rigorous distance to 𝒫_n) for n = 4..12: this would give rigorous finite upper bounds on ρ_n, still not (U1). (2) Resolved: (U1) is PROVED in split result PD-T144 by an explicit eventual corner witness at the (1, 1) node (ρ_n = O(n^-5)). A matching lower rate for ρ_n is not part of (U1) and remains open there. (3) (U2) needs information about all obstruction certificates, e.g. the existence for fixed δ and large n of a nonzero p ∈ Π_{2n+1} that is ≥ 0 on K_δ(n) ⊇ [−1, 1]² and vanishes on 𝒫_n.

## History

- 2026-11-01T08:33:39+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: created per finding LC-M1 of Codex audit-01 (topics/bivariate-lanczos-20261031/audit-01/L3-certificates.md; candidate 5ccfac2), which disputes the inference "δ_0(n) → 0 … no radius uniform in n" from finite lower bounds and sampled negative values (accepted in response-recon-02 as finding L7 of L3-reconstruction-02). The withdrawn wording is quoted in "Split from"; the stronger statements are recorded here as OPEN questions (U1), (U2), distinguishing a chosen radius, ρ_n and δ_obs(n) as the audit requested.
- 2026-11-01, Claude PR preparation (configured claude-opus-5-5, high): original subquestion (U1) split to PD-T144 (PROVED; Claude audit-01 CONFIRMED, topics/padua-lanczos-drift-20261101/audit-01.md). Overall status OPEN → PARTIAL ((U1) PROVED under the split ID, (U2) OPEN, an explicit decomposition of this file's own Statement); the (U1) row OPEN → PROVED; title, "Split into", Open item (2) and "Proof or evidence" updated. The Statement's questions (U1), (U2) are unchanged. Original wording: title «… — OPEN: dependence on n of the Padua obstruction radius …»; «Overall status: OPEN.»; «| (U1) ρ_n → 0 | OPEN | reviewer-certified lower bounds and floating samples below; no all-n argument |»; «Split into: none.»; «(2) An all-n argument for (U1), e.g. from growth of the third derivatives of P_n near the corner nodes versus the decay of λ_min(Hess P_n) at (j, k) = (1, 1).»; «No proof. The routine facts follow from the definitions.».
