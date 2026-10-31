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
- Actual test results and committed evidence: see R01.md §3 and `logs/r01_*.log`.
- Disposition and precise rejected scope, if any: see R01.md.
- Topic / audit / history: created R01, 2026-10-31.

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
- Actual test results: R01.md §3.
- Topic / history: created R01, 2026-10-31.

## IDEA?bivariate-lanczos-claude-103 — exact coefficient pattern of the code's ordering (re-derivation)

Aliases: window lemma; exact-support window; HL BIT Thm 2.3 / BJ Thm 1 for the input ordering.

- Question / scope: [EXACT] which entries of H_F (full operator) and H_J (injecting operator) are nonzero, which are formed by the recurrence, which are implicit.
- Closest: HL BIT Thm 2.3 (LIT?…-106), BJ Thm 1 / Cor 3-4 (LIT?…-129/-130), HL SIMAX Thm 3.7 (LIT?…-116).
- Novelty gate verdict: duplicate (re-derivation for the campaign's ordering, kept as a checked dependency, no novelty).
- Cheapest decisive test: count check against the code's coefficients (structural zeros below 10⁻¹³ in a long-double run).
- Kill criterion: a nonzero coefficient outside the derived support in a reference run.
- Canonical theory ID: PD-T?bivariate-lanczos-claude-101 (`theory/window-coefficient-pattern-exact.md`).

## IDEA?bivariate-lanczos-claude-104 — [FP] local relations and the growing-block Paige identity for the full operator

Aliases: F-relations; "band Lanczos for F with injected J-vectors"; growing-block Paige identity.

- Question / scope: exact algebraic consequences of the [FP] local relations of the operator whose products of every vector are formed.
- Closest: block Paige identity (sinha-2026, abstract-level), Paige 1976/1980 (as reported), OBST-06.
- Separation criterion: the blocks grow by one per degree and one column per degree is injected by the other operator; the identity has a band-leak term determined by the window width (2n+1), not by a fixed block size. Falsified if the identity reduces to a fixed-block-size block-Lanczos identity after a change of basis (it cannot: the block sizes of S_n ⊖ S_{n−1} are n+1).
- Novelty gate verdict: variant with difference (of the block Paige identity); within documented search.
- Kill criterion: an algebraic error (identity residual not at rounding level in a numerical check).
- Canonical theory IDs: PD-T?bivariate-lanczos-claude-102 (`theory/fp-local-relations-window-recurrence.md`), PD-T?…-103 (`theory/full-operator-paige-identity-growing-blocks.md`).

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
