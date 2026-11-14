# PD-T?padua-effective-cubature-20261112-claude-02 — Delsarte LP bound for positive cube cubature, finite and continuous forms (exactness 2n−2: L = n−½; exactness E: L = (E+1)/2)

ID kind: PD-T.
Aliases: E1 Delsarte transference; torus Delsarte bound; M ≥ (n−1/2)³ D(2O); M ≥ n³D(2O) at exactness 2n−1.
Split from: none. It supports the separate records -03 (uniform Theorem A), -04 (cap) and -05 (explicit-constant target).
Split into: none.

## Statement

Fix an integer n ≥ 1. Let (x_i, w_i), i = 1…N, be a positive cubature rule with all nodes in the closed cube [−1,1]³, exact on Π_{2n−2} for the normalized product Chebyshev measure μ. (Exactness on Π_{2n−1}, as in Theorem A, is stronger.) Let M ≤ 8N be the number of atoms of its sign-orbit lift to 𝕋³ = (ℝ/2πℤ)³ (D1-01).

**(a) Finite Delsarte bound.** Let f(t) = Σ_{k∈F} c_k e^{ik·t} be a trigonometric polynomial with these properties:
- F ⊂ ℤ³ is finite;
- every c_k is real, so f is real and even when c_{−k} = c_k; reality alone is all the proof uses;
- c₀ > 0;
- f ≥ 0 on 𝕋³;
- c_k ≤ 0 for every k ∈ F with |k|₁ ≥ 2n−1.

Then M ≥ f(0)/c₀, and hence N ≥ f(0)/(8c₀).

**(b) Continuous transference.** Let φ: ℝ³ → ℝ be continuous and compactly supported, with:
- φ(0) = 1;
- φ(ξ) ≤ 0 whenever |ξ|₁ ≥ 2;
- φ̂ ≥ 0 everywhere, where φ̂(x) = ∫ φ(ξ) e^{−2πi ξ·x} dξ.

Then, with L = n − 1/2,

  M ≥ L³ ∫φ,  N ≥ (n − 1/2)³ ∫φ / 8.

**(c) Supremum form.** Let D(U) be the Delsarte constant of Kolountzakis–Lev–Matolcsi (LIT?padua-effective-cubature-20261112-claude-01, Definition 5.1) for the open set U = int(2O) = {|ξ|₁ < 2}. That is, D(U) is the supremum of ∫φ over continuous real φ ∈ L¹(ℝ³) with φ(0) = 1, φ ≤ 0 on ℝ³∖U and φ̂ ≥ 0. Then for every n ≥ 1 and every rule as above,

  M ≥ (n − 1/2)³ D(int 2O),  N ≥ (n − 1/2)³ D(int 2O) / 8.

**(d) Exactness range E (added 2026-11-12, after the session-1 numerics).** Let the rule be exact on Π_E for some integer E ≥ 0 (nodes in the closed cube, positive weights). Then the lift satisfies ν̂(k) = 0 for 0 < |k|₁ ≤ E. Statement (a) holds with "c_k ≤ 0 for |k|₁ ≥ E+1" in place of "|k|₁ ≥ 2n−1", and (b), (c) hold with L = (E+1)/2. For the Theorem A setting E = 2n−1 this gives L = n:

  M ≥ n³ D(int 2O),  N ≥ n³ D(int 2O)/8   (rules exact on Π_{2n−1}).

The case E = 2n−2 is (a)–(c) as stated above.

The definition of D is restated here in full. Only the definition is taken from the source; no theorem of KLM is used in (a)–(d).

## Definitions

- O = {ξ ∈ ℝ³ : |ξ|₁ ≤ 1}, so |O| = 4/3.
- **Lift (D1-01, PD-T?padua-3d-20261106-codex-D1-01).** Each node x_i, written as x_i = cos θ_i coordinatewise with θ_i ∈ [0,π]³, is replaced by its distinct coordinate sign orbit on 𝕋³, with mass w_i/s_i at each of its s_i points. The lifted measure ν = Σ_j v_j δ_{t_j} has M = Σ s_i atoms, Σ v_j = 1, and ν̂(k) := Σ_j v_j e^{−ik·t_j} = 0 for 0 < |k|₁ ≤ 2n−2.

## Assumptions

As in the statement. In (b), compact support is used only to make the series in the proof finite. Under (c) the regularity is removed by approximation.

## Status by part

Overall status: **PROVED** (local elementary proof; no external theorem).

| Part | Status | Evidence |
|---|---|---|
| (a) finite bound | PROVED | proof below; uses D1-01 lift exactness only |
| (b) transference | PROVED | proof below (periodization, Fourier coefficients of an L¹ function) |
| (c) supremum form | PROVED | approximation argument below; uses KLM's definition only |
| (d) exactness range E | PROVED | lift computation and the proofs of (a)–(c) with 2L = E+1 (below) |

## Depends on

- PD-T?padua-3d-20261106-codex-D1-01 (finite-frame.md), for the lift and its exactness for 0 < |k|₁ ≤ 2n−2 and M ≤ 8N. Its hypotheses are exactness on Π_{2n−2} and nodes in the closed cube. Part (d) extends the exactness statement to general E with the same computation, written out below.
- Elementary harmonic analysis: Fourier inversion for continuous φ with φ, φ̂ ∈ L¹; uniqueness of Fourier coefficients on L¹(𝕋³).

## Proof

**(a).** All series below are finite. Since |ν̂(k)| ≤ 1,

  Σ_{j,l} v_j v_l f(t_j − t_l) = Σ_k c_k Σ_{j,l} v_j v_l e^{ik·t_j} e^{−ik·t_l} = Σ_k c_k |ν̂(k)|².

Exactness gives ν̂(0) = 1 and ν̂(k) = 0 for 0 < |k|₁ ≤ 2n−2. Every remaining k has |k|₁ ≥ 2n−1, so c_k ≤ 0 there. Hence the right side is at most c₀.

On the left, every off-diagonal term is ≥ 0 because f ≥ 0. Thus f(0) Σ_j v_j² ≤ c₀. By Cauchy–Schwarz, 1 = (Σ_j v_j)² ≤ M Σ_j v_j². So f(0)/M ≤ c₀, which is the claim for f(0) > 0; for f(0) ≤ 0 it is trivial. Finally M ≤ 8N. ∎

**(b).** φ̂ ≥ 0 is real, so φ(−ξ) = φ(ξ). Moreover φ̂ ∈ L¹ with ∫φ̂ = φ(0) = 1. To see this, take the Gaussian G_ε(x) = e^{−πε|x|²}. Then

  ∫ φ̂ G_ε = ∫ φ(ξ) ε^{−3/2} e^{−π|ξ|²/ε} dξ → φ(0),

since φ is bounded and continuous at 0. Monotone convergence then gives ∫φ̂ = 1. In particular φ̂ is continuous and bounded (it is the Fourier transform of φ ∈ L¹), and Fourier inversion φ(ξ) = ∫ φ̂(x) e^{2πi ξ·x} dx holds at every ξ.

Put c_k = φ(k/L) for k ∈ ℤ³. These are finitely many nonzero real numbers, with c₀ = 1. If |k|₁ ≥ 2n−1 = 2L, then |k/L|₁ ≥ 2, so c_k ≤ 0.

Define the trigonometric polynomial P(s) = Σ_k c_k e^{2πi k·s} on ℝ³/ℤ³, and

  Q(s) = L³ Σ_{m∈ℤ³} φ̂(L(s + m)).

Q is a sum of nonnegative terms with ∫_{[0,1)³} Q = ∫_{ℝ³} φ̂ = 1, so Q ∈ L¹(ℝ³/ℤ³) and Q ≥ 0. Its Fourier coefficients are

  ∫ Q(s) e^{−2πi k·s} ds = L³ ∫_{ℝ³} φ̂(Ly) e^{−2πi k·y} dy = ∫ φ̂(x) e^{−2πi (k/L)·x} dx = φ(−k/L) = c_k.

Hence P = Q almost everywhere, by uniqueness of Fourier coefficients on L¹. Since P is continuous and Q ≥ 0 a.e., P ≥ 0 everywhere.

For a.e. s in a neighbourhood of 0, dropping the m ≠ 0 terms gives P(s) = Q(s) ≥ L³ φ̂(Ls). Both sides are continuous, so P(0) ≥ L³ φ̂(0) = L³ ∫φ.

Apply (a) to f(t) = P(t/2π) = Σ_k c_k e^{ik·t}, which has f ≥ 0 and c₀ = 1. It gives M ≥ f(0) ≥ L³ ∫φ. ∎

**(c).** Let φ be admissible in KLM's sense for U = int(2O). Fix a continuous h ≥ 0, not identically zero, supported in the unit ball. Put g = (h ∗ h̃)/‖h‖₂², where h̃(ξ) = h(−ξ). Then:
- g is continuous, g ≥ 0, supp g is compact, g(0) = 1;
- ĝ = |ĥ|²/‖h‖₂² ≥ 0 and ∫ĝ = g(0) = 1.

For R > 0 set ψ_R(ξ) = φ(ξ) g(ξ/R). Then:
- ψ_R is continuous and compactly supported, with ψ_R(0) = 1;
- ψ_R ≤ 0 wherever φ ≤ 0, in particular for |ξ|₁ ≥ 2;
- ψ̂_R = φ̂ ∗ (R³ ĝ(R·)) ≥ 0.

So ψ_R satisfies (b). Moreover ∫ψ_R = ψ̂_R(0) = ∫ φ̂(−x) R³ ĝ(Rx) dx → φ̂(0) = ∫φ as R → ∞, because φ̂ is bounded and continuous and R³ĝ(R·) is an approximate identity.

By (b), M ≥ L³ ∫ψ_R for every R. Letting R → ∞ gives M ≥ L³ ∫φ. Taking the supremum over admissible φ gives M ≥ L³ D(int 2O). ∎

**(d).** For a node x = cos θ (coordinatewise), let σ range over the 8 coordinate sign changes. The distinct points of the orbit {σθ} each have the same stabiliser size, so the lifted mass w/s spread over the s distinct points equals the average of w δ_{σθ} over all 8 σ. Hence

  ν̂(k) = Σ_i w_i (1/8) Σ_σ e^{−ik·σθ_i} = Σ_i w_i Π_{j=1}^{3} cos(k_j θ_{ij}) = Σ_i w_i Π_j T_{|k_j|}(x_{ij}).

The product Π_j T_{|k_j|} is a polynomial of total degree |k|₁. For 0 < |k|₁ ≤ E, exactness gives ν̂(k) = ∫ Π_j T_{|k_j|} dμ = 0, by orthogonality of the Chebyshev polynomials under the product Chebyshev measure; and ν̂(0) = Σ w_i = 1. (For E = 2n−2 this is the D1-01 statement.) The proof of (a) used only these vanishing coefficients and c_k ≤ 0 on the complement, so it holds with E in place of 2n−2. In (b), c_k = φ(k/L) ≤ 0 is needed for |k|₁ ≥ E+1 = 2L, which is |k/L|₁ ≥ 2; the rest of (b) and (c) is unchanged. ∎

## Checks

- **Consistency with Fisher.** φ₀ = 1_O ∗ 1_O / |O| satisfies (b): it is supported in 2O and φ̂₀ = |1̂_O|²/|O|. It gives M ≥ (4/3)(n − 1/2)³ = m_n − (5/3)n + 5/6 (checked exactly for n = 1…5), which is strictly below the exact Fisher-type bound M ≥ m_n of D1-01. So (b) loses only O(n) relative to the projection bound. Here m_n = (4n³ − 6n² + 8n − 3)/3.
- **Calibration.** At n = 3, (c) together with the cap of record -04 gives at most N ≥ (5/2)³ (38/27)/8 ≈ 2.75. This is consistent with the 20-node D3 rule (Q0c).
- **Numerical LP values.** The finite LP values of (a) (E = 2n−2) were MEASURED by `../code/lp_torus.py`; see `../evidence/lp-torus.json` and the Q1/Q2 verdicts in `../gates.md`. They are not premises of this record.

## Sources

- KLM, LIT?padua-effective-cubature-20261112-claude-01. Only the definition of the Delsarte constant (§5.2, Definition 5.1, arXiv:2510.10172v1, pp. 15–16) is used here. It was read in full text by the orchestrator on 2026-11-12.
- Delsarte's LP method for designs is the classical origin of (a): Delsarte–Goethals–Seidel 1977, cited through KLM §1. Kuperberg (LIT-663, arXiv math/0405366v2 p. 15) reports that "Xu observed that the method for t-designs also yields bounds on PI t-cubature", citing Y. Xu. Both are read at the level of these quoted sentences only. No priority is claimed for (a).

## Scope

- (a) and (b) are valid for every n. No asymptotic or non-effective step is used.
- The bound is weaker than Fisher's unless ∫φ > 4/3. Whether a φ with ∫φ > 4/3 exists is decided in record -03, with literature dependency; an explicit one is the OPEN target -05.
- Signed weights are excluded, since positivity is used in v_j ≥ 0 and in dropping the off-diagonal terms.
- Nodes outside the closed cube are excluded, as the lift requires.

## Open items

None for this record.

## History

2026-11-12, Claude (Opus 5.5 xhigh, orchestrator) wrote this record. The BRIEF §1.4 plain LP required spectrum ⊂ {|k|₁ ≤ 2n−2}. The Delsarte refinement allows higher frequencies with nonpositive coefficients, which turns the asymptotic problem from Turán's T(2O) into Delsarte's D(2O). This change was made after reading KLM 2025 (see `../literature-effective.md`).

2026-11-12, orchestrator: added (d). The records -02/-03 had used the exactness range 2n−2 throughout, as in D1-01. The lift of a rule exact on Π_{2n−1} is exact up to |k|₁ = 2n−1, which gives L = n instead of n − 1/2. Nothing earlier was wrong; (d) is a strengthening noticed while setting up the lattice witnesses of record -06.
