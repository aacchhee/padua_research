# L3 summary — after R01–R06, reconstructions 01–02 and the response to Codex audit-01 (2026-11-01T08:33+01:00)

> Orchestrator note: saved by the orchestrator from the L3 developer's hand-back (the developer's write is blocked by the tool); content unchanged. The version before this response was saved by the orchestrator from the developer's hand-back after reconstruction 02 (Git history; replaced lines quoted in History below). Responses: [response-recon-01.md](response-recon-01.md), [response-recon-02.md](response-recon-02.md), [response-audit-01.md](response-audit-01.md).

Developer: Claude Opus 5.5, xhigh. 6 of 10 rounds used; the audit response adds no round. IDs provisional (PD-T?bivariate-lanczos-claude-3nn, PD-N?…-N3nn).

## 1. L3-Q1 verdict by reading

- **(L0)** Relations on the sections alone: trivially negative.
- **(L)** With an added forward-accuracy hypothesis: trivially positive (μ′ = μ).
- **(E)** Exact representation of specified consistent ε-perturbations given as data (or a residual strictly smaller than the perturbation, in one of the conventions (R1)–(R3) of 302(b)). Every obstruction below is a statement in reading (E) only.
  - Rate theorem (303), with S₀ := {p ∈ Π_{2n+1} : p(z_i) = 0 ∀ i}, S₁ := {p ∈ Π_{2n+1} : p(z_i) = 0, ∇p(z_i) = 0 ∀ i} and (H): no nonzero p ∈ S₁ has Hess p(z_i) ⪰ 0 at every node:
    - S₀ = {0} (nodes Π_{2n+1}-determining): δ*(ε) = 0 for ε < r(0) (same nodes, weights w + O(ε)). PROVED.
    - S₀ ≠ {0} and S₁ = {0}: δ*(ε) ≍ ε. PROVED.
    - S₁ ≠ {0}: δ*(ε) ≥ (ε/C)^{1/2}; if moreover (H) holds, δ*(ε) ≍ √ε. PROVED.
    - Some p* ∈ S₁ with Hess p*(z_i) ≻ 0 at every node: δ*(ε) ≥ δ₀ > 0 for every ε ∈ (0, ε₁] (obstruction). PROVED.
    - S₁ ≠ {0}, (H) fails, but no p* ∈ S₁ with all node Hessians positive definite: OPEN.
    - These conditions are not "absence/existence of a nonnegative annihilator": for any triangle (n = 1) no nonzero polynomial ≥ 0 on K_δ, δ > 0, is annihilated by L_μ, yet δ*(ε) ≍ √ε (305).
  - Inradius criteria: all ε-perturbations exactly representable on K_δ ⟺ r(δ) ≥ ε (302(b1)); all mass-preserving ones ⟺ r₀(δ) ≥ ε, with r₀/(A + Br₀) ≤ r ≤ r₀ (302(b2)). Residual thresholds hold with constant 1 only in their own convention ((R1) with r, (R2) with r₀ and fixed-mass approximants); for mass-normalised section data the factor m/(m + E(1)) must be carried (302(b3)). The pre-audit factor-1 normalised threshold is refuted (N309).
  - Square case M = N_n: δ = O(ε) impossible; δ ≥ c√ε and δ ≥ c√‖[Ĥ_x, Ĥ_y]_{nn}‖ necessary (N302, also for residuals ≤ θε in each convention; 304(a)). PROVED.
  - δ ≍ √ε: n = 1, Padua n = 2, equispaced checkerboards n ≤ 7 (PROVED); equispaced n = 8 (reviewer computation, pending independent rerun).
  - No δ(ε) → 0: Padua n = 3 (PROVED) and every Padua n ≥ 4 (PROVED under unisolvence), each with a per-degree radius δ₀(n) > 0 (a chosen radius, which may be taken nonincreasing in n). The certified lower bounds for the positivity radius of the certificate P_n decrease over n = 4..12; no uniform-in-n obstruction radius is established, and the dependence on n is OPEN (319).
  - "Explicit δ(ε)" is met as a rate; constants come from compactness.
- **(G)** Greenbaum regime: OPEN. The reading-(E) obstructions do not show that Padua recurrences have no Greenbaum-type backward model for actual finite-precision runs. 314 (PROVED): the completed computed pair is consistent iff it is symmetric. Rotated square, BJ/CGS, linear regime n ≤ 20 (MEASURED): asymmetry ≈ forward error ≈ (2–10)·loss; no first-order consistent fit removes more than ≈ 55% of the forward error. Random square: the inaccurate F data are nearly symmetric — a Greenbaum-like counter-indication, unresolved.

## 2. Ranked survivors

1. **N301 + 313/N303** — Padua obstruction in reading (E). Certificate p* for n = 3; for n ≥ 4, P_n = 9(g₁² − ½g₀g₂) + (g₂² − g₁g₃), g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y), with double zeros and PD Hessians at all nodes. PROVED (N303 under unisolvence, a trusted LITERATURE dependency); independent exact rerun for n = 4..16; certificate checks rerun and independently re-implemented by Codex audit-01.
2. **303 + 302** — rate theorem in terms of S₀, S₁ and (H) (§1); reduction to localized positive cubature; inradius criteria r(δ) ≥ ε (all perturbations) and r₀(δ) ≥ ε (mass-preserving), residual conventions (R1)–(R3). PROVED (302(b) corrected after audit-01 LF-M1).
3. **N302 + 304 + 318** — no δ = O(ε) in the square case; ‖κ‖ ≤ Cδ²; commuting data give δ ≤ ‖ΔH‖; dκ factors through V*/T (PROVED). 318 (PROVED): dκ(E)_ab = E(s_ab), s_ab = R^y_aR^x_b − R^x_aR^y_b ∈ S₁, and rank dκ = dim{p_C : C ⊥ Hankel}. The first-order isomorphism is a separate OPEN claim (316), equivalent by 318 to the open conjunct of 309; its finite rank observations are MEASURED (317).
4. **301** — truncated Favard: commutator supported on block (n,n) ⟺ functional on Π_{2n+1}; words-formula inverse; excess count e_n. PROVED.
5. **305, 306, 310** — √ε attained. PROVED.
6. **312, 309** — interior Turán lemma; quadratic-generator (Hankel) form. PROVED (309 under unisolvence).
7. **314** — consistency ⟺ symmetry. PROVED.
8. **308, N304, N306** — compression model; compression ⇏ section (reading (E)); (H) not decided by the node count. PROVED.
9. **N309** — the pre-audit normalised residual threshold of 302(b) is false (exact counterexample of the audit, explicit radius δ′ = 10⁻⁸). PROVED.
10. **MEASURED:** 307, 311, 315, 317, N305, N307, N308.
- **OPEN:** 300 (combined target), 316 (first-order isomorphism), 319 (dependence on n of the Padua obstruction radius).

## 3. Failed routes

Dilation route (N304); quantitative Lin (no Krylov structure); count route as first stated; C1 candidate (N305); κ-family certificates for n ≤ 3 (fail for every c); "count decides (H)" (N306); R06 hypotheses A (N307) and C (N308); the Greenbaum-width parallel (withdrawn, sources contested); the factor-1 normalised residual threshold (N309).

## 4. Prior-art separations (from reviews/L3-prior-art-01.md)

| Result | Closest prior work | What L3 adds |
|---|---|---|
| 301 | Xu, Trans. AMS 1994, Thm 4.2; Degani–Schiff–Tannor 2005, Thms 9–11 | Truncated commutator-support characterisation and the count e_n. Still to read: Delgado–Geronimo–Iliev–Marcellán 2006, Cichoń–Stochel–Szafraniec 2005 |
| 302 | Tchakaloff; Di Dio–Schmüdgen, Prop. 27 | Localisation to K_δ, the inradius criteria and the residual conventions |
| 303 | Di Dio–Schmüdgen, Thm 40, Lemma 37, Prop. 43; Blekherman 2012, Lemma 3.1 | The quantitative trichotomy in terms of S₀, S₁ and condition (H) |
| 304, 318 | Möller and DST node counts | Where the extra support lies; exact first-order formula of κ |
| Padua certificates | none found in the documented search | — |
| 308 | Passer–Shalit–Solel; Davidson–Dor-On–Shalit–Solel | Routine |

(All comparisons as reported by the prior-art check; no exhaustive search, no novelty claim. Canonical literature records are an orchestrator task at PR preparation.)

## 5. Development briefs

- **319:** certify the sampled negative values of P_n exactly (rigorous finite upper bounds on its positivity radius); an all-n argument for ρ_n → 0; the uniform-radius question (U2).
- **303:** explicit constants; the degenerate PSD-singular subcase.
- **316 / 309:** prove injectivity of C ↦ p_C on {C ⊥ Hankel} (then the 304(c) isomorphism follows by 318); rerun `indep_generator_cert.py` for Padua n ≤ 3.
- **310:** rerun the reviewer's n = 8 certificate; extended precision for n ≥ 9.
- **(G):** a-priori relation between asymmetry and the commutator residual; HL/ORTH, O(1) loss and large M (AC's servers). Decisive test: the random-square near-symmetry.

## 6. Runs needed

- Independent reruns still missing: `r05_*`; `r06_weight_fit.py` with the developer's reference (the reviewer's and audit's reruns used `consistency_recheck.py`); the reviewer's `equi_H_cert.py 8 8 60`; `review_L3/indep_generator_cert.py` (Padua n ≤ 3, for 316); independent checks of the new `t302b_conventions_check.py` and `t318_dkappa_formula_check.py` (Codex re-audit). Done by Codex audit-01: `favard_check.py 4 0`, `r06_consistency.py random 40`, `consistency_recheck.py rot03 18 20`, `equi_H_cert.py 1 7 40`, `padua_delta0.py 4 12`, `padua_turan_check.py 3 16`, `turan_symbolic.py`, `indep_exact_check.py`, `unisolvence_check.py`.
- On AC's servers: `r06_consistency.py` at M = 10⁴–10⁵.

## History

- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): response to Codex audit-01 (LF-M1, LF-M2, LC-M1, LC-L1, report-level items; consolidated items 1, 4, 5). Replaced lines of the previous version (after reconstruction 02) are preserved verbatim in Git history (commit 32f0467 and later) and quoted in the developer's hand-back: title and date line; orchestrator note; developer line; the (E) bullets for the overdetermined case, square case and "No δ(ε) → 0 … δ₀(n) → 0 as n grows"; the (G) bullet opening; ranked items 1, 2, 3, 8, 9 and the "300 OPEN" line; the failed-routes sentence; prior-art rows 302, 303, 304; briefs N303, 304(c), 309; the independent-reruns line.
