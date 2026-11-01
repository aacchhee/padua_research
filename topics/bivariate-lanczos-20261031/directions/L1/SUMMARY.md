# L1 (+L4) — Direction summary after R07, corrected after reconstructions 01 and 02 (2026-10-31)

> Orchestrator note (kept): saved by the orchestrator from the developer's hand-back (the developer's write is blocked by the tool). The recurrence is **Bartels–Jezioranski 1985** (record `bartels-jezioranski-1985`); "Brezinski–Jelassi" was the developer's error.

> Developer corrections: 2026-10-31T23:14Z after reconstruction 01 ([response-recon-01.md](response-recon-01.md)); 2026-10-31T23:38Z after reconstruction 02 ([response-recon-02.md](response-recon-02.md)) — changed item 3 (113 PROVED), item 5 (dev rule; actual-rounding resolution), §4, §5 (selection ranking depends on the set), §6. Earlier versions are in Git history. 2026-11-01T08:41:34+01:00, after Codex audit-01 ([response-audit-01.md](response-audit-01.md)): changed items 1–7, 9, 10 and §6. The pre-audit wording is at branch head `5f52331`.

Claude Opus 5.5, xhigh; 7 of 10 rounds used; IDs provisional. Reconstruction 01 covered R01–R03 (two blocking findings, both applied); reconstruction 02 covered the response and R04–R07 (no blocking findings). No novelty is claimed.

## Setting

- Recurrence: window recurrence for X = diag(x), Y = diag(y).
- BJ ("dev") parent rule: (t,0) = X·(t−1,0), (t,j≥1) = Y·(t−1,j−1); HL is the mirror. Other parent rules give the same basis but different numerics, and which rule is best depends on the set (PD-N-105).
- Windows: block or exact. Orthogonalisation: CGS (BJ) or MGS with reorthogonalisation (HL).
- The plan's u is 2⁻⁵³. Verdicts depending on 2⁻⁵² vs 2⁻⁵³ are marked; the R07 ones are resolved by actual rounding (item 5).
- MEASURED = floating-point experiment only.

## 1. Surviving claims, ranked

1. **Ritz residuals do not govern the loss on the listed non-product sets (L1-Q1, via K2).** N101 (scoped after audit-01 LL-M1):
   - (a1) the 14 R01 main non-product runs, all sections: excess over u/ρ_O 1.0·10²–1.0·10¹⁴ at u = 2^-52, 4.4·10¹–2.1·10¹⁴ at 2^-53, never in the factor-3 band;
   - (a2) the seed-11 rotation 0.3, π/4, disk and triangle sets, Z only: ≈ 3·10²–10¹³;
   - probe-only sets (rotation 0.05, shears, rotated Beta set): no Ritz claim. The 0.05 rotation is near the Ritz level (audit: 3.7–7.2).
   - Single and joint residuals never separate. K1 inconclusive; N101(b) withdrawn (chain-completion degree). 107(a,b): Ritz-type loss on the listed product-aligned set types; on the listed non-product sets under the dev rule the log-loss is convex from n ≈ 8–12. Support shape does not classify the regime (N106; ‖A‖ factor noted).
2. **L4 obstruction.** 401 PROVED; confirmed by reconstruction 01 and Codex audit-01, which completed the edge case of Corollary 2's proof.
3. **A-priori amplification for a given selection rule; certified for the dev rule.** 109(a) MEASURED. Loss depends strongly on the selection rule (N105). Original 109 Consequence REJECTED: refuted. 113 PROVED: part 1 impulse identity; part 2 exact finite dev-rule certificate (G over k > s, n ≤ 12): T_24 log₁₀G(12) − log₁₀G(6) = 8.69, so G(12) ≥ 10⁶G(6); Q_24 0.80, so G(12) ≤ 10²G(6); independently reproduced two ways by reconstruction 02. Part 3 PROVED (finite) for T_40, rotated Q_24 and Q_40; Q_40 was independently rerun by Codex audit-01. The affine scaling holds for c > 0, with signs for c < 0 (audit-01 LL-L1). No asymptotic claim.
4. **Product factorisation.** 105 PROVED; part 2 is the idealised propagator — it explains the propagator, not the loss; part 1 known (BPS Remark 5). The floating-point transfer is split off as 116, CONDITIONAL on near-exact computed coefficients (H_δ; audit-01 S1). 111 PROVED; confirmed by reconstruction 02.
5. **Coefficient channel on product-type measures (dev rule; shown on extreme-weight checkerboards).** 114 PROVED (exact gain formulas; confirmed by reconstruction 02). The gain census and first-order channel are split off as 117 MEASURED: on/off split reproduced independently, magnitudes reproduced by the audit's producer rerun (audit-01 LL-M2). 115 MEASURED (closed-loop dot-product rounding *reproduces* the loss: sufficiency within the tested models; dot64 includes operand conversion): off-pattern values feedback-dominated with structured signs (random signs 10³×; feedback and rounding parts cancel); open-loop estimates over-estimate, more with clustering; 115(d) REVIEWER-MEASURED: with actual double dot products the closed loop reproduces the loss (C/L 0.56–1.86 on six sets; IDEA-120 survives, IDEA-119 inconclusive; feedback damping ≈ 1.5, 8, 30 for quadratic, cubic, quartic clustering); noise-model versions convention-sensitive. Under the alt rule the cubic-checkerboard loss is 3.1e-13 at n = 24 (dev 1.0e-6); the channel under other rules is not analysed.
6. **Paige-type identities.** 102, 103, 104, 106 PROVED; confirmed by reconstruction 01 and Codex audit-01 (103: the division by ‖Bs‖ needs Bs ≠ 0).
7. **Row selection.** 108 PROVED, with the statement corrected after audit-01 F1/F2: other selections must be admissible (A·lm(q_l) = lm(q_k)), and the left inverse is of the normalised system with π_0 = 1 (square for n = 1, overdetermined for n ≥ 2). Framing known (Xu/Dunkl–Xu, BPS). Separations in §3.
8. **Pattern.** 101 PROVED.
9. **Near-product bound.** 110 PROVED (confirmed by reconstruction 02); informative only near exact products. The consistency check used 28/28/28/27 sampled nodes.
10. **Measurements.** 112 ((a), (b), (d) confirmed by reconstruction 02; dev rule; PC-12 applied; (e) uses computed reference coefficients); 107(c–f); 109(b) narrowed; N102 (its 'full' control widens only the N-products).

## 2. Failed and refuted routes

Ritz governance on non-product sets (N101a); SIMAX windowed form (N102); H_lin, a universal predictor, two relations as an unconditional fix (N103; (c) confirmed by reconstruction 02); "selection, not truncation" (N105, refuted); support classifier (N106, refuted); open-loop noise estimates (N104: generic noise and random signs fail; term-wise estimate inconclusive); block-Paige identity as a control; near-product bound off-product; local Gram–Schmidt as the cause.

## 3. Prior art

BPS 2010 (closest predecessor; Remark 9 and §5 anticipate selection dependence); Zaccaron 2014 (geometry dependence); Liu–Narayan 2023 (two-relation predecessor); Sinha 2026 (103 is a variant). Separations: coupled graded basis, discrete Lanczos with truncation, the loss link, quantified and set-dependent selection effects, the finite exact certificate, the coefficient channel.

## 4. Briefs (changes)

- (1) A measure-based regime classifier.
- (3) Name the selection rule in every growth statement. Certificate rerun done. Next: selection dependence of the certified quantity, and any all-n bound.
- (7) Selection principle (for L2). The ranking depends on the set: adapt wins on rotation 0.3 and the triangle but is 9× worse than dev on the cubic checkerboard, where alt is best.
- (5) Use actual reduced-precision dot products rather than per-term noise models. Next: an analytic account of the feedback damping (I − T)⁻¹.

## 5. L2 hand-off

Selection rules change the loss by up to 10⁸, but no tested rule is best everywhere (alt and adapt reduce the dev loss by 10³–10⁸ on the non-product sets; on the cubic checkerboard alt reduces it 3·10⁶× while adapt makes it 9× worse). Full single-pass CGS is stable on rotation π/4 and the disk. Two relations fail on clustered checkerboards and are worse on tensor grids. Zeroing off-pattern window coefficients works when the product structure is known. Compensated dot products untested.

## 6. Runs needed

M = 10⁵–10⁶ on syvert0/1/2; a selection-rule sweep with more seeds and sets; graded checkerboards m = 40–60, HL, ORTH. Independent implementations, beyond the audit's producer reruns, for 112(e,f), N103(a,b), the 117 gain magnitudes, and the C01 and R07 anatomy. A measurement of δ·κ(z_i) to test H_δ of 116. Fresh reruns of the T_40 and rotated-Q_24 certificates. [Q_40 rerun removed 2026-11-01T08:41:34+01:00: done by Codex audit-01.]
