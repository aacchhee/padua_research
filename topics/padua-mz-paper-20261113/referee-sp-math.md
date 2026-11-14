# Internal referee report (mathematics): MZ-SP manuscript

**Referee:** Claude subagent, independent of the authoring session. Model Claude Opus 5.5 (`claude-opus-5-5`). Requested effort xhigh; the runtime does not expose the effort setting. Reason for the choice: a mathematics referee needs Opus at high or xhigh effort (`agents/claude/CLAUDE_ROLES.md`).
**Role:** independent mathematical referee (AUDIT-style record). I did not write the paper. I made no Git state changes and did not edit the manuscript. This is the only file I wrote in the repository. Scratch scripts and outputs are in `/tmp/ref-sp-math/`.
**Rules/head read:** `AGENTS.md`, plus `agents/claude/CLAUDE_ROLES.md` and `agents/WORKFLOW.md` (grep for the audit format), at `8f08d9a82a174974b0b26ed5bb98932835f2fc71` (branch `claude/padua-mz-paper-20261113`).
**Audited object:** `tracks/mz-constants/paper-sp/manuscript.tex` at head `8f08d9a`, sha256 `956fdee6…50b5` (2478 lines); `refs.bib` sha256 `318b8320…481c`.
**Build:** `tools/build.sh … /tmp/ref-sp-math` produced 47 pp (elsarticle preprint, A4) with no LaTeX or BibTeX warnings. PDF sha256 `4239a7f0…bef11`. Statement numbers below come from this build.
**Read coverage:** the whole manuscript, line by line: §§1–9, the data and code statement, and Appendices A and B.
- *Companion paper:* `tracks/mz-constants/paper/manuscript.tex`, at the statements cited for the three Clenshaw–Curtis inputs: Thm 1.1, 1.2, 1.3, Cor 3.2, Thm 4.3, 4.6, Cor 6.1, Prop 8.1, and the frozen numbering in `correspondence-cc.md`.
- *Records consulted for comparison only:* `correspondence-sp.md`; S3-full-form-log-model, S3-corner-operator-limit, S3-corner-kernel-hard, S3-carrier-family-ceiling and P2-measurements (`topics/padua-mz-sharp-constants-20261106/theory/`); f4-uniform-density-bound and f12-local-weight-asymptotic (`topics/padua-mz-2d-frontier-20261105/theory/`); finite-indefiniteness and odd-weight-asymptotic (`topics/padua-mz-cleanup-20261105/theory/`).
- *Code read:* `code/P1_rectangle.py` and `code/interval_dyadic.py`, in full.

Every judgement below rests on the paper's own text.

Target venue: J. Approx. Theory. Scale: CRITICAL = a wrong statement, or a gap that breaks a theorem; MAJOR = a gap that one paragraph can fix; MINOR; TYPO.

---

## Overall assessment

I checked every proof line by line, in the requested priority order. I found **no CRITICAL and no MAJOR finding**. Every theorem, proposition and lemma is correct as stated, and its proof is complete at journal level. This covers:

- the CC-weights lemma (2.1), the compression theorem (3.1), and the weight lemma, theorem and proposition (4.1–4.3);
- the carrier chain (5.1–5.8, including Lemma 5.5);
- the corner-operator chain (6.1–6.5 with Appendix A);
- the structure and enclosure chain (6.6–6.10 with Appendix B);
- Theorem 7.1, Remark 7.2 and Proposition 7.3;
- the two computer-assisted finite results (8.1, 8.2).

Every explicit constant that I could test holds:

- with large margins for 4096, 4300, 120, 120/K, E_K and 8192;
- to all printed digits for C_P, κ_new, κ^car_+, U_−, the enclosure endpoints and the brackets.

The rerun of the enclosure checker reproduces the paper's integers n_L and n_U bit for bit. An independent float computation of the limit operator B_K confirms that the normalisation (the factor 16, the single-corner operator, and the doubling by the two active corners) is consistent with the finite forms L_m.

The three companion-paper inputs exist in MZ-CC with exactly the stated content and the same normalisation. The paper cites them only globally, not by statement number (F1).

The three additions flagged in the correspondence log are sound:

- **η < 0.83** is correct arithmetic on the certified brackets: the maximum is 0.82727, at m = 80.
- **(2+C_P)E_k** (Remark 7.2) is an immediate and correct consequence of Theorem 7.1 and reproduction.
- **PD-T534 constants:** the appendix proves 3360 ≤ 4096 and 4096 + 120 log(5/2) = 4205.95 < 4300, so the stated constants have margin.

I found no other statement stronger than its record.

The findings concern abstract and introduction precision, measurement wording, data pointers, and presentation. Two should be fixed before submission:

- **F1:** pointers into MZ-CC, plus the companion title in the bibliography (F2).
- **F3:** "the marginals" are not both Clenshaw–Curtis.

---

## Findings

**F1. MINOR (fix before submission). CC inputs are cited without statement pointers.**
*Location:* Prop 2.2 (`prop:cc-inputs`), l.274–278; Introduction "Clenshaw–Curtis inputs", l.143–148.
*Problem:* The three inputs are attributed to [MZ-CC] as a whole. I checked that each exists in the frozen companion with the same content and the same normalisation (unnormalized dx, λ_±(N,n) on Π_n):
- λ_+(N,n) ≤ 2 − 4/N + 4/N² for 0 ≤ n < N and N ≥ 2: MZ-CC **Corollary 3.2** (`cor:ratio-endpoint`), "the same holds on every Π_n with n < N".
- λ_−(N,N−1) → 0: MZ-CC **Theorem 4.3** (`thm:harmonic`, λ_−(N,N−1) ≤ 128000/(log N)²). Theorems 1.2 and 4.6 also give it.
- λ_−(512,511) < 1/4: MZ-CC **Proposition 8.1** (`prop:counterexample`).

Since the companion is frozen, a referee will expect precise pointers.
*Fix:* In the heading of Prop 2.2, write `\citealp[Cor.~3.2, Thm~4.3 and Prop.~8.1]{MZ-CC}`. Repeat the pointers at l.147.

**F2. TYPO. Companion title in the bibliography.**
*Location:* `refs.bib`, entry `MZ-CC`, l.3.
*Problem:* The entry reads "…constants of Clenshaw–Curtis **rules** beyond half-exactness". The companion's `\title` is "Marcinkiewicz–Zygmund constants of Clenshaw–Curtis **quadrature** beyond half-exactness".
*Fix:* Replace "rules" with "quadrature" in the title field.

**F3. MINOR (fix before submission). Only one marginal is Clenshaw–Curtis.**
*Location:* Abstract l.38–40 ("The marginals of the rule are the Clenshaw–Curtis rule, with a factor two"); Introduction l.96–97 ("through the marginals of the Padua rule") and item A, l.106–107 ("For every rule exact on P_m, the weights summed over one coordinate…").
*Problem:* Theorem 3.1 correctly proves the statement for the sum over k at each x-node (mesh N = m). The other marginal (the sum over j at each y_k) is not twice the CC rule with m+1 intervals.
- For even m, Q(T_{m+1}(y)) = Q(T_m(x)) = 2h_m ≠ 0 = 2h_{m+1}; this is the computation in the proof of Prop 7.3.
- For odd m, Q(T_{m+1}(y)) = 0 ≠ 2h_{m+1}.
- Numerically, max_k |Σ_j W_jk − 2w^CC_{m+1,k}| = 1.6·10⁻² at m = 6 and 2.3·10⁻³ at m = 11.

Item A also omits that the rule must live on X_m.
*Fix:*
- Abstract: "The marginal of the rule in the first coordinate is the Clenshaw–Curtis rule with m intervals, with a factor two, and this bounds…".
- l.97: "through the first-coordinate marginal of the Padua rule".
- Item A: "For every rule on the Padua points exact on P_m, the weights summed over the second coordinate at each node abscissa equal twice the Clenshaw–Curtis weights with m intervals, and…".

**F4. MINOR. Abstract wording on brackets and ratios.**
*Location:* Abstract l.41 and l.47–48.
*Problem:*
- (a) "Exact spectral brackets" suggests exact eigenvalues. Prop 8.1 gives certified rational brackets of width 10⁻⁶.
- (b) "For every fixed ratio n/m>1/2" is broader than Corollary 5.3, which covers τ ∈ (1/2,1). The endpoint n = m−1 is covered by Thm 5.1 and Prop 5.2, and n = m only by an unstated monotonicity argument.

*Fix:* "Certified spectral brackets at six degrees up to 80…". "For every fixed ratio 1/2 < n/m < 1 the least eigenvalue…".

**F5. MINOR. The motivational paragraph of §6 overstates the corner sign pattern.**
*Location:* §6 opening, l.904–908 ("close to a corner of the square the signed weights are of order m⁻⁴ log m, with signs alternating along the checkerboard and with the coefficient −16e_je_k(−1)^j").
*Problem:*
- (a) This holds only near the two **active** corners. Near the inactive corners the logarithmic terms cancel (App A.3, Step 1; Remark 6.5).
- (b) Theorem 4.2 is a fixed-index limit with corrections of relative size about π⁴jk/(8 log m). These are far from negligible at any realistic m. With the exact density formula I computed m⁴w_{22}/log m ≈ +47 at m = 409 600, against the limit −16. The rule has exactly two negative weights at every m ≤ 401 that I tested, which is consistent with §8.3(1).

A reader who takes the sentence literally will expect alternating signs in the actual weights.
*Fix:* "In the limit m→∞ at a fixed index distance from one of the two active corners (Remark 6.5), the signed weights are of order m⁻⁴ log m with the coefficient −16e_je_k(−1)^j; the approach to this limit is only logarithmic, and at moderate m the sign pattern is not yet visible."

**F6. MINOR. §8.3(3) contradicts Remark 6.4 on the rate.**
*Location:* l.1553–1555 ("Theorem 6.3 gives a limit of λ^P_±/log m with no rate").
*Problem:* Remark 6.4 gives an explicit rate, coarse but proved. §9, item 3 phrases this correctly ("no usable rate").
*Fix:* "…gives a limit of λ^P_±/log m with no rate usable at these degrees (the explicit bound of Remark 6.4 is far too coarse), and the slope of a window…".

**F7. MINOR. "Mode 2" is defined ambiguously.**
*Location:* §8.3(2), l.1549–1550, and l.1566–1568.
*Problem:* "Mode 2 is the span of the second eigenvalue of the finite form L_m, a doublet by Remark 6.5."
- Record PD-T543 defines mode 2 as the **second ordered doublet** of L_m (the 3rd and 4th eigenvalues).
- The lowest eigenvalue of L_m is itself a near-doublet. For example, at m = 80 my computation gives −0.13535, −0.13534, then −0.09672. So "the second eigenvalue" literally names the partner of the lowest one.
- Remark 6.5 proves only the limiting multiplicity; at finite m the doublets are nearly, not exactly, degenerate.
- "The decay rate of the compressed branches" (l.1567–1568) is undefined in the paper.

*Fix:* "Mode 2 is the two-dimensional span of the eigenvectors of the third and fourth smallest eigenvalues of L_m (its second near-doublet; cf. Remark 6.5); its weight is the squared norm of the projection of the minimizer onto this span." Either define the "compressed branches" in one clause or drop the parenthesis.

**F8. MINOR. Data pointer for the second proxy eigenvalue.**
*Location:* §8.3(4), l.1559 (−0.0955); data and code statement, l.1658–1661.
*Problem:* The receipt `S3-corner-model.json` records only λ_min and λ_max of B_K (−0.13358, 0.04560). The second negative eigenvalue b₂ = −0.0955298 comes from P2 (PD-T543), receipt `evidence/P2-b2-calibration.json`, produced by `P2_modes.py`. The closeness figures 0.0034 and 0.0031 also use the unrounded b₂ from P2; with the rounded −0.0955 the second would read 0.0030.
*Fix:* Add "`evidence/P2-b2-calibration.json` (the proxy b₂)" to the measurements paragraph. In (4), optionally write "about −0.09553".

**F9. MINOR. The size of the "strict improvement" is not shown.**
*Location:* Prop 5.7; orientation sentences l.897–899 and l.1224–1225.
*Problem:* The paper never gives κ^car_−. I computed:

| Quantity | Value |
|---|---|
| κ^car_− | 0.0296218 |
| κ_new | 0.0296418 |
| Improvement | 2.0·10⁻⁵ (0.07 %) |
| Measured supremum of κ_−(a, ½−a) | 0.029643, at a ≈ 0.257 |
| U_− | 0.0333 |

So κ_new is within 2·10⁻⁶ of the best scalar-family value, while U_− overshoots it by about 12 %. Prop 5.7 is correct, but readers should see that the improvement is marginal and that the ceiling is not tight. The paper does say that no optimality claim is made.
*Fix:* Change l.897 to "For orientation only, κ^car_− ≈ 0.02962, κ_new ≈ 0.02964 and U_− ≈ 0.0333; …". Optionally add a measured remark that a floating scan of the family gives sup ≈ 0.02964.

**F10. MINOR. Remark 6.5 overstates what Lemma A.4 gives about "nonzero eigenvalues".**
*Location:* Remark 6.5, l.1058–1061; proof sketch l.2129–2133.
*Problem:* Lemma A.4 gives convergence of the N ordered eigenvalues of X_m to those of X_∞ = X_B ⊕ X_B ⊕ 0 ⊕ 0. The inactive corners contribute eigenvalues of size O(K/m), which are nonzero at finite m. So "the nonzero eigenvalues … converge … to those of B_K ⊕ B_K" is imprecise, although the intended content is right. My computation of X_m (K = 8, m = 40…321) shows clean doublets converging to the eigenvalues of B_8.
*Fix:* "…the eigenvalues of the finite-rank form obtained from (6.1) by keeping the nodes within (1+d_j)(1+d'_k) ≤ K converge, counted with multiplicity, to those of X_B ⊕ X_B ⊕ 0 ⊕ 0 (Lemma A.4): each nonzero eigenvalue of B_K is the limit of two of them, and the remaining ones tend to zero."

**F11. MINOR. Corollary 5.3: state that the variational principle is used on P_{⌊τm⌋}.**
*Location:* Proof of Cor 5.3, l.656–661.
*Problem:* Theorem 5.1 and Prop 5.2 conclude only at n = m−1. The corollary needs the same carriers on P_{⌊τm⌋}. The proof checks the degree bounds but only says "the even-m proof and its odd-m extension therefore apply". The step is correct, because the energy limits and norm bounds do not depend on n.
*Fix:* Add: "Since these carriers lie in P_{⌊τm⌋}, and their signed-energy limits and norm bounds do not depend on the ambient degree, the variational principle on P_{⌊τm⌋} gives the two divergences."

**F12. MINOR (presentation). Theorem 7.1 proof, first paragraph.**
*Location:* l.1264–1282.
*Problem:*
- (a) The display at l.1267–1270 uses A_R before it is defined (the definition ":=" appears in the next display).
- (b) "The absolutely convergent coefficients t_r used above" refers to the proof of Thm 4.2, three sections earlier.
- (c) "affects only the two nonzero coordinate axes" is unclear.
- (d) The bound Σ(2i−1)⁻¹ ≤ (R+2)/3 is correct but very crude. It suffices only because equality then holds in A_R ≥ −4/M′; I checked this in exact rationals for R ≤ 39. A one-line justification (induction, since each new term 1/(2R+1) ≤ 1/3) would help.

*Fix:* Define A_R := Σ_{r+s≤R} t_r t_s first. Write "the coefficients t_r of the proof of Theorem 4.2". Write "affects only the pairs (0,s), (r,0) with r,s ≥ 1 on the coordinate axes".

**F13. TYPO.**
- App B.1, l.2195–2196: "and sin u = sin v turns the integral into ξ_s⁻¹K(1/ξ_s)". This substitution is the identity. Write "and the integral equals ξ_s⁻¹K(1/ξ_s) directly".
- Lemma 5.5, l.715: "(Dirichlet's test justifies the limit)". The limit ϱ↓0 needs uniform convergence in ϱ ≥ 0, so write "(Abel's test gives uniform convergence in ϱ ≥ 0, which justifies the limit)".
- l.793: "obtained on the closures" should be "approached on the closures": the suprema are not attained by admissible parameters.

**F14. MINOR (presentation). Symbol overloads inside proofs.**
These clashes can mislead a reader checking constants:
- g: the Fejér profile in Lemma 5.5 and Prop 5.6, but g(x) = π√(1−x²) in Thm 7.1.
- κ: κ = ½ + 1/π in Thm 7.1, against κ_new and κ^car.
- α, β: α = π − 4/3 and the least-squares fit α + β log m, against the CC weights α_j, β_k (Lemma A.2), the kernel β, and β_K(m).
- L: r+1 in §5, ⌊R/2⌋ in Lemma A.1, and the enclosure endpoint L.
- U: the enclosure endpoint, the cube size in Lemma 6.2, U_−, U_{m,j}, and the rectangles U×V.
- r: the Fejér degree, and ‖B‖ in §6.2.
- τ: the degree ratio, and min(t, π−t) in Lemma A.1.
- Q_i in Prop 6.8(b), against the quadrature Q.

*Fix:* Rename the local ones. For example: ĝ for the Fejér profile, κ₀ in Thm 7.1, w^CC_{m,j} in place of α_j, and t̄, s̄ in Lemma A.1. Leave the rest to the exposition round.

**F15. MINOR (evidence reading, not the paper's mathematics). The witness receipts need the reconstruction rule.**
*Location:* Proof of Prop 8.2, l.1509–1522; data and code statement, l.1631–1640.
*Problem:* The independent checker's printed `q_enclosure` loses display digits. At m = 1240 it is [−2.7e−5 ± 2.30e−7], and at m = 1600 it is [−0.023414 ± 5.91e−7]. Both are wider than the table intervals. Containment holds only for `q_center ± q_absolute_error`. I reconstructed:
- (−2.7230, −2.7066)·10⁻⁵ ⊂ (−2.73, −2.70)·10⁻⁵ at m = 1240;
- (−0.0234146, −0.0234142) ⊂ (−0.023415, −0.023414) at m = 1600.

The record states this rule, but the paper does not. A reader checking the deposit could wrongly conclude that the second program does not support the table.
*Fix:* Add to the data and code statement: "the second program's interval is q_center ± q_absolute_error in its receipt; the printed q_enclosure field is rounded for display."

---

## What I verified

Numerical checks are in `/tmp/ref-sp-math/check_{constants,weights,corner,kernel,density}.py`.

**1. Lemma 2.1 (CC weights).**
- Line-checked: the discrete orthogonality Φᵀdiag(ε)Φ = (N/2)diag(ε)⁻¹, the cardinal expansion, endpoint values, the even-N regrouping, the concavity step and the floor.
- Numerically for N = 2…399: the closed form against a moment solve (N < 60); |W_N − (π/2)sin| ≤ 1/N or N/(N²−1) (equality at the endpoints for odd N); w_j ≥ (π−4/3)sinθ_j/N; w_j ≥ (1+d_j)/N².

**2. Prop 2.2 against MZ-CC.** See F1: the statements exist and the normalisation matches.

**3. Thm 3.1.** Line-checked the marginal, the isometry ι and the compression. Numerically, the marginal identity holds to 2·10⁻¹⁶ for m ≤ 401 and the total mass is 4.

**4. Lemma 4.1.**
- Line-checked the checkerboard orthogonality: an alternating term needs total degree ≥ 2m+1, and the (m,0) norm is 2.
- Numerically, the density formula equals the moment-solve weights to 1.6·10⁻¹⁵ for m = 4…9.

**5. Thm 4.2 and Prop 4.3.**
- Line-checked |T_R| ≤ 2/(2R+1), |V_R| ≤ 64(1+log R)/R² (strip counting), 260 + 16/3, m/R ≤ 5/2 and 400(1+log R).
- The strip asymptotics give (−1)^j + (−1)^k.
- Numerically, max |w|/majorant ≤ 0.041 (m ≤ 401, both parities).
- The fixed-index ratios at m = 409 600 and 409 601 are 0.982 and 1.021 at (0,0) and still converging slowly elsewhere, consistent with the O(1/log m) corrections (F5).

**6. Thm 5.1, Prop 5.2, Cor 5.3.**
- Line-checked the degrees, ‖F_r‖² ≤ (1+π⁴)/2, D_r, the T_{2r} coefficient 2/(r+1)², the trapezoid ranges (degree < M for the alternating identity; 2a + b < ½ implies 4r < m), and the profile decay and majorant for dominated convergence.
- Limits checked: −16ab/9 and 8ab/9 for even m, and the odd-m analogue.
- Choice a = b = (τ−½)/4 checked.

**7. Lemma 5.5.**
- Line-checked the product-to-sum, Σc_t = Σc_t t = Σc_t t² = Σc_t t³ = 0, the double integration by parts, and Frullani.
- Numerically, ∫u g cos(qu) agrees with Δ⁴h(q) at seven values of q (to ≈10⁻⁷).

**8. Prop 5.6.** Norm limits checked. J_−(1/4) = 1.352883 (closed form and quadrature). J_+(1/8) = 0.784005, from a closed form via Δ⁴h at 2, 6, 8 and 10 and from quadrature. κ^car_− = 0.0296218 and κ^car_+ = 0.0127789 (paper: 0.01278).

**9. Prop 5.7.**
- h'''' = −2/x², the B-spline representation of Δ⁴, Jensen's inequality, J′ ≤ −a (also numerically on the interval), 21/16000, and e^{0.7} > 2.0121.
- κ_new = 0.0296418 (paper: 0.02964).

**10. Prop 5.8.** Δ⁴h(2) = 28 log 2 − 18 log 3; J_end = 16 log 2 − 9 log 3 = 1.20284; U_− = 0.0333167 < 1/24; 2¹⁶ > 3¹⁰ and e² < 8.

**11. Thm 6.1 with Lemmas A.1–A.3.** Every constant was checked: 12a/R, 8 + (4/3)Rτ, the bound < 4, 256/9, 53, 54, π⁴/4 < 25, π(π+8/3)/2 < 10, 112, mM/R² ≤ 15/2, 840 and 3360.
Numerical results:
- Lemma A.1: LHS/RHS ≤ 0.068 for R ≤ 80.
- The remainder over 54D_jk: ≤ 0.40.
- |w − log R·ℓ|/(α_jβ_k): ≤ 4.02 (bound 840) for m = 4…200.

**12. Lemma 6.2.**
- Line-checked Rodrigues and the generating function, Laplace's integral, the Bessel representation, |P_k(cos t) − J₀(kt)| ≤ kt²/4, telescoping, the Riemann sum (area of U_m∖T = 1/(2m)), the alternating pairs, and C_U (both shift choices).
- Numerically, 160 random trials at m = 10…300 give error/bound ≤ 3.6·10⁻⁴, and K_∞(0) = 1/24.

**13. Thm 6.3, Lemma A.4, Rem 6.4 and 6.5.**
- Line-checked q_m − 8 ∈ (0, 16/m] (m³ − 3m² − m + 2 ≥ 0 for m ≥ 5), the cosine errors, the inactive bound (needs m ≥ 2K), the closed form m(m+1)(m²+m+1)/24 and its increment, the √-perturbation bound 4√δ/π, the telescoping 64/√8 < 24, the Cauchy argument for B_K, and the parity bookkeeping of the active corners.
- Independent float computation:
  - B_K for K = 8…128: extremes −0.133580 and +0.045598, and b₂ = −0.095530. These match the receipts S3-corner-model.json and P2 b₂ and the paper's −0.1336, +0.0456 and −0.0955.
  - X_m (K = 8, m = 40…321): doublets converge to the spectrum of B_8.
  - Full L_m (m = 20…80): ν_− = −0.13535 and ν_+ = 0.04620 at m = 80, consistent with c_± ≈ −0.1336 and 0.0456.

**14. Prop 6.6 and App B.1–B.2.**
- Line-checked the arcsine convolution, the elliptic substitutions (Σ₀ = q°(0), Σ₁ = 2q°(1)), the Poisson/Abel identity, Scheffé's lemma, the Schur bound 32/π² = 3.2423, and the identification B = B̃ on C_c^∞.
- Numerically, Σ₀ and Σ₁ match the Abel sums (5 digits) at 4 points; the row integrals are ≤ 0.318 (≤ 1/π) and ≤ 0.272 (≤ 2/π).

**15. Prop 6.7.** Line-checked positivity improvement of (B⁻)², the Perron argument, simplicity via 4⟨w₊, Tw₋⟩, and c₊ < r.

**16. Prop 6.8.** Line-checked E(s), (a)–(c), and the weighted Schur test. Numerically, I_t equals ∫Σ_t a′da′ (6 digits) on three test cases.

**17. Prop 6.9 and App B.5.**
- `P1_rectangle.py` and `interval_dyadic.py` match the description: outward 2⁻²⁵⁶ arithmetic, isqrt, the cosine Taylor stop rule, Machin, 136 outer and 120 inner cells, and lower = 24·Σ m.
- **Rerun:** `P1_rectangle.py --N 16 --theta 256` took 1.4 s. Its endpoints are bit-identical to the receipt and equal the paper's n_L and n_U. The decimals are outward-rounded.
- U/L = 36.3, and κ_new/L = 2.2516 (paper: 2.25).
- Note: the "second run" receipt is the same program rerun, which the paper states correctly.

**18. Cor 6.10.** Checked.

**19. Thm 7.1.**
- A_R: both closed forms equal the direct sum in exact rationals for R = 1…39, and A_R ≥ −4/M′. The tail equals 16/M′ − A_R ≤ 20/M′.
- 4/(m²−1) ≤ 8/(3m); the Legendre sup bound; κ = ½ + 1/π; the discrete identity Σρp² = ∫p² d(ν⊗ν) on P_{m−1}.
- v-bound; Σv_z equals the cot formula and is ≤ 4 (m = 2…400).
- C_P = 28.37633483.

**20. Rem 7.2 and Prop 7.3.** Line-checked. The defect computed from the weights matches h_{m−1} − h_{m+1} (odd m) and h_m (even m) for m = 4…9.

**21. Prop 8.1.**
- All 12 brackets equal the producer receipts `cert-m*.json` and the independent receipts. The negative counts are 0/1 and dim−1/dim, with zero = 0.
- A float recomputation at m = 10, 20, 30 and 40 falls inside every bracket.
- η_max = 0.82727 < 0.83.
- The aliasing rule ϱ(r,s) = h_{m−A}h_{m+1−B} and the diagonal-dominance inertia argument were line-checked.

**22. Prop 8.2.** The producer Rayleigh enclosures lie inside the table. The independent enclosures, reconstructed as in F15, also lie inside. The m = 1600 numbers in the text match the receipt, and the archive sizes of 4.2, 5.4 and 8.7 MB match the payload identities.

**23. Measurements.** λ_min table, mode weights, b₂ and secants. Recomputed from the table: −0.09212 and −0.09247. Distances from b₂: 0.00341 and 0.00307 (records PD-T538 and PD-T543).

**24. Data and code statement.** All 18 cited code and receipt paths exist at `8f08d9a`.

**25. Abstract and Introduction items A–D.** Compared with the proved statements. Scope matches except F3 and F4.

## Remaining uncertainty

- I did not rerun the bracket programs: python-flint is not installed, and m = 80 takes about 300 s for the producer alone. I did not rerun the witness programs: the payloads are not in the repository. I relied on the receipts and on my float cross-check at m ≤ 40.
- The carrier limits (Thm 5.1, Prop 5.2) were verified analytically only. Their logarithmic convergence is too slow for a meaningful numerical test.
- Literature attributions are outside this mathematics round and were not checked: BCDMVX06 Thm 2, SVZ08 formula (33) and p. 421, Xu96, KLP18, CDMV07, ASV27 (including whether its rule is the same Lebesgue Padua rule, which bears on "extend it" at l.1431), and Wu26.
