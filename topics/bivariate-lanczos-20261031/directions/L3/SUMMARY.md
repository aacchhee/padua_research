# L3 summary — after R01–R06 and reconstructions 01–02 (2026-11-01T00:49+01:00)

> Orchestrator note: saved by the orchestrator from the L3 developer's hand-back (the developer's write is blocked by the tool). Content is the developer's, lightly formatted. Earlier version (after R06, before reconstruction 02) is in Git history. Responses: [response-recon-01.md](response-recon-01.md), [response-recon-02.md](response-recon-02.md).

Developer: Claude Opus 5.5, xhigh. 6 of 10 rounds used. IDs provisional (PD-T?bivariate-lanczos-claude-3nn, PD-N?…-N3nn).

## 1. L3-Q1 verdict by reading

- **(L0)** Relations on the sections alone: trivially negative.
- **(L)** With an added forward-accuracy hypothesis: trivially positive (μ′ = μ).
- **(E)** Exact representation of consistent ε-perturbed data:
  - Overdetermined case (Π_{2n+1}-determining nodes): δ = 0 for ε < r(0). PROVED.
  - Square case M = N_n: δ = O(ε) impossible; δ ≥ c√ε and δ ≥ c√‖[Ĥ_x, Ĥ_y]_{nn}‖ necessary. PROVED.
  - δ ≍ √ε: n = 1, Padua n = 2, equispaced checkerboards n ≤ 7 (PROVED); equispaced n = 8 (reviewer computation, pending independent rerun).
  - No δ(ε) → 0: Padua n = 3 (PROVED) and every Padua n ≥ 4 (PROVED under unisolvence). δ₀(n) → 0 as n grows.
  - "Explicit δ(ε)" is met as a rate; constants come from compactness.
- **(G)** Greenbaum regime: OPEN. 314 (PROVED): the completed computed pair is consistent iff it is symmetric. Rotated square, BJ/CGS, linear regime n ≤ 20 (MEASURED): asymmetry ≈ forward error ≈ (2–10)·loss; no first-order consistent fit removes more than ≈ 55% of the forward error. Random square: the inaccurate F data are nearly symmetric — a Greenbaum-like counter-indication, unresolved.

## 2. Ranked survivors

1. **N301 + 313/N303** — Padua obstruction. Certificate p* for n = 3; for n ≥ 4, P_n = 9(g₁² − ½g₀g₂) + (g₂² − g₁g₃), g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y), with double zeros and PD Hessians at all nodes. PROVED (N303 under unisolvence, a trusted LITERATURE dependency); independent exact rerun for n = 4..16.
2. **303 + 302** — rate theorem: S₀ = 0 → δ = 0; S₁ = 0 → ε; S₁ ≠ 0 → δ ≳ √ε, with (H) ≍ √ε; a PD-Hessian p* ∈ S₁ → obstruction. Reduction to localized positive cubature with inradius r(δ) ≥ ε. PROVED.
3. **N302 + 304** — no δ = O(ε) in the square case; ‖κ‖ ≤ Cδ²; commuting data give δ ≤ ‖ΔH‖. PROVED, except 304(c) isomorphism part (MEASURED).
4. **301** — truncated Favard: commutator supported on block (n,n) ⟺ functional on Π_{2n+1}; words-formula inverse; excess count e_n. PROVED.
5. **305, 306, 310** — √ε attained. PROVED.
6. **312, 309** — interior Turán lemma; quadratic-generator (Hankel) form. PROVED (309 under unisolvence).
7. **314** — consistency ⟺ symmetry. PROVED.
8. **308, N304, N306** — compression model; compression ⇏ section; (H) not decided by the node count. PROVED.
9. **MEASURED:** 307, 311, 315, N305, N307, N308.
- **300** (combined target): OPEN.

## 3. Failed routes

Dilation route (N304); quantitative Lin (no Krylov structure); count route as first stated; C1 candidate (N305); κ-family certificates for n ≤ 3 (fail for every c); "count decides (H)" (N306); R06 hypotheses A (N307) and C (N308); the Greenbaum-width parallel (withdrawn, sources contested).

## 4. Prior-art separations (from reviews/L3-prior-art-01.md)

| Result | Closest prior work | What L3 adds |
|---|---|---|
| 301 | Xu, Trans. AMS 1994, Thm 4.2; Degani–Schiff–Tannor 2005, Thms 9–11 | Truncated commutator-support characterisation and the count e_n. Still to read: Delgado–Geronimo–Iliev–Marcellán 2006, Cichoń–Stochel–Szafraniec 2005 |
| 302 | Tchakaloff; Di Dio–Schmüdgen, Prop. 27 | Localisation to K_δ and the inradius criterion |
| 303 | Di Dio–Schmüdgen, Thm 40, Lemma 37, Prop. 43; Blekherman 2012, Lemma 3.1 | The quantitative trichotomy and condition (H) |
| 304 | Möller and DST node counts | Where the extra support lies |
| Padua certificates | none found in the documented search | — |
| 308 | Passer–Shalit–Solel; Davidson–Dor-On–Shalit–Solel | Routine |

## 5. Development briefs

- **N303:** independent rerun of the reviewer's δ₀(n) bounds; asymptotics of δ₀(n).
- **303:** explicit constants; the degenerate PSD-singular subcase.
- **304(c):** proof of the isomorphism part.
- **309:** prove S₁ = {p_C}.
- **310:** rerun the reviewer's n = 8 certificate; extended precision for n ≥ 9.
- **(G):** a-priori relation between asymmetry and the commutator residual; HL/ORTH, O(1) loss and large M (AC's servers). Decisive test: the random-square near-symmetry.

## 6. Runs needed

- Independent reruns: `r05_*`, `r06_*`; the reviewer's `equi_H_cert.py 8 8 60` and `padua_delta0.py`.
- On AC's servers: `r06_consistency.py` at M = 10⁴–10⁵.
