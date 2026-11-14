# Internal referee report (mathematics): MZ-CC manuscript

**Referee:** Claude subagent, independent of the authoring session. Model Claude Opus 5.5 (`claude-opus-5-5`). Requested effort xhigh; the runtime does not expose the effort setting.
**Role:** independent mathematical referee (AUDIT-style record). I did not write the paper. I made no Git state changes and no edits to the manuscript. This is the only file written in the repository.
**Rules/head read:** `AGENTS.md`, `agents/claude/CLAUDE_ROLES.md` and `agents/WORKFLOW.md` (grep for audit format) at `d2e80007686706d8805debf168f4ee389134d55e`.
**Audited object:** `tracks/mz-constants/paper/manuscript.tex` at head `d2e8000`, sha256 `6f53026dfc72b4e55d5f80f628aabe49afd9f792e0ba18d0e076fa11cc375833` (2160 lines); `refs.bib` sha256 `84c81943…48c5`.
**Build:** `tools/build.sh … /tmp/ref-math`. 31 pp, no LaTeX/BibTeX warnings, PDF sha256 `f1b5b394…51d3`. Numbering used below is from that build.
**Read coverage:** the whole manuscript, line by line (§§1–9, Appendices A–C). Records consulted for comparison: `S2-qualitative-limit.md` (in full), `S2-uniform-upper.md` (grep), `theory/cc-defect-condition-corollary.md` (in full), `correspondence-cc.md`, and the certificate code `code/interval_dyadic.py`, `code/P4_rayleigh.py` (in full). Every judgement below rests on the paper's own text.

Target venue: SIAM J. Numer. Anal. Scale: CRITICAL = a wrong statement or a proof gap that breaks a theorem; MAJOR = a gap that one paragraph can fix; MINOR; TYPO.

---

## Overall assessment

I checked every proof line by line, in the requested priority order. I found **no CRITICAL and no MAJOR finding.** All theorems are correct as stated, and their proofs are complete at SINUM level:

- Theorem 3.4 (5/3);
- the π⁴/8 chain: Lemma 4.4, Proposition 4.5, Theorem 4.6 with the finite bound (4.14), Lemmas 4.8, 4.9 and A.1;
- the Λ_edge chain: Proposition 5.1, Theorem 5.2, Lemmas B.1 and B.2;
- Lemma C.1 and the certificate;
- Corollaries 4.7, 6.1 and 7.2, Propositions 8.1 and 8.2.

Every explicit constant I could test numerically holds. The §1 restatements match the proved statements in scope. The findings are wording, presentation and measurement issues:

- **F1**, an overstated measurement claim about the digits of Λ_edge, should be fixed before submission.
- **F2** points out that the proof of Theorem 3.4 already gives 23/15, which also justifies the paper's unproved remark that 5/3 is "not sharp".

---

## Findings

**F1. MINOR (fix before submission). Overstated numerical claim on Λ_edge.**
*Location:* text after Prop 5.3 (`prop:edge-certified`), l.1117–1121; also §9, l.1432–1436.
*Problem:* The paper says that floating Galerkin computations "with the same basis" and Table 1 "suggest that Λ_edge agrees with 1.0044369 to several further digits." They do not. The J-Galerkin values increase with J, because the subspaces are nested, and they are not converged at J = 512. My float64 runs used the closed forms of Lemma C.1 (script `/tmp/ref-math/c8.py`). The J = 512 value equals the certified q(u) to 12 digits, which confirms the assembly. The values are:

| J | Galerkin value |
|---|---|
| 256 | 1.0044364937 |
| 512 | 1.0044369189 |
| 1024 | 1.0044369474 |
| 2048 | 1.0044369671 |

The table value at N = 1280 is 1.004437035. So the eighth decimal of Λ_edge is not determined by any of these measurements, and the J = 512 value is about 5·10⁻⁸ below the J = 2048 value.
*Fix (replace l.1117–1121 from "Floating-point Galerkin…" to "…no digit beyond the certified bound is claimed."):* "Floating-point Galerkin computations on the spans of ζ₁,…,ζ_J give values that still increase at J = 2048 (1.00443692, 1.00443695, 1.00443697 for J = 512, 1024, 2048). Together with Table 1 they suggest Λ_edge ≈ 1.004437. These are measurements, and no digit beyond the certified bound is claimed." In §9 l.1434–1436, add after "gives 1.00443691886…": "(and 1.0044369671… on ζ₁,…,ζ₂₀₄₈, so the J = 512 value is not converged)". Label it MEASURED as usual.

**F2. MINOR. "5/3 is not sharp" is asserted but not proved; the proof already gives 23/15.**
*Location:* l.182 ("The constants 5/3 and C_* are not sharp"), l.554 (after Thm 3.4); Thm 3.4 proof, l.617–619.
*Problem:* The record S2-uniform-upper only says "not asserted sharp". The paper asserts non-sharpness without giving a reason. The proof itself gives λ₊(N,N−1) ≤ 1+β_N, and the following facts hold:
- β_N ≤ 8/15 for every N ≥ 3. The maximum is at N = 4. For odd N, β_N < 1/2. For even N, β_N decreases.
- λ₊(2,1) = 1 by exactness.

So sup_N λ₊(N,N−1) ≤ 23/15 < 5/3. Combined with Cor 3.3 (take min{1+ρ, 1+β_N} for N ≤ 8), the bound is even 95/63 ≈ 1.5079, attained by the bound at N = 8. I checked β_N exactly for N = 2…13.
*Fix (minimal):* append to the proof of Thm 3.4, after "…the second is below 1/2.": "In fact β_N ≤ 8/15 for N ≥ 3 and λ₊(2,1) = 1, so λ₊(N,N−1) ≤ 23/15 for every N ≥ 2. In particular 5/3 is not sharp." *Optional:* state 23/15 in Thm 3.4 and propagate it. Cor 6.1's 1/3 becomes 7/15. Cor 1.4(3) and (8.4) become 1+√(23/15) < 2.2385 (√(23/15) ≈ 1.23828). The threshold in (8.3) becomes n/N > (1+√(8/15))/2 ≈ 0.8651.

**F3. MINOR. Abstract formula does not match Theorem 1.1.**
*Location:* abstract, l.36–37.
*Problem:* "all eigenvalues lie below min{1+(2n/N−1)², 5/3} for n<N" omits the max{·,0} of ρ_{N,n}. For n < N/2 this is a weaker bound than the theorem's, so it is not a restatement. At n = N/2 the eigenvalues equal the bound, 1.
*Fix:* "We prove that for n<N all eigenvalues lie in (0, min{1+ρ_{N,n}, 5/3}] with ρ_{N,n}=max{2n/N−1,0}², strictly below 1+ρ_{N,n} when n>N/2, whereas the bound two fails at n=N."

**F4. MINOR. "Equivalently" in the abstract.**
*Location:* abstract, l.39–41.
*Problem:* The interpolation-norm statement is equivalent to the limit for λ₋(N,N) (Cor 4.7), not for λ₋(N,N−1), which is the only one the sentence mentions. Thm 1.2 gets this right because it states both limits.
*Fix:* "…satisfies (log N)²λ_min → π⁴/8, and the same holds on Π_N; equivalently, interpolation from CC-weighted nodal ℓ² data to L² has norm (2√2/π²+o(1)) log N."

**F5. MINOR. "Norm" versus "squared norm" of the endpoint operator, which is never defined.**
*Location:* abstract l.42 ("converges to the norm Λ_edge"); Thm 1.3 l.152 ("squared norm"); §5 intro l.1033 ("as the norm of an explicit sampling operator"); open problem 3, l.1444.
*Problem:* The wording is inconsistent. The "sampling operator" is only implicit in (5.2).
*Fix:* after (5.2) add: "Equivalently, Λ_edge = ‖𝒮‖², where 𝒮 g = (ĝ(0), ω₁^{1/2}ĝ(π), ω₂^{1/2}ĝ(2π), …) maps the completion of 𝒱₀ under 𝖬^{1/2} to ℓ²; by Lemma B.2 this completion is 𝒱 and the supremum over 𝒱 equals that over 𝒱₀." Then use "squared norm" in the abstract and in §5.

**F6. MINOR. Size of the gap between Theorems 4.1 and 4.3.**
*Location:* §4.1 first sentence, l.873 ("open by a factor of order 10⁶").
*Problem:* K_N ~ 32π²(π+1)²(log N)² ≈ 5418 (log N)². So (log N)²λ₋ ∈ [≈1.85·10⁻⁴, 128000], a factor of about 128000 × 5418 ≈ 6.9·10⁸. At N = 10⁶ I computed L²/K_N = 1.84·10⁻⁴.
*Fix:* "…but leave the constant open by a factor of order 10⁹."

**F7. MINOR. Wording in §1 bullet 6.**
*Location:* l.276–278 ("…gives the single-U upper bound λ₋(N,N−1) = O(1/log N) and hence vanishing for every N").
*Problem:* λ₋ is positive for every N. The intended meaning is convergence to 0 along all N, not just a subsequence.
*Fix:* "…= O(1/log N), hence λ₋(N,N−1) → 0 along all N, not only along a subsequence."

**F8. MINOR. Redundant minimum in Cor 6.1.**
*Location:* Cor 6.1, l.1136, "min{K_N^{-1}, 1/3}".
*Problem:* K_N increases with N and K₂ = 4π²(π+1)²·(8/3)(17/3) ≈ 1.02·10⁴ > 3, so the minimum always equals K_N^{-1}. The display suggests otherwise.
*Fix:* write "K_N^{-1} ≤ 1−η_N ≤ min{1,128000/(log N)²}". The proof can keep its sentence, noting that K_N^{-1} < 1/3.

**F9. MINOR. Placement and wording of Remark 3.5.**
*Location:* Remark 3.5, l.628–639.
*Problem:* The remark sits after Thm 3.4 and refers to "the preceding sign argument", but the proof that precedes it (Thm 3.4) has no |a|-replacement. The argument meant is the one in Thm 3.1. "Used again in Theorem 3.4" also reads oddly after Thm 3.4.
*Fix:* move the remark to just after Thm 3.1, or replace "in the preceding sign argument" with "in the sign argument of the proof of Theorem 3.1".

**F10. MINOR. Section 4 has a single subsection; Lemma A.1 numbering.**
*Location:* l.657–870 and l.1595.
*Problem:* §4 contains only "4.1 The sharp constant". The order-of-magnitude part has no heading, while the correspondence and plan refer to "§4.1" for that part and "§4.2" for the sharp constant. In Appendix A, the only numbered lemma is "Lemma A.1" but it sits in §A.3, so "Lemma A.1(c)" next to "§A.1" invites confusion.
*Fix:* insert `\subsection{The order of magnitude}` before Theorem 4.1. Optionally give Lemma A.1 a name ("Endpoint representation").

**F11. MINOR. Appendix C stopping rule is described incompletely.**
*Location:* App. C.1 bullet 2, l.2113–2115.
*Problem:* The text says the series is "summed until the ratios … are decreasing and at most 1/2". The code (`interval_dyadic.taylor_integral`) also requires 2·(next term) ≤ 2⁻¹²⁸ before stopping. Without that condition the description guarantees a valid enclosure but no accuracy. The Laplace remainders at x = 16π are about 1.5·10⁻²² (40!/x⁴¹), and they dominate the reported widths; that is harmless but worth stating for a reader who reruns the check.
*Fix:* "…summed until the ratio of successive absolute terms is at most 1/2, after which the ratios decrease, and twice the next term is below 2⁻¹²⁸; the tail is then bounded by twice the next term." Optionally add after the Laplace bullet: "(At x = 16π these remainders are below 2·10⁻²², which dominates the final interval widths.)"

**F12. MINOR. Hypothesis on f in Prop 8.2.**
*Location:* Prop 8.2, l.1341–1356.
*Problem:* 𝓛_n f uses point values and E_k(f) uses ‖·‖_∞, but the class of f is not stated.
*Fix:* "Let Ω be compact, μ a finite positive measure on Ω, …, and f ∈ C(Ω)."

**F13. MINOR. Logical precision about Mastroianni–Totik.**
*Location:* l.283–288 and §7 l.1172–1175.
*Problem:* An unspecified constant M means the inequality "yields nothing explicit". It does not follow that it yields "nothing" (if M < 2/π it would say something qualitative).
*Fix (l.1173–1175):* "…yields no explicit information beyond this, because its sampling constant is unspecified (Section 1)."

**F14. MINOR (optional). Overlap count in Lemma 4.8.**
*Location:* App. A.1, l.1506–1507.
*Problem:* k ∈ 𝒥_j exactly when log₂k − 2 < j < log₂k + 1, so each k lies in at most **three** sets, not four. "At most four" is true and the constants stay valid. With three, the pole part is ≤ √3·π and the comparable part ≤ (729 log 2)^{1/2} < 23.
*Fix:* none required. Either keep "four" or write "at most three (we use four)".

**F15. MINOR. Notation overloads a referee will notice.**
*Problem:*
- K: the constant K_N, the filter K(t) in §7, K(ϖ) in Lemma C.1, and 𝒦(t,k) in A.1.
- H: H_s, H(t,j) in §7, and 𝓗 in Lemma C.1.
- δ: N−n in Thm 3.2, 2^j in A.1, and the cutoff in A.4.
- σ: σ_N and σ_± in A.4.
- u: u_N in Thm 3.4, the Schur weights u_j in Thm 4.1, nodal data, and u, v in Lemma B.2.
- M: the matrix M, M₀ in Thm 4.3, and the Mastroianni–Totik constant.
- J: ⌊N/2⌋ in Thm 4.6, and the trial dimension in §5 and App. C.

*Fix (suggested renames):* I(ϖ), K(ϖ) in Lemma C.1 → I₁(ϖ), I₂(ϖ); the filter K → 𝒦_{N,n} or F^{(N,n)}; H(t,j) → 𝓗(t,j) or Ψ(t,j); δ = N−n → d₀; u_N → υ_N; the Schur weights u_j → φ_j.

**F16. MINOR (presentation). Theorem 3.1 depends forward on Theorem 3.2.**
*Location:* Thm 3.1 proof, l.490–494; Cor 3.3 proof, l.537–538.
*Problem:* Thm 3.1's displayed constant is exactly Cor 3.3, proved from Thm 3.2. The logic is not circular, but the order reads backwards ("This proves the endpoint refinement used in Theorem 3.1").
*Fix:* either state Thm 3.1 without the explicit constant (strict threshold and positivity only) and let Cor 3.3 carry 2−4/N+4/N², or put Thm 3.2 first.

**F17. TYPO.**
*Location:* §8, l.1298–1299.
*Problem:* "An and Wu assume … in its main theorem. Its Section 4 assumes…"
*Fix:* "…in their main theorem. Their Section 4 assumes…"

**F18. TYPO.**
*Location:* §4.1 heuristic, l.883–886.
*Problem:* "…the CC energy becomes π² log N times an L² norm and the continuous mass becomes 2(log N)³ times the L² norm of the primitive" — both are *squared* norms.
*Fix:* "…times a squared L² norm … times the squared L² norm of the primitive…"

---

## What I verified as correct

**§2 (Lemmas 2.1–2.3).**
- Weights (2.2): positivity via (2.6), the endpoint weights, aliasing, and the mass and defect matrices.
- Sign of D: positive exactly when i+j > N is even (n < N).
- Maximal exactness (1.4).
- Lemma 2.2: the row sums (Mb)_i = k_i/(k_i²−i²) were checked in exact rationals for N = 5, 6, 11, 12. The identity behind the lower bound, the upper bound M ⪯ (π/2)E, and the eigenvalue check of E/N ⪯ M ⪯ (π/2)E for N ∈ {2,3,4,5,8,9,16,33} are also correct.
- Lemma 2.3: tail bounds, the (2/3) sin θ_j error including N = 2, the inequalities π/2 − 2/3 ≥ 1/2 and π + 4/3 < 5, and w_j ≥ m_j/N². The §1 claim ½Δ_N ≤ w_j ≤ 5Δ_N holds.

**§3.**
- Thm 3.1: the signs of A, inequality (3.1), the |a| → v argument, and positivity.
- Thm 3.2: r − d ≥ 2δ, d/r ≤ t, and the sign of (A_ρ)_{ij}.
- Cor 3.3 is correct.
- **Thm 3.4, line by line:**
  - the identity R = M − Y + Z (numerically to 1e−15 for N ≤ 33);
  - Y ⪰ 0 via the moment integral ½∫x^{2N−2−i−j}(1−x²) = 1/(r²−1);
  - Z entries ≤ 1/(u_N²−1) with u_N even;
  - at most ⌈N/2⌉ nonzeros per row;
  - the bound on a^TZa, and the use of Lemma 2.2;
  - β_N in both parities (exact rationals), β_N ≤ 2/3, and limsup ≤ 3/2.
- Remark 3.5's arithmetic is correct.
- Remark 3.6: the 2×2 minor −D_{ij}² for N ≥ 5, and the quotient 2(4N²−1)/(4N²−2) for T_N.
- Measured spectra for N ≤ 33 satisfy all the bounds.

**§4.**
- Thm 4.1: the cardinal formula (checked against Chebyshev reconstruction to 1e−13). The bounds sin θ ≤ 2 sin((θ+θ_k)/2), (4.3) and (4.4) are correct, as are the weighted Schur test, h_N, 2H_{⌊N/2⌋+1}, and K_N.
- Lemma 4.2: ∫U_{N−1}² = 2S_N and Q_N(U_{N−1}²). In exact rationals: S₅₇ > 3, S₅₈ > 3·58²/(58²−1), q₅₆ > 1/3 (also q₅₅ > 1/3), and q_N < 1/3 for every N in 57…2999. The monotonicity argument covers all N.
- Thm 4.3:
  - the witness has degree N−1, parity N−1 and zero endpoint values;
  - identity (4.6) (numerically to 1e−14);
  - the geometric and Abel bounds;
  - |𝓑| ≤ π+1 and 𝓐 ≤ 2 + log(π/(2θ)), checked on a grid, where max |𝓑| was 1.85;
  - (4.8) using 3 + log π < 5;
  - (4.9) with 125H_{⌊N/2⌋};
  - for L ≥ 128: the inequality (a−b)² ≥ a²/2 − b², X₁ ≥ L/8 including the integration-by-parts bound N^{-1/2}, X₂ ≤ L, L² ≥ 12800, and 250·512 = 128000;
  - the case L < 128 and √128000 ≈ 357.77.
- **Lemma 4.4 (Volterra):** the Riccati identity, the boundary terms, density, and equality at sin(πx/2), giving the value π⁴/8.
- **Prop 4.5:**
  - the T_N coefficient N⁻¹Σa_k/c_k vanishes because a_{N−k} = −a_k;
  - the weight asymptotics, with relative error O(N^{2σ₊−2} + N^{−σ₋}), and the sum–integral comparison via total variation;
  - |S − LF| ≤ C_f N^{−σ₋};
  - the Jacobian lower bound on I_δ and the oscillation averaging (integration by parts gives O(N^{−δ}));
  - ‖p_N − P_u‖ = O(L) = o(L^{3/2}), and the final variational limit.
  - Numerically (`c9.py`, f = sin²-bump on (0.1, 0.9)), at N = 2001 and 8000:
    - Q_N/(2π²L‖f‖²) = 0.997 and 0.999;
    - ∫p_N²/(4L³‖Vf‖²) = 1.18 and 1.11 (decreasing towards 1 from above, consistent with liminf ≥ 1);
    - ‖p_N − P_u‖/‖u‖_w ≈ 0.77, far below the bound 80 + 6√(L+1).
- **Thm 4.6 given (4.14):** α_J/L → 2/π, σ_N/L → 2√2/π², τ_N/L → 0, and restriction for the Π_N statement.
- Cor 4.7: the bijection and the identity ‖𝓘_N‖² = 1/λ₋(N,N).
- **Lemma 4.8, line by line:**
  - the sinc orthogonality and isometry, and the dyadic split (Φ-split);
  - pole part ≤ 2π < 7;
  - comparable scales: |Ψ_k| ≤ 9/(2t), Σk ≤ 12t², the factor 243, and (972 log 2)^{1/2} = 25.96 < 32;
  - separated scales: the bounds 4/3(k/t)², row sums ≤ 1/3 and ≤ 1/2, column integrals = 1/3, Schur norm < 1;
  - total 40, hence 1600.
  - A discretized operator-norm estimate (K = 48 modes) gives a ratio of about 2.45, far below 1600.
- **Lemma 4.9, line by line:** ‖S̄ − F‖² = Σ|g_m|²/(3m³), the rescaled Volterra bound, the cell integral ≤ 1/(2m) + 1/(4m²), |S_m|² ≤ H_m‖g‖²_h, 2ζ(3/2) = 5.22 ≤ 6. Discretized suprema for T = 16, 64, 256 were 2.28, 4.55 and 7.60, all within the bounds 6.47, 9.58 and 13.50, and they match (2H_J/π)²/2 asymptotically, so the leading coefficient is the right one.
- **Lemma A.1:**
  - (a) the 3/N² bound and Σw⁻¹ ≤ 2N²(L+1), checked numerically;
  - (b) the cotangent identity, Υ_u, e(z) odd and nonincreasing, max |e| on [−π, 3π/2] = 1 + 4/(3π) = 1.4244 (numerically confirmed), and the r_u bound (observed max |r_u|/‖u‖_w ≈ 0.02 against the bound 7.1 at N = 201);
  - (c) the near-part identity with 𝓔g, the measure bound π²t dt/N², the factor 80, the far-part bound 32/(5π) ≤ 3, 9π²/32 = 2.776 < 3, the reflection with the factor (−1)^N, and the assembly 80 + 2√(L+1) + 4√(L+1). The sign convention was confirmed numerically for both parities (`c9.py`).
- **A.5, finite bound (4.14):**
  - 1 < k₀ ≤ k* < N/4 for L ≥ 16;
  - N²w_k/k ≥ π²(1 − 2/L²), using π²/6 + 3/π² = 1.949 ≤ 2;
  - good layers via Lemma 4.9 with T = N/2;
  - microscopic layers via Lemma A.1(c) with the same k*, H_{k₀}, and the endpoint columns (L + π²/2 ≤ L + 5);
  - the bulk trapezoidal identity, including the −(π/2)|b_N|² term;
  - assembly ≤ σ_N + τ_N.

**§5 and Appendix B.**
- χ_j formula (5.1), χ_j(0) = −2(−1)^j, χ_j(πk) = δ_{jk}, and the Q formula on 𝒱₀.
- p_{N,j} ∈ Π_{N−1}.
- **Prop 5.1:**
  - exact factorization (B.1) and 0 ≤ φ ≤ 3π³/(8√2) = 8.22 < 9;
  - |χ_j| ≤ 4 and |χ_j| ≤ 3ϖ_j²/ξ³, with domination by 81ξ(Σ|u_j||χ_j|)²;
  - Riemann sum for N²w_j: per-term error b²/(4N(4r²−1)) verified, and max |F′|/b³ = 0.0675 ≤ 1/12;
  - integration by parts to (−1)^j + πj Si(πj); N²w_j → ω_j verified numerically at N up to 4001, both parities;
  - positivity, Λ_edge ≤ 5/3, the liminf, and the ζ_j asymptotics giving Λ_edge ≥ 1.
- **Lemma B.1:** dilation isometry and continuity, mollification, the cosine series, C² convergence, and the two integration-by-parts bounds.
- **Lemma B.2:**
  - coefficients a_i = g(i/N) with a₀ = g(0)/2;
  - N²Z → z uniformly, and the Y corner via |g| ≤ C(1−s)² and the factor 3/4;
  - continuum identity: checked numerically for a 4-term g with dblquad, Q = 12.92332451 against M + ½(Z − Y) = 12.92332453; finite-N a^TZa → Z/2 and a^TYa → Y/2 at N = 200, 800;
  - |Z| ≤ ‖g‖² ≤ M, Y ≤ 3M, extension to 𝒱 (Laplace and sampling arguments), and Λ_edge ≤ 3/2.
- **Thm 5.2:**
  - profiles, (B.4) with the cell errors and the odd half-cell bound, and (B.5);
  - the compact Z part;
  - the exact sinh formula (checked numerically to 1e−15 at N = 200, 800) and Fatou with the parallelogram identity;
  - the conclusion, which uses Λ_edge ≥ 1.
- Agrees with record S2-qualitative-limit §1–5; the paper contains every step the record has.

**Appendix C and Prop 5.3.**
- **Lemma C.1:** the I(ϖ) partial fractions, the evenness of 𝓗, translation, I = −Cin(2ϖ)/(2ϖ²), the integration by parts for K(ϖ), Si(2ϖ)/ϖ, the diagonal decomposition, M_ij and M_jj. The closed forms match direct quadrature for (1,1), (1,2), (2,3), (3,3), (1,5), (4,7) to 1e−8, the quadrature tolerance.
- Si/Ci auxiliary-function identities, F′ = −G, G′ = F − 1/x, and the remainder signs and bounds.
- The code agrees with the described reduction (Q_J = diag ω + 4ss^T; c_ij formula).
- **Rerun:** `python3 code/P4_rayleigh.py --trial evidence/P4-trial-J512.json --output /tmp/ref-math/P4-rerun.json` took 4.4 s. Quotient enclosure [1.004436918864667280457774, …779], threshold pass True, and numerator, denominator and quotient identical to the committed receipt.

**§6–8.**
- Cor 6.1: identity (6.1), the two-sided bound, N ≥ 57, the limits, and the intervals: 8/π⁴ = 0.0821279, 12/π⁴ = 0.1231918, 8·1.0044369/π⁴ = 0.0824923 ≥ 0.08249.
- Thm 7.1, line by line: the Fejér identity and the filter coefficients, the exactness of the reconstruction (|l−k| < 2N), the bound C₀ = 2(1+π)², the Lipschitz property of ν, the shell count, Γ_r and Γ_c, and the constants 3N and C_* = 12(1+π)⁴(1+2/π).
- Cor 7.2 is correct.
- Prop 8.1: S₈ = 2.0218 > 2.01, e ≤ 87/32, (11/4)⁴ = 57.19 < 1025/17 = 60.29, 4·512²/(512²−1) = 4.0000153 < 4.01, and q₅₁₂ = 0.24385 < 1/4.
- Prop 8.2 is correct apart from F12.
- (8.3)–(8.4): threshold (1+√(2/3))/2 = 0.908248…, 1+√(5/3) = 2.2909944 < 2.2910, and k ≤ min(n, d_N − n). For N = 512, n = 511, k = 2 is allowed.

**§1 restatements.**
- Thm 1.1 = Thm 3.2 + Thm 3.4 + Remark 3.6, with the same scope (n<N, N ≥ 2, ρ_{N,n} with max).
- Thm 1.2 = Thm 4.6 + Thm 4.1 + Thm 4.3 + Cor 4.7. "Equivalently" is correct here because both limits are stated.
- Thm 1.3 = Thm 5.2 + Prop 5.3; the only issue is the operator wording, see F5.
- Cor 1.4 (1) = Cor 6.1, (2) = Cor 7.2, (3) = (8.4).
- The abstract is the only place with mismatches (F3, F4, F5).

**§9.** Table 1 rows N = 40, 80, 160, 320 were recomputed independently, from my own CC weights and Chebyshev pencil. They agree to all 9 printed decimals, and the (log N)²λ₋ column agrees as well.

## Scripts and reruns

The scripts are in `/tmp/ref-math/` and are not durable: `c1.py` (scalars and exact S_N, β_N), `c2.py` (matrices and decomposition), `c3.py` (ω_j limits, closed forms, Galerkin), `c4.py` (cardinal formula, r_u, e(z), witness), `c5.py` (continuum identity, sinh formula), `c6.py` (Table 1), `c7.py` (row sums, operator-norm sanity), `c8.py` (Galerkin J up to 2048), `c9.py` (trial family and P_u). The `c9.py` run at N = 30001 ran out of memory; the N = 2001 and 8000 results are reported above. All other runs completed.

## Remaining uncertainty

- The literature characterizations in §1 and §8 (An–Wu, ASV, Mastroianni–Russo and the others) were not checked against the sources. That is outside this mathematical remit.
- The float Galerkin values for J ≥ 1024 in F1 are float64 measurements. The accuracy estimate is about 1e−10, based on cond(M_J) ≈ 4·10³ and the cancellation analysis of the off-diagonal formula. They are uncertified, but the nesting makes the J-sequence nondecreasing, so the conclusion of F1 does not depend on their last digits.
- The 1.35·10⁻¹³ Legendre/Chebyshev agreement claimed in §9 was not rerun.
