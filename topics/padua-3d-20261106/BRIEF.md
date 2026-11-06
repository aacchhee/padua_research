# BRIEF — Padua-type points in three dimensions

Written by Claude (claude-opus-5-5), 2026-11-06, at AC's request: "Make a proper adventurous reasoning topic on 3D, write what you know and what you expect."

This is a knowledge base and an expectations memo. It is not a result file, and nothing here carries a status.

- Every literature statement below is a pointer. Some come from partial readings and some are marked UNVERIFIED in `literature/INDEX.md`; cite each only after a fulltext read.
- Every "expectation" (§4) is Claude's judgment. It steers effort and is not a premise of anything.

## 1. The target

Find an explicit family X_n ⊂ [−1,1]³, n = 1, 2, … (or an infinite subsequence of degrees), with:

1. |X_n| = dim Π_n(ℝ³) = binom(n+3, 3) = (n+1)(n+2)(n+3)/6;
2. unisolvence for total-degree interpolation Π_n, proved for every n in the family;
3. Lebesgue constant Λ(X_n) = O(log³ n). In 2-D, Padua points give exactly (4/π²) log² n + O(log n), with the full three-term expansion now proved here (PD-T101, PD-T269–271). Below that, at least a proved polylogarithmic bound, or polynomial growth with a small exponent beating the known baselines;
4. ideally, Padua's algebraic extras: explicit Lagrange or kernel formulas, a positive cubature or hyperinterpolation link, and a fast transform.

The community calls the existence of such points the field's biggest open problem. De Marchi's 2022 survey: "We do not know the Padua points on [−1,1]^d, d ≥ 3" (LIT-377; secondary, UNVERIFIED).

## 2. Why the 2-D mechanism works, and where each part breaks in 3-D

**Padua in 2-D.** Pad_n is the even (or odd) checkerboard of the (n+1)×(n+2) Chebyshev–Lobatto grid. Equivalently, it is the self-intersections and boundary contacts of the degenerate Lissajous curve t ↦ (−cos((n+1)t), −cos(nt)), sampled at t = kπ/(n(n+1)) (LIT-312, LIT-313). Four facts combine:

- **(P1) Counting.** The grid has (n+1)(n+2) points, and the half with fixed index parity has exactly (n+1)(n+2)/2 = dim Π_n.
- **(P2) Cubature.** The positive product-Chebyshev rule on Pad_n integrates every polynomial of degree ≤ 2n−1 exactly, and degree 2n except one alias direction (as reported in LIT-312/313; verify the exact exactness statement against the fulltexts). In this repository the exceptional coefficient appears as c_{n,0} = 1 in the reproducing kernel.
- **(P3) Unisolvence from (P2).** Discrete orthogonality on Π_n follows from exactness up to degree 2n except one alias, and the corrected kernel gives the Lagrange basis. The ideal-theory approach writes the vanishing ideal with explicit generators of degree n+1 (LIT-313).
- **(P4) Quality.** The Lebesgue function is a lattice sum of a rhombic Dirichlet kernel, which gives (4/π²) log² n. This repository's PD-T101/T206–231 analyse it exactly.

**In 3-D:**

- **(P1′) Counting works.** (n+1)(n+2)(n+3) is a 3-axis Lobatto grid, and a density-1/6 subset has about the right size. PD-T081 (PROVED here): a periodic congruence fibre {Σ aⱼiⱼ ≡ c mod k} of a product grid can have exactly binom(n+3, 3) points infinitely often only if its density is 1/3! = 1/6. Among k ≤ 6, only a single fibre modulo 6 qualifies. PD-T082 (PROVED here): i + j + l ≡ c (mod 6) in [0,n]×[0,n+1]×[0,n+2] has exactly the right count for n ≡ 3, 4, 5 (mod 6), for c ∈ {0, 3} when n ≡ 0, 2 (mod 6), and never for n ≡ 1.
- **(P1′, caveat) Mod 6 doesn't fold the way mod 2 does.** In 2-D, parity is invariant under the cosine-folding reflections i ↦ 2n − i, so the checkerboard is the cosine image of a subgroup coset of the torus. A mod-6 index condition is generally *not* reflection-invariant. So the mod-6 fibres are not automatically cosine images of torus-subgroup cosets, and the cubature and aliasing machinery of (P2)–(P3) does not apply directly. Check this.
- **(P2′) Cubature probably fails.** Li–Sun–Xu reportedly conjecture that product-Chebyshev cubature of degree 2n−1 on the cube needs at least about n³/4 nodes, while dim Π_n ≈ n³/6 (secondary, via the programme "Open problems verification" notes). Xu 2024 states that no cubature family attaining Möller's lower bound is known for d > 2 (LIT record xu-2024, partial). If the conjecture holds, no 3-D set can play Padua's cubature role with dim Π_n points.
- **(P2′, existing 3-D cubature).** De Marchi–Vianello–Xu 2009 (LIT-322, partial) build degree-(2n+1) Chebyshev cubature from two complementary parity subgrids of the (n+2)³ Lobatto grid, about n³/4 nodes. They state explicitly that degree-n hyperinterpolation there is *not* interpolation, because there are more nodes than dim Π_n.
- **(P3′) The generating curve fails.** In 3-D, Chebyshev or Lissajous curves generically do not self-intersect (Bos–De Marchi–Vianello, arXiv 1502.04114, IMA JNA 2017; LIT-321/392, partial). So "self-intersections = nodes" gives no total-degree set. Their substitute extracts approximate Fekete/Leja points from the weakly admissible mesh. Lebesgue constants "seem to increase quadratically", numerically only (LIT-392, secondary).
- **(P3′, Lissajous–Chebyshev nodes)** (Dencker–Erb JAT 2017 and the "unifying" preprint; LIT-014, 319, 320, 380). These are unisolvent in d dimensions with discrete orthogonality, fast transforms and product-of-logs Lebesgue bounds, for **spectral** index sets defined by the Lissajous parameters, not for the total-degree simplex. Whether some parameter choice makes the spectral set alias-equivalent to Π_n in 3-D is exactly the kind of question this topic should settle.
- **(P4′) Quality is unexplored analytically.** Hyperinterpolation on the cube has operator norm O(logᵈ n) (Wang–Wang–Wang 2014, reported). In 3-D, log³ n is therefore the natural target for a "Padua quality" claim.

## 3. What this repository already has in 3-D

From the lattice-unisolvence track, `tracks/lattice-unisolvence/` (topic `topics/lattice-unisolvence-20261031/`):

- **PD-T081 and PD-T082:** density and exact counts, above.
- **PD-T093 (PROVED).** The single fibre 3i + j + 2k ≡ 0 (mod 6) in a 3×4×5 grid (degree n = 2, ten points) has a determinant that factorizes into axis-only factors. It is unisolvent for Π₂ over any field iff two explicit y and z conditions hold, and in particular whenever the y and z lists are strictly monotone. This is the only proved 3-D "Padua-like" axis factorization, and it is isolated.
- **PD-N036 (PROVED).** A degree-1 mod-4 fibre whose unisolvence condition genuinely mixes the axes.
- **PD-T090, PD-T091 (PROVED):** generic witness reduction, and coordinate-layer and projected-count annihilator certificates.
- **PD-N035, PD-N038 (MEASURED):** of 364 catalogue representatives, 222 are deficient in every modular draw, and there are rectangle obstructions in finite degrees.
- **PD-N037 (MEASURED):** Chebyshev–Lobatto specializations of the surviving small-index fibres have bad sampled Lebesgue values at n = 3–6 (88.99, 1497.8, 3863.7, 97819). On the same mesh, the references are:

  | n | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|
  | Leja-ordered lower set | 13.2 | 19.5 | 26.3 | 40.3 |
  | QR approximate Fekete | 8.32 | 11.2 | 13.9 | 22.2 |

  **These two rows are the baselines any new family must beat.**
- **PD-T094 (OPEN):** an unbounded-degree periodic 3-D total-degree family with an axis-factorized determinant or a proved good Lebesgue growth.
- **Code:** `tracks/lattice-unisolvence/code/` (c0_catalogue, c3_rank, c3_lebesgue, c3_obstructions, …).
- **Related tools elsewhere in the repo:**
  - the 2-D Padua alias formula PD-T106 and its defect architecture PD-T109;
  - the Padua Lebesgue-function machinery (`topics/padua-argmax-*`);
  - the finite-field Padua dictionary (programme notes, round 3: Padua identities hold modulo p ∤ 2n(n+1), which gives fast exact rank certificates);
  - the commuting-pair / joint-spectrum results PD-T095–T097, PD-T102.
- **Scope history.** IDEA-120 ("3D Padua via joint spectra / minimal cubature") and IDEA-013 were recorded as "out of scope (AC: 3D Padua)" in campaign scoping documents (bivariate-Lanczos baseline, charter-unisolvence plan). On 2026-11-06 AC said he does not remember ruling it out of scope and guesses the note applied to one specific item. **This topic is in scope by AC's instruction.**

## 4. What Claude expects (judgment, not evidence)

- **E1. An exact Padua analogue built by Padua's own mechanism probably does not exist in 3-D.**
  - The mechanism: the cosine image of a single torus-subgroup coset, or a union of a few cosets, with exactly binom(n+3, 3) points, unisolvent because of discrete orthogonality or a near-exact cubature.
  - Reasons: the (P2′) counting conflict with Li–Sun–Xu, and the reflection-invariance problem of mod-6 fibres.
  - **A proof within a precisely defined class would be a real, publishable negative theorem**, in the spirit of "no Chebyshev-lattice Padua points in dimension ≥ 3". Claude's confidence that such a theorem is true for a natural class: moderate to high. Confidence that it is provable in this campaign: moderate.
- **E2. Unisolvent total-degree sets are abundant; quality is the real question.**
  - Radon/Berzolari stacking (unisolvent sets of degrees n, n−1, …, 0 on n+1 parallel planes) is always unisolvent. With 2-D Padua slices on Chebyshev planes it is an explicit, provably unisolvent family.
  - Claude expects its Lebesgue constant to grow polynomially, by analogy with Morrow–Patterson-type stackings in 2-D (O(n²)–O(n³)). That makes it a baseline, not the answer.
- **E3. The most promising positive route is "aliasing-designed" sets.**
  - Choose a Lissajous–Chebyshev or rank-1 Chebyshev-lattice node set whose spectral index set is *alias-equivalent* to the total-degree simplex. Then prove unisolvence by an exact aliasing argument, as PD-T106 does for 2-D Padua, without needing a positive cubature.
  - The Dencker–Erb framework and the rank-1 Chebyshev-lattice literature (Cools–Poppe; Potts–Volkmer; Kämmerer and coauthors on reconstructing rank-1 lattices; verify all) are the toolkits.
  - Claude expects that exact interpolation (|X| = |I|) is rare there, because reconstruction-by-orthogonality usually needs |X| well above |I|. But "unisolvent with a structured Vandermonde" is weaker than orthogonality, and that gap is where a new family could live.
- **E4. A union of a few structured pieces, if it exists, is likelier to have polylog quality than any single fibre.** Examples: a parity subgrid thinned by a second character, or "Lissajous points + boundary correction". PD-N037 suggests single mod-6 fibres on Lobatto axes are poor.
- **E5. Minimal cubature and joint spectra.** A Gaussian-type or near-minimal Chebyshev cubature on the cube with about dim Π_n nodes probably does not exist (Li–Sun–Xu). Small-degree **non-existence certificates** (degrees 5–9, the programme's X7) are plausible and publishable as a side result.
- **E6. Lower bounds on quality are plausible.** For example, Λ(X) ≥ c log³ n for every unisolvent total-degree set in the cube. Transferring 1-D and 2-D lower-bound techniques for the cube or square may be feasible, and would frame any positive result. Check the literature first; such bounds may be known.

## 5. Literature to read first (fulltexts; cite only after reading)

- **The problem and its status:** De Marchi 2022, *Constr. Math. Anal.* (doi:10.33205/cma.1070020).
- **3-D Lissajous and cubature:**
  - Bos–De Marchi–Vianello 2017, IMA JNA 37 (doi:10.1093/imanum/drw013; arXiv 1502.04114);
  - De Marchi–Vianello–Xu 2009, BIT 49 (arXiv 0805.3529).
- **General Lissajous–Chebyshev:**
  - Dencker–Erb, JAT 219 (2017) (doi:10.1016/j.jat.2017.03.003);
  - the "unifying theory" preprint;
  - Dencker–Erb–Kolomoitsev–Lomako, J. Complexity 2017.
- **2-D Padua theory to transfer:** Bos–Caliari–De Marchi–Vianello–Xu 2006, JAT 143 (generating curve); Bos–De Marchi–Vianello–Xu 2007, Numer. Math. 108 (ideal theory).
- **Cubature bounds:**
  - Möller's lower bound;
  - the Li–Sun–Xu cube conjecture (locate the paper);
  - Xu 2024 (arXiv 2407.09903);
  - Noskov–Schmid; Hirao–Sawa.
- **Rank-1 Chebyshev lattices:** Cools–Poppe (BIT 2011); Potts–Volkmer; Kämmerer–Potts–Volkmer. Locate exact references.
- **Unisolvent constructions:** Radon 1948; Chung–Yao natural lattices; Berzolari.
- **Lebesgue lower bounds in several variables:** Sündermann; Bos; and others. Survey first.

Give AC clickable DOI or journal links for any paywalled item.
