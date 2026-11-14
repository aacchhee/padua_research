# Literature and conventions — Xu points (X1) and Morrow–Patterson points (X2)

Orchestrator: Claude (Opus 5.5), 2026-11-14. Detailed source notes, reading coverage, search logs and published numbers are in [lit-notes/X1-sources.md](lit-notes/X1-sources.md) and [lit-notes/X2-sources.md](lit-notes/X2-sources.md) (Opus 5.5 readers, finalized by the orchestrator). This file fixes the conventions used by code and theory and records the literature verdicts that change the BRIEF's targets. No PDFs or extracts are committed; fulltexts were read from AC's `Downloads\padua\papers` (staged, not committed), open author copies, and ScienceDirect HTML via AC's institutional browser.

## 1. Conventions (Xu points)

Source: Xu, JAT 87 (1996) 220–238, §2 (journal PDF), with the kernel index correction of BCDMV (Computing 76 (2006) p. 313); see X1-sources §8 for locators and flags F1–F5.

- z_k = cos(kπ/n), k = 0..n. X_n = {(z_a, z_b) : 0 ≤ a, b ≤ n, a + b ≡ n + 1 (mod 2)}; |X_n| = n(n+2)/2 (n even), (n+1)²/2 (n odd).
- V_n = Π_{n−1} ⊕ span{T_{n−j}(x)T_j(y) − σ T_j(x)T_{n−j}(y) : 0 ≤ j < ⌈n/2⌉}, σ = +1 (n even), σ = −1 (n odd). dim V_n = |X_n|.
- ℓ_ξ = K*_n(·, ξ)/K*_n(ξ, ξ), K*_n(x, ξ) = ½[K_n + K_{n+1}](x, ξ) − ½(−1)^r (T_n(x₁) − σ T_n(x₂)) for ξ = (z_r, z_s), where K_d reproduces Π_{d−1} for the product Chebyshev weight of the first kind (orthonormal normalization) and T_n is unscaled.
- Vertices: for n even no vertex is a node; for n odd, (1,1) and (−1,−1) are nodes and V* = {(1,−1), (−1,1)}.
- Conjecture (17) of BCDMV (p. 319) is stated in an even-n setting (BdMV, BCDMV and the ETNA survey treat even n). The X1 targets are therefore stated for even n with V* = all four vertices; odd n is studied as a separate, explicitly labelled variant with V* = {(1,−1), (−1,1)}.

### 1.1 Symmetries used by the G1 screen (orchestrator proof)

**Lemma S.** Let g be a linear isometry of the square, i.e. a composition of x ↦ −x, y ↦ −y and (x, y) ↦ (y, x). If g(X_n) = X_n and V_n ∘ g = V_n, then λ_n ∘ g = λ_n.

*Proof.* The interpolation projector L at X_n onto V_n is unique (unisolvence). For f ∈ C(Q), the function (L(f∘g))∘g⁻¹ lies in V_n, because V_n is invariant under composition with g⁻¹. It interpolates f at g(X_n) = X_n. Hence L f = (L(f∘g))∘g⁻¹, so ℓ_ξ∘g = ℓ_{g⁻¹ξ}. Summing |ℓ_ξ(g x)| over ξ ∈ X_n is therefore a sum over the permuted node set, which gives λ_n(gx) = λ_n(x). ∎

Invariances (T_k(−t) = (−1)^k T_k(t); Π_{n−1} is invariant under every g):
- **n even.** a ↦ n − a preserves the parity of a + b (n even), and so does the swap. On the extra functions, x ↦ −x multiplies both terms by (−1)^j = (−1)^{n−j}, and the swap maps each function to −σ times itself. Hence **λ_n is invariant under the full dihedral group of the square**.
- **n odd.** The swap and (a, b) ↦ (n − a, n − b) preserve a + b mod 2; x ↦ −x alone does not. On the extra functions, (x, y) ↦ (−x, −y) multiplies by (−1)^n, and the swap by −σ = +1. Hence **λ_n is invariant under (x, y) ↦ (y, x) and (x, y) ↦ (−x, −y)**.

## 2. Conventions (Morrow–Patterson points)

Source: Beberok–Białas-Cież–De Marchi, Constr. Approx. 63 (2026) 31–65 (published PDF), and Beberok, JAT 311 (2025) 106191 (HTML fulltext); details in X2-sources.

- n even. x_m = cos(mπ/(n+2)), m = 1..n+1. y_k = cos(2kπ/(n+3)) for m odd and cos((2k−1)π/(n+3)) for m even, k = 1..n/2+1. |MP_n| = dim Π_n. MP_n = Pad_{n+2} minus its edge points.
- ℓ_{m,k}(x, y) = ω_{m,k} Σ_{i+j≤n} U_i(x_m)U_j(y_k)U_i(x)U_j(y), with 1/ω_{m,k} = Σ_{i+j≤n} U_i(x_m)² U_j(y_k)². Equivalently, in the published form, weights 8 sin²w_m sin²v_k/((n+2)(n+3)) times the kernel.
- **Symmetry.** BBDM Lemma 15: λ_n(x, y) = λ_n(−x, y) (also from Lemma S). The node set is *not* invariant under (x, y) ↦ (−x, −y): the image of a node with m odd has an odd numerator in its y-angle, which is the even-m pattern.

## 3. Literature verdicts that change the targets (2026-11-14)

1. **X2 lower bound is already published.** Beberok, "A lower bound for the Lebesgue constant of the Morrow–Patterson points", JAT 311 (2025) 106191 ([doi](https://doi.org/10.1016/j.jat.2025.106191)), Theorem 0.1: Λ_MP(n) ≥ c n² for an existential c. The proof works at the point (1,1). It gives a closed form for the kernel at (1,1), eq. (2), and its final display yields, for n ≥ 8, Λ_MP(n) ≥ (√3−1)²(n/4−1)(2n+5)(n+2)(n+3)/(16π²(3n/2+2)²), a constant of about 7.5·10⁻⁴. BRIEF target X2.1 is therefore **LITERATURE, not new**. Any X2 result must go beyond it: a sharp constant, the exact corner values, or the argmax location.
2. **BBDM's stated open problems** (Constr. Approx. 63 (2026), §7 p. 63 and §7.1 p. 64):
   - prove λ(x, y) = λ(−x, −y);
   - prove that the Lebesgue constant is attained at each corner.

   Their numerics report the corner values as (n+1)(n+2)/2. The readers' numerics, still to be reproduced under G0, contradict both statements: λ(±1, −1) = n + 1 and λ(±1, 1) ≈ 1.033·(n+1)(n+2)/2. The asymmetry is consistent with §2 above. A certified negative answer, plus exact corner values, is a clean target.
3. **"MPX" variants.** BBDM, CDMV 2005 and Białas-Cież–De Marchi–Suder do not define them, so LIT-378's "MPX open" clause is a secondary-source artefact. BRIEF target X2.3 is dropped unless a defining source is found (Xu, JAT 164 (2012) and JAT 214 (2017) generalize MP points; not read).
4. **X1.** The documented forward-citation search found nothing that settles either part of Conjecture (17). Kolomoitsev–Lomako's Theorem 2.1 requires n = lm + p with 1 ≤ p < m and so does not cover Xu points. The (4/π²) log² n leading constant for Xu points is not stated as known in any source read. Lower bounds c log² n with an unspecified c are reported secondhand: Szili–Vértesi 2009, Della Vecchia–Mastroianni–Vértesi 2009 and others; not read (see X1-sources §4.3, §9).

## 4. Orchestrator primary checks (2026-11-14, PDFs fetched through AC's Chrome on the NTNU network, filed in `Downloads\padua\papers`, not committed)

- **BCDMV, Computing 76 (2006), p. 319, eq. (17)** (Springer PDF, page image inspected). The conjecture says that the Lebesgue function of the Xu points can be bounded as max λ^Xu_n = Λ^Xu_n **≲** ((2/π) log(n+1))² as n → ∞, and that the maximum is attained at the four vertices of the square. The relation is "≲", i.e. an asymptotic upper bound, so flag F4 of X1-sources is resolved. The X1 target "Λ^Xu_n ~ (4/π²) log² n" therefore implies the first part of (17) and is strictly stronger. The second part is the argmax statement.
- **BdMV, JAT 141 (2006) 134–141, Theorem 1** (journal PDF): Λ^Xu_n ≤ 8((2/π) log n + 5)² + 4. This confirms the reader's reconstruction (X1-sources F5). The introduction places the Xu space in the even-n setting, with N = n(n+2)/2.
- **Della Vecchia–Mastroianni–Vértesi, Studia Sci. Math. Hungar. 46 (2009) 97–102** ([doi](https://doi.org/10.1556/SSCMath.2008.1078)). Only the abstract is accessible (NTNU has no subscription): exact order (log n)² for "two sets of nodes", which are not named there. Order only, with no constant. Not used.
- **Szili–Vértesi, JAT 159 (2009) 154–164** and **Morrow–Patterson 1978**: not obtained (download not completed; SIAM backfile not licensed). Not used.

## 5. Novelty re-gate for the X1 round-2 claims (2026-11-14)

Opus 5.5 checker; full record in [lit-notes/X1-novelty-exact-constant.md](lit-notes/X1-novelty-exact-constant.md).
- **Known method, inequality only.**
  - BdMV 2006 (proof of Thm 1, pp. 137–140) uses the rotation (θ₁ ± θ₂)/2 and enlarges the sum to a product of two 1D sums. Its leading coefficient is 32/π², nothing is said about vertices, and nothing is sharp.
  - Li–Sun–Xu, NMTMA 2 (2009), §3.3 derives Xu interpolation from rhombus-lattice trigonometric interpolation plus symmetrization. The X1-01 lift refines this. The paper has no Lebesgue statement.
  - Xu, JAT 164 (2012), Cor. 5.2: ‖L‖ ≤ (1D constant)² for a *different* (symmetric-polynomial) interpolation. Its §6.2 states that the Xu-type case "cannot be deduced" from the 1D constant, and Thm 6.6 gives only O(log² n).
- **Classical 1D facts.** The cotangent formula for L_n, the maximum at ±1, and the expansion (2/π)(log n + γ + log(8/π)) + O(n⁻²): Ehlich–Zeller 1966, Günttner 1980, Shivakumar–Wong 1982, and Smith, Ann. Math. Inform. 33 (2006) §2.2. X1-02 and X1-06 re-prove them, and X1-06's two-sided n⁻⁴ enclosure is a refinement. Neither is claimed as new.
- **Not found in the documented search**, so plausibly new:
  - the exact identity Λ^Xu_n = L_n² for both parities;
  - the exact fiber-sum lift with the pointwise bound λ_n ≤ ω_n(u)ω_n(v);
  - the maximizer set V* for every n ≥ 2;
  - hence BCDMV Conj. (17) in sharpened form.
- **Coverage limits.**
  - Xu, *Minimal Cubature Rules* (CUP 2025, [doi](https://doi.org/10.1017/9781009663939)): NTNU has no Cambridge Core access. All eleven chapter summaries were read on 2026-11-14 by the orchestrator; none mentions interpolation or Lebesgue constants. The chapter bodies are unread.
  - Della Vecchia–Mastroianni–Vértesi 2009 (abstract only: order (log n)²) and Szili–Vértesi 2009 are unread.
  - The arXiv reads were WebFetch digests.
