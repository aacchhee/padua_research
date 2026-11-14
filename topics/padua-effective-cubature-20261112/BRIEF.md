# BRIEF — making Theorem A effective; registering the Padua Lebesgue-constant corollary

Written by Claude (claude-opus-5-5), 2026-11-12. AC: "I'd like a Claude topic on making theorem A effective. You may also register Lebesgue corollary on the same. Open a branch, write a brief, another Claude thread will continue then."

This file is a knowledge base and plan. It carries no status. Literature items below are pointers: cite each only after a fulltext read, unless an existing LIT record already covers the exact statement.

## Part 1 — Theorem A and where it is non-effective

### 1.1 The statement

[`topics/padua-3d-20261106/final-d1/spectral-obstruction.md`](../padua-3d-20261106/final-d1/spectral-obstruction.md) (PR #33). Status: PROVED with an explicit LITERATURE dependency (Greenfeld–Lev Thm 1.1, LIT-659).

> There exist γ > 0 and n₀ such that every positive cubature rule with all nodes in the closed cube [−1,1]³, exact on Π_{2n−1} for normalized product Chebyshev measure μ, with n ≥ n₀ and N distinct nodes, satisfies N ≥ (1+γ)·binom(n+2, 3).

**Consequence.** No positive "Padua-package" rule (N = binom(n+3, 3), exactness 2n−1) exists once n > max(n₀, 3/γ). Neither γ nor n₀ is known.

### 1.2 The proof chain, and the steps that are not effective

1. **D1-01, [finite-frame.md](../padua-3d-20261106/final-d1/finite-frame.md): effective and exact.**
   - Lift the rule to the torus 𝕋³ by coordinate sign orbits, with stabilizer-corrected masses v_j. The lifted rule is exact for characters with |k|₁ ≤ 2n−2, and has M ≤ 8N atoms.
   - With A_n = {|k|₁ ≤ n−1}, m_n = |A_n| and D_n(t) = Σ_{k∈A_n} e^{ik·t}, the leverages are q_j = m_n v_j ≤ 1 and η_j = 1 − q_j. They satisfy Σ η_j = M − m_n and Σ_{l≠j} v_j v_l |D_n(t_j − t_l)|² = q_j η_j.
   - There is a squeeze from N/binom(n+2, 3) → 1 to M/m_n → 1.
2. **D1-02, [stationary-limit.md](../padua-3d-20261106/final-d1/stationary-limit.md): NOT effective.**
   - It removes high-leverage atoms, rescales by n/(2π), and passes to a limit of translation-invariant laws.
   - The tools are Arzelà–Ascoli diagonal compactness and the representation of positive functionals. This produces a stationary law of separated sets whose exponentials are orthogonal in L²(O), O = {|u|₁ ≤ 1}, with mean intensity |O|.
3. **D1-03, [complete-law.md](../padua-3d-20261106/final-d1/complete-law.md): qualitative.** Orthogonal at intensity |O| almost surely means complete, so O would be spectral.
4. **Greenfeld–Lev Thm 1.1 (LIT-659): qualitative.** A spectral convex polytope has centrally symmetric facets. The octahedron's triangular facets are not centrally symmetric, so O is not spectral. Contradiction.
5. **Assembly:** the contradiction argument (D1-04) gives existence of γ and n₀ only.

**Making the theorem effective means making steps 2–4 quantitative,** or replacing them by a direct finite-n argument.

### 1.3 Facts that constrain any effective statement

- **Small degrees.** Exact Padua-type positive packages exist at n = 1, 2 (lattice classification, `theory/r08-lattice-complement.md`). A 20-node positive degree-5 rule that is Π₃-unisolvent exists at **n = 3** (D3, `final-d3/theory.md`, PROVED).
  - So any claim "no package for all n ≥ n₀" needs n₀ ≥ 4. Any finite-degree exclusion must be consistent with D3.
  - **An effective theory should aim to determine the exact set of degrees where a positive package exists:** {1, 2, 3, …?}.
- **The zero-phase lattice class is already settled finitely** (`r08-lattice-complement.md`, `r08-lattice-higher.md`; computer-assisted PROVED):

  | n | 3 | 4 | 5 |
  |---|---|---|---|
  | minimal full-rank folded count | 24 | 45 | 75 |
  | required N | 20 | 35 | 56 |

  At n = 6 and 7 every positive rule with at most 84 or 120 nodes is excluded. These results are for lattice rules only, not for arbitrary nodes.
- **Expected size of the excess.** The conjectured sharp excess (Li–Sun–Xu, signed weights allowed) is N ≈ n³/4, against binom(n+2, 3) ≈ n³/6, so γ ≈ 1/2. DMVX parity-grid rules attain about n³/4. Any effective γ must lie in (0, 1/2]. The frontier scout S4 mentions a "lattice value 1/18" for a related constant; reconcile or discard it.

### 1.4 Route E1 — the Delsarte linear-programming bound, connected to Turán's problem (main route)

This is the classical way to get **effective** lower bounds for cubature and designs: Delsarte; Yudin for spherical designs (LIT-669, secondary); Lyubich for projective cubature (LIT-668, primary-read by the D1b auditor; it shows that positive projective cubature asymptotically exceeds the Fisher-type LP bound by a factor 1/κ > 1).

**The finite inequality.** Take the lifted torus rule: positive masses v_j, Σ v_j = 1, exact on |k|₁ ≤ 2n−2. For any real trigonometric polynomial f(t) = Σ_k c_k e^{ik·t} with:
- spectrum in {|k|₁ ≤ 2n−2},
- f ≥ 0 on 𝕋³,

we have Σ_{j,l} v_j v_l f(t_j − t_l) = Σ_k c_k |Σ_j v_j e^{ik·t_j}|² = c₀, since exactness kills every k ≠ 0. Dropping the off-diagonal terms, which are ≥ 0, gives f(0) Σ_j v_j² ≤ c₀. With Σ_j v_j² ≥ 1/M this gives

  M ≥ f(0)/c₀.

- f = |D_n|² recovers the Fisher-type bound M ≥ m_n.
- **Any f beating |D_n|² gives an effective, explicit excess at that n.**
- The same inequality, applied directly to μ-cubature on the cube with nonnegative polynomials of degree ≤ 2n−1, is an alternative that avoids the factor-8 lift. Choose whichever is sharper, and track the M ↔ N conversion exactly via the stabilizers.

**The asymptotic problem is a Turán problem.** Rescale by n. Nonnegative f with spectrum in 2nO becomes F ≥ 0 on ℝ³ with F̂ supported in 2O = O − O. The ratio becomes F(0)/F̂(0) = ∫G / G(0) with G = F̂, a positive-definite function supported in 2O.

- **Turán's problem:** T(K) = sup { ∫G : G positive definite, supp G ⊂ K, G(0) = 1 }.
- G = 1_O ∗ 1_O / |O| gives T(2O) ≥ |O|, which is the Fisher bound.
- **The effective γ_LP is T(2O)/|O| − 1, if that is positive.**

**Known results on Turán's problem** (verify every one; these are Claude's recollection, not records):
- equality T(K) = |K/2| holds when K/2 tiles (Arestov–Berdysheva);
- or when K/2 is spectral (Kolountzakis–Révész, Proc. AMS 2003, "On a problem of Turán about positive definite functions");
- and for the ball (Siegel; Gorbachev).

Whether strict inequality holds for the octahedron, which neither tiles nor is spectral, is the question. **Claude does not know the answer.**

**If T(2O) = |O|, the LP gives no fixed-fraction gain, and route E1 is killed for γ.** Theorem A would then be strictly stronger than LP, which is possible: LP is a relaxation. In that case E1 can still give effective finite-n excesses from lower-order terms. Those may suffice to exclude packages at small n, because the target there is only 1 + 3/n.

**Strengthenings beyond plain LP**, if needed:
- **Cohn–Elkies style:** use f ≤ 0 off a forbidden-difference region. Here separation of the near-critical atoms, of order 1/n (S4), supplies forbidden differences.
- **Second-moment / three-point (SDP) bounds.**
- **Exploit the leverage identity** Σ_{l≠j} v_j v_l |D_n|² = q_j η_j rather than discarding the off-diagonal terms.

### 1.5 Route E2 — quantitative compactness (alternative)

Make D1-02 and D1-03 quantitative with explicit error terms:
- kernel convergence rates;
- explicit removal of high-leverage atoms;
- window counts with explicit Beurling–Selberg majorants.

Then prove a **quantitative non-spectrality of O**: an explicit δ₀ > 0 such that no uniformly separated, approximately orthogonal exponential system on L²(O) has density ≥ (1 − δ₀)|O|.

Greenfeld–Lev's proof structure (facet-normal asymptotics of the Fourier transform of 1_O and its zero set) is the place to look. Lev–Matolcsi (LIT-660) and Kolountzakis (LIT-662, a quantitative compactness precedent for packings) are adjacent. This route is likely to give very small constants, but any explicit γ is a result.

### 1.6 Route E3 — finite-degree certificates

For n = 4, 5, …, n₁, solve the finite Delsarte LP of §1.4 numerically, then certify a rational dual f exactly (exact or outward arithmetic, an independent checker). This gives an explicit lower bound N ≥ L_n for **all** positive rules with nodes in the closed cube, not only lattice rules.

**Target:** decide, degree by degree, whether a positive degree-(2n−1) rule with N = binom(n+3, 3) can exist. The D3 package at n = 3 is the calibration: any certificate claiming exclusion at n = 3 is wrong.

### 1.7 What a good outcome looks like

In decreasing strength:
1. explicit γ and n₀, with finite certificates closing every n with 4 ≤ n < n₀ that the asymptotic bound does not cover. That would give the exact list of degrees with a positive package, presumably {1, 2, 3};
2. explicit γ and n₀ only;
3. certified finite exclusions for n = 4…n₁;
4. a proof that the LP route cannot give fixed γ (T(2O) = |O|), which is itself a Turán-problem result for the octahedron.

## Part 2 — the Padua Lebesgue-constant corollary (register in this topic)

### 2.1 Statement to register

Λ(Pad_n) := max_{[−1,1]²} λ_n, using exactly the conventions of PD-T101 (even-checkerboard Padua points, total-degree cardinal functions).

- **(i)** For every n with 2 ≤ n ≤ 32, and for every n ≥ N_*, Λ(Pad_n) = Λ_c(n), the exact corner value of PD-T101. The maximum is attained exactly at the two parity-correct non-node corners.
- **(ii)** Consequently, for every n ≥ max(32, N_*), with N = n + ½,

  Λ(Pad_n) = (4/π²) log² N + b log N + c + R_n,

  where b and c are PD-T271's constants (c ≈ 1.846160310423926…, with the decimal enclosures given there) and |R_n| obeys PD-T271's explicit bound (1). In particular Λ(Pad_n) − (4/π²) log² N − b log N → c.

### 2.2 Dependencies (all on main)

- **PD-T229** (eventual argmax, N_* non-effective);
- **PD-T246**, together with PD-T209/162/166/169/174/177/181/214 for the finite range 2–32;
- **PD-T101** (the corner value);
- **PD-T271**, with PD-T269/270.

### 2.3 Scope and wording

- **Part (ii) is unconditional as an asymptotic statement:** non-effective in where it starts, effective in the size of its error.
- **PR #27** (the argmax bridge, open draft) would extend (i) to 2 ≤ n ≤ 40 and make N_* effective, ⌈exp(10¹²)⌉. Do not use PR #27 as a dependency while it is unmerged. Add a dated note when it merges.
- **Priority wording.** The merged literature comparison (`topics/padua-literature-20261103/p1-comparison.md`, LIT records) finds only the leading term published: Kolomoitsev–Lomako 2021, Λ_n^Pad = (4/π²) log² n + O(log n), with pointwise O(log n) work going back to Kuznetsova 1995. The second and third terms are new **as far as the documented search goes**. Use that comparison's proposed sentences, not a stronger claim.
- **Novelty gate:** IDEA-206 and the argmax entries. This is a corollary assembly, not a new mechanism, so state that in the gate.

## Part 3 — reading list

Read fulltexts before citing. Give AC clickable links for anything paywalled.

- **Theorem A chain:** `topics/padua-3d-20261106/final-d1/` (all files), `final-check/d1-audit.md`, `audit-05.md`, `response-05.md`. Sources: LIT-659 (Greenfeld–Lev), LIT-660 (Lev–Matolcsi), LIT-662 (Kolountzakis), LIT-663 (Kuperberg), LIT-664 (AMO), LIT-668 (Lyubich), LIT-669 (Yudin).
- **Delsarte, Turán, LP bounds:**
  - Delsarte–Goethals–Seidel 1977;
  - Yudin 1997 (spherical designs);
  - Kolountzakis–Révész 2003 (Proc. AMS) and their later group-setting paper;
  - Arestov–Berdysheva (hexagon/tile Turán);
  - Gorbachev (ball Turán; extremal problems with positive definite functions);
  - Cohn–Elkies 2003 (sphere-packing LP);
  - Y. Xu 2003, J. Complexity 19 (ball cubature lower bound; snippet-level only so far).
- **Cube cubature context:**
  - Möller's lower bound;
  - Li–Sun–Xu (arXiv 0808.0180);
  - De Marchi–Vianello–Xu (arXiv 0805.3529).
