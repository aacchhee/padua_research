# PD-T?bivariate-lanczos-claude-300 — L3-Q1 target: Greenbaum-type backward interpretation of computed degree-n sections

ID kind: PD-T.
Aliases: L3-Q1; IDEA?bivariate-lanczos-claude-031 (seed); nearby representing measure; commuting backward model; backward interpretation.
Split from: none.
Split into: PD-T?bivariate-lanczos-claude-301 (truncated Favard), 302 (precise form / reduction), 303 (rate theorem), 304 (square-case commutator bounds), 305 (n = 1 √ε), 306 (Padua n = 2 √ε, PROVED after independent rerun), 307 (MEASURED survey), 308 (compression model); PD-N?bivariate-lanczos-claude-301 (Padua n = 3 obstruction, PROVED after independent rerun), PD-N?bivariate-lanczos-claude-302 (no δ = O(ε) in the square case). Added after R04–R06: 310 (equispaced checkerboards n ≤ 7, (H), PROVED), 311 (MEASURED margins), 312 (interior Turán lemma, PROVED), 313 (Turán certificate for all Padua n ≥ 4, PROVED), PD-N?…-303 (Padua n ≥ 4 obstruction, PROVED under Padua unisolvence), 314 (consistency ⟺ symmetry of computed data, PROVED), 315 (MEASURED consistency defect, reading (G)). Added in the response to Codex audit-01 (second-level splits and new files): 316 (OPEN first-order isomorphism, split from 304(c)), 317 (MEASURED rank of dκ, split from 304(c)), 318 (PROVED derivative formula for κ), 319 (OPEN dependence on n of the Padua obstruction radius, split from 313/N303), PD-N?…-309 (refuted pre-audit normalised residual threshold of 302(b)). Mapping to be recorded in ID_CROSSWALK.md at PR preparation.

## Statement

Frozen wording (plan.md §L3-Q1, not reworded): "Given [IDEALIZED: perturbations given as data] computed sections (Ĥ_x, Ĥ_y) of degree n that satisfy the exact structural zero pattern and the recurrence relations up to O(ε), does there exist a positive discrete measure μ′ supported within distance δ of the original nodes whose exact degree-n sections equal (Ĥ_x, Ĥ_y) up to O(ε) (a Greenbaum-type backward interpretation)? Decide, separately for the overdetermined case (M ≥ dim Π_{2n+1}, generic nodes) and the square case M = N_n (Padua), either an existence statement with an explicit δ(ε) or an explicit obstruction family."

Readings (PD-T?…-302; corrected per finding M1 of L3-reconstruction-01): the frozen hypothesis does not tie Ĥ to the nodes. (L0) relations on the sections alone — literal question trivially NEGATIVE (Ĥ = Φ(ν), ν positive and far from the nodes); (L) literal plus an ADDED forward-accuracy hypothesis — trivially positive (μ′ = μ, δ = 0); (E), a recorded substitution with a stronger conclusion: (E) exact representation of consistent ε-perturbed data given as data (or a residual strictly smaller than the perturbation, in one of the conventions (R1)–(R3) of PD-T?…-302(b)) — decided case by case below; every obstruction below is a statement in reading (E) only; (G) Greenbaum regime — data far from Φ(μ) but satisfying the local relations of the recurrence up to O(ε) (loss of orthogonality) — OPEN.

## Definitions / Assumptions

As in PD-T?…-301/302/303.

## Status by part

Overall status: OPEN (reading (G) open; reading (E) decided in the cases below with mixed statuses, so not PARTIAL).

| Part of the target | Status | Result / file |
|---|---|---|
| (L0) literal, relations on sections alone | PROVED (routine) | trivially negative; 302(c) |
| (L) literal + added forward accuracy | PROVED (routine) | trivial with δ = 0; 302(c) |
| (E) overdetermined, M ≥ dim Π_{2n+1}, nodes Π_{2n+1}-determining (S_0 = {0}) | PROVED | existence with δ = 0 (same nodes, weights w + O(ε)) for ε < r(0) ≥ w_min σ_1; 303(a) |
| (E) intermediate M with S_1 = {0} | PROVED | δ(ε) ≍ ε; 303(b) |
| (E) square case, all Π_n-unisolvent sets, n ≥ 1: δ = O(ε) impossible, δ ≳ √ε necessary; δ ≥ c√‖κ(Ĥ)‖ | PROVED | PD-N?…-302, 303(c), 304(a) |
| (E) square case with exactly commuting data | PROVED | δ ≤ ‖ΔH‖, N_n atoms; 304(b) |
| (E) square, n = 1 (any triangle incl. Padua n = 1) | PROVED | δ ≍ √ε; 305 |
| (E) Padua n = 2 | PROVED (independent exact rerun, L3-reconstruction-01) | δ ≍ √ε; 306 |
| (E) Padua n = 3 | PROVED (independent exact rerun, L3-reconstruction-01) | obstruction: no δ(ε) → 0 (ε ≤ ε_1); explicit family E = −ε ev_ζ; PD-N?…-301 |
| (E) Padua n ≥ 4 | PROVED under the Padua-unisolvence assumption (LITERATURE); independent exact check n = 4..16 and hand check by L3-reconstruction-02; per-degree radius δ_0(n) > 0, no uniform-in-n radius established (dependence on n OPEN, 319) | obstruction via P_n = 9(g_1² − ½g_0g_2) + (g_2² − g_1g_3); 312, 313, PD-N?…-303 |
| (E) equispaced checkerboards n ≤ 7 | PROVED (independent exact rerun, L3-reconstruction-02; fresh rerun n = 1..7 by Codex audit-01); n = 8 reviewer computation pending independent rerun | δ ≍ √ε; 310 |
| (E) random square sets | MEASURED | (H) n ≤ 2, mixed n = 3, robust failure in 7 of 9 cases n = 4..6 (two marginal); 307 (the floating Padua n = 4..7 survey of 307 is superseded by the proof for all n ≥ 4, 313/N303) |
| (E) other square sets (ordered Harris–Simanek checkerboards) | MEASURED | node-set dependent: equispaced (H) n ≤ 5, graded n ≤ 4, sorted-uniform mixed; 307 item 6 (R03) |
| (G) Greenbaum (loss-of-orthogonality) regime, both cases | OPEN | R06: computed data consistent ⟺ completed pair symmetric (314, PROVED); on the rotated square, asymmetry ≈ forward error ≈ (2–10)·loss and no first-order consistent fit removes more than ≈ 55% of the forward error (315, MEASURED, linear regime n ≤ 20 with an 80-bit reference): no Greenbaum regime there; on the random square the inaccurate F data are nearly symmetric — a Greenbaum-like counter-indication, unresolved |

Literature context (R03, `directions/L3/lit_reading.md`, WebFetch readings): the quantitative Lin bound C‖[X,Y]‖^{1/2} is Kachkovskiy–Safarov (1.3) (confirmed); the two-matrix commuting-extension problem is "wide open" per Koiran §1.4 (confirmed); Greenbaum's 1D proof covers interval width √ε‖A‖ (as reported by Šimonová–Tichý; Greenbaum unread), — CONTESTED (finding L9; LIT?…-209 records conflicting secondary accounts: Chen arXiv 2608.21268 ε^{1/4}, Meurant–Strakoš Thm 4.9); the comparison with the square-case rate is withdrawn (it also compared different ε's: unit roundoff vs perturbation size); Greenbaum 1989 is pending-reference.

## Depends on

The split-off files listed above.

## Checks

See the split-off files and `topics/bivariate-lanczos-20261031/directions/L3/R01.md`.

## Sources

`xu-siam-1994` (context for the cubature link), arXiv:1703.01497 (context for boundary points of moment cones; summary only).

## Proof or evidence

In the split-off files.

## Scope

Cubature link (recorded as required by plan.md): by PD-T?…-302(a), reading (E) is exactly the existence of a positive cubature formula of degree 2n+1 for the perturbed functional L̂ with all nodes in K_δ. Exactly commuting square data (κ = 0) ⟺ L̂ has an N_n-node positive cubature of degree 2n+1 (odd-degree "Gaussian" type, the Mysovskikh situation: degree-(n+1) orthogonal polynomials with N_n common zeros), and then the nodes are the joint eigenvalues (304(b)), the discrete analogue of Xu's joint-eigenvalue characterisation (xu-siam-1994 Thm 3.1/4.1, which concerns even degree 2n−2 with dim Π_{n−1} nodes and a modified last block). The obstruction p* of PD-N?…-301 is a classical dual certificate for non-existence of a localized positive cubature (a polynomial nonnegative on the node region whose functional value is negative).

## Open items

(1) Reading (G): characterize the reconstructed functional L̂ of a long finite-precision run and decide L̂ ∈ C(K_δ) + B(0, O(u)). (2) Dependence on n of the Padua obstruction radius (319, OPEN; exact certificates for all n ≥ 4 are done, 313/N303). (3) Structural reason for the n = 2 → 3 transition. (4) Degenerate subcase of 303. (5) Constants. (6) First-order isomorphism of the last-block commutator (316, OPEN; reduced by 318 to the 309 conjunct).

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01 with the split listed above. The frozen wording is preserved verbatim; the readings (L)/(E)/(G) are interpretations recorded in 302 with reasons, not a narrowing of the target ((G) stays OPEN).
- 2026-10-31T23:54:40+01:00, L3 developer: response to L3-reconstruction-01 — M1 (readings L0/L/E/G; "L3-Q1 decided" only in reading (E)), statuses of 306/N301 upgraded to PROVED after the independent rerun, L9 (Greenbaum-width remark marked contested and withdrawn), L12 (explicit rates only, see 303), rows for R04–R06 added.
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «306 (Padua n = 2 √ε, CONDITIONAL)»; «PD-N?bivariate-lanczos-claude-301 (Padua n = 3 obstruction, CONDITIONAL)»; «Mapping to be recorded in ID_CROSSWALK.md at PR preparation.»; «Precise readings (PD-T?…-302): (L) literal, perturbative — trivial (μ′ = μ, δ = 0);»; «| (L) literal perturbative reading | PROVED (routine) | trivial with δ = 0; 302(c) |»; «| (E) Padua n = 2 | CONDITIONAL (independent rerun of exact checker) | δ ≍ √ε; 306 |»; «| (E) Padua n = 3 | CONDITIONAL (independent rerun of exact checker) | obstruction: no δ(ε) → 0; explicit family E = −ε ev_ζ; PD-N?…-301 |»; «the same order as the square-case (H) rate.»; «| (G) Greenbaum (loss-of-orthogonality) regime, both cases | OPEN | needs the L1 local relations; R01 next question |».
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): findings L9/L11 residual ('unisolvent' → 'determining'), M2 ((G) row restricted to the rotated square) and status updates for 310/313/N303 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «| (E) overdetermined, M ≥ dim Π_{2n+1}, nodes Π_{2n+1}-unisolvent |»; «| (E) Padua n ≥ 4 | CONDITIONAL (rerun/hand check of three symbolic expansions; the reconstruction independently certified n = 4 exactly) |»; «| (E) equispaced checkerboards n ≤ 7 | CONDITIONAL (independent rerun) | δ ≍ √ε; 310 |»; «measured asymmetry ≈ forward error ≈ (0.7–10)·loss and no better first-order consistent fit (315, MEASURED): no Greenbaum regime seen in the tested BJ runs |».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): findings LC-M1 (Padua n ≥ 4 row: «δ_0(n) → 0» withdrawn → 319), LC-L1 and the L3-framework stale-label note (split list and rows synchronised with current statuses), consolidated item 4 (obstructions restricted to reading (E); (G) OPEN) and item 5 (new split files listed) of Codex audit-01 (audit-01.md, L3-framework.md, L3-certificates.md; candidate 5ccfac2). Status OPEN unchanged. Original wording of the replaced passages: «Added after R04–R06: 310 (equispaced checkerboards n ≤ 7, (H), CONDITIONAL), 311 (MEASURED margins), 312 (interior Turán lemma, PROVED), 313 (Turán certificate for all Padua n ≥ 4, CONDITIONAL), PD-N?…-303 (Padua n ≥ 4 obstruction, CONDITIONAL), 314 (consistency ⟺ symmetry of computed data, PROVED), 315 (MEASURED consistency defect, reading (G)).»; «(E), a recorded substitution with a stronger conclusion: (E) exact representation of consistent ε-perturbed data (residual strictly smaller than the perturbation) — decided case by case below;»; «| (E) Padua n ≥ 4 | PROVED under the Padua-unisolvence assumption (LITERATURE); independent exact check n = 4..16 and hand check by L3-reconstruction-02; δ_0(n) → 0 | obstruction via P_n = 9(g_1² − ½g_0g_2) + (g_2² − g_1g_3); 312, 313, PD-N?…-303 |»; «| (E) equispaced checkerboards n ≤ 7 | PROVED (independent exact rerun, L3-reconstruction-02); n = 8 reviewer computation pending rerun | δ ≍ √ε; 310 |»; «| (E) Padua n = 4..7; random square sets | MEASURED | robust failure of (H) numerically (obstruction regime) for Padua 4..7; random sets: (H) n ≤ 2, mixed n = 3, failure n ≥ 4; 307 |»; «(2) Exact certificates for Padua n ≥ 4.»; «(5) Constants.».
