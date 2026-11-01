# PD-T?bivariate-lanczos-claude-205 — For one-relation selections satisfying condition (C) (every unformed product belongs to a column created by the other operator) with an acyclic implicit-section recursion, the residuals of the two sections obey a coupled clamped recursion; the BJ case is the decoupled special case (the selection-independent drift bound for both operators is PD-T?…-208; (C) ⟹ acyclicity is PD-T?…-209)

ID kind: PD-T.
Aliases: coupled commutator residuals; general-selection shadow recursion; residual coupling C_A ← C_B Ĥ_A. Former alias "drift bound for both operators" now belongs to PD-T?…-208.
Split from: none (generalises PD-T?…-202 parts 2, 4 from the BJ selection to (C)-selections).
Split into: PD-T?bivariate-lanczos-claude-208 (second sentence of part 4: the drift bound for both operators and any computed nested spans, PROVED; `reference-free-span-drift-lower-bound.md`); PD-T?bivariate-lanczos-claude-209 (the target "(C) ⟹ (W)", OPEN here at the audited candidate; proved there for windows/reorthogonalization sets inside the preceding columns; `condition-C-staircase-selections-acyclic-sections.md`). Mapping: `topics/bivariate-lanczos-20261031/SPLITS.md` § L2 (audit-01, L2-F4).

## Statement

[EXACT algebra on computed quantities] Graded columns (t, j) as in PD-T?…-101; a **selection** assigns to each column c = (t, j), t ≥ 1, an operator B_c ∈ {X, Y} and a parent p(c) of degree t − 1 (X·(t−1, j) if B_c = X, Y·(t−1, j−1) if B_c = Y), and the run satisfies β_c q̂_c = B_c q̂_{p(c)} − Q̂_{W_c}h_c − Q̂_{L_c}g_c − f_c (any window W_c, any reorthogonalization set L_c). For A ∈ {X, Y} and each column m of degree ≤ n−1 call the A-product of m **formed** if m = p(c) with B_c = A for some c, and define the A-section Ĥ_A column by column in increasing m:

- formed: Ĥ_Ae_m := Σ_{W_c}(h_c)_le_l + Σ_{L_c}(g_c)_le_l + β_ce_c (coefficients of that relation; if two columns c are A-children of m, any fixed one);
- unformed: Ĥ_Ae_m := (Ĥ_{B_m}Ĥ_Ae_{p(m)} − Σ_{W_m}(h_m)_lĤ_Ae_l − Σ_{L_m}(g_m)_lĤ_Ae_l)/β_m.

**Scope restriction (reconstruction 01, F1).** If m was created by A itself (B_m = A) and A·m is unformed, then (Ĥ_Ae_{p(m)})_m = β_m and the right-hand side contains β_mĤ_Ae_m: the equation is self-referential and defines nothing. The statement below therefore assumes
- **(C)** every unformed A-product belongs to a column created by the other operator (B_m ≠ A), and
- **(W)** the system of definitions above is acyclic (each Ĥ_Ae_m with A·m unformed depends only on already defined columns in some order).
dev (BJ), mirror and alt satisfy (C). Whether (C) implies (W) is split off as PD-T?…-209 (audit-01, L2-F4), where it is proved after audit-01 for windows and reorthogonalization sets inside the preceding columns, together with the characterisation of the (C)-selections as the 2^{n−1} "staircase" selections; the statement below keeps (W) as an explicit hypothesis. Corrected evidence account (audit-01 `cycles-rerun.log`): the exhaustive checks n ≤ 5 found (C) for 2, 4, 8, 16 selections, all well defined; reconstruction 01's random samples at n = 6..9 contained 5, 0, 0, 0 (C)-selections out of 3000 each, so the sampled evidence for (C) ⟹ (W) was vacuous at n = 7–9 (PD-T?…-209 explains the 2^{−(n−1)(n−2)/2} sampling probability); for BJ, (W) is also PD-T?…-104 part 2 (the J-columns use only T_F). The pivot-adaptive selection of PD-T?…-206 violates (C) from degree 3 on rotπ/4, rot0.3, the disk and the square (holds on the triangle up to n = 20). Remark (not a proof of (W)): the two candidate parents of a column (t, j) are (t−1, j) via X and (t−1, j−1) via Y and exactly one relation is formed; this excludes the shortest candidate cycle Ĥ_Ye_{(s,i)} ↔ Ĥ_Xe_{(s,i+1)}, because both products would have the same child (s+1, i+1).
Let C_A := AQ̂_{n−1} − Q̂Ĥ_A (columns c_{A,m}). Then, under (C) and (W):

1. Formed columns: c_{A,m} = f_c (local rounding of the relation that forms it).
2. Unformed columns: β_m c_{A,m} = B_m c_{A,p(m)} + C_{B_m}Ĥ_Ae_{p(m)} − Σ_{W_m}(h_m)_l c_{A,l} − Σ_{L_m}(g_m)_l c_{A,l} − A f_m.
3. For the BJ selection C_Y = E (all Y-products formed, part 1), so part 2 for A = X reduces to PD-T?…-202 part 2 (C_Y Ĥ_X e_p = E Ĥ_X e_p): the X-residual is driven by rounding only. For any selection in which both operators have unformed products, C_X and C_Y drive each other through the terms C_{B_m}Ĥ_Ae_{p(m)}.
4. For deg m = s: (I − Π̂_{s+1})Aq̂_m = (I − Π̂_{s+1})c_{A,m} whenever supp Ĥ_Ae_m ⊆ {deg ≤ s+1}. (The selection-independent drift bound that followed here — max(θ_s, θ_{s+1}) ≥ max_A δ_A(s)/(2‖A‖₂) for any computed nested spans, and θ_LB(n) ≤ max_{s≤n} θ_s — is split off unchanged as PD-T?…-208; original wording in History.)

## Definitions

As in PD-T?…-202. Π̂_s projector onto the span of computed columns of degree ≤ s.

## Assumptions

β_c > 0; full column rank; exact algebra on the computed quantities; part 4's support condition holds for formed columns by the window structure (W_c ⊆ degrees ≤ deg c) and propagates to unformed columns by part 2's recursion when supp Ĥ_{B}e_m ⊆ {deg ≤ deg m + 1} for all m (induction on degree).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1–2 under (C) and (W) | PROVED | proof below |
| (C) ⟹ (W) | split off: PD-T?…-209 (OPEN at the audited candidate; PROVED there after audit-01 under (P): windows/reorthogonalization sets inside the preceding columns; pending audit) | PD-T?…-209 |
| 3 | PROVED (reading of 1–2) | |
| 4 (defect = projected residual) | PROVED (minor routine; proof below) | |
| drift bound for both operators, any selection (former second sentence of 4) | split off: PD-T?…-208, PROVED | PD-T?…-208 |
| sizes for the dev/mirror/alt/adapt selections | MEASURED | PD-T?…-206 |

## Depends on

PD-T?…-202 (BJ case; CONDITIONAL inputs PD-T?…-101/-104 there). PD-T?…-209 discharges (W) for (C)-selections satisfying its hypothesis (P); the statement here does not depend on it, because it keeps (W) as a hypothesis.

## Checks

Measured counterparts (both defects δ_X, δ_Y per selection) in `tracks/bivariate-lanczos/code/L2/l2_core.py::defects` and `l2_r02_selection.py`. The recursion itself is not separately checked numerically (its BJ case is PD-T?…-104 part 3, checked by L1 and reconstruction 01). Independent checks recorded after audit-01: Codex audit-01 reconstructed parts 1–2 under (C) + (W) (multiply the creator relation by A, commute the diagonal operators, substitute the formed/unformed definitions) and confirmed that without (C) the definition is self-referential; its rerun of reconstruction 01's exact checker (`topics/bivariate-lanczos-20261031/audit-01/L2/exact-rerun.log`) gives exact rational part 1–2 residual 0 over 18 columns in six BJ/alt cases (one-pass window, CGS2-against-all, partial reorthogonalization, with and without injected errors), and cyclic definitions for arbitrary random (non-(C)) selections, as expected. Structural (C)/(W) checks: PD-T?…-209.

## Sources

Selection rules: reconstruction 01 (`reviews/L1-reconstruction-01.md`, PD-T?…-109 section), BPS 2010 Remark 9 / §5 (LIT?…-302) — as origins of the rules, not of the identity.

## Proof or evidence

1. By definition of the formed column: Aq̂_m = Q̂Ĥ_Ae_m + f_c.
2. Multiply β_mq̂_m = B_mq̂_{p} − Q̂_Wh − Q̂_Lg − f_m (p = p(m)) by A and use AB_m = B_mA: β_mAq̂_m = B_m(Aq̂_p) − Σ h_lAq̂_l − Σ g_lAq̂_l − Af_m. Substitute Aq̂_l = Q̂Ĥ_Ae_l + c_{A,l} (l = p and l ∈ W ∪ L) and B_mQ̂ = Q̂Ĥ_{B_m} + C_{B_m} on the columns supporting Ĥ_Ae_p: B_m(Q̂Ĥ_Ae_p) = Q̂Ĥ_{B_m}Ĥ_Ae_p + C_{B_m}Ĥ_Ae_p. The Q̂-terms equal β_mQ̂Ĥ_Ae_m by the definition of the unformed column; what remains is part 2.
3. Immediate.
4. Aq̂_m = Q̂Ĥ_Ae_m + c_{A,m} by the definition of C_A, and Q̂Ĥ_Ae_m ∈ Ŝ_{s+1} under the support condition; apply I − Π̂_{s+1}. ∎ (The drift bound is proved in PD-T?…-208.)

## Scope

Identifies what a selection rule changes: the propagating operator (B_m, h_m) of each residual and the coupling between the two residuals; it does not bound either. Reorthogonalization enters only through the extra coefficients g (no reset term), as in the BJ case; as there, this form of the recursion gives no lower bound on the residuals (PD-T?…-202 Scope, audit-01 L2-F1).

## Open items

A residual description for selections violating (C) (the adaptive β/‖Aq̂‖ rule), where the implicit sections must be defined differently (e.g. by least squares on all available relations); an a priori criterion bounding the coupled residual growth. ((C) ⟹ (W): PD-T?…-209.)

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02), after the R02 selection pre-registration and before reading the full selection results.
- 2026-11-01T01:28:43+01:00: (reconstruction 01, HIGH finding F1) statement restricted to condition (C) and acyclicity (W); the claim "for any one-relation-per-column selection" was false. Original title: "PD-T?bivariate-lanczos-claude-205 — For any one-relation-per-column selection, the residuals of the two sections obey a coupled clamped recursion; the BJ case is the decoupled special case, and the drift bound holds for both operators". Original sentence: "(Each step uses Ĥ_A columns of smaller index and Ĥ_{B_m} columns of degree ≤ deg m; the recursion is well defined when processed by degree, formed columns of degree s being available once degree s+1 is complete and unformed ones computed in increasing j.)" Part 4 made explicit as selection-independent and as a bound on max_{s≤n} θ_s (F7). No measured verdict changes (PD-T?…-206 and PD-N?…-203 use only the part-4 bound) (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, finding **L2-F4**, and claim-coverage note on the cycle evidence; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) The explicitly OPEN target "(C) ⟹ (W)" split off as PD-T?…-209 (proved there under (P) after audit-01; pending audit); the selection-independent drift bound (second sentence of part 4) split off unchanged as PD-T?…-208; the conditional theorem under (C) and (W) is retained exactly. Original sentence of the statement: "Under (C), (W) is **not proved**: reconstruction 01 checked it exhaustively for all selections with n ≤ 5 and by sampling (3000 each) for n = 6..9 (well-defined ⟺ (C) in all cases), and for dev, mirror, alt up to n = 20; for BJ it is proved (PD-T?…-104 part 2: the J-columns use only T_F)." — the parenthesis "(well-defined ⟺ (C) in all cases)" overstated the sampled evidence (no (C)-selection was sampled at n = 7–9). Original part 4: "4. For deg m = s: (I − Π̂_{s+1})Aq̂_m = (I − Π̂_{s+1})c_{A,m} whenever supp Ĥ_Ae_m ⊆ {deg ≤ s+1}. Independently of (C), (W) and of Ĥ (any computed nested spans, any selection): under U(s+1), max(θ_s, θ_{s+1}) ≥ max_{A∈{X,Y}} δ_A(s)/(2‖A‖₂), δ_A(s) the A-defect of the computed nested spans (PD-T?…-202 part 5, verbatim for each operator); in particular θ_LB(n) := max_{s<n} max_A δ_A(s)/(2‖A‖₂) bounds max_{s≤n} θ_s from below (not θ_n alone)." Original proof of 4: "4. As PD-T?…-202 parts 4–5, applied to each A. ∎" (now a self-contained one-line proof of the first sentence). Original status rows: "| (C) ⟹ (W) | OPEN | checked exhaustively n ≤ 5, sampled n ≤ 9, named rules to n = 20 (reconstruction 01, `review_L2/rl2_cycles.py`); proved for BJ |" and "| 4 | PROVED (routine; PD-T?…-202 parts 4–5); the drift bound needs no Ĥ and holds for every selection | |". Original title: "PD-T?bivariate-lanczos-claude-205 — For one-relation selections satisfying condition (C) (every unformed product belongs to a column created by the other operator) with an acyclic implicit-section recursion, the residuals of the two sections obey a coupled clamped recursion; the BJ case is the decoupled special case; the drift bound holds for both operators for any selection". Original alias list included "drift bound for both operators"; original Split from: "none (generalises PD-T?…-202 parts 2, 4, 5 from the BJ selection to any selection)."; original Split into: "none."; original Scope sentence: "Reorthogonalization enters only through the extra coefficients g (no reset), as in the BJ case."; original Open items began "A proof of (C) ⟹ (W);". Checks: audit-01 reruns recorded. Status PROVED unchanged (the remaining statement parts 1–4 are PROVED).
