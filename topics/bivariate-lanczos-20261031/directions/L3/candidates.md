# L3 candidates (IDEA template records)

Direction L3, topic bivariate-lanczos-20261031. Developer Claude Opus 5.5 (xhigh, requested). Base 2d8c3ab8348be80a6f16f69ee7ef9c7bb66ed42e (rules d36722823441dc40c6e19d69a174459348dd309c). Provisional IDs `IDEA?bivariate-lanczos-claude-3nn`; final IDs at PR preparation. Kill criteria were written in R01 §2 before the corresponding test was run. No novelty claims (see R01 §1 for the gate and its limits).

---

## IDEA?bivariate-lanczos-claude-301 — Moment-cone inradius formulation of L3-Q1 (route (i), refined)

Aliases: route (i); localized positive cubature; r(δ); jet spaces S_0/S_1; "interior vs boundary of the moment cone over K_δ".

- Question / scope: decide L3-Q1 (reading (E)) via the truncated moment cone C(K_δ) at L_μ.
- Mechanism and hypotheses: sections ↔ functionals on Π_{2n+1} (PD-T?…-301); exact representability ⟺ L̂ ∈ C(K_δ); all ε-perturbations ⟺ r(δ) ≥ ε; rate of r(δ) from the jets of polynomials vanishing at the nodes.
- Closest registry entries (read in full): seed 005 (Greenbaum-type commuting extension), 031 (L3-Q1 core), 032 (commuting extensions), 033 (cubature link); OBST-01, OBST-11.
- Separation criterion vs closest entry: 005/031 state the question; none has a criterion. Distinguishing property: the answer is governed by S_0, S_1 and the Hessian cone condition (H), not by commutator size alone. Falsifier: a node set with S_1 ≠ {0} where an O(ε) construction works (would contradict 303(c)).
- Literature baseline and search limitations: Di Dio–Schmüdgen arXiv:1703.01497 (boundary/inner points of moment cones; summary only). No source found (documented search only) on rates δ(ε) for localized support of perturbed truncated moment functionals; search was two web queries plus repository grep — not exhaustive.
- Applicable obstructions and exact hypotheses broken: OBST-01 (needs commuting extension): reformulated exactly (graded extension ⟺ representing measure); OBST-11 (Xu 1994 scope): avoided — no use of Xu's theorems.
- Novelty gate verdict: variant with difference (relative to 005/031: a concrete criterion), within documented search.
- Cheapest decisive test: n = 1 by hand; SDP for (H) on Padua n ≤ 7.
- Kill criterion written before testing: if for Padua n = 2 an LP shows δ_min ∝ ε (slope 1 in log-log over 3 decades), the √ε necessity claim is wrong.
- Test discriminability: δ_min/√ε vs δ_min/ε over 4 decades separates the two rates by a factor 100.
- Actual test results and committed evidence: n = 2: δ_min/√ε = 0.054 constant over ε = 1e-2..1e-6 (logs `lp_rate_n2_r0.03.log`); kill criterion did not fire.
- Disposition: survived → PD-T?…-302, 303.
- Disposition reason: —
- Canonical theory / negative-result ID: PD-T?bivariate-lanczos-claude-302, 303.
- Topic / audit / history: R01.

## IDEA?bivariate-lanczos-claude-302 — Hessian cone condition (H) decides the square case

Aliases: (H); PD Hessian certificate; dual PD certificate Σ⟨A_i, Hess p(z_i)⟩ = 0.

- Question / scope: in the square case (S_1 ≠ {0} always), which of √ε or obstruction occurs?
- Mechanism and hypotheses: second-order spreading of clusters reaches the S_1*-directions iff (H); a p ∈ S_1 with all Hessians PD is a locally nonnegative supporting polynomial.
- Closest registry entries: 005, 033; OBST-11.
- Separation criterion vs closest entry: none of the entries contains a condition on Hessians; falsifier: a node set with (H) where δ_min does not scale like √ε.
- Literature baseline and search limitations: as 301.
- Applicable obstructions and exact hypotheses broken: none.
- Novelty gate verdict: new within documented search (no claim of novelty in the literature).
- Cheapest decisive test: n = 1 hand proof; SDP primal/dual for Padua n = 1..7; exact certificates n = 1, 2, 3.
- Kill criterion written before testing: if the exact checker rejects the n = 3 primal certificate (any Hessian not PD exactly), the obstruction claim for n = 3 is withdrawn.
- Test discriminability: exact sign tests in Q(√2); no tolerance.
- Actual test results and committed evidence: n = 1, 2 dual certificates PASS; n = 3 primal certificate PASS (log `exact_certificates.log`).
- Disposition: survived → PD-T?…-303(d)–(f), 305, 306; PD-N?…-301.
- Canonical theory / negative-result ID: as above.
- Topic / audit / history: R01.

## IDEA?bivariate-lanczos-claude-303 — Dilation / POVM formulation (route (ii))

Aliases: minimal matrix convex set; Naimark dilation; compression of a commuting pair.

- Question / scope: does (Ĥ_x, Ĥ_y) = compression of a commuting pair with joint spectrum in K_δ answer L3-Q1?
- Mechanism and hypotheses: degree-1 matrix moment cone.
- Closest registry entries: 004 (two sections + commutator), 032.
- Separation criterion vs closest entry: compression ignores the Krylov/graded structure; falsifier: compression existence implying section existence (would contradict PD-N?…-301 + PD-T?…-308 together).
- Literature baseline: none read (route suggested by the orchestrator).
- Applicable obstructions and exact hypotheses broken: none.
- Novelty gate verdict: variant (not pursued for novelty).
- Cheapest decisive test: dual-cone argument at the square point.
- Kill criterion written before testing: if the square point is on the boundary of the matrix cone for small δ, the route would give an obstruction of its own.
- Actual test results: square point is interior for every δ > 0 (PD-T?…-308, PROVED) — so the route answers a weaker question and cannot detect the obstruction.
- Disposition: REJECTED for L3-Q1.
- Disposition reason: failed — the mechanism (compression model) does not achieve the aim (exact sections) under the stated hypotheses; scope: square case, perturbative regime. Positive side result kept as PD-T?…-308. No PD-N (the negative content is the logical gap "compression ⇏ section", recorded here and in 308's Scope).
- Topic / audit / history: R01.

## IDEA?bivariate-lanczos-claude-304 — Xu block-Jacobi commutativity with free last block / graded commuting extensions (route (iii))

Aliases: interior commutativity conditions; truncated Favard; graded commuting extension; DST-type extension.

- Question / scope: characterize consistent section data and relate to commuting extensions.
- Mechanism and hypotheses: words formula; commutator supported on block (n,n).
- Closest registry entries: 030 (commutator identity), 032, 033; LIT xu-siam-1994 eqs (2.5)–(2.7).
- Separation criterion: finite truncated statement with explicit inverse (Xu states infinite-sequence consequences of orthogonality and cites Favard); falsifier: a structured pair with interior commutativity not arising from any functional (checked exactly not to occur, n ≤ 4, and proved).
- Novelty gate verdict: variant of known theory (finite truncated form; treated as a tool, no novelty claim).
- Cheapest decisive test: exact rational check of commutator support for a measure and a non-measure functional.
- Kill criterion written before testing: nonzero commutator rows of degree < n in the exact check.
- Actual test results: no nonzero low rows (n = 1..4), log `favard_check.log`.
- Disposition: survived as tool → PD-T?…-301. Graded commuting extensions of Ĥ with joint spectrum in K_δ ⟺ positive measures on K_δ with sections Ĥ (routine, PD-T?…-302(a)); general (non-graded) DST extensions do not preserve the sections (coupling block from degree ≤ n−1 columns must vanish).
- Topic / audit / history: R01.

## IDEA?bivariate-lanczos-claude-305 — Quantitative Lin theorem for the nearly commuting computed pair (route (iv))

Aliases: Lin's theorem; Kachkovskiy–Safarov √‖[A,B]‖ bound (attribution UNVERIFIED in R01; CONFIRMED in R03 from the arXiv fulltext via WebFetch: Introduction (1.3), dimension-free C, consequence of Thm 1.1 — see lit_reading.md; record kachkovskiy-safarov-2016 to be updated by the orchestrator).

- Question / scope: obtain the backward measure from a nearby commuting pair.
- Mechanism: almost commuting symmetric (Ĥ_x, Ĥ_y) ⇒ commuting (A′, B′) at distance f(‖[Ĥ_x, Ĥ_y]‖), joint spectrum near the nodes.
- Closest registry entries: 029, 031, 034.
- Separation criterion / falsifier: would give a measure whose sections equal Ĥ only if (A′, B′) kept the structural pattern; falsified in general (the joint spectral measure of (A′, B′) has sections ≠ (A′, B′) unless the pattern holds).
- Literature baseline: Lin 1997 / Kachkovskiy–Safarov not read (pending-reference); used only as a hypothetical tool.
- Cheapest decisive test: logical — in the perturbative regime Ĥ is already ε-close to the commuting pair H, so any Lin bound f(ε) ≥ ε is dominated by the trivial one, and it never enforces the Krylov structure.
- Kill criterion written before testing: if a Lin-type nearby commuting pair could be chosen structured (graded) with spectrum within o(√ε) of the nodes for all perturbations, PD-N?…-302 would be contradicted.
- Actual test results: PD-N?…-302 (PROVED) shows the structured version cannot beat √ε in the square case, and PD-N?…-301 shows it can fail entirely.
- Disposition: REJECTED for L3-Q1. Disposition reason: failed (does not produce exact sections; dimension-free content irrelevant at fixed N; scope: perturbative regime). Possibly relevant for reading (G) at large N — deferred there.
- Topic / audit / history: R01.

## IDEA?bivariate-lanczos-claude-306 — "A construction that always works with δ = O(ε)" (kill-test branch 2) in the square case

- Disposition: REJECTED: refuted for every Π_n-unisolvent square set, n ≥ 1 → PD-N?bivariate-lanczos-claude-302 (PROVED).
- Kill criterion (plan.md, written before testing): a construction that always works with δ = O(ε) kills the obstruction claim — refuted, so it cannot fire in the square case.

## IDEA?bivariate-lanczos-claude-307 — Greenbaum-type exact commuting (graded) backward model with δ(ε) → 0 in the square case

Aliases: seed 005 in its exact form.
- Disposition: REJECTED: refuted for Padua n = 3 → PD-N?bivariate-lanczos-claude-301 (CONDITIONAL on independent rerun of the exact checker); MEASURED failure for Padua n = 4..7 (PD-T?…-307); holds with δ ≍ √ε for n = 1 (PROVED) and Padua n = 2 (CONDITIONAL).
- Kill criterion (plan.md): explicit small-n perturbation satisfying all interior commutativity conditions, no representing measure with δ → 0 — FIRED at Padua n = 3 (family E = −ε ev_ζ, p*(ζ) > 0).

## IDEA?bivariate-lanczos-claude-308 — Weight-only backward model in the overdetermined case

Aliases: same nodes, perturbed weights; δ = 0.
- Mechanism: if the nodes are Π_{2n+1}-unisolvent, every functional near L_μ is a positive combination of the same point evaluations.
- Closest registry entries: 017 (structured backward stability, "ill-posed as stated").
- Separation: 017's ill-posedness concerns exact commutation of computed sections; here the sections need not commute (overdetermined) and the backward data are weights only.
- Disposition: survived → PD-T?…-303(a) (PROVED), threshold ε < r(0) ≥ w_min σ_1.

## IDEA?bivariate-lanczos-claude-309 — Quadratic-generator (Hankel) form of S_1 in the square case (R02)

Aliases: p_C = Σ c_jk q_j q_k, C ⊥ Hankel; Hankel test Σ G_iA_iG_iᵀ ∈ Hankel.
- Closest: IDEA 302 (H); seed 033; record bos-dmv-xu-2007 (two-term Padua generators, as reported).
- Separation: turns (H) into an SDP with explicit generator gradients; falsifier (K5): span{p_C} ≠ S_1 numerically.
- Kill criterion (before testing): K5 (R02 §1). Result: did not fire (Padua n ≤ 7, random n ≤ 6).
- Disposition: survived → PD-T?…-309 (PROVED parts), PD-T?…-307 item 5 (MEASURED). Open: proof of S_1 = {p_C}.

## IDEA?bivariate-lanczos-claude-310 — Closed-form certificate C1 = Σ_j (q_j² − q_{j−1}q_{j+1}) for all Padua n ≥ 3 (R02)

- Kill criterion (before testing, K6): reject if λ_min(G_iᵀC1G_i) < 0 at some node for some n ∈ [3, 12].
- Result: fired — min λ = −0.199 (n = 3) … −1.4e-5 (n = 12), negative for every n = 2..12 (log `r02_closed_form_C.log`).
- Disposition: REJECTED; reason: failed (this explicit C does not certify PD Hessians; scope n = 2..12, Padua). No PD-N (single explicit trial; the deficit → 0 suggests a corrected C may work — R02 next question).

## IDEA?bivariate-lanczos-claude-311 — "(H) is decided by the square count / checkerboard structure alone" (R03 control)

- Hypothesis tested: all ordered square checkerboards behave like Padua (transition at n = 3).
- Kill criterion (before testing): an ordered checkerboard family with (H) at some n ≥ 3 (t_D > 1e-6) kills it.
- Result: fired — equispaced checkerboards satisfy (H) for n = 3, 4, 5 (t_D = 1.8e-3, 1.3e-4, 4.8e-6); graded for n = 3, 4 (PD-T?…-307 item 6, MEASURED).
- Disposition: REJECTED; reason: refuted within the measured scope (numerical, MEASURED evidence only; no PD-N because the refuted statement was a working hypothesis, recorded here). Consequence: the Padua obstruction is a property of the Chebyshev–Lobatto distribution, not of the square count; δ(ε) in the square case is node-set dependent (√ε vs obstruction).

## Proposed obstruction rows for state/IDEAS.md (orchestrator to merge at PR preparation)

| Obstruction | Exact obstruction and hypotheses | Affected | Evidence | Scope / escape |
|---|---|---|---|---|
| OBST?…-L3-a | Square case M = N_n: dim Π_{2n+1} − 3N_n = n(n+1)/2 > 0 polynomials vanish to second order at all nodes, so exact backward measures need support spread ≥ c√ε (≥ c√‖κ̂‖) | 004, 005, 031, 032 | PD-N?…-302 PROVED; PD-T?…-304 PROVED | escape: residual ≥ perturbation (trivial), or fully commuting data (δ = O(ε)) |
| OBST?…-L3-b | Locally nonnegative singular polynomial: Padua n = 3 has p* ∈ Π_7 with double zeros and PD Hessians at all nodes ⇒ no exact backward measure within δ_0 for perturbations with E(p*) < 0 | 005, 031, 032 | PD-N?…-301 CONDITIONAL (rerun); n = 4..7 MEASURED | escape: support beyond δ_0, residual ≥ |E(p*)|, or error directions with E(p*) ≥ 0 |
| OBST?…-L3-c | Computed coefficients are overdetermined (excess e_n = 1, 6, 17, 36, … relations), so the completed H_y and the functional L̂ are defined only up to the consistency defect | 008, 031 | PD-T?…-301(d) PROVED (count) | relevant for reading (G) and L2's ω-recurrence |

## IDEA?bivariate-lanczos-claude-312 — "Equispaced checkerboards satisfy (H) for every n" (R04)

- Kill criterion (before testing, K9): killed by an exact primal (failure) certificate at any tested n.
- Result: not killed for n ≤ 7 (exact dual certificates, PD-T?…-310, CONDITIONAL on rerun); n = 8 unresolved; margins collapse super-geometrically (PD-T?…-311, MEASURED).
- Disposition: open (neither confirmed nor refuted beyond n = 7).

## Pending corrections (frozen files not edited; recorded per coordinator instruction 2026-10-31)

- PD-T?…-307 item 6 and R03 §2 say "equispaced … n = 6 unresolved": superseded by R04 — (H) is exactly certified for n = 6, 7 (PD-T?…-310); first unresolved n is 8.
- R02/R03 STATUS.md timestamps (23:20, 23:40) were estimates written before the hand-back at ≈ 23:05, not observed times (orchestrator note in STATUS.md). From R04 on, STATUS lines use `date -Iseconds`.
- R01 §7 / candidates IDEA 305 (R01 text) call the Kachkovskiy–Safarov attribution UNVERIFIED; R03 lit_reading.md confirms it (Introduction (1.3)). Same for Koiran §1.4 "wide open".
