# L1 (+L4) — Direction summary after R07, corrected after reconstruction 01 (2026-10-31)

> Orchestrator note (kept): saved by the orchestrator from the developer's hand-back (the developer's write was blocked by the tool). The recurrence is **Bartels–Jezioranski 1985** (record `bartels-jezioranski-1985`); "Brezinski–Jelassi" was the developer's error.

> Developer correction 2026-10-31T23:14Z ([response-recon-01.md](response-recon-01.md)): items 1, 3, 5, 7, 10 and §§2–5 are updated after reconstruction 01 and the C01 checks. The earlier text is at commit 6a5bf89.

Claude Opus 5.5, xhigh. 7 of 10 rounds used; IDs provisional. Reconstruction 01 (R01–R03) confirmed 101–104, 106, 401 and N102; corrected 105 and 108; and raised B1 and B2. R04–R07 have not been reconstructed. No novelty is claimed.

## Setting

- Recurrence: window recurrence for X = diag(x), Y = diag(y).
- BJ ("dev") parent rule: (t,0) = X·(t−1,0), (t,j≥1) = Y·(t−1,j−1). HL is the mirror. Other parent rules give the same basis but different numerics (PD-N-105).
- Windows: block or exact. Orthogonalisation: CGS (BJ) or MGS + reorthogonalisation (HL).
- u: the plan's u is 2⁻⁵³. The R01–R07 rules used 2⁻⁵²; verdicts that change with this are marked convention-sensitive.
- MEASURED means a floating-point experiment only.

## 1. Surviving claims, ranked

1. **Ritz residuals do not govern loss on the listed non-product sets (L1-Q1, via K2).** N101(a): loss exceeds u/ρ_O by 10²–10¹⁴ for X, Y, Z, an oblique section and N_k; single and joint residuals never separate. K1 is inconclusive (B2). N101(b) is withdrawn (chain-completion degree). 107(a,b): Ritz-type behaviour on the listed product-aligned set types; on the non-product sets with the dev rule the log-loss grows convexly from n ≈ 8–12, scales with u, and does not track Ritz convergence. The support shape does not classify the regime (N106).
2. **L4 obstruction.** 401, PROVED. U(2m+1) is necessary. A commuting A admits no fixed-m band Krylov description of S_m and S_{m+1}. Corollaries: m ≥ n in general, m ≥ n+1 for affine A (covered via Lemma 1).
3. **Amplification is a priori for a fixed selection rule.** 109(a): P* = P for the dev rule. The size depends on the selection rule (10³–10⁸, N105). The truncation is a cause on rotation π/4 and the disk. The original Consequence is REJECTED: refuted. 113: part 1 (impulse identity) PROVED; part 2 is a dev-rule certificate on T_24 (8.69 vs 0.80), CONDITIONAL on an independent rerun.
4. **Product factorisation.** 105 part 2: PROVED, IDEALIZED; it explains the propagator, not the loss; 2′ needs ‖L⁻¹‖δ ≪ 1. Part 1 is known (BPS Remark 5). 111: PROVED (moment matching, checkerboards, Padua cubature).
5. **Coefficient channel (product-type measures).** 114: parts 1–4 PROVED; part 5 MEASURED. 115, MEASURED: off-pattern values are feedback-dominated and sign-structured (random signs give 10³×; φ and ρ cancel); the open-loop over-estimate grows with clustering (0.5–1×, 2–13×, 11–120×); closed-loop C/L ∈ [0.14, 1.06]. The pre-registered verdicts are convention-sensitive.
6. **Paige-type identities.** 102, 103, 104, 106, PROVED and confirmed. Minor fixes in 102 and 106. 103 is a variant of Sinha's identity.
7. **Row selection.** 108, PROVED; the framing is known (Xu/Dunkl–Xu, BPS eq. (5), Remark 9, §5, (18)–(20)). Separation: a coupled graded orthonormal basis (BPS is monic); discrete Lanczos with truncation; the loss link; the measured selection dependence (N105).
8. **Pattern.** 101, PROVED.
9. **Near-product bound.** 110, PROVED; informative only near exact products.
10. **Measurements.** 112 (PC-11, PC-12; dev rule). 107(c–f). 109(b), narrowed: two relations remove the growth on rotated squares, disk, annulus and rotated tensor; they reduce the triangle's loss, do not help the Gaussian cloud, and are worse on tensor 41² and the clustered checkerboard. N102: onset at n ≈ 6 with CGS, 8–10 with ORTH.

## 2. Failed and refuted routes

Ritz governance on non-product sets (N101a; the tensor falsifier is withdrawn); the SIMAX windowed form (N102); H_lin (N103a); a universal propagator predictor (N103b); two relations as an unconditional fix (N103c); "selection, not truncation" (N105, refuted); the support classifier (N106, refuted); open-loop noise estimates (N104; the term-wise kill is convention-sensitive); the block-Paige identity as a control; the near-product bound off-product; local Gram–Schmidt as the cause.

## 3. Prior art

- **BPS 2010** (pp. 409–410, 413, 418–419 read): closest predecessor of items 7 and 6/104. Remark 9 and §5 anticipate the selection dependence qualitatively. Separation: coupled basis, discrete Lanczos with truncation, the loss link, the quantified selection dependence and its a-priori form, factorisation, the coefficient channel.
- **Zaccaron 2014** (via the prior-art check): the geometry dependence is prior art. Separation: the a-priori property for a fixed rule, the certificate, factorisation, the quantified selection dependence.
- **Liu–Narayan 2023:** the two-relation predecessor. Separation: the scoped equal-truncation comparison, including where it does not help.
- **Sinha 2026** (summary only): 103 is a variant.

## 4. Briefs (changes only)

- (1) Find a measure-based classifier: coupling, exact-propagator norm per rule, or the 114 gains.
- (3) Name the selection rule in every growth statement; rerun the certificate first.
- (7) The selection principle — minimising max_z‖L*⁻¹‖ — is the central open question, for L2.
- (5) Calibrate the rounding model (standard deviation ≈ u/√3; BLAS summation) before 5×-band tests.
- Other briefs are as at commit 6a5bf89.

## 5. L2 hand-off

The alt and adapt rules reduce the loss by 10³–10⁸; full single-pass CGS is stable on rotation π/4 and the disk; two relations fail on clustered checkerboards and are worse on tensor grids; zeroing the off-pattern coefficients works when the product structure is known; compensated dot products are untested.

## 6. Runs needed

Certificate rerun; M = 10⁵–10⁶ on syvert; a selection-rule sweep with more seeds; m = 40–60 checkerboards, HL, ORTH; independent reruns of R04–R07 and C01.
