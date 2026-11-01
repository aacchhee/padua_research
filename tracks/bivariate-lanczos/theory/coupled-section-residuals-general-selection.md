# PD-T?bivariate-lanczos-claude-205 — For one-relation selections satisfying condition (C) (every unformed product belongs to a column created by the other operator) with an acyclic implicit-section recursion, the residuals of the two sections obey a coupled clamped recursion; the BJ case is the decoupled special case; the drift bound holds for both operators for any selection

ID kind: PD-T.
Aliases: coupled commutator residuals; general-selection shadow recursion; residual coupling C_A ← C_B Ĥ_A; drift bound for both operators.
Split from: none (generalises PD-T?…-202 parts 2, 4, 5 from the BJ selection to any selection).
Split into: none.

## Statement

[EXACT algebra on computed quantities] Graded columns (t, j) as in PD-T?…-101; a **selection** assigns to each column c = (t, j), t ≥ 1, an operator B_c ∈ {X, Y} and a parent p(c) of degree t − 1 (X·(t−1, j) if B_c = X, Y·(t−1, j−1) if B_c = Y), and the run satisfies β_c q̂_c = B_c q̂_{p(c)} − Q̂_{W_c}h_c − Q̂_{L_c}g_c − f_c (any window W_c, any reorthogonalization set L_c). For A ∈ {X, Y} and each column m of degree ≤ n−1 call the A-product of m **formed** if m = p(c) with B_c = A for some c, and define the A-section Ĥ_A column by column in increasing m:

- formed: Ĥ_Ae_m := Σ_{W_c}(h_c)_le_l + Σ_{L_c}(g_c)_le_l + β_ce_c (coefficients of that relation; if two columns c are A-children of m, any fixed one);
- unformed: Ĥ_Ae_m := (Ĥ_{B_m}Ĥ_Ae_{p(m)} − Σ_{W_m}(h_m)_lĤ_Ae_l − Σ_{L_m}(g_m)_lĤ_Ae_l)/β_m.

**Scope restriction (reconstruction 01, F1).** If m was created by A itself (B_m = A) and A·m is unformed, then (Ĥ_Ae_{p(m)})_m = β_m and the right-hand side contains β_mĤ_Ae_m: the equation is self-referential and defines nothing. The statement below therefore assumes
- **(C)** every unformed A-product belongs to a column created by the other operator (B_m ≠ A), and
- **(W)** the system of definitions above is acyclic (each Ĥ_Ae_m with A·m unformed depends only on already defined columns in some order).
dev (BJ), mirror and alt satisfy (C). Under (C), (W) is **not proved**: reconstruction 01 checked it exhaustively for all selections with n ≤ 5 and by sampling (3000 each) for n = 6..9 (well-defined ⟺ (C) in all cases), and for dev, mirror, alt up to n = 20; for BJ it is proved (PD-T?…-104 part 2: the J-columns use only T_F). The pivot-adaptive selection of PD-T?…-206 violates (C) from degree 3 on rotπ/4, rot0.3, the disk and the square (holds on the triangle up to n = 20). Remark (not a proof of (W)): the two candidate parents of a column (t, j) are (t−1, j) via X and (t−1, j−1) via Y and exactly one relation is formed; this excludes the shortest candidate cycle Ĥ_Ye_{(s,i)} ↔ Ĥ_Xe_{(s,i+1)}, because both products would have the same child (s+1, i+1).
Let C_A := AQ̂_{n−1} − Q̂Ĥ_A (columns c_{A,m}). Then, under (C) and (W):

1. Formed columns: c_{A,m} = f_c (local rounding of the relation that forms it).
2. Unformed columns: β_m c_{A,m} = B_m c_{A,p(m)} + C_{B_m}Ĥ_Ae_{p(m)} − Σ_{W_m}(h_m)_l c_{A,l} − Σ_{L_m}(g_m)_l c_{A,l} − A f_m.
3. For the BJ selection C_Y = E (all Y-products formed, part 1), so part 2 for A = X reduces to PD-T?…-202 part 2 (C_Y Ĥ_X e_p = E Ĥ_X e_p): the X-residual is driven by rounding only. For any selection in which both operators have unformed products, C_X and C_Y drive each other through the terms C_{B_m}Ĥ_Ae_{p(m)}.
4. For deg m = s: (I − Π̂_{s+1})Aq̂_m = (I − Π̂_{s+1})c_{A,m} whenever supp Ĥ_Ae_m ⊆ {deg ≤ s+1}. Independently of (C), (W) and of Ĥ (any computed nested spans, any selection): under U(s+1), max(θ_s, θ_{s+1}) ≥ max_{A∈{X,Y}} δ_A(s)/(2‖A‖₂), δ_A(s) the A-defect of the computed nested spans (PD-T?…-202 part 5, verbatim for each operator); in particular θ_LB(n) := max_{s<n} max_A δ_A(s)/(2‖A‖₂) bounds max_{s≤n} θ_s from below (not θ_n alone).

## Definitions

As in PD-T?…-202. Π̂_s projector onto the span of computed columns of degree ≤ s.

## Assumptions

β_c > 0; full column rank; exact algebra on the computed quantities; part 4's support condition holds for formed columns by the window structure (W_c ⊆ degrees ≤ deg c) and propagates to unformed columns by part 2's recursion when supp Ĥ_{B}e_m ⊆ {deg ≤ deg m + 1} for all m (induction on degree).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1–2 under (C) and (W) | PROVED | proof below |
| (C) ⟹ (W) | OPEN | checked exhaustively n ≤ 5, sampled n ≤ 9, named rules to n = 20 (reconstruction 01, `review_L2/rl2_cycles.py`); proved for BJ |
| 3 | PROVED (reading of 1–2) | |
| 4 | PROVED (routine; PD-T?…-202 parts 4–5); the drift bound needs no Ĥ and holds for every selection | |
| sizes for the dev/mirror/alt/adapt selections | MEASURED | PD-T?…-206 |

## Depends on

PD-T?…-202 (BJ case; CONDITIONAL inputs PD-T?…-101/-104 there).

## Checks

Measured counterparts (both defects δ_X, δ_Y per selection) in `tracks/bivariate-lanczos/code/L2/l2_core.py::defects` and `l2_r02_selection.py`. The recursion itself is not separately checked numerically (its BJ case is PD-T?…-104 part 3, checked by L1 and reconstruction 01).

## Sources

Selection rules: reconstruction 01 (`reviews/L1-reconstruction-01.md`, PD-T?…-109 section), BPS 2010 Remark 9 / §5 (LIT?…-302) — as origins of the rules, not of the identity.

## Proof or evidence

1. By definition of the formed column: Aq̂_m = Q̂Ĥ_Ae_m + f_c.
2. Multiply β_mq̂_m = B_mq̂_{p} − Q̂_Wh − Q̂_Lg − f_m (p = p(m)) by A and use AB_m = B_mA: β_mAq̂_m = B_m(Aq̂_p) − Σ h_lAq̂_l − Σ g_lAq̂_l − Af_m. Substitute Aq̂_l = Q̂Ĥ_Ae_l + c_{A,l} (l = p and l ∈ W ∪ L) and B_mQ̂ = Q̂Ĥ_{B_m} + C_{B_m} on the columns supporting Ĥ_Ae_p: B_m(Q̂Ĥ_Ae_p) = Q̂Ĥ_{B_m}Ĥ_Ae_p + C_{B_m}Ĥ_Ae_p. The Q̂-terms equal β_mQ̂Ĥ_Ae_m by the definition of the unformed column; what remains is part 2.
3. Immediate.
4. As PD-T?…-202 parts 4–5, applied to each A. ∎

## Scope

Identifies what a selection rule changes: the propagating operator (B_m, h_m) of each residual and the coupling between the two residuals; it does not bound either. Reorthogonalization enters only through the extra coefficients g (no reset), as in the BJ case.

## Open items

A proof of (C) ⟹ (W); a residual description for selections violating (C) (the adaptive β/‖Aq̂‖ rule), where the implicit sections must be defined differently (e.g. by least squares on all available relations); an a priori criterion bounding the coupled residual growth.

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R02), after the R02 selection pre-registration and before reading the full selection results.
- 2026-11-01T01:28:43+01:00: (reconstruction 01, HIGH finding F1) statement restricted to condition (C) and acyclicity (W); the claim "for any one-relation-per-column selection" was false. Original title: "PD-T?bivariate-lanczos-claude-205 — For any one-relation-per-column selection, the residuals of the two sections obey a coupled clamped recursion; the BJ case is the decoupled special case, and the drift bound holds for both operators". Original sentence: "(Each step uses Ĥ_A columns of smaller index and Ĥ_{B_m} columns of degree ≤ deg m; the recursion is well defined when processed by degree, formed columns of degree s being available once degree s+1 is complete and unformed ones computed in increasing j.)" Part 4 made explicit as selection-independent and as a bound on max_{s≤n} θ_s (F7). No measured verdict changes (PD-T?…-206 and PD-N?…-203 use only the part-4 bound) (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
