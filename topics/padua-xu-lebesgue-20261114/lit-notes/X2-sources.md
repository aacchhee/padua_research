# X2 literature notes: Morrow–Patterson (MP) points and their Lebesgue constant

- Reader: Claude (claude-opus-5-5), literature subagent of topic `padua-xu-lebesgue-20261114`. Date: 2026-11-14.
- **Access method and its limits.**
  - Direct HTTP to arxiv.org, Springer, SIAM, Elsevier, Wiley, dblp and JSTOR is blocked from this sandbox. Some of these refuse the connection; others answer with bot checks, which were not bypassed.
  - Every fulltext below was therefore read through WebFetch. WebFetch returns a model-written rendering of the page, not the raw PDF text. Formulas were requested in LaTeX and cross-checked between two or three renderings and against my own computations (§6). For CDMV and BCDS, printed page numbers come from running headers in the extracted text and **may be off by one**. BBDM locators are exact (see the update below).
  - No PDF was saved. The quotes below are all under 15 words.
  - **Update (same day).** The orchestrator then staged the published BBDM PDF outside the repo. I re-read it with pdftotext, plus a page render of p. 38, so all BBDM page and equation locators in §1 are now **exact (published version)**. The orchestrator also read the JAT lower-bound paper (§1b); that entry is the orchestrator's reading, recorded here as reported.
- Status words used here:
  - "READ (WebFetch)": fulltext seen through the rendering described above.
  - "CHECKED-NUM": the statement was reproduced by my own numerical computation (scratch code in /tmp, not committed; §6).
  - "NOT READ": could not access.

---

## 0. Headline findings for the orchestrator

1. **A published paper titled "A lower bound for the Lebesgue constant of the Morrow–Patterson points" exists.**
   - Citation: T. Beberok, *J. Approx. Theory* **311** (2025), article 106191, DOI [10.1016/j.jat.2025.106191](https://doi.org/10.1016/j.jat.2025.106191). Found through Crossref; Crossref print date Nov 2025, record created 2025-05-09.
   - I could not reach the fulltext from this sandbox. The **orchestrator read the full HTML** through institutional access on 2026-11-14; see §1b.
   - Content, as reported by the orchestrator:
     - Theorem 0.1: Λ_n^MP ≥ c·n², with c existential.
     - The proof evaluates λ_n(1,1) through a closed form (2) for the corner kernel.
     - The final inequality gives an explicit, if unstated, constant of about 7.5·10⁻⁴ for n ≥ 8.
   - **X2.1 as posed (some explicit c·n² lower bound) is therefore already published in substance.** Any remaining novelty lies only in a sharp constant, the argmax, or the limit Λ/n².
   - Crossref reference list of the paper (13 entries): BBDM 2024 preprint; Bos 2001 notes; BCDMVX 2006 (JAT 143); BDMVX 2007 (Numer. Math. 108); CDMV 2005; De Marchi–Sommariva–Vianello 2014 (DRNA 7); Erb 2016 (two Lissajous papers); Liu 2019 (Acta Math. Hungar. 159, 618); Morrow–Patterson 1978; Sloan 1995; Xu 2012 and Xu 2017 ("Minimal cubature rules and polynomial interpolation in two variables" I and II, JAT 164 and JAT 214).
   - OpenAlex conflates this JAT paper with BBDM (W4410230682 lists both DOIs, and the JAT title with the Constr. Approx. DOI). That is a metadata merge error: Crossref gives two distinct records with different authors and titles.
2. **BBDM (Constr. Approx. 63 (2026) 31–65) proves only an upper bound, Λ_n^MP = O(n²).**
   - The constant is not explicit (Thm 4). There is no lower bound.
   - The "can be improved" remark refers to their sub-square estimate (§6), not to the O(n²) theorem. LIT-378's paraphrase is slightly off here.
   - BBDM define **no "MPX" points**. Remark 3 (p. 63) only mentions Xu's generalization of MP points to weights |x−y|^{2a+1}|x+y|^{2b+1}(1−x²)^{±1/2}(1−y²)^{±1/2}, a, b ≥ −1/2 (Xu JAT 2012/2017), and n² growth for "Xu points" with the second-kind weight (Liu–Zhu 2022). It says the latter are "not for Morrow–Patterson points".
   - The open problems they state (§7.1) are: (i) prove λ(x,y) = λ(−x,−y); (ii) prove that the Lebesgue constant is attained at each corner.
3. **My numerics contradict both BBDM open-problem statements as written, under the paper's own node definition** (CHECKED-NUM, §6).
   - For even n, λ_n is maximal only at the two corners with y = +1, namely (±1, 1).
   - At (±1, −1) it equals n+1: to 40 digits by mpmath for n = 2…10, and to double precision for n ≤ 40.
   - So λ(x,y) ≠ λ(−x,−y), and the maximum is not at "each corner".
   - The maximal corner value is **not** (n+1)(n+2)/2. Its ratio to (n+1)(n+2)/2 rises with n:
     - 0.9743 at n = 2, 1.0009 at n = 6, 1.0139 at n = 10;
     - about 1.032 at n = 50 and 1.0336 at n = 120.
   - In BBDM's code, `(n+1)(n+2)/2` is only a comparison curve labelled `leb_mp_true`.
   - My top-corner values reproduce CDMV 2005 Table 4 exactly after rounding (649, 1264, 2082, 3102; EMP 237, 456, 746, 1106). This is a strong G0 check of the conventions in §7.
4. Forward-citation search (§5): the JAT paper above is the only lower-bound-related hit. No other matching result was found in the documented search.
5. **The §2.2 zero-set formula is printed as given in BBDM** (p. 34): R_j^n = U_j(x₁)U_{n−j}(x₂) + U_{n−j−1}(x₁)U_j(x₂), 0 ≤ j ≤ n. As printed, it does not vanish on MP_n. The correct set is the index-shifted one, R_j^{n+1} (§6.3). This is an error in the paper, not in the rendering.

---

## 1. Source A: Beberok–Białas-Cież–De Marchi (BBDM)

- **Citation.** T. Beberok, L. Białas-Cież, S. De Marchi, "On the Lebesgue Constant of the Morrow–Patterson Points".
  - Journal: *Constr. Approx.* **63**(1) (2026) 31–65, DOI [10.1007/s00365-025-09710-x](https://doi.org/10.1007/s00365-025-09710-x).
  - Dates: received 28 Nov 2024; revised 25 Mar 2025; accepted 1 Apr 2025; published online 14 May 2025.
  - Communicated by Yuan Xu. Open access, CC-BY.
  - The volume, issue, pages and DOI were verified via Crossref and the Springer PDF header. LIT-378's "63 (2026) 31–65" is correct.
- **Versions read (all 2026-11-14).**
  - arXiv [2412.14595](https://arxiv.org/abs/2412.14595). v1 (19 Dec 2024) is the **only** arXiv version, with no journal-ref.
    - HTML: https://arxiv.org/html/2412.14595v1. Read completely, Sections 1–7.1.
    - PDF: https://arxiv.org/pdf/2412.14595v1. Used for references; no page numbers were available.
  - Published Springer PDF: https://link.springer.com/content/pdf/10.1007/s00365-025-09710-x.pdf.
    - First read through WebFetch.
    - **Then re-read from the staged copy** (orchestrator-supplied, outside the repo) with pdftotext and a raster render of p. 38. Read pp. 31–39, 43–46, 52–53, 63–65 and the reference list.
    - **All page and equation numbers below are now exact and refer to the published version.**
  - Author revision "R1": https://www.math.unipd.it/~demarchi/papers/draftMP-R1.pdf. Used for equation numbering, which differs between versions.
  - Author draft of Nov 2024: https://www.math.unipd.it/~demarchi/papers/LebesgueMP_Nov2024.pdf. Checked only for a lower bound; it has none.
  - GitHub repository https://github.com/demarchi-github/MP-points: README, `Leb_MP.m` and `ext_morr_patt.m`, read through WebFetch.
- **Reading gaps.**
  - Proof details of Thm 4 (pp. 53–63): the case analysis was read only at the structure level.
  - Equation numbers differ between versions. Below, "(k)" is the **published** numbering. "v1 (k)" is the arXiv v1 numbering where it differs; published = R1.
  - **In-text citation numbers in the published version are offset from its reference list.**
    - Examples: "Morrow and Patterson [18]" on p. 31 is list item 17; "[16, Thm. 1]" for Xu points on p. 63 is list item 15 (Liu–Zhu); "[10]" for the hyperinterpolation bound is list item 8 (De Marchi–Sommariva–Vianello).
    - Cite by content, not by bracket number.

### 1.1 Definitions (BBDM)

- **MP points** (§1, pp. 31–32, display unnumbered). Let Q = [−1,1]², with n a positive **even** integer.
  - Admissibility: p. 31 says "for an even positive integer n". §2 (p. 32) says n is "usually a positive even integer" and defines C_n := 8/((n+2)(n+3)). The index k = 1,…,n/2+1 requires n even.
  - The set is MP_n = {(x_m, y_k) : m = 1,…,n+1; k = 1,…,n/2+1}, with x_m = cos(mπ/(n+2)).
  - The ordinate depends on the parity of m:
    - y_k = cos(2kπ/(n+3)) if m is odd;
    - y_k = cos((2k−1)π/(n+3)) if m is even.
  - #MP_n = (n+1)(n+2)/2 = dim P²_n, and MP_n is unisolvent for P²_n (p. 32; in-text cites "[5, 6]").
- **Construction 1, Lissajous** (§2.1, pp. 33–34).
  - The curve is γ_{n,1}(t) = (−cos((n+3)t), −cos((n+2)t)), eq. (1) on p. 33. It lies on the algebraic curve T_{n+p}(x) − T_n(y) = 0.
  - Sampling at t_k = πk/((n+2)(n+3)), k = 0,…,(n+2)(n+3), gives Pad_{n+2}.
  - MP_n is Pad_{n+2} with the edge points removed, "including the two vertices touched by the Padua points" (p. 34).
  - Remark 1 (p. 34): the reflected curve (cos((n+3)t), cos((n+2)t)) gives −MP_n, the upside-down set. This is a *different* set.
- **Construction 2, zeros** (§2.2, pp. 34–35, display unnumbered).
  - **Printed:** MP_n are the zeros of R^n_j(x₁,x₂) := U_j(x₁)U_{n−j}(x₂) + U_{n−j−1}(x₁)U_j(x₂), 0 ≤ j ≤ n.
  - **Flag F3:** the printed formula is wrong by an index shift. It does **not** vanish on MP_n (CHECKED-NUM, n = 2…6).
    - The polynomials that vanish are R^{n+1}_j = U_j(x)U_{n+1−j}(y) + U_{n−j}(x)U_j(y), 0 ≤ j ≤ n+1, with U_{−1} := 0, so j = n+1 gives U_{n+1}(x) (§6.3).
    - This is the printed text, not a rendering artefact; verified on the staged PDF.
  - p. 35: MP_n are "equally spaced" in the Dubiner metric.
- **Construction 3** (§2.3, pp. 35–37): two interlacing rectangular grids, via Floater, JAT 222 (2017), Thm 1, quoted as BBDM Thm 1. BBDM take (μ,ν) = (n,n) and (r,s) = (n,n−1).
- **Orthonormal basis and kernel** (§3, p. 37).
  - U_j(cosθ) = sin((j+1)θ)/sinθ, with ∫U_jU_k√(1−x²)dx = (π/2)δ_jk and max|U_j| = j+1 at ±1.
  - P_{i,j} = Û_i(x)Û_j(y) with Û = √(2/π) U, for 0 ≤ i+j ≤ n, is an orthonormal basis of P²_n.
  - Equivalently, with the probability-normalized measure (4/π²)√(1−x²)√(1−y²)dxdy, the products U_i(x)U_j(y) are orthonormal.
- **Interpolant** (§3, pp. 37–38, unnumbered; restated in Thm 2, p. 43). It is "classical", cf. Sloan 1995:
  - L_n f(x,y) = Σ_{m,k} ω_{m,k} K_n((x,y),(x_m,y_k)) f(x_m,y_k);
  - K_n(P,Q) = Σ_{i=0}^{n} Σ_{j=0}^{n−i} U_i(x_P)U_j(y_P)U_i(x_Q)U_j(y_Q) is the reproducing kernel of P²_n for the normalized second-kind product measure.
  - So the fundamental Lagrange polynomial is ℓ_{m,k}(x,y) = ω_{m,k} K_n((x,y),(x_m,y_k)).
  - CHECKED-NUM: ℓ_{m,k}(node) = δ for n ≤ 40.
- **Cubature, Theorem 2** (§3.2, p. 43, eqs. (7)–(9); v1 (10)–(12)). For every p ∈ P²_{2n}:
  - (4/π²) ∫_Q p(x,y) √(1−x²)√(1−y²) dx dy = C_n Σ_{m,k} (1−x_m²)(1−y_k²) p(x_m,y_k) = C_n Σ sin²w_m sin²v_k p(cos w_m, cos v_k), eq. (7), with C_n = 8/((n+2)(n+3));
  - hence ω_{m,k} = C_n(1−x_m²)(1−y_k²), eq. (8).
  - Eq. (9) gives the Lebesgue function in this form.
  - **Weight convention:** the second-kind weight √(1−x²)√(1−y²) sits in the *numerator*.
    - Verified on the staged PDF, p. 43.
    - One WebFetch rendering of R1 put it in the denominator; that rendering was wrong. CHECKED-NUM: exact on P²_{2n} for the second-kind weight, fails for the first-kind weight.
  - The rule is **not** exact at degree 2n+1 (CHECKED-NUM).
  - Proof route: [BCDMVX 2006, Thm 1] applied to q = p(1−x²)(1−y²).
  - Remark 2 (p. 44) contrasts this with Padua points, which need the extra condition (12) (v1 (15)): the Padua rule fails for T_{2n}(y).
- **Lebesgue function** (eq. (2), p. 38, with weights ω_{m,k}; eq. (9), p. 43, explicit; v1 (3), (12)):
  - λ_n(x,y) = C_n Σ_{m=1}^{n+1} Σ_{k=1}^{n/2+1} (1−x_m²)(1−y_k²) |K_n((x,y),(x_m,y_k))|;
  - Λ_n^MP = max_Q λ_n (p. 38, unnumbered).
- **Trigonometric form** (§6, p. 52, unnumbered). For θ, φ ∈ [0,π], λ_n(cosθ, cosφ) = Σ_{m,k} K̃_n, where:
  - K̃_n = C_n sin w_m sin v_k · |Σ_{0≤i+j≤n} sin((i+1)w_m) sin((i+1)θ) sin((j+1)v_k) sin((j+1)φ)| / (sinθ sinφ);
  - w_m = mπ/(n+2), and v_k = 2kπ/(n+3) for m odd, (2k−1)π/(n+3) for m even.
- **Lemma 1** (p. 45): λ_n(x,y) = λ_n(−x,y) on Q.
  - The proof uses n even, so that m ↦ n+2−m preserves parity and MP_n is symmetric in x. CHECKED-NUM.
  - §7.1 (p. 64) refers to this result as "Lemma 15".
- **EMP points** (§7, p. 63, Fig. 5, citing CDMV 2005):
  - x^EMP = x^MP/α_n and y^EMP = y^MP/β_n, with α_n = cos(π/(n+2)) and β_n = cos(π/(n+3));
  - BBDM say the values are "lower but still show a n² growth". No theorem.
- **"MPX" / Xu-type variants.** **Not defined in BBDM.**
  - Remark 3 (p. 63) only mentions:
    - Xu's "generalization of Morrow–Patterson points" for weights |x−y|^{2a+1}|x+y|^{2b+1}(1−x²)^{±1/2}(1−y²)^{±1/2}, a, b ≥ −1/2 (Xu JAT 164 (2012) 6–30 and JAT 214 (2017) 49–68), with reported growth O(n^{2max{a,b}+1}) for a, b > −1/2 and O(log² n) for a = b < −1/2;
    - n² growth "not for Morrow–Patterson points but for the so-called Xu points" with the second-kind weight (Liu–Zhu 2022, Thm 1).
  - So the natural "MPX" candidates are Xu's 2012/2017 generalized MP points, which neither BBDM nor this note define. Those Xu papers were not read.
  - LIT-378's "Xu-type MPX variants remain open" is **not supported** by the BBDM text as read. Treat "MPX" as a repository label without a BBDM definition.
- **Meshes** (§4, pp. 46–48; Thm 3, p. 47, eqs. (13)–(14)).
  - 𝒜_ν = MP_ν ∪ {two corners}. ℬ_ν = MP_ν ∪ {two near-corner points}.
  - Both are defined separately for ν even and ν odd, so BBDM implicitly use MP_ν for odd ν here without stating a formula.
  - Thm 3 ((13); v1 (16)): ‖p‖_Q ≤ (cos(π/μ))^{-1} min{‖p‖_{𝒜_{⌈μn⌉}}, ‖p‖_{ℬ_{⌈μn⌉}}, ‖p‖_{MP_{⌈2μn⌉}}} for μ > 2.
  - The Dubiner covering radii are π/(ν+2) for 𝒜 and ℬ, and 2π/(ν+3) for MP_ν.

### 1.2 Main results, exactly

- **Prop. 1** (p. 38, eq. (3); v1 (6)). This is the hyperinterpolation route via De Marchi–Sommariva–Vianello, DRNA 7 (2014):
  - Λ_n^MP ≤ (1/(6√10)) √((n+1)(n+2)(n+3)(n+4)(2n²+10n+15)) = O(n³).
  - The square root is present in print (verified from the page render). The p. 38 text adds that (3) holds for any hyperinterpolation operator for the product second-kind Chebyshev measure.
- **Sub-square bound** (§6, p. 52, unnumbered): λ_n(x,y) ≤ 4C_n(n+1)³(n/2+1) = O(n²) for (x,y) ∈ [−√3/2, √3/2]².
  - Explicit, but only interior: it uses θ, φ ∈ [π/6, 5π/6].
  - The same p. 52 says the same argument gives O(n²) on [−δ,δ]² for any fixed δ ∈ (0,1).
  - **"Can be improved" remark** (p. 53, first lines, immediately before Thm 4): this estimate "can be improved" but needs more tedious reasoning, "as seen in the proof of the following theorem".
    - It refers to the sub-square estimate.
    - It is not a statement that the O(n²) bound of Thm 4 is improvable.
  - Near the end of the proof of Thm 4 (p. 63) they also state λ_n(cosθ, cosφ) ≤ O(n) for θ, φ ∈ (δ, π−δ).
- **Theorem 4** (p. 53, unnumbered; v1 (22)): verbatim content, "The Lebesgue constant of the Morrow–Patterson points has the upper bound Λ_n^MP ≤ O(n²)".
  - **No explicit constant**, in the statement or in the proof.
  - The proof reduces, via (14) (Thm 3 mesh inequality) and Lemma 1, to θ, φ ∈ [c/n, π−c/n] with "c > 0 a fixed constant independent of n" (p. 53), WLOG θ ∈ [c/n, π/2].
  - Tools:
    - Lemmas 2–5 (closed-form trigonometric sums, eqs. (15)–(17));
    - Lemma 6, the closed form of Υ_n(x,y,z) = Σ_{j=0}^n sin((j+1)x) sin((j+1)y) sin((2n−2j+3)z) as eight cosine quotients;
    - kernel estimates (18)–(21), O(n²) or O(n) per kernel row, and (22)–(27).
- **Lower bound:** none in BBDM. BBDM do not cite the JAT lower-bound paper.
- **Stated open problems** (§7.1, p. 64):
  1. Prove λ(x,y) = λ(−x,−y). They say the numerics suggest symmetry "not only for y, but also to the origin".
  2. Prove that the Lebesgue constant is attained at each corner of Q.
  - §7.1 cites "Lemma 15" for the x-symmetry; this means Lemma 1.

### 1.3 Numerics (BBDM)

- **§3.1 and Fig. 3** (p. 38): for n = 2, 4, …, 60, Λ_n^MP is "well-fitted" below by (0.7n+1)² and above by (0.75n+1)². No table.
- **§7 and Fig. 4** (p. 63): n = 30 Lebesgue function on a Chebyshev–Lobatto grid of 10,000 points. For 2 ≤ n ≤ 30 the constant is compared with (n+1)(n+2)/2, and "both curves are almost overlapping".
  - The text says the constant is numerically attained at each corner of Q, with computed values (n+1)(n+2)/2. Verified in print, p. 63.
  - **Flag F1:** this is not exact (§6.2).
- **Code** (`Leb_MP.m`, read via WebFetch):
  - degrees `2:2:30`; 101×101 Chebyshev–Lobatto target grid;
  - Lebesgue constant computed as `norm(V_mp'\V_leb',1)` with a Chebyshev Vandermonde;
  - `leb_mp_true = (deg+1)*(deg+2)/2` is only a reference curve.
  - The WebFetch rendering reports that the plotted "Lebesgue function" is `sum(abs(V_leb'))`, i.e. basis values rather than Lagrange values. **That would make Fig. 4-top and the symmetry/corner observations unreliable** (flag F2; reconfirm from the raw file).
  - `ext_morr_patt.m` builds the EMP points exactly as in §1.1.

---

## 1b. Source A′: Beberok 2025, the published lower bound

- **Citation.** T. Beberok, "A lower bound for the Lebesgue constant of the Morrow–Patterson points", *J. Approx. Theory* **311** (2025), article 106191, DOI [10.1016/j.jat.2025.106191](https://doi.org/10.1016/j.jat.2025.106191). Single author per Crossref and Semantic Scholar.
- **Reading.** The **orchestrator** read the full HTML on ScienceDirect through institutional access on 2026-11-14. This literature subagent did **not** read it. The content below is the orchestrator's report, paraphrased; page and section locators were not supplied.
- **Main result.** Theorem 0.1: Λ_n^MP ≥ c·n² for MP points. The constant c is stated existentially.
- **Proof route.**
  - Evaluate the Lebesgue function at the corner (1,1), using the weights 8 sin²w_m sin²v_k/((n+2)(n+3)).
  - Closed form (2) for the corner kernel K(1,1,w_m,v_k) := Σ_{i+j≤n} (i+1)(j+1) U_i(cos w_m) U_j(cos v_k):
    - K = (−1)^m (2 + cos w + cos v)/(2 (cos v − cos w)³) + (−1)^m (2n+5)/(4 (cos w − cos v)²), at the nodes w = w_m, v = v_k.
    - **CHECKED-NUM by me** against the direct double sum: relative difference ≤ 2·10⁻³⁷ at 40-digit precision over all nodes, n = 4 and 10.
  - The final inequality, as transcribed by the orchestrator, gives for n ≥ 8:
    - Λ_n ≥ (√3−1)² (n/4−1)(2n+5)(n+2)(n+3) / (16π² (n/2+n+2)²);
    - this is about 7.5·10⁻⁴·n² asymptotically, an explicit but unstated constant.
    - The odd-looking denominator term "(n/2+n+2)" is as transcribed; re-check against the HTML.
- **Other content.**
  - Fig. 1 compares Λ_n with (n+1)(n+2)/2.
  - The paper cites Xu JAT 164 (2012) and JAT 214 (2017) as generalizations of MP points.
- **Consequences for X2.**
  - G4 ("Λ_MP ≥ c n², explicit c, n₀") is already essentially in the literature: a constant can be read off for n ≥ 8, though it is tiny.
  - Remaining novelty can only be:
    - a near-sharp constant, since the measured λ(1,1)/n² is about 0.53;
    - the exact value or asymptotics of λ_n(1,1);
    - the argmax location (flag F1);
    - lim Λ/n².
  - The novelty gate must cite this paper.

## 2. Source B: Morrow–Patterson 1978

- **Citation.** C. R. Morrow, T. N. L. Patterson, "Construction of algebraic cubature rules using polynomial ideal theory", *SIAM J. Numer. Anal.* **15**(5) (1978) 953–976, DOI [10.1137/0715062](https://doi.org/10.1137/0715062).
  - Volume, issue, pages and DOI were verified via Crossref (print Oct 1978; 81 citations in Crossref).
- **Status: NOT READ.** epubs.siam.org and doi.org returned client errors, JSTOR (stable/2156719) showed a bot check that was not bypassed, and zbMATH and dblp were blocked.
- The node definition used here is taken from BBDM (§1.1) and CDMV 2005 (§3). They agree, and both cite MP 1978 for it.
- Not verified from MP 1978:
  - their original indexing and orientation;
  - whether they treat odd degrees;
  - the claimed minimality, i.e. dim P_n nodes with exactness 2n for the second-kind product weight.

## 3. Source C: Caliari–De Marchi–Vianello 2005 (CDMV)

- **Citation.** M. Caliari, S. De Marchi, M. Vianello, "Bivariate polynomial interpolation on the square at new nodal sets", *Appl. Math. Comput.* **165**(2) (2005) 261–274, DOI [10.1016/j.amc.2004.07.001](https://doi.org/10.1016/j.amc.2004.07.001).
  - Verified from the PDF header ("© 2004 Elsevier") and OpenAlex (W2109990880, 98 citations).
- **URL read:** https://profs.scienze.univr.it/caliari/pdf/CDMV05.pdf (author copy with the journal header), through WebFetch, on 2026-11-14. Read: §3.3–3.5, Table 4, Figs. 1, 2, 4 and the conclusions.
- **Gaps:** the rendering lost the minus signs of the error exponents in Tables 4–6; page numbers are from the rendering.
- **Definitions.**
  - MP: §3.3, eq. (7), p. 269. Identical to BBDM, n positive even, N = (n+1)(n+2)/2.
    - The text credits the explicit Lagrange formula to Xu's Christoffel–Darboux formulas, in terms of second-kind Chebyshev polynomials. It gives no equation.
  - EMP: §3.4, eq. (8), pp. 269–270. MP scaled by 1/a_n in x and 1/b_n in y, with a_n = cos(π/(n+2)) and b_n = cos(π/(n+3)).
    - Unisolvence follows because the Vandermonde matrix is the MP one with columns scaled.
  - "PD" (2005 Padua, the original non-standard family): §3.5, eq. (9), p. 270. x_m = cos((m−1)π/n), and y = cos((2k−1)π/(n−1)) or cos((2k−2)π/(n−1)) by the parity of m. Not used for X2.
- **Published Lebesgue constants.**
  - Table 4 (p. 271, "Interpolation errors for the Franke function"), K_n columns, values "rounded to the nearest integer":

    | n | MP | EMP | PD |
    |---|---|---|---|
    | 34 | 649 | 237 | 11 |
    | 48 | 1264 | 456 | 13 |
    | 62 | 2082 | 746 | 14 |
    | 76 | 3102 | 1106 | 15 |

  - Tables 5–6 contain no K columns.
- **Fitted growth** (Fig. 4, p. 271, degrees up to 60, least squares):
  - MP: (0.7n+1.0)²;
  - EMP: (0.4n+0.9)²;
  - PD: ((2/π)log(n+1)+1.1)².
  - The text states K_n^MP = O(n²), based on experiment only, and that Bos proved O(n⁶).
- **Where the maximum lies:** not reported. Constants were computed by maximizing over grids.
- **Open points stated:** asymptotic analysis of the MP, EMP and PD constants (§4).
- Internal inconsistency: a §3.4 sentence says K(MP) < K(EMP), contradicting Fig. 4 and Table 4. Probably a typo.

## 4. Source D (context): Białas-Cież–De Marchi–Suder, arXiv 2605.23299 v1 (LIT-388)

- Re-read today only for its MP content, https://arxiv.org/pdf/2605.23299.
- §3.2 (p. 8) gives an **all-n** MP definition (odd n allowed): MP_n = {(μ_j, η_k)}, with μ_j = cos(jπ/(n+2)) and η_k as in BBDM.
  - The k-range is ⌊n/2⌋+1+δ_j, with δ_j = 1 for even j when n is odd.
  - The rendering of the δ_j rule is garbled, and so is the j-range: it shows j = 1..n, but the count requires j = 1..n+1.
  - It also states MP_n = Pad_{n+2} \ {edge points}.
  - CHECKED-NUM: the "Pad_{n+2} minus edges" description gives (n+1)(n+2)/2 unisolvent points for n = 1…12 and coincides with BBDM's formula for even n (§6.4).
- It cites only BBDM and Liu–Zhu 2022 for the O(n²) growth. **No lower bound, and no citation of the JAT lower-bound paper.**
- Table 4: counts of local maxima for MP, n = 3–8. No Lebesgue-constant values.

---

## 5. Forward-citation search log (2026-11-14)

| # | Query / endpoint | Outcome |
|---|---|---|
| 1 | WebSearch `Beberok Białas-Cież De Marchi "Morrow-Patterson" Lebesgue constant Constructive Approximation` | arXiv 2412.14595, arXiv 2605.23299, De Marchi drafts (draftMP-R1); nothing new on lower bounds |
| 2 | Crossref `query.bibliographic=On the Lebesgue constant of the Morrow-Patterson points` | **Beberok, "A lower bound for the Lebesgue constant of the Morrow–Patterson points", JAT 311 (2025) 106191**; BBDM Constr. Approx. 63(1) 31–65 |
| 3 | Crossref works/10.1016/j.jat.2025.106191 | metadata + 13 references (see §0); no abstract |
| 4 | ScienceDirect pii S0021904525000498 (full, abs), linkinghub, Elsevier API | blocked / redirect stub / denied (not pursued) |
| 5 | Semantic Scholar DOI:10.1016/j.jat.2025.106191 | single author Beberok, abstract null, citationCount 0 (first call); openAccessPdf wrongly points to the BBDM Springer PDF |
| 6 | OpenAlex works/doi:10.1016/j.jat.2025.106191 | rate-limited; works/doi:10.1007/s00365-025-09710-x → W4410230682 (merged record, cited_by 0) |
| 7 | OpenAlex `filter=cites:W4410230682` | 0 results |
| 8 | Semantic Scholar DOI:10.1007/s00365-025-09710-x citations | 1 citing paper: arXiv 2605.23299 (no lower bound) |
| 9 | OpenAlex `filter=cites:W2109990880` (CDMV 2005), from 2018 | 38 results, all titles screened; MP/Lebesgue-relevant: the JAT lower-bound paper (#6 in list, under merged DOI), Liu–Zhu 2022 J. Math. 5649969 (upper bound O((n+2)²) for interpolation at common zeros of product second-kind Chebyshev polynomials; relation to MP not verified), De Marchi 2022 CMA survey (LIT-377), Kolomoitsev–Lomako AMC 2021 (LIT-379). No other lower-bound result |
| 10 | OpenAlex `search="Morrow-Patterson"` | 35 results screened; relevant: JAT lower-bound paper, Deterding 2017 (MP nodes from Geronimus polynomials, DOI 10.1353/mpr.2017.0005), Harris 2014 JAT (Lagrange polys/kernels/cubature), Cao–Ghimire–Wang 2022 PAMS, Noskov 1992; none (by title) is a Lebesgue lower bound besides the JAT paper |
| 11 | OpenAlex `raw_author_name.search:Beberok`, from 2023 | no arXiv version of the JAT lower-bound paper; other Beberok items are Bernstein/Markov inequalities |
| 12 | WebSearch `Beberok "A lower bound for the Lebesgue constant of the Morrow-Patterson points"`; `"Morrow-Patterson" "lower bound" Lebesgue constant Beberok 2025` (extended); `... "Journal of Approximation Theory" 311 ...` (extended); `"lower bound for the Lebesgue constant of the Morrow" abstract "we prove"` | only ResearchGate 391623684 (blocked) and already-known items; Tao arXiv 2603.21453 (univariate only, not relevant) |
| 13 | De Marchi paper directory https://www.math.unipd.it/~demarchi/papers/ | MP-named files: draftMP-R1, draftMP_RM (= BCDS 2605.23299 draft), mp.pdf (= DRNA 2014), LebesgueMP_Nov2024 (= BBDM draft), PaperBDeMP (unrelated RBF); no lower-bound preprint |
| 14 | Vanderbilt "Constructive Functions 2025" abstract book | Beberok talk = BBDM upper bound only |
| 15 | arXiv author page / export API for Beberok; dblp jat/Beberok25 | rate-limited / robots-disallowed / bot check — not read |

- **Outcome.** One matching result: Beberok, JAT 311 (2025) 106191. The orchestrator subsequently read it via institutional access (§1b).
- Apart from it, no other lower-bound result for Λ_MP was found in the documented search.

---

## 6. My numerical checks (CHECKED-NUM; reader-produced, not literature)

All checks are double precision, using BBDM's node formula (even n unless stated). Lagrange values were computed two ways, which agree to about 1e−12:
- (a) the kernel ω_{m,k}K_n;
- (b) solving the T_iT_j Vandermonde system.

### 6.1 Cubature and interpolation basics

- #MP_n = dim P²_n and the Vandermonde matrix has full rank, for n = 2…10. The T-Vandermonde condition number is 3.6 at n = 2 and 59 at n = 24.
- The weights C_n(1−x²)(1−y²) sum to 1. The rule is exact for U_aU_b, a+b ≤ 2n, against the normalized second-kind measure, with error ≤ 2e−15.
- At a+b = 2n+1 the rule fails with error 1.
- For the first-kind measure (T_aT_b) the rule fails with error 0.5.

### 6.2 Corner values

- **Independent re-check with mpmath** (40 digits). This uses the published formulas only:
  - nodes as on pp. 31–32;
  - λ_n = C_n Σ (1−x_m²)(1−y_k²)|Σ_{i+j≤n} U_i(x_m)U_j(y_k)U_i(x)U_j(y)|, eq. (9);
  - U evaluated by the three-term recurrence, so the corners need no special-casing.

  | n | λ(±1,1) | λ(±1,−1) | dim = (n+1)(n+2)/2 | ratio λ(1,1)/dim |
  |---|---|---|---|---|
  | 2 | 5.8455592331681269677 | 3 (to 4.6e−41) | 6 | 0.9742598722 |
  | 4 | 14.840835466034328742 | 5 (to 9.2e−41) | 15 | 0.9893890311 |
  | 6 | 28.025027605997461565 | 7 (to 3.7e−40) | 28 | 1.000893843 |
  | 8 | 45.387845253668956996 | 9 (to 3.7e−40) | 45 | 1.008618783 |
  | 10 | 66.918451980140371957 | 11 (to 3.7e−40) | 66 | 1.013915939 |

  - So λ(±1,−1) = n+1 holds to 40 digits.
  - The ratio to dim is below 1 for n ≤ 4, crosses 1 between n = 4 and 6, and approaches about 1.033 only for large n (table below).
  - "λ(1,1) ≈ 1.033·dim" is therefore an asymptotic description, not valid for small n.
- Double-precision computation: λ_n(1,−1) = λ_n(−1,−1) = n+1, exactly to rounding, for n = 2…40.
- λ_n(±1,1) and Chebyshev–Lobatto grid maxima ((8n+41)² grid):

| n | λ(±1,1) | grid max (location) | (n+1)(n+2)/2 |
|---|---|---|---|
| 2 | 5.845559 | same, corner (±1,1) | 6 |
| 4 | 14.840835 | same | 15 |
| 6 | 28.025028 | same | 28 |
| 8 | 45.387845 | same | 45 |
| 10 | 66.918452 | same | 66 |
| 12 | 92.608814 | same | 91 |
| 20 | 236.900953 | same | 231 |
| 24 | 333.929638 | same | 325 |
| 30 | 510.54221 | same | 496 |
| 40 | 887.736967 | same | 861 |

- Further corner values λ(1,1), not grid-checked:

| n | λ(1,1) | ratio to n² | ratio to dim |
|---|---|---|---|
| 34 | 649.005 | | |
| 48 | 1263.994 | | |
| 60 | 1952.52 | | |
| 62 | 2081.761 | | |
| 76 | 3102.258 | | |
| 50 | 1368.40 | 0.5474 | 1.0320 |
| 80 | 3431.05 | 0.5361 | 1.0331 |
| 100 | 5323.27 | 0.5323 | 1.0334 |
| 120 | 7629.14 | 0.5298 | 1.0336 |

- The n = 34, 48, 62, 76 values round to **CDMV Table 4** (649, 1264, 2082, 3102).
- EMP: λ(±1,1) = 237.18, 456.01, 745.63, 1105.98 at n = 34, 48, 62, 76, matching CDMV (237, 456, 746, 1106). For EMP, (±1,−1) are nodes, so λ = 1 there.
- The corner value has an explicit form, since U_i(1) = i+1:
  - λ_n(1,1) = C_n Σ_{m,k} (1−x_m²)(1−y_k²) |Σ_{i+j≤n} (i+1)(j+1) U_i(x_m) U_j(y_k)|.
  - This is the natural single-point candidate for a lower bound c·n². The MEASURED ratio λ(1,1)/n² is about 0.53 at n = 120 and still decreasing slowly.
- Interior spot checks at n = 2, 4, 6, 12, 24 also give λ(0.3,0.7) ≠ λ(−0.3,−0.7). So there is **no central symmetry**.
  - This is consistent with Remark 1 (−MP_n ≠ MP_n), since (x,y) → (x,−y) swaps the two column-parity classes of ordinates.

### 6.3 Zero-set polynomials

- With U_{−1} = 0, the polynomials vanishing on MP_n (n = 2, 4) include:
  - R_j = U_j(x)U_{n+1−j}(y) + U_{n−j}(x)U_j(y), for 0 ≤ j ≤ n, with coefficient exactly 1;
  - U_{n+1}(x).
- The transcription "U_j(x)U_{n−j}(y) + U_{n−j−1}(x)U_j(y)" does not vanish there.
- **Flag F3:** confirmed on the staged PDF (p. 34). The printed R^n_j is wrong; the vanishing family is R^{n+1}_j.

### 6.4 Odd n

- "Pad_{n+2} minus edges" means: the j+k odd class of {(cos(jπ/(n+2)), cos(kπ/(n+3))) : 1 ≤ j ≤ n+1, 1 ≤ k ≤ n+2}.
- This gives (n+1)(n+2)/2 unisolvent points for n = 1…12, and equals BBDM's set for even n.
- For odd n the large corners are (1,±1), with λ = 2.914, 9.819, 20.91, 36.185, 55.633, 79.244 for n = 1, 3, 5, 7, 9, 11. The other two corners give n+1.
- BBDM's cubature theorem and Lemma 1 are stated for even n only.

---

## 7. Conventions to implement (self-contained specification)

1. **Degree.** n ≥ 2 even [BBDM Intro p. 31; CDMV (7) p. 269]. Odd n only via item 2b [BCDS §3.2; BBDM §2.1 / §4, implicit].
2. **Nodes.**
   - **2a, even n** [BBDM Intro; CDMV (7); BBDM code `ext_morr_patt.m` without scaling]: for m = 1..n+1 and k = 1..n/2+1, x_m = cos(mπ/(n+2)); y = cos(2kπ/(n+3)) if m is odd, cos((2k−1)π/(n+3)) if m is even.
   - **2b, all n**: the set {(cos(jπ/(n+2)), cos(kπ/(n+3))) : 1 ≤ j ≤ n+1, 1 ≤ k ≤ n+2, j+k odd}. This equals 2a for even n [BBDM §2.1; CHECKED-NUM].
   - Count: (n+1)(n+2)/2.
   - Symmetric under x → −x for even n [BBDM Lemma 1]. Not symmetric under y → −y.
   - The corners (±1,±1) are not nodes.
3. **EMP nodes** [CDMV (8) pp. 269–270; BBDM §7]: divide x by cos(π/(n+2)) and y by cos(π/(n+3)). Then (±1,−1) become nodes for even n [CHECKED-NUM].
4. **MPX.** **Not defined** in BBDM, CDMV or BCDS. Candidate sources are Xu 2012/2017 JAT ("Minimal cubature rules … I/II"), cited by the JAT lower-bound paper, and Liu 2019 / Liu–Zhu 2022. Not read.
5. **Space and basis.**
   - Interpolate in P²_n (total degree), unisolvent [BBDM Intro, citing BCDMVX 2006, BDMVX 2007, Bos 2001; CHECKED-NUM n ≤ 12].
   - Basis {U_i(x)U_j(y) : i+j ≤ n}, orthonormal for dμ = (4/π²)√(1−x²)√(1−y²)dxdy [BBDM §3].
   - For an implementation in product Chebyshev T-polynomials, use U_i = 2Σ_{l≡i (2), 0<l≤i} T_l + [i even]·T_0, or simply solve the T_iT_j Vandermonde system (well conditioned: about 59 at n = 24).
6. **Cubature** [BBDM Thm 2, p. 43, (7)–(8)]:
   - ∫ p dμ = Σ ω_{m,k} p(node), with ω_{m,k} = 8(1−x_m²)(1−y_k²)/((n+2)(n+3)).
   - Exact on P²_{2n}, not on P²_{2n+1} [CHECKED-NUM].
   - BBDM's weights 1/ω = Σ_{i+j≤n} U_i²U_j² (Christoffel form, §3) agree with this.
7. **Fundamental polynomials** [BBDM §3]: ℓ_{m,k}(x,y) = ω_{m,k} Σ_{i+j≤n} U_i(x)U_j(y)U_i(x_m)U_j(y_k).
8. **Lebesgue function and constant** [BBDM (2) p. 38, (9) p. 43]: λ_n = Σ|ℓ_{m,k}| and Λ_n^MP = max over Q.
   - Trigonometric form [BBDM §6]: see §1.1.
9. **Literature reference values** (G0):
   - CDMV Table 4: MP K_n = 649, 1264, 2082, 3102 and EMP K_n = 237, 456, 746, 1106 at n = 34, 48, 62, 76. Reproduced as top-corner values (§6.2).
   - BBDM §3.1 envelope: (0.7n+1)² ≤ Λ_n ≤ (0.75n+1)² for even n ≤ 60. Consistent with §6.2; for example n = 60 gives 1849 ≤ 1952.5 ≤ 2116.

### Disagreement / verification flags

- **F1.** BBDM §7 says the corner values *are* (n+1)(n+2)/2 and that the maximum sits at *each* corner. Measured: the values are not dim (ratio 0.974 at n = 2, 1.014 at n = 10, about 1.033 for large n; mpmath table in §6.2), the maximum is at the two y = +1 corners only, and the other corners give n+1. The open problem "λ(x,y) = λ(−x,−y)" is false numerically. Reconfirm with exact or interval arithmetic before recording a PD-N.
- **F2.** The `Leb_MP.m` plotting line, as rendered, plots Σ|basis| instead of Σ|ℓ|. This may explain F1. Reconfirm from the raw file.
- **F3.** The §2.2 zero polynomials are printed with an index shift (p. 34; confirmed on the staged PDF). Use R^{n+1}_j (§6.3).
- **F4.** Resolved: the weight is in the numerator in print (p. 43).
- **F8.** BBDM in-text citation numbers are offset from their reference list (§1).
- **F5.** MP 1978 is not read, so orientation and odd-degree conventions are not checked against the original.
- **F6.** OpenAlex merges BBDM with the JAT lower-bound paper. Cite them as two distinct works.
- **F7.** LIT-378 corrections:
  - the "can be improved" remark belongs to the §6 sub-square estimate;
  - BBDM do not define or leave open "MPX" variants;
  - BBDM's stated open problems are the symmetry and corner-location problems;
  - a lower bound has meanwhile been published: Beberok, JAT 2025, §1b, read by the orchestrator.

## 8. Sources NOT read (for institutional-browser fetch)

1. ~~Beberok, JAT 311 (2025) 106191.~~ Now read by the orchestrator (§1b). Section and page locators are still to be recorded by the orchestrator.
2. Morrow–Patterson, SIAM J. Numer. Anal. 15 (1978) 953–976. https://doi.org/10.1137/0715062. Needed for the node definition, the original indexing and the minimality claim.
3. Liu–Zhu, J. Math. 2022, 5649969. https://doi.org/10.1155/2022/5649969. Need to determine whether its nodes are MP or Xu-type second-kind, and its exact bound.
4. Liu, Acta Math. Hungar. 159 (2019) 618–. https://doi.org/10.1007/s10474-019-00988-5. Possible source for an "MPX" / Xu-type definition.
5. Xu, JAT 164 (2012) 6–30, https://doi.org/10.1016/j.jat.2011.09.003, and Xu, JAT 214 (2017) 49–, https://doi.org/10.1016/j.jat.2016.11.002. Possible MPX definitions.
6. ~~BBDM published PDF.~~ Read from the staged copy; locators in §1 are exact.
7. The raw `Leb_MP.m` and any `morr_patt.m` in https://github.com/demarchi-github/MP-points (flag F2; `morr_patt.m` was not listed in the repo view).
8. Optional context: Deterding 2017 (https://doi.org/10.1353/mpr.2017.0005); Harris 2014 JAT (https://doi.org/10.1016/j.jat.2014.10.017).
