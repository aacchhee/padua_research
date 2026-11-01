# mz-classical-mz-screen — historical inequalities requiring exact hypotheses

- Access/read date: 2026-10-31. Reader: Codex; gpt-6.1-sol, high (explicit orchestrator assignment).
- Status: selected publisher abstracts/author bibliography. Exact theorem coverage remains **FULLTEXT UNVERIFIED** as specified below.

## Source records

### LIT-050 — Lubinsky–Máté–Nevai 1987

- Citation: D. S. Lubinsky, A. Máté, P. Nevai, *Quadrature sums involving pth powers of polynomials*, SIAM J. Math. Anal. 18(2) (1987), 531–544, <https://doi.org/10.1137/0518041>.
- Coverage: primary publisher abstract, not full text. The abstract reports quadrature-sum estimates for p>0 under suitable node spacing and weight bounds, including generalized Jacobi and Freud weights.
- Locator: publisher Abstract. Exact constants, degree/sample ratio and converse inequality not extracted.
- Relation/gap: check CC angular spacing, weights, endpoint scale and degree range. The supplied claim that this only handles a small fixed ratio is **FULLTEXT UNVERIFIED**. No M3 exclusion or proof follows from the abstract.

### LIT-051 — Mastroianni–Totik 2000

- Citation: G. Mastroianni, V. Totik, *Weighted Polynomial Inequalities with Doubling and A-infinity Weights*, Constr. Approx. 16 (2000), 37–71, <https://doi.org/10.1007/s003659910002>.
- Coverage: primary publisher abstract/metadata. It concerns trigonometric and algebraic weighted inequalities under doubling or stronger A-infinity assumptions; exact MZ theorem not read.
- Locator: publisher Abstract; fulltext **FULLTEXT UNVERIFIED**.
- Relation/gap: M3 is a strong prior-art risk. Extract exact sampling theorem and translate CC weights before distinguishing “some oversampling” from every fixed theta<1; a generic positive upper constant is insufficient for eta<1.

### LIT-052 — Lubinsky 1998 survey

- Citation: D. S. Lubinsky, *Marcinkiewicz–Zygmund Inequalities: Methods and Results*, in *Recent Progress in Inequalities*, 1998, pp. 213–240, DOI <https://doi.org/10.1007/978-94-015-9086-0_12>.
- Author link: <https://lubinsky.math.gatech.edu/Research%20papers/MarZygSurveyPaper137.pdf> (listed as paper 137 on <https://lubinsky.math.gatech.edu/SelectedPapers.html>).
- Coverage: author bibliography and PDF availability checked. Connector reports 35 PDF pages but no extracted text; screenshot responses did not provide inspectable page content to this reader. **FULLTEXT UNVERIFIED**.
- Relation/gap: trace direct/converse inequalities, Chebyshev extrema and endpoint norm behavior; follow exact references instead of assuming the supplied summary exhausts the survey.

## Coverage conclusion

These are source-discovery records, not a claim that historical MZ results fail to cover CC. M3's novelty is unresolved. The literature kill test is the exact hypothesis and weight translation, not terminology matching.

## History

2026-10-31: primary abstract/bibliography screen; exact theorems remain named gaps.

## 2026-11-01 fulltext reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5 (orchestrator). Access: publisher PDF via AC's NTNU institutional access in AC's built-in browser, text extracted in-page with pdf.js and read in the session only; no PDF or fulltext extract stored anywhere in the repository. Rules `9739a0c`.

### LIT-051 — Mastroianni–Totik 2000 read

- Coverage: complete article (35 pp.) keyword-indexed, with §4.2 (pp. 46–47, Theorem 4.2, weak Marcinkiewicz inequality) and §7 (pp. 63–66, translation to [−1,1] including the algebraic Marcinkiewicz inequality) read in full.
- Statement (p. 65, algebraic Marcinkiewicz inequality, stated as the translation of Theorem 4.2 under x=cos t): for a doubling weight w on [−1,1] and 1≤p<∞ there are M, C such that ∫|p_n|^p w ≤ C Σ_j|p_n(x_j)|^pΔ_n(x_j)w_n(x_j) for all p_n∈Π_n whenever x_j=cos ξ_j, x_0=−1, x_S=1, with gaps ξ_{j+1}−ξ_j≤1/(Mn). For every M there is C_M with the converse inequality when gaps are ≥1/(Mn). Here Δ_n(x)=√(1−x²)/n+1/n² (p. 63) and (7.14) gives λ_n(1,p,x)∼√(1−x²)/n+1/n² for w≡1 (p. 66).
- Relation: translated in topics/mz-prior-art-20261101/translation.md §T4 (with CC weight comparison §T3). It yields λ_−(N,n)≥c>0 for n≤θ₀N with unspecified absolute θ₀=1/(πM) and c. **Verdict: IMPLIES PART of PD-T023/PD-T024** (positive lower constant for small fixed ratio, non-explicit). It does not give every θ<1, explicit constants, an upper constant <2 (PD-T022) or the endpoint order (PD-T017/018): RELATED for those. Lubinsky 1999, p. 578, likewise describes Mastroianni–Totik as degree≤εn results.

### LIT-052 — Lubinsky 1998 survey read

- Coverage: published chapter, Springer DOI 10.1007/978-94-015-9086-0_12 (pp. 213–240, 28 PDF pages, text layer). Keyword-screened throughout; §3 (pp. 229–232, converse quadrature sums) read in full; open problems (p. 238) read.
- Statements: the duality method (p. 229); Theorems 3.1–3.2 for Freud weights (p. 230); Theorem 3.3 (p. 231), Xu's converse quadrature-sum estimate at Gauss points of generalized Jacobi distributions, extending Nevai; König's method (pp. 231–233); open problem 3° (p. 238) notes gaps between necessary and sufficient conditions for converse estimates.
- Relation: no Lobatto/CC-weighted ℓ²→L² theorem or logarithmic rate is stated. **Verdict: RELATED, DIFFERENT SETTING**; pointers to Xu II and Nevai III. The scanned author PDF gap is superseded by the publisher text.

### LIT-050 — Lubinsky–Máté–Nevai 1987 read (2026-11-01, topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5. Access: PDF supplied by AC in Downloads\\padua\\papers (2026-11-01, NTNU access), staged to the session; text via pdftotext, or tesseract OCR for image-only scans (Xu I/II). Read in the session only; nothing stored in Git. Rules `9739a0c`.

- Coverage: pp. 531–538 read (introduction, Definition 3, Theorems 4–5, Corollary 6, Definition 7, Theorem 8, Corollary 9, start of §2). The rest is proofs, not audited.
- Statement (Theorem 5, p. 534): for w∈GJ, 0<p<∞, a fixed positive integer l, convex nondecreasing ψ≥0, and arbitrary points −1≤y_m<…<y_1≤1 with θ_j=arccos y_j and δ=min(θ_{j+1}−θ_j)>0: for all P of degree ≤ln, Σ_jλ_n(w,y_j)ψ(|P(y_j)|^p)≤C_3{1+(nδ)^{−1}}∫ψ(C_2|P|^p)w (1.20); a companion (1.19) has weights w_n-type. Constants are independent of m, {y_j}, n and P. Corollary 6 (p. 535) is the Gauss-node case. This solves Askey's problem (1.11) on **forward** quadrature sums.
- Relation: at CC nodes (δ=π/N, w≡1, p=2, ψ(t)=t, λ_N(1,x_j)≍Δ_N(x_j)≍w_j by translation.md T3) it gives λ_+(N,n)≤C for all n≤lN with an absolute, unspecified C. This is uniform boundedness of the upper Gram constant, which is not itself one of our claims. It does not give the threshold 2 (PD-T014), 1+ρ (PD-T022) or 2−4/N+4/N². It is consistent with PD-T016 (λ_+>2 at full degree). **Verdict: RELATED** (implies only a weaker, unregistered boundedness statement); for PD-T017/018/023: RELATED (forward direction only).
