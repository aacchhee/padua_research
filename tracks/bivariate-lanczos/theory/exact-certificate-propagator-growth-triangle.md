# PD-T?bivariate-lanczos-claude-113 — Exact rational certificate: for the dev (BJ) rule the window-recurrence propagator grows exponentially on the triangle grid and stays polynomial on the square grid (degrees ≤ 12, computer-assisted; "exponentially" and "polynomial" describe the finite range only)

ID kind: PD-T.
Aliases: exact certificate; monic/orthonormal impulse identity; triangle-grid lower bound; rational propagator entries.
Split from: none.
Split into: none.

## Statement

1. **[EXACT] Impulse identity.** For the window recurrence of a positive discrete measure with monic polynomials ψ_k (BJ form: ψ_k = A_kψ_{p(k)} − Σ_{l∈W_k} α_{k,l}ψ_l), orthonormal vectors q_k = ψ_k/‖ψ_k‖ and exact propagator matrix L*(z) (PD-T?…-104 with exact coefficients), for every column s ≥ 1, every k ≥ s and every point z,
   ((L*(z))⁻¹)_{k,s}² = ‖ψ_{p(s)}‖² g_k(z)² / ‖ψ_k‖²,
   where g is the monic impulse response: g_l = 0 for l < s, g_s = 1, g_k = a_k(z) g_{p(k)} − Σ_{l∈W_k} α_{k,l} g_l (k > s). For integer nodes and integer weights every quantity on the right is rational. Under an affine change of coordinates z ↦ cz + d the entries scale by c⁻¹.
2. **[EXACT, computer-assisted; PROVED as a finite statement after the independent rerun of reconstruction 02] Certificate.** Let T_m = {(i, j) ∈ Z² : i, j ≥ 0, i + j ≤ m} and Q_m = {0, …, m}², equal weights, coordinates rescaled to [−1, 1] (factor c = 2/m), BJ ordering of the input code. With G(n) := max over impulse columns s of degree 2, columns **k > s** of degree n and nodes z_i of ((L*(z_i))⁻¹)_{k,s}² [corrected 2026-10-31T23:36Z, recon-02 M2 (i): the original read "columns k of degree n"; the checker uses k > s (`range(s + 1, N)`), which is why G(2) = 0 exactly on Q_24], exact rational computation gives
   - T_24 (M = 325): log10 G(n) = 0.446, 2.445, 3.874, 5.224, 6.525, 7.931, 9.360, 10.768, 12.172, 13.696, 15.211 for n = 2, …, 12; in particular G(12)/G(6) ≥ 10^{8.68}.
   - Q_24 (M = 625): log10 G(n) = −∞ (exactly 0), 1.102, 1.544, 1.836, 2.014, 2.166, 2.286, 2.379, 2.471, 2.591, 2.809 for n = 2, …, 12; G(12)/G(6) ≤ 10^{0.80}.
   The proved content is this exact finite statement: dev rule, degree-2 impulses, rescaled coordinates, n ≤ 12, the listed values, G(12) ≥ 10⁶·G(6) on T_24 and G(12) ≤ 10²·G(6) on Q_24. Both inequalities were decided in exact rational arithmetic by reconstruction 02. No asymptotic statement is made.
   So on T_24 single entries of the exact propagator exceed 10^{7.6} by degree 12 and grow by a factor ≥ 10^{4.3} between degrees 6 and 12 (squared: 10^{8.69}), whereas on the product grid Q_24 they stay below 10^{1.41} and grow by a factor ≤ 10^{0.40}.
3. **[EXACT, computer-assisted, descriptive extension — not pre-registered]** T_40 (M = 861, n ≤ 16): log10 G(n) rises by 1.35–1.50 per degree from n = 6 to 16 (20.90 at n = 16), within 0.2 of the T_24 values at common degrees; Q_40: 2.08 at n = 6, 3.09 at n = 16; the square grid Q_24 rotated by the rational rotation (cos, sin) = (3/5, 4/5) (nodes (3i − 4j, 4i + 3j), M = 625, n ≤ 14): log10 G rises from 4.49 (n = 6) to 13.95 (n = 14), 0.93–1.44 per degree (increasing).

## Definitions

‖·‖: ℓ² norm over the nodes with the given (integer) weights. Degree-2 impulses: s ∈ {(2,0), (2,1), (2,2)}.

## Assumptions

Part 1: positive weights, β_k > 0 (no breakdown), exact arithmetic. Part 2: the measures listed; U(12) holds for T_24 (principal lattice, unisolvent for Π_24) and for Q_24.

## Status by part

Overall status: PROVED (parts 1 and 2; part 2 as the exact finite dev-rule statement). Part 3 is PROVED for T_40 and the rotated Q_24, and CONDITIONAL for Q_40, which was not rerun. Updated 2026-10-31T23:36Z after reconstruction 02. Before that, part 2 was CONDITIONAL, awaiting the independent rerun.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. impulse identity | PROVED | proof below |
| 2. certificate on T_24, Q_24 | PROVED (finite, dev rule). The independent rerun was done by recon-02 `rv2_certificate.py`, two ways: (A) full exact Gram–Schmidt with off-window coefficients checked exactly 0; (B) exact LDLᵀ of the moment matrix. Identical values and maximisers; criterion decided exactly; logs `reviews/logs_L1b/cert_{T24,Q24}*.log`. Before recon-02: CONDITIONAL. | exact Fraction arithmetic; built-in exact check that all 4095 pairwise inner products of the computed monic basis vanish; `logs/r05_certificate_{triangle,square}.log` |
| 3. T_40, Q_40, rotated Q_24 | T_40 and rotated Q_24: PROVED (reproduced exactly by recon-02, `cert_T40.log`, `cert_rotQ24.log`). Q_40: CONDITIONAL (not rerun). Descriptive, not pre-registered. | `logs/r05_certificate_more.log` |

## Depends on

PD-T?…-101 (graded basis; uniqueness of the graded Gram–Schmidt basis), PD-T?…-104 (node propagator).

## Checks

Checker: `tracks/bivariate-lanczos/code/L1/l1_r05_exact_certificate.py` (`python3 -I l1_r05_exact_certificate.py triangle 24 12 2`, `... square 24 12 2`; 8.6 s and 12.6 s) and `l1_r05_exact_more.py` (T_40, Q_40, rotated Q_24; ≈ 4 min). Trusted dependencies: CPython `fractions` (exact rationals), the ordering/window tables of `l1_recurrence.py`. Reduction: part 1 (proved) reduces the propagator entries to rational expressions computed exactly; the exact orthogonality check certifies that the computed ψ_k are the monic orthogonal polynomials of the measure (the graded Gram–Schmidt basis is unique and the window recurrence produces the correct leading terms by construction). Independent rerun: **done** by reconstruction 02 (`tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py`). It works from the statement only, with its own tables; trusted dependencies are CPython `fractions` and big integers; part 1 was cross-checked in mpmath at 60 digits (relative deviation ≤ 1.9e-56).

## Sources

None needed for the statement. Context (not dependencies): Barrio–Peña–Sauer 2010 (LIT?…-301–303) analyse evaluation recurrences for monic multivariate OPs as triangular substitution with forward bounds through the inverse of a comparison matrix (eqs. (18)–(20)); this file certifies sizes of the inverse of the corresponding triangular matrix of the window recurrence itself on explicit measures.

## Proof or evidence

*1.* Write ψ_k = A_kψ_p − Σ α_lψ_l. Dividing by ‖ψ_p‖ gives β_k q_k = A_k q_p − Σ h_l q_l with β_k = ‖ψ_k‖/‖ψ_p‖ and h_l = α_l‖ψ_l‖/‖ψ_p‖ — exactly the coefficients of L*(z) (rows of PD-T?…-104 with exact coefficients). The column s of L*(z)⁻¹ is the solution γ of β_kγ_k = a_k(z)γ_{p(k)} − Σ h_lγ_l (k > s), γ_l = 0 (l < s), β_sγ_s = 1 (unit forcing at s, sign convention immaterial for squares). Put γ_k = C g_k/‖ψ_k‖. Then β_kγ_k = C g_k/‖ψ_p‖ and a_kγ_p − Σ h_lγ_l = (C/‖ψ_p‖)(a_k g_p − Σ α_l g_l) = C g_k/‖ψ_p‖, so γ satisfies the recurrence for k > s; at k = s, γ_s = C/‖ψ_s‖ must equal 1/β_s = ‖ψ_{p(s)}‖/‖ψ_s‖, so C = ‖ψ_{p(s)}‖. Squaring gives the identity. Rationality: integer nodes and weights make ψ_k(z_i), α, ‖ψ‖² and g_k(z_i) rational. Scaling: under z ↦ cz + d, β and h scale by c and a_k(z) − h_{k,p(k)} by c, so the homogeneous recurrence is invariant and the unit forcing contributes c⁻¹.
*2–3.* Exact computation (see Checks).

## Scope

A finite-range, exact statement about the **exact** propagator (amplification capacity of the recurrence for a single local error), not about floating-point loss for a particular rounding pattern; it certifies the a priori nature of the non-product amplification (PD-T?…-109 (a)) on an explicit rational measure, and the product-type contrast (PD-T?…-105) on the square grid, where the within-degree responses vanish exactly (G(2) = 0). It is not an asymptotic theorem (no statement for n → ∞).

## Open items

Asymptotic growth rate for the triangle (and its independence of m suggested by T_24/T_40); independent rerun; an analytic lower bound.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R05).
- 2026-10-31T23:05Z (re-check after reconstruction 01):
  - Scope (B1): the certificate and the impulse identity are for the dev (BJ input-code) selection, whose monic form is the BJ recurrence. The certified contrast "exponential on T_24, polynomial on Q_24" is a dev-rule statement. Recon-01's `prop_selection.log` shows the exact propagator on a random triangle is selection-dependent: u·max‖L*⁻¹‖ at n = 20 is 1.2 (dev) and 3.4e-8 (adapt), though still far above the square.
  - "Exponential" in the title is a finite-range description (log₁₀G increments over degrees 6–12); recon-01 measured the double loss to be convex in n, so no fixed rate is presupposed.
  - Part 2 remains CONDITIONAL on the independent rerun.
- 2026-10-31T23:36Z (response to reconstruction 02, M2):
  - G(n) definition corrected to k > s.
  - The finite exact statement is made explicit.
  - Part 2 is upgraded CONDITIONAL → PROVED, citing recon-02's independent two-way exact rerun. Part 3 is PROVED except Q_40.
  - The title gains "dev (BJ) rule" and a finite-range gloss. Original title: "Exact rational certificate: the window-recurrence propagator grows exponentially on the triangle grid and stays polynomial on the square grid (degrees ≤ 12, computer-assisted)".
