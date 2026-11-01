# mz-mean-convergence-screen — audit-01 M2 targeted primary-source screen

- Access/read date: 2026-10-31. Literature developer: Codex, `gpt-6.1-sol`, high (explicit orchestrator assignment).
- Rules read at `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`. Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, `literature/INDEX.md`, the complete `state/IDEAS.md`, and audit-01 M2. This is an attribution/coverage response, with no new candidate, mathematical proof status or novelty claim.
- Coverage: selected primary text where specified; bibliographic discovery otherwise. Queries and failures are appended to [M0](../../topics/mz-constants/literature-search.md). No third-party PDF or fulltext extract is stored in the public tree.
- The literature worker used provisional pointers. The MZ allocation owner subsequently assigned LIT-061–065 through the reconciled batch ledger, preserving the existing 60 source IDs; scope/reading coverage is unchanged.

## Comparison being screened

The campaign uses `x_k=cos(kπ/N)`, `0≤k≤N`, positive Clenshaw–Curtis weights `w_k^CC` for Lebesgue measure, and `Q_N(p²)=Σw_k^CC|p(x_k)|²`. PD-T017 bounds the full interpolation map from this nodal weighted `l²` norm to `L²(dx)` by `O(1+log N)`. PD-T018 supplies a matching growth witness already in `Π_(N−1)`. An equivalent prior statement must match the nodal norm and continuous measure, the Lobatto endpoints, degree range, and quantitative borderline logarithm. Mean convergence of each continuous input, or a uniform `C[-1,1]→L²` bound, alone does not identify this `l²→L²` norm. A result for Gauss zeros or another Jacobi measure needs a weight/node translation; no such translation is asserted from an abstract.

## Extracted statements and named pending references

### LIT-061 — Erdős–Feldheim 1936

- Citation: P. Erdős and E. Feldheim, *Sur le mode de convergence pour l'interpolation de Lagrange*, C. R. Acad. Sci. Paris **203** (1936), 913–915. [Original scan at Rényi](https://www.renyi.hu/~p_erdos/1936-10.pdf). No DOI verified.
- Coverage: scan title and pp. 913–914; p. 914 also visually inspected. Equation (1) states convergence in every positive even power for Chebyshev abscissae with measure `dx/√(1−x²)`. Its notation refers to a preceding note (203 (1936), p. 650), whose precise node convention and function hypotheses were not reread here.
- Relation/limit: primary statement found; it concerns mean convergence in the Chebyshev measure, rather than a quantitative nodal CC-weighted `l²→L²(dx)` norm. The exact node convention and any norm-growth implication remain pending-reference. This is historical proximity, not an exclusion of overlap.

### LIT-062 — Askey 1972 and its 1969 report

- Citation: R. Askey, *Mean convergence of orthogonal series and Lagrange interpolation*, Acta Math. Acad. Sci. Hungar. **23** (1972), 71–85, [DOI](https://doi.org/10.1007/BF01889904). [Bibliography](https://celebratio.org/Askey_RA/article/963/), entry 49; [1969 TW 113 report](https://ir.cwi.nl/pub/7742/7742D.pdf).
- Coverage: bibliography/abstract and report introduction, PDF pp. 3–6, Gaussian quadrature step on PDF p. 7, selected theorem/discussion PDF pp. 9–11. The bibliography identifies the journal version as corrected; the journal body was inaccessible and was not compared.
- Statement found in the report: interpolation is at zeros of orthogonal polynomials; Conjecture 1 explicitly distinguishes the Jacobi weight defining nodes from the weight of the mean. Theorem 1 treats a same-weight mean-convergence range. These are separate from a uniform estimate on arbitrary nodal data.
- Relation/limit: Gauss zeros and Gaussian Christoffel numbers in the inspected argument differ from CC Lobatto nodes/weights. The mixed-weight conjecture must not be cited as a theorem. No matching borderline CC logarithmic norm was extracted; journal corrections and endpoint implications remain pending-reference.

### LIT-063 — Nevai 1984, with 1990 addendum pending

- Citation: P. Nevai, *Mean convergence of Lagrange interpolation. III*, Trans. Amer. Math. Soc. **282** (1984), 669–698, [DOI](https://doi.org/10.1090/S0002-9947-1984-0732113-4). Citation verified in the [author bibliography](https://people.math.osu.edu/nevai.1/MYMATH/paul_nevai_publ.pdf), item 58, and [AMS reference list](https://doi.org/10.1090/S0025-5718-97-00808-9).
- Coverage: primary bibliographic metadata only. AMS article page/PDF returned 403 or connector errors; a CiteSeer mirror also returned 403. A third-party search summary repeats the audit's description of necessary/sufficient weighted mean-convergence conditions for generalized Jacobi zeros; it is discovery evidence, **not a primary theorem inspected here**.
- Named gap: extract exact generalized-Jacobi hypotheses, quasi-Lagrange/added-endpoint cases, critical parameter equalities, and any finite-degree norm growth. In particular, determine whether the CC `l²` weights and `u=1`, `p=2` borderline are covered.
- Also pending: Nevai, *Hilbert transforms and Lagrange interpolation. Addendum to: “Mean convergence of Lagrange interpolation. III”*, J. Approx. Theory **60** (1990), 360–363, [DOI](https://doi.org/10.1016/0021-9045(90)90065-X), identified in that AMS reference list; body unread. Neither the 1984 criterion nor its corrected scope is treated as verified.

### LIT-064 — Lubinsky converse MZ paper 147

- Citation: D. S. Lubinsky, *On Converse Marcinkiewicz–Zygmund Inequalities in Lp, p>1*, Constr. Approx. **15** (1999), 577–610, [DOI](https://doi.org/10.1007/s003659900123); [author preprint, dated 1998-11-23](https://lubinsky.math.gatech.edu/Research%20papers/marzyg98Paper147.pdf), linked as paper 147 in the [author bibliography](https://lubinsky.math.gatech.edu/SelectedPapers.html).
- Coverage: publisher abstract; preprint pp. 1–7 and bibliography selected, especially Theorems 1.1/1.2, Corollary 1.5 and Example 1.6. PDF page index 3 (printed p. 4), Theorem 1.2, visually inspected because extracted formulas are corrupted. No complete proof audit or final-version comparison.
- Statement found: converse `L^p` polynomial-to-nodal inequalities on the full `Π_(n−1)` interpolation space, with general ordered nodes (endpoints allowed), separation/local conditions, and an auxiliary `A_p` weight. The conclusion's nodal coefficients involve local cardinal integrals and nodal-polynomial derivatives.
- Relation/limit: this is a theorem-level match in *form*, not a verified match to CC coefficients or a quantitative `log N` bound. No explicitly named Lobatto specialization was found in the selected portions (text search also found no “Lobatto”). Endpoint allowance does not verify the critical CC hypotheses. The CC specialization, constants and borderline behavior remain pending-reference.

### LIT-065 — Smith's explicit Lobatto comparison

- Citation: W. E. Smith, *Erdös–Turán mean convergence theorem for Lagrange interpolation at Lobatto points*, Bull. Austral. Math. Soc. **34** (1986), 375–381, [DOI](https://doi.org/10.1017/S000497270001025X); [primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S000497270001025X).
- Coverage: abstract, introduction p. 376, Theorem 1 p. 377 and Corollary 1 p. 379, extracted text; remaining proof not audited. Screenshot retry for p. 379 timed out.
- Statement found: continuous-function mean-square convergence at zeros of `(1−x²)q_n`, where `q_n` is orthogonal for `ρ`, with continuous weight `w=ρ/(1−x²)` assumed integrable. The introduction identifies the CC case `ρ=√(1−x²)`; its resulting `w=1/√(1−x²)` differs from Lebesgue measure. The proof controls `C→L²(w)` boundedness, rather than the campaign's nodal `l²` norm.
- Relation/limit: an actual Lobatto theorem is found, but its stated norm/weight does not identify the target endpoint logarithmic norm. The paper points to stronger Jacobi results including Nevai III; those remain unresolved.

### Mastroianni–Russo follow-up pointers (bibliography only)

- Primary discovery: [Mastroianni author bibliography](https://service.unibas.it/utenti/mastroianni/listOfPublications.html), items 107 and 114.
- G. Mastroianni and M. G. Russo, *Lagrange Interpolation in Weighted Besov Spaces*, Constr. Approx. **15** (1999), 257–289.
- G. Mastroianni and M. G. Russo, *Weighted Marcinkiewicz inequalities and boundedness of the Lagrange operator*, in *Mathematical analysis and applications*, Hadronic Press, Palm Harbor, FL (2000), 149–182.
- Coverage: author bibliographic metadata only; no DOI verified and neither body inspected. These are named follow-up gaps, not extracted mathematical statements. Nodes, weights, precise boundedness domain, parameter inequalities and borderline growth all require reading before any overlap/exclusion claim.

### Xu generalized-Jacobi follow-up pointers (bibliography only)

- Primary discovery: [Y. Xu author bibliography](https://pages.uoregon.edu/yuan/pub.html), 1993/1994 entries; also Lubinsky paper 147 references 25–26.
- Y. Xu, *Mean convergence of generalized Jacobi series and interpolating polynomials, I*, J. Approx. Theory **72** (1993), 237–251; DOI [10.1006/jath.1993.1019](https://doi.org/10.1006/jath.1993.1019), additionally indexed in the [AMS reference list](https://doi.org/10.1090/S0025-5718-97-00808-9).
- Y. Xu, *Mean convergence of generalized Jacobi series and interpolating polynomials, II*, J. Approx. Theory **76** (1994), 77–92. DOI candidate `10.1006/jath.1994.1006` appeared in secondary discovery only and is **UNVERIFIED against a primary DOI record**.
- Coverage: primary bibliography only; DOI body opens failed. No theorem extracted. Gauss/Lobatto handling, nodal weights, critical equality and log-growth consequences remain pending-reference; titles alone do not establish applicability.

## Disposition and remaining work

**Audit M2 disposition: named unresolved pending-reference gap, after an actual targeted screen.** The family is now explicitly in M0's threat list. Source-level evidence above neither proves an equivalent prior theorem nor excludes one. PD-T017/PD-T018 may be presented as self-contained proofs; no novelty or exhaustive coverage claim follows. Full interpolation-space converse inequalities and weighted mean convergence are the principal historical overlap risk, including for the endpoint logarithmic order.

Next decisive reading: Nevai III plus its addendum; corrected Askey journal text; the Lobatto/critical-parameter specialization of Lubinsky 147; then Mastroianni–Russo and Xu. For each, calculate the actual nodal coefficients at `cos(kπ/N)`, including `k=0,N`, compare them uniformly with CC weights, and check the critical logarithmic norm and the `Π_(N−1)` constraint for a growth witness. Do not infer a critical rate merely from failure of uniform boundedness.

## History

2026-10-31: added for audit-01 M2; five provisional statement/pointer groups plus unnumbered follow-up bibliography, source-specific coverage and unsuccessful access recorded. Orchestrator owns final allocations, shared registries, manuscript integration and Git.

## 2026-11-01 fulltext reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5 (orchestrator). Access: publisher PDF via AC's NTNU institutional access in AC's built-in browser, text extracted in-page with pdf.js and read in the session only; no PDF or fulltext extract stored anywhere in the repository. Rules `9739a0c`.

### LIT-062 — Askey 1972 journal version read

- Coverage: complete journal article pp. 71–85. Pp. 71–78 read in full; pp. 79–85 keyword-screened (theorem/Lobatto/endpoint/quadrature/log/Christoffel/Chebyshev/conjecture).
- Statements: interpolation at the zeros x_{k,n} of p_n for dα (p. 71). Theorem 1 (p. 75): for α=β≥−1/2, or α+β=0 with 0<α<1/2, and continuous f, ∫|L_n f−f|^p(1−x)^α(1+x)^β dx→0 for 0<p<4(α+1)/(2α+1). The proof uses Gaussian quadrature and Christoffel numbers (p. 74), and pp. 76–77 show sharpness via a Nikolskii-type inequality. Conjecture 1 (pp. 72–73) remains a conjecture in the journal version. Theorems 2–3 (in the keyword-screened pp. 79–85; exact pages not recorded) concern mean convergence of orthogonal series (Pollard/Muckenhoupt). The "added in proof" note (p. 84) points to Askey, Summability of Jacobi series.
- Relation: Gauss nodes (no endpoints), uniform-norm input, L^p convergence. **Verdict for PD-T017/PD-T018: RELATED, DIFFERENT SETTING** (no Lobatto nodes, no nodal ℓ² norm, no rate). The journal-version gap is closed.

### LIT-064 — Lubinsky 1999 published version read

- Coverage: published Constr. Approx. 15 (1999) 577–610 (34 pp.). Pp. 577–584 read in full, covering Theorems 1.1–1.3, Corollaries 1.4–1.5, Example 1.6, Theorem 1.7 and Definition 1.8. Pp. 585–610 keyword-screened (log/Lobatto/Jacobi/sharp/borderline/endpoint/Chebyshev/Remark); no Lobatto, Jacobi-borderline or logarithmic interpolation-norm statement found.
- Statement (Theorem 1.7, p. 583): for b∈[1/2,1], c∈[0,1/2], −1/p<σ<1−1/p and ω(t)=(|1−|t/b||+c)^σ, under spacing condition (1.7), (1.31) and |π_nν|≤ω, one has for P∈Π_{n−1}: ∫|Pν|^p ≤ C Σ_j|P(t_j)|^p{∫_{t_{j−K}}^{t_{j+K+1}}|ℓ_jν|^p + δ_jω(t_j)^p/[δ_j|π_n′(t_j)|]^p}. C depends on L, α, σ, τ, p only. Endpoints t_1=−1, t_n=1 are allowed by (1.1). Remark (b), p. 579, verifies (1.7) for Chebyshev-type points cos θ_j with θ_j−θ_{j+1}≍1/n.
- Relation: theorem-level match in **form** for the full interpolation space, but at CC/Lobatto nodes with p=2, ν≡1 the natural exponent is σ=1/2=1−1/p, the excluded endpoint of (1.29). Admissible σ<1/2 gives nodal weights exceeding CC weights by up to ≍N^{2−4σ} near ±1, with untracked C(σ). See topics/mz-prior-art-20261101/translation.md §T5, which is our analysis and not a source claim. **Verdict for PD-T017: RELATED, DIFFERENT SETTING (borderline excluded); for PD-T018: RELATED, DIFFERENT SETTING (only an upper-type inequality).**

### LIT-065 — Smith 1986 complete

- Coverage: complete article pp. 375–381 (Cambridge PDF, text layer), including p. 379.
- Statements: Theorem 1 (p. 377): if w=ρ/(1−x²) is integrable and the nodes are the zeros of Q_n (orthogonal for ρ) plus ±1, then ∫w(L_{n+1}f−f)²→0 for f∈C[−1,1]. The proof bounds the C→L²(w) operator norm uniformly (pp. 377–378) using the Lobatto rule of precision 2n+1 and an Aitken splitting. Corollary 1 (p. 379): Jacobi (α,β>0) zeros plus endpoints, with weight (1−x)^{α−1}(1+x)^{β−1}. The CC case α=β=1/2 gives the Chebyshev weight (1−x²)^{−1/2}. Corollary 2 (pp. 379–380) is a product-integration consequence.
- Relation: uniform-norm data (‖f‖_∞) and Chebyshev weight. Uniform C→L²(dx) boundedness at CC nodes follows, since dx≤(1−x²)^{−1/2}dx, and is consistent with an unbounded ℓ²(w)→L²(dx) norm (nodal ℓ²(w) is weaker than sup on nodes). **Verdict for PD-T017/PD-T018: RELATED, DIFFERENT SETTING.** Gap closed.

### Secondary pointer from the Lubinsky 1998 survey (LIT-052), p. 231

Survey Theorem 3.3, attributed to Y. Xu [J. Approx. Theory 76 (1994), p. 82] and described as extending earlier results of Nevai: a converse quadrature-sum inequality for generalized Jacobi distributions u, v and generalized Jacobi weight w, at the **Gauss** points and weights for u, under four integrability conditions. Nodes are Gauss, not Lobatto. Whether a Lobatto/CC version with the borderline exponent appears in Xu II or Nevai III remains to be read (both on AC's missing list). No theorem is imported from the survey's paraphrase.
