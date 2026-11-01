# PD-N?programme-ideas-claude-01 — The symmetrised-product inertia box count can fail at square-root commutator scale for symmetric pairs

Final ID: **PD-N039** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N.
Aliases: √δ cluster counterexample (gen2-3 adversary); half-integer box count; "n_box = ½(n₊(S) − N + n₊(M_x) + n₊(M_y))" failure.
Split from: `checks/adversarial-gen2-3.md` (iii) and its salvage bullet at `614709d` ("no δ-only certificate for computed sections beyond √δ"). The broad computed-section claim is withdrawn (audit-01 A5); this record holds only the restricted method failure.
Split into: PD-N072, PD-N073, PD-T193 (PR12, exact scoped splits; original status/history retained).

## Statement

For a pair of real symmetric N × N matrices (H_x, H_y) and an open box (a, a′) × (b, b′), the *symmetrised-product count* is

  n_box := ½ (n₊(S) − N + n₊(M_x) + n₊(M_y)),  M_x = (H_x − aI)(a′I − H_x),  M_y = (H_y − bI)(b′I − H_y),  S = ½(M_xM_y + M_yM_x),

where n₊ counts positive eigenvalues (`checks/code/adv/gen2-3/pairs.py`: `box_matrices`, `box_count_numerator`). For commuting pairs with no eigenvalue of H_x in {a, a′} and none of H_y in {b, b′} it equals the number of joint eigenvalues in the box (proof below).

**Claim (PROVED).** For every e with 0 < e < (8 − 2√2)/11 ≈ 0.470, the 2 × 2 pair H_x = diag(0, e), H_y = R diag(0, e) Rᵀ (R the rotation by 45°) and the box (−e/10, 1)² give n_box = 3/2, whereas every commuting symmetric pair (H′_x, H′_y) with spec H′_x = spec H_x and spec H′_y = spec H_y has exactly 2 joint eigenvalues in the box. Here ‖[H_x, H_y]‖₂ = δ := e²/2, and the box boundary is at distance e/10 = √(2δ)/10 from both marginal spectra. Hence no inequality of the form "n_box is correct whenever the boundary distance exceeds C·δ^α" can hold with α > ½ on the class of all symmetric pairs.

## Definitions

Joint eigenvalues of a commuting symmetric pair: the pairs of eigenvalues of a common orthonormal eigenbasis.

## Assumptions

Exact arithmetic; real symmetric pairs; the formula exactly as defined above.

## Status by part

Overall status: PROVED (explicit two-node family).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| n_box is the box count for exactly commuting pairs | PROVED (routine) | proof below |
| n_box = 3/2 on the two-node family | PROVED | proof below; exact SymPy check `checks/code/response-01/inertia_two_node_family.py/.out` (symbolic det S and five rational e); independently reconstructed by the Codex audit (`audit-support/obstructions-check.py`, e ≤ 1/10) |
| failures at √δ scale on larger symmetric banded pairs | MEASURED (supporting, restricted) | `checks/code/adv/gen2-3/t3_delta_exponent.py`, `t3b_diagnose.py`: N = 45 rotated-cluster pairs (rotation of an eigenbasis; the recurrence pattern is generally not preserved) and an N = 38 symmetric block-tridiagonal direct sum with a 2 × 2 cluster (reducible, constant vector not cyclic, N ≠ dim Π_n); wrong half-integer counts at boundary distance ≈ 0.24–0.28 √δ, δ from 5e-5 to 5e-9 (e.g. N = 38, δ = 5e-7, distance 2e-4: numerator 7 instead of 8) |

Candidate / claim disposition: the mechanism "δ-robust symmetrised-product inertia count" (gen2-draft-3 sub-problem 3, IDEA?programme-ideas-claude-09) is REJECTED.
Rejection reason: failed — the mechanism does not achieve a δ-tolerance better than √δ on symmetric pairs, by the explicit family above.

## Negative-result scope (PD-N only)

Attempted mechanism: the symmetrised-product count n_box above as a certificate for nearly commuting pairs (IDEA?programme-ideas-claude-09, gen2-draft-3 sub-problem 3).
Parameter range: real symmetric pairs; the two-node family for the proof; symmetric banded pairs of sizes 38 and 45 for the measurements. **Not covered:** pairs produced by the positive-pivot bivariate recurrence (computed sections of size dim Π_n with a cyclic constant vector); other count objects (in the developer's own failing cases restricted-subspace and degree-2 disc/singular-value counts stayed correct); certificates that use information other than δ.

## Depends on

None.

## Checks

`python -I checks/code/response-01/inertia_two_node_family.py > checks/code/response-01/inertia_two_node_family.out` (SymPy 1.14.0, Python 3.12; this commit). Measured supporting runs frozen at `614709d` (`checks/code/adv/gen2-3/`), replayed by the audit (`audit-support/obstructions-check.json`).

## Sources

LITERATURE context for the √δ scale (not used in the proof): Kachkovskiy–Safarov (1.3); Cerjan–Loring–Vides, J. Math. Phys. 64 (2023) 023501, Prop. II.4 (coverage as recorded in `checks/adversarial-gen2-3.md`).

## Proof or evidence

*Commuting case.* If [H_x, H_y] = 0, then M_x, M_y and S = M_xM_y are simultaneously diagonal in a joint eigenbasis, with diagonal entries m_x(i) = (ξ_i − a)(a′ − ξ_i), m_y(i) = (η_i − b)(b′ − η_i), nonzero by assumption; m_x(i) > 0 iff ξ_i ∈ (a, a′), and likewise for y. With p, q, r, s the numbers of joint eigenvalues with signs (+,+), (+,−), (−,+), (−,−): n₊(S) = p + s, N = p + q + r + s, n₊(M_x) = p + q, n₊(M_y) = p + r, so n_box = ½(p + s − p − q − r − s + p + q + p + r) = p. ∎

*Two-node family.* M_x = diag(a, b) with a = (e/10)(1) = e/10 and b = (e + e/10)(1 − e) = 11e(1 − e)/10; M_y = R diag(a, b) Rᵀ. Both are positive definite for 0 < e < 1, so n₊(M_x) = n₊(M_y) = 2. With R the 45° rotation, a direct computation gives

  det S = −(a + b)² (a² − 6ab + b²)/16 = −e⁴ (11e − 12)² (121e² − 176e + 56)/160000,  tr S = e² (11e − 12)²/200 > 0.

The quadratic 121e² − 176e + 56 has roots (8 ∓ 2√2)/11, so it is positive for 0 < e < (8 − 2√2)/11, hence det S < 0 there; S is 2 × 2, so it has one positive and one negative eigenvalue, n₊(S) = 1 and n_box = ½(1 − 2 + 2 + 2) = 3/2. Any commuting symmetric pair with the same marginal spectra {0, e} has its two joint eigenvalues in {0, e}², which lies inside (−e/10, 1)². Finally [H_x, H_y] = (e²/2)[[0, 1], [−1, 0]], so ‖[H_x, H_y]‖₂ = e²/2. ∎

## Scope

Exactly the formula and pair class stated. This is a scoped method failure, not an impossibility theorem for δ-only certificates on computed sections.

## Open items

Whether a δ-tolerant count with α > ½ exists on the class of positive-pivot computed sections (cyclic, size dim Π_n) is not addressed: `OPEN_TARGETS.md` B3. Transfer to the Lanczos topic (LZ-034 / L3) only in this restricted form.

Dated separate extension after accepted Part2 Claude audit-01: the scope left unresolved by PD-N039's historical statement above is resolved for the specified symmetrised-product S(α) by PROVED PD-N072. The specified count has disposition REJECTED: refuted at fixed n = 1, p = 1/10, M = 4 for all 0 < t ≤ 10^−6, with computed gap ≥ √δ/10 and n_box = 1/2 versus valid reference count 1. This does not broaden the original PD-N039 theorem retrospectively or relabel its old measurements as section certificates. Other count objects S_F, other degrees and reference-existence questions remain OPEN. The complete proof and exact evidence are in the Part2 topic; the distinct route obstruction is PD-N073, supported by PD-T193.

## History

- 2026-11-01, gen2-3 adversarial agent (claude-fable-5-1, xhigh): cluster counterexamples, fitted slopes 0.52–0.55, broad salvage wording "no δ-only certificate for computed sections beyond √δ".
- 2026-11-01, Codex audit-01 A5 / obstructions O3: restrict to the formula and the explicit class; exact two-node reconstruction.
- 2026-11-01, response-01 addendum: commuting-case proof added; registered in `PROOF_STATUS.md` and `state/IDEAS.md` (provisional ID) at AC's instruction "register negative results".
- 2026-11-01, response-01 (claude-opus-5-5, effort not exposed): this record, with the developer's own exact derivation (range extended to e < (8 − 2√2)/11) and script; broad wording struck in the sources.
