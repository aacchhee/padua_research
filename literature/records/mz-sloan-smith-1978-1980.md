# mz-sloan-smith-1978-1980 — CC product integration

- Sources: I. H. Sloan, W. E. Smith, *Product-integration with the Clenshaw–Curtis and related points: Convergence properties*, Numer. Math. 30 (1978), 415–428, <https://doi.org/10.1007/BF01398509>; *Product integration with the Clenshaw–Curtis points: Implementation and error estimates*, Numer. Math. 34 (1980), 387–401, <https://doi.org/10.1007/BF01403676>.
- Access/read: 2026-10-31, publisher metadata and complete summaries at the linked article pages. Both fulltexts are subscription-only in the inspected interface: **FULLTEXT UNVERIFIED**.
- Reader: Codex, gpt-6.1-sol, high (explicit orchestrator assignment).

## Extracted source reports

### LIT-047 — 1978 convergence/weight result (summary coverage)

The publisher summary describes interpolatory product integration of kf at cos(i pi/n), i=0,...,n. For k in Lp with p>1 it reports convergence for continuous, even Riemann-integrable f, convergence of the sum of absolute weights to integral |k|, and limiting individual-weight expressions under additional assumptions.

- Hypotheses/locator: publisher Summary; k absolutely integrable in the setup, stronger Lp hypothesis for stated principal convergence result.
- Gap: exact additional hypotheses and theorem numbers, proof estimates for interpolation norms and their possible uniformity in n.
- Relation: close node/weight ancestor, but the summary's fixed-integrand convergence is not the campaign's supremum over n-dependent squared polynomials. Fulltext must be screened before excluding equivalent M1–M3 bounds.

### LIT-048 — 1980 implementation/error result (summary coverage)

The publisher summary describes the same interpolatory product rule and two error estimates; k=1 yields CC. It reports tests for singular and oscillatory k and smooth f.

- Locator: publisher Summary, no theorem number read.
- Gap: exact norm estimates, degree dependence and hypotheses in full text.
- Relation: potential source of explicit CC error bounds. No inference here converts a smooth fixed-f estimate into a sharp uniform MZ estimate.

## History

2026-10-31: publisher-summary screen; fulltext exclusion remains pending.

## 2026-11-01 fulltext reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5 (orchestrator). Access: publisher PDF via AC's NTNU institutional access in AC's built-in browser, text extracted in-page with pdf.js and read in the session only; no PDF or fulltext extract stored anywhere in the repository. Rules `9739a0c`.

### LIT-047 — fulltext coverage upgrade

- Coverage: complete article, pp. 415–428. Pp. 415–421 read in full; pp. 422–428 keyword-screened (Theorem/Lemma/norm/log/interpolation/Lobatto/Corollary).
- Statements: Theorem 1 (p. 419): if ∫|k|^p<∞ for some p>1, then lim_n Σ_i|w_ni|=∫|k| for the interpolatory product rule at cos(iπ/n). Theorem 2 (§3, after the proof of Theorem 1; exact page not recorded in the keyword screen): pointwise limit n·w_ni → πk(x)(1−x²)^{1/2} under local regularity. Theorem 3 (§4; exact page not recorded): convergence for every continuous f, with error ≤(‖I_n‖+‖I‖)E_n(f) in the C[−1,1] functional norm. Tools: modified Fourier partial sums and the trigonometric Marcinkiewicz inequality in L¹ (Zygmund, vol. 2, pp. 28–30) (p. 421).
- Relation: the only norm controlled is the C[−1,1] dual (Σ|w_ni|) of a linear functional. There is no quadratic form, no Gram/mass matrix, no nodal ℓ²→L² interpolation bound and no logarithmic rate. For k≡1 the weights are the CC weights (p. 419), so this is the node/weight ancestor only. **Verdict for PD-T014/017/018/022/024/025: RELATED, DIFFERENT SETTING.** The FULLTEXT UNVERIFIED gap is closed for this article.

### LIT-048 — fulltext coverage upgrade

- Coverage: pp. 387–388 read; remainder not needed after the summary and the 1978 reading. It concerns implementation and two computable error estimates for smooth f, with numerical tests. Remaining pages 389–401 are **not read**; a keyword screen is still pending. No theorem about ℓ²/L² norms is suggested by the read portion.
- Relation: RELATED, DIFFERENT SETTING (practical error estimation).

### Further companion (not yet read)

Smith 1986 cites I. H. Sloan, W. E. Smith, "Properties of interpolatory product integration rules", SIAM J. Numer. Anal. 19 (1982) 427–442, as its source for product-integration convergence. SIAM fulltext is not reachable from the automated browser (bot check); it is on AC's missing-fulltext list.
