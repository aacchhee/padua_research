# PD-T?bivariate-lanczos-claude-209 — Condition (C) holds exactly for the 2^(n−1) "staircase" one-relation selections, and for them the implicit-section definitions of PD-T?…-205 are acyclic ((C) ⟹ (W)) whenever every window and reorthogonalization set lies in the preceding columns

Final ID: **PD-T054** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: (C) ⟹ (W); acyclicity of the coupled implicit sections; staircase (monotone X/Y split) selections; former PD-T?…-205 status row "(C) ⟹ (W) | OPEN".
Split from: PD-T?bivariate-lanczos-claude-205 — the OPEN target in its status row "| (C) ⟹ (W) | OPEN | checked exhaustively n ≤ 5, sampled n ≤ 9, named rules to n = 20 (reconstruction 01, `review_L2/rl2_cycles.py`); proved for BJ |", the statement-paragraph sentence "Under (C), (W) is **not proved**: reconstruction 01 checked it exhaustively for all selections with n ≤ 5 and by sampling (3000 each) for n = 6..9 (well-defined ⟺ (C) in all cases), and for dev, mirror, alt up to n = 20; for BJ it is proved (PD-T?…-104 part 2: the J-columns use only T_F)." and the Open item "A proof of (C) ⟹ (W)". Split after Codex audit-01 finding L2-F4 (an explicitly OPEN distinct target inside a file whose overall status is PROVED).
Split into: none.

## Statement

[EXACT combinatorics on index sets; no floating point] Setting and definitions of PD-T?…-205: graded columns (t, j), 0 ≤ j ≤ t ≤ n, in grevlex order ((t, j) precedes (t′, j′) iff t < t′, or t = t′ and j < j′); a one-relation selection assigns to every column (t, j), t ≥ 1, an operator B_{(t,j)} ∈ {X, Y} with parent p = (t−1, j) if B = X (admissible iff j ≤ t−1) and p = (t−1, j−1) if B = Y (admissible iff j ≥ 1); formed/unformed A-products of the columns m of degree ≤ n−1, the implicit sections Ĥ_A, condition (C) and acyclicity (W) exactly as defined there. Hypothesis

- **(P)** for every column c, W_c ∪ L_c ⊆ {columns preceding c} (true for every run of a recurrence that orthogonalizes against already computed columns; any windows and reorthogonalization sets otherwise).

(a) **(Lemma S.)** A selection satisfies (C) iff it is a *staircase*: for every t = 1, …, n there is s_t ∈ {0, …, t−1} such that B_{(t,j)} = X ⟺ j ≤ s_t, with s_1 = 0 and s_{t+1} − s_t ∈ {0, 1} for t = 1, …, n−1. Hence exactly 2^{n−1} selections of degree n satisfy (C).
(b) **(Theorem.)** Every selection satisfying (C) and (P) satisfies (W). Explicitly, with σ_s := s_{s+1}, the unformed Y-products at degree s are those of the columns (s, j) with j < σ_s and the unformed X-products those with j > σ_s, and the definitions are acyclic in the order: degree s = 0, 1, …, n−1; within degree s, first the formed products (given data), then the unformed Y-columns in increasing j, then the unformed X-columns in increasing j. Moreover (support lemma) supp Ĥ_Ae_{(s,j)} ⊆ {columns of degree ≤ s+1} and its degree-(s+1) part is contained in {(s+1, j′) : j′ ≤ j + [A = Y]}.
(c) **(Consequence.)** For (C)-selections satisfying (P), hypothesis (W) of PD-T?…-205 is automatic, so its parts 1–3 hold under (C) and (P) alone. The named rules are staircases: BJ (s_t = 0), HL mirror (s_t = t−1), alt (X for 2j < t: s_t = ⌈t/2⌉ − 1). The pivot-adaptive rule is not covered (it violates (C) on several benchmarks, PD-T?…-205).

## Definitions

[A = Y] := 1 if A = Y, 0 if A = X. The A-child position of m = (s, j) is c_X(m) = (s+1, j), c_Y(m) = (s+1, j+1); A·m is *formed* iff B_{c_A(m)} = A (a one-relation selection forms each product at most once, because the A-parent of a column is unique).

## Assumptions

One relation per column; (P); β_c > 0 is not needed for (a)–(b) (they concern index dependencies only) but is assumed by PD-T?…-205 for the definitions to make sense.

## Status by part

Overall status: PROVED (developer proof written 2026-11-01T08:32 in response to audit-01; the target was OPEN at the audited candidate 5ccfac22; requires independent audit).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) Lemma S: (C) ⟺ staircase; count 2^{n−1} | PROVED | proof below; exhaustive check over all selections n ≤ 6 (2, 8, 64, 1024, 32768 selections) agrees |
| (b) (C) + (P) ⟹ (W), with explicit order and support lemma | PROVED | proof below; all 2^{n−1} staircases n ≤ 13 (block window) and n ≤ 10 with random windows/L-sets satisfying (P): no cycle, no support violation |
| (c) consequence for PD-T?…-205 | PROVED (routine) | (b) |

## Depends on

PD-T?…-205 (definitions only). No numerical or literature dependency.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_audit01_staircase.py > topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw` (Python 3.13.18; 30 s; exact integer/set computations, own support-only dependency-graph implementation, cross-checked for n ≤ 5 against reconstruction 01's `review_L2/rl2_cycles.analyse`: 0 disagreements). Output: n = 2..6 exhaustive — (C) holds for 2, 4, 8, 16, 32 selections, each a staircase, none cyclic, no support-lemma violation; n = 7..13 all staircases (64 … 4096) acyclic with the block window; n = 2..10 staircases × 3 random window/L-sets inside the preceding columns (6 … 1536 cases) acyclic; BJ, mirror, alt at n = 6, 12, 20 staircases, (C), acyclic. These finite checks supplement, and do not replace, the proof.

Correction of the evidence previously cited in PD-T?…-205 (from audit-01's `cycles-rerun.log`): reconstruction 01's random sampling at n = 6..9 found (C) in 5, 0, 0, 0 of 3000 samples, so the statement "well-defined ⟺ (C) in all cases" was vacuous for (C)-selections at n = 7–9. Lemma S explains this: a uniformly random selection satisfies (C) with probability 2^{n−1}/2^{n(n−1)/2} = 2^{−(n−1)(n−2)/2} (n = 6: 9.8e-4, i.e. 2.9 expected in 3000; n = 7: 3.1e-5).

## Sources

None (definitions from PD-T?…-205; selection rules from reconstruction 01 / BPS 2010 Remark 9 as recorded there).

## Proof or evidence

**(a)** The root (0, 0) has no creator, and both of its products are formed because (1, 0) can only be X·(0, 0) and (1, 1) only Y·(0, 0). For m = (t, j), 1 ≤ t ≤ n−1, (C) says B_m = A ⟹ A·m formed, i.e.
 (i) B_{(t,j)} = X ⟹ B_{(t+1,j)} = X,  (ii) B_{(t,j)} = Y ⟹ B_{(t+1,j+1)} = Y.
(⟸) For a staircase: if j ≤ s_t then j ≤ s_{t+1}, so (i) holds; if j > s_t then j + 1 > s_t + 1 ≥ s_{t+1}, so (ii) holds.
(⟹) Degree 1 is forced: B_{(1,0)} = X, B_{(1,1)} = Y, s_1 = 0. Let degree t ≤ n−1 be a staircase with s_t. By (i), B_{(t+1,j)} = X for j ≤ s_t; by (ii), B_{(t+1,j′)} = Y for j′ ∈ {s_t + 2, …, t + 1}. These position sets are disjoint, and the only remaining position j′ = s_t + 1 satisfies 1 ≤ s_t + 1 ≤ t, so both operators are admissible there: X gives s_{t+1} = s_t + 1, Y gives s_{t+1} = s_t. Hence degree t+1 is a staircase with s_{t+1} − s_t ∈ {0, 1} (and s_{t+1} ≤ t). Induction gives the claim; there is exactly one binary choice at each degree 2, …, n, so 2^{n−1} selections. ∎

**(b)** Fix a staircase and write σ := σ_s = s_{s+1}. For m = (s, j): X·m is formed iff B_{(s+1,j)} = X iff j ≤ σ; Y·m is formed iff B_{(s+1,j+1)} = Y iff j + 1 > σ iff j ≥ σ. So the unformed Y-products at degree s are U_Y(s) = {(s, j) : j < σ} and the unformed X-products U_X(s) = {(s, j) : j > σ}. A column of U_Y(s) has j < σ ≤ s_s + 1, so j ≤ s_s: it is created by X from p = (s−1, j). A column of U_X(s) has j > σ ≥ s_s: it is created by Y from p = (s−1, j−1). (This re-derives (C) for these columns.)

Let ≺ be the order of the statement. We prove by induction along ≺ that each Ĥ_Ae_m is defined from ≺-earlier columns only and satisfies (Sp): supp Ĥ_Ae_{(s,j)} ⊆ {deg ≤ s+1} with degree-(s+1) part ⊆ {(s+1, j′) : j′ ≤ j + [A = Y]}.

*Formed products.* Ĥ_Ae_m = Σ_{l∈W_c}(h_c)_le_l + Σ_{l∈L_c}(g_c)_le_l + β_ce_c with c = c_A(m) = (s+1, j + [A = Y]); no dependency. By (P) every l in W_c ∪ L_c precedes c, so it has degree ≤ s+1 and, if its degree is s+1, a j-index < j + [A = Y]; with c itself, (Sp) holds.

*Unformed products.* Let m = (s, j) ∈ U_A(s), B := B_m ≠ A, p = (s−1, i_p) its parent, and
 Ĥ_Ae_m = (Ĥ_BĤ_Ae_p − Σ_{l∈W_m}(h_m)_lĤ_Ae_l − Σ_{l∈L_m}(g_m)_lĤ_Ae_l)/β_m.
Its dependencies are: (α) Ĥ_Ae_p, of degree s−1, hence earlier; (β) Ĥ_Be_l for l ∈ supp Ĥ_Ae_p — by (Sp) for p, deg l ≤ s, and if deg l = s then l = (s, j″) with j″ ≤ i_p + [A = Y]; (γ) Ĥ_Ae_l for l ∈ W_m ∪ L_m — by (P) l precedes m, so deg l ≤ s−1 (earlier) or l = (s, j_l) with j_l < j.
- A = Y (j < σ, B = X, i_p = j): in (β), j″ ≤ j + 1 ≤ σ, so X·(s, j″) is formed — given data, earlier. In (γ), j_l < j < σ, so Y·(s, j_l) ∈ U_Y(s) with smaller j — earlier.
- A = X (j > σ, B = Y, i_p = j − 1): in (β), j″ ≤ j − 1; Y·(s, j″) is formed or in U_Y(s) — both precede every column of U_X(s). In (γ), X·(s, j_l) with j_l < j is formed (j_l ≤ σ) or in U_X(s) with smaller j — earlier.
(Sp) for m: the terms Ĥ_Ae_l of (γ) have, by (Sp) for l, support in degrees ≤ s+1 with degree-(s+1) part in {j′ ≤ j_l + [A = Y]} ⊆ {j′ ≤ j + [A = Y]} (no degree-(s+1) part if deg l ≤ s−1). In Ĥ_BĤ_Ae_p, the entries l of Ĥ_Ae_p of degree ≤ s−1 give support in degrees ≤ s, and the entries (s, j″), j″ ≤ i_p + [A = Y], give support in degrees ≤ s+1 with degree-(s+1) part in {j′ ≤ j″ + [B = Y]} ⊆ {j′ ≤ i_p + [A = Y] + [B = Y]} = {j′ ≤ i_p + 1} (as {A, B} = {X, Y}); and i_p + 1 = j + [A = Y] in both cases.
Every pair (A, m) with deg m ≤ n−1 occurs in exactly one stage, so the system of definitions is acyclic: (W). ∎

**(c)** Immediate from (b). ∎

## Scope

A purely combinatorial statement about which implicit sections PD-T?…-205 can define. It identifies the (C)-selections completely (one binary choice per degree: whether the X/Y boundary advances) and removes (W) as a separate hypothesis for them under (P). It says nothing about the sizes of the coupled residuals, and nothing about selections that violate (C) (e.g. the pivot-adaptive rule), for which the definitions of PD-T?…-205 are not available.

## Open items

A residual description for selections violating (C) (PD-T?…-205 open item); whether the staircase family contains a rule whose coupled residuals stay small on non-product measures (alt is a staircase and is killed on four of six non-product sets, PD-N?…-203; mirror on four). This item is also the durable OPEN home of the E3 target of topic padua-lanczos-drift-20261101, in polynomial span-drift form: does some staircase keep the full-reorthogonalization span drift O(u·poly(s)·χ) on a non-product family? The same question is open beyond (C), for some admissible one-relation selection such as the selection the pivot-adaptive rule makes on exact data. OPEN. PD-T142/11 give a computed-data span certificate and a finite exact-data sufficient criterion with a first-order guarantee. Whether any selection passes that criterion with polynomially bounded scores is unproved, and no such bound is claimed on the triangle or rotated-square families.

## History

- 2026-11-01T08:32:22+01:00: created by split from PD-T?…-205 (Codex audit-01, finding **L2-F4**); the original OPEN wordings are quoted in "Split from". In the same response the developer wrote proofs of Lemma S and of (C) + (P) ⟹ (W) (the hypothesis (P) is made explicit here; PD-T?…-205's definitions implicitly use only previously computed columns), so this file's status is PROVED rather than OPEN; the evidence account of PD-T?…-205 is corrected (vacuous sampling at n = 7–9, audit-01 `cycles-rerun.log`) and new exhaustive/structural checks added (`l2_audit01_staircase.py`). No status upgrade without this written proof; independent audit required (Claude Opus 5.5, xhigh; L2 developer, response to audit-01, `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa).
