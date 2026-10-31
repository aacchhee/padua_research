# L3 — Direction summary after R06 (2026-10-31)

> Orchestrator note: saved by the orchestrator from the L3 developer's hand-back text (the developer's file write was blocked by the tool). Content is the developer's, lightly formatted; no changes of substance. Statuses are the developer's after applying reconstruction 01 ([response](response-recon-01.md)); R04–R06 claims (310–315, N303–N306) are not yet independently reconstructed.

Developer: Claude Opus 5.5, xhigh. 6 of 10 rounds used. IDs provisional (PD-T?bivariate-lanczos-claude-3nn, PD-N?…-N3nn). Readings of the frozen L3-Q1 (after reconstruction finding M1): L0 literal, L sections-only, E exact representation (answered here), G Greenbaum (with local relations of the computed basis).

## 1. Verdict

In reading (E): overdetermined case δ = 0 (PROVED). Square case: δ = O(ε) impossible and δ ≥ c√ε necessary (PROVED); δ ≍ √ε attained for n = 1 and Padua n = 2 (PROVED) and for equispaced checkerboards n ≤ 7 (CONDITIONAL); no δ → 0 for Padua n = 3 (PROVED) and n ≥ 4 (CONDITIONAL). δ(ε) is explicit only as a rate. Reading (G) is OPEN; no Greenbaum regime was observed in the tested runs.

## 2. Ranked survivors

1. N301 (Padua n = 3 obstruction, PROVED after the quantifier fix, independent exact rerun by reconstruction 01) and 313/N303 (all n ≥ 4: P_n = 9(g₁² − ½g₀g₂) + (g₂² − g₁g₃), g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y), double zeros and PD Hessians at all Padua nodes; CONDITIONAL on three short symbolic expansions; the reviewer's exact n = 4 certificate supports n = 4).
2. 303 (rate theorem) and 302 (reduction to moment-cone membership over K_δ, residual with c = 1).
3. N302 and 304 (square-case √ε necessity; commutator bound).
4. 301 (truncated Favard correspondence).
5. 305, 306, 310 (√ε attained: n = 1, Padua n = 2, equispaced n ≤ 7).
6. 312 (interior-node Turán-type lemma: Hessian PD iff 0 < c sin²θ sin²φ < 1/4) and 309 (generator form).
7. 314 (computed data are exact sections of some functional iff the completed pair (Ĥ_F, Ĥ_J) is symmetric; PROVED).
8. 308 and N304 (compression/dilation model).
9. MEASURED: 307, 311, 315 (asymmetry ≈ forward error ≈ (0.7–10)·loss on rotated/random squares; no first-order consistent fit does much better), N305, N306.

## 3. Prior-art separations (from reviews/L3-prior-art-01.md)

- 301 vs Xu Trans. AMS 1994 Thm 4.2 and Degani–Schiff–Tannor 2005 Thms 9–11: the truncated commutator-support characterisation and the excess count. Delgado–Geronimo–Iliev–Marcellán SIMAX 2006 and Cichoń–Stochel–Szafraniec JAT 2005 must be read first.
- 302 vs Tchakaloff / Di Dio–Schmüdgen Prop. 27: localisation to K_δ and the inradius criterion.
- 303 vs Di Dio–Schmüdgen Thm 40 / Lemma 37 / Prop. 43 and Blekherman 2012 Lemma 3.1: the quantitative trichotomy and condition (H).
- 304 vs Möller / DST counts: where the extra support lies.
- Padua certificates: no match found in the documented search.
- 308: framework known (Passer–Shalit–Solel; Davidson–Dor-On–Shalit–Solel).
- Withdrawn: the parallel between the 303(d) √ε rate and a "1D Greenbaum width √ε" (literature accounts conflict; Greenbaum 1989 pending-reference).

## 4. Development briefs

- N303: hand check or independent rerun of the symbolic expansions, then explicit δ₀(n).
- 303: explicit constants and the degenerate subcase.
- 304(c): prove the isomorphism part (currently full rank measured for n = 2, 3).
- 309: prove S₁ equals the quadratic-generator family.
- 310: extended precision for n ≥ 8.
- 314/315: an a-priori asymmetry–residual bound; HL/ORTH, O(1) loss and large M.

## 5. Runs needed

- Independent reruns: `exact_checkerboard.py 1 7 equi`, `r05_boundary_proof.py`, `r05_interior_identity.py`, `r05_direct_check.py 3 14`, `r06_consistency.py` (rot03 26, random 40, tensor 40), `r06_weight_fit.py rot03 14 26` (all in tracks/bivariate-lanczos/code/L3/).
- Servers: `r06_consistency.py` with M = 10⁴–10⁵ on syvert0/1/2.

Ready for adversarial reconstruction: 310, 312, 313/N303, 314, N304–N306.
