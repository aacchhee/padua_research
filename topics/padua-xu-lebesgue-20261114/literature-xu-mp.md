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
