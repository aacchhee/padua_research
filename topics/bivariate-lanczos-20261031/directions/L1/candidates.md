# L1 (+L4) candidate records

Direction L1 (+L4) of topic `bivariate-lanczos-20261031`. Developer: Claude Opus 5.5, xhigh (mathematical development). Template: `templates/IDEA.md`. Provisional IDs `IDEA?bivariate-lanczos-claude-1nn` (L1) and `-4nn` (L4); final IDs only at PR preparation. No novelty claims (the adversarial reconstruction is a separate agent).

Novelty-gate scope (2026-10-31, R01): read `state/IDEAS.md` in full (seed rows 001-048, obstruction rows OBST-01..15, disposition table), `baseline-candidates.md` rows 001-010, 048 and notes 1-9, `literature/INDEX.md` rows 001-055 and 101-162, records `huhtanen-larsen-bit-2002`, `huhtanen-larsen-simax-2002`, `bartels-jezioranski-1985` in full, the first sections of `sinha-2026`, `simonova-tichy-2025`, `carson-et-al-2025`, `paige-1976`, `paige-1980-lanczos`, `paige-1971`, `greenbaum-1989`, `freund-2000`; the HL BIT and HL SIMAX fulltexts (pdftotext into the scratchpad; HL BIT pp. 394-398 re-read for Algorithm 1 and Thm 2.3). Terms searched in the registry and index: Paige, block Paige, band Lanczos, injected, joint Ritz, single section, commutator, implicit column, defect, rotation, complex symmetric, bilinear, Christoffel, node component. Limitation: block-Lanczos sources are abstract-level in the repository (fulltexts not inspected); any transfer statement citing them is LITERATURE-as-reported.

Kill criteria below were written **before** the corresponding experiment was run (R01, 2026-10-31); the run logs are in `logs/`.

---

## IDEA?bivariate-lanczos-claude-101 — per-operator (single-section) governance of loss of orthogonality

Aliases: single-section Paige; "L1 reduces to per-operator block Paige theory"; H_x-alone / H_y-alone Ritz prediction.

- Question / scope: in [FP], for the BJ window recurrence (CGS, no reorthogonalization) and the HL variant (window + local MGS with one conditional reorthogonalization), is max|Q̂ᵀQ̂ − I| predicted by u / (min Ritz residual) of a single section H_x = UᵀXU or H_y = UᵀYU (U an orthonormal basis of the computed span)?
- Mechanism and hypotheses: per-operator Paige identity for the operator whose local relations are complete; diagonal X, Y, distinct nodes, positive weights.
- Closest registry entries (read in full): IDEA?…-002 (joint-Ritz Paige theorem), -006 (loss ≈ u/joint residual, measured by supplier), -009 (band placement), OBST?…-02, -03, -05, -06.
- Separation criterion vs closest entry: -002/-006 posit the joint section Z = H_x + iH_y; this candidate posits a single real section. Falsified (for this candidate) by a run where Z predicts within the factor-3 band and neither single section does, or by a run where a single section has converged Ritz pairs (u/res ≫ measured loss) without loss.
- Literature baseline and search limitations: HL SIMAX p. 1088 (observation, (N, N*) form); no paper in the corpus compares single vs joint sections (reading result, not exhaustive).
- Applicable obstructions and exact hypotheses broken: OBST-03 (one operator's section is only partly formed) — this candidate must say which operator; OBST-06 (block Paige itself conditional).
- Novelty gate verdict: variant with difference (of -002, the opposite hypothesis); within documented search.
- Cheapest decisive test: the frozen L1-Q1 measurement (below), plus a rotation pair (same node set rotated by θ = 0.3 rad): the graded spaces and the joint residuals are rotation invariant in exact arithmetic, the single-section residuals are not.
- Kill criterion written before testing (pre-registered decision rule, R01):
  - Quantities per run r (node set, method) at analysis degrees n: L(n) = max|Q̂_nᵀQ̂_n − I| (Q̂_n = computed columns of degree ≤ n); ρ_O(n) = min over Ritz pairs of object O of ‖A_O y − θ y‖/‖y‖ with y = U_n s, U_n = orthonormal basis of span Q̂_n (one Householder QR of Q̂, nested), A_X = X, A_Y = Y, A_Z = N = X + iY, A_Nk = N on the span computed by the complex HL SIMAX run; prediction P_O(n) = u/ρ_O(n) with u := 2^-52 (the input's convention).
  - Informative degrees D_{r,O} = {n : L(n) ≥ τ or P_O(n) ≥ τ}, τ = 10³u.
  - O **predicts** on r iff D_{r,O} ≠ ∅ and L(n)/P_O(n) ∈ [1/3, 3] for all n ∈ D_{r,O} (the frozen "factor-3 band"); O **tracks** (secondary, weaker) iff max/min of L/P_O over D_{r,O} ≤ 9.
  - Frozen kill test K1 (plan.md L1-Q1, first clause) fires iff there is at least one run on which Z predicts and on every run on which Z predicts, H_x or H_y also predicts. If K1 fires, the joint formulation is not the governing object (this candidate survives); if K1 does not fire, this candidate is killed on the runs where Z predicts and no single section does.
  - Frozen kill test K2 (second clause) fires iff on the node sets outside the input's three (Padua with cubature weights, irregular domains, rotated sets), on every run with nonempty D, no O predicts.
- Test discriminability: tensor-type sets have exactly X-invariant subspaces inside S_n (S_n contains all functions of x on a grid with ≤ n+1 distinct abscissae), so single sections converge with no 2D localization; random and irregular sets localize jointly at isolated nodes; the rotation pair changes single-section residuals while leaving joint ones invariant.
- Actual test results and committed evidence (R01, `logs/r01_verdict.txt`): single sections PREDICT on the four bj runs where Z predicts (random squares; K1 fires as operationalised); they over-predict by ~10¹³ on tensor 41² at n = 40 (exact one-coordinate invariant subspaces, no loss); on all 23 informative non-product runs no object predicts (K2 fires).
- Disposition and precise rejected scope: REJECTED: failed — as the governing object of loss, within the R01 node sets (tensor over-prediction; non-product supports). Scoped negative statement: PD-N?bivariate-lanczos-claude-101 (MEASURED).
- Disposition reason: failed (MEASURED; scope R01 sets, M ≤ 6724, n ≤ 48).
- **Correction 2026-10-31T23:10Z (reconstruction 01, B2; developer re-check `logs/c01_rule_sensitivity.log`):**
  - K1 as reported ("fires") is not confirmed. The rule fixed u := 2^-52, while the plan's [FP] u is the unit roundoff 2^-53. At u = 2^-53, K1 does **not** fire: Z predicts on random1681_s0 hl, random1681_s7 hl and random6724_s0 bj. On random1681_s0 hl neither single section predicts (both only "track"); conversely, single sections predict where Z only tracks on random1681_s0, s0_swapxy and s7 bj.
  - The factor-3 band cannot separate objects whose residuals agree within 2×, which holds on every informative product-type run. Corrected report: **K1 inconclusive (no separation between single and joint sections).**
  - The tensor over-prediction rests only on the chain-completion degree n = 40. Excluded symmetrically to Padua N = M, no single-section falsifier remains.
  - Disposition narrowed: REJECTED: failed on the non-product sets (PD-N?…-101 (a), via K2) only. The rejection reason "tensor over-prediction" is withdrawn.
  - The K1 consequence "L1 reduces to per-operator Paige theory" is neither established nor refuted by R01.
  - Original disposition text kept above.
- Canonical theory / negative-result ID: PD-N?bivariate-lanczos-claude-101.
- Topic / audit / history: created R01, 2026-10-31; disposition R01.

## IDEA?bivariate-lanczos-claude-102 — joint (Z / (N, N*)) governance, retested against single sections

Aliases: joint-Ritz prediction; HL SIMAX p. 1088 observation, quantified; loss ≈ u / min joint residual.

- Question / scope: as -101, with O = Z (and N_k of the complex HL SIMAX run).
- Mechanism and hypotheses: Ritz pairs of the compression of the normal operator N = X + iY to the computed span.
- Closest registry entries: IDEA?…-002, -006 (this is -006 re-measured on new node sets and against single sections; not new).
- Separation criterion vs closest entry: none in mechanism (variant of -006 by scope only: new node sets, both methods, rotation pairs, single-section comparison). Falsified by a run with informative degrees where Z does not predict (in particular any loss without joint convergence, or joint convergence without loss).
- Literature baseline: HL SIMAX p. 1088 (LIT?…-119, observation only).
- Applicable obstructions: OBST-02 (non-normal sections), OBST-04 (Padua M = N: no long run).
- Novelty gate verdict: duplicate in mechanism of -002/-006; kept as the measured comparison record.
- Cheapest decisive test / kill criterion (pre-registered): identical rule as -101 with O = Z; killed (as a predictor) on any run where D_{r,Z} ≠ ∅ and Z does not predict.
- Actual test results: R01 — Z predicts on random squares (bj), indistinguishable from single sections there; fails on every informative non-product run; N_k (simax run) fails everywhere because the windowed (N, N*) recurrence is itself unstable (PD-N?…-102).
- Disposition: REJECTED: failed as a general mechanism (MEASURED, non-product supports); consistent but not separated from single sections on product-aligned supports (PD-T?…-107 (a)).
- **Correction 2026-10-31T23:10Z (reconstruction 01, B2):** K1 is inconclusive at the plan's u = 2^-53 (see IDEA?…-101), so this record and -101 stand or fall together. Both fail on (a) only, and are not separated on product-type runs. "Product-aligned supports" means the listed set types, not a classifier by support (PD-N?…-106).
- Canonical theory / negative-result ID: PD-N?bivariate-lanczos-claude-101 (shared), PD-N?…-102 (N_k / complex form).
- Topic / history: created R01, 2026-10-31; disposition R01.

## IDEA?bivariate-lanczos-claude-103 — exact coefficient pattern of the code's ordering (re-derivation)

Aliases: window lemma; exact-support window; HL BIT Thm 2.3 / BJ Thm 1 for the input ordering.

- Question / scope: [EXACT] which entries of H_F (full operator) and H_J (injecting operator) are nonzero, which are formed by the recurrence, which are implicit.
- Closest: HL BIT Thm 2.3 (LIT?…-106), BJ Thm 1 / Cor 3-4 (LIT?…-129/-130), HL SIMAX Thm 3.7 (LIT?…-116).
- Novelty gate verdict: duplicate (re-derivation for the campaign's ordering, kept as a checked dependency, no novelty).
- Cheapest decisive test: count check against the code's coefficients (structural zeros below 10⁻¹³ in a long-double run).
- Kill criterion: a nonzero coefficient outside the derived support in a reference run.
- Canonical theory ID: PD-T?bivariate-lanczos-claude-101 (`theory/window-coefficient-pattern-exact.md`).
- Actual test result: long-double check, max coefficient outside the derived support 1.25e-19 (R01 §2). Disposition: duplicate (re-derivation kept as a checked dependency; PROVED).

## IDEA?bivariate-lanczos-claude-104 — [FP] local relations and the growing-block Paige identity for the full operator

Aliases: F-relations; "band Lanczos for F with injected J-vectors"; growing-block Paige identity.

- Question / scope: exact algebraic consequences of the [FP] local relations of the operator whose products of every vector are formed.
- Closest: block Paige identity (sinha-2026, abstract-level), Paige 1976/1980 (as reported), OBST-06.
- Separation criterion: the blocks grow by one per degree and one column per degree is injected by the other operator; the identity has a band-leak term determined by the window width (2n+1), not by a fixed block size. Falsified if the identity reduces to a fixed-block-size block-Lanczos identity after a change of basis (it cannot: the block sizes of S_n ⊖ S_{n−1} are n+1).
- Novelty gate verdict: variant with difference (of the block Paige identity); within documented search.
- Kill criterion: an algebraic error (identity residual not at rounding level in a numerical check).
- Canonical theory IDs: PD-T?bivariate-lanczos-claude-102 (`theory/fp-local-relations-window-recurrence.md`), PD-T?…-103 (`theory/full-operator-paige-identity-growing-blocks.md`).
- Actual test results (R02): identity residuals at rounding level; the identity controls 0–47% (typically ≤ 10% for F-Ritz vectors) of the new block's component along y. Disposition: survives as a PROVED identity (variant with difference); not a loss bound (R02 F5).

## IDEA?bivariate-lanczos-claude-105 — the HL SIMAX section equals Z

Aliases: N_k square part = H_x + iH_y; (N, N*) section identity.

- Statement: [EXACT] the square part of N_k in HL SIMAX (4.2) is unitarily similar to Z = UᵀXU + iUᵀYU for any real orthonormal basis U of S_k; Ritz values and Ritz residuals coincide.
- Closest: LIT?…-117 (HL SIMAX (4.2)); this is an identification, not a mechanism.
- Novelty gate verdict: routine identification; recorded because it collapses two of the four objects of the frozen comparison in exact arithmetic.
- Canonical theory ID: folded into PD-T?…-101 as a minor routine lemma.

## IDEA?bivariate-lanczos-claude-401 — L4: no commuting operator reproduces consecutive graded spaces with a fixed number of starts

Aliases: L4 obstruction; band-Krylov non-placement; codimension obstruction.

- Question / scope: plan L4-Q1.
- Mechanism and hypotheses: codimension of S_n ∩ A S_n in S_n bounds the number of starting vectors of any band/block Krylov sequence through S_n from below; A S_n ⊂ S_{n+1} forces A affine in (X, Y) on unisolvent nodes.
- Closest: IDEA?…-009, -048, OBST-05, OBST-12 (Huhtanen reduction B = q(A), unbounded degree).
- Separation criterion: -009/OBST-05 is a heuristic (ill-conditioned monomial start block, x-degree order); this candidate is a proof for every A in the commutant of {X, Y} and every block/band start, and it records the non-commutant counterexample A = Q T Qᵀ that makes the question trivial without the commutant restriction. Falsified by an explicit A = f(X, Y) and fixed start block reproducing S_n, S_{n+1} for some n ≥ m on nodes satisfying the stated unisolvence.
- Novelty gate verdict: variant with difference (proof of a reported heuristic); within documented search.
- Cheapest decisive test: the proof; numerical sanity check of the codimension count.
- Kill criterion (frozen, plan.md): an explicit A = f(X, Y) and fixed start block reproducing the graded spaces for all n.
- Canonical theory ID: PD-T?bivariate-lanczos-claude-401 (`theory/l4-band-krylov-obstruction.md`).
- Actual test result: proof complete (R01); numerical sanity check of the codimension count `logs/r01_l4_codim_check.log`. Disposition: PROVED; frozen L4 kill test not triggered.

## IDEA?bivariate-lanczos-claude-106 — instability of the window recurrence on non-product supports

Aliases: non-product instability; rotation sensitivity of the window recurrence; marching instability; "defect instability" (R01 working name).

- Question / scope: why loss grows exponentially from low degree on supports that are not products in the recurrence's coordinates (R01 M3), for BJ and HL alike.
- Mechanism and hypotheses: amplification of local rounding by the computed recurrence's per-node propagator (PD-T?…-104), whose factorisation into univariate Jacobi propagators holds exactly for product measures (PD-T?…-105) and fails otherwise (within-degree coupling A′_t not diagonal).
- Closest registry entries (read in full): IDEA?…-008 (commutator-defect ω-recurrence remark), OBST?…-03 (H_y only partly computed), IDEA?…-006, OBST?…-04; literature: HL BIT p. 401 and HL SIMAX p. 1088 (observations of loss at "very high degree"); Zaccaron 2014 Table 2.1 as reported (exponential profile, node set unidentified).
- Separation criterion vs closest entry: -008 posits that the commutator defect must enter a 2D ω-recurrence; here the defect enters (PD-T?…-106) but is not what grows — the growth is amplification by the propagation term, present for errors from F-products alone. Falsified by a non-product support on which errors injected only in F-products are not amplified (mixed-precision test) or by an exact product measure with growing propagator.
- Literature baseline and search limitations: no rounding analysis in the seven fulltexts (Step 0); block-Lanczos sources are single-operator (abstract-level); no source in the corpus mentions dependence on the orientation/shape of the support.
- Applicable obstructions and exact hypotheses broken: OBST-04 (Padua M = N) does not apply (M ≫ N sets used).
- Novelty gate verdict: new within documented search (no claim of novelty in the literature; adversarial reconstruction pending).
- Cheapest decisive test: rotation pairs (R01) and mixed-precision localisation (R02).
- Kill criterion (stated post hoc in R02, **not** pre-registered: the mixed-precision run was designed and run before this record was written): if F-only-double and J-only-double runs differ in growth rate by more than a factor 10 per 4 degrees, the instability is attributed to the product type with the larger rate (not intrinsic amplification).
- Test discriminability: the two partial-precision runs isolate the origin of the amplified errors.
- Actual test results: both partial runs reproduce the all-double growth on the rotated square (R02 §3); kill criterion not met → intrinsic amplification.
- Disposition: active (theory PD-T?…-105 for the product case; lower bound for a non-product case OPEN, R03).
- Canonical theory ID: PD-T?…-105, PD-T?…-107; negative statement PD-N?…-101.
- **Correction 2026-10-31T23:10Z (reconstruction 01, P2/P3):**
  - The conclusion "intrinsic amplification" was not tested against the selection rule. The mixed-precision test only localises the error source between F- and J-products. Different one-relation parent rules change the loss by 10³–10⁸ (PD-N?…-105), so "intrinsic" holds per selection rule only.
  - The geometry-dependence observation is prior art (Zaccaron 2014, PC-5); the novelty-gate verdict is corrected to "variant with difference" per PC-5.
  - "Supports that are not products" is not a classifier: product supports with non-product weights also lose (PD-N?…-106).
- Topic / history: opened R01 (as "defect instability"), reframed R02.

## IDEA?bivariate-lanczos-claude-107 — per-node propagator response as a loss predictor (shadow recurrence)

Aliases: node-propagator predictor P(n); shadow recurrence; node-space ω-estimate.

- Question / scope: a computable quantity that predicts loss in both regimes.
- Mechanism: drive the run's own computed recurrence at all nodes with rounding-size iid forcing (PD-T?…-104 part 1); cost of one extra recurrence pass without inner products (O(M·window) per column).
- Closest registry entries: IDEA?…-003, -008 (ω-recurrence / partial reorthogonalisation, plan L2), simon-1984-mathcomp (ω-recurrence in coefficient space, abstract-level).
- Separation criterion: Simon's ω-recurrence runs in coefficient space (O(N²) state for the window recurrence); this runs in node space with the computed coefficients; falsified if P(n) misses the loss by more than 10× on a product-aligned or non-product set with M ≥ 1681 where the loss exceeds 10³u.
- Kill criterion (stated post hoc in R02, **not** pre-registered: the predictor was run before this record was written): as in the separation criterion.
- Actual test results: within 1–5× on 7 of 8 sets; misses by 50× (n = 12) and 10³ (n = 16) on the triangle → kill criterion met on the triangle; survives as a diagnostic on the other sets.
- Disposition: deferred to L2 (diagnostic for a reorthogonalisation criterion), with the triangle failure recorded (scope: diagnostic, not a bound).
- Canonical theory ID: PD-T?…-107 (c).
- Topic / history: R02.

## IDEA?bivariate-lanczos-claude-108 — exact ω-recurrence with commutator sources

Aliases: 2D ω-recurrence (exact); loss-source identity.

- Closest: IDEA?…-008 (remark, no derivation), -003; simon-1984-mathcomp, bai-day-ye-1999 (first-order models, as reported).
- Separation criterion: exact identity rather than first-order model; the bivariate term enters only through the J-products. Falsified by an algebraic error (identity residual above rounding in long double).
- Actual test result: residual ≤ 1e-19 (R02). Disposition: PROVED (PD-T?…-106); hand-off to L2 (plan L2-Q1).

## IDEA?bivariate-lanczos-claude-109 — product-measure factorisation of the node propagator

Aliases: product decoupling; tensor stability mechanism.

- Closest: IDEA?…-038 (sparse Padua / product recurrences, settled background), OBST?…-04.
- Separation criterion: a propagator (error-amplification) statement, not a statement about sparsity of the exact sections; falsified by a product measure with propagator growth not explained by its marginals.
- Actual test result: tensor 41² and Padua cubature flat (R02). Disposition: PROVED under the idealisation (PD-T?…-105); FP transfer CONDITIONAL.

## IDEA?bivariate-lanczos-claude-110 — the non-product amplification is a property of the exact recurrence (a priori computable)

Aliases: exact-coefficient propagator growth; intrinsic marching instability; P* test.

- Question / scope: does the idealised per-node propagator with **exact** window coefficients (PD-T?…-105 setting, without the product assumption) already grow exponentially on non-product supports, or is the growth a feedback through the computed (rounding-corrupted) coefficients?
- Closest: IDEA?…-106 (mechanism), -109 (product factorisation), PD-T?…-107 (c).
- Separation criterion: an a priori statement (a property of the measure and the ordering) vs an a posteriori one (a property of the run). Falsified as stated in the kill criterion.
- Kill criterion written before testing (R03, before `l1_exact_propagator.py` was run): with M = 1681 (seed 11 sets) and n ≤ 20, if P*(n) (exact coefficients, long double) grows by less than 10× from n = 4 to n = 20 on the square rotated by π/4 and on the disk while P(n) (computed coefficients) grows by ≥ 10³ there, the amplification is a feedback of coefficient corruption, not intrinsic (candidate killed). Conversely, if P* and P agree within 3× per degree-4 step on those sets and P* stays within 10× growth on the square, the amplification is intrinsic (candidate survives).
- Test discriminability: P* uses only exact coefficients (full long-double reorthogonalisation); P uses the run's coefficients; the forcing is identical in size.
- Actual test results (R03, `logs/r03_exact_propagator.log`): P* = P to the printed digit on square, square rotated by π/4, disk, triangle; P* grows by ≈ 4·10⁹ from n = 4 to 20 on the rotated square. Kill criterion not met.
- Disposition: survives (MEASURED, scope M = 1681, n ≤ 20); canonical record PD-T?bivariate-lanczos-claude-109 (a); an a priori bound is OPEN (R04).
- Novelty gate verdict (added 2026-10-31T23:10Z; the template line was missing, recon-01 P2): variant with difference. The exact-coefficient propagator is classical as an object (BPS 2010 (18)–(20), Clenshaw as triangular substitution); the measured a-priori growth for the dev selection is not found in the documented search.
- **Correction 2026-10-31T23:10Z (reconstruction 01, B1/P4):** "a property of the measure and the ordering" must include the selection (parent) rule. The P* test was run for the dev rule only, and other rules give different exact propagators (recon-01 `prop_selection.log`; PD-N?…-105). Disposition unchanged in substance: survives for the dev rule.

## IDEA?bivariate-lanczos-claude-111 — the non-product amplification comes from the single-relation row selection, not from truncation

Aliases: triangular row selection of the Jacobi pencil; two-relation block recurrence control; Xu-type left inverse.

- Question / scope: the window recurrence at a point z is forward substitution for a triangular selection of one row per column out of the stacked pencil [xI − H_X; yI − H_Y] (R03 §2). Is the amplification due to that selection?
- Closest: IDEA?…-110, -106; xu-siam-1994 (block three-term relations with both coordinates, as recalled there; Favard theory in Xu's Trans. AMS paper, pending-reference); liu-narayan-2023 (multivariate Stieltjes with both relations, as reported); fasondini-olver-xu-2023 (block Lanczos on multiplication matrices, as reported).
- Separation criterion: keeps the same exact truncation (block tridiagonal, window = two previous blocks) but uses both relations per block with an orthonormal (SVD) completion; differs from the window recurrence only in the row selection.
- Kill criterion written before testing (R03, before `l1_both_relations.py` was run): on the square rotated by 0.3 and by π/4 and on the disk (M = 1681, seed 11), if the two-relation block recurrence (one CGS pass against blocks n−2, n−1, then SVD) has loss at n = 20 within 10× of the BJ window recurrence's, the row selection is not the cause (killed); if its loss at n = 20 stays below 10³u ≈ 2.2e-13 on all three, the selection is the cause (survives).
- Actual test results (R03, `logs/r03_both_relations.log`): two-relation loss at n = 20: 2e-14 (rotated 0.3), 1e-14 (π/4), 9e-15 (disk); BJ: 1e-8, 2e-6, 2e-10. Kill criterion not met.
- Disposition: survives (MEASURED); canonical records PD-T?…-108 (row-selection lemma, PROVED) and PD-T?…-109 (b); hand-off to L2/L5 as a remedy candidate (no analysis yet).
- Novelty gate verdict (added 2026-10-31T23:10Z; the line was missing, recon-01 P2): variant with difference. The algorithmic predecessor is Liu–Narayan 2023 (block Stieltjes with all coordinate relations, PC-6); the stacked system and left inverses are classical (Xu, Dunkl–Xu, BPS 2010; PC-7, PC-9).
- **Correction 2026-10-31T23:10Z (reconstruction 01, B1):**
  - The kill criterion can only show that the truncation is not *sufficient* for the growth: two relations with the same truncation are stable on the three tested sets. The recorded inference "the row selection, not the truncation, causes the instability" (R03 §3 B) exceeds that, and it is **REJECTED: refuted** (PD-N?…-105, MEASURED).
    - Some one-relation selections are 10³–10⁸ more stable than dev at the same truncation.
    - Without truncation, single-pass CGS with the dev rule is stable on rotation π/4 and the disk, but as unstable as BJ on the triangle and rotation 0.3.
  - What survives (MEASURED): the two-relation block recurrence removes the growth on the rotated squares and the disk at the same truncation, and reduces it on the triangle. It does not help, or is worse, on the Gaussian cloud, the tensor grid and the clustered checkerboard (PD-T?…-109 (b), narrowed; PD-N?…-103 (c)).
  - Disposition: the candidate as titled is REJECTED: refuted; the two-relation control is kept as a measured, scoped observation (L2 hand-off).

---

## Pending corrections to reviewed R01–R03 files (found in R04; the reviewed files are not edited — corrections are stated in R04.md §6)

- PC-1 (PD-N?…-101, (a) parameter range): the probe sets of `l1_defect_probe.py` (square rotated by 0.05; sheared squares; rotated Beta-product set) were listed as sets on which loss exceeds u/ρ_O by 10²–10¹⁴, but that probe computed **no** Ritz residuals. The 10²–10¹⁴ statement is supported only on the R01 main sets and on the seed-11 square rotated by 0.3 and π/4, disk and triangle (u/ρ_Z from `l1_node_propagator.py`). For the square rotated by 0.05 the loss at n = 24 is 2e-13, i.e. borderline (≈ 3× the seed-11 square's u/ρ_Z), not a 10²-fold miss.
- PC-2 (PD-T?…-107 (b)): "loss grows exponentially from degree ≈ 8–12" does not hold for the 0.05 rotation (loss 7e-15, 2e-14, 2e-13 at n = 16, 20, 24: growth starts near n ≈ 18).

## IDEA?bivariate-lanczos-claude-112 — near-product perturbation bound for the node propagator (R04)

Aliases: discrete-Gronwall transfer bound; near-product upper bound; product-of-marginals reference.

- Question / scope: R03 §8(a): an a priori upper bound on ‖L*(z)⁻¹‖ for measures whose window coefficients are close to those of a product-type reference.
- Mechanism and hypotheses: write L*(z)⁻¹ through block transfer matrices T_t(z) (degree blocks); compare with the reference μ_x ⊗ μ_y (product of the marginals of μ), whose transfers factorise (PD-T?…-105); perturbed-product (discrete Gronwall) lemma.
- Closest: IDEA?…-109, -110, -111; Bauer–Fike/perturbed-product lemmas are textbook (not recorded).
- Separation criterion: quantitative bound in terms of ε_t = ‖T_t − T⁰_t‖ and the reference constant K; falsified by any sampled (node, s, t) where the measured transfer-product norm exceeds the bound (that would be a proof or code error).
- Kill criteria written before testing (R04, before `l1_r04_near_product.py` was run): (K1) consistency: at every sampled node and pair s < t ≤ 20 the actual ‖T_t⋯T_{s+1}‖₂ ≤ K Π(1 + Kε_r); any violation kills the implementation/proof until explained. (K2) informativeness (classification, not a kill): at θ = 0 (random square vs product of its marginals) and θ = 0.05 the bound is "informative" if log10(bound/actual) ≤ 2 for the median sampled node at t = 20, s = 0. (K3) rate scaling hypothesis H_lin (toy-model prediction, R04 §2): the excess growth rate g̃(θ) = g(θ) − g(0) of the exact-coefficient propagator response (per degree, between n = 12 and n = 24, square M = 1681 seed 11 rotated by θ) is linear in θ: H_lin is killed if g̃(θ)/θ at θ = 0.025 differs from g̃(θ)/θ at θ = 0.2 by more than a factor 3.
- Actual test results: R04.md.

## IDEA?bivariate-lanczos-claude-113 — measures that agree with a product measure up to degree 2n+1 (Padua cubature, Harris–Simanek checkerboards) inherit the product factorisation; checkerboard control (R04)

Aliases: moment-matching extension; checkerboard control; product-type measure on a non-tensor support.

- Question / scope: PD-T?…-105 assumed a tensor grid. Does the factorisation hold whenever the inner products up to degree 2n+1 equal those of a product measure, and does the FP recurrence on Harris–Simanek checkerboards (M = N, ordered X of length m+1, Y of length m+2, weights |1/ω′|) behave like the product regime?
- Closest: IDEA?…-038 (sparse Padua/HS recurrences, settled background), plan.md Benchmarks (HS checkerboards; codex branch claims cited by ID only, not used as dependencies), IDEA?…-109.
- Separation criterion: support is not a tensor grid and M = N; falsified if the exact window coefficients of a checkerboard are not product-type below degree m (within-degree coupling > 1e-12 relative), or if (product-type coefficients but) the FP loss shows bivariate amplification.
- Kill criteria written before testing (R04, before `l1_r04_checkerboard.py` was run), m = 30 (M = N_30 = 496), e = 0, three node families (Chebyshev–Lobatto-type, equispaced, clustered x = s|s|² on equispaced s): (C1) product type: max within-degree coupling ratio (PD-T?…-107 (e)) over degrees ≤ m − 1 is ≤ 1e-12 for all three families — else the moment-matching claim is killed for that family; (C2) no bivariate amplification: the 2D BJ loss at every degree t ≤ m − 2 is ≤ 100 × max(10³u, L_x(t), L_y(t)), where L_x(t), L_y(t) are the losses of univariate Lanczos (no reorthogonalisation) on (X, |w_X|) and (Y, |w_Y|) at step t — else the CONDITIONAL FP transfer of PD-T?…-105 fails on that family.
- Actual test results: R04.md.

## IDEA?bivariate-lanczos-claude-114 — componentwise-scaled forcing for the node-propagator predictor; factorised explanation of the clustered checkerboard (R04)

Aliases: scaled shadow recurrence; factorised propagator test.

- Question / scope: after the R04 checkerboard run fired (C1) and (C2) on the clustered family (disclosed in R04.md), and the R02 predictor was found to use a forcing model that is wrong for strongly non-uniform node magnitudes (uniform u/√M at every node): does componentwise-scaled forcing (u·N(0,1)·(|a q̂_p(i)| + Σ|h||q̂_l(i)| + β|q̂_k(i)|)) repair the triangle discrepancy, and does the factorised (product-reference) propagator explain the clustered-checkerboard loss?
- Closest: IDEA?…-107 (predictor), -109/-113 (factorisation).
- Kill criteria written before testing (R04, before `l1_r04_scaled_predictor.py` was run; written after the R04 checkerboard and diagnosis runs, which motivated it): (S1) improvement: on the triangle (seed 11, M = 1681) the scaled predictor Ps is within 10× of the loss at n = 12 and 16, and within 5× on the seed-11 square, square rotated by π/4 and disk at their largest degree — else the scaled predictor is no improvement (killed as an improvement). (S2) clustered checkerboard (m = 30, cubic clustering): if Ps_factorised (product-reference coefficients) is within 10× of the measured loss at n = 8..24, the clustered growth is univariate (factorised) amplification with no bivariate component; if Ps_factorised stays more than 100× below the loss while Ps (run coefficients) tracks it, the growth is bivariate amplification by rounding-induced coupling.
- Actual test results: R04.md.

## IDEA?bivariate-lanczos-claude-115 — coefficient-aware forcing: absolute inner-product errors on structurally zero window coefficients (R04)

Aliases: coefficient-noise predictor; rounding-induced non-product coupling.

- Question / scope: the exact split Q̂ = Ξ̄ − Φ̃ (`logs/r04_actual_forcing.log`) shows that on the clustered checkerboard the loss sits in Ξ̄ (computed-coefficient polynomials) while the propagated vector-operation errors Φ̃ stay at 5e-16; the R02/R04 forcing models scale coefficient errors relative to |h|, which is ~0 for the structurally zero (product-type) window entries, whereas a computed inner product has an absolute error ~u‖q̂_l‖‖A q̂_p‖. Hypothesis: the clustered-checkerboard loss is amplification of this rounding-induced non-product coupling.
- Mechanism: forcing at node i, step k: u·ζ·(|a q̂_p(i)| + Σ_{l∈W_k}(|h_l| + ‖q̂_l‖‖A q̂_p‖)|q̂_l(i)| + β_k|q̂_k(i)|), ζ ~ N(0,1), propagated with the run's coefficients.
- Closest: IDEA?…-107, -114.
- Kill criterion written before testing (R04, before `l1_r04_coef_forcing.py` was run; motivated by the post-hoc split above): accepted if the predictor is within 10× of the loss at every degree n ≥ 8 with loss ≥ 10³u on the clustered checkerboard and on the seed-11 triangle, and within 5× on the seed-11 square, square rotated by π/4 and disk at their largest degree; otherwise killed.
- Actual test results: R04.md.

## Pending corrections from the independent prior-art check (`reviews/L1-prior-art-01.md`, received during R04; reviewed records are not edited)

- PC-5 (IDEA?…-106, novelty-gate verdict "new within documented search"): the bare observation — loss of the HL-type window recurrence depends on the domain geometry, the square is fine while the square rotated by π/4 (0.74 at degree 60) and general quadrangles lose orthogonality geometrically from degree ≈ 10 — is prior art: Zaccaron 2014, Tables 2.1–2.2, p. 16 (as read by the checker through WebFetch; locators to be re-checked). Corrected verdict: **variant with difference** — what remains not found in the documented searches is the product/non-product dichotomy as a principle, "before Ritz convergence", and the univariate (factorised) behaviour on product measures (PD-T?…-105, -111).
- PC-6 (IDEA?…-111, two-relation remedy): Liu–Narayan, SIAM J. Sci. Comput. 45(3) (2023) A1125–A1147 (arXiv 2202.04843), a block Stieltjes procedure using all coordinate relations with an eigen/SVD completion and the same three-term truncation, is the algorithmic predecessor; cite it. What remains not found: the comparison showing that, at the same truncation, the stacked relations remove the one-relation instability on non-product supports (R03) — now also known to fail on clustered checkerboards (PD-N?…-103 (c)).
- PC-7 (PD-T?…-108, row-selection lemma): the stacked overdetermined consistent system and the non-uniqueness of the left inverse D_n are classical (Xu survey arXiv 1701.02709 §2.2 eq. (2.14); Liu–Narayan Thm 3.1; Olver–Townsend–Vasil 2019 §2.3); the window recurrence's triangular selection is a special case of Xu's left inverse. No novelty is claimed for the algebra; Barrio–Peña–Sauer, J. Approx. Theory 162 (2010) 407–420, is unread and may overlap the stability link — no priority statement until it is read.
- PC-8 (PD-T?…-103 corollary): Sinha 2026 (arXiv 2609.08066) describes its block Paige identity as bounding "the overlap with a Ritz vector along its residual coordinate direction" (introduction, via WebFetch summary, R04), which is the content of the PD-T?…-103 corollary for one operator. Its E_k^inj in relation (54) is "the coordinate injection into the final block" (a selector), not injected start vectors, so the L4 "one start injected per degree" framing is not that term (per the same summary; Theorem 7 not seen). PD-T?…-103 is a variant (growing blocks with an injected column, bilinear complex-symmetric form, commutator-residual error term) of a known identity; no novelty claim for the identity itself.

## IDEA?bivariate-lanczos-claude-116 — exact rational certificate of exponential propagator growth for an explicit non-product measure (R05)

Aliases: exact certificate; triangle-grid lower bound; rational propagator entries.

- Question / scope: R03 §8(b)/R04 §10: an exact (not floating-point) lower bound on ‖L*(z)⁻¹‖ for one explicit non-product measure over a finite degree range, with a product control.
- Mechanism: identity (L*(z)⁻¹)_{k,s}² = ‖ψ_{p(s)}‖² g_k(z)²/‖ψ_k‖² between the orthonormal propagator and the monic (BJ) impulse response g; all quantities rational for integer nodes and equal weights; exact Fraction arithmetic.
- Closest: IDEA?…-110 (P* = P, floating point), PD-T?…-109 (a); Zaccaron 2014 (measured domain dependence, prior art via the checker).
- Kill criterion written before testing (R05, before the m = 24 runs of `l1_r05_exact_certificate.py`; only the m = 12, n ≤ 6 smoke test had been run): sets = triangle grid {(i, j) : i + j ≤ 24} and square grid {0..24}², equal weights, impulses at all columns of degree 2, degrees 2..12. The certificate "certifies exponential growth on the triangle" if the exact G(n) (max squared entry) satisfies log10 G(12) − log10 G(6) ≥ 6 (i.e. the entries grow by ≥ 10³ over six degrees) and the square control satisfies log10 G(12) − log10 G(6) ≤ 2; killed if the triangle increment is < 3 or the square increment is > 4; in between: inconclusive. Consistency: the exact orthogonality check must report 0 nonzero inner products (else the window or code is wrong).
- Actual test results: R05.md.
- IDEA?…-116 actual test results (R05): T_24 increment log10 G(12) − log10 G(6) = 8.69 (≥ 6), Q_24 increment 0.80 (≤ 2); exact orthogonality checks 0 nonzero. Disposition: survives; canonical record PD-T?bivariate-lanczos-claude-113 (CONDITIONAL on independent rerun).

## Pending corrections from Barrio–Peña–Sauer 2010 (received during R05; record `literature/records/barrio-pena-sauer-2010.md`)

- PC-9 (IDEA?…-111, PD-T?…-108, -104): BPS (J. Approx. Theory 162 (2010) 407–420) is the closest predecessor of the row-selection/propagator framing in the evaluation setting (eq. (5) one variable per polynomial; eq. (6)/Thm 8 averaged form; Remark 9 choice of j matters numerically; §5 heuristics; (18)–(20) triangular substitution with comparison-matrix bounds). Corrected novelty-gate verdict for IDEA?…-111 and the PD-T?…-108 framing: variant with difference; separation = discrete-measure Lanczos vectors with window truncation, the orthogonality-loss link (PD-T?…-104, -106), and the non-product exponential amplification vs product factorisation (PD-T?…-105, -107, -109, -111, -113). See R05.md §5.
- PC-10 (IDEA?…-109 / PD-T?…-105 part 1): product measures give products of univariate monic OPs generated by univariate three-term recurrences (BPS Remark 5) — known; the propagator factorisation (part 2) is the part not found.

---

## IDEA?bivariate-lanczos-claude-117 — the coefficient channel on clustered product-type measures: which coefficient errors carry the loss (R06)

Aliases: coefficient-map conditioning test; off-pattern (structural-zero) coupling hypothesis H_off; u-perturbation tests H_cond.

- Question / scope: R05 §8 / R04 PD-T?…-112 (a, b): on the cubic-clustered checkerboard (m = 30) the loss sits in Ξ̄, the node values of the polynomials defined by the computed coefficients. Which part of the coefficient error carries it, and do u-sized perturbations of the exact (product-type) coefficients reproduce it?
- Mechanism tested: build Ξ(c) = node values of the polynomials generated by coefficients c (window recurrence from q̂_0 without forcing, long double) and measure the Gram defect D(n) = max|Ξ_nᵀΞ_n − I|.
- Closest: PD-T?…-112, IDEA?…-114/-115, PD-T?…-105/-111 (exact product-type coefficients).
- Kill criteria written before testing (R06, before `l1_r06_coefficient_channel.py` was run), clustered checkerboard m = 30, n = 16 and 20, BJ loss L(n) as measured in the same script:
  - H_off ("the loss is carried by the off-pattern entries — computed values at positions where the exact product-type coefficient is 0"): survives iff D for (BJ on-pattern values, off-pattern zeroed) is ≥ 100× below L(n) **and** D for (exact coefficients + BJ off-pattern values) is within 10× of L(n), at both degrees; killed otherwise.
  - H_cond-abs ("absolute u-noise on the structural zeros reproduces the loss"): with exact coefficients plus u·N(0,1) on every off-pattern window entry (3 seeds, median D): survives iff within 10× of L(n) at both degrees; killed if ≥ 100× below at either degree; otherwise inconclusive.
  - H_rel-harmless ("relative u-noise on the nonzero product-type entries and β is harmless"): survives iff the median D is ≥ 100× below L(n) at both degrees; killed if within 10× at either.
- Actual test results: R06.md.

- R06 note (2026-10-31, after the IDEA-117 run, before `l1_r06_gain_identity.py` was run): the first-order product-case gain identity (PD-T?…-114, derived after seeing the IDEA-117 results) is checked numerically by the criterion, written before the check run: for every sampled window entry (k, l) of the clustered and the equispaced checkerboard (m = 30, degrees ≤ 20), |A_direct − A_formula|_{e,d} ≤ 1e-8·‖R_d‖ for all (e, d), where A_direct = Ξ*ᵀR is computed by propagating the forcing through the exact-coefficient recursion in long double and A_formula from univariate data only. A violation means the identity (or its implementation) is wrong. The comparisons of first-order predictions with the IDEA-117 measurements are descriptive (no criterion).

- **Pending correction PC-11 (R06, 2026-10-31T22:36:02Z; PD-T?…-112 (a)):** the clustered-checkerboard coefficient deviations quoted in PD-T?…-112 (1.0e-6 double, 9.4e-10 long double) are maxima over degrees ≤ 29; over degrees ≤ 24 the on-pattern deviation is 1.6e-14 and harmless, and the channel is carried by the off-pattern values (2.1e-13). Read PD-T?…-112 with PD-T?…-114. Details: R06 §5.

---

## IDEA?bivariate-lanczos-claude-118 — why the BJ off-pattern errors are benign: rounding vs feedback vs signs (R07)

Aliases: off-pattern error anatomy; φ/ρ split.

- Question / scope: R06 §8. Clustered checkerboard m = 30 (as in R06), BJ block CGS, nmax = 24, degrees n = 16 and 20, L(n) = BJ loss in the same script, D(·) = nonlinear long-double Gram defect of Ξ(c* + δ) with δ only on off-pattern entries (R06 definitions).
- Split of the BJ off-pattern values h = φ + ρ, φ_{k,l} = Σ_i q̂_{i,l} u0_i evaluated in long double from the stored double vectors (u0 = fl(a ⊙ q̂_{p(k)}) as in the code), ρ = h − φ (rounding of the double dot product).
- Kill criteria written before testing (2026-10-31T22:36:02Z, before `l1_r07_offpattern_anatomy.py` was written or run; the script name was lost to shell substitution in the first write and restored by hand at once):
  - H_fb ("the feedback part carries the loss"): survives iff D(c* + φ) is within 10× of L(n) and D(c* + ρ) ≥ 100× below L(n) at both degrees; killed if D(c* + φ) ≥ 100× below L(n) at either degree; otherwise inconclusive.
  - H_rd ("the rounding part carries the loss"): survives iff D(c* + ρ) within 10× of L(n) and D(c* + φ) ≥ 100× below L(n) at both degrees; killed if D(c* + ρ) ≥ 100× below L(n) at either degree; otherwise inconclusive.
  - H_term ("independent rounding of every product term, δh_{k,l} = u Σ_i ε_i ξ*_{i,l}(a ξ*_{p(k)})_i with ε_i iid N(0,1), reproduces the loss"; 3 seeds, median D): survives iff within 10× of L(n) at both degrees; killed if ≥ 100× above or ≥ 100× below at either degree; otherwise inconclusive.
  - H_sign ("magnitudes suffice: |h| with random signs reproduces the loss"; 3 seeds, median D): survives iff within 10× of L(n) at both degrees; killed if ≥ 100× above at either degree; otherwise inconclusive.
- Descriptive only (no criterion): sizes of φ, ρ, u·s, u·ŝ (s = Σ_i |ξ*_{i,l}||(aξ*_p)_i|, ŝ = ‖ξ*_l ⊙ aξ*_p‖₂) on the 100 largest-gain off-pattern entries; equispaced control.
- Actual test results: R07.md.

---

## IDEA?bivariate-lanczos-claude-119 — term-wise rounding through the exact coefficient map as an a-priori loss estimate on product-type measures (R07)

Aliases: term-wise first-order predictor; exact-data loss estimate.

- Motivation (after the IDEA-118 run, which is in R07.md): on the clustered m = 30 checkerboard the term-wise rounding model put on the exact coefficients (δh_{k,l} = u Σ_i ε_i ξ*_{i,l}(aξ*_p)_i on off-pattern entries) gave 10.3×, 4.6×, 3.2× the BJ loss at n = 16, 20, 24; on the equispaced control 0.5× and 0.5×. This estimate uses only exact data (c*, Ξ*) and random draws.
- Kill criterion written before testing (before `l1_r07_termwise_predictor.py` was written or run; 2026-10-31T22:38:55Z), on sets not used so far: checkerboards with clustering s|s| (quadratic, m = 30), s|s|³ (quartic, m = 30), s|s|² with m = 36, and Chebyshev–Lobatto nodes cos(πi/m), m = 30. Estimate E(n) = median over 3 seeds of the nonlinear long-double D(c* + term-wise model), BJ block CGS loss L(n), n ∈ {16, 20}:
  - on sets with L(20) ≥ 1e-13: survives iff 0.1 ≤ E(n)/L(n) ≤ 10 at both degrees on every such set; killed if some ratio is < 0.01 or > 100; otherwise inconclusive;
  - on sets with L(20) < 1e-13: survives iff E(20) < 1e-12; killed if E(20) ≥ 1e-11.
  The overall verdict is the worst over the sets (killed > inconclusive > survives).
  - Clarification added before the run: "not used so far" means not used in R06–R07; the Chebyshev–Lobatto checkerboard m = 30 was used in R04 for its BJ loss (flat at 3e-15, PD-T?…-112 (a)), so it is a known-flat control and enters through the L(20) < 1e-13 branch.

- **Pending correction PC-12 (R07, 2026-10-31T22:40:30Z; PD-T?…-112 (a), R04 §3 C1 wording, R06.md §1 before commit):** "weights 1.7e-33…0.47" for the cubic-clustered m = 30 checkerboard is the range of the x-factor weights (y-factor: 5.3e-35…0.48); the bivariate checkerboard weights span 1.8e-67…0.47. R06.md §1 was corrected in place before commit (it had copied the factor range as the bivariate range).

---

## IDEA?bivariate-lanczos-claude-120 — closed-loop dot-product rounding as the sole error source (R07)

Aliases: closed-loop term-wise model; dot-product-only rounding.

- Motivation (after IDEA-118/-119, R07.md): the open-loop estimate (term-wise noise on exact coefficients) over-estimates the loss by about 1×, 10×, 20–150× for quadratic, cubic, quartic clustering, and the BJ off-pattern values contain a feedback part φ that cancels the rounding part ρ. A closed-loop model keeps the feedback: run the BJ recurrence (block window, CGS) entirely in long double, but replace each computed coefficient h_{k,l} by its long-double inner product plus u Σ_i ε_i q_{i,l} u0_i (ε iid N(0,1), all window entries, u = 2^-52). Elementwise products, vector updates and norms then carry only long-double rounding.
- Kill criterion written before testing (before `l1_r07_closed_loop.py` was written or run; 2026-10-31T22:40:30Z). Checkerboards: cubic m = 30, equispaced m = 30, quadratic m = 30, quartic m = 30, cubic m = 36, Chebyshev–Lobatto m = 30. Closed-loop loss C(n) = median over 3 seeds of max|QᵀQ − I| (long double) at degree n; BJ double loss L(n); n ∈ {16, 20}:
  - sets with L(20) ≥ 1e-13: survives iff 0.2 ≤ C(n)/L(n) ≤ 5 at both degrees on every such set; killed if some ratio is < 0.02 or > 50; otherwise inconclusive;
  - sets with L(20) < 1e-13: survives iff C(20) < 1e-12; killed if C(20) ≥ 1e-11.
  The overall verdict is the worst over the sets.

---

## C01 — verification criteria for reconstruction 01 (reviews/L1-reconstruction-01.md), written 2026-10-31T23:02:34Z before `l1_c01_recon_checks.py` was written or run

These are checks of the reviewer's findings with my own code and seeds. They are not new candidates. u = 2^-53 (the plan's unit roundoff) is used in every Ritz prediction u/ρ; the R01 rule is also re-applied at 2^-52 for comparison.
- C01-1 (B2 (i)): the frozen R01 rule (τ = 10³u, factor-3 band) is re-applied to the R01 raw logs at u = 2^-53. The finding is confirmed iff K1 does not fire there.
- C01-1′ (B2 (ii)): with the chain-completion degree of tensor 41² (n = 40, where S_n contains every function of x) excluded, symmetric to the R01 N = M exclusion for Padua. The finding is confirmed iff, at both conventions, no run has a single section tagged 'over' while Z predicts or is uninformative.
- C01-2 (B1, selection): BJ-type recurrence (block window, one CGS pass, double), seed-11 sets of R02/R03 (M = 1681), parent rules dev (input code), mirror (HL BIT), alt (balanced: X-product for j < t/2, Y-product otherwise), adapt (per column the admissible product with the larger β/‖Aq_p‖). The finding is confirmed iff on at least two of {rotation 0.3, rotation π/4, triangle} the best of mirror/alt/adapt is ≥ 10³ below dev at n = 24 (the first degree where dev saturates at ≥ 0.1, if that is earlier).
- C01-3 (B1, truncation): dev rule, one CGS pass against all previous columns (no truncation). The finding is confirmed iff the loss at n = 24 is ≤ 1e-12 on rotation π/4 and on the disk, and ≥ 1e-6 at n = 20 on the triangle.
- C01-4 (major, support classifier): the finding is confirmed iff BJ loss at n = 24 is ≥ 100·u/ρ_Z on the seed-11 square with weights exp(8xy), and ≥ 10·u/ρ_Z on a Gaussian cloud (M = 1681, default_rng(12), standard normal coordinates).
- C01-5 (major, two-relation scope; l1_both_relations.both): the finding is confirmed iff the two-relation loss on tensor 41² at n = 24 is ≥ 10× BJ's, and on the triangle the one-pass loss is ≥ 1e-12 at n = 24 while the two-pass loss is below the one-pass loss.
- C01-6 (written 2026-10-31T23:09:22Z, before `l1_c01_u53_rerun.py` was written or run; prompted by the B2 convention finding and the orchestrator's instruction to use the plan's u = 2^-53). The R07 noise models (IDEA?…-118 H_term, IDEA?…-119, IDEA?…-120) used u = 2^-52 (the scripts' EPS) as the noise scale, which is twice the plan's unit roundoff. They are re-run unchanged except for the noise scale u = 2^-53, and the verdicts are re-evaluated by the same written rules. A verdict that changes between the two conventions is recorded as convention-sensitive, i.e. not decided at the resolution of the rule.

### C01 results (written 2026-10-31T23:10:52Z; logs `c01_rule_sensitivity.log`, `c01_recon_runs.log`, `c01_u53_rerun.log`)

Every reconstruction finding checked is confirmed with my own code and seeds:
- C01-1: K1 fires at 2^-52 and does not fire at 2^-53.
- C01-1′: with tensor n = 40 excluded, no single-section 'over' remains.
- C01-2: dev vs best other rule at n = 24 (n = 20 for the triangle): rotation 0.3, 5.8e-6 vs 2.9e-12; rotation π/4, 4.2e-3 vs 1.5e-8; triangle, 1.0 vs 1.6e-9.
- C01-3: no truncation, n = 24: rotation π/4 1.9e-14, disk 6.9e-15; the triangle is 1.0 at n = 20.
- C01-4: square with exp(8xy) weights, 1.6·10⁵ × u/ρ_Z at n = 24; Gaussian cloud, 2.4·10³ ×.
- C01-5: tensor two-relation vs BJ, 8.0e-13 vs 1.8e-14; triangle one pass 2.6e-10, two passes 1.4e-11.

C01-6 (R07 noise models at the plan's u = 2^-53). The verdicts change:
- IDEA?…-118 H_term: 5.1× / 2.3× → survives (inconclusive at 2^-52).
- IDEA?…-119 overall: inconclusive (quartic 60× / 11×; killed at 2^-52).
- IDEA?…-120 overall: inconclusive (quadratic 0.17 / 0.19; cubic m = 36 0.14 at n = 16; survives at 2^-52).

These three verdicts are therefore **convention-sensitive**, i.e. not decided at the resolution of the written rules. The N(0,1)·u noise model is itself a calibration choice: round-to-nearest relative errors have standard deviation ≈ u/√3. Corrected dispositions:
- IDEA?…-118: H_sign killed (unaffected); H_fb, H_rd inconclusive (unaffected); H_term convention-sensitive.
- IDEA?…-119: convention-sensitive (no longer "REJECTED: failed"). The over-estimate grows with the clustering strength at both conventions: about 0.5–1× quadratic, 2–13× cubic, 11–120× quartic at n = 16, 20.
- IDEA?…-120: convention-sensitive. Across both conventions, C/L lies in [0.14, 1.06] on the clustered sets for n = 16, 20; closed-loop dot-product rounding reproduces the order of magnitude, within a factor ≤ 8 below the loss.
