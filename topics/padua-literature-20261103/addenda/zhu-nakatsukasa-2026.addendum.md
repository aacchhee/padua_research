# zhu-nakatsukasa-2026 — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/zhu-nakatsukasa-2026.md`. W. Zhu, Y. Nakatsukasa, Convergence and near-optimal sampling for multivariate function approximations in irregular domains via Vandermonde with Arnoldi, IMA J. Numer. Anal. 46(4) (2026) 2072–2106, [doi:10.1093/imanum/draf055](https://doi.org/10.1093/imanum/draf055); free version [arXiv:2301.12241](https://arxiv.org/abs/2301.12241).

- Access and reading date: 2026-11-03.
- Version read: arXiv v2 (PDF dated 20 May 2025; footer `arXiv:2301.12241v2 [math.NA] 19 May 2025`). The IMA version of record was NOT read (OUP pages not attempted; list for AC if the published wording matters).
- Reading coverage: exact PDF pages 1–8 (abstract, §1, §1.1, §2, §2.1, Algorithms 1–2, §3 with Algorithms 3–4), 10–11 (end of §3.1, start of §4), 13 (Definition 4.1 and the Theorem 4.2 heading only), 14 (Theorem 4.3 statement), 15 (Theorem 4.4 with proof, Remark 4.3, Example 4.5), 18–25 (§4.4, §5, Algorithm 5, Remark 5.1, Theorem 5.1, §5.2, §6), reference list (entries [7], [11], [19], [23], [24] located). Pages 9, 12, 16–17 (Markov-inequality lemmas, Theorems 4.1–4.2, 4.6–4.7, convergence-rate section) NOT read. Text extracted with pdf.js in the built-in browser.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: IMA version of record; pp. 9, 12, 16–17.

## Extracted published statements

### LIT?padua-literature-claude-48 — Multivariate V+A algorithm, its parent rule and its orthogonalisation (Algorithm 3)

- Statement in faithful paraphrase: The multivariate monomial basis does not correspond to a Krylov subspace and has no canonical ordering, so the algorithm fixes an ordering and creates each new column by multiplying one preceding column by one coordinate, then Gram–Schmidt against the previous columns (p. 7). The parent is chosen by the smallest k such that I[l+1] = I[k] + e_r; grevlex satisfies the needed span condition for total degree (p. 8). Algorithm 3 (credited to Hokanson) runs classical Gram–Schmidt twice against all l previous columns, with column norm √M; Algorithm 4 evaluates the basis at new points with the stored H. The online cost of the orthogonalisation step is O(MN²) (p. 21).
- Hypotheses and notation: sample points in R^d, total-degree or maximum-degree spaces; numerical experiments mainly d = 2, total degree (p. 7).
- Page / theorem / equation: §3 pp. 6–8, Algorithms 3–4 p. 8; cost p. 21.
- Reading evidence and limitations: read in full on those pages.
- Relation to campaign claims (no inherited proof status): with the grevlex example order, the smallest-k rule multiplies by the first coordinate only to create the pure power of the first coordinate and by the second coordinate for every other new monomial of each degree (reader's check from the rule as printed: e.g. (1,1) comes from (1,0)·y, (2,1) from (2,0)·y). This is a one-relation selection of the BJ/dev type (one coordinate formed, the other injecting one vector per degree), orthogonalised against all previous columns, i.e. the "CGS2 + dev" configuration of PD-N?bivariate-lanczos-claude-201 and PD-T146. The identification of variable roles with the repo's X/Y convention must be read from the repo's dev definition (not re-read here).

### LIT?padua-literature-claude-49 — Rounding content: loss of orthogonality by cancellation and the CGS2 bound (Remark 5.1(5))

- Statement in faithful paraphrase: In the VA+Weight algorithm the basis is built by Algorithm 3; numerically, the orthogonalisation is subject to a loss of orthogonality due to cancellation, so the computed basis is only ε_m-orthonormal (‖Q*Q − I‖_F ≤ ε_m); with CGS run twice, ε_m ∼ O(MN^{3/2})u, citing Higham Thm 19.4 and Giraud–Langou–Rozložník–van den Eshof (Thm 2). Theorem 5.1 (adapted from a cited source) then bounds the reduced Gram matrix of the weighted subsample in probability, with ε_m entering additively. The convergence theorems of §4 (e.g. Theorem 4.4) are stated for the exact discrete orthonormal basis.
- Hypotheses and notation: ε_m-orthonormality is an assumption fed into Theorem 5.1; no statement about the span of the computed columns, the computed H, or their distance to the exact polynomial space appears in the pages read.
- Page / theorem / equation: Remark 5.1 item 5, pp. 20–21; Theorem 5.1 p. 21 (sketch of proof p. 22); Theorem 4.4 p. 15.
- Reading evidence and limitations: read in full on those pages.
- Relation to campaign claims (no inherited proof status): resolves the conflict recorded in the existing record: the sentence reported for LIT-090 IS in arXiv v2, in Remark 5.1(5), p. 20 (not in a "Remark 3"; v2 has no Remark 3 and no appendix). The bound concerns ‖Q*Q − I‖, i.e. orthogonality, not span accuracy; it does not address PD-N?bivariate-lanczos-claude-201 / PD-T146 (span drift at near-machine orthogonality).

### LIT?padua-literature-claude-50 — Near-optimality theorem, sampling results, the "unaffected by ill-conditioning" sentence, and the stated open problem (LIT-361)

- Statement in faithful paraphrase: Theorem 4.4: on a convex body or finite union of convex bodies in R^d (d > 1), with M = O(N²) equispaced points (Remark 4.2 construction), the V+A least-squares approximant satisfies ‖f − L(f)‖_Ω ≤ (1 + (2/M)‖QQ*‖_∞)‖f − p*‖_Ω ≤ (1 + O(N))‖f − p*‖_Ω, p* the best total-degree approximation, Q the exact discrete orthonormal basis. Theorem 4.3: M log M uniform random points give ‖p‖_Ω ≤ 2‖p‖_X with high probability. §5: VA+Weight uses O(N log N) weighted subsamples (Theorem 5.1). §5.2 (p. 22) attributes the advantage over QR+Weight to the discrete orthogonal polynomials generated by V+A being unaffected by the ill-conditioning of the Vandermonde matrix, with a 1D figure (30th polynomial vs scaled Legendre on [−5, 10], Fig. 13) as evidence; the 2D evidence (Fig. 14) is approximation error. Stated open problem: finding the best/optimal distribution of sample points in a high-dimensional irregular domain is an open question in the literature (pp. 2, 23); VA+Weight is offered as a practical tool, with selected points clustering near boundaries and corners, compared to Padua points on tensor domains (pp. 21, 23). Future work (p. 25): hyperbolic-cross spaces in the sup norm, scalable high-dimensional algorithms, convergence of VA+Lawson, vector/matrix-valued rational V+A.
- Hypotheses and notation: exact arithmetic in §4 theorems; domains satisfying a Markov condition (Remark 4.7, not read).
- Page / theorem / equation: Theorem 4.3 p. 14; Theorem 4.4 p. 15; §5.2 p. 22 (Figs. 12–13), p. 23; open problem pp. 2, 23; future work pp. 24–25.
- Reading evidence and limitations: read; Theorem 4.2 and the Markov-condition remark not read.
- Relation to campaign claims (no inherited proof status): no statement about the computed span or the computed recurrence coefficients in 2D. The "unaffected" sentence is the closest contrary-sounding claim to the span-drift findings and rests on 1D evidence (as the existing record already says; locator now Fig. 13, p. 22–23 of v2).

## Corrections and upgrades (old → new)

- LIT-090: UNVERIFIED (reported) → verified against arXiv v2: two-pass CGS (Algorithm 3, p. 8), O(MN²) cost (p. 21), and the loss-of-orthogonality-by-cancellation sentence in Remark 5.1(5), p. 20. The record's 2026-11-01 annotation "sentence not found in v2" is withdrawn; the L1 reviewer's locator "Remark 3" is wrong for v2.
- LIT-283: digest → verified, §3 p. 7 (v2).
- LIT-284: locator corrections for v2: "Remark 3 (§5.1)" → Remark 5.1(5), pp. 20–21; "Thm 6 ('stable with high probability')" → the phrase is in §1 p. 2 and the probabilistic statement is Theorem 5.1, p. 21; "§2.3.1, Fig. 2 and Fig. 10" → the 1D basis-versus-Legendre comparison is Fig. 13 (p. 23) cited in §5.2 (p. 22); Fig. 10 (p. 18) shows 1D/2D convergence rates. "Appendix B (Algorithms 4–5) not seen": in v2 there is no appendix; Algorithm 4 (evaluation) is on p. 8 and Algorithm 5 (VA+Weight) on p. 20. The gap is restated as "IMA version of record not read". "[15, Thm 2]" → in v2 the citation is [19] (Giraud et al.).
- LIT-361: "UNVERIFIED beyond abstract" → verified against arXiv v2: sample counts (abstract p. 1; Theorems 4.3–4.4 pp. 14–15; Theorem 5.1 p. 21), the loss-of-orthogonality sentence (Remark 5.1(5), p. 20) and the open problem on optimal sampling (pp. 2, 23). Locator "abstract and main theorem (as reported)" → "abstract; Thm 4.4 p. 15; Rem. 5.1(5) p. 20; pp. 2, 23 (arXiv v2)".
- LIT-089: abstract-checked → abstract confirmed in arXiv v2, p. 1.

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
