# PD-T?bivariate-lanczos-claude-113 — Exact rational certificate: for the dev (BJ) rule the window-recurrence propagator grows exponentially on the triangle grid and stays polynomial on the square grid (degrees ≤ 12, computer-assisted; "exponentially" and "polynomial" describe the finite range only)

Final ID: **PD-T041** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: exact certificate; monic/orthonormal impulse identity; triangle-grid lower bound; rational propagator entries.
Split from: none.
Split into: none.

## Statement

1. **[EXACT] Impulse identity.** For the window recurrence of a positive discrete measure with monic polynomials ψ_k (BJ form: ψ_k = A_kψ_{p(k)} − Σ_{l∈W_k} α_{k,l}ψ_l), orthonormal vectors q_k = ψ_k/‖ψ_k‖ and exact propagator matrix L*(z) (PD-T?…-104 with exact coefficients), for every column s ≥ 1, every k ≥ s and every point z,
   ((L*(z))⁻¹)_{k,s}² = ‖ψ_{p(s)}‖² g_k(z)² / ‖ψ_k‖²,
   where g is the monic impulse response: g_l = 0 for l < s, g_s = 1, g_k = a_k(z) g_{p(k)} − Σ_{l∈W_k} α_{k,l} g_l (k > s). For integer nodes and integer weights every quantity on the right is rational. Under an affine change of coordinates z ↦ cz + d with a scalar c ≠ 0 (the same factor for both coordinates) and d ∈ R², with the weights unchanged, the graded order, the parent rule and the windows are unchanged. The propagator L*′ of the transformed measure satisfies ((L*′(cz + d))⁻¹)_{k,s} = sign(c)^{deg k − deg s}|c|⁻¹((L*(z))⁻¹)_{k,s} for s ≥ 1, k ≥ s. So the entries scale by c⁻¹ for c > 0, which is the case used by the certificate rescalings (c = 2/m), and the squared entries scale by c⁻² for every c ≠ 0. [Corrected 2026-11-01T08:33:59+01:00, Codex audit-01 LL-L1. It read "Under an affine change of coordinates z ↦ cz + d the entries scale by c⁻¹", which is false for c < 0 under the positive-pivot normalisation.]
2. **[EXACT, computer-assisted; PROVED as a finite statement after the independent rerun of reconstruction 02] Certificate.** Let T_m = {(i, j) ∈ Z² : i, j ≥ 0, i + j ≤ m} and Q_m = {0, …, m}², equal weights, coordinates rescaled to [−1, 1] (factor c = 2/m), BJ ordering of the input code. With G(n) := max over impulse columns s of degree 2, columns **k > s** of degree n and nodes z_i of ((L*(z_i))⁻¹)_{k,s}² [corrected 2026-10-31T23:36Z, recon-02 M2 (i): the original read "columns k of degree n"; the checker uses k > s (`range(s + 1, N)`), which is why G(2) = 0 exactly on Q_24], exact rational computation gives
   - T_24 (M = 325): log10 G(n) = 0.446, 2.445, 3.874, 5.224, 6.525, 7.931, 9.360, 10.768, 12.172, 13.696, 15.211 for n = 2, …, 12; in particular G(12)/G(6) ≥ 10^{8.68}.
   - Q_24 (M = 625): log10 G(n) = −∞ (exactly 0), 1.102, 1.544, 1.836, 2.014, 2.166, 2.286, 2.379, 2.471, 2.591, 2.809 for n = 2, …, 12; G(12)/G(6) ≤ 10^{0.80}.
   The proved content is this exact finite statement: dev rule, degree-2 impulses, rescaled coordinates, n ≤ 12, the listed values, G(12) ≥ 10⁶·G(6) on T_24 and G(12) ≤ 10²·G(6) on Q_24. Both inequalities were decided in exact rational arithmetic by reconstruction 02. No asymptotic statement is made.
   So on T_24 single entries of the exact propagator exceed 10^{7.6} by degree 12 and grow by a factor ≥ 10^{4.3} between degrees 6 and 12 (squared: 10^{8.69}), whereas on the product grid Q_24 they stay below 10^{1.41} and grow by a factor ≤ 10^{0.40}.
3. **[EXACT, computer-assisted, descriptive extension — not pre-registered; PROVED as a finite statement for all three measures since 2026-11-01T08:33:59+01:00]** T_40 (M = 861, n ≤ 16): log10 G(n) rises by 1.35–1.50 per degree from n = 6 to 16 (20.90 at n = 16), within 0.2 of the T_24 values at common degrees; Q_40: 2.08 at n = 6, 3.09 at n = 16; the square grid Q_24 rotated by the rational rotation (cos, sin) = (3/5, 4/5) (nodes (3i − 4j, 4i + 3j), M = 625, n ≤ 14): log10 G rises from 4.49 (n = 6) to 13.95 (n = 14), 0.93–1.44 per degree (increasing).

## Definitions

‖·‖: ℓ² norm over the nodes with the given (integer) weights. Degree-2 impulses: s ∈ {(2,0), (2,1), (2,2)}.

## Assumptions

Part 1: positive weights, β_k > 0 (no breakdown), exact arithmetic. Part 2: the measures listed; U(12) holds for T_24 (principal lattice, unisolvent for Π_24) and for Q_24.

## Status by part

Overall status: PROVED (parts 1–3; parts 2 and 3 as exact finite dev-rule statements). Updated 2026-11-01T08:33:59+01:00: the Q_40 obligation of part 3 is discharged by the fresh independent exact rerun in Codex audit-01 (Checks). Before that, part 3 was PROVED for T_40 and the rotated Q_24 and CONDITIONAL for Q_40. Updated 2026-10-31T23:36Z after reconstruction 02; before that, part 2 was CONDITIONAL, awaiting the independent rerun.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. impulse identity | PROVED | proof below |
| 2. certificate on T_24, Q_24 | PROVED (finite, dev rule). The independent rerun was done by recon-02 `rv2_certificate.py`, two ways: (A) full exact Gram–Schmidt with off-window coefficients checked exactly 0; (B) exact LDLᵀ of the moment matrix. Identical values and maximisers; criterion decided exactly; logs `reviews/logs_L1b/cert_{T24,Q24}*.log`. Before recon-02: CONDITIONAL. | exact Fraction arithmetic; built-in exact check that all 4095 pairwise inner products of the computed monic basis vanish; `logs/r05_certificate_{triangle,square}.log` |
| 3. T_40, Q_40, rotated Q_24 | PROVED (finite). T_40 and rotated Q_24: reproduced exactly by recon-02 (`cert_T40.log`, `cert_rotQ24.log`). Q_40: reproduced exactly by Codex audit-01 (`audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`); CONDITIONAL (not rerun) before 2026-11-01T08:33:59+01:00. Descriptive, not pre-registered. | `logs/r05_certificate_more.log` |

## Depends on

PD-T?…-101 (graded basis; uniqueness of the graded Gram–Schmidt basis), PD-T?…-104 (node propagator).

## Checks

Checker: `tracks/bivariate-lanczos/code/L1/l1_r05_exact_certificate.py` (`python3 -I l1_r05_exact_certificate.py triangle 24 12 2`, `... square 24 12 2`; 8.6 s and 12.6 s) and `l1_r05_exact_more.py` (T_40, Q_40, rotated Q_24; ≈ 4 min). Trusted dependencies: CPython `fractions` (exact rationals), the ordering/window tables of `l1_recurrence.py`. Reduction: part 1 (proved) reduces the propagator entries to rational expressions computed exactly; the exact orthogonality check certifies that the computed ψ_k are the monic orthogonal polynomials of the measure (the graded Gram–Schmidt basis is unique and the window recurrence produces the correct leading terms by construction). Independent rerun: **done** by reconstruction 02 (`tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py`). It works from the statement only, with its own tables; trusted dependencies are CPython `fractions` and big integers; part 1 was cross-checked in mpmath at 60 digits (relative deviation ≤ 1.9e-56).
Independent rerun of the Q_40 extension (added 2026-11-01T08:33:59+01:00):
- Executed by Codex audit-01 (L1-later): `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I -u tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 40 16`, Python 3.12.14, 48.1 s.
- Log: `topics/bivariate-lanczos-20261031/audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`. Provenance and command are also in `audit-01/L1-later/manifest.json` (executions[2]).
- Method A: full exact Gram–Schmidt with the dev products. No coefficient is nonzero outside the exact window, and none of the 11628 off-diagonal inner products is nonzero.
- The checker's second method (moment-matrix LDLᵀ) was omitted at this size. The reduction above needs only the exact orthogonality check.
- Values: log10 G(6) = 2.080 and log10 G(16) = 3.088, matching the stated 2.08 and 3.09. The values at every n = 2…16 match the developer's `logs/r05_certificate_more.log` to its two printed decimals.
- The checker computes G in integer coordinates and adds 2 log10(m/2), i.e. it uses the scaling of part 1 with c = 2/m > 0.
- The decimal values are floating-point log10 of exact rational numerators and denominators (trusted: CPython `math.log10` on integers). Their error is far below the 0.005 and 0.003 distances of the two quoted Q_40 values from the 2-decimal rounding boundaries.
- The same audit freshly reran T_24 and Q_24 (`cert_triangle_rerun.log`, sha256 `b328c93fccdccf009a3c48d07c5df0a19adc4f60eeb97a4db0085f774b65c95d`; `cert_square_rerun.log`, sha256 `8606323c1890a4eea9d8c3528f9b40adada016130e3729e1fa4be367ed374f5a`), both ways, and confirmed part 2. T_40 and the rotated Q_24 were not freshly rerun there (recon-02 reproduced them).
- Developer check of the corrected scaling sentence of part 1 (exact squares and signs for c = −2, −1/3, 3/2 on T_6, n ≤ 4, plus a 50-digit check of the signed entries): `tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py`, log `topics/bivariate-lanczos-20261031/directions/L1/logs/a01_exact_checks.log`.

## Sources

None needed for the statement. Context (not dependencies): Barrio–Peña–Sauer 2010 (LIT?…-301–303) analyse evaluation recurrences for monic multivariate OPs as triangular substitution with forward bounds through the inverse of a comparison matrix (eqs. (18)–(20)); this file certifies sizes of the inverse of the corresponding triangular matrix of the window recurrence itself on explicit measures.

## Proof or evidence

*1.* Write ψ_k = A_kψ_p − Σ α_lψ_l. Dividing by ‖ψ_p‖ gives β_k q_k = A_k q_p − Σ h_l q_l with β_k = ‖ψ_k‖/‖ψ_p‖ and h_l = α_l‖ψ_l‖/‖ψ_p‖ — exactly the coefficients of L*(z) (rows of PD-T?…-104 with exact coefficients). The column s of L*(z)⁻¹ is the solution γ of β_kγ_k = a_k(z)γ_{p(k)} − Σ h_lγ_l (k > s), γ_l = 0 (l < s), β_sγ_s = 1 (unit forcing at s, sign convention immaterial for squares). Put γ_k = C g_k/‖ψ_k‖. Then β_kγ_k = C g_k/‖ψ_p‖ and a_kγ_p − Σ h_lγ_l = (C/‖ψ_p‖)(a_k g_p − Σ α_l g_l) = C g_k/‖ψ_p‖, so γ satisfies the recurrence for k > s; at k = s, γ_s = C/‖ψ_s‖ must equal 1/β_s = ‖ψ_{p(s)}‖/‖ψ_s‖, so C = ‖ψ_{p(s)}‖. Squaring gives the identity. Rationality: integer nodes and weights make ψ_k(z_i), α, ‖ψ‖² and g_k(z_i) rational.
*Scaling* (corrected 2026-11-01T08:33:59+01:00, LL-L1). Let σ = sign(c) and z′ = cz + d, with the same weights.
- For a column k of degree t_k, ψ′_k(z′) := c^{t_k}ψ_k((z′ − d)/c) has leading monomial lm(k) with coefficient 1 and otherwise only earlier monomials, because the substitution maps Π_t onto Π_t and acts on the top-degree part by c^{−t}.
- ⟨ψ′_k, ψ′_r⟩′ = c^{t_k+t_r}⟨ψ_k, ψ_r⟩ = 0 for k ≠ r. By uniqueness of the graded monic orthogonal basis, ψ′_k is that basis for the transformed measure, with ‖ψ′_k‖ = |c|^{t_k}‖ψ_k‖. Hence q′_k = σ^{t_k}q_k as node vectors.
- With A′ = cA + d_A I and t_k = t_{p(k)} + 1: β′_k = σ^{t_k+t_p}cβ_k = |c|β_k. For l ∈ W_k \ {p}, h′_{k,l} = σ^{t_l+t_p}c h_{k,l} = σ^{t_k+t_l}|c|h_{k,l}. Finally h′_{k,p} − a′_k(z′) = c(h_{k,p} − a_k(z)) = σ^{t_k+t_p}|c|(h_{k,p} − a_k(z)). Zero coefficients stay zero, so the window pattern is unchanged.
- Thus L*′(z′) = S D L*(z) D with D = diag(σ^{t_k}) and S = diag(1, |c|, …, |c|) (row 0 is e_0ᵀ in both). Then (L*′(z′))⁻¹ = D(L*(z))⁻¹DS⁻¹, and its (k, s) entry for s ≥ 1 is σ^{t_k+t_s}|c|⁻¹((L*(z))⁻¹)_{k,s} = σ^{t_k−t_s}|c|⁻¹((L*(z))⁻¹)_{k,s}.
- The original argument ("β and h scale by c") holds for c > 0 only. For c < 0, β scales by |c| and the basis vectors change sign by σ^{t_k}.
*2–3.* Exact computation (see Checks).

## Scope

A finite-range, exact statement about the **exact** propagator (amplification capacity of the recurrence for a single local error), not about floating-point loss for a particular rounding pattern; it certifies the a priori nature of the non-product amplification (PD-T?…-109 (a)) on an explicit rational measure, and the product-type contrast (PD-T?…-105) on the square grid, where the within-degree responses vanish exactly (G(2) = 0). It is not an asymptotic theorem (no statement for n → ∞).

## Open items

Asymptotic growth rate for the triangle (and its independence of m suggested by T_24/T_40); an analytic lower bound. ["independent rerun" removed 2026-11-01T08:33:59+01:00: done for parts 2–3, by recon-02 and, for Q_40, by Codex audit-01.]

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
- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later LL-L1 and the T113 status note under LL-M2; branch head 5f52331).
  - Q_40 status: CONDITIONAL → PROVED (finite). The written proof is unchanged: the reduction by part 1 and the exact orthogonality check. The only missing obligation was an independent rerun of the Q_40 extension. Codex audit-01 executed it with the independent checker `review_L1b/rv2_certificate.py` (log `audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`), with exact orthogonality and reproduced values; details in Checks. Part 3 is now PROVED for all three measures as a finite descriptive statement. This upgrade rests on the audit's executed evidence, not on new developer reasoning. Original status line: "Overall status: PROVED (parts 1 and 2; part 2 as the exact finite dev-rule statement). Part 3 is PROVED for T_40 and the rotated Q_24, and CONDITIONAL for Q_40, which was not rerun. Updated 2026-10-31T23:36Z after reconstruction 02. Before that, part 2 was CONDITIONAL, awaiting the independent rerun." Original table row 3: "T_40 and rotated Q_24: PROVED (reproduced exactly by recon-02, `cert_T40.log`, `cert_rotQ24.log`). Q_40: CONDITIONAL (not rerun). Descriptive, not pre-registered."
  - LL-L1: the affine-scaling sentence of part 1 is restricted and corrected: entries scale by c⁻¹ for c > 0, and by sign(c)^{deg k − deg s}|c|⁻¹ for c ≠ 0, so squared entries scale by c⁻² for every c ≠ 0. A corrected proof replaces the scaling sentence of the proof (original wording quoted there). The impulse identity and the finite certificate are unaffected, because all certificate rescalings use c = 2/m > 0. Checked exactly in `directions/L1/logs/a01_exact_checks.log`.
  - Stale open item "independent rerun" removed.
