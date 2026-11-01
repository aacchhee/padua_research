# PD-N?programme-ideas-claude-04 — The commutant of H_x inside the generalized-Hessenberg pattern of H_y is not always span{I, H_x, H_y}

Final ID: **PD-N042** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: refutation of "the 3-dimensional commutant is the affine-triangular group" (M2 adversary (ii)(2)); Padua n = 2 commutant of dimension 6; audit-01 A3 counterexample.
Split from: the commutant clause of the combined `report.md` row on finite Favard at `614709d`; the retained Favard statement is `PD-T?programme-ideas-claude-01`.
Split into: none.

## Statement

Let 𝒞_y(H) := {E real symmetric N × N supported on pattern(H_y), [H_x, E] = 0}, with pattern(H_y) = {(i, j) : i ≤ π_y(j) and j ≤ π_y(i)} for the graded order 1; x, y; x², xy, y²; … (π_y(j) the index of y·m_j; no constraint if deg m_j = n) as in `checks/code/adv/M2/m2_common.py`. For the exact degree-2 Padua section pair (Padua points x = cos(jπ/2), y = cos(kπ/3), j + k even, with their cubature weights 1/12, 1/6, 1/3, 1/6, 1/12, 1/6, built by weighted Gram–Schmidt with positive leading coefficients), pattern(H_y) admits 17 symmetric variables, the linear map E ↦ [H_x, E] on them has rank 11, and dim 𝒞_y(H) = 6 > 3 = dim span{I, H_x, H_y}. Hence the statement "for commuting positive-pivot pattern pairs, 𝒞_y(H) = span{I, H_x, H_y}" is false.

## Definitions

As above and in PD-T?programme-ideas-claude-01.

## Assumptions

Exact arithmetic; the pattern convention above.

## Status by part

Overall status: PROVED (exact finite computation).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| dim 𝒞_y(H) = 6 for Padua n = 2 | PROVED (exact computation) | `checks/code/response-02/padua_pattern_commutant.py/.out`: det V = −27/2, exact commutation, all pivots positive (√2/2, …, 1/2), no pattern violation, 17 variables, rank 11; independently computed by the Codex audit (`audit-support/obstructions-check.py/.json`) |
| larger Padua degrees | MEASURED (audit, floating point) | dimensions 6, 8, 9, 11, 12, 14 for Padua n = 2..7 (`audit-support/obstructions-report.md` O1) |
| random nodes/weights give dimension 3 | MEASURED (developer) | `checks/code/adv/M2/m2_favard_commutant.py`, n = 3..6; kept as an observation with IDEA?programme-ideas-claude-08 |

Candidate / claim disposition: the side claim "the pattern commutant is span{I, H_x, H_y} (the affine-triangular group)" (`checks/adversarial-M2.md` (ii)(2), placed under a P label in `report.md` at `614709d`) is REJECTED.
Rejection reason: refuted (an explicit positive-pivot commuting pattern pair with a six-dimensional pattern commutant).

## Negative-result scope (PD-N only)

Attempted mechanism: identifying the pattern commutant with the affine substitutions y ↦ a + bx + cy as a structural theorem for all commuting positive-pivot pattern pairs (IDEA?programme-ideas-claude-08).
Parameter range: the stated pattern convention; the counterexample is Padua n = 2. The universal claim remains refuted. Generic node sets are covered separately by PD-T102 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`): for every n≥2, distinct x coordinates imply the three-dimensional commutant, and this condition holds outside a proper real-algebraic subset. The structure on repeated-x strata is not classified.

## Depends on

PD-T?programme-ideas-claude-01 (definitions only). Complementary comparison, not a dependency of this negative proof: PD-T102 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`) proves the all-degree generic equality under distinct x coordinates.

## Checks

`python -I checks/code/response-02/padua_pattern_commutant.py > checks/code/response-02/padua_pattern_commutant.out` (SymPy 1.14.0, exact; ≈ 1 min).

## Sources

None.

## Proof or evidence

Exact computation as tabulated: the 6 × 6 pair is computed in closed form (rationals and √2, √3 from the Gram–Schmidt normalisation); the commutator map's 36 × 17 coefficient matrix is formed symbolically and its rank computed exactly.

## Scope

A single explicit counterexample suffices for the refutation. The extra commutant directions are presumably produced by the symmetries of the Padua points; this is not analysed.

## Open items

Genericity of dimension 3 is PROVED for every n≥2 by the split-off PD-T102. Description of the commutant on repeated-x strata, including Padua sets, remains OPEN. The exact Padua n=2 counterexample in this record is unchanged.

## History

- 2026-11-01, M2 adversarial agent (claude-fable-5-1, max): observation on random instances stated as the "affine-triangular group".
- 2026-11-01, Codex audit-01 A3 / O1: exact Padua n = 2 counterexample.
- 2026-11-01, response-01 (claude-opus-5-5): relabelled MEASURED on random instances.
- 2026-11-01, response-01 addendum (claude-opus-5-5), at AC's instruction "register negative results": registered as this PD-N with an independent developer script.

- 2026-11-01, Codex PR #9 finalization (gpt-6.1-sol medium), Claude audit-01 ACCEPTED: PD-T102 closes B5 under its distinct-x hypothesis, as a positive generic complement only. The universal counterexample and its proof are unchanged.
