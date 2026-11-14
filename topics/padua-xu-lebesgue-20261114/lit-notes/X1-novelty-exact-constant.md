# X1 novelty check: exact Xu Lebesgue constant Λ^Xu_n = L_n², argmax at the non-node vertices, rotated product lift

Checker: Claude (Opus 5.5), independent literature/novelty checker. Date of all reads and queries: 2026-11-14.

Claim under check (developer result, X1-01..X1-05, not yet audited): for the Xu points of degree n (Xu 1996), Λ^Xu_n = L_n², where L_n = (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)) is the Lebesgue constant of interpolation at the n zeros of T_n. The maximum is attained exactly at the non-node vertices (all four vertices for even n). Mechanism: with u = (θ₁+θ₂)/2 and v = (θ₁−θ₂)/2, every fundamental function lifts to a fiber sum of products d_n(u−u_p) d_n(v−u_q) of 1D trigonometric fundamental functions. This gives λ_n ≤ ω_n(u) ω_n(v) ≤ L_n², with equality at the vertices.

Access and reading methods:
- **BdMV.** Journal PDF at /mnt/user-data/uploads/Downloads/1-s2.0-S0021904506000220-main.pdf, read in full with `pdftotext -layout` into /tmp (not copied into the repo).
- **arXiv papers.** WebFetch digests of the PDF/HTML text layers. A digest is a model summary with short quotes, not the page itself. Direct `curl` to arxiv.org and api.crossref.org was refused by the egress proxy (CONNECT 403), so Crossref was queried through WebFetch.
- Paraphrases only. Every quote is under 15 words.

Verdict vocabulary: **KNOWN** (stated in a source read), **PARTIALLY KNOWN** (an ingredient or a weaker form is published), **NOT FOUND** (no matching result found in the documented search; this is the only negative used).

---

## 1. BdMV, J. Approx. Theory 141 (2006) 134–141, DOI 10.1016/j.jat.2006.01.005 — full text read

Page map (journal pagination):
- §2 setup, eqs. (2)–(9): pp. 136–137.
- Theorem 1, eq. (10), and Lemma 1, eq. (11): p. 137.
- Kernel decomposition (12), Lemmas 2–3, eqs. (13)–(15): pp. 137–138.
- Type-A/B sums (16), (17), (18): pp. 138–139.
- Lemmas 4–5, eqs. (19)–(20): p. 140.
- Proof of the main theorem: pp. 140–141.
- Acknowledgment: p. 141.

**Theorem 1 (p. 137), eq. (10):** Λ^Xu_n ≤ 8((2/π) log n + 5)² + 4, for even n only ("for simplicity's sake", §2 p. 136). The text layer is clean here, so this confirms X1-sources F5 and literature-xu-mp §4.

**Proof structure. The rotation and product structure IS present, but only as inequalities:**
1. K*_n is written as ½ Σ over the four sign choices of (D_n + D_{n+1})(θ₁±φ₁, θ₂±φ₂), minus the T_n correction ½(−1)^k (cos nθ₁ − cos nθ₂) (eq. (12), p. 137).
2. Lemma 1, eq. (11), p. 137, writes D_n(α, β) as ¼ times a sum of two products. Each product is [sin(n(α+β)/2)/sin((α+β)/2)]·[sin(n(α−β)/2)/sin((α−β)/2)] (the second has n−1 for n). With α = θ₁+φ₁ and β = θ₂+φ₂, these are exactly the rotated variables (θ₁+θ₂)/2 + node shift and (θ₁−θ₂)/2 + node shift. So the factorization into 1D Dirichlet-type kernels in u, v is published here.
3. The losses come in the following places:
   - Lemma 2 (p. 138) bounds the (n±1)-products by 2|n-product| + 2.
   - Lemma 3, eq. (13), gives |D_n + D_{n+1}| ≤ |n-product| + ½.
   - The T_n correction and the K_n/K_{n+1} averaging are absorbed into additive constants (eq. (14)).
   - The four sign terms are bounded separately by the triangle inequality (eq. (14), "+3 other terms").
4. The node sum is split by type (A: (z_{2i}, z_{2j+1}); B: (z_{2i+1}, z_{2j})). For one sign term, the change of variables k = i+j, m = i−j (p. 139) maps the node indices into a superset of a product range. The sum is enlarged to it, which gives a product of two 1D sums, eq. (18).
5. Lemma 4, eq. (19), and Lemma 5, eq. (20), p. 140, bound each 1D factor crudely, by (2/π) log n + 4 and (2/π) log n + 5, using the convexity of csc.
6. Total: 2 types × (2 + 4 × product). The leading coefficient is 8·(4/π²) = 32/π² on log² n, against the true 4/π². That is a factor 8 too large, plus large additive constants. Numerically, the bound is 423.9 against L_n² = 10.288 at n = 34, and 507.3 against 15.165 at n = 100 (computed here).

**What BdMV do not contain:**
- **Exactness.** There is no identity: every step is an inequality. There is no fiber-sum formula, and the four sign terms and two node types are not recombined into one product.
- **L_n² or any sharp constant.** The 1D factors are never identified with the Chebyshev-zero Lebesgue constant.
- **Lower bounds.** The intro (p. 135) only quotes the 1D, ball and tensor-product facts.
- **Maximizers.** A grep of the full text for vert|corner|maxim|attain|sharp|exact|optimal finds no statement about where the maximum lies. The "attained" hits (p. 135) concern 1D and tensor-product minimal growth.

The acknowledgment (p. 141) thanks Yuan Xu for suggestions in deriving the proof of the main theorem. This is consistent with the rotation idea coming from Xu (cf. §3, Xu 2012).

**Verdict, item 1: PARTIALLY KNOWN (mechanism only).** The rotated product factorization and the k = i+j, m = i−j reindexing are published (eqs. (11), (17)–(18)), but only as a lossy upper bound. L_n², the exact fiber lift and the vertex statement are NOT FOUND in BdMV.

---

## 2. Lissajous–Chebyshev literature

| Source | Read | Xu points as LC nodes? | Lebesgue statement | Exact value / product formula / maximizer |
|---|---|---|---|---|
| Dencker–Erb, "A unifying theory for multivariate polynomial interpolation on general Lissajous-Chebyshev nodes", arXiv 1711.00557v1 (1 Nov 2017). Title verified on arXiv. Crossref returned no journal record for this title. | Digest, chars 0–157k (whole text) | Yes, §9.2: "Morrow-Patterson-Xu points" = LC with m = (m, m); Xu studied LC^{(2k,2k)}_{(0,1)} and LC^{(2k+1,2k+1)}_{(0,0)}. Interpolation space (9.2) with the boundary symmetry c_{(γ₁,γ₂)} = (−1)^{κ₂−κ₁} c_{(γ₂,γ₁)} | None. §1 only mentions tensor-like growth for other LC nodes, citing DEKL | None |
| Dencker–Erb–Kolomoitsev–Lomako, "Lebesgue constants for polyhedral sets and polynomial interpolation on Lissajous-Chebyshev nodes", J. Complexity 43 (2017) 1–27, DOI 10.1016/j.jco.2017.05.001 (Crossref via WebFetch); arXiv 1608.03451v2. Title and arXiv id verified. | Digest of PDF | No. N_d requires **pairwise relatively prime** entries (eq. (1.1)), which excludes (n, n). "Xu" appears only as the source of a proof idea (Prop. 3.2) and as a co-author in the references; no "Morrow". | Thm 3.4, eq. (3.9): Λ ≍ Π log(n_i+1), order only; lower bound (3.15) Λ ≥ 3^{−d} L(Γ) | No exact value. The proof bounds ‖K(x, ·)‖ by its value at x = 1 (eqs. (3.11)–(3.12)) for the polyhedral kernel; that is not a maximizer claim for the interpolation, and not for Xu |
| Erb, "Bivariate Lagrange interpolation at the node points of Lissajous curves – the degenerate case", Appl. Math. Comput. 289 (2016) 409–425, DOI 10.1016/j.amc.2016.05.019; arXiv 1503.00895 | Digest of PDF | No. LD_{n,p} needs p ≥ 1 and gcd(n, n+p) = 1, so (n, n) is excluded except n = 1. The Xu points are cited, and Lemmas 8–9 borrow Xu's 1996 ideas (Remark 6) | Thm 11: D ln² n ≤ Λ_{n,p} ≤ C ln²(n+p), constants unspecified; the proof uses Yudin's bound for the rhombic Dirichlet kernel | No. The lower bound evaluates at (1,1) but no maximizer claim is made |
| Erb–Kaethner–Ahlborg–Buzug, "Bivariate Lagrange interpolation at the node points of non-degenerate Lissajous curves", Numer. Math. 133 (2016) 685–705 (online 2015), DOI 10.1007/s00211-015-0762-1; arXiv 1411.7589 | Digest of PDF | Remark 1: Lisa_{n,0} "correspond with" XU_{2n}, formally only (non-degenerate case needs odd p). §6 defines XU_{2n+1} and compares numerically (Fig. 4, Tables 3–4) | No theorem: numerics to n = 60, plus a conjecture of O(log² n) for Lisa points | None |
| Kolomoitsev–Lomako, AMC 403 (2021) 126192 (repo LIT-379; prior reader X1-sources §5) | Not re-read; repo record | Thm 2.1 needs n = lm + p, 1 ≤ p < m, so m = n is excluded | (4/π²)(2 log m log n − log² m) + O(·) | No |
| Pimenova 1979; Kuznetsova 1995 (repo LIT-484, LIT-482/483) | Not re-read; repo records | Periodic rhombic trigonometric interpolation on full (2n+1)² or 2m×2n torus grids. Not the Xu sublattice; no cosine symmetrization | Pointwise ln²-asymptotics with an angular factor and O(ln n) remainder | No exact value |

**Verdict, item 2: NOT FOUND.** No LC-literature item gives an exact Lebesgue constant, an exact product formula or the maximizers for Xu points. Dencker–Erb 1711.00557 §9.2 is the only one that places Xu points inside the LC framework, and it has no Lebesgue result. The others exclude (n, n) by coprimality or non-degeneracy.

---

## 3. Harris; Xu 2012/2017; Li–Sun–Xu; general searches

**Xu, "Minimal cubature rules and polynomial interpolation in two variables", JAT 164 (2012) 6–30, DOI 10.1016/j.jat.2011.09.003 (Crossref via WebFetch); arXiv 1102.0055.** This is the **closest predecessor found**. Read as a digest of the PDF and of ar5iv (both halves).
- **The node sets are the rotated product grid.**
  - Thm 6.1 / (6.2): the nodes are (s_{j,k}, t_{j,k}) and its three images (t, s), (−s, −t), (−t, −s), where s_{j,k} = cos((θ_j − θ_k)/2) and t_{j,k} = cos((θ_j + θ_k)/2).
  - Here x_{k,n} = cos θ_{k,n} are the zeros of P_n^{(α,β)}.
  - For α = β = −1/2 these are Chebyshev angles. Section 6.2 says the case α = β = −1/2 was introduced in [20] (Xu 1996). The cross-check below (by this checker, not stated in the paper) shows these are the even-degree (2n) Xu points.
- **Gaussian case** (symmetric polynomials on a parabola–two-lines domain Ω, nodes (x_j + x_k, x_j x_k)), Cor. 5.2: ‖L_n‖_∞ ≤ (‖I_n‖_{C[−1,1]})². This is a "square of the 1D Lebesgue constant" bound, but only an upper bound, and for a **different** node set and space.
- **Minimal (Xu-type) case.**
  - Section 6.2 says the result "cannot be deduced" from the one-variable Lebesgue constant "as we did in Corollary 5.2", "since there are four remaining sums". Only the first of these is directly a 1D fundamental-polynomial sum.
  - Lemma 6.2: the Lebesgue constant is ¼ max of a four-subset sum, ∼ the single-subset sum.
  - Lemma 6.5: max Λ_n^{(i,j)} = O(log n) at max{α, β} = −1/2.
  - Thm 6.6: ‖L_n‖ = O(1)(log n)² at max{α, β} = −1/2.
  - The proof substitutes x₁ = cos((θ₁−θ₂)/2), x₂ = cos((θ₁+θ₂)/2) and reduces to products of the Λ_n^{(i,j)}.
  - No exact value, no square of L_n and no maximizer.
- Section 6.2 also says the α = β = −1/2 order "was determined in [3] based on the explicit expression in [20]", i.e. in BdMV based on Xu 1996.

Cross-check by this checker, not stated in the paper: with α = β = −1/2, θ_k = (2k−1)π/(2n). Then (θ_j ∓ θ_k)/2 = (j−k)π/(2n) and (j+k−1)π/(2n), whose index sum is odd. These are Xu points of degree N = 2n, and the 1D building block has n = N/2 nodes. The X1 lift instead uses 2N equispaced trigonometric nodes, equivalent to N Chebyshev zeros. So the decomposition differs from X1's.

**Xu, "Minimal cubature rules and polynomial interpolation in two variables II", JAT 214 (2017) 49–68, DOI 10.1016/j.jat.2016.11.002; arXiv 1603.08162.** Digest.
- Near-minimal rules of degree 4m+1.
- Thm 4.3: O(1)(log n)² for n = 2m+1, max{α, β} = −1/2.
- No explicit constant, no univariate-square bound and no maximizer.
- Cites BdMV for the α = β = −1/2 order.

**Li–Sun–Xu, "Cubature formula and interpolation on the cubic domain", Numer. Math. Theor. Meth. Appl. 2(2) (2009) 119–152, DOI 10.4208/nmtma.2009.v2n2.p119.**

This is the developer's lift source and the orchestrator's priority check. Venue and title verified:
- the journal's own first-page excerpt (admin.global-sci.org …/v2n2/22-119_short.pdf) gives the title, authors, vol. 2 no. 2 and pp. 119–152;
- arXiv 0808.0180v2 (submitted 1 Aug 2008, v2 15 Aug 2008) has the same title and authors, with no journal reference on the abstract page;
- the DOI is from repo record LIT-010.

Read: two full-text digests of the arXiv PDF. The second was confined to §3. The digest reports the text complete through §4 and the references. Locators are in the arXiv numbering; the journal pagination of §3 was not seen.

§3 structure:
- §3.1 Discrete Fourier analysis and cubature on the plane: Thms 3.1–3.2.
- §3.2 Cubature for algebraic polynomials: Thms 3.3–3.5.
- §3.3 Interpolation by polynomials: Prop. 3.6, Lemmas 3.7–3.8, Thms 3.9–3.10.

The lattice and interpolants:
- The lattice is B = n[[1,1],[−1,1]], with rhombus spectral set Ω_B = {−n ≤ x₁+x₂ < n, −n ≤ x₂−x₁ < n} and index change k₁ = j₁+j₂, k₂ = j₂−j₁ (proof of Thm 3.1).
- Prop. 3.6: the lattice interpolant is I_n f(x) = Σ_{k∈X_n} f(k/2n) Φ_n(x − k/2n), with Φ_n = (1/(2n²)) Σ_{ν∈Λ_n} e_ν. This is a single exponential sum over the rhombus index set.
- Symmetrization: P f = ¼[f(x₁,x₂) + f(−x₁,x₂) + f(x₁,−x₂) + f(−x₁,−x₂)].
- Lemma 3.8: Φ*_n = 2[D_n + D_{n−1}] − ¼(cos 2πnx₁ + cos 2πnx₂). Here D_n is Xu's closed form, a ratio of differences in x₁ and x₂ separately.
- Thm 3.9: L_n f ∈ T_n, even, interpolating on {j/2n : j ∈ Ξ_n}.
- Thm 3.10: L_n f ∈ Π²_n interpolating on Γ_n, with ℓ*_k = ½ P[D_n + D_{n−1}](· − k/2n) minus a T_n correction. The printed index T_{k_i} appears to be a typo for T_n, judging from its proof.

This is the published "lattice trigonometric interpolation + even symmetrization ⇒ Xu interpolation" derivation, i.e. the structural precursor of X1-01. However:
- **No 2D Lebesgue statement of any kind.** "Lebesgue", "norm" and "log" do not occur in the body of §3. The only BCDMV/BdMV-group mention in §3 says the polynomials were "tested and studied numerically in [3, 4]". BdMV appears only as bibliography entry [5].
- **No product form.** Neither Φ_n, Φ*_n nor D_n is written as a product of 1D kernels in x₁+x₂ and x₁−x₂. The rotated coordinates appear only in the definition of Ω_B.
- **No maximizer or vertex statement** for any Lebesgue function. The vertex remarks in §3 concern cubature weights and the congruence of boundary points (Thm 3.2, Lemma 3.7).
- **3D only:** Thm 4.9 and Cor. 4.12 give ‖I*_n‖_∞, ‖L_n‖_∞ ≤ c(log n)³ with c unspecified. The proof bounds sums by the cube of a 1D Dirichlet-type sum over an enlarged index range ("standard estimate of one variable", Zygmund). This is an upper bound only, with no sharp constant.

**Companion Li–Sun–Xu papers.**
- "Discrete Fourier analysis, cubature and interpolation on a hexagon and a triangle", arXiv 0712.3093, abstract only: hexagon/triangle setting; the Lebesgue constant is "in the order of (log n)²". No square, Chebyshev or Xu points.
- "Discrete Fourier analysis with lattices on planar domains", arXiv 0910.5286, PDF digest:
  - §3.1 (square–rhombus) restates the Xu-point cubature (Thm 3.2), with "first appeared in [20]";
  - it says the Lagrange interpolation on these points was defined in [21] and recovered in [8] (= the NMTMA paper above);
  - its c(log n)² bounds (§3.4, §3.5.2) concern the triangle and hexagon operators only;
  - nothing exact, no product bound, no maximizers.

**Verdict for the lift's most likely source:**
- **PARTIALLY KNOWN:** the lattice-trigonometric-plus-symmetrization derivation of Xu interpolation (NMTMA 2009, §3.3, Prop. 3.6–Thm 3.10).
- **NOT FOUND** in that paper or its companions:
  - the rotated product factorization of the fundamental functions;
  - any 2D Lebesgue bound;
  - a product or square-of-1D bound;
  - the exact value;
  - the maximizers.

**Li–Sun–Xu, "Discrete Fourier analysis with lattices on planar domains", Numer. Algorithms (2010); arXiv 0910.5286.** Digest.
- §3.1 gives the Xu-point cubature (Thm 3.2).
- Lebesgue bounds c(log n)² for triangle and hexagon operators (§3.4, §3.5.2) only.
- Nothing exact; nothing about maxima.

**Harris.** Bibliographic pages and abstracts only.
- "Bivariate Lagrange interpolation at the Chebyshev nodes", Proc. AMS 138 (2010) 4447–4453, DOI 10.1090/S0002-9939-2010-10581-6.
- "Lagrange polynomials, reproducing kernels and cubature in two dimensions", JAT 195 (2015) 43–56, DOI 10.1016/j.jat.2014.10.017.
- "Alternation points and bivariate Lagrange interpolation", JCAM preprint, author page (full text, digest).

Interpolation and cubature theory only. None of them mentions Lebesgue constants; the JCAM preprint names the Xu points.

**Other items opened.**
- Caliari–De Marchi–Vianello, "Hyperinterpolation on the square" (preprint hypXu.pdf): uses BdMV's bound with a_n = (2/π) log(n+1) + 5 (§2.3) and nothing sharper.
- An–Sommariva–Vianello, arXiv 2601.04708 (2026): no Xu Lebesgue result in the digest (abstract-level).
- All BdMV/BCDMV citing works listed in X1-sources §6 (prior reader): none has an exact constant or a vertex proof.

**Verdict, item 3:**
- **NOT FOUND:** Λ^Xu_n = L_n² (exact), or any statement that the Xu Lebesgue constant equals the square of a univariate constant.
- **PARTIALLY KNOWN:**
  - the rotated-grid description of the Xu nodes (Xu 2012 Thm 6.1);
  - the (θ₁±θ₂)/2 reduction to products of 1D sums (Xu 2012 Thm 6.6 proof; BdMV (11), (18));
  - a "≤ square of the 1D Lebesgue constant" bound for a different, Gaussian/symmetric-polynomial interpolation (Xu 2012 Cor. 5.2).

  Xu explicitly says that argument does not transfer to the minimal (Xu) case.

---

## 4. One-dimensional ingredients (classical)

- **L_n = (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)) for n Chebyshev zeros, attained at ±1: KNOWN (classical).**
  - Statement with the n-node convention: S. J. Smith, "Lebesgue constants in polynomial interpolation", Ann. Math. Inform. 33 (2006) 109–123, §2.2, p. 112 (unnumbered display Λ_n(T) = λ_n(T, ±1) = cotangent sum). There, the maximum at ±1 is credited to Ehlich–Zeller.
  - Primary source: H. Ehlich, K. Zeller, Math. Ann. 164 (1966) 105–112, DOI 10.1007/BF01429047 (repo LIT-470; OCR-level reading).
    - Satz 1, pp. 106–107: trigonometric interpolation at equispaced nodes (2n+1 or 2n), maximum at the interval midpoints.
    - Satz 2, pp. 107–108: Chebyshev zeros, maximum at ±1; the algebraic Lebesgue function equals the transformed trigonometric one on the end intervals.
    - Satz 3 gives the explicit 1D constant (per the repo p1-comparison).
    - Ehlich–Zeller (via LIT-470) thus also covers the X1-02 step ω_n ≤ L_n with equality at the midpoint/vertex.
  - Attribution chain: Brutman, SIAM J. Numer. Anal. 15 (1978) 694–704, p. 695 (repo LIT-466): the Luttmann–Rivlin conjecture, proved by Ehlich–Zeller; see also Powell, Comput. J. 9 (1967) 404–407.
  - Rivlin's books were not opened in this check, so no Rivlin locator is given.
- **L_n = (2/π)(log n + γ + log(8/π)) + O(1/n²): KNOWN (classical).**
  - Smith 2006, eq. (2.2), p. 112, n nodes, O(1/n²). The expansion is said to be deducible from the cotangent form, with Brutman's 1997 survey as the reference (Ann. Numer. Math. 4 (1997) 111–127; not opened).
  - Full asymptotic series: P. N. Shivakumar, R. Wong, Math. Comp. 39 (1982) 195–200, DOI 10.1090/S0025-5718-1982-0658223-X. Abstract read: an infinite asymptotic expansion for the Chebyshev-zeros Lebesgue constants, with the truncation error bounded by the first neglected term and of the same sign. Coefficients and n/n+1 convention not seen.
  - Günttner, SIAM J. Numer. Anal. 17 (1980) 512–520 (repo LIT-487, partial reading): expansions of the form (2/π) log n + c + r_n with bounds on r_n.
  - The repo record brutman-1978.md covers local-maxima monotonicity and the ±1 attribution, **not** the log(8/π) expansion. Do not cite Brutman 1978 for the expansion.
  - The next term π/(72n²) of X1-06 was not seen in any source opened here. X1-06 itself claims no novelty for it.

---

## 5. Query log

| # | Query / endpoint | Outcome |
|---|---|---|
| Q1 | pdftotext BdMV journal PDF; grep vert/corner/maxim/attain/sharp/exact/optimal | Full read (§1). No vertex or sharpness statement |
| Q2 | WebSearch: Harris "Bivariate Lagrange interpolation at the Chebyshev nodes" Proc AMS | AMS page (Q8); Erb degenerate-case hits |
| Q3 | WebSearch: Harris "Lagrange polynomials, reproducing kernels and cubature in two dimensions" | uky Scholars page (Q9); Xu arXiv 1102.0055; Harris JCAM preprint |
| Q4 | WebSearch: Li Sun Xu lattices planar domains Lebesgue | arXiv 0910.5286, 0808.0180 |
| Q5 | WebFetch ar5iv 0910.5286 (first 100k chars), then arxiv.org/pdf/0910.5286 | §2 only from ar5iv; the PDF digest gave §3.1 Xu cubature, Lebesgue bounds only on the triangle and hexagon |
| Q6 | WebFetch global-sci short PDF (NMTMA 2(2) 119) | Title, abstract and intro only |
| Q7 | WebFetch arxiv.org/pdf/0808.0180 | §3 2D: no Lebesgue result; 3D: c(log n)³ |
| Q8 | WebFetch AMS Proc. 138 page (Harris 2010) | Abstract: no Lebesgue constants |
| Q9 | WebFetch uky page (Harris JAT 195) | Abstract: no Lebesgue, no Xu |
| Q10 | WebFetch Harris Alternation_JCAM | No Lebesgue; Xu points named |
| Q11 | curl arxiv.org PDFs and api.crossref.org | CONNECT 403 (proxy). Switched to WebFetch |
| Q12 | WebFetch api.crossref.org: Xu minimal cubature I/II | JAT 164 (2012) 6–30; JAT 214 (2017) 49–68 |
| Q13 | WebFetch arxiv.org/pdf/1102.0055 (twice) + ar5iv 1102.0055 (both offsets) | §3 above. Closest predecessor; explicit "cannot be deduced" sentence |
| Q14 | WebFetch arxiv.org/abs/1711.00557 and pdf (both offsets) | Title verified; §9.2 MPX = LC (m, m); no Lebesgue |
| Q15 | WebFetch arxiv.org/abs/1608.03451 and pdf | Title verified; pairwise coprime; Thm 3.4 order only |
| Q16 | WebFetch arxiv.org/pdf/1503.00895 | Thm 11 order only; (n, n) excluded |
| Q17 | WebFetch arxiv.org/pdf/1411.7589 | Remark 1, §6 numerics; no theorem |
| Q18 | WebFetch api.crossref.org: DEKL; Erb; EKAB; Dencker–Erb unifying | DOIs above; no Crossref record for the 1711.00557 title |
| Q19 | WebSearch: "Xu points" "Lebesgue constant" exact value square of univariate Chebyshev | Only BdMV, hypXu, BCDMV, Padua papers, 2605.23299 |
| Q20 | WebSearch: "Xu interpolation" Lebesgue function maximum vertices proof conjecture BCDMV | Only known items (BCDMV, ETNA, BdMV, MP papers) |
| Q21 | WebSearch: "Morrow-Patterson-Xu" Lebesgue constant asymptotics | 2601.04708 (Q23), 2412.14595, 2605.23299, KL, DRNA. Nothing new on Xu |
| Q22 | WebSearch: Szili Vértesi Lebesgue Xu lower bound | Only known items |
| Q23 | WebFetch arxiv.org/abs/2601.04708; hypXu.pdf | No Xu Lebesgue result; hypXu uses BdMV's bound |
| Q24 | WebSearch: Xu "Minimal cubature … II" arXiv Lebesgue | arXiv 1603.08162; fetched (§3) |
| Q25 | WebSearch: "Lebesgue constant" "Xu" "Chebyshev zeros" product rotated θ1+θ2 exact | Only known items |
| Q26 | WebSearch (extended): Lebesgue constant Xu interpolation exact formula 2024/2025/2026 vertices | Only known items (ETNA, BdMV, BCDMV, EKAB, MP 2412.14595, 2605.23299) |
| Q27 | WebSearch: Chebyshev Lebesgue cotangent Luttmann Rivlin Ehlich Zeller; Günttner expansion γ + log(8/π) | Smith 2006 survey; Shivakumar–Wong 1982 |
| Q28 | WebFetch Smith 2006 PDF; AMS Math. Comp. 39 page | §4 locators |
| Q30 | Orchestrator addition: WebFetch arxiv.org/pdf/0808.0180 (§3-only pass), arxiv.org/abs/0808.0180, arxiv.org/abs/0712.3093 | §3 above: lattice derivation confirmed; no 2D Lebesgue, no product form, no maximizers; venue verified |
| Q29 | Repo grep: literature/records for Lebesgue, rotation, 8/π, Luttmann, Rivlin | LIT-466, LIT-470, LIT-487, LIT-482–484, LIT-379 used as cited |

Not obtained in this check:
- Della Vecchia–Mastroianni–Vértesi 2009 and Szili–Vértesi 2009 (blocked per X1-sources §9);
- Brutman's 1997 survey;
- Rivlin's books;
- Günttner 1980, beyond the repo record;
- the published Numer. Algorithms version of Li–Sun–Xu 2010;
- Pan–Li 2020.

Xu's 2025 book "Minimal Cubature Rules" (Cambridge, DOI prefix 10.1017/9781009663939; chapters surfaced by Crossref in Q12) was **not read**. It is the most likely place for a later treatment of the Xu Lebesgue constant and should be checked before any priority claim.

---

## 6. Summary verdict and what is plausibly new

| Component of the claim | Verdict | Closest locator |
|---|---|---|
| Rotation u, v = (θ₁±θ₂)/2 and factorization of the kernel into 1D Dirichlet-type products | PARTIALLY KNOWN (as inequality tools) | BdMV Lemma 1 (11) p. 137, (17)–(18) p. 139; Xu 2012 Thm 6.6 proof |
| Xu nodes as the image of a 1D×1D angle grid under the rotation | KNOWN for even degree, in Xu 2012's form | Xu 2012 Thm 6.1 / (6.2) |
| Derivation of Xu interpolation from rhombus-lattice trigonometric interpolation plus even symmetrization | KNOWN | Li–Sun–Xu NMTMA 2 (2009) §3.3, Prop. 3.6, Lemma 3.8, Thms 3.9–3.10 |
| Exact fiber-sum lift ℓ_ξ = Σ_{F(ξ)} d_n(u−u_p) d_n(v−u_q), with fibers = orbits of order-8 group | NOT FOUND (closest: Li–Sun–Xu 2009 §3.3, unfactored) | — |
| λ_n ≤ ω_n(u) ω_n(v) pointwise (exact product majorant) | NOT FOUND | Weaker: BdMV (18) with factor 8 and constants; Xu 2012 Cor. 5.2 (different node set) |
| Λ^Xu_n = L_n² exactly (both parities) | NOT FOUND | BdMV Thm 1 (upper bound with leading coefficient 32/π²); BCDMV Conj. (17) (≲ ((2/π) log(n+1))²) |
| Argmax exactly at the non-node vertices | NOT FOUND (conjectured in BCDMV (17) for even n; odd-n variant not stated anywhere) | BCDMV p. 319 |
| 1D: L_n cotangent formula, max at ±1; ω_n max at midpoints | KNOWN | Ehlich–Zeller 1966 Satz 1–2; Smith 2006 §2.2 p. 112 |
| 1D: L_n = (2/π)(log n + γ + log(8/π)) + O(n⁻²) | KNOWN | Smith 2006 (2.2) p. 112; Shivakumar–Wong 1982; Günttner 1980 |

**Plausibly new (no matching result found in the documented search):**
- the exact identity Λ^Xu_n = L_n² for every n (even and odd);
- the exact fiber-sum product lift and the pointwise majorant λ_n ≤ ω_n(u) ω_n(v);
- the identification of the maximizers as the non-node vertices.

These together settle BCDMV Conjecture (17) in a sharper form. A consequence worth stating carefully: the Xu Lebesgue constant equals the tensor-product Chebyshev-zeros constant L_n², with about half as many nodes.

Suggested wording:
- Credit Li–Sun–Xu 2009 §3.3 for the lattice-plus-symmetrization derivation that the lift refines.
- Credit BdMV (and Xu, per their acknowledgment) and Xu 2012 for the rotation and product-reduction idea.
- Credit Ehlich–Zeller for the 1D ingredients.
- Claim exactness and the argmax only.
- Read Xu's 2025 book before any priority statement.
