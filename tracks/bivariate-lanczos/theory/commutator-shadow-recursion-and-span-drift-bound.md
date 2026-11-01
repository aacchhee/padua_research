# PD-T?bivariate-lanczos-claude-202 — J-part of the section theorem: the in-span commutator residual obeys the F-step ω-recursion with clamped J-columns, in which reorthogonalization coefficients enter only as further coefficients (no reset term; this bounds nothing from below — that the residual stays large under the tested schemes is measured, PD-N?…-201), and the J-defect equals the projected residual (the drift lower bound formerly part 5 is PD-T?…-208)

ID kind: PD-T.
Aliases: commutator obstruction (identities only; see Scope); shadow ω-recursion; K-recursion; J-section decomposition; L2-Q1(b) J-part (identities). Former alias "drift lower bound θ ≥ δ_J/(2‖J‖)" now belongs to PD-T?…-208.
Split from: none (the J-part of the L2-Q1(b) target; the measured failure is PD-N?…-201).
Split into: PD-T?bivariate-lanczos-claude-208 (former part 5, the reference-free drift lower bound, PROVED; `reference-free-span-drift-lower-bound.md`); PD-T?bivariate-lanczos-claude-210 (the universal statement formerly in Scope, "no reorthogonalization rule can by itself make the implicit J-section accurate or the computed spaces J-closed", OPEN; `bj-universal-reorthogonalization-obstruction-open.md`). Mapping: `topics/bivariate-lanczos-20261031/SPLITS.md` § L2 (audit-01, L2-F1/L2-F4).

## Statement

[EXACT algebra on computed quantities] Setting and notation of PD-T?…-201 (BJ ordering, block window, relations (H1) for F with reorthogonalization terms (L_k, g_k)); in addition each J-column relation, k = (t+1, 0), c = (t, 0):

  β_k q̂_k = J q̂_c − Q̂_{W_k}h_k − Q̂_{L_k}g_k − f_k,   τ̃_c := Σ_{W_k}(h_k)_l e_l + Σ_{L_k}(g_k)_l e_l + β_k e_k.

Define the implicit J-section Ĥ (N × N_{n−1}) by Ĥe_c := τ̃_c for c = (t,0) and, for c = (t, j ≥ 1) created by k′ = c from parent p = (t−1, j−1) with coefficients (h, g, β) of c's own relation,

  β Ĥe_c := (T + G)Ĥe_p − Σ_{l∈W_c}h_lĤe_l − Σ_{l∈L_c}g_lĤe_l   (all reorthogonalization coefficients included),

and C := JQ̂_{n−1} − Q̂Ĥ (commutator residual), K := Q̂ᵀC (in-span part). Then:

1. **(J-section decomposition.)** W_nᵀJW_{n−1} − Ĥ = (ΔĤ − ĤΔ′)R′⁻¹ + R⁻ᵀKR′⁻¹.
2. **(Residual recursion, with reorthogonalization.)** c_{(t,0)} = f_{(t+1,0)}, and for c = (t, j ≥ 1) with parent p: β c_c = F c_p − Σ_{l∈W_c}h_l c_l − Σ_{l∈L_c}g_l c_l + EĤe_p − J f_c.
3. **(Shadow recursion.)** For every row m of degree ≤ n−1 and c = (t, j ≥ 1) of degree ≤ n−1:
   β K_{m,c} = Σ_a (T + G)_{am} K_{a,p} − Σ_{l∈W_c}h_l K_{m,l} − Σ_{l∈L_c}g_l K_{m,l} + σ_{m,c},  σ_{m,c} := (Ee_m)ᵀc_p + q̂_mᵀEĤe_p − q̂_mᵀJf_c,
   and K_{m,(t,0)} = q̂_mᵀf_{(t+1,0)}. The Gram matrix Γ := Q̂ᵀQ̂ (= I + Ω) satisfies, for the same (m, c), the F-step ω-identity β Γ_{m,c} = Σ_a (T + G)_{am}Γ_{a,p} − Σ_{W_c}h_lΓ_{m,l} − Σ_{L_c}g_lΓ_{m,l} + s_{m,c}, s_{m,c} := (Ee_m)ᵀq̂_p − q̂_mᵀf_c (PD-T?…-106 with reorthogonalization terms). **K and Γ are driven by the same linear operator** (acting on the column index, with the same coefficients); they differ in the sources, in the clamped J-columns of K, and in that the reorthogonalization coefficients g are chosen to cancel Γ_{L_c,c} — they enter K's recursion only as further coefficients (−Σ g_lK_{m,l}), and the recursion contains no term that resets K. This is a statement about the form of the recursion only: it gives no lower bound on K, and K does change with g.
4. **(J-defect.)** For deg l = s ≤ n−1: (I − Π̂_{s+1})Jq̂_l = (I − Π̂_{s+1})c_l, Π̂_s the orthogonal projector onto Ŝ_s := span{q̂_b : deg b ≤ s}. Hence the J-defect δ_J(s) := max over the orthonormal degree-s columns w of W of ‖(I − Π̂_{s+1})Jw‖ satisfies δ_J(s) ≤ ‖R⁻¹‖₂ max_{deg l ≤ s}‖c_l‖·√(N_s).
5. **(Drift lower bound.)** Split off after audit-01 (L2-F4): now **PD-T?bivariate-lanczos-claude-208** (`reference-free-span-drift-lower-bound.md`), stated there for any operator A ∈ {X, Y} and any computed nested spans, with the J/BJ form of this part as its special case; statement and proof unchanged (original wording preserved in History below).

## Definitions

As in PD-T?…-201 and PD-T?…-104 (whose Ĥ_J and C_res are the case L = ∅). ‖J‖₂ = max_i|x_i|.

## Assumptions

Full column rank of Q̂; β > 0 in every relation; exact arithmetic on the computed quantities for parts 1–4. (The U(s+1) hypothesis of former part 5 moved with it to PD-T?…-208.)

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. decomposition | PROVED | proof below |
| 2. residual recursion with reorthogonalization | PROVED (extends PD-T?…-104 part 3 to L ≠ ∅) | proof below |
| 3. shadow recursion and comparison with the ω-identity | PROVED | proof below |
| 4. J-defect = projected residual | PROVED (minor routine step of this file's argument; proposed classification: no other result cites it — PD-T?…-205 part 4 restates and proves its own generalisation, and the measured files use only PD-T?…-208) | proof below |
| 5. drift lower bound | split off: PD-T?…-208, PROVED (substantive: PD-N?…-201, -203, -204, PD-T?…-205, -206, -207 depend on it; audit-01 L2-F4) | PD-T?…-208 |
| universal reading "no reorthogonalization rule can make the J-section accurate / the spaces J-closed" | not a consequence of parts 1–3; OPEN target PD-T?…-210 (audit-01 L2-F1) | PD-T?…-210 |
| size of K, C, δ_J under reorthogonalization | MEASURED (PD-N?…-201) | exponential growth on non-product benchmarks with full CGS2 (tested schemes only) |

## Depends on

PD-T?…-101 (supports), PD-T?…-104 parts 2–4 (case L = ∅), PD-T?…-106 (ω-identity) — CONDITIONAL inputs (developer results; reconstruction 01: CONFIRMED). PD-T?…-201 (notation, Lemma 1 pattern).

## Checks

`tracks/bivariate-lanczos/code/L2/l2_core.py::coef_mats` builds Ĥ with the reorthogonalization coefficients as in the statement; `section_errors` reports max‖c_l‖, max|K|, δ_J(s) and δ_F(s) (the F-defect, which stays at 1e-15 on every run, as part 2 of PD-T?…-102 predicts). The identities themselves are not re-checked numerically here (PD-T?…-104 part 3 was checked in long double by L1 and reconstructed exactly). Independent checks recorded after audit-01: Codex audit-01 reconstructed the decomposition, the commutator/source terms and the Gram comparison (signs and reorthogonalization coefficients consistent) and reran reconstruction 01's exact checker (`tracks/bivariate-lanczos/code/review_L2/rl2_exact.py` → `topics/bivariate-lanczos-20261031/audit-01/L2/exact-rerun.log`): exact rational part 3 shadow residual, K(t,0) residual and Gram-identity residual 0 for BJ with one-pass window, CGS2-against-all and partial reorthogonalization (with and without injected errors); 80-digit part 1 decomposition residual ≤ 1.6e-81 and part 4 projected-identity residuals ≤ 1.3e-81.

## Sources

None.

## Proof or evidence

1. W_nᵀJW_{n−1} = R⁻ᵀQ̂ᵀ(Q̂Ĥ + C)R′⁻¹ = RĤR′⁻¹ + R⁻ᵀKR′⁻¹, and RĤR′⁻¹ − Ĥ = (ΔĤ − ĤΔ′)R′⁻¹ (PD-T?…-201 Lemma 1).
2. (t,0): Jq̂_{(t,0)} = Q̂τ̃ + f_{(t+1,0)} by the J-relation. (t, j ≥ 1): multiply β q̂_c = Fq̂_p − Q̂_{W}h − Q̂_{L}g − f_c by J, use JF = FJ, substitute Jq̂_b = Q̂Ĥe_b + c_b for b = p and b ∈ W ∪ L, and FQ̂ = Q̂(T + G) + E on the columns of degree ≤ t (Ĥe_p is supported there by induction: supp Ĥe_b ⊆ {deg ≤ deg b + 1}). The Q̂-terms equal βQ̂Ĥe_c by the definition of Ĥ; the rest is the stated right-hand side.
3. Multiply part 2 by q̂_mᵀ: q̂_mᵀFc_p = (Fq̂_m)ᵀc_p = (Q̂(T+G)e_m + Ee_m)ᵀc_p = Σ_a(T+G)_{am}K_{a,p} + (Ee_m)ᵀc_p (deg m ≤ n−1, so m's F-relation exists); the other terms give −Σ h_lK_{m,l} − Σ g_lK_{m,l} + q̂_mᵀEĤe_p − q̂_mᵀJf_c. The Γ-identity is the same computation applied to the relation of c itself: β q̂_mᵀq̂_c = q̂_mᵀ(Fq̂_p − Q̂_Wh − Q̂_Lg − f_c) and q̂_mᵀFq̂_p = (Q̂(T+G)e_m + Ee_m)ᵀq̂_p = Σ_a(T+G)_{am}Γ_{a,p} + (Ee_m)ᵀq̂_p. (Written with Γ, not Ω = Γ − I: in terms of Ω the identity acquires the mirror-entry difference (T+G)_{pm} − (coefficient of q̂_m in the relation of c), which is O(ε_c) but not zero.) Reading: the operator acting on the column index is identical; in an orthogonalization step the coefficients g (L ≠ ∅) are chosen from Q̂_Lᵀr, which makes Γ_{L,c} = O(u), whereas K_{L,c} = Σ_a(T+G)_{aL}K_{a,p} − ... is unaffected by that choice except through the extra terms −Σ g_lK_{m,l} (size ‖g‖·‖K‖).
4. Q̂Ĥe_l ∈ Ŝ_{s+1} (support of Ĥe_l in degrees ≤ s+1), so (I − Π̂_{s+1})Jq̂_l = (I − Π̂_{s+1})c_l. A degree-s column of W is w = Σ_{b≤l}(R⁻¹)_{bl}q̂_b with deg b ≤ s; Jw = Σ(R⁻¹)_{bl}Jq̂_b and the bound follows by Cauchy–Schwarz. ∎
5. Proof moved to PD-T?…-208.

## Scope

Parts 1–3 say exactly where semi-orthogonality stops helping for the J-section: the error W_nᵀJW_{n−1} − Ĥ contains R⁻ᵀKR′⁻¹, an additional residual that semi-orthogonality alone does not control. K is propagated by the same operator as the loss of orthogonality; reorthogonalization enters its recursion only through the further coefficients −Σ g_lK_{m,l}, and the recursion has no term that resets K (in contrast with the Gram entries Γ_{L_c,c}, which the choice of g makes O(u)). These identities establish no lower bound on K and no invariance of K under the choice of g; they do **not** prove that every reorthogonalization rule fails to make the implicit J-section accurate or the computed spaces J-closed (that universal statement is the OPEN target PD-T?…-210). The failure of the **tested** reorthogonalization schemes (plain, two-pass window, oracle partial, CGS2 against all previous columns, PRO-2D-J; BJ selection) is MEASURED in PD-N?…-201 and PD-T?…-207 (b). Whether K stays small is a property of the propagator (on product-type measures, PD-T?…-105/-111, it does in the measured cases; on the tested non-product measures it grows, PD-N?…-201). The reference-free lower bound converting a computable defect into a bound on the distance of the computed spaces from S_n is PD-T?…-208.

## Open items

A priori growth bound for K under the clamped recursion (equivalently for the clamped F-marching of PD-T?…-104 part 3); whether a different selection rule (reconstruction 01: balanced or pivot-adaptive) keeps K and both defects at rounding level (L2 R02: measured in PD-T?…-206); whether any reorthogonalization rule with the BJ selection keeps K small on non-product measures (PD-T?…-210, OPEN).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01). Parts 1–4 were derived before the R01 section suite (as the intended obstruction route, candidates.md IDEA?…-203); part 5 was added after the rotπ/4 smoke test showed the pre-registered drift reference to be non-discriminating (disclosed, candidates.md amendment to IDEA?…-204).
- 2026-11-01T01:28:43+01:00: title reworded (reconstruction 01 wording note: "does not reset it" is an interpretation of part 3; part 3 proves only that g enters as coefficients, the size of K is MEASURED). Original title: "J-part of the section theorem: the in-span commutator residual obeys the F-step ω-recursion with clamped J-columns, reorthogonalization does not reset it, and the J-defect bounds the drift of the computed spaces from S_n from below". Statement and status unchanged (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, findings **L2-F1** and **L2-F4**; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) **L2-F1:** the universal deduction in Scope removed and registered as the OPEN target PD-T?…-210; Scope now limits the implication of parts 1–3 to an additional residual not controlled by semi-orthogonality alone and attaches the failure of the tested schemes to MEASURED PD-N?…-201. Original Scope: "Parts 1–3 say exactly where semi-orthogonality stops helping for the J-section: the error W_nᵀJW_{n−1} − Ĥ contains R⁻ᵀKR′⁻¹, and K is propagated by the same operator as the loss of orthogonality but is not acted on by reorthogonalization. Hence no reorthogonalization rule can by itself make the implicit J-section accurate or the computed spaces J-closed; whether K stays small is a property of the propagator (on product-type measures, PD-T?…-105/-111, it does in the measured cases; on non-product measures it grows, PD-N?…-201). Part 5 converts a computable defect into a reference-free lower bound for the distance of the computed spaces from S_n." Part 3's last clause reworded; original: "— they enter K's recursion only as further coefficients and do not reset K." **L2-F4:** part 5 (substantive: other results depend on it) split off unchanged as PD-T?…-208; original part 5: "5. **(Drift lower bound.)** [EXACT, for the exact graded spaces] Assume U(s+1) (no nonzero polynomial of degree ≤ s+1 vanishes on all nodes) and let P_s be the orthogonal projector onto S_s = {p(X,Y)√w : deg p ≤ s}, θ_s := ‖Π̂_s − P_s‖₂ (sine of the largest principal angle; dim Ŝ_s = dim S_s = N_s). Then ‖(I − Π̂_{s+1})JΠ̂_s‖₂ ≤ ‖J‖₂(θ_s + θ_{s+1}); in particular max(θ_s, θ_{s+1}) ≥ δ_J(s)/(2‖J‖₂)."; original proof of part 5: "5. U(s+1) gives JS_s ⊆ S_{s+1} with dim S_{s+1} = N_{s+1}, so (I − P_{s+1})JP_s = 0 and (I − Π̂_{s+1})JΠ̂_s = (P_{s+1} − Π̂_{s+1})JΠ̂_s + (I − P_{s+1})J(Π̂_s − P_s). ∎"; original status row: "| 5. drift lower bound | PROVED (minor routine) | proof below |"; original Assumptions: "Full column rank of Q̂; β > 0 in every relation; exact arithmetic on the computed quantities for parts 1–4; part 5 additionally U(s+1) so that dim S_{s+1} = N_{s+1}."; original Split into: "none."; original alias list included "drift lower bound θ ≥ δ_J/(2‖J‖)". Title updated accordingly; original title: "PD-T?bivariate-lanczos-claude-202 — J-part of the section theorem: the in-span commutator residual obeys the F-step ω-recursion with clamped J-columns, in which reorthogonalization coefficients enter only as further coefficients (no reset term; that the residual stays large is measured, PD-N?…-201), and the J-defect bounds the drift of the computed spaces from S_n from below". Part 4 classified as a minor routine step (proposal; auditor to check). Checks: audit-01 reruns recorded; original Open items: "A priori growth bound for K under the clamped recursion (equivalently for the clamped F-marching of PD-T?…-104 part 3); whether a different selection rule (reconstruction 01: balanced or pivot-adaptive) keeps K and both defects at rounding level (L2 R02)." Parts 1–4 statements and proofs unchanged; status PROVED unchanged.
